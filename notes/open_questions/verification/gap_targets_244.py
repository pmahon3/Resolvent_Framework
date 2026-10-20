"""Direct membership test for the 4 undecided binary rays at sizes (2,4,4): grow the Dynkin closure of the
pair events (complements + disjoint unions), stopping when all targets are found or a size cap is hit."""
import itertools, numpy as np, sys
sys.argv = ["x", "2,4,4"]
from triangle_gap_pullback import setup, binary_rays, buildable
sz = (2, 4, 4); pts, E, M = setup(sz); N = len(pts); full = (1 << N) - 1
base = {}
rays = binary_rays(sz)
targets = {sum(1 << pts.index(p) for p in R) for R in rays if not buildable(sz, R, {(1,1,1): lambda S: True}) }
# recompute undecided properly: rays that are not swap-invariant in any coordinate
def swap_inv(R):
    for i in range(3):
        for v, w in itertools.combinations(range(sz[i]), 2):
            sw = lambda p: tuple((w if p[k] == v else v if p[k] == w else p[k]) if k == i else p[k] for k in range(3))
            if all((sw(p) in R) == (p in R) for p in pts): return True
    return False
targets = {sum(1 << pts.index(p) for p in R) for R in rays if not swap_inv(R)}
print("targets:", len(targets), flush=True)
gens = set()
for (i, j) in E:
    for S in range(1 << (sz[i] * sz[j])):
        gens.add(sum(1 << t for t, p in enumerate(pts) if S >> (p[i] * sz[j] + p[j]) & 1))
D = gens | {0, full}; fr = list(D); CAP = 4_000_000; rnd = 0
while fr and not targets <= D and len(D) < CAP:
    new = set(); L = list(D)
    for a in fr:
        if full ^ a not in D: new.add(full ^ a)
        for b in L:
            if a & b == 0 and (a | b) not in D: new.add(a | b)
    D |= new; fr = list(new); rnd += 1
    print(f"round {rnd}: |D| = {len(D)}, targets found {len(targets & D)}/{len(targets)}", flush=True)
print("DONE: all targets buildable" if targets <= D else ("closure complete: some target NOT buildable" if not fr else "cap hit"))
