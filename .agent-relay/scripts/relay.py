#!/usr/bin/env python3.11
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
from contextlib import contextmanager
from pathlib import Path
from types import SimpleNamespace

try:
    import tomllib
except ModuleNotFoundError:
    tomllib = None

HERE = Path(__file__).resolve().parent
RELAY = HERE.parent
REPO = RELAY.parent
sys.path.insert(0, str(HERE))
import backends, candidate_reporting, claim_ledger, git_ops, packet_builder, schema_validation, validation

CANDIDATE_STATUSES = {
    "ready", "executing", "execution_error", "executed",
    "validation_passed", "validation_failed", "validation_error",
    "reviewing", "review_error", "awaiting_human", "needs_correction",
    "recovery_required", "integrating_prepared", "control_committed",
}


def now(): return dt.datetime.now(dt.timezone.utc).isoformat()
def load_json(path): return json.loads(Path(path).read_text())
def write_json(path, data):
    write_text_atomic(Path(path), json.dumps(data, indent=2) + "\n")
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_text_atomic(path: Path, text: str):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            stream.write(text); stream.flush(); os.fsync(stream.fileno())
        os.replace(temporary, path)
        directory_fd = os.open(path.parent, os.O_RDONLY)
        try: os.fsync(directory_fd)
        finally: os.close(directory_fd)
    except Exception:
        try: os.close(fd)
        except OSError: pass
        Path(temporary).unlink(missing_ok=True)
        raise


@contextmanager
def repository_lock():
    import fcntl
    path = REPO / ".agent-relay-local" / "relay.lock"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a+") as stream:
        try: fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc: raise RuntimeError("another state-changing relay command is active") from exc
        stream.seek(0); stream.truncate(); stream.write(json.dumps({"pid": os.getpid(), "hostname": socket.gethostname(), "acquired_at": now()})); stream.flush()
        try: yield
        finally: fcntl.flock(stream.fileno(), fcntl.LOCK_UN)


def phase_record(name: str, *, candidate_head: str, packet_path: Path | None = None):
    return {
        "name": name, "pid": os.getpid(), "hostname": socket.gethostname(),
        "started_at": now(), "candidate_head": candidate_head,
        "packet_sha256": sha(packet_path) if packet_path and packet_path.exists() else None,
    }


def phase_process_alive(phase: dict | None):
    if not phase or phase.get("hostname") != socket.gethostname(): return False
    try: os.kill(int(phase["pid"]), 0); return True
    except (OSError, KeyError, TypeError, ValueError): return False


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


def report_snapshot(args=None):
    state=current(); cfg=config(); run_id=getattr(args,"run_id",None)
    return candidate_reporting.collect(REPO,state,cfg,git_ops,run_id=run_id)


def automatic_report():
    try:
        data,_=report_snapshot(); candidate_reporting.print_report(data)
    except Exception as exc:
        print(f"WARNING: candidate report unavailable: {exc}",file=sys.stderr)


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
    require_candidate_status(value, "ready", "needs_correction", "execution_error")
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
    value.update(status="executing", latest_run_id=run_id,
                 phase=phase_record("executor", candidate_head=meta["candidate_start"], packet_path=directory / "EXECUTOR_PACKET.md")); save_current(state)
    error = None
    try: backends.run_codex(packet, command, directory / "executor-events.jsonl")
    except Exception as exc: error = exc
    changed = git_ops.changed_paths(worktree)
    tip = canonical_tip(worktree)
    if changed:
        value.update(status="recovery_required", current_tip=tip); value.pop("phase", None); save_current(state)
        raise RuntimeError("executor left uncommitted changes in the preserved candidate worktree")
    if error:
        value.update(status="execution_error", current_tip=tip); value.pop("phase", None); save_current(state); raise error
    if tip == meta["candidate_start"]:
        value.update(status="needs_correction", current_tip=tip); value.pop("phase", None); save_current(state)
        raise RuntimeError("executor did not create a commit")
    meta["executor_commit"] = tip  # Always rev-parse HEAD; never RESULT.json[commits].
    write_json(directory / "META.json", meta)
    result = load_json(output) if output.exists() else {}
    value.update(status="executed", current_tip=tip); value.pop("phase", None)
    state["last_run_id"] = run_id; state["last_outcome"] = result.get("outcome")
    save_current(state); automatic_report()


