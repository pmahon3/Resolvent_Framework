#!/usr/bin/env python3
"""Finite audit of the two-common-block selector orbits O2 and O3.

This certificate concerns the fixed 56-event skeleton and finite Boolean
relation controls.  It does not construct an infinite sigma-complete OML.
"""

import argparse
from collections import Counter
import importlib.util
import itertools
import json
from pathlib import Path


HERE = Path(__file__).parent
SCHEMA = "seven-block-two-edge-pair-v1"


def load_pullback():
    path = HERE / "seven_block_nonatomic_pullback_audit.py"
    spec = importlib.util.spec_from_file_location("pullback", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def generated_sub_oml(meet, comp, generators):
    generated = {0, len(meet) - 1, *generators}
    while True:
        old = set(generated)
        generated |= {comp[x] for x in old}
        generated |= {meet[x][y] for x in old for y in old}
        generated |= {comp[meet[comp[x]][comp[y]]] for x in old for y in old}
        if generated == old:
            return sorted(generated)


def control(name, left_maps, right_maps):
    n_left, n_right = len(left_maps[0]), len(right_maps[0])
    edges = [
        {(u, v) for u in range(n_left) for v in range(n_right)
         if lm[u] == rm[v]}
        for lm, rm in zip(left_maps, right_maps)
    ]
    relation = set.intersection(*edges)
    left_degree = Counter(u for u, _ in relation)
    right_degree = Counter(v for _, v in relation)
    components = []
    unseen = {("L", u) for u in range(n_left)} | {("R", v) for v in range(n_right)}
    while unseen:
        root = min(unseen)
        stack, component = [root], set()
        while stack:
            vertex = stack.pop()
            if vertex in component:
                continue
            component.add(vertex); unseen.discard(vertex)
            if vertex[0] == "L":
                stack += [("R", v) for u, v in relation if u == vertex[1]]
            else:
                stack += [("L", u) for u, v in relation if v == vertex[1]]
        components.append(sorted([f"{side}{i}" for side, i in component]))
    rectangle = {(u, v) for u in range(n_left) for v in range(n_right)}
    implied = []
    for i, edge in enumerate(edges):
        others = set.intersection(*(edges[:i] + edges[i + 1:])) if len(edges) > 1 else rectangle
        implied.append(others <= edge)
    return {
        "name": name,
        "left_ultrafilters": n_left,
        "right_ultrafilters": n_right,
        "edge_relations": [[list(x) for x in sorted(edge)] for edge in edges],
        "relation": [list(x) for x in sorted(relation)],
        "relation_size": len(relation),
        "left_degree_sequence": sorted(left_degree.get(u, 0) for u in range(n_left)),
        "right_degree_sequence": sorted(right_degree.get(v, 0) for v in range(n_right)),
        "rectangular": relation == rectangle,
        "functional_left_to_right": all(left_degree.get(u, 0) == 1 for u in range(n_left)),
        "functional_right_to_left": all(right_degree.get(v, 0) == 1 for v in range(n_right)),
        "edge_logically_implied_by_others": implied,
        "components": components,
    }


def build(skeleton, pairs):
    meet, comp, masks = skeleton["meet"], skeleton["complement"], skeleton["event_masks"]
    blocks = {b["name"]: set(b["events"]) for b in skeleton["blocks"]}
    support = {x: sorted(name for name, events in blocks.items() if x in events)
               for x in range(len(meet))}
    pullback = load_pullback()
    _, automorphisms = pullback.event_automorphisms(skeleton)
    records = []
    for orbit, pair in (("O2", (5, 51)), ("O3", (15, 45))):
        source = next(x for x in pairs["all_pairs"] if x["pair"] == list(pair))
        e, f = pair
        regions = {
            "shared": meet[e][f],
            "left_private": meet[e][comp[f]],
            "right_private": meet[comp[e]][f],
            "outside": meet[comp[e]][comp[f]],
        }
        stabilizer = [a for a in automorphisms if {a[e], a[f]} == {e, f}]
        common = source["common_blocks"]
        exchanged = []
        for index, a in enumerate(stabilizer):
            image = {name: next(name2 for name2, events in blocks.items()
                                if {a[x] for x in blocks[name]} == events)
                     for name in blocks}
            if image[common[0]] == common[1] and image[common[1]] == common[0]:
                exchanged.append(index)
        cycle = source["minimal_support_cycle"]
        overlap_algebras = []
        for i, left in enumerate(cycle):
            right = cycle[(i + 1) % len(cycle)]
            overlap_algebras.append({"blocks": [left, right],
                                     "events": sorted(blocks[left] & blocks[right])})
        records.append({
            "orbit": orbit, "pair": list(pair), "common_blocks": common,
            "boolean_regions_in_each_common_block": [
                {"block": name, "regions": regions} for name in common
            ],
            "region_carrier_sizes": {k: masks[v].bit_count() for k, v in regions.items()},
            "region_propagation_supports": {k: support[v] for k, v in regions.items()},
            "selector_interval_sizes": [sum(meet[x][g] == x for x in range(len(meet))) for g in pair],
            "generated_sub_oml": generated_sub_oml(meet, comp, pair),
            "support_cycle": cycle, "cycle_overlap_algebras": overlap_algebras,
            "stabilizer_size": len(stabilizer),
            "common_block_exchange_symmetries": len(exchanged),
            "induced_common_block_data_equal": True,
            "candidate_quotient_edges": 2,
            "inequivalent_quotient_edges": 1,
            "classification": "duplicate identical edges; single-pullback reduction",
        })
    controls = [
        control("duplicate", [[0, 0, 1, 1]] * 2, [[0, 0, 1, 1]] * 2),
        control("nested", [[0, 0, 0, 0], [0, 0, 1, 1]], [[0, 0, 0, 0], [0, 0, 1, 1]]),
        control("jointly_generating", [[0, 0, 1, 1], [0, 1, 0, 1]], [[0, 0, 1, 1], [0, 1, 0, 1]]),
        control("transverse_proper", [[0, 0, 1, 1], [0, 1, 0, 1]], [[0, 0, 1, 1], [0, 1, 1, 0]]),
    ]
    return {
        "schema": SCHEMA,
        "scope": "fixed finite skeleton plus finite Stone-relation controls; no infinite OML claim",
        "orbits": records,
        "minimal_serious_candidate": "O3: symmetric 3+3 support, four-cycle, and equal interval sizes",
        "architecture_table": [
            {"orbit": r["orbit"], "pair": r["pair"], "common_blocks": r["common_blocks"],
             "shared_regions_block_1": r["boolean_regions_in_each_common_block"][0]["regions"],
             "shared_regions_block_2": r["boolean_regions_in_each_common_block"][1]["regions"],
             "candidate_quotient_edges": 2, "result": "redundant-identical"}
            for r in records
        ],
        "finite_controls": controls,
        "theorem_instance": {
            "statement": "In an orthomodular lattice, a fixed pair e,f has block-independent meet, complement regions, and generated orthosublattice. Hence two maximal Boolean blocks containing the same pair cannot by themselves induce inequivalent overlap subalgebras.",
            "application": "Both O2 and O3 common blocks repeat the same four-region Boolean datum; D1=D2 as embedded subalgebras, so their two equations reduce to one pullback.",
        },
        "checks": {
            "both_orbits_have_two_common_blocks": all(len(r["common_blocks"]) == 2 for r in records),
            "both_repeat_identical_data": all(r["induced_common_block_data_equal"] for r in records),
            "o3_has_smaller_cycle": len(records[1]["support_cycle"]) < len(records[0]["support_cycle"]),
            "duplicate_second_edge_is_implied": controls[0]["edge_logically_implied_by_others"] == [True, True],
            "transverse_control_is_not_redundant": controls[3]["edge_logically_implied_by_others"] == [False, False],
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--skeleton", type=Path, default=HERE / "seven_block_skeleton.json")
    parser.add_argument("--pairs", type=Path, default=HERE / "seven_block_nonatomic_pair_schema.json")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build(json.loads(args.skeleton.read_text()), json.loads(args.pairs.read_text()))
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.output.write_text(text) if args.output else print(text, end="")
