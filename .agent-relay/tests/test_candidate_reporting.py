import contextlib
import io
import json
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

SCRIPTS=Path(__file__).resolve().parents[1]/"scripts";sys.path.insert(0,str(SCRIPTS))
import candidate_reporting, git_ops, relay
from test_lifecycle import Fixture, git, review_data


def args(**values):
    defaults={"full":False,"diff":False,"json":False,"watch":False,"run_id":None,"no_color":True,"interval":0.001,"allow_large_diff":False}
    defaults.update(values); return SimpleNamespace(**defaults)


def result_data():
    return {"run_id":"run-0001","outcome":"C","headline":"Candidate headline","summary":"EXECUTOR-SUMMARY-MARKER",
            "claims":[{"claim":"Detailed claim","status":"proved","scope":"scope marker","evidence":["EVIDENCE-MARKER"],"confidence":"high"}],
            "uncertainties":["uncertain marker"],"possible_overstatements":["overstatement marker"],"recommended_next_task":"next task",
            "commits":["model-bogus-hash"]}


def validation_data():
    return {"status":"pass","changed_files":["math.txt"],"commands":[{"command":"check one","exit_code":0,"duration_seconds":1.25,"tail":"RAW-LOG-MARKER"}]}


def detailed_review(verdict="accept"):
    data=review_data(verdict); data["verified_claims"]=["one"]; data["required_corrections"]=["REQUIRED-CORRECTION-MARKER"]
    data["scope_corrections"]=[{"claim":"claim","correction":"SCOPE-CORRECTION-MARKER","severity":"material"}]
    data["unsupported_claims"]=["unsupported marker"]; data["strategic_assessment"]="STRATEGIC-MARKER"; data["next_handoff"]="NEXT-HANDOFF-MARKER"
    return data