def validate_candidate(_):
    state = current(); value = candidate(state)
    require_candidate_status(value, "executed", "validation_passed", "validation_failed", "validation_error", "awaiting_human")
    directory = run_dir(state)
    if value["status"] in {"validation_passed", "validation_failed", "validation_error", "awaiting_human"} and (directory / "VALIDATION.json").exists():
        automatic_report(); return
    worktree = candidate_worktree(value); git_ops.ensure_clean(worktree)
    accepted = canonical_tip(REPO); tip = canonical_tip(worktree)
    try:
        data = validation.run_all(worktree, accepted, tip, directory, config())
    except Exception as exc:
        data = {"status": "error", "changed_files": [], "commands": [], "commit": tip, "error": str(exc)}
        write_json(directory / "VALIDATION.json", data)
    outcome = {"pass": "validation_passed", "fail": "validation_failed", "error": "validation_error"}.get(data.get("status"))
    if outcome is None:
        raise RuntimeError(f"validator returned invalid status: {data.get('status')}")
    value.update(status=outcome, current_tip=tip); save_current(state); automatic_report()


def review_candidate(args):
    state = current(); value = candidate(state)
    allow_failed = bool(getattr(args, "failed_validation", False))
    require_candidate_status(value, *("validation_passed", "validation_failed", "validation_error") if allow_failed else ("validation_passed", "review_error"))
    directory = run_dir(state); validations = load_json(directory / "VALIDATION.json")
    if not allow_failed and validations.get("status") != "pass":
        raise RuntimeError("ordinary review requires passing validation")
    worktree = candidate_worktree(value); accepted = canonical_tip(REPO); tip = canonical_tip(worktree)
    result_path = directory / "RESULT.json"; result = load_json(result_path) if result_path.exists() else {"outcome":"UNKNOWN"}
    stat = git_ops.run(["git", "diff", "--stat", f"{accepted}..{tip}"], worktree).stdout
    diff = git_ops.run(["git", "diff", f"{accepted}..{tip}"], worktree).stdout
    cfg = config()
    _, included, omitted = packet_builder.bounded_diff(diff, cfg["review_diff_limit_bytes"])
    changed_files = git_ops.run(["git", "diff", "--name-only", f"{accepted}..{tip}"], worktree).stdout.splitlines()
    manifest = packet_builder.change_manifest(worktree, tip, changed_files, included)
    packet = packet_builder.review_packet(worktree / ".agent-relay", result, accepted, tip, stat, diff, validations, cfg["review_diff_limit_bytes"], manifest=manifest)
    metrics = packet_builder.packet_metrics(packet, [worktree / ".agent-relay" / p for p in ("prompts/reviewer-codex.md", "RUNBOOK.md", "STATE.md", "HANDOFF.md")])
    packet_builder.enforce_packet_limit(metrics, warning_tokens=cfg.get("packet_warning_tokens",100000), hard_tokens=cfg.get("packet_hard_limit_tokens",150000), allow_large=args.allow_large_packet, label="review")
    (directory / "REVIEW_PACKET.md").write_text(packet)
    marker=directory/"REVIEW_ACTIVE"; marker.write_text(str(os.getpid()))
    value["status"] = "reviewing"
    value["phase"] = phase_record("reviewer", candidate_head=tip, packet_path=directory / "REVIEW_PACKET.md")
    save_current(state)
    try:
        if cfg["review_backend"] == "codex":
            command = backends.codex_command(cwd=worktree, schema=RELAY / "schemas/review.schema.json", output=directory / "REVIEW.json", sandbox=cfg["reviewer_sandbox"], model=cfg["reviewer_model"])
            backends.run_codex(packet, command, directory / "reviewer-events.jsonl")
        else:
            backends.run_openai_review(packet, load_json(RELAY / "schemas/review.schema.json"), directory / "REVIEW.json", cfg["reviewer_model"], cfg["api_retry_count"])
    except Exception:
        value["status"] = "review_error"; value.pop("phase", None); save_current(state)
        raise
    finally: marker.unlink(missing_ok=True)
    review = load_json(directory / "REVIEW.json")
    visibility_reason = None
    if validations.get("status") != "pass": visibility_reason = f"mechanical validation status is {validations.get('status')}"
    elif omitted: visibility_reason = f"review diff omitted {len(omitted)} changed file(s): {', '.join(omitted)}"
    elif cfg["review_backend"] != "codex": visibility_reason = "review backend had no read-only candidate checkout"
    if visibility_reason:
        review.update(verdict="human_review", safe_for_automatic_acceptance=False,
                      requires_human_review_reason=visibility_reason)
        write_json(directory / "REVIEW.json", review)
    value["status"] = "awaiting_human"; value.pop("phase", None); save_current(state); automatic_report()


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
    automatic_report()


