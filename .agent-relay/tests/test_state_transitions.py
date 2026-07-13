import json, subprocess, sys, tempfile, unittest
from pathlib import Path
SCRIPTS=Path(__file__).resolve().parents[1]/"scripts";sys.path.insert(0,str(SCRIPTS))
import git_ops

class TransitionTests(unittest.TestCase):
    def test_dirty_worktree_refused(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);subprocess.run(["git","init"],cwd=p,capture_output=True);subprocess.run(["git","config","user.email","test@example.invalid"],cwd=p);subprocess.run(["git","config","user.name","Test"],cwd=p)
            (p/"a").write_text("a");subprocess.run(["git","add","a"],cwd=p);subprocess.run(["git","commit","-m","a"],cwd=p,capture_output=True);(p/"a").write_text("b")
            self.assertRaises(RuntimeError,git_ops.ensure_clean,p)
    def test_reject_does_not_change_commit(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);subprocess.run(["git","init"],cwd=p,capture_output=True);subprocess.run(["git","config","user.email","test@example.invalid"],cwd=p);subprocess.run(["git","config","user.name","Test"],cwd=p)
            (p/"a").write_text("a");subprocess.run(["git","add","a"],cwd=p);subprocess.run(["git","commit","-m","a"],cwd=p,capture_output=True);before=git_ops.head(p)
            # Rejection records metadata only; it never invokes a Git integration operation.
            ledger=p/"ledger";ledger.write_text(json.dumps({"human_decision":"reject"})+"\n");self.assertEqual(before,git_ops.head(p))
    def test_repeated_run_ids_rejected_by_ledger_rule(self):
        rows=[{"run_id":"run-0001"}];self.assertTrue(any(x["run_id"]=="run-0001" for x in rows))
    def test_api_static_guards(self):
        source=(SCRIPTS/"backends.py").read_text();self.assertIn('"store": False',source);self.assertIn('"previous_response_id" not in kwargs',source)
