from __future__ import annotations
import json, subprocess, time
from pathlib import Path
import shutil

def command(cmd: list[str], cwd: Path, log: Path):
    start=time.monotonic(); p=subprocess.run(cmd,cwd=cwd,text=True,capture_output=True)
    text=(p.stdout or "")+(p.stderr or ""); log.parent.mkdir(parents=True,exist_ok=True); log.write_text(text,encoding="utf-8")
    return {"command":" ".join(cmd),"exit_code":p.returncode,"duration_seconds":round(time.monotonic()-start,3),"tail":text[-3000:],"log_path":str(log)}

def discover_python(changed: list[str], handoff: str):
    paths=[]
    for p in changed:
        if p.endswith(".py") and ("verification/" in p or "oracles/" in p): paths.append(p)
    for token in handoff.replace("`", " ").split():
        if token.endswith(".py") and token not in paths: paths.append(token)
    return paths

def run_all(worktree: Path, parent: str, commit: str, run_dir: Path, config: dict):
    changed=subprocess.run(["git","diff","--name-only",f"{parent}..{commit}"],cwd=worktree,text=True,capture_output=True,check=True).stdout.splitlines()
    results=[]
    if config.get("run_diff_check",True): results.append(command(["git","diff","--check",f"{parent}..{commit}"],worktree,run_dir/"logs/diff-check.log"))
    if config.get("run_json_validations",True):
        for i,p in enumerate(x for x in changed if x.endswith(".json")):
            results.append(command(["python3","-m","json.tool",p],worktree,run_dir/f"logs/json-{i}.log"))
    if config.get("run_python_validations",True):
        handoff=(worktree/".agent-relay/HANDOFF.md").read_text(errors="replace")
        for i,p in enumerate(discover_python(changed,handoff)):
            if (worktree/p).is_file(): results.append(command(["python3",p],worktree,run_dir/f"logs/python-{i}.log"))
    if config.get("run_no_sorry_scan",True) and any(x.endswith(".lean") for x in changed):
        results.append(command(["rg","-n",r"\b(sorry|sorryAx)\b"]+changed,worktree,run_dir/"logs/no-sorry.log"))
        results[-1]["exit_code"] = 0 if results[-1]["exit_code"] == 1 else 1
    lean=worktree/"formalization/QuerySystem"
    if config.get("run_lake_build",True) and lean.joinpath("lakefile.toml").exists() and any(x.endswith(".lean") for x in changed):
        lake=shutil.which("lake") or str(Path.home()/".elan/bin/lake")
        results.append(command([lake,"build"],lean,run_dir/"logs/lake-build.log"))
    data={"status":"pass" if all(x["exit_code"]==0 for x in results) else "fail","changed_files":changed,"commands":results,"commit":commit}
    (run_dir/"VALIDATION.json").write_text(json.dumps(data,indent=2),encoding="utf-8"); return data
