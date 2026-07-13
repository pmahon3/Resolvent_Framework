import os, sys, tempfile, unittest
from pathlib import Path
SCRIPTS=Path(__file__).resolve().parents[1]/"scripts"; sys.path.insert(0,str(SCRIPTS))
import backends, packet_builder

class PacketTests(unittest.TestCase):
    def test_deterministic_packet_ordering(self):
        relay=Path(__file__).resolve().parents[1]
        a=packet_builder.executor_packet(relay,"run-0001"); b=packet_builder.executor_packet(relay,"run-0001")
        self.assertEqual(a,b); self.assertLess(a.index("Stable runbook"),a.index("Accepted state")); self.assertLess(a.index("Accepted state"),a.index("Current handoff"))
    def test_state_soft_limit_warning(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"STATE.md";p.write_text("x"*20);self.assertIsNotNone(packet_builder.state_size_warning(p,10))
    def test_fresh_command(self):
        cmd=backends.codex_command(cwd=Path("/tmp/w"),schema=Path("s"),output=Path("o"),sandbox="workspace-write")
        self.assertIn("--ephemeral",cmd);self.assertNotIn("resume",cmd)
    def test_secret_environment_value_rejected(self):
        old=os.environ.get("OPENAI_API_KEY"); os.environ["OPENAI_API_KEY"]="sk-test-do-not-copy"
        try:self.assertRaises(ValueError,packet_builder.reject_secrets,"prefix sk-test-do-not-copy suffix")
        finally:
            if old is None:os.environ.pop("OPENAI_API_KEY",None)
            else:os.environ["OPENAI_API_KEY"]=old
