#!/usr/bin/env python3.11
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    tomllib = None

HERE = Path(__file__).resolve().parent
RELAY = HERE.parent
REPO = RELAY.parent
sys.path.insert(0, str(HERE))
import backends, git_ops, packet_builder, validation

CANDIDATE_STATUSES = {"ready", "executing", "validated", "awaiting_human", "needs_correction"}


def now(): return dt.datetime.now(dt.timezone.utc).isoformat()
def load_json(path): return json.loads(Path(path).read_text())
def write_json(path, data):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(data, indent=2) + "\n")
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def config():
    path = RELAY / ("config.toml" if (RELAY / "config.toml").exists() else "config.example.toml")
    if tomllib:
        with path.open("rb") as stream:
            return tomllib.load(stream)
    raise RuntimeError("Python 3.11 or newer is required")


def local_state_path(): return REPO / ".agent-relay-local" / "CURRENT.json"


def current():
    path = local_state_path()
    return load_json(path if path.exists() else RELAY / "CURRENT.json")


def save_current(state):
    state["updated_at"] = now()
    write_json(local_state_path(), state)


def candidate(state=None):
    state = state or current()
    value = state.get("candidate")
    if not value:
        raise RuntimeError("no active candidate; run candidate-start first")
    if value.get("status") not in CANDIDATE_STATUSES:
        raise RuntimeError(f"invalid candidate status: {value.get('status')}")
    return value


def candidate_worktree(value): return REPO / value["worktree"]
def run_root(): return REPO / config()["run_root"]


def next_run_id():
    numbers = []
    for path in run_root().rglob("run-*") if run_root().exists() else []:
        match = re.fullmatch(r"run-(\d+)", path.name)
        if match: numbers.append(int(match.group(1)))
    return f"run-{max(numbers, default=0) + 1:04d}"


def run_dir(state=None):
    run_id = candidate(state).get("latest_run_id")
    if not run_id: raise RuntimeError("candidate has no run yet")
    return run_root() / run_id


def canonical_tip(worktree):
    # The checked-out Git state is authoritative. Executor JSON is deliberately ignored.
    return git_ops.run(["git", "rev-parse", "HEAD"], worktree).stdout.strip()


def require_candidate_status(value, *allowed):
    if value["status"] not in allowed:
        raise RuntimeError(f"command requires candidate status {', '.join(allowed)}; current status is {value['status']}")


def require_accepted_branch(state):
    branch = git_ops.branch(REPO)
    if branch != state["branch"]:
        raise RuntimeError(f"accepted worktree must be on configured branch {state['branch']}; current branch is {branch}")


def candidate_start(args):
    state = current()
    if state.get("candidate") is not None:
        raise RuntimeError("a candidate already exists")
    require_accepted_branch(state)
    git_ops.ensure_clean(REPO)
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", args.name):
        raise RuntimeError("candidate name must use lowercase letters, digits, and hyphens")
    branch = f"relay/candidate-{args.name}"
    relative = Path(config()["worktree_root"]) / f"candidate-{args.name}"
    worktree = REPO / relative
    if git_ops.run(["git", "show-ref", "--verify", "--quiet", f"refs/heads/{branch}"], REPO, check=False).returncode == 0:
        raise RuntimeError(f"candidate branch already exists: {branch}")
    if worktree.exists(): raise RuntimeError(f"candidate worktree already exists: {worktree}")
    initial_base = canonical_tip(REPO)
    git_ops.create_worktree(REPO, worktree, branch, initial_base)
    try:
        for supplied in args.cherry_pick:
            commit = git_ops.run(["git", "rev-parse", f"{supplied}^{{commit}}"], REPO).stdout.strip()
            git_ops.run(["git", "cherry-pick", commit], worktree)
        tip = canonical_tip(worktree)
    except Exception:
        git_ops.run(["git", "cherry-pick", "--abort"], worktree, check=False)
        git_ops.remove_worktree(REPO, worktree)
        git_ops.run(["git", "branch", "-D", branch], REPO, check=False)
        raise
    state["candidate"] = {
        "name": args.name, "branch": branch, "worktree": str(relative),
        "initial_base": initial_base, "current_tip": tip, "status": "ready",
        "latest_run_id": None,
    }
    save_current(state)
    print(f"candidate {args.name} started at {tip} in {relative}")


