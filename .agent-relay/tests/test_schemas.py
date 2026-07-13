import json, unittest
from pathlib import Path
class SchemaTests(unittest.TestCase):
    def test_all_schemas_parse_and_close_top_level(self):
        for p in (Path(__file__).resolve().parents[1]/"schemas").glob("*.json"):
            data=json.loads(p.read_text());self.assertEqual(data["type"],"object");self.assertFalse(data["additionalProperties"])
    def test_current_status_is_closed_enum(self):
        data=json.loads((Path(__file__).resolve().parents[1]/"schemas/current-state.schema.json").read_text())
        self.assertEqual(["uninitialized","initialized"],data["properties"]["status"]["enum"])
        candidate=data["properties"]["candidate"]["oneOf"][1]
        self.assertEqual(["ready","executing","executed","validated","awaiting_human","needs_correction"],candidate["properties"]["status"]["enum"])
    def test_finalized_ledger_decision_is_closed_enum(self):
        data=json.loads((Path(__file__).resolve().parents[1]/"schemas/ledger-entry.schema.json").read_text())
        self.assertEqual(["accept","reject"],data["properties"]["human_decision"]["enum"])
        self.assertIn("review_override",data["properties"])
