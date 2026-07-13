from __future__ import annotations
import os, subprocess, tempfile
from pathlib import Path

def run(args, cwd: Path, check=True, input_text=None):
    return subprocess.run(args, cwd=cwd, text=True, input=input_text, capture_output=True, check=check)

def root(cwd: Path) -> Path:
    return Path(run(["git", "rev-parse", "--show-toplevel"], cwd).stdout.strip()).resolve()

def _resolved_git_path(raw: str, repo_root: Path) -> Path:
    path = Path(raw.strip())
    return (path if path.is_absolute() else repo_root / path).resolve()

def resolve_git_common_dir(repo_root: Path) -> Path:
    """Return and safety-check this repository's absolute common Git directory."""
    repo_root = root(repo_root)
    result = run(
        ["git", "rev-parse", "--path-format=absolute", "--git-common-dir"],
        repo_root,
        check=False,
    )
    if result.returncode == 0:
        common = _resolved_git_path(result.stdout, repo_root)
    else:
        fallback = run(["git", "rev-parse", "--git-common-dir"], repo_root)
        common = _resolved_git_path(fallback.stdout, repo_root)

    home = Path.home().resolve()
    if not common.exists() or not common.is_dir():
        raise RuntimeError(f"Git common directory does not exist: {common}")
    if common in (Path("/"), home):
        raise RuntimeError(f"Refusing unsafe Git common directory: {common}")
    # A Git directory may legitimately be separate from the worktree, but it must
    # never broaden access to a directory containing the entire repository.
    if common == repo_root or common in repo_root.parents:
        raise RuntimeError(f"Refusing unexpectedly broad Git common directory: {common}")
    if not (common / "HEAD").exists() or not (common / "objects").is_dir():
        raise RuntimeError(f"Path is not a Git common directory: {common}")
    verified = _resolved_git_path(
        run(["git", f"--git-dir={common}", "rev-parse", "--git-common-dir"], repo_root).stdout,
        repo_root,
    )
    if verified != common:
        raise RuntimeError(f"Git common directory does not belong to this repository: {common}")
    return common

def absolute_git_dir(cwd: Path) -> Path:
    return _resolved_git_path(run(["git", "rev-parse", "--absolute-git-dir"], cwd).stdout, cwd)

def changed_paths(cwd: Path) -> list[str]:
    tracked = set(run(["git", "diff", "--name-only", "HEAD"], cwd).stdout.splitlines())
    staged = set(run(["git", "diff", "--cached", "--name-only", "HEAD"], cwd).stdout.splitlines())
    untracked = set(run(["git", "ls-files", "--others", "--exclude-standard"], cwd).stdout.splitlines())
    return sorted(tracked | staged | untracked)

def preflight_commit_permissions(worktree: Path, git_common_dir: Path):
    """Probe only disposable paths and always remove them."""
    worktree = worktree.resolve(); git_common_dir = git_common_dir.resolve()
    if root(worktree) != worktree:
        raise RuntimeError(f"Executor worktree is not a repository root: {worktree}")
    if resolve_git_common_dir(worktree) != git_common_dir:
        raise RuntimeError("Executor worktree common Git directory differs from --add-dir")
    git_dir = absolute_git_dir(worktree)
    try:
        git_dir.relative_to(git_common_dir)
    except ValueError as exc:
        raise RuntimeError(f"Linked worktree Git directory is outside common Git directory: {git_dir}") from exc

    probe_dir = git_common_dir / "relay-permission-probes"
    created_probe_dir = False
    probes: list[Path] = []
    try:
        probe_dir.mkdir(exist_ok=True); created_probe_dir = True
        for directory in (git_dir, probe_dir):
            fd, name = tempfile.mkstemp(prefix="relay-", dir=directory)
            os.close(fd); probe = Path(name); probes.append(probe)
            probe.unlink(); probes.remove(probe)
    except OSError as exc:
        raise RuntimeError(f"Git commit permission preflight failed: {exc}") from exc
    finally:
        for probe in probes:
            probe.unlink(missing_ok=True)
        if created_probe_dir:
            try: probe_dir.rmdir()
            except OSError: pass

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