def recover_candidate(_):
    state = current(); value = candidate(state); status = value["status"]
    if status not in {"executing", "reviewing", "recovery_required", "integrating_prepared", "control_committed"}:
        raise RuntimeError(f"candidate status {status} has no recoverable active phase")
    phase = value.get("phase")
    if status in {"executing", "reviewing"} and phase_process_alive(phase):
        raise RuntimeError(f"{phase.get('name', 'relay phase')} process is still alive")
    worktree = candidate_worktree(value)
    if status == "executing":
        changed = git_ops.changed_paths(worktree); tip = canonical_tip(worktree)
        if changed:
            value.update(status="recovery_required", current_tip=tip)
        elif tip != (phase or {}).get("candidate_head") and (run_dir(state) / "RESULT.json").exists():
            value.update(status="executed", current_tip=tip)
        else:
            value.update(status="execution_error", current_tip=tip)
    elif status == "reviewing":
        value["status"] = "awaiting_human" if (run_dir(state) / "REVIEW.json").exists() else "review_error"
    elif status == "recovery_required":
        if git_ops.changed_paths(worktree):
            raise RuntimeError("candidate is dirty; run candidate-snapshot-dirty before recovery")
        value.update(status="needs_correction", current_tip=canonical_tip(worktree))
    else:
        return recover_integration(state)
    value.pop("phase", None); save_current(state); automatic_report()


def candidate_snapshot_dirty(_):
    state = current(); value = candidate(state); worktree = candidate_worktree(value)
    changed = git_ops.changed_paths(worktree)
    if not changed: raise RuntimeError("candidate worktree has no uncommitted changes to snapshot")
    before = canonical_tip(worktree)
    git_ops.run(["git", "add", "-A"], worktree)
    git_ops.run(["git", "commit", "-m", "Quarantine interrupted candidate work"], worktree)
    tip = canonical_tip(worktree)
    directory = run_dir(state) if value.get("latest_run_id") else run_root() / "recovery"
    write_json(directory / "DIRTY_SNAPSHOT.json", {
        "candidate": value["name"], "created_at": now(), "base": before,
        "commit": tip, "paths": changed, "classification": "quarantine",
    })
    value.update(status="needs_correction", current_tip=tip); value.pop("phase", None); save_current(state)
    print(f"Quarantined dirty candidate work in commit {tip}")


def review_override(review, override, reason):
    if review.get("verdict") == "accept": return None
    if not override: raise RuntimeError(f"reviewer verdict is {review.get('verdict')}; use --override-review --reason TEXT")
    if not reason or not reason.strip(): raise RuntimeError("--override-review requires a non-empty --reason")
    return {"reason": reason.strip(), "recorded_at": now()}


def apply_state_patch(review, relay_root: Path, *, mathematical_tip: str, run_id: str):
    ledger = claim_ledger.load_or_initialize(relay_root, accepted_commit=mathematical_tip)
    ledger = claim_ledger.apply_review_patch(ledger, review, mathematical_tip=mathematical_tip, run_id=run_id)
    write_json(relay_root / "CLAIMS.json", ledger)
    write_text_atomic(relay_root / "STATE.md", claim_ledger.render(ledger))
    write_text_atomic(relay_root / "HANDOFF.md", review["next_handoff"].rstrip() + "\n")


def integration_journal_path(state): return run_dir(state) / "INTEGRATION.json"


def update_integration_journal(state, **updates):
    path = integration_journal_path(state)
    data = load_json(path) if path.exists() else {}
    data.update(updates, updated_at=now()); write_json(path, data); return data