def candidate_run(args):
    state = current(); value = candidate(state)
    require_candidate_status(value, "ready", "needs_correction")
    worktree = candidate_worktree(value)
    git_ops.ensure_clean(worktree)
    if git_ops.branch(worktree) != value["branch"]: raise RuntimeError("candidate worktree is on the wrong branch")
    run_id = next_run_id(); directory = run_root() / run_id; directory.mkdir(parents=True)
    packet = packet_builder.executor_packet(worktree / ".agent-relay", run_id)
    metrics = packet_builder.packet_metrics(packet, [worktree / ".agent-relay" / p for p in ("prompts/executor.md", "RUNBOOK.md", "STATE.md", "HANDOFF.md")])
    cfg = config()
    packet_builder.enforce_packet_limit(metrics, warning_tokens=cfg.get("packet_warning_tokens", 100000), hard_tokens=cfg.get("packet_hard_limit_tokens", 150000), allow_large=args.allow_large_packet, label="executor")
    (directory / "EXECUTOR_PACKET.md").write_text(packet)
    meta = {"run_id": run_id, "started_at": now(), "accepted_head": canonical_tip(REPO), "candidate_start": canonical_tip(worktree), "worktree": str(worktree), "branch": value["branch"], "executor_packet_metrics": metrics}
    output = directory / "RESULT.json"
    common = git_ops.resolve_git_common_dir(REPO)
    git_ops.preflight_commit_permissions(worktree, common)
    command = backends.codex_command(cwd=worktree, schema=RELAY / "schemas/executor-result.schema.json", output=output, sandbox=cfg["executor_sandbox"], model=cfg["executor_model"], add_dirs=[common])
    meta.update(executor_command=command, git_common_dir=str(common)); write_json(directory / "META.json", meta)
    value.update(status="executing", latest_run_id=run_id); save_current(state)
    error = None
    try: backends.run_codex(packet, command, directory / "executor-events.jsonl")
    except Exception as exc: error = exc
    changed = git_ops.changed_paths(worktree)
    tip = canonical_tip(worktree)
    if changed:
        value.update(status="needs_correction", current_tip=tip); save_current(state)
        raise RuntimeError("executor left uncommitted changes in the preserved candidate worktree")
    if error:
        value.update(status="needs_correction", current_tip=tip); save_current(state); raise error
    if tip == meta["candidate_start"]:
        value.update(status="needs_correction", current_tip=tip); save_current(state)
        raise RuntimeError("executor did not create a commit")
    meta["executor_commit"] = tip  # Always rev-parse HEAD; never RESULT.json[commits].
    write_json(directory / "META.json", meta)
    result = load_json(output) if output.exists() else {}
    value.update(status="ready", current_tip=tip)
    state["last_run_id"] = run_id; state["last_outcome"] = result.get("outcome")
    save_current(state); print(tip)


def validate_candidate(_):
    state = current(); value = candidate(state)
    require_candidate_status(value, "ready", "validated", "awaiting_human")
    directory = run_dir(state)
    if value["status"] in {"validated", "awaiting_human"} and (directory / "VALIDATION.json").exists():
        print(load_json(directory / "VALIDATION.json")["status"]); return
    worktree = candidate_worktree(value); git_ops.ensure_clean(worktree)
    accepted = canonical_tip(REPO); tip = canonical_tip(worktree)
    data = validation.run_all(worktree, accepted, tip, directory, config())
    value.update(status="validated", current_tip=tip); save_current(state); print(data["status"])


def review_candidate(args):
    state = current(); value = candidate(state); require_candidate_status(value, "validated")
    directory = run_dir(state); validations = load_json(directory / "VALIDATION.json")
    worktree = candidate_worktree(value); accepted = canonical_tip(REPO); tip = canonical_tip(worktree)
    result_path = directory / "RESULT.json"; result = load_json(result_path) if result_path.exists() else {"outcome":"UNKNOWN"}
    stat = git_ops.run(["git", "diff", "--stat", f"{accepted}..{tip}"], worktree).stdout
    diff = git_ops.run(["git", "diff", f"{accepted}..{tip}"], worktree).stdout
    cfg = config(); packet = packet_builder.review_packet(worktree / ".agent-relay", result, accepted, tip, stat, diff, validations, cfg["review_diff_limit_bytes"])
    metrics = packet_builder.packet_metrics(packet, [worktree / ".agent-relay" / p for p in ("prompts/reviewer-codex.md", "RUNBOOK.md", "STATE.md", "HANDOFF.md")])
    packet_builder.enforce_packet_limit(metrics, warning_tokens=cfg.get("packet_warning_tokens",100000), hard_tokens=cfg.get("packet_hard_limit_tokens",150000), allow_large=args.allow_large_packet, label="review")
    (directory / "REVIEW_PACKET.md").write_text(packet)
    if cfg["review_backend"] == "codex":
        command = backends.codex_command(cwd=None, schema=RELAY / "schemas/review.schema.json", output=directory / "REVIEW.json", sandbox=cfg["reviewer_sandbox"], model=cfg["reviewer_model"])
        backends.run_codex(packet, command, directory / "reviewer-events.jsonl")
    else:
        backends.run_openai_review(packet, load_json(RELAY / "schemas/review.schema.json"), directory / "REVIEW.json", cfg["reviewer_model"], cfg["api_retry_count"])
    value["status"] = "awaiting_human"; save_current(state)


