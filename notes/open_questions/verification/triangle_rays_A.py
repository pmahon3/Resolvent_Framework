"""Problem 1 (2026-10-20): does the finite triangle see every twist at alphabet A?
Hidden twist at A exists iff (i) gap V01\\D nonempty or (ii) the cone V+ = {g in span of pair cells, g >= 0}
has an extreme ray that is not a multiple of a 0/1 vector (Maharam 6.1 + separation).
Here: sample vertices of {g in V+, sum g = 1} by random-objective LPs; report any non-binary vertex.
"""
import itertools, sys
import numpy as np
from scipy.optimize import linprog
A = int(sys.argv[1]); trials = int(sys.argv[2]); rng = np.random.default_rng(int(sys.argv[3]) if len(sys.argv) > 3 else 0)
pts = list(itertools.product(range(A), repeat=3)); E = [(0, 1), (1, 2), (2, 0)]
cells = [(e, a, b) for e in range(3) for a in range(A) for b in range(A)]
M = np.array([[1.0 if (p[E[e][0]] == a and p[E[e][1]] == b) else 0.0 for (e, a, b) in cells] for p in pts])
nb = 0; seen = set(); example = None
for t in range(trials):
    w = rng.normal(size=len(pts))
    res = linprog(w @ M, A_ub=-M, b_ub=np.zeros(len(pts)), A_eq=[np.ones(len(pts)) @ M], b_eq=[1.0],
                  bounds=[(None, None)] * len(cells), method="highs")
    if res.status != 0: continue
    g = M @ res.x; g[np.abs(g) < 1e-9] = 0
    nz = g[g > 0]; key = tuple(np.round(g / nz.min(), 6))
    if key in seen: continue
    seen.add(key)
    if not np.allclose(nz, nz[0], atol=1e-7):
        nb += 1
        if example is None: example = np.round(g / nz.min(), 4)
print(f"A={A}: distinct vertices sampled {len(seen)}, non-binary {nb}")
if example is not None:
    print("example non-binary ray (values on points with g>0):",
          {pts[i]: example[i] for i in range(len(pts)) if example[i] > 0})
