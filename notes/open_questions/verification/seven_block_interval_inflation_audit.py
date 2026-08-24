#!/usr/bin/env python3
"""Audit the smallest literal one-block interval inflation of L*.

The atom q_0 of the distinguished Boolean block B is replaced there by an
n-atom Boolean interval.  All other skeleton events are lifted through the
carrier projection and hence see no new fibre coordinate.  We then compute
the canonical finite Dynkin closure (complements and disjoint unions) and
test whether it is already a lattice/OML.  This is an approximant audit, not
an infinite sigma-completeness argument.
"""

import argparse
import json
from pathlib import Path

from seven_block_skeleton_data import build


SCHEMA = "seven-block-one-interval-inflation-v1"


def unions(atoms):
    out = set()
    for choice in range(1 << len(atoms)):
        event = 0
        for i, atom in enumerate(atoms):
            if choice >> i & 1:
                event |= atom
        out.add(event)
    return out


def unique_extrema(events, x, y, upper):
    if upper:
        candidates = [z for z in events if (x | y) & ~z == 0]
        extrema = [z for z in candidates
                   if not any(w != z and w & ~z == 0 for w in candidates)]
    else:
        candidates = [z for z in events if z & ~x == 0 and z & ~y == 0]
        extrema = [z for z in candidates
                   if not any(w != z and z & ~w == 0 for w in candidates)]
    return extrema


def dynkin_closure(seed, full):
    events = set(seed)
    rounds = []
    while True:
        old = set(events)
        events |= {full ^ x for x in old}
        events |= {x | y for x in old for y in old if x & y == 0}
        rounds.append(len(events))
        if events == old:
            return events, rounds


def maximal_cliques(vertices, adjacent):
    out = []

    def visit(r, p, x):
        if not p and not x:
            out.append(frozenset(r))
            return
        pivot = next(iter(p | x), None)
        neighbours = ({w for w in vertices if adjacent(pivot, w)}
                      if pivot is not None else set())
        for v in tuple(p - neighbours):
            nv = {w for w in vertices if w != v and adjacent(v, w)}
            visit(r | {v}, p & nv, x & nv)
            p.remove(v)
            x.add(v)

    visit(set(), set(vertices), set())
    return out


def boolean_closure(generators, full):
    events = {0, full, *generators}
    while True:
        old = set(events)
        events |= {full ^ x for x in old}
        events |= {x & y for x in old for y in old}
        if events == old:
            return events