def install_correction_handoff(state, review_path):
    value = candidate(state); review = load_json(review_path); worktree = candidate_worktree(value)
    git_ops.ensure_clean(worktree)
    handoff = worktree / ".agent-relay" / "HANDOFF.md"
    handoff.write_text(review["next_handoff"].rstrip() + "\n")
    git_ops.run(["git", "add", "--", ".agent-relay/HANDOFF.md"], worktree)
    if git_ops.run(["git", "diff", "--cached", "--quiet"], worktree, check=False).returncode:
        git_ops.run(["git", "commit", "-m", "Install reviewer correction handoff"], worktree)
    value.update(status="needs_correction", current_tip=canonical_tip(worktree))
    save_current(state)
    return review["next_handoff"]


def candidate_correct(_):
    state = current(); value = candidate(state)
    source_run = getattr(_, "from_run", None)
    if source_run:
        require_candidate_status(value, "ready")
        review_path = run_root() / source_run / "REVIEW.json"
        if not review_path.exists(): raise RuntimeError(f"review not found: {review_path}")
    else:
        require_candidate_status(value, "awaiting_human")
        review_path = run_dir(state) / "REVIEW.json"
    text = install_correction_handoff(state, review_path)
    print(text)


def review_override(review, override, reason):
    if review.get("verdict") == "accept": return None
    if not override: raise RuntimeError(f"reviewer verdict is {review.get('verdict')}; use --override-review --reason TEXT")
    if not reason or not reason.strip(): raise RuntimeError("--override-review requires a non-empty --reason")
    return {"reason": reason.strip(), "recorded_at": now()}


def apply_state_patch(review):
    patch = review["state_patch"]
    additions = patch["banked_results_add"] + patch["closed_architectures_add"]
    state_text = (RELAY / "STATE.md").read_text() + "\n## Accepted iteration additions\n" + "\n".join(f"- {item}" for item in additions)
    state_text += f"\n\n## Current open gate\n\n{patch['open_gate']}\n\n## Formalization boundary\n\n{patch['formalization_boundary']}\n\n## Single best next strategic problem\n\n{patch['next_task']}\n"
    (RELAY / "STATE.md").write_text(state_text)
    (RELAY / "HANDOFF.md").write_text(review["next_handoff"].rstrip() + "\n")


def candidate_accept(args):
    state = current(); value = candidate(state); require_candidate_status(value, "awaiting_human")
    directory = run_dir(state); review = load_json(directory / "REVIEW.json"); validations = load_json(directory / "VALIDATION.json")
    if validations.get("status") != "pass": raise RuntimeError("cannot accept failed validations")
    override = review_override(review, args.override_review, args.reason)
    require_accepted_branch(state); git_ops.ensure_clean(REPO)
    worktree = candidate_worktree(value); git_ops.ensure_clean(worktree)
    # Fetch the branch tip from Git immediately before integration.
    accepted_head = git_ops.run(["git", "rev-parse", state["branch"]], REPO).stdout.strip()
    rebase = git_ops.run(["git", "rebase", state["branch"]], worktree, check=False)
    if rebase.returncode:
        print(f"Rebase conflict preserved in {worktree}.\nResolve files there, then run:\n  git -C {worktree} add <resolved-files>\n  git -C {worktree} rebase --continue\nOr abort with:\n  git -C {worktree} rebase --abort")
        raise RuntimeError("candidate rebase conflicted; accepted branch was not mutated")
    tip = canonical_tip(worktree); value["current_tip"] = tip; save_current(state)
    post = directory / "post-rebase"; post.mkdir(exist_ok=True)
    rerun = validation.run_all(worktree, accepted_head, tip, post, config())
    if rerun["status"] != "pass": raise RuntimeError("post-rebase validations failed; candidate preserved")
    git_ops.run(["git", "merge", "--ff-only", value["branch"]], REPO)
    apply_state_patch(review)
    state.update(accepted_commit=tip, iteration=state.get("iteration",0)+1, last_outcome=(load_json(directory/"RESULT.json").get("outcome") if (directory/"RESULT.json").exists() else None))
    state["candidate"] = None
    # Commit only durable accepted control state; live candidate state remains local.
    tracked = load_json(RELAY / "CURRENT.json"); tracked.update(accepted_commit=tip, iteration=state["iteration"], last_run_id=value["latest_run_id"], last_outcome=state["last_outcome"], candidate=None, updated_at=now())
    write_json(RELAY / "CURRENT.json", tracked)
    git_ops.run(["git", "add", "--", ".agent-relay/STATE.md", ".agent-relay/HANDOFF.md", ".agent-relay/CURRENT.json"], REPO)
    git_ops.run(["git", "commit", "-m", f"Accept relay candidate {value['name']}"], REPO)
    git_ops.remove_worktree(REPO, worktree); git_ops.run(["git", "branch", "-d", value["branch"]], REPO)
    save_current(state); git_ops.ensure_clean(REPO)
    if override: write_json(directory / "ACCEPT_OVERRIDE.json", override)
    print(tip)


