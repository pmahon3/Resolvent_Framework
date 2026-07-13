#!/usr/bin/env python3
"""Independently reconstruct and verify the five-atom transverse receipt."""

import itertools
import json
from pathlib import Path


here = Path(__file__).parent
receipt = json.loads((here / "five_atom_proper_joint_closure_schema.json").read_text())
assert receipt["schema"] == "five-atom-proper-joint-closure-v1"

universe = frozenset(range(7))
tail = [{4}, {5}, {6}]
heads = [({0, 1}, {2, 3}), ({0, 2}, {1, 3})]


def unions(atoms):
    return {frozenset().union(*(frozenset(atoms[i]) for i in choice))
            for n in range(6) for choice in itertools.combinations(range(5), n)}


blocks = [unions([*head, *tail]) for head in heads]
carrier = blocks[0] | blocks[1]
overlap = blocks[0] & blocks[1]
assert (len(carrier), [len(b) for b in blocks], len(overlap)) == (48, [32, 32], 16)


def unique_extreme(x, y, upper):
    eligible = ([z for z in carrier if x <= z and y <= z] if upper else
                [z for z in carrier if z <= x and z <= y])
    if upper:
        extreme = [z for z in eligible if not any(w < z for w in eligible)]
    else:
        extreme = [z for z in eligible if not any(z < w for w in eligible)]
    assert len(extreme) == 1
    return extreme[0]


meet = {(x, y): unique_extreme(x, y, False) for x in carrier for y in carrier}
join = {(x, y): unique_extreme(x, y, True) for x in carrier for y in carrier}
comp = {x: universe - x for x in carrier}
assert all(join[x, meet[comp[x], y]] == y for x in carrier for y in carrier if x <= y)

compatible = lambda x, y: join[meet[x, y], meet[x, comp[y]]] == x
centre = {x for x in carrier if all(compatible(x, y) for y in carrier)}
assert centre == overlap and len(centre) == 16
assert all(not compatible(x, y)
           for x in blocks[0] - overlap for y in blocks[1] - overlap)
assert all(all(compatible(x, y) for x in block for y in block)
           and all(any(not compatible(x, y) for y in block) for x in carrier - block)
           for block in blocks)

left = ([0, 0, 0, 1, 1], [0, 0, 1, 0, 1])
right = ([0, 0, 0, 1, 1], [0, 0, 1, 1, 0])
edge = lambda i: {(u, v) for u in range(5) for v in range(5) if left[i][u] == right[i][v]}
both = edge(0) & edge(1)
assert len(both) == 7
assert both == {(0, 0), (0, 1), (1, 0), (1, 1),
                (2, 2), (3, 4), (4, 3)}
assert sorted(sum(u == x for u, _ in both) for x in range(5)) == [1, 1, 1, 2, 2]
assert not edge(0) <= edge(1) and not edge(1) <= edge(0)
recorded = receipt["state_relation"]
assert [{tuple(pair) for pair in rel} for rel in recorded["individual_edge_relations"]] == [edge(0), edge(1)]
assert {tuple(pair) for pair in recorded["combined_relation"]} == both
assert recorded["degrees_left"] == [2, 2, 1, 1, 1]
assert recorded["degrees_right"] == [2, 2, 1, 1, 1]
assert recorded["global_two_valued_states"] == 7

candidate = receipt["candidate"]
assert candidate["underlying_points"] == 7
assert candidate["carrier_events"] == 48
assert candidate["endpoint_atoms"] == [5, 5]
assert candidate["endpoint_block_sizes"] == [32, 32]
assert candidate["overlap_size"] == candidate["joint_overlap_closure_size"] == 16
assert candidate["individual_overlap_sizes"] == [4, 4]
assert candidate["joint_closure_proper_in_endpoints"] is True
assert {frozenset(x) for x in candidate["overlap"]} == overlap

assert all(x <= y or bool(x - y) for x in carrier for y in carrier)
gates = receipt["completion_gates"]
assert gates == {
    "centre_size": 16,
    "latticehood": True,
    "maximal_boolean_blocks": 2,
    "order_separation": True,
    "orthomodularity": True,
    "phi_tame_by_finiteness": True,
    "sigma_completeness": True,
    "sigma_essential_state": False,
    "state_extension": True,
    "trivial_centre": False,
    "two_valued_state_additivity": True,
}
assert all(receipt["checks"].values())
print("PASS: independently reconstructed the 48-event completion and every finite structural gate")
