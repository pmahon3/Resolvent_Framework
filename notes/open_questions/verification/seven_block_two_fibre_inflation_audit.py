#!/usr/bin/env python3
"""Finite approximants for two jointly coherent, disjoint-support fibres.

The distinguished selectors are q0 (event 1) and the smallest jointly
coherent atom in the other orbit (event 2).  Carrier points in both concrete
selector sets acquire both independent coordinates.  Only one block in each
support is initially substituted; canonical Dynkin closure determines the
propagation and any mixed events.
"""

import argparse
import itertools
import json
from pathlib import Path

from seven_block_interval_inflation_audit import (
    boolean_closure,
    dynkin_closure,
    maximal_cliques,
    unique_extrema,
    unions,
)
from seven_block_skeleton_data import build


SCHEMA = "seven-block-two-fibre-inflation-v1"


def atoms_of(block):
    return sorted(
        event
        for event in block
        if event
        and not any(
            other and other != event and other & ~event == 0 for other in block
        )
    )


def audit(a_atoms, c_atoms):
    skeleton = build()
    base_masks = skeleton["event_masks"]
    base_blocks = {
        block["name"]: {base_masks[event] for event in block["events"]}
        for block in skeleton["blocks"]
    }
    q = base_masks[skeleton["generators"]["B_atoms"][0]]
    r = base_masks[2]
    assert q & r

    expanded_points = []
    fibres = {}
    for point in range(16):
        a_copies = range(a_atoms) if q >> point & 1 else range(1)
        c_copies = range(c_atoms) if r >> point & 1 else range(1)
        fibres[point] = {}
        for a_copy, c_copy in itertools.product(a_copies, c_copies):
            fibres[point][a_copy, c_copy] = len(expanded_points)
            expanded_points.append((point, a_copy, c_copy))

    def lift(mask):
        return sum(
            1 << expanded
            for point, copies in fibres.items()
            if mask >> point & 1
            for expanded in copies.values()
        )

    full = (1 << len(expanded_points)) - 1
    lifted_blocks = {
        name: {lift(event) for event in block} for name, block in base_blocks.items()
    }

    def interval_atoms(selector, count, coordinate):
        result = []
        for chosen in range(count):
            atom = 0
            for point, copies in fibres.items():
                if not (selector >> point & 1):
                    continue
                for (a_copy, c_copy), expanded in copies.items():
                    if (a_copy if coordinate == "A" else c_copy) == chosen:
                        atom |= 1 << expanded
            result.append(atom)
        return result

    a_interval = interval_atoms(q, a_atoms, "A")
    c_interval = interval_atoms(r, c_atoms, "C")

    expected_blocks = {}
    for name, block in lifted_blocks.items():
        old_atoms = atoms_of(block)
        replacements = []
        for atom in old_atoms:
            if atom == lift(q):
                replacements.extend(a_interval)
            elif atom == lift(r):
                replacements.extend(c_interval)
            else:
                replacements.append(atom)
        expected_blocks[name] = unions(replacements)

    # B seeds A; D2 seeds C.  The other occurrences must be forced by closure.
    raw_blocks = dict(lifted_blocks)
    raw_blocks["B"] = expected_blocks["B"]
    raw_blocks["D2"] = expected_blocks["D2"]
    raw = set().union(*raw_blocks.values())
    closed, closure_rounds = dynkin_closure(raw, full)

    extrema = {
        (left, right): (
            unique_extrema(closed, left, right, upper=False),
            unique_extrema(closed, left, right, upper=True),
        )
        for left in closed
        for right in closed
    }
    is_lattice = all(len(lower) == len(upper) == 1 for lower, upper in extrema.values())
    if not is_lattice:
        return {
            "schema": SCHEMA,
            "datum": {"A_atoms": a_atoms, "C_atoms": c_atoms},
            "counts": {"raw": len(raw), "closed": len(closed)},
            "checks": {"dynkin_is_lattice": False},
        }

    meet = {pair: value[0][0] for pair, value in extrema.items()}
    join = {pair: value[1][0] for pair, value in extrema.items()}

    def compatible(left, right):
        return join[meet[left, right], meet[left, full ^ right]] == left

    blocks = maximal_cliques(
        closed, lambda left, right: left != right and compatible(left, right)
    )
    names = {
        frozenset(block): name for name, block in expected_blocks.items()
    }
    named_blocks = {names.get(block, "unexpected"): block for block in blocks}
    centre = {event for event in closed if all(compatible(event, x) for x in closed)}
    boundaries = []
    for block in blocks:
        shared = set().union(*(block & other for other in blocks if other != block))
        boundaries.append(boolean_closure(shared, full))

    # Compatible local atom choices enumerate every two-valued block state.
    block_atoms = [atoms_of(block) for block in blocks]
    global_states = []
    for choices in itertools.product(*block_atoms):
        values = {}
        valid = True
        for block, chosen in zip(blocks, choices):
            for event in block:
                value = int(chosen & ~event == 0)
                if event in values and values[event] != value:
                    valid = False
                    break
                values[event] = value
            if not valid:
                break
        if valid:
            global_states.append(values)

    relation = set()
    for state in global_states:
        if not state[lift(q)] or not state[lift(r)]:
            continue
        a_choice = next(i for i, atom in enumerate(a_interval) if state[atom])
        c_choice = next(i for i, atom in enumerate(c_interval) if state[atom])
        relation.add((a_choice, c_choice))
    a_projection = {left for left, _ in relation}
    c_projection = {right for _, right in relation}
    rectangle = {(left, right) for left in a_projection for right in c_projection}

    return {
        "schema": SCHEMA,
        "scope": "finite approximant only; no infinite sigma-completeness inference",
        "datum": {
            "selectors": {"q0": 1, "r": 2},
            "supports": {
                "q0": ["B", "D0", "D1"],
                "r": ["D2", "Ca"],
            },
            "A_atoms": a_atoms,
            "C_atoms": c_atoms,
            "seed_blocks": {"A": "B", "C": "D2"},
        },
        "counts": {
            "expanded_carrier_points": len(expanded_points),
            "raw_events": len(raw),
            "dynkin_closed_events": len(closed),
            "closure_round_sizes": closure_rounds,
            "global_two_valued_states": len(global_states),
        },
        "checks": {
            "raw_complement_closed": all(full ^ event in raw for event in raw),
            "raw_disjoint_union_closed": all(
                left | right in raw
                for left in raw
                for right in raw
                if left & right == 0
            ),
            "dynkin_complement_closed": all(full ^ event in closed for event in closed),
            "dynkin_disjoint_union_closed": all(
                left | right in closed
                for left in closed
                for right in closed
                if left & right == 0
            ),
            "dynkin_is_lattice": True,
            "orthomodular": all(
                join[left, meet[right, full ^ left]] == right
                for left in closed
                for right in closed
                if left & ~right == 0
            ),
            "maximal_blocks_equal_expected_seven": set(blocks)
            == {frozenset(block) for block in expected_blocks.values()},
            "centre_is_trivial": centre == {0, full},
            "all_boundaries_saturate": all(
                boundary == set(block)
                for boundary, block in zip(boundaries, blocks)
            ),
            "fibre_relation_is_rectangular": relation == rectangle,
            "monodromy_is_identity_product": relation == rectangle,
        },
        "completed_candidate": {
            "maximal_block_count": len(blocks),
            "maximal_block_names": sorted(named_blocks),
            "maximal_block_sizes": sorted(len(block) for block in blocks),
            "centre_size": len(centre),
            "fibre_relation": sorted([list(pair) for pair in relation]),
            "fibre_relation_size": len(relation),
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-fibre-atoms", type=int, default=3)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    results = []
    for a_atoms in range(2, args.max_fibre_atoms + 1):
        for c_atoms in range(2, args.max_fibre_atoms + 1):
            result = audit(a_atoms, c_atoms)
            checks = result["checks"]
            assert checks["dynkin_is_lattice"]
            assert checks["orthomodular"]
            assert checks["maximal_blocks_equal_expected_seven"]
            assert checks["centre_is_trivial"]
            assert checks["all_boundaries_saturate"]
            assert checks["fibre_relation_is_rectangular"]
            results.append(result)
    receipt = {"schema": SCHEMA, "approximants": results}
    text = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
