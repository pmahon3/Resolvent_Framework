import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import git_ops, relay


def git(repo, *args, check=True):
    return subprocess.run(["git", *args], cwd=repo, text=True, capture_output=True, check=check).stdout.strip()


def review_data(verdict="accept"):
    return {"run_id":"run-0001","verdict":verdict,"headline":"review","verified_claims":[],"scope_corrections":[],"unsupported_claims":[],"validation_assessment":"pass","formalization_assessment":"none","strategic_assessment":"useful","required_corrections":[],"state_patch":{"banked_results_add":[],"closed_architectures_add":[],"open_gate":"gate","formalization_boundary":"boundary","next_task":"next"},"next_handoff":"correct the candidate","safe_for_automatic_acceptance":verdict=="accept","requires_human_review_reason":""}


class Fixture:
    def __init__(self):
        self.temp=tempfile.TemporaryDirectory(); self.repo=Path(self.temp.name); self.relay=self.repo/".agent-relay"
        git(self.repo,"init"); git(self.repo,"config","user.email","test@example.invalid"); git(self.repo,"config","user.name","Test")
        (self.repo/".gitignore").write_text(".agent-relay-local/\n"); (self.repo/"math.txt").write_text("base\n")
        (self.relay/"prompts").mkdir(parents=True); (self.relay/"schemas").mkdir()
        for path,text in (("prompts/executor.md","execute"),("prompts/reviewer-codex.md","review"),("RUNBOOK.md","rules"),("STATE.md","state"),("HANDOFF.md","handoff")):
            (self.relay/path).write_text(text+"\n")
        (self.relay/"schemas/executor-result.schema.json").write_text("{}")
        (self.relay/"schemas/review.schema.json").write_text("{}")
        production_schemas=Path(__file__).resolve().parents[1]/"schemas"
        for name in ("current-state.schema.json","claim-ledger.schema.json"):
            (self.relay/"schemas"/name).write_text((production_schemas/name).read_text())
        self.accepted_branch=git_ops.branch(self.repo)
        state={"schema_version":2,"project":"Resolvent_Framework","branch":self.accepted_branch,"accepted_commit":"","iteration":0,"status":"initialized","current_handoff_path":".agent-relay/HANDOFF.md","last_run_id":None,"last_outcome":None,"consecutive_rejections":0,"review_backend":"codex","candidate":None,"updated_at":"2026-01-01T00:00:00+00:00"}
        (self.relay/"CURRENT.json").write_text(json.dumps(state,indent=2)+"\n")
        git(self.repo,"add","."); git(self.repo,"commit","-m","base"); self.base=git_ops.head(self.repo)
        state["accepted_commit"]=self.base; (self.relay/"CURRENT.json").write_text(json.dumps(state,indent=2)+"\n"); git(self.repo,"add","."); git(self.repo,"commit","-m","state")
        self.base=git_ops.head(self.repo)
        self.cfg={"run_root":Path(".agent-relay-local/runs"),"worktree_root":Path(".agent-relay-local/worktrees"),"review_backend":"codex","executor_sandbox":"workspace-write","executor_model":"","reviewer_sandbox":"read-only","reviewer_model":"","review_diff_limit_bytes":100000,"packet_warning_tokens":100000,"packet_hard_limit_tokens":150000,"api_retry_count":1,"run_diff_check":True,"run_json_validations":False,"run_python_validations":False,"run_no_sorry_scan":False,"run_lake_build":False}
        self.old=(relay.REPO,relay.RELAY,relay.config); relay.REPO,relay.RELAY,relay.config=self.repo,self.relay,lambda:self.cfg

    def close(self): relay.REPO,relay.RELAY,relay.config=self.old; self.temp.cleanup()
    def start(self, picks=None): relay.candidate_start(SimpleNamespace(name="outcome-c",cherry_pick=picks or [])); return relay.current()["candidate"]
    def candidate_path(self): return self.repo/relay.current()["candidate"]["worktree"]
    def commit_candidate(self,text,message):
        wt=self.candidate_path(); (wt/"math.txt").write_text(text+"\n"); git(wt,"add","math.txt"); git(wt,"commit","-m",message); state=relay.current(); state["candidate"]["current_tip"]=git_ops.head(wt); relay.save_current(state); return git_ops.head(wt)
    def awaiting(self, verdict="accept"):
        state=relay.current(); run_id="run-0001"; directory=self.repo/self.cfg["run_root"]/run_id; directory.mkdir(parents=True,exist_ok=True)
        relay.write_json(directory/"RESULT.json",{"outcome":"SUCCESS","commits":["bogus"]}); relay.write_json(directory/"VALIDATION.json",{"status":"pass","changed_files":["math.txt"]}); relay.write_json(directory/"REVIEW.json",review_data(verdict))
        state["candidate"].update(status="awaiting_human",latest_run_id=run_id,current_tip=git_ops.head(self.candidate_path())); relay.save_current(state)


