import json, subprocess, sys, tempfile, unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

SCRIPTS=Path(__file__).resolve().parents[1]/"scripts";sys.path.insert(0,str(SCRIPTS))
import git_ops, relay

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

class RecoveryTests(unittest.TestCase):
    def test_executor_commit_failure_records_uncommitted(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); rd=root/"run"; wt=root/"wt"; rd.mkdir(); wt.mkdir()
            meta={"worktree":str(wt),"accepted_parent_commit":"parent"}; (rd/"META.json").write_text(json.dumps(meta))
            state={"status":"prepared","last_outcome":None}
            def save(c): state.update(c)
            with mock.patch.object(relay,"current",return_value=state), mock.patch.object(relay,"run_dir",return_value=rd), mock.patch.object(relay,"config",return_value={"executor_sandbox":"workspace-write","executor_model":""}), mock.patch.object(relay,"save_current",side_effect=save), mock.patch.object(relay.git_ops,"resolve_git_common_dir",return_value=root/"git"), mock.patch.object(relay.git_ops,"preflight_commit_permissions"), mock.patch.object(relay.git_ops,"changed_paths",return_value=["changed.txt"]), mock.patch.object(relay.git_ops,"head",return_value="parent"), mock.patch.object(relay.backends,"run_codex",side_effect=RuntimeError("commit failed")):
                (rd/"EXECUTOR_PACKET.md").write_text("packet")
                with self.assertRaisesRegex(RuntimeError,"did not create a commit"): relay.execute(None)
            self.assertEqual("executor_uncommitted",state["status"])
            self.assertEqual(["changed.txt"],json.loads((rd/"META.json").read_text())["reported_changed_files"])
    def test_review_refuses_missing_executor_commit(self):
        with tempfile.TemporaryDirectory() as d:
            rd=Path(d); wt=rd/"wt"; wt.mkdir(); (rd/"META.json").write_text(json.dumps({"worktree":str(wt),"accepted_parent_commit":"parent"})); (rd/"RESULT.json").write_text("{}"); (rd/"VALIDATION.json").write_text("{}")
            with mock.patch.object(relay,"current",return_value={}), mock.patch.object(relay,"run_dir",return_value=rd), mock.patch.object(relay,"config",return_value={}):
                with self.assertRaisesRegex(RuntimeError,"executor commit missing"): relay.review(SimpleNamespace(allow_large_packet=False))
    def test_recover_commit_records_commit_exactly_once(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); wt=root/"wt"; wt.mkdir(); init_repo(wt); parent=git_ops.head(wt); (wt/"a").write_text("changed")
            rd=root/"run"; rd.mkdir(); (rd/"META.json").write_text(json.dumps({"run_id":"run-0001","worktree":str(wt),"accepted_parent_commit":parent,"reported_changed_files":["a"]})); (rd/"RESULT.json").write_text(json.dumps({"headline":"Recovered change","outcome":"PARTIAL"}))
            state={"status":"executor_uncommitted","last_outcome":"FAILED"}
            def save(c): state.update(c)
            with mock.patch.object(relay,"current",return_value=state), mock.patch.object(relay,"run_dir",return_value=rd), mock.patch.object(relay,"config",return_value={}), mock.patch.object(relay,"save_current",side_effect=save), mock.patch.object(relay.validation,"run_uncommitted",return_value={"status":"pass"}):
                relay.recover_commit(SimpleNamespace(yes=True,message=None)); recovered=json.loads((rd/"META.json").read_text())["executor_commit"]
                self.assertEqual(recovered,git_ops.head(wt))
                with self.assertRaisesRegex(RuntimeError,"not executor_uncommitted"): relay.recover_commit(SimpleNamespace(yes=True,message=None))
                self.assertEqual(2,int(git(wt,"rev-list","--count","HEAD").stdout))
