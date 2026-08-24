#!/usr/bin/env python3
"""Independent bit-mask verifier for the diagonal-overlap completion."""

import hashlib
import itertools
import json
from pathlib import Path

NAMES = ("A00", "A01", "C01", "A10", "A11")
old = tuple(itertools.product(range(4), range(2), range(2)))
ev = lambda f: frozenset(p for p in old if f(p))
b = [ev(lambda p, i=i: p[0] == i) for i in range(4)]
a = [ev(lambda p, s=s, v=v: p[0] in s and p[1] == v)
     for s in ({0, 1}, {2, 3}) for v in range(2)]
c = [ev(lambda p, s=s, v=v: p[0] in s and p[2] == v)
     for s in ({0, 2}, {1, 3}) for v in range(2)]
parts = {"A00": (*b[:2], *b[2:]), "A01": (*b[:2], *a[2:]),
         "C01": (b[0], b[2], *c[2:]), "A10": (*a[:2], *b[2:]),
         "A11": (*a[:2], *a[2:])}
q, r = b[0] | b[1], b[0] | b[2]

# On the common old region B0 retain only diagonal coordinate pairs.
points = []
for p in old:
    if p in q & r:
        points.extend((p, i, i) for i in range(2))
    else:
        xs, ys = (range(2) if p in q else (None,)), (range(2) if p in r else (None,))
        points.extend((p, x, y) for x in xs for y in ys)
points.sort()
full = (1 << len(points)) - 1


def powerset_union(atoms):
    ans = {0}
    for atom in atoms:
        ans |= {x | atom for x in tuple(ans)}
    return ans


named = {}
for name, partition in parts.items():
    sees_q = any(frozenset().union(*z) == q for k in range(5)
                 for z in itertools.combinations(partition, k))
    sees_r = any(frozenset().union(*z) == r for k in range(5)
                 for z in itertools.combinations(partition, k))
    atoms = []
    for atom in partition:
        for x in (range(2) if sees_q and atom <= q else (None,)):
            for y in (range(2) if sees_r and atom <= r else (None,)):
                cell = sum(1 << i for i, (p, px, py) in enumerate(points)
                           if p in atom and (x is None or px == x)
                           and (y is None or py == y))
                if cell:
                    atoms.append(cell)
    assert sum(atoms) == full and all(x & y == 0 for x, y in itertools.combinations(atoms, 2))
    named[name] = powerset_union(atoms)

raw = set().union(*named.values())
raw_hash = hashlib.sha256("\n".join(
    sorted(format(x, f"0{len(points)}b")[::-1] for x in raw)).encode()).hexdigest()
carrier, rounds = set(raw), [len(raw)]
while True:
    before = set(carrier)
    carrier |= {full ^ x for x in tuple(carrier)}
    snapshot = tuple(carrier)
    carrier |= {x | y for i, x in enumerate(snapshot) for y in snapshot[i:] if x & y == 0}
    rounds.append(len(carrier))
    if carrier == before:
        break
events = sorted(carrier)
where = {x: i for i, x in enumerate(events)}
descending = sorted(events, key=lambda x: (-x.bit_count(), x))
meets = {}


def meet(x, y):
    cut = x & y
    if cut not in meets:
        candidates = [z for z in descending if z & ~cut == 0]
        maximum = candidates[0]
        assert all(z & ~maximum == 0 for z in candidates)
        meets[cut] = maximum
    return meets[cut]


def join(x, y):
    return full ^ meet(full ^ x, full ^ y)


commutation = {}


def commutes(x, y):
    key = tuple(sorted((x, y)))
    if key not in commutation:
        commutation[key] = join(meet(x, y), meet(x, full ^ y)) == x
    return commutation[key]


assert all(full ^ x in carrier for x in events)
assert all(x | y in carrier for i, x in enumerate(events) for y in events[i:] if x & y == 0)
assert all(join(x, meet(y, full ^ x)) == y for x in events for y in events if x & ~y == 0)
assert [x for x in events if all(commutes(x, y) for y in events)] == [0, full]

# Exhaustive maximal compatibility cliques.
vertices = events[1:-1]
adj = []
for i, x in enumerate(vertices):
    adj.append(sum(1 << j for j, y in enumerate(vertices) if i != j and commutes(x, y)))
blocks = []


def bron(chosen, possible, excluded):
    if not possible and not excluded:
        blocks.append(frozenset({0, full, *(vertices[i] for i in chosen)}))
        return
    pool = possible | excluded
    if pool:
        indices = [i for i in range(len(vertices)) if pool >> i & 1]
        pivot = max(indices, key=lambda i: (possible & adj[i]).bit_count())
        extension = possible & ~adj[pivot]
    else:
        extension = possible
    while extension:
        bit = extension & -extension
        i = bit.bit_length() - 1
        bron(chosen + (i,), possible & adj[i], excluded & adj[i])
        possible &= ~bit
        excluded |= bit
        extension &= ~bit