class CandidateLifecycleTests(unittest.TestCase):
    def setUp(self): self.f=Fixture()
    def tearDown(self): self.f.close()

    def test_candidate_created_from_current_accepted_head(self):
        accepted=git_ops.head(self.f.repo); value=self.f.start()
        self.assertEqual(accepted,value["initial_base"]); self.assertEqual(accepted,git_ops.head(self.f.candidate_path()))

    def test_rejected_commit_cherry_picked_exactly_once(self):
        branch="seed"; git(self.f.repo,"checkout","-b",branch); (self.f.repo/"seed.txt").write_text("seed\n"); git(self.f.repo,"add","seed.txt"); git(self.f.repo,"commit","-m","seed"); seed=git_ops.head(self.f.repo); git(self.f.repo,"checkout",self.f.accepted_branch)
        self.f.start([seed]); wt=self.f.candidate_path()
        self.assertEqual(1,int(git(wt,"rev-list","--count",f"{self.f.base}..HEAD"))); self.assertEqual("seed",git(wt,"log","-1","--format=%s"))

    def test_correction_uses_same_worktree_and_accumulates_linearly(self):
        accepted=git_ops.head(self.f.repo); self.f.start(); wt=self.f.candidate_path(); first=self.f.commit_candidate("one","one"); self.f.awaiting("accept_with_corrections")
        relay.candidate_correct(SimpleNamespace(from_run=None)); self.assertEqual(wt,self.f.candidate_path()); correction=git_ops.head(wt)
        second=self.f.commit_candidate("two","two")
        self.assertTrue(git_ops.is_ancestor(wt,first,correction)); self.assertTrue(git_ops.is_ancestor(wt,correction,second)); self.assertEqual(accepted,git_ops.head(self.f.repo))

    def test_correction_handoff_preserves_candidate_files(self):
        self.f.start(); wt=self.f.candidate_path(); (wt/"candidate.txt").write_text("keep\n"); git(wt,"add","candidate.txt"); git(wt,"commit","-m","candidate"); self.f.awaiting("accept_with_corrections")
        relay.candidate_correct(SimpleNamespace(from_run=None)); self.assertEqual("keep\n",(wt/"candidate.txt").read_text()); self.assertEqual("correct the candidate\n",(wt/".agent-relay/HANDOFF.md").read_text())

    def test_candidate_run_uses_rev_parse_not_reported_commits(self):
        self.f.start(); wt=self.f.candidate_path()
        def fake_run(prompt,cmd,events):
            (wt/"math.txt").write_text("executor\n"); git(wt,"add","math.txt"); git(wt,"commit","-m","executor"); relay.write_json(Path(cmd[cmd.index("--output-last-message")+1]),{"outcome":"SUCCESS","commits":["not-a-commit"]})
        with mock.patch.object(relay.backends,"run_codex",side_effect=fake_run): relay.candidate_run(SimpleNamespace(allow_large_packet=False))
        state=relay.current(); meta=relay.load_json(self.f.repo/self.f.cfg["run_root"]/state["candidate"]["latest_run_id"]/"META.json")
        self.assertEqual(git_ops.head(wt),meta["executor_commit"]); self.assertNotEqual("not-a-commit",meta["executor_commit"])

    def test_accept_rebases_updated_accepted_and_ff_only_and_cleans(self):
        self.f.start(); wt=self.f.candidate_path(); self.f.commit_candidate("candidate","candidate"); self.f.awaiting()
        (self.f.repo/"accepted.txt").write_text("new accepted\n"); git(self.f.repo,"add","accepted.txt"); git(self.f.repo,"commit","-m","accepted moved"); updated=git_ops.head(self.f.repo)
        calls=[]; original=git_ops.run
        def recording(args,cwd,**kwargs):
            if args[:2]==["git","merge"]: calls.append(args)
            return original(args,cwd,**kwargs)
        with mock.patch.object(relay.validation,"run_all",return_value={"status":"pass","changed_files":[],"commands":[]}), mock.patch.object(relay.git_ops,"run",side_effect=recording): relay.candidate_accept(SimpleNamespace(override_review=False,reason=None))
        self.assertTrue(git_ops.is_ancestor(self.f.repo,updated,git_ops.head(self.f.repo))); self.assertIn(["git","merge","--ff-only","relay/candidate-outcome-c"],calls); self.assertIsNone(relay.current()["candidate"]); self.assertFalse(wt.exists()); self.assertEqual([],git_ops.porcelain(self.f.repo))

    def test_rebase_conflict_preserves_both_histories(self):
        self.f.start(); wt=self.f.candidate_path(); self.f.commit_candidate("candidate","candidate"); candidate_tip=git_ops.head(wt); self.f.awaiting()
        (self.f.repo/"math.txt").write_text("accepted\n"); git(self.f.repo,"add","math.txt"); git(self.f.repo,"commit","-m","accepted conflict"); accepted_tip=git_ops.head(self.f.repo)
        with self.assertRaisesRegex(RuntimeError,"rebase conflicted"): relay.candidate_accept(SimpleNamespace(override_review=False,reason=None))
        self.assertEqual(accepted_tip,git_ops.head(self.f.repo)); self.assertTrue(wt.exists()); self.assertTrue(git_ops.commit_exists(wt,candidate_tip)); self.assertIsNotNone(relay.current()["candidate"])

    def test_abandon_deletes_candidate_not_accepted_history(self):
        accepted=git_ops.head(self.f.repo); self.f.start(); wt=self.f.candidate_path(); self.f.commit_candidate("candidate","candidate")
        relay.candidate_abandon(SimpleNamespace(yes=True)); self.assertEqual(accepted,git_ops.head(self.f.repo)); self.assertFalse(wt.exists()); self.assertIsNone(relay.current()["candidate"])

    def test_fresh_ephemeral_backend_never_resumes(self):
        source=(Path(relay.backends.__file__)).read_text(); self.assertNotIn("codex exec resume",source)
        command=relay.backends.codex_command(cwd=self.f.repo,schema=Path("s"),output=Path("o"),sandbox="workspace-write")
        self.assertIn("--ephemeral",command); self.assertNotIn("resume",command)


if __name__ == "__main__": unittest.main()
