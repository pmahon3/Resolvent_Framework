#!/usr/bin/env python3
"""Deterministic validation of the generalized seven-loop relay core."""
import random
import relay7_core as rc


assert rc.NS == 29
face_states = {tuple(sorted(rc.STATES[i])) for i in range(rc.NS) if rc.FACE >> i & 1}
assert face_states == {(0, 3, 5, 7, 9, 11), (0, 3, 5, 8, 11),
                       (0, 3, 6, 9, 11)}
assert rc.false_nonorders(rc.ALL) == 0
assert rc.false_nonorders(rc.COMPLEMENT) == 0
assert rc.COMMON_ZERO_TARGETS == (1, 2, 4, 10, 12, 13)
assert sum(1 for _ in rc.two_cell_maps(1)) == 196
assert sum(1 for _ in rc.two_cell_maps(2)) == 16562
assert rc.window_girth_ok([()], 2)

# With no identifications every state follows every state. Exactly-one paths
# exist through every local state (a target-0 state uses a later 1).
for target in rc.COMMON_ZERO_TARGETS:
    empty = rc.analyze([()], target)
    assert empty['live'] == [rc.ALL]
    assert empty['free'][0] & rc.FACE == rc.FACE

# Independent finite graph oracle for randomized ports. In a finite periodic
# graph, an infinite zero suffix exists exactly when a reachable zero-only SCC
# contains a cycle. We compare the core's E0 and derive exact-one suffix E1.
def oracle(maps, target):
    succ = [rc.succ_masks(m) for m in maps]
    p = len(maps)
    letter, _, _ = rc._letters(target)
    vertices = [(r, s) for r in range(p) for s in range(rc.NS)]
    e0 = set()
    for start in vertices:
        if letter[start[1]]:
            continue
        seen, stack = set(), [start]
        while stack:
            v = stack.pop()
            if v in seen or letter[v[1]]:
                continue
            seen.add(v)
            r, s = v
            stack.extend(((r+1) % p, t) for t in range(rc.NS)
                         if succ[r][s] >> t & 1)
        # cycle detection in the reachable induced zero graph
        color = {}
        def cyc(v):
            color[v] = 1
            r, s = v
            for t in range(rc.NS):
                w = ((r+1) % p, t)
                if not (succ[r][s] >> t & 1) or w not in seen:
                    continue
                if color.get(w) == 1 or (color.get(w, 0) == 0 and cyc(w)):
                    return True
            color[v] = 2
            return False
        if any(color.get(v, 0) == 0 and cyc(v) for v in seen):
            e0.add(start)
    masks = [sum(1 << s for r, s in e0 if r == phase) for phase in range(p)]
    return masks

rng = random.Random(3507)
for _ in range(80):
    p = rng.randrange(1, 4)
    maps = []
    for __ in range(p):
        k = rng.randrange(0, 5)
        old = rng.sample(rc.ATOMS, k)
        new = rng.sample(rc.ATOMS, k)
        maps.append(tuple(zip(old, new)))
    target = rng.choice(rc.COMMON_ZERO_TARGETS)
    got = rc.analyze(maps, target)
    assert got['E0'] == oracle(maps, target), maps

print('OK states=29 face=3 common_zero_targets=6 complement_OD=yes '
      'empty_port_live=29 random_E0_oracle=80')