class CandidateReportTests(unittest.TestCase):
    def setUp(self): self.f=Fixture()
    def tearDown(self): self.f.close()

    def start_with_commit(self):
        self.f.start(); return self.f.commit_candidate("candidate","candidate commit")

    def artifacts(self,status="awaiting_human",verdict="accept",include_result=True,include_validation=True,include_review=True):
        state=relay.current(); run_id="run-0001"; directory=self.f.repo/self.f.cfg["run_root"]/run_id; directory.mkdir(parents=True,exist_ok=True)
        if include_result: relay.write_json(directory/"RESULT.json",result_data())
        if include_validation: relay.write_json(directory/"VALIDATION.json",validation_data())
        if include_review: relay.write_json(directory/"REVIEW.json",detailed_review(verdict))
        state["candidate"].update(status=status,latest_run_id=run_id,current_tip=git_ops.head(self.f.candidate_path())); relay.save_current(state)
        return directory

    def collect(self): return candidate_reporting.collect(self.f.repo,relay.current(),self.f.cfg,git_ops)

    def test_no_active_candidate(self):
        data,structural=self.collect(); self.assertTrue(structural); self.assertIn("no active candidate",data["errors"])

    def test_candidate_before_first_run(self):
        self.f.start(); data,structural=self.collect(); self.assertFalse(structural); self.assertIsNone(data["executor"]); self.assertEqual(["candidate-run","candidate-abandon"],data["available_actions"])

    def test_executor_completed_validation_absent(self):
        self.start_with_commit(); self.artifacts(status="executed",include_validation=False,include_review=False); data,_=self.collect(); self.assertIsNotNone(data["executor"]); self.assertIsNone(data["validation"])

    def test_validation_present_review_absent(self):
        self.start_with_commit(); self.artifacts(status="validated",include_review=False); data,_=self.collect(); self.assertEqual("pass",data["validation"]["status"]); self.assertIsNone(data["review"])

    def test_complete_accept_review(self):
        self.start_with_commit(); self.artifacts(); data,_=self.collect(); self.assertEqual("accept",data["review"]["verdict"]); self.assertEqual("candidate-accept",data["available_actions"][0])

    def test_accept_with_corrections_actions(self):
        self.start_with_commit(); self.artifacts(verdict="accept_with_corrections"); data,_=self.collect(); self.assertEqual("candidate-correct",data["available_actions"][0]); self.assertTrue(any("override-review" in x for x in data["available_actions"]))

    def test_rejected_review_actions(self):
        self.start_with_commit(); self.artifacts(verdict="reject"); data,_=self.collect(); self.assertEqual(["candidate-correct","candidate-abandon"],data["available_actions"])

    def test_malformed_optional_json_is_partial(self):
        self.start_with_commit(); directory=self.artifacts(include_validation=False,include_review=False); (directory/"RESULT.json").write_text("{")
        data,structural=self.collect(); self.assertFalse(structural); self.assertIsNone(data["executor"]); self.assertTrue(any("malformed RESULT" in x for x in data["errors"]))

    def test_git_tip_authoritative_over_model_result(self):
        tip=self.start_with_commit(); self.artifacts(); data,_=self.collect(); self.assertEqual(tip,data["git"]["tip"]); self.assertNotIn("model-bogus-hash",data["git"]["tip"])

    def test_dirty_candidate_worktree_displayed(self):
        self.f.start(); (self.f.candidate_path()/"math.txt").write_text("dirty\n"); data,_=self.collect(); self.assertFalse(data["git"]["clean"]); self.assertIn("DIRTY",candidate_reporting.render(data))

    def test_json_output_is_only_json(self):
        self.start_with_commit(); self.artifacts(); data,_=self.collect(); stream=io.StringIO(); candidate_reporting.print_report(data,as_json=True,stream=stream)
        parsed=json.loads(stream.getvalue()); self.assertEqual(data["git"]["tip"],parsed["git"]["tip"]); self.assertFalse(stream.getvalue().startswith("Candidate\n"))

    def test_full_includes_claims_and_corrections(self):
        self.start_with_commit(); self.artifacts(); text=candidate_reporting.render(self.collect()[0],full=True)
        for marker in ("EVIDENCE-MARKER","SCOPE-CORRECTION-MARKER","STRATEGIC-MARKER","NEXT-HANDOFF-MARKER"): self.assertIn(marker,text)
        self.assertNotIn("RAW-LOG-MARKER",text)

    def test_default_omits_large_details(self):
        self.start_with_commit(); self.artifacts(); text=candidate_reporting.render(self.collect()[0])
        for marker in ("EVIDENCE-MARKER","SCOPE-CORRECTION-MARKER","STRATEGIC-MARKER","EXECUTOR-SUMMARY-MARKER"): self.assertNotIn(marker,text)

    def test_diff_uses_accepted_branch_to_candidate(self):
        self.start_with_commit(); self.artifacts(); stream=io.StringIO()
        with contextlib.redirect_stdout(stream): code=relay.candidate_report(args(diff=True,allow_large_diff=True))
        self.assertEqual(0,code); self.assertIn("diff --git a/math.txt b/math.txt",stream.getvalue())

    def test_large_diff_guard(self):
        self.start_with_commit(); self.artifacts(); self.f.cfg["review_diff_limit_bytes"]=1; stream=io.StringIO()
        with contextlib.redirect_stdout(stream): code=relay.candidate_report(args(diff=True))
        self.assertEqual(1,code); self.assertIn("--allow-large-diff",stream.getvalue())

    def test_watch_exits_when_phase_finishes(self):
        active={"candidate":{"executor_active":True,"reviewer_active":False},"git":{},"executor":None,"validation":None,"review":None,"available_actions":[],"errors":[]}
        done={**active,"candidate":{"executor_active":False,"reviewer_active":False}}
        sequence=iter([(active,False),(done,False)])
        with mock.patch.object(candidate_reporting.time,"sleep") as sleep, contextlib.redirect_stdout(io.StringIO()): code=candidate_reporting.watch(lambda:next(sequence),interval=2)
        self.assertEqual(0,code); sleep.assert_called_once_with(2)

    def test_automatic_reporting_after_validation(self):
        self.start_with_commit(); self.artifacts(status="executed",include_validation=False,include_review=False)
        with mock.patch.object(relay.validation,"run_all",return_value=validation_data()), mock.patch.object(relay,"automatic_report") as report: relay.validate_candidate(None)
        report.assert_called_once()

    def test_all_successful_candidate_phases_share_renderer(self):
        source=Path(relay.__file__).read_text()
        for function in ("candidate_run","validate_candidate","review_candidate","candidate_correct"):
            body=source.split(f"def {function}(",1)[1].split("\ndef ",1)[0]
            self.assertIn("automatic_report()",body)

    def test_action_recommendations_match_statuses(self):
        expected={"ready":"candidate-run","needs_correction":"candidate-run","executed":"validate","validation_passed":"review",
                  "validation_failed":"review-failed-validation","validation_error":"review-failed-validation"}
        for status,first in expected.items(): self.assertEqual(first,candidate_reporting.available_actions(status,None)[0])

    def test_report_performs_no_writes(self):
        self.start_with_commit(); self.artifacts(); state_path=relay.local_state_path(); before=state_path.read_bytes(); status=git(self.f.repo,"status","--porcelain")
        self.collect(); self.assertEqual(before,state_path.read_bytes()); self.assertEqual(status,git(self.f.repo,"status","--porcelain"))

    def test_report_calls_no_model_backend(self):
        self.start_with_commit(); self.artifacts()
        with mock.patch.object(relay.backends,"run_codex") as codex, mock.patch.object(relay.backends,"run_openai_review") as reviewer, contextlib.redirect_stdout(io.StringIO()): relay.candidate_report(args())
        codex.assert_not_called(); reviewer.assert_not_called()


if __name__=="__main__": unittest.main()
