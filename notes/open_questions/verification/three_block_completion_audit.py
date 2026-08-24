#!/usr/bin/env python3
"""Exhaustive audit of the 56-event centre-free completion.

Starting with the crossed-interface carrier from
`three_block_interface_audit.py`, complete B∪Ca intervalwise as
MO2×MO2, do the same for B∪Cb, and take the union La∪Lb.  The audit checks
the concrete-logic, lattice, orthomodularity, maximal-block, centre,
original-interface, and overlap-generated-boundary claims.
"""

from itertools import product


def powerset_events(atoms):
    return {
        frozenset().union(*(atoms[i] for i in range(len(atoms)) if mask >> i & 1))
        for mask in range(1 << len(atoms))
    }


omega = tuple(product(range(4), range(2), range(2)))
univ = frozenset(omega)

b_atoms = [frozenset(v for v in omega if v[0] == i) for i in range(4)]
ca_atoms = [
    frozenset(v for v in omega if v[0] in side and v[1] == refinement)
    for side in ({0, 1}, {2, 3})
    for refinement in range(2)
]
cb_atoms = [
    frozenset(v for v in omega if v[0] in side and v[2] == refinement)
    for side in ({0, 2}, {1, 3})
    for refinement in range(2)
]

B = powerset_events(b_atoms)
Ca = powerset_events(ca_atoms)
Cb = powerset_events(cb_atoms)


def mo2_interval(first_decomposition, second_decomposition):
    side = first_decomposition[0] | first_decomposition[1]
    assert side == second_decomposition[0] | second_decomposition[1]
    return {frozenset(), side, *first_decomposition, *second_decomposition}


def interval_product(left, right):
    return {x | y for x in left for y in right}


La = interval_product(
    mo2_interval(b_atoms[0:2], ca_atoms[0:2]),
    mo2_interval(b_atoms[2:4], ca_atoms[2:4]),
)
Lb = interval_product(
    mo2_interval((b_atoms[0], b_atoms[2]), cb_atoms[0:2]),
    mo2_interval((b_atoms[1], b_atoms[3]), cb_atoms[2:4]),
)
logic = La | Lb
events = tuple(logic)


def unique_extrema(candidates, maximal):
    extrema = [
        z for z in candidates
        if not any((z < w if maximal else w < z) for w in candidates)
    ]
    return extrema[0] if len(extrema) == 1 else None


meet = {}
join = {}
for x in events:
    for y in events:
        meet[x, y] = unique_extrema(
            [z for z in events if z <= x and z <= y], maximal=True
        )
        join[x, y] = unique_extrema(
            [z for z in events if x <= z and y <= z], maximal=False
        )

is_lattice = all(z is not None for z in meet.values()) and all(
    z is not None for z in join.values()
)


def compatible(x, y):
    # OML commutation identity x = (x∧y)∨(x∧y⊥).
    return join[meet[x, y], meet[x, univ - y]] == x


def maximal_cliques(vertices, adjacent):
    out = []

    def bron_kerbosch(r, p, x):
        if not p and not x:
            out.append(frozenset(r))
            return
        pivot = next(iter(p | x), None)
        candidates = p - ({w for w in vertices if adjacent(pivot, w)} if pivot else set())
        for v in tuple(candidates):
            neighbours = {w for w in vertices if w != v and adjacent(v, w)}
            bron_kerbosch(r | {v}, p & neighbours, x & neighbours)
            p.remove(v)
            x.add(v)

    bron_kerbosch(set(), set(vertices), set())
    return out


max_blocks = maximal_cliques(events, lambda x, y: x != y and compatible(x, y)) if is_lattice else []


def generated_boolean_algebra(generators):
    closure = {frozenset(), univ, *generators}
    changed = True
    while changed:
        old = set(closure)
        closure |= {univ - x for x in old}
        closure |= {x & y for x in old for y in old}
        changed = closure != old
    return closure


boundaries = []
for block in max_blocks:
    overlap_union = set().union(*(block & other for other in max_blocks if other != block))
    boundaries.append(generated_boolean_algebra(overlap_union))

orthomodular = is_lattice and all(
    join[x, meet[y, univ - x]] == y
    for x in events for y in events if x <= y
)
centre = {x for x in events if all(compatible(x, y) for y in events)} if is_lattice else set()

print({
    "carrier_points": len(omega),
    "La_size": len(La),
    "Lb_size": len(Lb),
    "La_Lb_intersection_size": len(La & Lb),
    "logic_size": len(logic),
    "closed_under_complement": all(univ - x in logic for x in events),
    "closed_under_disjoint_binary_union": all(
        x | y in logic for x in events for y in events if x.isdisjoint(y)
    ),
    "is_lattice": is_lattice,
    "orthomodular": orthomodular,
    "maximal_block_count": len(max_blocks),
    "maximal_block_sizes": sorted(len(block) for block in max_blocks),
    "original_blocks_maximal": {
        "B": frozenset(B) in max_blocks,
        "Ca": frozenset(Ca) in max_blocks,
        "Cb": frozenset(Cb) in max_blocks,
    },
    "original_overlap_sizes": {
        "B_Ca": len(B & Ca),
        "B_Cb": len(B & Cb),
        "Ca_Cb": len(Ca & Cb),
    },
    "centre_size": len(centre),
    "centre_is_trivial": centre == {frozenset(), univ},
    "boundary_sizes": sorted(len(boundary) for boundary in boundaries),
    "all_boundaries_saturate_blocks": all(
        boundary == set(block) for boundary, block in zip(boundaries, max_blocks)
    ),
})
