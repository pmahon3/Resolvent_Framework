#!/usr/bin/env python3
"""Audit the smallest crossed-interface three-block pasting candidate.

The distinguished four-atom Boolean block B has crossing two-atom events
`a={0,1}` and `b={0,2}`.  Block Ca replaces the two decompositions below
`a,a^c`; block Cb does the same below `b,b^c`.  Events are represented on
the complete set of compatible two-valued block valuations.  The script
checks whether the union of the three represented Boolean blocks is a
concrete logic and a lattice, and reports the first exact obstruction.
"""

from itertools import product


def powerset_events(atom_truth_sets):
    out = set()
    for mask in range(1 << len(atom_truth_sets)):
        event = frozenset().union(
            *(atom_truth_sets[i] for i in range(len(atom_truth_sets)) if mask >> i & 1)
        )
        out.add(event)
    return out


# A valuation chooses one B atom, one of two Ca refinements on the matching
# side of a, and one of two Cb refinements on the matching side of b.
omega = tuple(product(range(4), range(2), range(2)))
univ = frozenset(omega)

b_atoms = [frozenset(v for v in omega if v[0] == i) for i in range(4)]
ca_atoms = [
    frozenset(v for v in omega if (v[0] in side and v[1] == refinement))
    for side in ({0, 1}, {2, 3})
    for refinement in range(2)
]
cb_atoms = [
    frozenset(v for v in omega if (v[0] in side and v[2] == refinement))
    for side in ({0, 2}, {1, 3})
    for refinement in range(2)
]

blocks = {
    "B": powerset_events(b_atoms),
    "Ca": powerset_events(ca_atoms),
    "Cb": powerset_events(cb_atoms),
}
logic = set().union(*blocks.values())


def labels(event):
    return [name for name, block in blocks.items() if event in block]


missing_disjoint_union = None
for x in logic:
    for y in logic:
        if x.isdisjoint(y) and x | y not in logic:
            missing_disjoint_union = (x, y, x | y)
            break
    if missing_disjoint_union:
        break

missing_meet = None
missing_join = None
for x in logic:
    for y in logic:
        lowers = [z for z in logic if z <= x and z <= y]
        maximal_lowers = [z for z in lowers if not any(z < w for w in lowers)]
        uppers = [z for z in logic if x <= z and y <= z]
        minimal_uppers = [z for z in uppers if not any(w < z for w in uppers)]
        if len(maximal_lowers) != 1 and missing_meet is None:
            missing_meet = (x, y, maximal_lowers)
        if len(minimal_uppers) != 1 and missing_join is None:
            missing_join = (x, y, minimal_uppers)

def summarize(event):
    return {"size": len(event), "blocks": labels(event)}


print({
    "carrier_points": len(omega),
    "block_sizes": {name: len(block) for name, block in blocks.items()},
    "logic_size": len(logic),
    "pairwise_intersection_sizes": {
        "B_Ca": len(blocks["B"] & blocks["Ca"]),
        "B_Cb": len(blocks["B"] & blocks["Cb"]),
        "Ca_Cb": len(blocks["Ca"] & blocks["Cb"]),
    },
    "closed_under_complement": all(univ - x in logic for x in logic),
    "closed_under_disjoint_binary_union": missing_disjoint_union is None,
    "is_lattice": missing_meet is None and missing_join is None,
    "first_missing_disjoint_union": None if missing_disjoint_union is None else {
        "left": summarize(missing_disjoint_union[0]),
        "right": summarize(missing_disjoint_union[1]),
        "union_size": len(missing_disjoint_union[2]),
    },
    "first_missing_meet": None if missing_meet is None else {
        "left": summarize(missing_meet[0]),
        "right": summarize(missing_meet[1]),
        "maximal_lower_bounds": [summarize(z) for z in missing_meet[2]],
    },
    "first_missing_join": None if missing_join is None else {
        "left": summarize(missing_join[0]),
        "right": summarize(missing_join[1]),
        "minimal_upper_bounds": [summarize(z) for z in missing_join[2]],
    },
})
