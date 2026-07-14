#!/usr/bin/env python3
"""Independent assertions for the 44-event selector-pair proxy receipt."""

import itertools
import json
from pathlib import Path

from exhaustive_boundary_properness_audit import OMEGA, UNIV, labelled_blocks, unique_extreme


HERE = Path(__file__).parent
receipt = json.loads((HERE / "five_block_selector_pair_proxy.json").read_text())
chosen = ("A00", "A01", "C01", "A10", "A11")
all_blocks = labelled_blocks()
blocks = {name: all_blocks[name] for name in chosen}
carrier = set().union(*blocks.values())
ordered = sorted(carrier, key=lambda x: (len(x), sorted(x)))
ids = {x: i for i, x in enumerate(ordered)}


def lower(x, y):
    candidates = [z for z in carrier if z <= x and z <= y]
    maximal = [z for z in candidates if not any(z < w for w in candidates)]
    assert len(maximal) == 1
    return maximal[0]


atoms = {x for x in carrier if x and not any(y and y < x for y in carrier)}
selectors = sorted(carrier - {frozenset(), UNIV} - atoms, key=ids.get)
support = {x: frozenset(name for name in chosen if x in blocks[name]) for x in carrier}
qualifiers = []
coherent = proper = distinct = 0
for e, f in itertools.combinations(selectors, 2):
    common = support[e] & support[f]
    regions = (lower(e, f), lower(e, UNIV - f), lower(UNIV - e, f))
    t1 = bool(e & f)
    t2 = bool(common) and support[e] != support[f] and not (
        support[e] <= support[f] or support[f] <= support[e])
    t3 = bool(common) and all(regions)
    coherent += t1
    distinct += t2
    proper += t3
    if t1 and t2 and t3:
        qualifiers.append((ids[e], ids[f]))

counts = receipt["counts"]
assert len(carrier) == counts["events"] == 44
assert len(atoms) == counts["lattice_atoms"] == 10
assert len(selectors) == counts["non_atomic_selectors"] == 32
assert len(list(itertools.combinations(selectors, 2))) == counts["unordered_pairs"] == 496
assert coherent == counts["jointly_point_coherent_pairs"] == 485
assert proper == counts["proper_three_region_pairs"] == 135
assert distinct == counts["distinct_overlapping_nonnested_support_pairs"] == 28
assert len(qualifiers) == counts["qualifying_two_coordinate_proxies"] == 24
assert qualifiers == [tuple(row["pair"]) for row in receipt["qualifying_pairs"]]
assert all(receipt["checks"].values())
print("verified five-block-selector-pair-proxy-v1: 44 events, 496 pairs, 24 qualifiers")
