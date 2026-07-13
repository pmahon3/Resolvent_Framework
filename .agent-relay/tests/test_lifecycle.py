import contextlib
import io
import json
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

SCRIPTS=Path(__file__).resolve().parents[1]/"scripts"
sys.path.insert(0,str(SCRIPTS))
import git_ops, relay


def git(repo,*args):
    return subprocess.run(["git",*args],cwd=repo,text=True,capture_output=True,check=True).stdout.strip()


def review_data(verdict="accept"):
    return {
        "run_id":"run-0001-review","verdict":verdict,"headline":"fake review",
        "verified_claims":["verified"],"scope_corrections":[],"unsupported_claims":["unsupported"],
        "validation_assessment":"pass","formalization_assessment":"none","strategic_assessment":"useful",
        "required_corrections":[],
        "state_patch":{"banked_results_add":["banked"],"closed_architectures_add":[],"open_gate":"gate","formalization_boundary":"boundary","next_task":"next"},
        "next_handoff":"repair or continue","safe_for_automatic_acceptance":verdict=="accept",
        "requires_human_review_reason":"test",
    }


class RelayFixture:
    def __init__(self):
        self.temp=tempfile.TemporaryDirectory(); self.repo=Path(self.temp.name); self.relay=self.repo/".agent-relay"
        git(self.repo,"init"); git(self.repo,"config","user.email","test@example.invalid"); git(self.repo,"config","user.name","Test")
        (self.repo/".gitignore").write_text(".agent-relay-local/\n")
        (self.repo/"math.txt").write_text("base\n")
        (self.relay/"prompts").mkdir(parents=True); (self.relay/"schemas").mkdir()
        (self.relay/"prompts/reviewer-codex.md").write_text("review")
        (self.relay/"prompts/executor.md").write_text("execute")
        (self.relay/"schemas/review.schema.json").write_text("{}")
        (self.relay/"RUNBOOK.md").write_text("rules\n"); (self.relay/"STATE.md").write_text("state\n"); (self.relay/"HANDOFF.md").write_text("handoff\n")
        (self.relay/"LEDGER.jsonl").write_text("")
        self.current={"schema_version":2,"project":"Resolvent_Framework","branch":"master","accepted_commit":"accepted-math-before-control", "iteration":0,"status":"initialized","current_handoff_path":".agent-relay/HANDOFF.md","last_run_id":None,"last_outcome":None,"consecutive_rejections":0,"review_backend":"codex","updated_at":"2026-01-01T00:00:00+00:00"}
        (self.relay/"CURRENT.json").write_text(json.dumps(self.current,indent=2)+"\n")
        git(self.repo,"add","."); git(self.repo,"commit","-m","base")
        self.base=git_ops.head(self.repo)
        self.cfg={"run_root":Path(".agent-relay-local/runs"),"worktree_root":Path(".agent-relay-local/worktrees"),"review_backend":"codex","reviewer_sandbox":"read-only","reviewer_model":"","review_diff_limit_bytes":100000,"packet_warning_tokens":100000,"packet_hard_limit_tokens":150000,"api_retry_count":1,"remove_worktree_on_accept":False}
        self.old_repo,self.old_relay,self.old_config=relay.REPO,relay.RELAY,relay.config
        relay.REPO,relay.RELAY,relay.config=self.repo,self.relay,lambda:self.cfg
        self.make_run()

    def write_current(self): (self.relay/"CURRENT.json").write_text(json.dumps(self.current,indent=2)+"\n")
    def read_current(self): return json.loads((self.relay/"CURRENT.json").read_text())
    def make_run(self):
        self.run=self.repo/self.cfg["run_root"]/"run-0001"; self.run.mkdir(parents=True)
        self.wt=self.repo/self.cfg["worktree_root"]/"run-0001"
        git_ops.create_worktree(self.repo,self.wt,"relay/run-0001",self.base)
        (self.wt/"math.txt").write_text("executor\n"); git(self.wt,"add","math.txt"); git(self.wt,"commit","-m","executor")
        self.executor=git_ops.head(self.wt)
        meta={"run_id":"run-0001","iteration":1,"started_at":"2026-01-01T00:00:00+00:00","base_commit":self.base,"worktree":str(self.wt),"branch":"relay/run-0001","handoff_sha256":relay.sha(self.relay/"HANDOFF.md"),"state_sha256_before":relay.sha(self.relay/"STATE.md"),"executor_commit":self.executor}
        relay.write_json(self.run/"META.json",meta)
        relay.write_json(self.run/"RESULT.json",{"outcome":"SUCCESS"})
        relay.write_json(self.run/"VALIDATION.json",{"status":"pass","changed_files":["math.txt"]})
        self.current.update(last_run_id="run-0001",status="validated"); self.write_current()

    def install_review(self,verdict="accept"):
        relay.write_json(self.run/"REVIEW.json",review_data(verdict)); self.current=self.read_current(); self.current["status"]="awaiting_human"; self.write_current()

    def fake_review(self,verdict="accept"):
        calls=[]
        def command(**kwargs): return ["fake",str(kwargs["output"])]
        def run(packet,cmd,events): calls.append(packet); relay.write_json(Path(cmd[1]),review_data(verdict))
        return calls,command,run

    def close(self):
        relay.REPO,relay.RELAY,relay.config=self.old_repo,self.old_relay,self.old_config
        self.temp.cleanup()


