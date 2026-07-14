#!/usr/bin/env python3
"""Produce finite certificates for the distinct two-selector inflation.

The selectors in the certified 44-event survivor are q=0x000f and
r=0x3300.  Their block supports meet only in A01.  This script substitutes
P(n) below q and P(m) below r and exhaustively audits the concrete OML.
"""

import argparse
import hashlib
import itertools
import json
from pathlib import Path

NAMES = ("A00", "A01", "C01", "A10", "A11")
SCHEMA = "five-block-distinct-two-selector-inflation-v1"


def powerset(atoms):
    return {frozenset().union(*(atoms[i] for i in range(len(atoms)) if mask >> i & 1))
            for mask in range(1 << len(atoms))}


def skeleton():
    omega = tuple(itertools.product(range(4), range(2), range(2)))
    base = [frozenset(w for w in omega if w[0] == i) for i in range(4)]
    a = [frozenset(w for w in omega if w[0] in side and w[1] == bit)
         for side in ({0, 1}, {2, 3}) for bit in range(2)]
    c = [frozenset(w for w in omega if w[0] in side and w[2] == bit)
         for side in ({0, 2}, {1, 3}) for bit in range(2)]
    adec = ((base[:2], a[:2]), (base[2:], a[2:]))
    cdec = (((base[0], base[2]), c[:2]), ((base[1], base[3]), c[2:]))
    blocks = {}
    for x, y in itertools.product(range(2), repeat=2):
        blocks[f"A{x}{y}"] = powerset((*adec[0][x], *adec[1][y]))
        blocks[f"C{x}{y}"] = powerset((*cdec[0][x], *cdec[1][y]))
    index = {point: i for i, point in enumerate(omega)}
    mask = lambda event: sum(1 << index[p] for p in event)
    carrier = set().union(*(blocks[name] for name in NAMES))
    q = next(event for event in carrier if mask(event) == 0x000f)
    r = next(event for event in carrier if mask(event) == 0x3300)
    return omega, blocks, q, r


def inflate(n, m):
    omega, old_blocks, q, r = skeleton()
    points = []
    for point in omega:
        if point in q:
            points.extend(("q", point, i) for i in range(n))
        elif point in r:
            points.extend(("r", point, i) for i in range(m))
        else:
            points.append(("o", point, 0))
    universe = frozenset(points)
    lift = lambda event: frozenset(z for z in universe if z[1] in event)
    blocks = {}
    for name in NAMES:
        old_atoms = [x for x in old_blocks[name] if x and
                     not any(y < x for y in old_blocks[name] if y)]
        atoms = []
        for atom in old_atoms:
            if atom == q:
                atoms.extend(frozenset(z for z in universe if z[0] == "q" and z[2] == i)
                             for i in range(n))
            elif atom == r:
                atoms.extend(frozenset(z for z in universe if z[0] == "r" and z[2] == i)
                             for i in range(m))
            else:
                atoms.append(lift(atom))
        blocks[name] = powerset(atoms)
    return universe, blocks


def sole_extreme(carrier, x, y, upper):
    candidates = ([z for z in carrier if x <= z and y <= z] if upper else
                  [z for z in carrier if z <= x and z <= y])
    extrema = [z for z in candidates if not any(
        z != w and ((w < z) if upper else (z < w)) for w in candidates)]
    return extrema


def audit(n, m):
    universe, blocks = inflate(n, m)
    carrier = set().union(*(blocks[name] for name in NAMES))
    events = tuple(carrier)
    complement_closed = all(universe - x in carrier for x in events)
    disjoint_pairs = [(x, y) for x in events for y in events if x.isdisjoint(y)]
    disjoint_union_closed = all(x | y in carrier for x, y in disjoint_pairs)
    meet, join = {}, {}
    unique_extrema = True
    for x in events:
        for y in events:
            lo, hi = sole_extreme(carrier, x, y, False), sole_extreme(carrier, x, y, True)
            if len(lo) != 1 or len(hi) != 1:
                unique_extrema = False
            else:
                meet[x, y], join[x, y] = lo[0], hi[0]
    orthomodular = unique_extrema and all(
        join[x, meet[y, universe - x]] == y
        for x in events for y in events if x <= y)
    commutes = lambda x, y: join[meet[x, y], meet[x, universe - y]] == x
    centre = {x for x in events if all(commutes(x, y) for y in events)}
    # Every named block is compatible, and every outsider fails against it.
    maximal_named = all(
        all(commutes(x, y) for x in blocks[name] for y in blocks[name]) and
        all(any(not commutes(x, y) for y in blocks[name]) for x in carrier - blocks[name])
        for name in NAMES)
    # Enumerate maximal compatibility cliques by Bron--Kerbosch.
    compatible_pairs = sum(commutes(x, y) for x in events for y in events)
    neighbours = {x: {y for y in events if y != x and commutes(x, y)} for x in events}
    cliques = []
    def bron_kerbosch(current, possible, excluded):
        if not possible and not excluded:
            cliques.append(frozenset(current))
            return
        pivot = next(iter(possible | excluded), None)
        candidates = possible - (neighbours[pivot] if pivot is not None else set())
        for vertex in tuple(candidates):
            bron_kerbosch(current | {vertex}, possible & neighbours[vertex],
                          excluded & neighbours[vertex])
            possible.remove(vertex)
            excluded.add(vertex)
    bron_kerbosch(set(), set(events), set())
    exact_named_blocks = maximal_named and set(cliques) == {
        frozenset(blocks[name]) for name in NAMES}
    enc = sorted("".join("1" if p in event else "0" for p in sorted(universe)) for event in events)
    digest = hashlib.sha256("\n".join(enc).encode()).hexdigest()
    return {
        "fibre_atoms": [n, m], "points": len(universe), "events": len(events),
        "block_sizes": {name: len(blocks[name]) for name in NAMES},
        "ordered_pairs": len(events) ** 2, "ordered_disjoint_pairs": len(disjoint_pairs),
        "ordered_compatible_pairs": compatible_pairs,
        "comparable_ordered_pairs": sum(x <= y for x in events for y in events),
        "centre_size": len(centre), "event_sha256": digest,
        "maximal_compatibility_clique_sizes": sorted(map(len, cliques)),
        "checks": {"complement_closed": complement_closed,
                   "disjoint_union_closed": disjoint_union_closed,
                   "unique_binary_extrema": unique_extrema,
                   "orthomodular": orthomodular,
                   "exact_five_maximal_blocks": exact_named_blocks,
                   "trivial_centre": centre == {frozenset(), universe}},
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    receipt = {"schema": SCHEMA, "selector_masks": ["0x000f", "0x3300"],
               "approximants": [audit(2, 2), audit(2, 3), audit(3, 2)]}
    assert all(all(item["checks"].values()) for item in receipt["approximants"])
    text = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    args.output.write_text(text) if args.output else print(text, end="")


if __name__ == "__main__":
    main()
