#!/usr/bin/env python3
"""Classify residual non-atomic selector pairs in the seven-block skeleton.

This is a finite skeleton certificate, not a completed-inflation theorem.
For a selector e, its propagation support is the set of certified maximal
Boolean blocks containing e.  A common block carries proper information from
both e and f precisely when the three Boolean regions e∧f, e∧f^perp, and
e^perp∧f are nonzero.  This excludes nested and merely orthogonal pairs.
"""

import argparse
import itertools
import json
from pathlib import Path


SCHEMA = "seven-block-nonatomic-pairs-v1"


def canonical_cycle(cycle):
    variants = []
    for oriented in (cycle, list(reversed(cycle))):
        for shift in range(len(cycle)):
            variants.append(tuple(oriented[shift:] + oriented[:shift]))
    return min(variants)


def cycles_containing(graph, required):
    """Simple block cycles containing every propagated support vertex."""
    cycles = set()
    nodes = sorted(graph)
    for length in range(max(3, len(required)), len(nodes) + 1):
        for cycle in itertools.permutations(nodes, length):
            if cycle[0] != min(cycle) or not required <= set(cycle):
                continue
            if all(cycle[(i + 1) % length] in graph[cycle[i]]
                   for i in range(length)):
                cycles.add(canonical_cycle(list(cycle)))
    return sorted(cycles, key=lambda cycle: (len(cycle), cycle))


def build(skeleton):
    meet = skeleton["meet"]
    comp = skeleton["complement"]
    masks = skeleton["event_masks"]
    size = len(meet)
    bottom = next(x for x in range(size) if all(meet[x][y] == x for y in range(size)))
    top = comp[bottom]

    def le(left, right):
        return meet[left][right] == left

    atoms = sorted(x for x in range(size) if x != bottom and not any(
        y not in (bottom, x) and le(y, x) for y in range(size)
    ))
    selectors = sorted(set(range(size)) - {bottom, top} - set(atoms))
    blocks = {block["name"]: set(block["events"])
              for block in skeleton["blocks"]}
    support = {event: {name for name, events in blocks.items() if event in events}
               for event in range(size)}
    incidence = {name: set() for name in blocks}
    for overlap in skeleton["pairwise_intersections"]:
        if overlap["size"] > 2:
            incidence[overlap["left"]].add(overlap["right"])
            incidence[overlap["right"]].add(overlap["left"])

    centre = set(skeleton["centre"])
    pairs = []
    qualifying = []
    for left, right in itertools.combinations(selectors, 2):
        left_support, right_support = support[left], support[right]
        common_blocks = left_support & right_support
        joint_state_witnesses = masks[left] & masks[right]
        overlap = meet[left][right]
        left_only = meet[left][comp[right]]
        right_only = meet[comp[left]][right]
        proper_both = all(region != bottom for region in (overlap, left_only, right_only))
        overlapping_non_nested = bool(common_blocks) and not (
            left_support <= right_support or right_support <= left_support
        )
        required = left_support | right_support
        cycles = cycles_containing(incidence, required)
        shared_fibre_is_forced_central = overlap in centre or support[overlap] == set(blocks)
        tests = {
            "jointly_coherent": bool(joint_state_witnesses),
            "both_selectors_non_atomic": True,
            "supports_overlap_but_are_not_nested": overlapping_non_nested,
            "common_block_has_proper_information_from_both": bool(common_blocks) and proper_both,
            "propagated_support_lies_on_nontrivial_cycle": bool(cycles),
            "no_forced_common_central_fibre": overlap != bottom and not shared_fibre_is_forced_central,
        }
        record = {
            "pair": [left, right],
            "masks": [masks[left], masks[right]],
            "supports": [sorted(left_support), sorted(right_support)],
            "common_blocks": sorted(common_blocks),
            "boolean_regions": {
                "shared_meet": overlap,
                "left_only": left_only,
                "right_only": right_only,
            },
            "joint_carrier_witness_count": joint_state_witnesses.bit_count(),
            "minimal_support_cycle": list(cycles[0]) if cycles else None,
            "tests": tests,
            "qualifies": all(tests.values()),
        }
        pairs.append(record)
        if record["qualifies"]:
            qualifying.append(record)

    smallest = qualifying[0] if qualifying else None
    # Minimal proper-shared-subalgebra control: D has two atoms and A,C each
    # split both D-atoms in two.  Ultrafilters are numbered by (D atom, split).
    target_relation = [[u, v] for u in range(4) for v in range(4)
                       if u // 2 == v // 2]
    return {
        "schema": SCHEMA,
        "scope": "finite incidence/state classification; no coarse substitution is constructed",
        "definitions": {
            "non_atomic_selector": "a nonzero, nontop event that is not a lattice atom",
            "propagation_support": "certified maximal Boolean blocks containing the selector",
            "proper_information_from_both": "e meet f, e meet f^perp, and e^perp meet f are all nonzero",
            "cycle": "a simple nontrivial-overlap block cycle containing the union of both supports",
            "forced_common_central_fibre": "the shared meet is central or occurs in every maximal block",
        },
        "counts": {
            "events": size,
            "lattice_atoms": len(atoms),
            "non_atomic_selectors": len(selectors),
            "unordered_pairs_audited": len(pairs),
            "qualifying_pairs": len(qualifying),
        },
        "lattice_atoms": atoms,
        "non_atomic_selectors": selectors,
        "qualifying_pairs": qualifying,
        "smallest_lexicographic_pair": smallest,
        "minimal_partial_relation_control": {
            "description": "Ult(A) times over Ult(D) Ult(C), with two lifts over each of two D ultrafilters",
            "left_ultrafilters": 4,
            "right_ultrafilters": 4,
            "pairs": target_relation,
            "checks": {
                "size_is_8_not_rectangle_16": len(target_relation) == 8,
                "every_left_has_two_partners": all(sum(u == x for x, _ in target_relation) == 2 for u in range(4)),
                "every_right_has_two_partners": all(sum(v == y for _, y in target_relation) == 2 for v in range(4)),
            },
        },
        "checks": {
            "all_pairs_were_audited": len(pairs) == len(selectors) * (len(selectors) - 1) // 2,
            "qualifying_filter_recomputes": qualifying == [p for p in pairs if all(p["tests"].values())],
            "smallest_pair_is_5_11": bool(smallest and smallest["pair"] == [5, 11]),
            "smallest_shared_meet_is_q0": bool(smallest and smallest["boolean_regions"]["shared_meet"] == skeleton["generators"]["B_atoms"][0]),
        },
        "all_pairs": pairs,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--skeleton", type=Path,
                        default=Path(__file__).with_name("seven_block_skeleton.json"))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build(json.loads(args.skeleton.read_text()))
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")