class LifecycleTests(unittest.TestCase):
    def setUp(self): self.f=RelayFixture()
    def tearDown(self): self.f.close()

    def run_review(self,verdict="accept"):
        calls,command,runner=self.f.fake_review(verdict)
        with mock.patch.object(relay.backends,"codex_command",side_effect=command), mock.patch.object(relay.backends,"run_codex",side_effect=runner):
            relay.review(SimpleNamespace(force=False,allow_large_packet=False))
        return calls

    def test_review_accept_review_is_immutable_and_does_not_invoke_backend(self):
        self.assertEqual(1,len(self.run_review()))
        original=(self.f.run/"REVIEW.json").read_bytes(); relay.finish("accept")
        with mock.patch.object(relay.backends,"run_codex") as backend:
            with self.assertRaisesRegex(RuntimeError,"already finalized as accept"):
                relay.review(SimpleNamespace(force=True,allow_large_packet=False))
            backend.assert_not_called()
        self.assertEqual(original,(self.f.run/"REVIEW.json").read_bytes())

    def test_accept_then_reject_is_immutable(self):
        self.run_review(); relay.finish("accept")
        with self.assertRaisesRegex(RuntimeError,"finalized as accept and cannot be changed to reject"): relay.finish("reject")

    def test_reject_then_accept_is_immutable(self):
        self.run_review("reject"); relay.finish("reject")
        with self.assertRaisesRegex(RuntimeError,"finalized as reject and cannot be changed to accept"): relay.finish("accept")

    def test_repeated_accept_is_idempotent_and_single_row(self):
        self.f.install_review(); relay.finish("accept"); relay.finish("accept")
        self.assertEqual(1,len(relay.ledger_entries()))

    def test_repeated_reject_is_idempotent_and_single_row(self):
        self.f.install_review("reject"); relay.finish("reject"); relay.finish("reject")
        self.assertEqual(1,len(relay.ledger_entries()))

    def test_duplicate_ledger_preflight_does_not_mutate(self):
        self.f.install_review(); row={"run_id":"run-0001","human_decision":"accept"}
        (self.f.relay/"LEDGER.jsonl").write_text(json.dumps(row)+"\n")
        before={p:p.read_bytes() for p in (self.f.relay/"CURRENT.json",self.f.relay/"STATE.md",self.f.relay/"HANDOFF.md",self.f.relay/"LEDGER.jsonl")}; head=git_ops.head(self.f.repo)
        with self.assertRaisesRegex(RuntimeError,"cannot be changed"): relay.finish("reject")
        self.assertEqual(head,git_ops.head(self.f.repo)); self.assertEqual(before,{p:p.read_bytes() for p in before})

    def test_reviewer_reject_requires_override_and_records_reason(self):
        self.f.install_review("reject")
        with self.assertRaisesRegex(RuntimeError,"override-review"): relay.finish("accept")
        relay.finish("accept",True,"independent human verification")
        self.assertEqual("independent human verification",relay.ledger_entry("run-0001")["review_override"]["reason"])

    def test_review_requires_validated(self):
        c=self.f.read_current(); c["status"]="executed"; relay.write_json(self.f.relay/"CURRENT.json",c)
        with mock.patch.object(relay.backends,"run_codex") as backend:
            with self.assertRaisesRegex(RuntimeError,"requires status validated"): relay.review(SimpleNamespace(force=False,allow_large_packet=False))
            backend.assert_not_called()

    def test_finalization_requires_awaiting_human(self):
        with self.assertRaisesRegex(RuntimeError,"requires status awaiting_human"): relay.finish("reject")
        with self.assertRaisesRegex(RuntimeError,"requires status awaiting_human"): relay.finish("accept")

    def test_accept_control_files_committed_and_worktree_clean(self):
        self.f.install_review(); relay.finish("accept")
        self.assertEqual("",git(self.f.repo,"status","--porcelain")); self.assertEqual("Finalize relay run run-0001: accept",git(self.f.repo,"log","-1","--format=%s"))
        self.assertEqual(self.f.executor,self.f.read_current()["accepted_commit"])

    def test_reject_control_files_committed_and_worktree_clean(self):
        before=self.f.base; self.f.install_review("reject"); relay.finish("reject")
        self.assertEqual("",git(self.f.repo,"status","--porcelain")); self.assertEqual("Finalize relay run run-0001: reject",git(self.f.repo,"log","-1","--format=%s")); self.assertFalse(git_ops.is_ancestor(self.f.repo,self.f.executor,git_ops.head(self.f.repo))); self.assertTrue(git_ops.is_ancestor(self.f.repo,before,git_ops.head(self.f.repo)))

    def test_next_worktree_starts_at_control_head(self):
        self.f.install_review("reject"); relay.finish("reject"); control_head=git_ops.head(self.f.repo)
        relay.prepare(SimpleNamespace(allow_large_packet=False))
        meta=relay.load_json(self.f.repo/self.f.cfg["run_root"]/"run-0002"/"META.json")
        self.assertEqual(control_head,meta["base_commit"]); self.assertEqual(control_head,git_ops.head(Path(meta["worktree"])))

    def test_reconcile_repairs_stale_finalized_state_and_archives_review(self):
        self.f.install_review(); relay.finish("accept"); later=review_data("reject"); relay.write_json(self.f.run/"REVIEW.json",later)
        c=self.f.read_current(); c["status"]="awaiting_human"; relay.write_json(self.f.relay/"CURRENT.json",c)
        with contextlib.redirect_stdout(io.StringIO()) as output: relay.reconcile(SimpleNamespace(apply=True))
        self.assertEqual("initialized",self.f.read_current()["status"]); self.assertTrue((self.f.run/"REVIEW.post-finalization.json").exists()); self.assertIn("non-authoritative",output.getvalue()); self.assertEqual("accept",relay.finalized_entry("run-0001")["human_decision"])

    def test_finalized_review_cannot_be_overwritten_even_with_force(self):
        self.f.install_review(); relay.finish("reject"); original=(self.f.run/"REVIEW.json").read_bytes()
        with self.assertRaisesRegex(RuntimeError,"finalized runs are immutable"): relay.review(SimpleNamespace(force=True,allow_large_packet=False))
        self.assertEqual(original,(self.f.run/"REVIEW.json").read_bytes())

    def test_conflicting_duplicate_ledger_rows_are_corruption(self):
        rows=[{"run_id":"run-0001","human_decision":"accept"},{"run_id":"run-0001","human_decision":"reject"}]
        (self.f.relay/"LEDGER.jsonl").write_text("".join(json.dumps(x)+"\n" for x in rows))
        with self.assertRaisesRegex(RuntimeError,"ledger corruption: duplicate rows"): relay.ledger_entries()


if __name__=="__main__": unittest.main()