def finalize_integration(state, journal):
    value = candidate(state); worktree = candidate_worktree(value)
    expected = journal["expected_control_commit"]
    if canonical_tip(REPO) != expected:
        raise RuntimeError("accepted branch does not point to the prepared control commit")
    if worktree.exists(): git_ops.remove_worktree(REPO, worktree)
    branch_ref = f"refs/heads/{value['branch']}"
    if git_ops.run(["git", "show-ref", "--verify", "--quiet", branch_ref], REPO, check=False).returncode == 0:
        git_ops.run(["git", "branch", "-d", value["branch"]], REPO)
    update_integration_journal(state, phase="accepted", completed_at=now())
    state.update(accepted_commit=journal["mathematical_tip"], iteration=journal["iteration"],
                 last_run_id=value["latest_run_id"], last_outcome=journal.get("last_outcome"), candidate=None)
    save_current(state)
    git_ops.ensure_clean(REPO)


def recover_integration(state):
    value = candidate(state); journal = load_json(integration_journal_path(state))
    expected = journal.get("expected_control_commit"); accepted = canonical_tip(REPO)
    if not expected:
        worktree = candidate_worktree(value); tip = canonical_tip(worktree)
        subject = git_ops.run(["git", "log", "-1", "--format=%s"], worktree).stdout.strip()
        if journal.get("mathematical_tip") and subject == f"Accept relay candidate {value['name']}":
            expected = tip
            update_integration_journal(state, phase="control_prepared_recovered", expected_control_commit=expected)
        elif git_ops.changed_paths(worktree):
            value["status"] = "recovery_required"; value.pop("phase", None); save_current(state)
            update_integration_journal(state, phase="recovery_required", recovery="snapshot dirty integration work")
            print("Interrupted integration left dirty work; run candidate-snapshot-dirty")
            return
    if not expected:
        value["status"] = "awaiting_human"; value.pop("phase", None); save_current(state)
        update_integration_journal(state, phase="recovery_required", recovery="retry candidate-accept")
        print("Integration had not prepared a control commit; candidate restored to awaiting_human")
        return
    if accepted == journal.get("old_accepted_head"):
        worktree = candidate_worktree(value)
        if canonical_tip(worktree) != expected: raise RuntimeError("prepared candidate tip differs from integration journal")
        git_ops.run(["git", "merge", "--ff-only", value["branch"]], REPO)
        value["status"] = "control_committed"; save_current(state)
        update_integration_journal(state, phase="control_committed", accepted_head=canonical_tip(REPO))
    elif accepted != expected:
        raise RuntimeError("accepted branch moved outside the journaled integration; manual recovery required")
    finalize_integration(state, load_json(integration_journal_path(state)))
    print("Candidate integration recovered and finalized")


