#!/usr/bin/env python3
"""Independently verify the O2/O3 duplicate-edge and finite-control claims.

Stabilizer and support-cycle metadata are outside this verifier's scope.
"""

from collections import Counter
import json
from pathlib import Path

here = Path(__file__).parent
s = json.loads((here / "seven_block_skeleton.json").read_text())
c = json.loads((here / "seven_block_two_edge_pair_schema.json").read_text())
meet, comp = s["meet"], s["complement"]
blocks = {b["name"]: set(b["events"]) for b in s["blocks"]}

assert c["schema"] == "seven-block-two-edge-pair-v1"
assert [(r["orbit"], r["pair"]) for r in c["orbits"]] == [
    ("O2", [5, 51]), ("O3", [15, 45])
]


def generated_sub_oml(generators):
    generated = {0, len(meet) - 1, *generators}
    while True:
        old = set(generated)
        generated |= {comp[x] for x in old}
        generated |= {meet[x][y] for x in old for y in old}
        generated |= {comp[meet[comp[x]][comp[y]]] for x in old for y in old}
        if generated == old:
            return sorted(generated)


for record in c["orbits"]:
    e, f = record["pair"]
    common = sorted(name for name, events in blocks.items() if e in events and f in events)
    assert common == record["common_blocks"]
    expected = {"shared": meet[e][f], "left_private": meet[e][comp[f]],
                "right_private": meet[comp[e]][f], "outside": meet[comp[e]][comp[f]]}
    assert all(x["regions"] == expected for x in record["boolean_regions_in_each_common_block"])
    assert all(set(expected.values()) <= blocks[name] for name in common)
    assert record["generated_sub_oml"] == generated_sub_oml((e, f))
    assert set(record["generated_sub_oml"]) <= set.intersection(*(blocks[name] for name in common))
    assert record["induced_common_block_data_equal"]
    assert record["candidate_quotient_edges"] == 2
    assert record["inequivalent_quotient_edges"] == 1

assert len(c["orbits"][1]["support_cycle"]) < len(c["orbits"][0]["support_cycle"])


def verify_control(control):
    n_left = control["left_ultrafilters"]
    n_right = control["right_ultrafilters"]
    edges = [{tuple(pair) for pair in edge} for edge in control["edge_relations"]]
    relation = set.intersection(*edges)
    recorded = {tuple(pair) for pair in control["relation"]}
    assert recorded == relation
    assert control["relation_size"] == len(relation)

    left_degree = Counter(u for u, _ in relation)
    right_degree = Counter(v for _, v in relation)
    left_sequence = sorted(left_degree.get(u, 0) for u in range(n_left))
    right_sequence = sorted(right_degree.get(v, 0) for v in range(n_right))
    assert control["left_degree_sequence"] == left_sequence
    assert control["right_degree_sequence"] == right_sequence
    rectangle = {(u, v) for u in range(n_left) for v in range(n_right)}
    assert control["rectangular"] == (relation == rectangle)
    assert control["functional_left_to_right"] == all(x == 1 for x in left_sequence)
    assert control["functional_right_to_left"] == all(x == 1 for x in right_sequence)

    implied = []
    for i, edge in enumerate(edges):
        others = set.intersection(*(edges[:i] + edges[i + 1:]))
        implied.append(others <= edge)
    assert control["edge_logically_implied_by_others"] == implied


controls = {x["name"]: x for x in c["finite_controls"]}
assert set(controls) == {"duplicate", "nested", "jointly_generating", "transverse_proper"}
for item in controls.values():
    verify_control(item)
assert controls["duplicate"]["relation"] == controls["duplicate"]["edge_relations"][0]
assert controls["duplicate"]["edge_logically_implied_by_others"] == [True, True]
assert controls["nested"]["edge_logically_implied_by_others"] == [True, False]
assert controls["jointly_generating"]["relation_size"] == 4
assert controls["transverse_proper"]["edge_logically_implied_by_others"] == [False, False]
print("PASS: independently recomputed O2/O3 duplicate-edge core and finite controls")
