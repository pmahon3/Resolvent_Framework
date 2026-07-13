import json
import socket
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import claim_ledger, git_ops, packet_builder, relay
from test_lifecycle import Fixture, review_data


class HardeningTests(unittest.TestCase):
    def setUp(self): self.f = Fixture()
    def tearDown(self): self.f.close()

    def executed_candidate(self):
        self.f.start(); self.f.commit_candidate("candidate", "candidate")
        state=relay.current(); directory=self.f.repo/self.f.cfg["run_root"]/"run-0001"; directory.mkdir(parents=True)
        relay.write_json(directory/"RESULT.json", {"outcome":"SUCCESS"})
        state["candidate"].update(status="executed", latest_run_id="run-0001")
        relay.save_current(state); return directory

    def test_failed_validation_has_distinct_state_and_blocks_ordinary_review(self):
        self.executed_candidate()
        failed={"status":"fail","changed_files":["math.txt"],"commands":[{"exit_code":1}],"commit":"tip"}
        with mock.patch.object(relay.validation,"run_all",return_value=failed): relay.validate_candidate(None)
        self.assertEqual("validation_failed", relay.current()["candidate"]["status"])
        with self.assertRaisesRegex(RuntimeError,"validation_passed"): relay.review_candidate(SimpleNamespace(allow_large_packet=False))

    def test_validator_exception_is_validation_error(self):
        directory=self.executed_candidate()
        with mock.patch.object(relay.validation,"run_all",side_effect=OSError("validator unavailable")): relay.validate_candidate(None)
        self.assertEqual("validation_error", relay.current()["candidate"]["status"])
        self.assertEqual("error", relay.load_json(directory/"VALIDATION.json")["status"])

    def test_atomic_write_preserves_previous_file_if_replace_fails(self):
        path=self.f.repo/"atomic.json"; path.write_text('{"old": true}\n')
        with mock.patch.object(relay.os,"replace",side_effect=OSError("injected")):
            with self.assertRaisesRegex(OSError,"injected"): relay.write_json(path,{"new":True})
        self.assertEqual({"old":True},json.loads(path.read_text()))

    def test_repository_lock_rejects_concurrent_state_change(self):
        with relay.repository_lock():
            with self.assertRaisesRegex(RuntimeError,"another state-changing"):
                with relay.repository_lock(): pass

    def test_stale_executor_phase_recovers_from_git_and_result(self):
        directory=self.executed_candidate(); state=relay.current()
        state["candidate"].update(status="executing", phase={"name":"executor","pid":99999999,"hostname":socket.gethostname(),"started_at":"old","candidate_head":state["candidate"]["initial_base"],"packet_sha256":None})
        relay.save_current(state); relay.recover_candidate(None)
        self.assertEqual("executed",relay.current()["candidate"]["status"])
        self.assertTrue((directory/"RESULT.json").exists())

    def test_integration_recovers_if_merge_was_interrupted_after_control_prepare(self):
        self.f.start(); self.f.commit_candidate("candidate","candidate"); self.f.awaiting()
        original=relay.git_ops.run; failed={"value":False}
        def interrupt_merge(args,cwd,**kwargs):
            if args[:2]==["git","merge"] and not failed["value"]:
                failed["value"]=True; raise RuntimeError("injected before ref move")
            return original(args,cwd,**kwargs)
        with mock.patch.object(relay.validation,"run_all",return_value={"status":"pass","changed_files":[],"commands":[]}), mock.patch.object(relay.git_ops,"run",side_effect=interrupt_merge):
            with self.assertRaisesRegex(RuntimeError,"injected"): relay.candidate_accept(SimpleNamespace(override_review=False,reason=None))
        self.assertEqual("integrating_prepared",relay.current()["candidate"]["status"])
        relay.recover_candidate(None)
        self.assertIsNone(relay.current()["candidate"])

    def test_integration_recovers_after_accepted_ref_move(self):
        self.f.start(); self.f.commit_candidate("candidate","candidate"); self.f.awaiting()
        with mock.patch.object(relay.validation,"run_all",return_value={"status":"pass","changed_files":[],"commands":[]}), mock.patch.object(relay,"finalize_integration",side_effect=RuntimeError("injected after ref move")):
            with self.assertRaisesRegex(RuntimeError,"injected"): relay.candidate_accept(SimpleNamespace(override_review=False,reason=None))
        self.assertEqual("control_committed",relay.current()["candidate"]["status"])
        relay.recover_candidate(None)
        self.assertIsNone(relay.current()["candidate"])

    def test_abandon_refuses_half_integrated_candidate(self):
        self.f.start(); state=relay.current(); state["candidate"]["status"]="integrating_prepared"; relay.save_current(state)
        with self.assertRaisesRegex(RuntimeError,"candidate-recover"): relay.candidate_abandon(SimpleNamespace(yes=True))

    def test_claim_ledger_replaces_canonical_fields_without_append_sections(self):
        ledger=claim_ledger.initial_ledger(accepted_commit="base")
        review=review_data(); review["state_patch"]["banked_results_add"]=["A new hand proof."]
        for run in ("run-1","run-2"): ledger=claim_ledger.apply_review_patch(ledger,review,mathematical_tip=run,run_id=run)
        rendered=claim_ledger.render(ledger)
        self.assertEqual(1,rendered.count("## Current open gate"))
        self.assertEqual(1,rendered.count("A new hand proof."))

    def test_truncated_diff_is_file_complete_and_forces_human_review(self):
        self.f.start(); self.f.commit_candidate("x"*2000,"large candidate")
        state=relay.current(); directory=self.f.repo/self.f.cfg["run_root"]/"run-0001"; directory.mkdir(parents=True)
        relay.write_json(directory/"RESULT.json", {"outcome":"SUCCESS","uncertainties":[],"possible_overstatements":[]})
        relay.write_json(directory/"VALIDATION.json", {"status":"pass","changed_files":["math.txt"],"commands":[]})
        state["candidate"].update(status="validation_passed",latest_run_id="run-0001"); relay.save_current(state)
        self.f.cfg["review_diff_limit_bytes"]=20
        def reviewer(_packet, command, _events):
            relay.write_json(Path(command[command.index("--output-last-message")+1]), review_data())
        with mock.patch.object(relay.backends,"run_codex",side_effect=reviewer):
            relay.review_candidate(SimpleNamespace(allow_large_packet=False))
        review=relay.load_json(directory/"REVIEW.json")
        self.assertEqual("human_review",review["verdict"])
        self.assertIn("omitted",review["requires_human_review_reason"])


class PacketBoundaryTests(unittest.TestCase):
    def test_bounded_diff_never_includes_partial_file(self):
        first="diff --git a/a b/a\n"+"a"*20+"\n"
        second="diff --git a/b b/b\n"+"b"*200+"\n"
        selected,included,omitted=packet_builder.bounded_diff(first+second,len(first.encode()))
        self.assertEqual(first+"\n[DIFF TRUNCATED AT FILE BOUNDARIES]\n",selected)
        self.assertEqual(["a"],included); self.assertEqual(["b"],omitted)


if __name__ == "__main__": unittest.main()
