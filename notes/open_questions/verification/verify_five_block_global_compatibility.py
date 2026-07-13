#!/usr/bin/env python3
"""Validate the committed arbitrary-base compatibility receipt."""

import json
from pathlib import Path

from five_block_global_compatibility_audit import SCHEMA, build


HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "five_block_global_compatibility_schema.json"


def main():
    committed = json.loads(RECEIPT.read_text())
    assert committed["schema"] == SCHEMA
    assert committed == build()
    checks = committed["checks"]
    assert checks["skeleton_maximal_compatible_families"] == 5
    assert checks["minimal_obstruction_search_bound"] == 5
    assert checks["compatible_family_without_common_named_block"] is None
    assert checks["global_five_block_cover"]
    assert checks["four_region_crosscheck"][
        "pointwise_equals_concrete_compatibility"
    ]
    print("five-block global compatibility receipt verified")


if __name__ == "__main__":
    main()
