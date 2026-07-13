#!/usr/bin/env python3
"""Audit the smallest binary transverse pattern with proper joint closure.

The finite candidate is the concrete 48-element OML MO2 x P(3).  The
calculation has no infinite or general-classification scope.
"""

import argparse
import itertools
import json
from pathlib import Path


SCHEMA = "five-atom-proper-joint-closure-v2"
UNIVERSE = frozenset(range(7))
TAIL = frozenset({4, 5, 6})
MO2_BLOCKS = (
    (frozenset({0, 1}), frozenset({2, 3})),
    (frozenset({0, 2}), frozenset({1, 3})),
)


def boolean_block(head_atoms):
    atoms = (*head_atoms, *(frozenset({x}) for x in sorted(TAIL)))
    return {frozenset().union(*(atoms[i] for i in choice))
            for n in range(len(atoms) + 1)
            for choice in itertools.combinations(range(len(atoms)), n)}


def bounds(carrier, x, y, upper):
    candidates = ([z for z in carrier if x <= z and y <= z] if upper else
                  [z for z in carrier if z <= x and z <= y])
    extremal = [z for z in candidates if not any(
        z != w and ((w < z) if upper else (z < w)) for w in candidates)]
    assert len(extremal) == 1
    return extremal[0]


def relation(left_bits, right_bits):
    left = range(5)
    right = range(5)
    return sorted([u, v] for u in left for v in right
                  if all(lb[u] == rb[v] for lb, rb in zip(left_bits, right_bits)))


def build():
    blocks = tuple(boolean_block(pair) for pair in MO2_BLOCKS)
    carrier = blocks[0] | blocks[1]
    overlap = blocks[0] & blocks[1]
    meet = {(x, y): bounds(carrier, x, y, False) for x in carrier for y in carrier}
    join = {(x, y): bounds(carrier, x, y, True) for x in carrier for y in carrier}
    complement = {x: UNIVERSE - x for x in carrier}

    lattice = len(meet) == len(carrier) ** 2 and len(join) == len(carrier) ** 2
    orthomodular = all(not (x <= y) or join[x, meet[complement[x], y]] == y
                          for x in carrier for y in carrier)
    compatible = {(x, y): join[meet[x, y], meet[x, complement[y]]] == x
                  for x in carrier for y in carrier}
    centre = {x for x in carrier if all(compatible[x, y] for y in carrier)}
    cross_noncentral_incompatible = all(
        not compatible[x, y]
        for x in blocks[0] - overlap for y in blocks[1] - overlap
    )
    maximal_blocks = [b for b in blocks
                      if all(compatible[x, y] for x in b for y in b)
                      and all(any(not compatible[x, y] for y in b)
                              for x in carrier - b)]

    # Endpoint labels duplicate cell 00 of the four-point P/Q versus P/R square.
    left_bits = ([0, 0, 0, 1, 1], [0, 0, 1, 0, 1])
    right_bits = ([0, 0, 0, 1, 1], [0, 0, 1, 1, 0])
    edge_relations = [relation([left_bits[i]], [right_bits[i]]) for i in range(2)]
    combined = relation(left_bits, right_bits)
    point_pairs = {(0, 0), (0, 1), (1, 0), (1, 1),
                   (2, 2), (3, 4), (4, 3)}

    # Point evaluations give all compatible pairs of endpoint ultrafilters.
    global_state_vectors = sorted([[int(point in x) for x in sorted(carrier, key=lambda s: (len(s), sorted(s)))]
                                   for point in UNIVERSE])
    order_separation = all(x <= y or any(point in x - y for point in UNIVERSE)
                           for x in carrier for y in carrier)
    state_additivity = all(
        not (x <= complement[y]) or
        all(int(point in join[x, y]) == int(point in x) + int(point in y)
            for point in UNIVERSE)
        for x in carrier for y in carrier
    )

    serial = lambda xs: sorted([sorted(x) for x in xs], key=lambda x: (len(x), x))
    return {
        "schema": SCHEMA,
        "scope": "finite five-atom-endpoint binary transverse candidate; no infinite OML or general transverse classification",
        "minimality_scope": "binary P/Q versus P/R pattern with four nonempty joint cells",
        "candidate": {
            "underlying_points": len(UNIVERSE),
            "carrier_events": len(carrier),
            "endpoint_atoms": [5, 5],
            "endpoint_block_sizes": [len(b) for b in blocks],
            "overlap_size": len(overlap),
            "overlap": serial(overlap),
            "individual_overlap_sizes": [4, 4],
            "joint_overlap_closure_size": len(overlap),
            "joint_closure_proper_in_endpoints": all(overlap < b for b in blocks),
            "left_bits": left_bits,
            "right_bits": right_bits,
        },
        "state_relation": {
            "individual_edge_relations": edge_relations,
            "combined_relation": combined,
            "combined_relation_size": len(combined),
            "degrees_left": [sum(u == x for u, _ in combined) for x in range(5)],
            "degrees_right": [sum(v == x for _, v in combined) for x in range(5)],
            "global_two_valued_states": len(global_state_vectors),
        },
        "completion_gates": {
            "latticehood": lattice,
            "orthomodularity": orthomodular,
            "sigma_completeness": lattice,
            "maximal_boolean_blocks": len(maximal_blocks),
            "centre_size": len(centre),
            "trivial_centre": len(centre) == 2,
            "state_extension": set(map(tuple, combined)) == point_pairs
                               and len(point_pairs) == len(global_state_vectors),
            "two_valued_state_additivity": state_additivity,
            "order_separation": order_separation,
            "phi_tame_by_finiteness": True,
            "sigma_essential_state": False,
        },
        "recorded_hand_conclusions": {
            "five_atoms_are_minimal_in_scope": True,
            "completion_is_mo2_times_p3": True,
        },
        "executable_checks": {
            "edges_are_distinct": edge_relations[0] != edge_relations[1],
            "neither_edge_implies_other": not (set(map(tuple, edge_relations[0])) <= set(map(tuple, edge_relations[1])))
                                          and not (set(map(tuple, edge_relations[1])) <= set(map(tuple, edge_relations[0]))),
            "mixed_completion_is_48_events": len(carrier) == 48,
            "block_and_overlap_sizes_match_hand_product_decomposition":
                len(blocks[0]) == len(blocks[1]) == 32 and len(overlap) == 16,
            "cross_block_noncentral_pairs_incompatible": cross_noncentral_incompatible,
            "centrality_kills_irreducibility": len(centre) == 16,
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    text = json.dumps(build(), indent=2, sort_keys=True) + "\n"
    args.output.write_text(text) if args.output else print(text, end="")