def candidate_accept(args):
    state = current(); value = candidate(state); require_candidate_status(value, "awaiting_human")
    directory = run_dir(state); review = load_json(directory / "REVIEW.json"); validations = load_json(directory / "VALIDATION.json")
    if validations.get("status") != "pass": raise RuntimeError("cannot accept failed validations")
    override = review_override(review, args.override_review, args.reason)
    require_accepted_branch(state); git_ops.ensure_clean(REPO)
    worktree = candidate_worktree(value); git_ops.ensure_clean(worktree)
    # Fetch the branch tip from Git immediately before integration and journal
    # every durable boundary before moving the accepted branch.
    accepted_head = git_ops.run(["git", "rev-parse", state["branch"]], REPO).stdout.strip()
    original_tip = canonical_tip(worktree)
    value["status"] = "integrating_prepared"
    value["phase"] = phase_record("integration", candidate_head=original_tip)
    save_current(state)
    write_json(integration_journal_path(state), {
        "candidate_id": value["name"], "run_id": value["latest_run_id"],
        "phase": "integrating_prepared", "started_at": now(),
        "old_accepted_head": accepted_head, "candidate_tip": original_tip,
        "rebased_tip": None, "mathematical_tip": None,
        "expected_control_commit": None, "accepted_head": None,
        "iteration": state.get("iteration", 0) + 1,
    })
    rebase = git_ops.run(["git", "rebase", state["branch"]], worktree, check=False)
    if rebase.returncode:
        update_integration_journal(state, phase="recovery_required", error="rebase_conflict")
        value["status"] = "awaiting_human"; value.pop("phase", None); save_current(state)
        print(f"Rebase conflict preserved in {worktree}.\nResolve files there, then run:\n  git -C {worktree} add <resolved-files>\n  git -C {worktree} rebase --continue\nOr abort with:\n  git -C {worktree} rebase --abort")
        raise RuntimeError("candidate rebase conflicted; accepted branch was not mutated")
    tip = canonical_tip(worktree); value["current_tip"] = tip; save_current(state)
    update_integration_journal(state, phase="rebased", rebased_tip=tip, mathematical_tip=tip)
    post = directory / "post-rebase"; post.mkdir(exist_ok=True)
    rerun = validation.run_all(worktree, accepted_head, tip, post, config())
    if rerun["status"] != "pass":
        value["status"] = "needs_correction"; value.pop("phase", None); save_current(state)
        update_integration_journal(state, phase="recovery_required", error="post_rebase_validation_failed")
        raise RuntimeError("post-rebase validations failed; candidate preserved")
    last_outcome = load_json(directory/"RESULT.json").get("outcome") if (directory/"RESULT.json").exists() else None
    candidate_relay = worktree / ".agent-relay"
    apply_state_patch(review, candidate_relay, mathematical_tip=tip, run_id=value["latest_run_id"])
    tracked = load_json(candidate_relay / "CURRENT.json")
    tracked.update(accepted_commit=tip, iteration=state.get("iteration", 0)+1,
                   last_run_id=value["latest_run_id"], last_outcome=last_outcome,
                   candidate=None, updated_at=now())
    write_json(candidate_relay / "CURRENT.json", tracked)
    schema_validation.validate(tracked, load_json(candidate_relay / "schemas/current-state.schema.json"))
    schema_validation.validate(load_json(candidate_relay / "CLAIMS.json"), load_json(candidate_relay / "schemas/claim-ledger.schema.json"))
    git_ops.run(["git", "add", "--", ".agent-relay/CLAIMS.json", ".agent-relay/STATE.md", ".agent-relay/HANDOFF.md", ".agent-relay/CURRENT.json"], worktree)
    git_ops.run(["git", "commit", "-m", f"Accept relay candidate {value['name']}"], worktree)
    control_tip = canonical_tip(worktree); value.update(current_tip=control_tip); save_current(state)
    update_integration_journal(state, phase="control_prepared", expected_control_commit=control_tip,
                               mathematical_tip=tip, last_outcome=last_outcome)
    git_ops.run(["git", "merge", "--ff-only", value["branch"]], REPO)
    value["status"] = "control_committed"; value.pop("phase", None); save_current(state)
    update_integration_journal(state, phase="control_committed", accepted_head=canonical_tip(REPO))
    if override: write_json(directory / "ACCEPT_OVERRIDE.json", override)
    journal = load_json(integration_journal_path(state)); finalize_integration(state, journal)
    print("Candidate accepted")
    print(f"  Mathematical tip: {tip}")
    print(f"  Control-plane HEAD: {canonical_tip(REPO)}")
    print("  Validations after rebase: PASS")
    branch_removed=git_ops.run(["git","show-ref","--verify","--quiet",f"refs/heads/{value['branch']}"],REPO,check=False).returncode != 0
    print(f"  Candidate branch removed: {'yes' if branch_removed else 'no'}")
    print(f"  Candidate worktree removed: {'yes' if not worktree.exists() else 'no'}")
    print(f"  Next handoff: {' '.join(review.get('next_handoff','-').splitlines())}")


def candidate_abandon(args):
    state = current(); value = candidate(state)
    if value["status"] in {"integrating_prepared", "control_committed"}:
        raise RuntimeError("integration is in progress; run candidate-recover before abandoning")
    if not args.yes:
        if not sys.stdin.isatty(): raise RuntimeError("candidate-abandon requires --yes or interactive confirmation")
        if input(f"Abandon candidate {value['name']}? [y/N] ").strip().lower() not in {"y","yes"}: raise RuntimeError("abandon cancelled")
    evidence=run_root()/value["latest_run_id"] if value.get("latest_run_id") else run_root()
    accepted_before=canonical_tip(REPO); worktree = candidate_worktree(value); git_ops.ensure_clean(worktree)
    git_ops.remove_worktree(REPO, worktree); git_ops.run(["git", "branch", "-D", value["branch"]], REPO)
    state["candidate"] = None; save_current(state)
    print("Candidate abandoned")
    print(f"  Accepted branch unchanged: {'yes' if canonical_tip(REPO)==accepted_before else 'no'}")
    print(f"  Local evidence preserved at: {evidence}")


