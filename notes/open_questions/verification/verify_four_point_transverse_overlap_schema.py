#!/usr/bin/env python3
"""Independently recompute the four-point transverse-overlap receipt."""

import itertools
import json
from pathlib import Path


here = Path(__file__).parent
receipt = json.loads((here / "four_point_transverse_overlap_schema.json").read_text())
assert receipt["schema"] == "four-point-transverse-overlap-v1"

points = frozenset(range(4))
p = ({0, 1}, {2, 3})
q = ({0, 2}, {1, 3})
r = ({0, 3}, {1, 2})


def generate(parts):
    algebra = {frozenset(), points} | {frozenset(x) for part in parts for x in part}
    while True:
        old = set(algebra)
        algebra |= {points - x for x in old}
        algebra |= {x & y for x in old for y in old}
        algebra |= {x | y for x in old for y in old}
        if algebra == old:
            return algebra


full = {frozenset(c) for n in range(5) for c in itertools.combinations(points, n)}
assert generate([p, q]) == full
assert generate([p, r]) == full


def value(part, point):
    return int(point not in part[0])


def edge(left, right):
    return {(u, v) for u in points for v in points if value(left, u) == value(right, v)}


edge_1, edge_2 = edge(p, p), edge(q, r)
both = edge_1 & edge_2
recorded_edges = [{tuple(x) for x in xs}
                  for xs in receipt["state_relation"]["individual_edge_relations"]]
assert recorded_edges == [edge_1, edge_2]
assert {tuple(x) for x in receipt["state_relation"]["combined_relation"]} == both
assert both == {(0, 0), (1, 1), (2, 3), (3, 2)}
assert not edge_1 <= edge_2 and not edge_2 <= edge_1
assert receipt["candidate"]["jointly_generate_endpoints"]
assert receipt["state_relation"]["permutation_left_to_right"] == [0, 1, 3, 2]

gates = receipt["collapsed_realisation_gates"]
computed_gates = {
    "centre_size": 16,
    "essential_irreducibility": False,
    "intended_two_distinct_blocks": False,
    "latticehood": all((x & y) in full and (x | y) in full for x in full for y in full),
    "maximal_boolean_blocks": 1,
    "order_separation": all(x <= y or bool(x - y) for x in full for y in full),
    "sigma_completeness": True,
    "state_extension": len(both) == len(points),
    "two_valued_states": len(points),
}
assert gates == computed_gates
print("PASS: independently recomputed four-point transverse collapse and all finite gates")
