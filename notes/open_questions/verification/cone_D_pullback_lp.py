"""Exact sufficient test (2026-10-21): no hidden twist at sizes sz if every extreme ray of V+ lies in cone(D).
Supply of D-sets: pair events at sz, plus pullbacks (coordinatewise value merges) of the FULL exact carrier at each
one-step-smaller size. For each extreme ray g, LP: g = sum lambda_k 1_{S_k}, lambda >= 0. All rays feasible =>
cone(D) = V+ => every carrier state is a mixture of points (Maharam 6.1). Exactness: closures exact, LP float with
residual check."""
import itertools, sys
import numpy as np, cdd
from scipy.optimize import linprog
from scipy.sparse import csc_matrix
from triangle_gap_pullback import setup
def carrier(sz):
    pts, E, M = setup(sz); N = len(pts); full = (1 << N) - 1; gens = set()
    for (i, j) in E:
        for S in range(1 << (sz[i] * sz[j])):
            gens.add(sum(1 << t for t, p in enumerate(pts) if S >> (p[i] * sz[j] + p[j]) & 1))
    D = gens | {0, full}; fr = list(D)
    while fr:
        new = set(); L = list(D)
        for a in fr:
            if full ^ a not in D: new.add(full ^ a)
            for b in L:
                if a & b == 0 and (a | b) not in D: new.add(a | b)
        D |= new; fr = list(new)
    return pts, D
def rays_of(sz):
    pts, E, M = setup(sz); cols = []
    for j in range(M.shape[1]):
        if np.linalg.matrix_rank(M[:, cols + [j]]) > len(cols): cols.append(j)
    B = M[:, cols]
    P = cdd.polyhedron_from_matrix(cdd.matrix_from_array([[0] + list(map(int, r)) for r in B], rep_type=cdd.RepType.INEQUALITY))
    out = []
    for row in cdd.copy_generators(P).array:
        if row[0] == 0:
            g = B @ np.array(row[1:]); g[np.abs(g) < 1e-9] = 0; out.append(g / g[g > 0].min())
    return pts, out
sz = tuple(map(int, sys.argv[1].split(",")))
pts, rays = rays_of(sz); idx = {p: t for t, p in enumerate(pts)}
supply = set()
_, Dfull = carrier(sz) if len(pts) <= 27 else (None, None)
if Dfull is not None: supply = set(Dfull)
for i in range(3):
    if sz[i] < 2: continue
    small = list(sz); small[i] -= 1; small = tuple(small)
    ptsS, DS = carrier(small); print(f"  base {small}: |D| = {len(DS)}", flush=True)
    for v, w in itertools.combinations(range(sz[i]), 2):
        mp = lambda x, v=v, w=w: v if x == w else (x if x < w else x - 1)
        for S in DS:
            supply.add(sum(1 << idx[p] for p in pts if (S >> ptsS.index(tuple(mp(p[k]) if k == i else p[k] for k in range(3)))) & 1))
supply = [s for s in supply if s]
print(f"{sz}: extreme rays {len(rays)}, supply of D-sets {len(supply)}", flush=True)
rows, colsI = [], []
for k, s in enumerate(supply):
    for t in range(len(pts)):
        if s >> t & 1: rows.append(t); colsI.append(k)
A = csc_matrix((np.ones(len(rows)), (rows, colsI)), shape=(len(pts), len(supply)))
bad = 0
for g in rays:
    res = linprog(np.zeros(len(supply)), A_eq=A, b_eq=g, bounds=(0, None), method="highs")
    if res.status != 0 or np.abs(A @ res.x - g).max() > 1e-7: bad += 1
print(f"  rays NOT shown in cone(D): {bad}  ->", "NO hidden twist at this size" if bad == 0 else "undecided")
