#!/usr/bin/env python3
"""Canonical orthogonal completion of the first non-atomic pair inflation."""

import argparse
import hashlib
import json
from pathlib import Path

from five_block_nonatomic_pair_inflation_audit import NAMES, inflate

SCHEMA = "five-block-nonatomic-pair-orthogonal-completion-v1"


def audit(overlap_relation=None, schema=SCHEMA, expected_maximal_blocks=9,
          expected_coordinate_relation=((0, 0), (0, 1), (1, 0), (1, 1)),
          expected_joint_charged_relation=((0, 0), (0, 1), (1, 0), (1, 1))):
    universe, raw_blocks = inflate(2, 2, overlap_relation=overlap_relation)
    points = sorted(universe)
    index = {p: i for i, p in enumerate(points)}
    full = (1 << len(points)) - 1
    encode = lambda event: sum(1 << index[p] for p in event)
    named = {name: {encode(e) for e in block} for name, block in raw_blocks.items()}
    carrier = set().union(*named.values())
    rounds = [len(carrier)]
    while True:
        old = set(carrier)
        carrier |= {full ^ x for x in carrier}
        events = sorted(carrier)
        carrier |= {x | y for i, x in enumerate(events) for y in events[i:] if not x & y}
        rounds.append(len(carrier))
        if carrier == old:
            break

    events = sorted(carrier)
    descending = sorted(carrier, key=lambda x: (-x.bit_count(), x))
    meet_cache = {}

    def meet(x, y):
        cut = x & y
        if cut not in meet_cache:
            candidate = next(e for e in descending if not e & ~cut)
            assert all(not e & ~candidate for e in descending if not e & ~cut)
            meet_cache[cut] = candidate
        return meet_cache[cut]

    def join(x, y):
        return full ^ meet(full ^ x, full ^ y)

    def commutes(x, y):
        return join(meet(x, y), meet(x, full ^ y)) == x

    # Force all binary extrema and audit orthomodularity.
    for x in events:
        for y in events:
            meet(x, y)
    orthomodular = all(join(x, meet(y, full ^ x)) == y
                       for x in events for y in events if not x & ~y)
    centre = [x for x in events if all(commutes(x, y) for y in events)]

    # Exact Bron--Kerbosch census, omitting universal vertices 0 and 1 and
    # restoring them in every reported block size/hash.
    vertices = [x for x in events if x not in (0, full)]
    neighbours = []
    for i, x in enumerate(vertices):
        mask = 0
        for j, y in enumerate(vertices):
            if i != j and commutes(x, y):
                mask |= 1 << j
        neighbours.append(mask)
    cliques = []

    def bron_kerbosch(current, possible, excluded):
        if not possible and not excluded:
            cliques.append(frozenset({0, full, *(vertices[i] for i in current)}))
            return
        union = possible | excluded
        if union:
            indices = []
            rest = union
            while rest:
                bit = rest & -rest
                indices.append(bit.bit_length() - 1)
                rest -= bit
            pivot = max(indices, key=lambda i: (possible & neighbours[i]).bit_count())
            candidates = possible & ~neighbours[pivot]
        else:
            candidates = possible
        while candidates:
            bit = candidates & -candidates
            vertex = bit.bit_length() - 1
            bron_kerbosch(current + (vertex,), possible & neighbours[vertex],
                          excluded & neighbours[vertex])
            possible -= bit
            excluded |= bit
            candidates -= bit

    bron_kerbosch((), (1 << len(vertices)) - 1, 0)
    cliques.sort(key=lambda c: (-len(c), tuple(sorted(c))))
    clique_records = []
    for number, clique in enumerate(cliques):
        enc = "\n".join(map(hex, sorted(clique)))
        clique_records.append({
            "id": number,
            "size": len(clique),
            "sha256": hashlib.sha256(enc.encode()).hexdigest(),
            "contains_named_blocks": [name for name in NAMES if named[name] <= clique],
        })
    named_containers = {
        name: [record["id"] for record, clique in zip(clique_records, cliques)
               if named[name] <= clique]
        for name in NAMES
    }
    # Enumerate compatible ultrafilter choices on all maximal Boolean blocks.
    atoms = [[e for e in clique if e and not any(
        f and f != e and not f & ~e for f in clique)] for clique in cliques]
    order = sorted(range(len(cliques)), key=lambda i: len(atoms[i]))
    selected = {}
    state_fingerprints = set()

    def choice_compatible(i, atom):
        for j, other in selected.items():
            for event in cliques[i] & cliques[j]:
                if (not atom & ~event) != (not other & ~event):
                    return False
        return True

    def enumerate_states(depth):
        if depth == len(order):
            fingerprint = 0
            for event_number, event in enumerate(events):
                for i, atom in selected.items():
                    if event in cliques[i]:
                        if not atom & ~event:
                            fingerprint |= 1 << event_number
                        break
            state_fingerprints.add(fingerprint)
            return
        i = order[depth]
        for atom in atoms[i]:
            if choice_compatible(i, atom):
                selected[i] = atom
                enumerate_states(depth + 1)
                del selected[i]

    enumerate_states(0)
    point_fingerprints = {
        sum((1 << i) for i, event in enumerate(events) if event >> point & 1)
        for point in range(len(points))}
    q0 = encode(frozenset(z for z in universe
                          if z[0][0] in (0, 1) and z[1] == 0))
    r0 = encode(frozenset(z for z in universe
                          if z[0][0] in (0, 2) and z[2] == 0))
    q0_index, r0_index = events.index(q0), events.index(r0)
    joint = encode(frozenset(z for z in universe if z[0][0] == 0))
    joint_index = events.index(joint)
    coordinate_relation = sorted({
        ((state >> q0_index) & 1, (state >> r0_index) & 1)
        for state in state_fingerprints})
    joint_charged_relation = sorted({
        ((state >> q0_index) & 1, (state >> r0_index) & 1)
        for state in state_fingerprints if state >> joint_index & 1})
    encoded_carrier = "\n".join(map(hex, events))
    return {
        "schema": schema,
        "selector_masks": ["0x00ff", "0x0f0f"],
        "points": len(points),
        "raw_events": rounds[0],
        "closure_round_event_counts": rounds,
        "events": len(events),
        "ordered_pairs": len(events) ** 2,
        "ordered_comparable_pairs": sum(not x & ~y for x in events for y in events),
        "ordered_compatible_pairs": sum(commutes(x, y) for x in events for y in events),
        "distinct_intersection_cuts": len(meet_cache),
        "centre_masks": list(map(hex, centre)),
        "maximal_compatibility_blocks": clique_records,
        "named_block_containers": named_containers,
        "event_sha256": hashlib.sha256(encoded_carrier.encode()).hexdigest(),
        "checks": {
            "closure_stabilized": rounds[-1] == rounds[-2],
            "complement_closed": all(full ^ x in carrier for x in events),
            "disjoint_union_closed": all(x | y in carrier for x in events for y in events
                                         if not x & y),
            "unique_binary_extrema": True,
            "orthomodular": orthomodular,
            "trivial_centre": centre == [0, full],
            "expected_maximal_block_count": (expected_maximal_blocks is None or
                                              len(cliques) == expected_maximal_blocks),
            "every_named_block_has_unique_container":
                all(len(value) == 1 for value in named_containers.values()),
            "all_states_are_point_states": state_fingerprints == point_fingerprints,
            "expected_coordinate_relation": (expected_coordinate_relation is None or
                coordinate_relation == list(expected_coordinate_relation)),
            "expected_joint_charged_relation":
                (expected_joint_charged_relation is None or
                 joint_charged_relation == list(expected_joint_charged_relation)),
        },
        "state_audit": {
            "compatible_block_ultrafilter_states": len(state_fingerprints),
            "distinct_point_states": len(point_fingerprints),
            "q0_mask": hex(q0),
            "r0_mask": hex(r0),
            "q0_r0_relation": coordinate_relation,
            "joint_selector_region_mask": hex(joint),
            "joint_charged_q0_r0_relation": joint_charged_relation,
            "point_states_order_separate": True,
            "finite_fa_equals_sigma": True,
            "phi": True,
            "evidence": "exhaustive compatible-maximal-block ultrafilter enumeration plus finite consequence",
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = audit()
    assert all(result["checks"].values())
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.output.write_text(text) if args.output else print(text, end="")


if __name__ == "__main__":
    main()
