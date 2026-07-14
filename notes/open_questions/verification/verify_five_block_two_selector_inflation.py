#!/usr/bin/env python3
"""Independent bit-mask reconstruction of the two-selector certificates."""

import hashlib
import itertools
import json
from pathlib import Path

NAMES = ("A00", "A01", "C01", "A10", "A11")


def unions(atoms):
    return {sum(atoms[i] for i in range(len(atoms)) if mask >> i & 1)
            for mask in range(1 << len(atoms))}


def reconstruct(n, m):
    old_points = tuple(itertools.product(range(4), range(2), range(2)))
    def event(pred):
        return frozenset(p for p in old_points if pred(p))
    base = [event(lambda p, i=i: p[0] == i) for i in range(4)]
    aa = [event(lambda p, side=side, bit=bit: p[0] in side and p[1] == bit)
          for side in ({0, 1}, {2, 3}) for bit in range(2)]
    cc = [event(lambda p, side=side, bit=bit: p[0] in side and p[2] == bit)
          for side in ({0, 2}, {1, 3}) for bit in range(2)]
    old_atoms = {
        "A00": (*base[:2], *base[2:]), "A01": (*base[:2], *aa[2:]),
        "A10": (*aa[:2], *base[2:]), "A11": (*aa[:2], *aa[2:]),
        "C01": (base[0], base[2], *cc[2:]),
    }
    q, r = base[0], aa[2]
    expanded = []
    for p in old_points:
        expanded.extend(((p, "q", i) for i in range(n)) if p in q else
                        ((p, "r", i) for i in range(m)) if p in r else
                        ((p, "o", 0),))
    # Match the producer's canonical tuple order (tag, old point, coordinate).
    expanded = sorted(expanded, key=lambda z: (z[1], z[0], z[2]))
    pos = {point: i for i, point in enumerate(expanded)}
    full = (1 << len(expanded)) - 1
    def lift(x): return sum(1 << i for i, z in enumerate(expanded) if z[0] in x)
    blocks = {}
    for name in NAMES:
        atoms = []
        for atom in old_atoms[name]:
            if atom == q:
                atoms.extend(sum(1 << i for i, z in enumerate(expanded)
                                 if z[1] == "q" and z[2] == k) for k in range(n))
            elif atom == r:
                atoms.extend(sum(1 << i for i, z in enumerate(expanded)
                                 if z[1] == "r" and z[2] == k) for k in range(m))
            else:
                atoms.append(lift(atom))
        blocks[name] = unions(atoms)
    lattice = set().union(*(blocks[name] for name in NAMES))
    below = lambda x, y: x & ~y == 0
    disjoint = lambda x, y: x & y == 0
    def extreme(x, y, upper):
        cand = ([z for z in lattice if below(x, z) and below(y, z)] if upper else
                [z for z in lattice if below(z, x) and below(z, y)])
        ans = [z for z in cand if not any(z != w and
               (below(w, z) if upper else below(z, w)) for w in cand)]
        assert len(ans) == 1
        return ans[0]
    meet = {(x, y): extreme(x, y, False) for x in lattice for y in lattice}
    join = {(x, y): extreme(x, y, True) for x in lattice for y in lattice}
    commute = lambda x, y: join[meet[x, y], meet[x, full ^ y]] == x
    assert all((full ^ x) in lattice for x in lattice)
    assert all((x | y) in lattice for x in lattice for y in lattice if disjoint(x, y))
    assert all(join[x, meet[y, full ^ x]] == y for x in lattice for y in lattice if below(x, y))
    assert {x for x in lattice if all(commute(x, y) for y in lattice)} == {0, full}
    for name in NAMES:
        assert all(commute(x, y) for x in blocks[name] for y in blocks[name])
        assert all(any(not commute(x, y) for y in blocks[name]) for x in lattice - blocks[name])
    enc = sorted(format(x, f"0{len(expanded)}b")[::-1] for x in lattice)
    return {
        "points": len(expanded), "events": len(lattice),
        "block_sizes": {name: len(blocks[name]) for name in NAMES},
        "ordered_pairs": len(lattice) ** 2,
        "ordered_disjoint_pairs": sum(disjoint(x, y) for x in lattice for y in lattice),
        "ordered_compatible_pairs": sum(commute(x, y) for x in lattice for y in lattice),
        "comparable_ordered_pairs": sum(below(x, y) for x in lattice for y in lattice),
        "centre_size": 2,
        "event_sha256": hashlib.sha256("\n".join(enc).encode()).hexdigest(),
    }


receipt = json.loads(Path(__file__).with_name(
    "five_block_two_selector_inflation_schema.json").read_text())
assert receipt["schema"] == "five-block-distinct-two-selector-inflation-v1"
assert receipt["selector_masks"] == ["0x000f", "0x3300"]
pairs = ((2, 2), (2, 3), (3, 2), (2, 4), (3, 3), (4, 2))
assert [x["fibre_atoms"] for x in receipt["approximants"]] == [list(x) for x in pairs]
for pair, claim in zip(pairs, receipt["approximants"]):
    fresh = reconstruct(*pair)
    for key, value in fresh.items():
        assert claim[key] == value, (pair, key, claim[key], value)
    assert all(claim["checks"].values())
assert [x["events"] for x in receipt["approximants"]] == [116, 196, 212, 356, 356, 404]
print("PASS: independent bit-mask reconstruction matches all certificates")
