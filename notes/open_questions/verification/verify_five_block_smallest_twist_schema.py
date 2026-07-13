#!/usr/bin/env python3
"""Independently validate the checked-in smallest-twist receipt."""

import itertools
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
receipt = json.loads((HERE / "five_block_smallest_twist_schema.json").read_text())

assert receipt["schema"] == "five-block-smallest-p2-twist-v1"
assert receipt["vertices"] == ["A00", "A01", "C01"]
assert receipt["summary"] == {
    "faithful_cocycle_cases": 4,
    "genuine_faithful_twists": 0,
    "labelled_cases": 8,
    "nonfaithful_swap_holonomy_cases": 4,
}

cases = {tuple(case["edge_labels"]): case for case in receipt["cases"]}
assert set(cases) == set(itertools.product(range(2), repeat=3))
for labels, case in cases.items():
    parity = sum(labels) % 2
    # A Z/2 triangle cocycle is a coboundary exactly when its cycle sum is 0.
    is_coboundary = any(
        all(labels[i] == gauges[u] ^ gauges[v]
            for i, (u, v) in enumerate(((0, 1), (1, 2), (2, 0))))
        for gauges in itertools.product(range(2), repeat=3)
    )
    assert case["swap_parity"] == parity
    assert case["faithful_cocycle"] == (parity == 0)
    assert case["gauge_trivial"] == is_coboundary == (parity == 0)
    assert case["fixed_subalgebra_events_if_closed"] == (4 if parity == 0 else 2)

print("smallest P(2) twist schema verified: 8/8 cases")
