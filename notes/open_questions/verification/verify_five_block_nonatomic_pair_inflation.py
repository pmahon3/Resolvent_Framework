#!/usr/bin/env python3
"""Independent bit-mask verification of the non-atomic P2 x P2 failure.

This reconstruction does not import the producer.  It builds the original
five block atom partitions directly, refines their atoms by the two selector
coordinates, and treats events as integer bit masks.
"""

import hashlib
import itertools
import json
from pathlib import Path


NAMES = ("A00", "A01", "C01", "A10", "A11")
old_points = tuple(itertools.product(range(4), range(2), range(2)))


def old_event(predicate):
    return frozenset(p for p in old_points if predicate(p))


base = [old_event(lambda p, i=i: p[0] == i) for i in range(4)]
a = [old_event(lambda p, side=side, bit=bit: p[0] in side and p[1] == bit)
     for side in ({0, 1}, {2, 3}) for bit in range(2)]
c = [old_event(lambda p, side=side, bit=bit: p[0] in side and p[2] == bit)
     for side in ({0, 2}, {1, 3}) for bit in range(2)]
partitions = {
    "A00": (*base[:2], *base[2:]),
    "A01": (*base[:2], *a[2:]),
    "C01": (base[0], base[2], *c[2:]),
    "A10": (*a[:2], *base[2:]),
    "A11": (*a[:2], *a[2:]),
}
q, r = base[0] | base[1], base[0] | base[2]

# Canonical point order agrees with sorting (old point, x, y).  For any fixed
# old point, each coordinate is either always an integer or always None.
points = []
for p in old_points:
    xs = range(2) if p in q else (None,)
    ys = range(2) if p in r else (None,)
    points.extend((p, x, y) for x in xs for y in ys)
points = sorted(points)
full = (1 << len(points)) - 1


def unions(atoms):
    return {sum(atoms[i] for i in range(len(atoms)) if selector >> i & 1)
            for selector in range(1 << len(atoms))}


blocks = {}
for name, partition in partitions.items():
    sees_q = any(frozenset().union(*choice) == q
                 for k in range(len(partition) + 1)
                 for choice in itertools.combinations(partition, k))
    sees_r = any(frozenset().union(*choice) == r
                 for k in range(len(partition) + 1)
                 for choice in itertools.combinations(partition, k))
    atoms = []
    for atom in partition:
        xs = range(2) if sees_q and atom <= q else (None,)
        ys = range(2) if sees_r and atom <= r else (None,)
        for x in xs:
            for y in ys:
                atoms.append(sum(1 << i for i, (p, px, py) in enumerate(points)
                                 if p in atom and (x is None or px == x)
                                 and (y is None or py == y)))
    assert sum(atoms) == full
    assert all(x & y == 0 for x, y in itertools.combinations(atoms, 2))
    blocks[name] = unions(atoms)

carrier = set().union(*blocks.values())
below = lambda x, y: x & ~y == 0


def minimal_upper_bounds(x, y):
    upper = [z for z in carrier if below(x, z) and below(y, z)]
    return sorted(z for z in upper if not any(z != w and below(w, z) for w in upper))


claim = json.loads(Path(__file__).with_name(
    "five_block_nonatomic_pair_inflation.json").read_text())
assert claim["schema"] == "five-block-nonatomic-pair-inflation-v1"
assert claim["selector_masks"] == ["0x00ff", "0x0f0f"]
assert len(points) == claim["points"] == 36
assert len(carrier) == claim["events"] == 648
assert {name: len(block) for name, block in blocks.items()} == claim["block_sizes"]

encoding = sorted(format(event, f"0{len(points)}b")[::-1] for event in carrier)
digest = hashlib.sha256("\n".join(encoding).encode()).hexdigest()
assert digest == claim["event_sha256"]
assert sum(x & y == 0 for x in carrier for y in carrier) == claim["ordered_disjoint_pairs"]
assert all((full ^ x) in carrier for x in carrier)

left = int(claim["first_disjoint_union_failure"]["left_mask"], 16)
right = int(claim["first_disjoint_union_failure"]["right_mask"], 16)
union = int(claim["first_disjoint_union_failure"]["union_mask"], 16)
assert left in carrier and right in carrier
assert left & right == 0 and left | right == union and union not in carrier
assert [left.bit_count(), right.bit_count()] == claim[
    "first_disjoint_union_failure"]["cardinalities"]
assert [name for name in NAMES if left in blocks[name]] == ["A00"]
assert [name for name in NAMES if right in blocks[name]] == ["A10", "A11"]

uppers = minimal_upper_bounds(left, right)
assert len(uppers) == claim["first_extrema_failure"]["upper_extrema"] == 2
assert not below(uppers[0], uppers[1]) and not below(uppers[1], uppers[0])
assert all(below(left, z) and below(right, z) for z in uppers)

print("PASS: independent reconstruction matches counts and event hash")
print("PASS: disjoint pair", hex(left), hex(right), "has missing union", hex(union))
print("PASS: its two incomparable minimal upper bounds are", *(hex(z) for z in uppers))
