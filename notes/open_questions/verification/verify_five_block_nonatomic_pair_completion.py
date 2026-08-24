#!/usr/bin/env python3
"""Independent verification of the 1128-event orthogonal completion.

No producer module is imported.  The raw block union, closure rounds, lattice
operations, compatibility graph, maximal cliques, and glued block states are
all reconstructed with integer bit masks.
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
points = []
for p in old_points:
    for x in (range(2) if p in q else (None,)):
        for y in (range(2) if p in r else (None,)):
            points.append((p, x, y))
points.sort()
full = (1 << len(points)) - 1


def all_unions(atoms):
    result = {0}
    for atom in atoms:
        result |= {event | atom for event in tuple(result)}
    return result


named = {}
for name, partition in partitions.items():
    sees_q = any(frozenset().union(*choice) == q
                 for length in range(len(partition) + 1)
                 for choice in itertools.combinations(partition, length))
    sees_r = any(frozenset().union(*choice) == r
                 for length in range(len(partition) + 1)
                 for choice in itertools.combinations(partition, length))
    atoms = []
    for atom in partition:
        for x in (range(2) if sees_q and atom <= q else (None,)):
            for y in (range(2) if sees_r and atom <= r else (None,)):
                atoms.append(sum(1 << i for i, (p, px, py) in enumerate(points)
                                 if p in atom and (x is None or px == x)
                                 and (y is None or py == y)))
    assert sum(atoms) == full
    named[name] = all_unions(atoms)

# Canonical closure under orthocomplement and binary orthogonal join.
carrier = set().union(*named.values())
rounds = [len(carrier)]
while True:
    before = frozenset(carrier)
    carrier.update(full ^ event for event in before)
    snapshot = tuple(carrier)
    carrier.update(x | y for i, x in enumerate(snapshot) for y in snapshot[i:]
                   if x & y == 0)
    rounds.append(len(carrier))
    if carrier == set(before):
        break
events = sorted(carrier)
event_index = {event: i for i, event in enumerate(events)}

# Independently calculate the unique largest carrier event inside each raw
# intersection cut.  This simultaneously checks uniqueness of every meet.
descending = sorted(events, key=lambda event: (-event.bit_count(), event))
meet_by_cut = {}


def meet(x, y):
    cut = x & y
    if cut not in meet_by_cut:
        candidates = [z for z in descending if z & ~cut == 0]
        maximum = candidates[0]
        assert all(z & ~maximum == 0 for z in candidates)
        meet_by_cut[cut] = maximum
    return meet_by_cut[cut]


def join(x, y):
    return full ^ meet(full ^ x, full ^ y)


commute_cache = {}


def commute(x, y):
    key = (x, y) if x <= y else (y, x)
    if key not in commute_cache:
        commute_cache[key] = join(meet(x, y), meet(x, full ^ y)) == x
    return commute_cache[key]


assert all(full ^ x in carrier for x in events)
assert all(x | y in carrier for i, x in enumerate(events) for y in events[i:]
           if x & y == 0)
assert all(join(x, meet(y, full ^ x)) == y
           for x in events for y in events if x & ~y == 0)
centre = [x for x in events if all(commute(x, y) for y in events)]
assert centre == [0, full]

# Independent bit-set Bron--Kerbosch implementation for the complete maximal
# compatibility-clique census.  Universal 0 and 1 are restored afterward.
vertices = events[1:-1]
adjacency = []
for i, x in enumerate(vertices):
    row = 0
    for j, y in enumerate(vertices):
        if i != j and commute(x, y):
            row |= 1 << j
    adjacency.append(row)
maximal = []


def maximal_cliques(chosen, candidates, rejected):
    if candidates == 0 and rejected == 0:
        maximal.append(frozenset({0, full, *(vertices[i] for i in chosen)}))
        return
    pivot_pool = candidates | rejected
    if pivot_pool:
        pool = [i for i in range(len(vertices)) if pivot_pool >> i & 1]
        pivot = max(pool, key=lambda i: (candidates & adjacency[i]).bit_count())
        extension = candidates & ~adjacency[pivot]
    else:
        extension = candidates
    while extension:
        bit = extension & -extension
        i = bit.bit_length() - 1
        maximal_cliques(chosen + (i,), candidates & adjacency[i],
                        rejected & adjacency[i])
        candidates &= ~bit
        rejected |= bit
        extension &= ~bit


maximal_cliques((), (1 << len(vertices)) - 1, 0)
maximal.sort(key=lambda block: (-len(block), tuple(sorted(block))))

# Glue ultrafilters (atoms) across all maximal Boolean blocks.  A selected atom
# gives value one exactly to the block events containing it.
block_atoms = []
for block in maximal:
    atoms = [x for x in block if x and not any(y and y != x and y & ~x == 0
                                               for y in block)]
    block_atoms.append(atoms)
order = sorted(range(len(maximal)), key=lambda i: len(block_atoms[i]))
chosen_atoms = {}
state_profiles = set()


def compatible_choice(block_number, atom):
    for other_number, other_atom in chosen_atoms.items():
        for event in maximal[block_number] & maximal[other_number]:
            if (atom & ~event == 0) != (other_atom & ~event == 0):
                return False
    return True


def glue(depth):
    if depth == len(order):
        state_profiles.add(tuple(next(atom & ~event == 0
                                      for i, atom in chosen_atoms.items()
                                      if event in maximal[i])
                                 for event in events))
        return
    block_number = order[depth]
    for atom in block_atoms[block_number]:
        if compatible_choice(block_number, atom):
            chosen_atoms[block_number] = atom
            glue(depth + 1)
            del chosen_atoms[block_number]


glue(0)
point_profiles = {tuple(bool(event >> point & 1) for event in events)
                  for point in range(len(points))}
assert state_profiles == point_profiles

q0 = sum(1 << i for i, (p, x, _) in enumerate(points)
         if p[0] in (0, 1) and x == 0)
r0 = sum(1 << i for i, (p, _, y) in enumerate(points)
         if p[0] in (0, 2) and y == 0)
assert q0 in carrier and r0 in carrier
relation = sorted({(int(profile[event_index[q0]]), int(profile[event_index[r0]]))
                   for profile in state_profiles})

claim = json.loads(Path(__file__).with_name(
    "five_block_nonatomic_pair_completion.json").read_text())
assert rounds == claim["closure_round_event_counts"] == [648, 1128, 1128]
assert len(events) == claim["events"] == 1128
assert hashlib.sha256("\n".join(map(hex, events)).encode()).hexdigest() == claim[
    "event_sha256"]
assert sum(x & ~y == 0 for x in events for y in events) == claim[
    "ordered_comparable_pairs"]
assert sum(commute(x, y) for x in events for y in events) == claim[
    "ordered_compatible_pairs"]
assert len(meet_by_cut) == claim["distinct_intersection_cuts"]

records = []
for number, block in enumerate(maximal):
    records.append({
        "id": number,
        "size": len(block),
        "sha256": hashlib.sha256("\n".join(map(hex, sorted(block))).encode()).hexdigest(),
        "contains_named_blocks": [name for name in NAMES if named[name] <= block],
    })
assert records == claim["maximal_compatibility_blocks"]
containers = {name: [i for i, block in enumerate(maximal) if named[name] <= block]
              for name in NAMES}
assert containers == claim["named_block_containers"]
assert len(state_profiles) == claim["state_audit"]["compatible_block_ultrafilter_states"] == 24
assert len(point_profiles) == claim["state_audit"]["distinct_point_states"] == 24
assert hex(q0) == claim["state_audit"]["q0_mask"]
assert hex(r0) == claim["state_audit"]["r0_mask"]
assert relation == [tuple(pair) for pair in claim["state_audit"]["q0_r0_relation"]]
assert relation == [(0, 0), (0, 1), (1, 0), (1, 1)]

print("PASS: independent closure reconstruction has 1128 events")
print("PASS: independent lattice, centre, and nine-maximal-block census")
print("PASS: all 24 glued states are point profiles; q0/r0 relation is full")
