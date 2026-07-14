#!/usr/bin/env python3
"""Produce the exact three-type transversal-relation certificate."""
from __future__ import annotations

import hashlib
import itertools
import json
import time
from pathlib import Path

import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher, categorical_node_match

CELLS = ("g", "h", "W", "Vi", "Vj", "R")
U = 63
FULL = (1 << 18) - 1


def section(column: int, names: tuple[str, ...]) -> int:
    return sum(1 << (6 * column + CELLS.index(name)) for name in names)


def primitives():
    sigmas = [0, 0, 0]
    collectors = {(1, 2): 0, (1, 3): 0, (2, 3): 0}
    for column, kind in enumerate((1, 2, 3)):
        low, high = sorted({1, 2, 3} - {kind})
        traces = {
            kind: ("g", "h"),
            low: ("g", "W", "Vi"),
            high: ("h", "W", "Vj"),
        }
        for name in (1, 2, 3):
            sigmas[name - 1] |= section(column, traces[name])
        for pair in collectors:
            if kind in pair:
                other = next(x for x in pair if x != kind)
                collectors[pair] |= section(column, ("g",) if other == low else ("h",))
    cylinders = [U << (6 * column) for column in range(3)]
    return cylinders, sigmas, [collectors[p] for p in ((1, 2), (1, 3), (2, 3))]


def close(generators):
    closure = {0, FULL, *generators}
    while True:
        old = len(closure)
        closure |= {FULL ^ x for x in tuple(closure)}
        items = tuple(closure)
        closure |= {
            x | y
            for index, x in enumerate(items)
            for y in items[index + 1 :]
            if not x & y
        }
        if len(closure) == old:
            return closure


def triple(mask):
    return [(mask >> (6 * column)) & U for column in range(3)]


def automorphisms(closure):
    graph = nx.Graph()
    for atom in range(18):
        graph.add_node(("a", atom), kind="atom")
    for index, event in enumerate(sorted(closure)):
        graph.add_node(("e", index), kind="event")
        for atom in range(18):
            if event >> atom & 1:
                graph.add_edge(("a", atom), ("e", index))
    matcher = GraphMatcher(
        graph, graph, node_match=categorical_node_match("kind", None)
    )
    return sorted(
        {
            tuple(mapping[("a", atom)][1] for atom in range(18))
            for mapping in matcher.isomorphisms_iter()
        }
    )


def main():
    started = time.perf_counter()
    cylinders, sigmas, collectors = primitives()
    named = cylinders + sigmas + collectors
    names = ["C1", "C2", "C3", "S1", "S2", "S3", "G12", "G13", "G23"]
    closure = close(named)
    profiles = sorted(map(triple, closure))
    projections_1 = [sorted({profile[i] for profile in profiles}) for i in range(3)]
    projections_2 = {
        f"{i + 1}{j + 1}": sorted({(p[i], p[j]) for p in profiles})
        for i, j in ((0, 1), (0, 2), (1, 2))
    }
    strata = []
    proper_values = [sorted(set(projections_1[i]) - {0, U}) for i in range(3)]
    for binary_count in range(1, 4):
        for binary in itertools.combinations(range(3), binary_count):
            proper = tuple(i for i in range(3) if i not in binary)
            for values in itertools.product(*(proper_values[i] for i in proper)):
                relation = sorted(
                    {
                        tuple(p[i] // U for i in binary)
                        for p in profiles
                        if all(p[i] in (0, U) for i in binary)
                        and all(p[i] == value for i, value in zip(proper, values))
                    }
                )
                if relation:
                    product = sorted(
                        itertools.product(
                            *[{row[k] for row in relation} for k in range(binary_count)]
                        )
                    )
                    strata.append(
                        {
                            "binary_coordinates": [i + 1 for i in binary],
                            "fixed_proper": {str(i + 1): v for i, v in zip(proper, values)},
                            "relation": [list(row) for row in relation],
                            "rectangular": relation == product,
                        }
                    )
    minimal_masks = []
    for mask in range(1 << 9):
        if close([g for i, g in enumerate(named) if mask >> i & 1]) == closure:
            if not any(mask & old == old for old in minimal_masks):
                minimal_masks.append(mask)
    distribution = {
        str(k): sum(sum(x in (0, U) for x in p) == k for p in profiles)
        for k in range(4)
    }
    raw = ",".join(map(str, sorted(closure))).encode()
    certificate = {
        "scope": "exhaustive closure on one labelled column of each of types 1,2,3",
        "cells": list(CELLS),
        "primitive_masks": dict(zip(names, named)),
        "primitive_profiles": dict(zip(names, map(triple, named))),
        "closure_size": len(closure),
        "closure_sha256": hashlib.sha256(raw).hexdigest(),
        "profiles": profiles,
        "projection_1": projections_1,
        "projection_2": projections_2,
        "binary_coordinate_count_distribution": distribution,
        "nonempty_fixed_proper_strata": strata,
        "all_nonempty_strata_rectangular": all(s["rectangular"] for s in strata),
        "minimal_named_generating_sets": [
            [names[i] for i in range(9) if mask >> i & 1] for mask in minimal_masks
        ],
        "single_deletion_closure_sizes": {
            names[i]: len(close(named[:i] + named[i + 1 :])) for i in range(9)
        },
        "incidence_hypergraph_automorphisms": [list(p) for p in automorphisms(closure)],
    }
    path = Path(__file__).with_name("q_certificate.json")
    path.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    summary = {k: certificate[k] for k in (
        "closure_size", "binary_coordinate_count_distribution",
        "all_nonempty_strata_rectangular", "minimal_named_generating_sets",
    )}
    summary["runtime_seconds"] = time.perf_counter() - started
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
