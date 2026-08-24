#!/usr/bin/env python3
"""Audit the first certified non-atomic selector-pair substitution.

The selectors are q=B0 union B1 (mask 0x00ff) and r=B0 union B2
(mask 0x0f0f).  A point below both is replaced by X times Y, a point below
q only by X, a point below r only by Y, and every other point is rigid.
In a named block, the X-coordinate is visible exactly when q belongs to that
block, and the Y-coordinate exactly when r belongs to that block.
"""

import argparse
import hashlib
import itertools
import json
from pathlib import Path

from five_block_two_selector_inflation_audit import NAMES, powerset, skeleton

SCHEMA = "five-block-nonatomic-pair-inflation-v1"


def inflate(n=2, m=2, overlap_relation=None):
    old_universe, old_blocks, _, _ = skeleton()
    b0 = frozenset(p for p in old_universe if p[0] == 0)
    b1 = frozenset(p for p in old_universe if p[0] == 1)
    b2 = frozenset(p for p in old_universe if p[0] == 2)
    q, r = b0 | b1, b0 | b2
    points = []
    for p in old_universe:
        if p in q and p in r and overlap_relation is not None:
            points.extend((p, x, y) for x, y in overlap_relation)
        else:
            xs = range(n) if p in q else (None,)
            ys = range(m) if p in r else (None,)
            points.extend((p, x, y) for x in xs for y in ys)
    universe = frozenset(points)
    lift = lambda event: frozenset(z for z in universe if z[0] in event)
    blocks = {}
    support_q, support_r = [], []
    for name in NAMES:
        old = old_blocks[name]
        old_atoms = [a for a in old if a and not any(b < a for b in old if b)]
        sees_q, sees_r = q in old, r in old
        if sees_q:
            support_q.append(name)
        if sees_r:
            support_r.append(name)
        atoms = []
        for atom in old_atoms:
            x_values = range(n) if sees_q and atom <= q else (None,)
            y_values = range(m) if sees_r and atom <= r else (None,)
            for x in x_values:
                for y in y_values:
                    cell = frozenset(
                        z for z in universe if z[0] in atom
                        and (x is None or z[1] == x)
                        and (y is None or z[2] == y))
                    if cell:
                        atoms.append(cell)
        assert all(atoms) and frozenset().union(*atoms) == universe
        assert all(a.isdisjoint(b) for a, b in itertools.combinations(atoms, 2))
        blocks[name] = powerset(atoms)
    assert support_q == ["A00", "A01", "A10", "A11"]
    assert support_r == ["A00", "C01"]
    return universe, blocks


def extrema(carrier, x, y, upper):
    candidates = ([z for z in carrier if x <= z and y <= z] if upper else
                  [z for z in carrier if z <= x and z <= y])
    return [z for z in candidates if not any(
        z != w and ((w < z) if upper else (z < w)) for w in candidates)]


def audit(n=2, m=2, overlap_relation=None):
    universe, blocks = inflate(n, m, overlap_relation=overlap_relation)
    carrier = set().union(*blocks.values())
    point_index = {p: i for i, p in enumerate(sorted(universe))}
    integer_mask = lambda e: sum(1 << point_index[p] for p in e)
    events = tuple(sorted(carrier, key=integer_mask))
    complement_closed = all(universe - x in carrier for x in events)
    disjoint_pairs = [(x, y) for x in events for y in events if x.isdisjoint(y)]
    disjoint_union_closed = all(x | y in carrier for x, y in disjoint_pairs)
    mask = lambda e: hex(integer_mask(e))
    signature = lambda e: [name for name in NAMES if e in blocks[name]]
    first_disjoint_failure = next(((x, y) for x, y in disjoint_pairs
                                   if x | y not in carrier), None)
    profiles = {}
    for p in universe:
        profiles.setdefault(tuple(p in e for e in events), []).append(p)
    meet, join, failures = {}, {}, []
    for i, x in enumerate(events):
        for y in events[i:]:
            lo, hi = extrema(carrier, x, y, False), extrema(carrier, x, y, True)
            if len(lo) != 1 or len(hi) != 1:
                failures.append((x, y, len(lo), len(hi)))
            else:
                meet[x, y] = meet[y, x] = lo[0]
                join[x, y] = join[y, x] = hi[0]
    lattice = not failures
    orthomodular = lattice and all(
        join[x, meet[y, universe - x]] == y
        for x in events for y in events if x <= y)
    if lattice:
        commutes = lambda x, y: join[meet[x, y], meet[x, universe - y]] == x
        centre = {x for x in events if all(commutes(x, y) for y in events)}
        maximal_named = all(
            all(commutes(x, y) for x in block for y in block)
            and all(any(not commutes(x, y) for y in block) for x in carrier - block)
            for block in blocks.values())
        compatible_pairs = sum(commutes(x, y) for x in events for y in events)
    else:
        centre, maximal_named, compatible_pairs = set(), False, None
    enc = sorted("".join("1" if p in e else "0" for p in sorted(universe))
                 for e in events)
    return {
        "schema": SCHEMA,
        "selector_masks": ["0x00ff", "0x0f0f"],
        "fibre_atoms": [n, m],
        "points": len(universe),
        "events": len(events),
        "block_sizes": {name: len(blocks[name]) for name in NAMES},
        "ordered_pairs": len(events) ** 2,
        "ordered_disjoint_pairs": len(disjoint_pairs),
        "ordered_compatible_pairs": compatible_pairs,
        "centre_size": len(centre) if lattice else None,
        "event_sha256": hashlib.sha256("\n".join(enc).encode()).hexdigest(),
        "generated_boolean_atoms": len(profiles),
        "generated_boolean_atom_sizes": sorted(map(len, profiles.values())),
        "first_disjoint_union_failure": None if first_disjoint_failure is None else {
            "left_mask": mask(first_disjoint_failure[0]),
            "right_mask": mask(first_disjoint_failure[1]),
            "union_mask": mask(first_disjoint_failure[0] | first_disjoint_failure[1]),
            "left_signature": signature(first_disjoint_failure[0]),
            "right_signature": signature(first_disjoint_failure[1]),
            "cardinalities": [len(first_disjoint_failure[0]),
                              len(first_disjoint_failure[1])]},
        "first_extrema_failure": None if not failures else {
            "left_mask": mask(failures[0][0]), "right_mask": mask(failures[0][1]),
            "left_signature": signature(failures[0][0]),
            "right_signature": signature(failures[0][1]),
            "cardinalities": [len(failures[0][0]), len(failures[0][1])],
            "lower_extrema": failures[0][2], "upper_extrema": failures[0][3]},
        "checks": {
            "complement_closed": complement_closed,
            "disjoint_union_closed": disjoint_union_closed,
            "unique_binary_extrema": lattice,
            "orthomodular": orthomodular,
            "named_blocks_maximal": maximal_named,
            "trivial_centre": lattice and centre == {frozenset(), universe},
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = audit()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.output.write_text(text) if args.output else print(text, end="")


if __name__ == "__main__":
    main()
