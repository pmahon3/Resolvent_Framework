"""Problem 1, wider search (2026-10-20): triangle with alphabet sizes (a0,a1,a2). Sample vertices of
{g in span of pair cells, g >= 0, sum g = 1} with random objectives (gaussian and sparse); report non-binary ones.
Non-binary extreme ray => a hidden twist exists at these sizes (Maharam 6.1 + separation).
"""
import itertools, sys
import numpy as np
from scipy.optimize import linprog
sz = tuple(map(int, sys.argv[1].split(","))); trials = int(sys.argv[2]); rng = np.random.default_rng(1)
pts = list(itertools.product(*[range(s) for s in sz])); E = [(0, 1), (1, 2), (2, 0)]
cells = [(e, a, b) for e in range(3) for a in range(sz[E[e][0]]) for b in range(sz[E[e][1]])]
M = np.array([[1.0 if (p[E[e][0]] == a and p[E[e][1]] == b) else 0.0 for (e, a, b) in cells] for p in pts])
seen = {}; 
for t in range(trials):
    w = rng.normal(size=len(pts)) if t % 2 else rng.exponential(size=len(pts)) * (rng.random(len(pts)) < 0.3) - 0.05
    res = linprog(w @ M, A_ub=-M, b_ub=np.zeros(len(pts)), A_eq=[np.ones(len(pts)) @ M], b_eq=[1.0],
                  bounds=[(None, None)] * len(cells), method="highs")
    if res.status != 0: continue
    g = M @ res.x; g[np.abs(g) < 1e-9] = 0; nz = g[g > 0]
    Z = np.where(g == 0)[0]
    # extreme ray iff {c : (M c)_Z = 0} maps to a 1-dim subspace of g-space: rank(M) - rank(M[Z]) == 1
    if np.linalg.matrix_rank(M) - (np.linalg.matrix_rank(M[Z]) if len(Z) else 0) != 1: continue
    key = tuple(np.round(g / nz.min(), 5)); seen[key] = not np.allclose(nz, nz[0], atol=1e-7)
nb = [k for k, v in seen.items() if v]
print(f"sizes {sz}: distinct EXTREME rays {len(seen)}, non-binary {len(nb)}", flush=True)
if nb:
    k = nb[0]; vals = sorted(set(x for x in k if x > 0))
    print("  value set of first non-binary ray:", vals[:8])
