#!/usr/bin/env python3
"""Audit the minimal two-edge transverse Boolean-overlap candidate.

This is a finite four-point control.  It does not construct an infinite
sigma-complete OML and does not classify non-generating transverse overlaps.
"""

import argparse
import itertools
import json
from pathlib import Path


SCHEMA = "four-point-transverse-overlap-v1"
POINTS = frozenset(range(4))
P = (frozenset({0, 1}), frozenset({2, 3}))
Q = (frozenset({0, 2}), frozenset({1, 3}))
R = (frozenset({0, 3}), frozenset({1, 2}))


def powerset(points):
    return {frozenset(c) for n in range(len(points) + 1)
            for c in itertools.combinations(points, n)}


def generated_boolean_algebra(generators):
    algebra = {frozenset(), POINTS, *generators}
    while True:
        old = set(algebra)
        algebra |= {POINTS - x for x in old}
        algebra |= {x & y for x in old for y in old}
        algebra |= {x | y for x in old for y in old}
        if algebra == old:
            return algebra


def bit(partition, point):
    return 0 if point in partition[0] else 1


def relation(left_partitions, right_partitions):
    return sorted([u, v] for u in POINTS for v in POINTS
                  if all(bit(lp, u) == bit(rp, v)
                         for lp, rp in zip(left_partitions, right_partitions)))


def serialise_sets(items):
    return sorted([sorted(x) for x in items], key=lambda x: (len(x), x))


def build():
    full = powerset(POINTS)
    left_generated = generated_boolean_algebra([*P, *Q])
    right_generated = generated_boolean_algebra([*P, *R])
    edges = [relation([P], [P]), relation([Q], [R])]
    both = relation([P, Q], [P, R])
    latticehood = all((x & y) in full and (x | y) in full for x in full for y in full)
    order_separation = all(x <= y or any(point in x and point not in y for point in POINTS)
                           for x in full for y in full)
    gates = {
        "latticehood": latticehood,
        "sigma_completeness": latticehood,  # every family is finite here
        "maximal_boolean_blocks": 1,
        "centre_size": len(full),  # all pairs in a Boolean algebra are compatible
        "two_valued_states": len(POINTS),
        "state_extension": len(both) == len(POINTS),
        "order_separation": order_separation,
        "intended_two_distinct_blocks": False,
        "essential_irreducibility": len(full) == 2,
    }
    return {
        "schema": SCHEMA,
        "scope": "finite four-point jointly-generating control; no infinite OML or general transverse-overlap classification",
        "candidate": {
            "left_partitions": [serialise_sets(P), serialise_sets(Q)],
            "right_partitions": [serialise_sets(P), serialise_sets(R)],
            "distinct_event_families": True,
            "each_overlap_proper": True,
            "left_generated_algebra": serialise_sets(left_generated),
            "right_generated_algebra": serialise_sets(right_generated),
            "full_boolean_algebra": serialise_sets(full),
            "jointly_generate_endpoints": left_generated == full and right_generated == full,
        },
        "state_relation": {
            "individual_edge_relations": edges,
            "combined_relation": both,
            "combined_relation_size": len(both),
            "functional_bijection": sorted(u for u, _ in both) == list(range(4))
                                    and sorted(v for _, v in both) == list(range(4)),
            "permutation_left_to_right": [next(v for x, v in both if x == u)
                                           for u in range(4)],
        },
        "collapsed_realisation_gates": gates,
        "checks": {
            "edges_are_distinct": edges[0] != edges[1],
            "neither_edge_implies_the_other": not (set(map(tuple, edges[0])) <= set(map(tuple, edges[1])))
                                               and not (set(map(tuple, edges[1])) <= set(map(tuple, edges[0]))),
            "combined_relation_is_permutation_graph": len(both) == 4,
            "joint_generation_forces_block_collapse": left_generated == full and right_generated == full,
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    text = json.dumps(build(), indent=2, sort_keys=True) + "\n"
    args.output.write_text(text) if args.output else print(text, end="")