def candidate_abandon(args):
    state = current(); value = candidate(state)
    if not args.yes:
        if not sys.stdin.isatty(): raise RuntimeError("candidate-abandon requires --yes or interactive confirmation")
        if input(f"Abandon candidate {value['name']}? [y/N] ").strip().lower() not in {"y","yes"}: raise RuntimeError("abandon cancelled")
    worktree = candidate_worktree(value); git_ops.ensure_clean(worktree)
    git_ops.remove_worktree(REPO, worktree); git_ops.run(["git", "branch", "-D", value["branch"]], REPO)
    state["candidate"] = None; save_current(state); print("candidate abandoned; run evidence preserved")


def archive_run(args):
    source = run_root() / args.run_id; target = run_root() / "archive" / args.run_id
    if not source.exists(): raise RuntimeError(f"run not found: {args.run_id}")
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists(): raise RuntimeError(f"archive already exists: {target}")
    shutil.move(str(source), str(target)); print(target)


def doctor(_):
    failures = []
    def check(label, ok, detail=""):
        print(f"{label}: {'PASS' if ok else 'FAIL'}{f' ({detail})' if detail else ''}")
        if not ok: failures.append(label)
    check("repository root", git_ops.root(REPO) == REPO)
    check("accepted worktree clean", not git_ops.porcelain(REPO))
    check("Python >= 3.11", sys.version_info >= (3,11))
    check("Git installed", shutil.which("git") is not None)
    check("Codex installed", shutil.which("codex") is not None)
    login = subprocess.run(["codex","login","status"],cwd=REPO,capture_output=True,text=True) if shutil.which("codex") else None
    check("Codex authenticated", bool(login and login.returncode == 0))
    check("lake available", Path(shutil.which("lake") or str(Path.home()/".elan/bin/lake")).is_file(), "required for Lean changes")
    for path in (RELAY/"schemas").glob("*.json"):
        try: json.loads(path.read_text()); ok=True
        except Exception: ok=False
        check(f"schema parses {path.name}", ok)
    check("transient directory untracked", not git_ops.run(["git","ls-files",".agent-relay-local"],REPO).stdout.strip())
    relay_text = "".join(path.read_text(errors="ignore") for path in RELAY.rglob("*") if path.is_file())
    check("no obvious committed API key", re.search(r"sk-(?:proj|live)-[A-Za-z0-9_-]{20,}",relay_text) is None)
    return 1 if failures else 0


def status(_):
    state = current(); value = state.get("candidate")
    if value:
        worktree = candidate_worktree(value)
        if worktree.exists(): value = {**value, "current_tip": canonical_tip(worktree)}
    print(json.dumps({**state, "candidate": value}, indent=2))


def deprecated(args): raise RuntimeError(f"{args.cmd} is deprecated; use the candidate-* lifecycle")


def main():
    parser=argparse.ArgumentParser(); sub=parser.add_subparsers(dest="cmd",required=True)
    for name, fn in (("doctor",doctor),("status",status),("candidate-run",candidate_run),("validate",validate_candidate),("review",review_candidate)):
        item=sub.add_parser(name)
        if name in {"candidate-run","review"}: item.add_argument("--allow-large-packet",action="store_true")
        item.set_defaults(fn=fn)
    item=sub.add_parser("candidate-correct"); item.add_argument("--from-run"); item.set_defaults(fn=candidate_correct)
    item=sub.add_parser("candidate-start"); item.add_argument("--name",required=True); item.add_argument("--cherry-pick",action="append",default=[]); item.set_defaults(fn=candidate_start)
    item=sub.add_parser("candidate-accept"); item.add_argument("--override-review",action="store_true"); item.add_argument("--reason"); item.set_defaults(fn=candidate_accept)
    item=sub.add_parser("candidate-abandon"); item.add_argument("--yes",action="store_true"); item.set_defaults(fn=candidate_abandon)
    item=sub.add_parser("archive-run"); item.add_argument("run_id"); item.set_defaults(fn=archive_run)
    for name in ("prepare","execute","accept","reject","cycle","run","carry-forward"):
        sub.add_parser(name).set_defaults(fn=deprecated)
    args=parser.parse_args()
    try: return args.fn(args) or 0
    except Exception as exc: print(f"ERROR: {exc}",file=sys.stderr); return 1


if __name__ == "__main__": raise SystemExit(main())
