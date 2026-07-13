#!/usr/bin/env python3
"""Independent verifier for seven_block_two_edge_pair_schema.json."""

import json
from pathlib import Path

here = Path(__file__).parent
s = json.loads((here / "seven_block_skeleton.json").read_text())
c = json.loads((here / "seven_block_two_edge_pair_schema.json").read_text())
meet, comp = s["meet"], s["complement"]
blocks = {b["name"]: set(b["events"]) for b in s["blocks"]}

for record in c["orbits"]:
    e, f = record["pair"]
    common = sorted(name for name, events in blocks.items() if e in events and f in events)
    assert common == record["common_blocks"]
    expected = {"shared": meet[e][f], "left_private": meet[e][comp[f]],
                "right_private": meet[comp[e]][f], "outside": meet[comp[e]][comp[f]]}
    assert all(x["regions"] == expected for x in record["boolean_regions_in_each_common_block"])
    assert record["induced_common_block_data_equal"]
    assert record["inequivalent_quotient_edges"] == 1

controls = {x["name"]: x for x in c["finite_controls"]}
assert controls["duplicate"]["relation"] == controls["duplicate"]["edge_relations"][0]
assert controls["duplicate"]["edge_logically_implied_by_others"] == [True, True]
assert controls["nested"]["edge_logically_implied_by_others"] == [True, False]
assert controls["jointly_generating"]["relation_size"] == 4
assert controls["transverse_proper"]["edge_logically_implied_by_others"] == [False, False]
assert all(c["checks"].values())
print("PASS: O2/O3 repeat one intrinsic four-region datum; finite controls checked")
