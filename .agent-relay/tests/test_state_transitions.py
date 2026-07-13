import subprocess, sys, tempfile, unittest
from pathlib import Path
SCRIPTS=Path(__file__).resolve().parents[1]/"scripts"; sys.path.insert(0,str(SCRIPTS))
import git_ops

class TransitionTests(unittest.TestCase):
    def test_dirty_worktree_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            repo=Path(directory); subprocess.run(["git","init"],cwd=repo,capture_output=True); subprocess.run(["git","config","user.email","test@example.invalid"],cwd=repo); subprocess.run(["git","config","user.name","Test"],cwd=repo)
            (repo/"a").write_text("a"); subprocess.run(["git","add","a"],cwd=repo); subprocess.run(["git","commit","-m","a"],cwd=repo,capture_output=True); (repo/"a").write_text("b")
            self.assertRaises(RuntimeError,git_ops.ensure_clean,repo)
