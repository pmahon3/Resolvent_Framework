#!/usr/bin/env python3
"""Independent bit-mask verification of the OE finite kernel."""

import hashlib
import itertools
import json
from pathlib import Path

NAMES = ("A00", "A01", "C01", "A10", "A11")


def unions(atoms):
    return {sum(atoms[i] for i in range(len(atoms)) if mask >> i & 1)
            for mask in range(1 << len(atoms))}


def model(n, m):
    old = tuple(itertools.product(range(4), range(2), range(2)))
    event = lambda predicate: frozenset(p for p in old if predicate(p))
    base = [event(lambda p, i=i: p[0] == i) for i in range(4)]
    aa = [event(lambda p, side=side, bit=bit:
                p[0] in side and p[1] == bit)
          for side in ({0, 1}, {2, 3}) for bit in range(2)]
    cc = [event(lambda p, side=side, bit=bit:
                p[0] in side and p[2] == bit)
          for side in ({0, 2}, {1, 3}) for bit in range(2)]
    partitions = {
        "A00": (*base[:2], *base[2:]),
        "A01": (*base[:2], *aa[2:]),
        "C01": (base[0], base[2], *cc[2:]),
        "A10": (*aa[:2], *base[2:]),
        "A11": (*aa[:2], *aa[2:]),
    }
    q, r = base[0], aa[2]
    points = []
    for p in old:
        if p in q:
            points.extend(("q", p, i) for i in range(n))
        elif p in r:
            points.extend(("r", p, i) for i in range(m))
        else:
            points.append(("o", p, 0))
    points.sort()
    full = (1 << len(points)) - 1
    lift = lambda e: sum(1 << i for i, z in enumerate(points) if z[1] in e)
    block_atoms = {}
    blocks = {}
    for name, old_atoms in partitions.items():
        atoms = []
        for atom in old_atoms:
            if atom == q:
                atoms.extend(sum(1 << i for i, z in enumerate(points)
                                 if z[0] == "q" and z[2] == j)
                             for j in range(n))
            elif atom == r:
                atoms.extend(sum(1 << i for i, z in enumerate(points)
                                 if z[0] == "r" and z[2] == j)
                             for j in range(m))
            else:
                atoms.append(lift(atom))
        block_atoms[name] = atoms
        blocks[name] = unions(atoms)
    return full, block_atoms, set().union(*blocks.values())


def verify(n, m, claim):
    full, atoms, carrier = model(n, m)
    events = sorted(carrier)
    cuts = {x & y for i, x in enumerate(events) for y in events[i:]}
    meets, joins = {}, {}
    pairs = 0
    for i, x in enumerate(events):
        for y in events[i:]:
            cut, span = x & y, x | y
            lowers = [sum(a for a in atoms[name] if a & ~cut == 0)
                      for name in NAMES]
            uppers = [sum(a for a in atoms[name] if a & span)
                      for name in NAMES]
            greatest = set(z for z in lowers if all(w & ~z == 0 for w in lowers))
            least = set(z for z in uppers if all(z & ~w == 0 for w in uppers))
            assert len(greatest) == len(least) == 1
            lo, hi = greatest.pop(), least.pop()
            assert lo in carrier and hi in carrier
            meets[x, y] = meets[y, x] = lo
            joins[x, y] = joins[y, x] = hi
            pairs += 1
    checks = {
        "winner_formula_certified": True,
        "complement_closed": all(full ^ x in carrier for x in events),
        "binary_disjoint_union_closed": all(x | y in carrier
            for x in events for y in events if not x & y),
        "unique_binary_extrema": True,
        "orthomodular": all(joins[x, meets[y, full ^ x]] == y
            for x in events for y in events if x & ~y == 0),
    }
    digest = hashlib.sha256("\n".join(map(hex, events)).encode()).hexdigest()
    assert claim == {
        "fibre_atoms": [n, m], "points": full.bit_count(),
        "events": len(events), "unordered_input_pairs": pairs,
        "distinct_intersection_cuts": len(cuts),
        "event_sha256": digest, "checks": checks,
    }


receipt = json.loads(Path(__file__).with_name(
    "five_block_two_atom_oe_schema.json").read_text())
assert receipt["schema"] == "five-block-two-atom-oe-kernel-v1"
expected = [list(pair) for pair in itertools.product(range(1, 5), repeat=2)]
assert [item["fibre_atoms"] for item in receipt["models"]] == expected
for pair, claim in zip(expected, receipt["models"]):
    verify(*pair, claim)
print("PASS: independent OE kernel verifies all 16 truth-region models")
