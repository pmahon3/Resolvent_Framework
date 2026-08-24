#!/usr/bin/env python3
"""Exhaustive selector-pair proxy census for the 44-event survivor.

This certificate does not construct a two-coordinate inflation.  It answers
the finite prerequisite: which pairs of non-atomic events have distinct,
overlapping propagation supports, admit a common point state, and carry
three nonzero Boolean regions in a common certified maximal block.
"""

import argparse
import itertools
import json
from collections import Counter
from pathlib import Path

from exhaustive_boundary_properness_audit import OMEGA, UNIV, labelled_blocks, unique_extreme


SCHEMA = "five-block-selector-pair-proxy-v1"
KEPT = ("A00", "A01", "C01", "A10", "A11")


def build(_skeleton=None):
    source_blocks = labelled_blocks()
    blocks = {name: set(source_blocks[name]) for name in KEPT}
    events = set().union(*blocks.values())
    ordered = sorted(events, key=lambda x: (len(x), sorted(x)))
    event_id = {event: i for i, event in enumerate(ordered)}
    meet = {(x, y): unique_extreme(events, x, y, False) for x in events for y in events}
    bottom, top = frozenset(), UNIV

    def comp(x):
        return UNIV - x

    def mask(x):
        return sum(1 << i for i, point in enumerate(OMEGA) if point in x)

    def le(x, y):
        return meet[x, y] == x

    atoms = sorted((x for x in events if x != bottom and not any(
        y not in (bottom, x) and le(y, x) for y in events)), key=event_id.get)
    selectors = sorted(events - {bottom, top} - set(atoms), key=event_id.get)
    support = {e: frozenset(name for name, block in blocks.items() if e in block)
               for e in events}

    records = []
    for left, right in itertools.combinations(selectors, 2):
        common = support[left] & support[right]
        regions = (meet[left, right], meet[left, comp(right)], meet[comp(left), right])
        distinct_overlapping_supports = bool(common) and support[left] != support[right] and not (
            support[left] <= support[right] or support[right] <= support[left])
        tests = {
            "joint_point_state": bool(mask(left) & mask(right)),
            "distinct_overlapping_nonnested_supports": distinct_overlapping_supports,
            "three_nonzero_boolean_regions": bool(common) and all(r != bottom for r in regions),
        }
        records.append({
            "pair": [event_id[left], event_id[right]],
            "masks": [mask(left), mask(right)],
            "supports": [sorted(support[left]), sorted(support[right])],
            "common_blocks": sorted(common),
            "regions": [event_id[x] for x in regions],
            "joint_point_witness_count": (mask(left) & mask(right)).bit_count(),
            "tests": tests,
            "qualifies": all(tests.values()),
        })

    qualifying = [r for r in records if r["qualifies"]]
    support_types = Counter(tuple(map(tuple, r["supports"])) for r in qualifying)
    region_types = Counter(tuple(sorted(ordered[x].__len__() for x in r["regions"]))
                           for r in qualifying)
    coherent = [r for r in records if r["tests"]["joint_point_state"]]
    proper = [r for r in records if r["tests"]["three_nonzero_boolean_regions"]]
    distinct = [r for r in records if r["tests"]["distinct_overlapping_nonnested_supports"]]
    return {
        "schema": SCHEMA,
        "scope": "exhaustive finite proxy only; no inflated event algebra is constructed",
        "kept_blocks": list(KEPT),
        "counts": {
            "events": len(events),
            "lattice_atoms": len(atoms),
            "non_atomic_selectors": len(selectors),
            "unordered_pairs": len(records),
            "jointly_point_coherent_pairs": len(coherent),
            "proper_three_region_pairs": len(proper),
            "distinct_overlapping_nonnested_support_pairs": len(distinct),
            "qualifying_two_coordinate_proxies": len(qualifying),
            "qualifying_support_types": len(support_types),
            "qualifying_region_cardinality_types": len(region_types),
        },
        "event_table": [{"id": i, "points": [list(p) for p in sorted(event)]}
                        for i, event in enumerate(ordered)],
        "lattice_atoms": [event_id[x] for x in atoms],
        "non_atomic_selectors": [event_id[x] for x in selectors],
        "qualifying_support_type_counts": [
            {"supports": [list(x) for x in key], "count": value}
            for key, value in sorted(support_types.items())
        ],
        "qualifying_region_cardinality_type_counts": [
            {"region_point_cardinalities": list(key), "count": value}
            for key, value in sorted(region_types.items())
        ],
        "qualifying_pairs": qualifying,
        "checks": {
            "exact_44_event_survivor": len(events) == 44,
            "all_pairs_audited": len(records) == len(selectors) * (len(selectors) - 1) // 2,
            "all_qualifiers_recompute": qualifying == [r for r in records if all(r["tests"].values())],
            "all_regions_are_survivor_events": all(
                0 <= x < len(ordered) for r in records for x in r["regions"]),
        },
        "all_pairs": records,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--skeleton", type=Path,
                        default=Path(__file__).with_name("seven_block_skeleton.json"))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")
