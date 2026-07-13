from __future__ import annotations

import json
import sys
import time
from collections import Counter
from pathlib import Path


def _git(git_ops, args, cwd, check=True):
    return git_ops.run(["git", *args], cwd, check=check)


def _optional_json(path: Path, label: str, errors: list[str]):
    if not path.exists(): return None
    try: return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"malformed {label}: {exc}"); return None


def available_actions(status: str, review: dict | None) -> list[str]:
    if status == "needs_correction": return ["candidate-run", "candidate-abandon"]
    if status == "executed": return ["validate", "candidate-abandon"]
    if status == "validated": return ["review", "candidate-abandon"]
    if status == "awaiting_human":
        verdict = (review or {}).get("verdict")
        if verdict == "accept": return ["candidate-accept", "candidate-abandon"]
        if verdict == "accept_with_corrections":
            return ["candidate-correct", "candidate-accept --override-review --reason ...", "candidate-abandon"]
        if verdict == "reject": return ["candidate-correct", "candidate-abandon"]
        return ["candidate-abandon"]
    if status == "ready": return ["candidate-run", "candidate-abandon"]
    if status == "executing": return ["candidate-report --watch"]
    return []


def collect(repo: Path, state: dict, cfg: dict, git_ops, run_id: str | None = None) -> tuple[dict, bool]:
    errors=[]; value=state.get("candidate")
    empty={"candidate":{},"executor":None,"validation":None,"review":None,
           "git":{"base":"","tip":"","clean":False,"commits":[],"changed_files":[],"diff_stat":""},
           "available_actions":[],"errors":["no active candidate"]}
    if not value: return empty, True
    candidate_data=dict(value); worktree=repo/value.get("worktree","")
    structural=False
    if not worktree.is_dir(): errors.append(f"candidate worktree missing: {worktree}"); structural=True
    branch=value.get("branch","")
    branch_check=_git(git_ops,["show-ref","--verify","--quiet",f"refs/heads/{branch}"],repo,check=False)
    if branch_check.returncode: errors.append(f"candidate branch absent: {branch}"); structural=True

    git_data={"base":"","tip":"","clean":False,"commits":[],"changed_files":[],"diff_stat":""}
    if not structural:
        try:
            base=_git(git_ops,["rev-parse",state["branch"]],repo).stdout.strip()
            tip=_git(git_ops,["rev-parse",branch],repo).stdout.strip()
            commits=_git(git_ops,["log","--oneline",f"{state['branch']}..{branch}"],repo).stdout.splitlines()
            changed=_git(git_ops,["diff","--name-status",f"{state['branch']}..{branch}"],repo).stdout.splitlines()
            stat=_git(git_ops,["diff","--stat",f"{state['branch']}..{branch}"],repo).stdout.rstrip()
            clean=not git_ops.porcelain(worktree)
            git_data.update(base=base,tip=tip,clean=clean,commits=commits,changed_files=changed,diff_stat=stat)
            stored=value.get("current_tip")
            if stored and stored != tip: errors.append(f"candidate Git tip {tip} differs from stored state {stored}")
        except Exception as exc:
            errors.append(f"candidate Git inspection failed: {exc}"); structural=True

    selected_run=run_id or value.get("latest_run_id"); candidate_data["report_run_id"]=selected_run
    result=validations=review=None
    if selected_run:
        directory=repo/cfg["run_root"]/selected_run
        if not directory.is_dir(): errors.append(f"latest run directory missing: {directory}"); structural=True
        else:
            result=_optional_json(directory/"RESULT.json","RESULT.json",errors)
            validations=_optional_json(directory/"VALIDATION.json","VALIDATION.json",errors)
            review=_optional_json(directory/"REVIEW.json","REVIEW.json",errors)
            candidate_data["executor_active"] = value.get("status")=="executing"
            candidate_data["reviewer_active"] = (directory/"REVIEW_ACTIVE").exists()
    else:
        candidate_data.update(executor_active=False,reviewer_active=False)
    data={"candidate":candidate_data,"executor":result,"validation":validations,"review":review,
          "git":git_data,"available_actions":available_actions(value.get("status",""),review),"errors":errors}
    return data, structural


def _short(value): return value[:8] if value else "-"
def _line_value(value): return " ".join(str(value or "-").splitlines())
def _compact(value, limit=240):
    value=_line_value(value)
    return value if len(value)<=limit else value[:limit-1]+"…"
def _duration(validation):
    seconds=sum(float(item.get("duration_seconds",0) or 0) for item in validation.get("commands",[]))
    return f"{seconds:.3f}s"


