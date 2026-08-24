#!/usr/bin/env python3
"""Independent consistency checker for the non-atomic pair receipt."""

import itertools
import json
from pathlib import Path


HERE = Path(__file__).parent
skeleton = json.loads((HERE / "seven_block_skeleton.json").read_text())
receipt = json.loads((HERE / "seven_block_nonatomic_pair_schema.json").read_text())
meet, comp, masks = skeleton["meet"], skeleton["complement"], skeleton["event_masks"]
blocks = {b["name"]: set(b["events"]) for b in skeleton["blocks"]}
bottom = 0


def below(x, y):
    return meet[x][y] == x


atoms = {x for x in range(1, len(meet))
         if not any(y not in (bottom, x) and below(y, x) for y in range(len(meet)))}
selectors = sorted(set(range(1, len(meet) - 1)) - atoms)
records = receipt["all_pairs"]
assert [r["pair"] for r in records] == [list(p) for p in itertools.combinations(selectors, 2)]

survivors = []
for record in records:
    e, f = record["pair"]
    se = {name for name, events in blocks.items() if e in events}
    sf = {name for name, events in blocks.items() if f in events}
    regions = (meet[e][f], meet[e][comp[f]], meet[comp[e]][f])
    assert record["supports"] == [sorted(se), sorted(sf)]
    assert record["common_blocks"] == sorted(se & sf)
    assert record["joint_carrier_witness_count"] == (masks[e] & masks[f]).bit_count()
    assert record["boolean_regions"] == {
        "shared_meet": regions[0], "left_only": regions[1], "right_only": regions[2]
    }
    finite_gates = (
        bool(masks[e] & masks[f]),
        bool(se & sf) and not (se <= sf or sf <= se),
        bool(se & sf) and all(x != bottom for x in regions),
        regions[0] not in skeleton["centre"] and len({name for name, events in blocks.items()
                                                     if regions[0] in events}) < len(blocks),
    )
    # Cycle enumeration is certified in the producer; here verify its witness edge by edge.
    cycle = record["minimal_support_cycle"]
    if cycle:
        required = se | sf
        assert required <= set(cycle) and len(cycle) == len(set(cycle)) >= 3
        nontrivial_edges = {(p["left"], p["right"])
                            for p in skeleton["pairwise_intersections"] if p["size"] > 2}
        nontrivial_edges |= {(b, a) for a, b in nontrivial_edges}
        assert all((cycle[i], cycle[(i + 1) % len(cycle)]) in nontrivial_edges
                   for i in range(len(cycle)))
    qualifies = all(finite_gates) and cycle is not None
    assert record["qualifies"] == qualifies
    if qualifies:
        survivors.append(record["pair"])

assert len(records) == 861
assert len(survivors) == 42
assert survivors[0] == [5, 11]
assert receipt["qualifying_pairs"] == [r for r in records if r["qualifies"]]
relation = {tuple(pair) for pair in receipt["minimal_partial_relation_control"]["pairs"]}
assert relation == {(u, v) for u in range(4) for v in range(4) if u // 2 == v // 2}
assert len(relation) == 8
assert {sum((u, v) in relation for v in range(4)) for u in range(4)} == {2}
assert {sum((u, v) in relation for u in range(4)) for v in range(4)} == {2}
print("PASS: 861 pairs independently checked; 42 qualify; minimum is (5,11)")
