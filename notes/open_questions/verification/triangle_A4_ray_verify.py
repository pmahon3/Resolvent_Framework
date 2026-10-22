"""Exact verification of a non-binary extreme ray at A = 4 (2026-10-20).
Find one candidate by LP (float), then verify in exact rational arithmetic (sympy):
 (1) g is a 1/2-valued integer vector, g >= 0; (2) g lies in the span of pair cells;
 (3) extremality: rank(M restricted to zero set of g) = rank(M) - 1 (so the face of the cone is a ray).
Then by Maharam 6.1 + separation there is a consistent family of pair laws that is a state on the triangle
carrier D (since D sits inside the 0/1 part of the span) but not a mixture of points: a hidden twist at A = 4.
"""
import itertools
import numpy as np
from scipy.optimize import linprog
import sympy as sp
A = 4; rng = np.random.default_rng(1)
pts = list(itertools.product(range(A), repeat=3)); E = [(0, 1), (1, 2), (2, 0)]
cells = [(e, a, b) for e in range(3) for a in range(A) for b in range(A)]
M = np.array([[1.0 if (p[E[e][0]] == a and p[E[e][1]] == b) else 0.0 for (e, a, b) in cells] for p in pts])
rM = np.linalg.matrix_rank(M); cand = None
for t in range(20000):
    w = rng.normal(size=len(pts)) if t % 2 else rng.exponential(size=len(pts)) * (rng.random(len(pts)) < 0.3) - 0.05
    res = linprog(w @ M, A_ub=-M, b_ub=np.zeros(len(pts)), A_eq=[np.ones(len(pts)) @ M], b_eq=[1.0],
                  bounds=[(None, None)] * len(cells), method="highs")
    if res.status != 0: continue
    g = M @ res.x; g[np.abs(g) < 1e-9] = 0; nz = g[g > 0]
    Z = np.where(g == 0)[0]
    if rM - np.linalg.matrix_rank(M[Z]) != 1 or np.allclose(nz, nz[0], atol=1e-7): continue
    cand = np.round(g / nz.min()).astype(int); break
assert cand is not None, "no candidate"
Ms = sp.Matrix(M.astype(int)); gs = sp.Matrix(cand)
assert set(cand) <= {0, 1, 2} and min(cand) >= 0
aug = Ms.row_join(gs); assert aug.rank() == Ms.rank(), "g not in span"
Z = [i for i in range(len(pts)) if cand[i] == 0]
r_full, r_Z = Ms.rank(), Ms.extract(Z, list(range(len(cells)))).rank()
print("exact: values", sorted(set(cand)), "| in span: yes | rank(M) =", r_full, "rank(M_Z) =", r_Z,
      "| extreme ray:", r_full - r_Z == 1)
print("support (value 2):", [pts[i] for i in range(len(pts)) if cand[i] == 2])
print("support (value 1):", [pts[i] for i in range(len(pts)) if cand[i] == 1])
# exact decomposition into pair functions (one solution)
sol = Ms.gauss_jordan_solve(gs)[0].subs({s: 0 for s in Ms.gauss_jordan_solve(gs)[0].free_symbols})
terms = [(cells[k], sol[k]) for k in range(len(cells)) if sol[k] != 0]
print("one decomposition g = sum c * [cell]:", terms)
