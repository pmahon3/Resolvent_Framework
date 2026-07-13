import subprocess, sys, tempfile, unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

SCRIPTS=Path(__file__).resolve().parents[1]/"scripts";sys.path.insert(0,str(SCRIPTS))
import git_ops

def git(cwd,*args):
    return subprocess.run(["git",*args],cwd=cwd,text=True,capture_output=True,check=True)

def init_repo(path: Path, separate: Path | None=None):
    cmd=["init"] + (["--separate-git-dir",str(separate)] if separate else [])
    git(path,*cmd); git(path,"config","user.email","test@example.invalid"); git(path,"config","user.name","Test")
    (path/"a").write_text("a"); git(path,"add","a"); git(path,"commit","-m","initial")

class GitCommonDirectoryTests(unittest.TestCase):
    def test_linked_worktree_resolves_common_directory(self):
        with tempfile.TemporaryDirectory() as d:
            repo=Path(d)/"repo"; repo.mkdir(); init_repo(repo)
            wt=Path(d)/"linked"; git(repo,"worktree","add","--detach",str(wt))
            self.assertEqual((repo/".git").resolve(),git_ops.resolve_git_common_dir(wt))
            self.assertNotEqual(git_ops.absolute_git_dir(wt),git_ops.resolve_git_common_dir(wt))
            git_ops.preflight_commit_permissions(wt,git_ops.resolve_git_common_dir(wt))
    def test_nonstandard_separate_git_directory(self):
        with tempfile.TemporaryDirectory() as d:
            repo=Path(d)/"repo"; repo.mkdir(); separate=Path(d)/"metadata.git"; init_repo(repo,separate)
            self.assertEqual(separate.resolve(),git_ops.resolve_git_common_dir(repo))
    def test_unsafe_root_common_directory_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            repo=Path(d)
            with mock.patch.object(git_ops,"root",return_value=repo), mock.patch.object(git_ops,"run",return_value=SimpleNamespace(returncode=0,stdout="/\n")):
                with self.assertRaisesRegex(RuntimeError,"unsafe Git common directory"):
                    git_ops.resolve_git_common_dir(repo)
