#!/usr/bin/env python3
"""Independently reconstruct the selected 44-event boundary survivor."""

import itertools
import json
from pathlib import Path


receipt = json.loads(Path(__file__).with_name(
    "exhaustive_boundary_properness_schema.json"
).read_text())
assert receipt["schema"] == "seven-block-subfamily-boundary-census-v1"
assert receipt["census"]["nonempty_subfamilies"] == 127
assert receipt["census"]["status_counts"] == {"not_concrete_logic": 100, "oml": 27}
assert receipt["census"]["survivor_count"] == 4
assert receipt["census"]["minimum_survivor_event_count"] == 44

omega = tuple(itertools.product(range(4), range(2), range(2)))
univ = frozenset(omega)


def powerset(atoms):
    return {
        frozenset().union(*(atoms[i] for i in range(4) if mask >> i & 1))
        for mask in range(16)
    }


base = [frozenset(w for w in omega if w[0] == i) for i in range(4)]
a = [frozenset(w for w in omega if w[0] in side and w[1] == bit)
     for side in ({0, 1}, {2, 3}) for bit in range(2)]
c = [frozenset(w for w in omega if w[0] in side and w[2] == bit)
     for side in ({0, 2}, {1, 3}) for bit in range(2)]
adec = ((base[0:2], a[0:2]), (base[2:4], a[2:4]))
cdec = (((base[0], base[2]), c[0:2]), ((base[1], base[3]), c[2:4]))
blocks = {}
for x, y in itertools.product(range(2), repeat=2):
    blocks[f"A{x}{y}"] = powerset((*adec[0][x], *adec[1][y]))
    blocks[f"C{x}{y}"] = powerset((*cdec[0][x], *cdec[1][y]))
del blocks["C00"]

chosen = tuple(receipt["selected_survivor"]["blocks"])
assert chosen == ("A00", "A01", "C01", "A10", "A11")
carrier = set().union(*(blocks[name] for name in chosen))
assert len(carrier) == 44
assert all(univ - x in carrier for x in carrier)
assert all(x | y in carrier for x in carrier for y in carrier if x.isdisjoint(y))


def sole_extreme(x, y, upper):
    candidates = ([z for z in carrier if x <= z and y <= z] if upper else
                  [z for z in carrier if z <= x and z <= y])
    extrema = [z for z in candidates if not any(
        z != w and ((w < z) if upper else (z < w)) for w in candidates
    )]
    assert len(extrema) == 1
    return extrema[0]


meet = {(x, y): sole_extreme(x, y, False) for x in carrier for y in carrier}
join = {(x, y): sole_extreme(x, y, True) for x in carrier for y in carrier}
assert all(join[x, meet[y, univ - x]] == y
           for x in carrier for y in carrier if x <= y)


def commutes(x, y):
    return join[meet[x, y], meet[x, univ - y]] == x


assert {x for x in carrier if all(commutes(x, y) for y in carrier)} == {
    frozenset(), univ
}
for name in chosen:
    assert all(commutes(x, y) for x in blocks[name] for y in blocks[name])
    assert all(any(not commutes(x, y) for y in blocks[name])
               for x in carrier - blocks[name])


maximal_compatible_sets = []


def bron_kerbosch(r, p, x):
    if not p and not x:
        maximal_compatible_sets.append(frozenset(r))
        return
    pivot = next(iter(p | x), None)
    pivot_neighbours = ({w for w in carrier if w != pivot and commutes(pivot, w)}
                        if pivot is not None else set())
    for v in tuple(p - pivot_neighbours):
        neighbours = {w for w in carrier if w != v and commutes(v, w)}
        bron_kerbosch(r | {v}, p & neighbours, x & neighbours)
        p.remove(v)
        x.add(v)


bron_kerbosch(set(), set(carrier), set())
assert set(maximal_compatible_sets) == {frozenset(blocks[name]) for name in chosen}


def boolean_closure(generators):
    closure = {frozenset(), univ, *generators}
    while True:
        old = set(closure)
        closure |= {univ - x for x in old}
        closure |= {x & y for x in old for y in old}
        if closure == old:
            return closure


boundaries = {
    name: boolean_closure(set().union(*(
        blocks[name] & blocks[other] for other in chosen if other != name
    )))
    for name in chosen
}
assert {name: len(boundary) for name, boundary in boundaries.items()} == {
    "A00": 16, "A01": 16, "C01": 8, "A10": 16, "A11": 16
}
assert boundaries["C01"] < blocks["C01"]

atoms = {
    name: [x for x in blocks[name] if x and
           not any(y < x for y in blocks[name] if y)]
    for name in chosen
}
coherent = set()
for values in itertools.product(range(4), repeat=5):
    if all(all(
        (atoms[chosen[i]][values[i]] <= event) ==
        (atoms[chosen[j]][values[j]] <= event)
        for event in blocks[chosen[i]] & blocks[chosen[j]])
        for i in range(5) for j in range(i + 1, 5)):
        coherent.add(values)
point_states = {
    tuple(next(i for i, atom in enumerate(atoms[name]) if point in atom)
          for name in chosen)
    for point in omega
}
assert coherent == point_states
assert len(coherent) == 12
triangle = ("A01", "C01", "A10")
positions = [chosen.index(name) for name in triangle]
local_triangle = {
    values for values in itertools.product(range(4), repeat=3)
    if all(all(
        (atoms[triangle[i]][values[i]] <= event) ==
        (atoms[triangle[j]][values[j]] <= event)
        for event in blocks[triangle[i]] & blocks[triangle[j]])
        for i in range(3) for j in range(i + 1, 3))
}
assert len(local_triangle) == 12
assert local_triangle == {tuple(values[i] for i in positions) for values in coherent}
assert all(x <= y or any(point in x - y for point in omega)
           for x in carrier for y in carrier)

print("PASS: independently reconstructed the 44-event OML and its proper exhaustive boundary")
