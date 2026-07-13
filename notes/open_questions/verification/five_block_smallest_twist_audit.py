#!/usr/bin/env python3
"""Enumerate P(2) automorphism labels on the inflated three-block triangle.

This is a bounded cocycle/gauge census, not a classification of larger
interfaces, correspondences, or concrete carrier twists.
"""

import argparse
import itertools
import json
from pathlib import Path


SCHEMA = "five-block-smallest-p2-twist-v1"
VERTICES = ("A00", "A01", "C01")
EDGES = ((0, 1), (1, 2), (2, 0))


def gauge_transform(labels, gauges):
    # Aut(P(2)) = Z/2, so inverse and composition are both xor.
    return tuple(labels[i] ^ gauges[u] ^ gauges[v]
                 for i, (u, v) in enumerate(EDGES))


def build():
    cases = []
    for labels in itertools.product(range(2), repeat=3):
        holonomy = labels[0] ^ labels[1] ^ labels[2]
        gauges_to_identity = [
            gauges for gauges in itertools.product(range(2), repeat=3)
            if gauge_transform(labels, gauges) == (0, 0, 0)
        ]
        cases.append({
            "edge_labels": list(labels),
            "swap_parity": sum(labels) % 2,
            "holonomy": "swap" if holonomy else "identity",
            "faithful_cocycle": holonomy == 0,
            "gauge_trivial": bool(gauges_to_identity),
            "fixed_subalgebra_events_if_closed": 2 if holonomy else 4,
        })

    faithful = [case for case in cases if case["faithful_cocycle"]]
    collapsed = [case for case in cases if not case["faithful_cocycle"]]
    assert len(cases) == 8
    assert len(faithful) == len(collapsed) == 4
    assert all(case["gauge_trivial"] for case in faithful)
    assert all(not case["gauge_trivial"] for case in collapsed)
    assert all(case["fixed_subalgebra_events_if_closed"] == 2
               for case in collapsed)
    return {
        "schema": SCHEMA,
        "scope": (
            "all Z/2 automorphism labels on the P(2) interval shared by "
            "A00,A01,C01; no larger-interface or concrete-carrier classification"
        ),
        "vertices": list(VERTICES),
        "edges": [[VERTICES[u], VERTICES[v]] for u, v in EDGES],
        "summary": {
            "labelled_cases": len(cases),
            "faithful_cocycle_cases": len(faithful),
            "nonfaithful_swap_holonomy_cases": len(collapsed),
            "genuine_faithful_twists": sum(
                case["faithful_cocycle"] and not case["gauge_trivial"]
                for case in cases
            ),
        },
        "cases": cases,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    text = json.dumps(build(), indent=2, sort_keys=True) + "\n"
    args.output.write_text(text) if args.output else print(text, end="")


if __name__ == "__main__":
    main()
