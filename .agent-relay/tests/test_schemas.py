import json, unittest
from pathlib import Path
class SchemaTests(unittest.TestCase):
    def test_all_schemas_parse_and_close_top_level(self):
        for p in (Path(__file__).resolve().parents[1]/"schemas").glob("*.json"):
            data=json.loads(p.read_text());self.assertEqual(data["type"],"object");self.assertFalse(data["additionalProperties"])