def audit(fibre_atoms):
    if fibre_atoms < 2:
        raise ValueError("fibre_atoms must be at least 2")

    skeleton = build()
    base_masks = skeleton["event_masks"]
    base_blocks = {
        block["name"]: {base_masks[event] for event in block["events"]}
        for block in skeleton["blocks"]
    }
    b_atom_masks = [base_masks[event] for event in skeleton["blocks"][0]["atoms"]]
    q0 = b_atom_masks[0]
    q0_points = [i for i in range(16) if q0 >> i & 1]

    # Points under q0 acquire a common fibre coordinate.  Points outside q0
    # remain singletons.  Every old event is lifted by inverse image.
    expanded_points = []
    fibres = {}
    for point in range(16):
        copies = range(fibre_atoms) if point in q0_points else range(1)
        fibres[point] = []
        for copy in copies:
            fibres[point].append(len(expanded_points))
            expanded_points.append((point, copy))

    def lift(mask):
        out = 0
        for point in range(16):
            if mask >> point & 1:
                for expanded in fibres[point]:
                    out |= 1 << expanded
        return out

    lifted_blocks = {name: {lift(event) for event in block}
                     for name, block in base_blocks.items()}
    full = (1 << len(expanded_points)) - 1

    # The substituted B has n atoms below q0 and retains q1,q2,q3.
    interval_atoms = []
    for copy in range(fibre_atoms):
        atom = 0
        for point in q0_points:
            atom |= 1 << fibres[point][copy]
        interval_atoms.append(atom)
    substituted_b_atoms = interval_atoms + [lift(atom) for atom in b_atom_masks[1:]]
    substituted_b = unions(substituted_b_atoms)

    expected_blocks = {}
    for name, block in lifted_blocks.items():
        if lift(q0) in block:
            # q0 is an atom in each of these blocks; replace that atom by A_n.
            old_atoms = [event for event in block if event and
                         not any(other and other != event and other & ~event == 0
                                 for other in block)]
            expected_blocks[name] = unions(
                interval_atoms + [atom for atom in old_atoms if atom != lift(q0)])
        else:
            expected_blocks[name] = block

    raw = set().union(*(block for name, block in lifted_blocks.items() if name != "B"),
                      substituted_b)
    closed, closure_rounds = dynkin_closure(raw, full)

    missing_meets = []
    missing_joins = []
    for x in closed:
        for y in closed:
            lowers = unique_extrema(closed, x, y, upper=False)
            uppers = unique_extrema(closed, x, y, upper=True)
            if len(lowers) != 1:
                missing_meets.append((x, y, lowers))
            if len(uppers) != 1:
                missing_joins.append((x, y, uppers))

    is_lattice = not missing_meets and not missing_joins
    complement_closed = all(full ^ x in closed for x in closed)
    disjoint_union_closed = all(x | y in closed for x in closed for y in closed
                                if x & y == 0)

    # A stable small witness is enough; full pairs would make the receipt noisy.
    witness = None
    if missing_meets:
        x, y, lowers = min(missing_meets, key=lambda item: (item[0], item[1]))
        witness = {
            "left": x,
            "right": y,
            "maximal_lower_bounds": sorted(lowers),
            "minimal_upper_bounds": sorted(unique_extrema(closed, x, y, upper=True)),
        }

    orthomodular = None
    centre = None
    maximal_blocks = None
    boundary_sizes = None
    boundaries_saturate = None
    if is_lattice:
        meet = {}
        join = {}
        for x in closed:
            for y in closed:
                meet[x, y] = unique_extrema(closed, x, y, upper=False)[0]
                join[x, y] = unique_extrema(closed, x, y, upper=True)[0]

        orthomodular = all(join[x, meet[y, full ^ x]] == y
                           for x in closed for y in closed if x & ~y == 0)

        def compatible(x, y):
            return join[meet[x, y], meet[x, full ^ y]] == x

        maximal_blocks = maximal_cliques(
            closed, lambda x, y: x != y and compatible(x, y))
        centre = {x for x in closed if all(compatible(x, y) for y in closed)}
        boundaries = []
        for block in maximal_blocks:
            shared = set().union(*(block & other for other in maximal_blocks
                                   if other != block))
            boundaries.append(boolean_closure(shared, full))
        boundary_sizes = sorted(len(boundary) for boundary in boundaries)
        boundaries_saturate = all(boundary == set(block)
                                  for boundary, block in zip(boundaries, maximal_blocks))

        expected_block_names = {
            next((name for name, expected in expected_blocks.items()
                  if block == frozenset(expected)), "unexpected")
            for block in maximal_blocks
        }

    return {
        "schema": SCHEMA,
        "scope": "finite approximant; no inference to infinite sigma-completeness or topology",
        "datum": {
            "skeleton_block": "B",
            "skeleton_interval": "[0,q0]",
            "fibre_boolean_algebra": f"P({fibre_atoms} atoms)",
            "distribution_rule": "only B sees the fibre; the other six blocks are projection lifts",
            "base_event_count": 56,
            "expanded_carrier_points": len(expanded_points),
        },
        "counts": {
            "substituted_B_events": len(substituted_b),
            "raw_events": len(raw),
            "dynkin_closed_events": len(closed),
            "closure_round_sizes": closure_rounds,
            "ordered_pairs_without_unique_meet": len(missing_meets),
            "ordered_pairs_without_unique_join": len(missing_joins),
        },
        "checks": {
            "raw_complement_closed": all(full ^ x in raw for x in raw),
            "raw_disjoint_union_closed": all(x | y in raw for x in raw for y in raw
                                              if x & y == 0),
            "dynkin_complement_closed": complement_closed,
            "dynkin_disjoint_union_closed": disjoint_union_closed,
            "dynkin_is_lattice": is_lattice,
            "orthomodular": orthomodular,
            "maximal_blocks_classified": maximal_blocks is not None,
            "centre_computed": centre is not None,
            "centre_is_trivial": None if centre is None else centre == {0, full},
            "all_boundaries_saturate": boundaries_saturate,
            "maximal_blocks_equal_expected_seven": None if maximal_blocks is None else
                set(maximal_blocks) == {frozenset(block) for block in expected_blocks.values()},
        },
        "first_failure": "latticehood after canonical mixed Dynkin closure"
        if not is_lattice else None,
        "lattice_failure_witness": witness,
        "completed_candidate": None if not is_lattice else {
            "maximal_block_count": len(maximal_blocks),
            "maximal_block_sizes": sorted(len(block) for block in maximal_blocks),
            "centre_size": len(centre),
            "boundary_sizes": boundary_sizes,
            "inflated_block_names": sorted(name for name, block in expected_blocks.items()
                                           if len(block) > 16),
            "maximal_block_names": sorted(expected_block_names),
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-fibre-atoms", type=int, default=4)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    results = [audit(n) for n in range(2, args.max_fibre_atoms + 1)]
    for result in results:
        checks = result["checks"]
        assert checks["raw_complement_closed"]
        assert not checks["raw_disjoint_union_closed"]
        assert checks["dynkin_complement_closed"]
        assert checks["dynkin_disjoint_union_closed"]
        assert checks["dynkin_is_lattice"]
        assert checks["orthomodular"]
        assert checks["maximal_blocks_equal_expected_seven"]
        assert checks["centre_is_trivial"]
        assert checks["all_boundaries_saturate"]
    receipt = {"schema": SCHEMA, "approximants": results}
    text = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
