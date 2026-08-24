#!/usr/bin/env python3
"""Finite approximants to the q0-inflation of the 44-event survivor.

This checks the finite Boolean fibres P(n), not an arbitrary Boolean
sigma-algebra and not infinite sigma-completeness.
"""

import argparse
import json
from pathlib import Path

from exhaustive_boundary_properness_audit import OMEGA, atom_list, labelled_blocks
from seven_block_interval_inflation_audit import (
    boolean_closure,
    dynkin_closure,
    maximal_cliques,
    unique_extrema,
    unions,
)


SCHEMA = "exhaustive-boundary-one-interval-inflation-v1"
CHOSEN = ("A00", "A01", "C01", "A10", "A11")


def audit(fibre_atoms):
    if fibre_atoms < 2:
        raise ValueError("fibre_atoms must be at least 2")

    base_blocks = labelled_blocks()
    q0 = frozenset(point for point in OMEGA if point[0] == 0)
    q0_points = [i for i, point in enumerate(OMEGA) if point in q0]
    fibres = {}
    expanded_points = []
    for point in range(len(OMEGA)):
        fibres[point] = []
        copies = range(fibre_atoms) if point in q0_points else range(1)
        for copy in copies:
            fibres[point].append(len(expanded_points))
            expanded_points.append((point, copy))

    def mask(event):
        return sum(1 << i for i, point in enumerate(OMEGA) if point in event)

    def lift(event):
        out = 0
        base = mask(event)
        for point in range(len(OMEGA)):
            if base >> point & 1:
                out |= sum(1 << copy for copy in fibres[point])
        return out

    interval_atoms = []
    for copy in range(fibre_atoms):
        atom = 0
        for point in q0_points:
            atom |= 1 << fibres[point][copy]
        interval_atoms.append(atom)

    expected = {}
    inflated = []
    for name in CHOSEN:
        atoms = atom_list(base_blocks[name])
        if q0 in atoms:
            inflated.append(name)
            expected[name] = unions(
                interval_atoms + [lift(atom) for atom in atoms if atom != q0]
            )
        else:
            expected[name] = {lift(event) for event in base_blocks[name]}

    full = (1 << len(expanded_points)) - 1
    raw = set().union(*(expected[name] for name in CHOSEN))
    closed, rounds = dynkin_closure(raw, full)
    assert closed == raw

    meet = {}
    join = {}
    for x in closed:
        for y in closed:
            lowers = unique_extrema(closed, x, y, upper=False)
            uppers = unique_extrema(closed, x, y, upper=True)
            assert len(lowers) == len(uppers) == 1
            meet[x, y], join[x, y] = lowers[0], uppers[0]

    def compatible(x, y):
        return join[meet[x, y], meet[x, full ^ y]] == x

    maximal_blocks = maximal_cliques(
        closed, lambda x, y: x != y and compatible(x, y)
    )
    named = {frozenset(block): name for name, block in expected.items()}
    centre = {x for x in closed if all(compatible(x, y) for y in closed)}
    boundaries = {}
    for block in maximal_blocks:
        shared = set().union(*(block & other for other in maximal_blocks if other != block))
        boundaries[named[block]] = boolean_closure(shared, full)

    orthomodular = all(
        join[x, meet[y, full ^ x]] == y for x in closed for y in closed if x & ~y == 0
    )
    exact_blocks = set(maximal_blocks) == set(named)
    boundary_sizes = {name: len(boundaries[name]) for name in CHOSEN}
    proper = sorted(name for name in CHOSEN if boundaries[name] < expected[name])

    return {
        "fibre_atoms": fibre_atoms,
        "scope": "finite Boolean-fibre approximant only",
        "counts": {
            "carrier_points": len(expanded_points),
            "events": len(closed),
            "closure_round_sizes": rounds,
            "maximal_blocks": len(maximal_blocks),
            "maximal_block_sizes": sorted(map(len, maximal_blocks)),
            "centre": len(centre),
        },
        "checks": {
            "complement_closed": all(full ^ x in closed for x in closed),
            "disjoint_union_closed": all(
                x | y in closed for x in closed for y in closed if x & y == 0
            ),
            "lattice": True,
            "orthomodular": orthomodular,
            "exact_five_maximal_blocks": exact_blocks,
            "trivial_centre": centre == {0, full},
            "inflated_blocks": inflated,
            "boundary_sizes": boundary_sizes,
            "proper_boundary_blocks": proper,
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-fibre-atoms", type=int, default=4)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    approximants = [audit(n) for n in range(2, args.max_fibre_atoms + 1)]
    for result in approximants:
        checks = result["checks"]
        assert checks["complement_closed"]
        assert checks["disjoint_union_closed"]
        assert checks["orthomodular"]
        assert checks["exact_five_maximal_blocks"]
        assert checks["trivial_centre"]
        assert checks["inflated_blocks"] == ["A00", "A01", "C01"]
        assert checks["proper_boundary_blocks"] == ["C01"]
    receipt = {"schema": SCHEMA, "approximants": approximants}
    text = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    args.output.write_text(text) if args.output else print(text, end="")


if __name__ == "__main__":
    main()
