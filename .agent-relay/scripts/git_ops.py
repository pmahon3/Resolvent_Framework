from __future__ import annotations
import subprocess
from pathlib import Path

def run(args, cwd: Path, check=True, input_text=None):
    return subprocess.run(args, cwd=cwd, text=True, input=input_text, capture_output=True, check=check)

def root(cwd: Path) -> Path:
    return Path(run(["git", "rev-parse", "--show-toplevel"], cwd).stdout.strip()).resolve()

def head(cwd: Path) -> str:
    return run(["git", "rev-parse", "HEAD"], cwd).stdout.strip()

def branch(cwd: Path) -> str:
    return run(["git", "branch", "--show-current"], cwd).stdout.strip()

def porcelain(cwd: Path, ignore_relay_setup=False) -> list[str]:
    lines = run(["git", "status", "--porcelain"], cwd).stdout.splitlines()
    if ignore_relay_setup:
        lines = [x for x in lines if ".agent-relay" not in x and not x.endswith(" .gitignore")]
    return lines

def ensure_clean(cwd: Path):
    dirty = porcelain(cwd)
    if dirty:
        raise RuntimeError("accepted worktree is dirty:\n" + "\n".join(dirty))

def commit_exists(cwd: Path, commit: str) -> bool:
    return run(["git", "cat-file", "-e", f"{commit}^{{commit}}"], cwd, check=False).returncode == 0

def create_worktree(repo: Path, path: Path, branch_name: str, commit: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    run(["git", "worktree", "add", "-b", branch_name, str(path), commit], repo)

def remove_worktree(repo: Path, path: Path):
    run(["git", "worktree", "remove", str(path)], repo)
