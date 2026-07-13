import json, unittest
from pathlib import Path
import sys
SCRIPTS=Path(__file__).resolve().parents[1]/"scripts"; sys.path.insert(0,str(SCRIPTS))
import schema_validation
class SchemaTests(unittest.TestCase):
    def test_all_schemas_parse_and_close_top_level(self):
        for p in (Path(__file__).resolve().parents[1]/"schemas").glob("*.json"):
            data=json.loads(p.read_text());self.assertEqual(data["type"],"object");self.assertFalse(data["additionalProperties"])
    def test_current_status_is_closed_enum(self):
        data=json.loads((Path(__file__).resolve().parents[1]/"schemas/current-state.schema.json").read_text())
        self.assertEqual(["uninitialized","initialized"],data["properties"]["status"]["enum"])
        candidate=data["properties"]["candidate"]["oneOf"][1]
        self.assertEqual(["ready","executing","execution_error","executed","validation_passed","validation_failed","validation_error","reviewing","review_error","awaiting_human","needs_correction","recovery_required","integrating_prepared","control_committed"],candidate["properties"]["status"]["enum"])
    def test_finalized_ledger_decision_is_closed_enum(self):
        data=json.loads((Path(__file__).resolve().parents[1]/"schemas/ledger-entry.schema.json").read_text())
        self.assertEqual(["accept","reject"],data["properties"]["human_decision"]["enum"])
        self.assertIn("review_override",data["properties"])
    def test_tracked_control_artifacts_validate_without_optional_dependencies(self):
        relay=Path(__file__).resolve().parents[1]
        for artifact,schema in (("CURRENT.json","current-state.schema.json"),("CLAIMS.json","claim-ledger.schema.json")):
            schema_validation.validate(json.loads((relay/artifact).read_text()),json.loads((relay/"schemas"/schema).read_text()))
    def test_control_validator_rejects_unknown_properties(self):
        schema={"type":"object","additionalProperties":False,"required":["known"],"properties":{"known":{"type":"string"}}}
        with self.assertRaisesRegex(ValueError,"additional property"): schema_validation.validate({"known":"yes","unknown":1},schema)
