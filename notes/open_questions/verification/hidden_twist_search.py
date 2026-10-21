"""Hidden-twist search at sizes sz (2026-10-21). Variables: pair laws (cells >= 0, each edge sums to 1, consistent
marginals). Constraints: Lambda(f) >= 0 for all 0/1 f in the pair span (MILP separation, cutting planes) -- this
certifies a carrier state. Objective: minimise Lambda(g) for a non-binary non-negative g in the span (found by
LP sampling with an exact-in-float extremality filter). Output the pair laws and whether each is uniform on its
support (the 'relational' form)."""
import itertools, sys, numpy as np, sympy as sp
from scipy.optimize import linprog, milp, LinearConstraint, Bounds
sz = tuple(map(int, sys.argv[1].split(","))); rng = np.random.default_rng(int(sys.argv[2]) if len(sys.argv) > 2 else 0)
E = [(0, 1), (1, 2), (2, 0)]; pts = list(itertools.product(*[range(s) for s in sz])); N = len(pts)
cells = [(e, a, b) for e in range(3) for a in range(sz[E[e][0]]) for b in range(sz[E[e][1]])]
M = np.array([[1.0 if (p[E[e][0]] == a and p[E[e][1]] == b) else 0.0 for (e, a, b) in cells] for p in pts])
rM = np.linalg.matrix_rank(M); Mp = np.linalg.pinv(M)
Nl = np.array([[float(x) for x in v] for v in sp.Matrix(M.astype(int)).T.nullspace()])
g = None
for t in range(20000):
    w = rng.normal(size=N) if t % 2 else rng.exponential(size=N) * (rng.random(N) < 0.3) - 0.05
    r = linprog(w @ M, A_ub=-M, b_ub=np.zeros(N), A_eq=[np.ones(N) @ M], b_eq=[1.0], bounds=[(None, None)] * len(cells), method="highs")
    if r.status: continue
    gg = M @ r.x; gg[np.abs(gg) < 1e-9] = 0; nz = gg[gg > 0]; Z = np.where(gg == 0)[0]
    if rM - np.linalg.matrix_rank(M[Z]) == 1 and not np.allclose(nz, nz[0]): g = gg / nz.min(); break
assert g is not None; print("non-binary ray found, values", sorted(set(np.round(g, 6))))
Aeq, beq = [], []
for e in range(3): Aeq.append([1.0 if c[0] == e else 0 for c in cells]); beq.append(1.0)
for v in range(3):
    es = [(e, E[e].index(v)) for e in range(3) if v in E[e]]; (e1, s1), (e2, s2) = es
    for val in range(sz[v]):
        Aeq.append([(1.0 if (c[0] == e1 and (c[1], c[2])[s1] == val) else 0) - (1.0 if (c[0] == e2 and (c[1], c[2])[s2] == val) else 0) for c in cells]); beq.append(0)
obj = Mp @ g; cuts = []
for it in range(400):
    Aub = [-(Mp @ f) for f in cuts]
    r = linprog(obj, A_ub=Aub or None, b_ub=[0] * len(cuts) or None, A_eq=Aeq, b_eq=beq, bounds=(0, None), method="highs")
    mu = r.x; wv = Mp.T @ mu
    sep = milp(c=wv, constraints=[LinearConstraint(Nl, 0, 0)], integrality=np.ones(N), bounds=Bounds(0, 1))
    f = np.round(sep.x)
    if wv @ f >= -1e-9: break
    cuts.append(f)
print(f"cutting planes: {len(cuts)}; min Lambda(g) = {r.fun:.6f} (negative => certified hidden twist on V01)")
for e in range(3):
    i, j = E[e]; T = np.zeros((sz[i], sz[j]))
    for k, c in enumerate(cells):
        if c[0] == e: T[c[1], c[2]] = mu[k]
    nz = T[T > 1e-9]
    print(f"pair ({i},{j}): support {int((T > 1e-9).sum())} cells, uniform on support: {np.allclose(nz, nz[0], atol=1e-6)}")
    print(np.round(T, 4))