def render(data: dict, *, full=False) -> str:
    c=data["candidate"]; git=data["git"]; out=[]
    if c:
        out += ["Candidate",f"  Name: {c.get('name','-')}",f"  Branch: {c.get('branch','-')}",
                f"  Status: {c.get('status','-')}",f"  Run: {c.get('report_run_id') or '-'}",
                f"  Base: {_short(git.get('base'))}",f"  Tip: {_short(git.get('tip'))}",
                f"  Commits ahead: {len(git.get('commits',[]))}",f"  Changed files: {len(git.get('changed_files',[]))}",
                f"  Worktree: {'clean' if git.get('clean') else 'DIRTY'}"]
        if c.get("executor_active"): out.append("  Process: executor active")
        if c.get("reviewer_active"): out.append("  Process: reviewer active")
    result=data.get("executor")
    if result:
        counts=Counter(item.get("status","unknown") for item in result.get("claims",[]))
        out += ["","Executor",f"  Outcome: {result.get('outcome','-')}",f"  Headline: {_line_value(result.get('headline'))}",
                f"  Repository change: {'committed' if git.get('commits') and git.get('clean') else 'uncommitted or unchanged'}","  Claims:"]
        for status,count in sorted(counts.items()): out.append(f"    {status}: {count}")
        out += [f"  Uncertainties: {len(result.get('uncertainties',[]))}",f"  Next task: {_compact(result.get('recommended_next_task'))}"]
        if full:
            out += [f"  Summary: {result.get('summary','-')}","  Claim details:"]
            for i,claim in enumerate(result.get("claims",[]),1):
                out += [f"    {i}. [{claim.get('status','-')}] {claim.get('claim','-')}",f"       Scope: {claim.get('scope','-')}",
                        f"       Confidence: {claim.get('confidence','-')}"]
                for evidence in claim.get("evidence",[]): out.append(f"       Evidence: {evidence}")
            out += ["  All uncertainties:"]+[f"    - {x}" for x in result.get("uncertainties",[])]
            out += ["  Possible overstatements:"]+[f"    - {x}" for x in result.get("possible_overstatements",[])]
    validation=data.get("validation")
    if validation:
        commands=validation.get("commands",[]); passed=sum(x.get("exit_code")==0 for x in commands); failed=len(commands)-passed
        out += ["","Validation",f"  Status: {str(validation.get('status','-')).upper()}",f"  Commands passed: {passed}",f"  Commands failed: {failed}",f"  Duration: {_duration(validation)}"]
        if full:
            out += ["  Command summaries:"]
            for item in commands: out.append(f"    [{'PASS' if item.get('exit_code')==0 else 'FAIL'}] {item.get('command','-')} ({float(item.get('duration_seconds',0) or 0):.3f}s)")
    review=data.get("review")
    if review:
        material=sum(x.get("severity") in {"material","critical"} for x in review.get("scope_corrections",[]))
        out += ["","Review",f"  Verdict: {review.get('verdict','-')}",f"  Verified claims: {len(review.get('verified_claims',[]))}",
                f"  Material corrections: {material}",f"  Unsupported claims: {len(review.get('unsupported_claims',[]))}"]
        if review.get("required_corrections"):
            out.append("  Required corrections:")
            out += [f"    {i}. {item}" for i,item in enumerate(review["required_corrections"],1)]
        out.append(f"  Next handoff: {_compact(review.get('next_handoff'))}")
        if full:
            out += ["  Scope corrections:"]
            for item in review.get("scope_corrections",[]): out.append(f"    [{item.get('severity','-')}] {item.get('claim','-')}: {item.get('correction','-')}")
            out += ["  Unsupported claims:"]+[f"    - {x}" for x in review.get("unsupported_claims",[])]
            out += [f"  Strategic assessment: {review.get('strategic_assessment','-')}","  Full next handoff:",review.get("next_handoff","-")]
    if git.get("commits"):
        out += ["","Candidate commits"]+[f"  {item}" for item in git["commits"]]
    if git.get("changed_files"):
        out += ["","Changed files"]+[f"  {item}" for item in git["changed_files"]]
    if data.get("available_actions"):
        out += ["","Available actions"]+[f"  {item}" for item in data["available_actions"]]
    if data.get("errors"):
        out += ["","Errors"]+[f"  - {item}" for item in data["errors"]]
    return "\n".join(out)+"\n"


def print_report(data: dict, *, as_json=False, full=False, stream=None):
    stream=stream or sys.stdout
    if as_json: print(json.dumps(data,indent=2),file=stream)
    else: print(render(data,full=full),end="",file=stream)


def watch(collector, *, interval: float, full=False, no_color=False):
    first=True
    try:
        while True:
            data,structural=collector()
            if not first and sys.stdout.isatty(): print("\033[2J\033[H",end="")
            print_report(data,full=full); first=False
            active=data.get("candidate",{}).get("executor_active") or data.get("candidate",{}).get("reviewer_active")
            if structural or not active: return 1 if structural else 0
            time.sleep(interval)
    except KeyboardInterrupt:
        return 0
