#!/usr/bin/env python3
"""Audit a proper-closure transverse triangle inside the 56-event OML.

This is a finite census of one explicitly labelled completion.  It does not
classify multi-block completions or address the infinite OML conjecture.
"""

import argparse
import itertools
import json
from pathlib import Path


SCHEMA = "three-block-noncentral-transverse-v1"
OMEGA = tuple(itertools.product(range(4), range(2), range(2)))
UNIV = frozenset(OMEGA)


def block(atoms):
    return {
        frozenset().union(*(atoms[i] for i in range(len(atoms)) if mask >> i & 1))
        for mask in range(1 << len(atoms))
    }


def generated(generators):
    out = {frozenset(), UNIV, *generators}
    while True:
        old = set(out)
        out |= {UNIV - x for x in old}
        out |= {x & y for x in old for y in old}
        if out == old:
            return out


def extreme(carrier, x, y, upper):
    candidates = ([z for z in carrier if x <= z and y <= z] if upper else
                  [z for z in carrier if z <= x and z <= y])
    extrema = [z for z in candidates if not any(
        z != w and ((w < z) if upper else (z < w)) for w in candidates
    )]
    return extrema[0] if len(extrema) == 1 else None


def atoms_of(boolean_block):
    return sorted(
        [x for x in boolean_block if x and not any(y < x for y in boolean_block if y)],
        key=lambda x: sorted(x),
    )


def build():
    b = [frozenset(w for w in OMEGA if w[0] == i) for i in range(4)]
    a = [
        frozenset(w for w in OMEGA if w[0] in side and w[1] == bit)
        for side in ({0, 1}, {2, 3}) for bit in range(2)
    ]
    c = [
        frozenset(w for w in OMEGA if w[0] in side and w[2] == bit)
        for side in ({0, 2}, {1, 3}) for bit in range(2)
    ]
    adec = ((b[0:2], a[0:2]), (b[2:4], a[2:4]))
    cdec = (((b[0], b[2]), c[0:2]), ((b[1], b[3]), c[2:4]))
    blocks = {}
    for x, y in itertools.product(range(2), repeat=2):
        blocks[f"A{x}{y}"] = block((*adec[0][x], *adec[1][y]))
        blocks[f"C{x}{y}"] = block((*cdec[0][x], *cdec[1][y]))
    del blocks["C00"]  # C00=A00 is the common original block.

    carrier = set().union(*blocks.values())
    meet = {(x, y): extreme(carrier, x, y, False) for x in carrier for y in carrier}
    join = {(x, y): extreme(carrier, x, y, True) for x in carrier for y in carrier}
    lattice = all(z is not None for z in (*meet.values(), *join.values()))
    compatible = lambda x, y: join[meet[x, y], meet[x, UNIV - y]] == x
    centre = {x for x in carrier if all(compatible(x, y) for y in carrier)}
    orthomodular = lattice and all(
        join[x, meet[y, UNIV - x]] == y for x in carrier for y in carrier if x <= y
    )

    triangle_names = ("A01", "C01", "A10")
    triangle = [blocks[name] for name in triangle_names]
    interfaces = [triangle[i] & triangle[j] for i, j in ((0, 1), (0, 2), (1, 2))]
    incident_closures = [
        generated((triangle[i] & triangle[j]) | (triangle[i] & triangle[k]))
        for i, j, k in ((0, 1, 2), (1, 0, 2), (2, 0, 1))
    ]
    full_boundaries = [
        generated(set().union(*(value & other for other in blocks.values() if other != value)))
        for value in blocks.values()
    ]

    names = tuple(blocks)
    atoms = {name: atoms_of(value) for name, value in blocks.items()}
    coherent = []
    for values in itertools.product(range(4), repeat=len(names)):
        if all(
            all((atoms[names[i]][values[i]] <= e) == (atoms[names[j]][values[j]] <= e)
                for e in blocks[names[i]] & blocks[names[j]])
            for i in range(len(names)) for j in range(i + 1, len(names))
        ):
            coherent.append(values)
    point_states = {
        tuple(next(i for i, atom in enumerate(atoms[name]) if point in atom) for name in names)
        for point in OMEGA
    }
    positions = [names.index(name) for name in triangle_names]
    global_triangle = {tuple(values[i] for i in positions) for values in coherent}
    local_triangle = {
        values for values in itertools.product(range(4), repeat=3)
        if all(
            all((atoms[triangle_names[i]][values[i]] <= e) ==
                (atoms[triangle_names[j]][values[j]] <= e)
                for e in triangle[i] & triangle[j])
            for i in range(3) for j in range(i + 1, 3)
        )
    }

    return {
        "schema": SCHEMA,
        "scope": "one explicit finite 56-event completion; no multi-block or infinite classification",
        "selected_triangle": list(triangle_names),
        "carrier": {
            "points": len(OMEGA),
            "events": len(carrier),
            "maximal_block_count": len(blocks),
            "maximal_block_sizes": sorted(map(len, blocks.values())),
        },
        "transverse_triangle": {
            "pairwise_interface_sizes": [len(x) for x in interfaces],
            "interfaces_distinct_at_each_endpoint": all(
                triangle[i] & triangle[j] != triangle[i] & triangle[k]
                for i, j, k in ((0, 1, 2), (1, 0, 2), (2, 0, 1))
            ),
            "incident_joint_closure_sizes": [len(x) for x in incident_closures],
            "incident_joint_closures_proper": all(
                incident_closures[i] < triangle[i] for i in range(3)
            ),
            "nontrivial_interface_events_noncentral": all(
                event not in centre for interface in interfaces
                for event in interface - {frozenset(), UNIV}
            ),
        },
        "completion_gates": {
            "closed_under_complement": all(UNIV - x in carrier for x in carrier),
            "closed_under_disjoint_binary_union": all(
                x | y in carrier for x in carrier for y in carrier if x.isdisjoint(y)
            ),
            "latticehood": lattice,
            "orthomodularity": orthomodular,
            "sigma_completeness_by_finiteness": lattice,
            "centre_size": len(centre),
            "trivial_centre": centre == {frozenset(), UNIV},
            "all_named_blocks_maximal": all(
                all(compatible(x, y) for x in value for y in value) and
                all(any(not compatible(x, y) for y in value) for x in carrier - value)
                for value in blocks.values()
            ),
            "full_maximal_boundary_sizes": sorted(map(len, full_boundaries)),
            "full_maximal_boundaries_saturated": all(
                boundary == value for boundary, value in zip(full_boundaries, blocks.values())
            ),
        },
        "state_gates": {
            "global_coherent_block_states": len(coherent),
            "global_states_equal_point_evaluations": set(coherent) == point_states,
            "selected_triangle_coherent_states": len(local_triangle),
            "selected_triangle_extendable_states": len(global_triangle),
            "every_selected_triangle_state_extends": local_triangle == global_triangle,
            "point_evaluations_order_separate": all(
                x <= y or bool(x - y) for x in carrier for y in carrier
            ),
            "phi_tame_by_finiteness": True,
            "sigma_essential_state": False,
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    text = json.dumps(build(), indent=2, sort_keys=True) + "\n"
    args.output.write_text(text) if args.output else print(text, end="")