bron((), (1 << len(vertices)) - 1, 0)
blocks.sort(key=lambda x: (-len(x), tuple(sorted(x))))

# Exhaust all overlap-compatible block ultrafilters.
atoms = [[x for x in block if x and not any(y and y != x and y & ~x == 0 for y in block)]
         for block in blocks]
order = sorted(range(len(blocks)), key=lambda i: len(atoms[i]))
selected, profiles = {}, set()


def compatible(i, atom):
    return all((atom & ~event == 0) == (other & ~event == 0)
               for j, other in selected.items() for event in blocks[i] & blocks[j])


def enumerate_states(depth):
    if depth == len(order):
        profiles.add(tuple(next(atom & ~event == 0 for i, atom in selected.items()
                                if event in blocks[i]) for event in events))
        return
    i = order[depth]
    for atom in atoms[i]:
        if compatible(i, atom):
            selected[i] = atom
            enumerate_states(depth + 1)
            del selected[i]


enumerate_states(0)
point_profiles = {tuple(bool(event >> p & 1) for event in events) for p in range(len(points))}
assert profiles == point_profiles
q0 = sum(1 << i for i, (p, x, _) in enumerate(points) if p[0] in (0, 1) and x == 0)
r0 = sum(1 << i for i, (p, _, y) in enumerate(points) if p[0] in (0, 2) and y == 0)
b0 = sum(1 << i for i, (p, _, _) in enumerate(points) if p[0] == 0)
relation = sorted({(int(s[where[q0]]), int(s[where[r0]])) for s in profiles})
conditioned = sorted({(int(s[where[q0]]), int(s[where[r0]])) for s in profiles if s[where[b0]]})

claim = json.loads(Path(__file__).with_name(
    "five_block_nonatomic_diagonal_completion.json").read_text())
assert len(points) == claim["points"] == 28
assert len(raw) == claim["raw_events"] == 264
assert raw_hash == claim["raw_structural_audit"]["event_sha256"]
assert all(full ^ x in raw for x in raw)
raw_failure = claim["raw_structural_audit"]["first_disjoint_union_failure"]
raw_left, raw_right = int(raw_failure["left_mask"], 16), int(raw_failure["right_mask"], 16)
raw_union = int(raw_failure["union_mask"], 16)
assert raw_left in raw and raw_right in raw and raw_left & raw_right == 0
assert raw_left | raw_right == raw_union and raw_union not in raw
raw_uppers = [z for z in raw if raw_left & ~z == 0 and raw_right & ~z == 0]
raw_minimal_uppers = [z for z in raw_uppers if not any(
    z != w and w & ~z == 0 for w in raw_uppers)]
assert len(raw_minimal_uppers) == claim["raw_structural_audit"][
    "first_extrema_failure"]["upper_extrema"] == 2
assert rounds == claim["closure_round_event_counts"] == [264, 392, 392]
assert len(events) == claim["events"] == 392
assert hashlib.sha256("\n".join(map(hex, events)).encode()).hexdigest() == claim["event_sha256"]
assert sum(x & ~y == 0 for x in events for y in events) == claim["ordered_comparable_pairs"]
assert sum(commutes(x, y) for x in events for y in events) == claim["ordered_compatible_pairs"]
assert len(meets) == claim["distinct_intersection_cuts"]
records = [{"id": i, "size": len(block),
            "sha256": hashlib.sha256("\n".join(map(hex, sorted(block))).encode()).hexdigest(),
            "contains_named_blocks": [name for name in NAMES if named[name] <= block]}
           for i, block in enumerate(blocks)]
assert records == claim["maximal_compatibility_blocks"]
assert {name: [i for i, block in enumerate(blocks) if named[name] <= block] for name in NAMES} == claim["named_block_containers"]
assert len(profiles) == len(point_profiles) == 20
assert hex(q0) == claim["state_audit"]["q0_mask"]
assert hex(r0) == claim["state_audit"]["r0_mask"]
assert hex(b0) == claim["state_audit"]["joint_selector_region_mask"]
assert relation == [tuple(x) for x in claim["state_audit"]["q0_r0_relation"]]
assert conditioned == [tuple(x) for x in claim["state_audit"]["joint_charged_q0_r0_relation"]]
assert relation == [(0, 0), (0, 1), (1, 0), (1, 1)]
assert conditioned == [(0, 0), (1, 1)]

print("PASS: independent diagonal completion reconstruction and nine-block census")
print("PASS: 20 global states are point states; global relation full")
print("PASS: B0-conditioned relation is diagonal")