def candidate_report(args):
    collector=lambda: report_snapshot(args)
    if args.watch:
        if args.json or args.diff: raise RuntimeError("--watch cannot be combined with --json or --diff")
        if args.interval <= 0: raise RuntimeError("--interval must be greater than zero")
        return candidate_reporting.watch(collector,interval=args.interval,full=args.full,no_color=args.no_color)
    data,structural=collector()
    if args.diff and not structural:
        branch=data["candidate"]["branch"]; accepted=current()["branch"]
        diff=git_ops.run(["git","diff",f"{accepted}..{branch}"],REPO).stdout
        limit=config()["review_diff_limit_bytes"]
        if len(diff.encode())>limit and not args.allow_large_diff:
            data["errors"].append(f"diff is {len(diff.encode())} bytes, above review limit {limit}; rerun with candidate-report --diff --allow-large-diff")
            structural=True; diff=None
        if diff is not None: data["git"]["diff"]=diff
    candidate_reporting.print_report(data,as_json=args.json,full=args.full)
    if args.diff and data.get("git",{}).get("diff") is not None and not args.json:
        print("\nCandidate diff\n"+data["git"]["diff"],end="" if data["git"]["diff"].endswith("\n") else "\n")
    return 1 if structural else 0


def candidate_next(args):
    state=current(); value=candidate(state); status=value["status"]
    if status=="executed": return validate_candidate(args)
    if status=="validation_passed": return review_candidate(SimpleNamespace(allow_large_packet=args.allow_large_packet, failed_validation=False))
    if status=="awaiting_human":
        directory=run_dir(state); review=_optional_report_json(directory/"REVIEW.json")
        if review and review.get("verdict")=="accept_with_corrections": return candidate_correct(SimpleNamespace(from_run=None))
    automatic_report()


def _optional_report_json(path):
    try: return load_json(path) if path.exists() else None
    except (OSError,json.JSONDecodeError): return None


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
    for artifact, schema_name in (("CURRENT.json", "current-state.schema.json"), ("CLAIMS.json", "claim-ledger.schema.json")):
        try:
            schema_validation.validate(load_json(RELAY/artifact), load_json(RELAY/"schemas"/schema_name)); ok=True
        except Exception: ok=False
        check(f"control artifact validates {artifact}", ok)
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
    item=sub.add_parser("review-failed-validation"); item.add_argument("--allow-large-packet",action="store_true"); item.set_defaults(fn=review_candidate,failed_validation=True)
    item=sub.add_parser("candidate-correct"); item.add_argument("--from-run"); item.set_defaults(fn=candidate_correct)
    item=sub.add_parser("candidate-start"); item.add_argument("--name",required=True); item.add_argument("--cherry-pick",action="append",default=[]); item.set_defaults(fn=candidate_start)
    item=sub.add_parser("candidate-accept"); item.add_argument("--override-review",action="store_true"); item.add_argument("--reason"); item.set_defaults(fn=candidate_accept)
    item=sub.add_parser("candidate-abandon"); item.add_argument("--yes",action="store_true"); item.set_defaults(fn=candidate_abandon)
    item=sub.add_parser("candidate-report"); item.add_argument("--full",action="store_true"); item.add_argument("--diff",action="store_true"); item.add_argument("--json",action="store_true"); item.add_argument("--watch",action="store_true"); item.add_argument("--run-id"); item.add_argument("--no-color",action="store_true"); item.add_argument("--interval",type=float,default=2.0); item.add_argument("--allow-large-diff",action="store_true"); item.set_defaults(fn=candidate_report)
    item=sub.add_parser("candidate-next"); item.add_argument("--allow-large-packet",action="store_true"); item.set_defaults(fn=candidate_next)
    sub.add_parser("candidate-recover").set_defaults(fn=recover_candidate)
    sub.add_parser("candidate-snapshot-dirty").set_defaults(fn=candidate_snapshot_dirty)
    item=sub.add_parser("archive-run"); item.add_argument("run_id"); item.set_defaults(fn=archive_run)
    for name in ("prepare","execute","accept","reject","cycle","run","carry-forward"):
        sub.add_parser(name).set_defaults(fn=deprecated)
    args=parser.parse_args()
    read_only = {"doctor", "status", "candidate-report"}
    try:
        if args.cmd in read_only: return args.fn(args) or 0
        with repository_lock(): return args.fn(args) or 0
    except Exception as exc: print(f"ERROR: {exc}",file=sys.stderr); return 1


if __name__ == "__main__": raise SystemExit(main())
