"""Conjecture 3 (2026-10-21): vertices of S' = {consistent pair laws, Lambda >= 0 on all 0/1 span vectors} at 3x4x4.
Random objectives, cutting planes with MILP separation (cuts shared). Classify vertices: point masses (a single
triple's pair laws) vs others; for others: uniform on support? support sizes per pair? realizable (joint exists)?"""
import itertools, sys, numpy as np, sympy as sp
from scipy.optimize import linprog, milp, LinearConstraint, Bounds
sz = (3, 4, 4); E = [(0, 1), (1, 2), (2, 0)]
pts = list(itertools.product(*[range(s) for s in sz])); N = len(pts)
cells = [(e, a, b) for e in range(3) for a in range(sz[E[e][0]]) for b in range(sz[E[e][1]])]
M = np.array([[1.0 if (p[E[e][0]] == a and p[E[e][1]] == b) else 0.0 for (e, a, b) in cells] for p in pts])
Mp = np.linalg.pinv(M); Nl = np.array([[float(x) for x in v] for v in sp.Matrix(M.astype(int)).T.nullspace()])
Aeq, beq = [], []
for e in range(3): Aeq.append([1.0 if c[0] == e else 0 for c in cells]); beq.append(1.0)
for v in range(3):
    es = [(e, E[e].index(v)) for e in range(3) if v in E[e]]; (e1, s1), (e2, s2) = es
    for val in range(sz[v]):
        Aeq.append([(1.0 if (c[0] == e1 and (c[1], c[2])[s1] == val) else 0) - (1.0 if (c[0] == e2 and (c[1], c[2])[s2] == val) else 0) for c in cells]); beq.append(0)
cuts = []; rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
def solve(obj):
    for it in range(500):
        Aub = [-(Mp @ f) for f in cuts]
        r = linprog(obj, A_ub=Aub or None, b_ub=[0] * len(cuts) or None, A_eq=Aeq, b_eq=beq, bounds=(0, None), method="highs")
        mu = r.x; w = Mp.T @ mu
        s = milp(c=w, constraints=[LinearConstraint(Nl, 0, 0)], integrality=np.ones(N), bounds=Bounds(0, 1))
        f = np.round(s.x)
        if w @ f >= -1e-9: return mu
        cuts.append(f)
    return None
def has_joint(mu):
    return linprog(np.zeros(N), A_eq=M.T, b_eq=mu, bounds=(0, None), method="highs").status == 0
verts = {}
T = int(sys.argv[2]) if len(sys.argv) > 2 else 200
import cdd
cols = []
for j in range(M.shape[1]):
    if np.linalg.matrix_rank(M[:, cols + [j]]) > len(cols): cols.append(j)
B = M[:, cols]
P = cdd.polyhedron_from_matrix(cdd.matrix_from_array([[0] + list(map(int, r)) for r in B], rep_type=cdd.RepType.INEQUALITY))
rays = []
for row in cdd.copy_generators(P).array:
    if row[0] == 0:
        gg = B @ np.array(row[1:]); gg[np.abs(gg) < 1e-9] = 0; nz = gg[gg > 0]
        if not np.allclose(nz, nz[0]): rays.append(gg / nz.min())
print("non-binary rays:", len(rays), flush=True)
idx = rng.choice(len(rays), size=min(T, len(rays)), replace=False)
for t in idx:
    mu = solve(Mp @ rays[t])
    if mu is None: continue
    key = tuple(np.round(mu, 6))
    if key in verts: continue
    verts[key] = mu
point, hidden, other = 0, [], []
for mu in verts.values():
    nz = mu[mu > 1e-7]
    if np.allclose(nz, 1.0): point += 1; continue
    (hidden if not has_joint(mu) else other).append(mu)
print(f"distinct vertices: {len(verts)}; point masses: {point}; non-point realizable: {len(other)}; NON-REALIZABLE (hidden): {len(hidden)}; cuts: {len(cuts)}")
from collections import Counter
shapes = Counter()
for mu in hidden:
    sup = [int(sum(1 for k, c in enumerate(cells) if c[0] == e and mu[k] > 1e-7)) for e in range(3)]
    nz = mu[mu > 1e-7]
    shapes[(tuple(sup), bool(np.allclose(nz, nz[0], atol=1e-6)), round(float(nz.max()), 4))] += 1
for k, v in shapes.most_common(): print("  hidden vertex: supports per pair", k[0], "| uniform on support:", k[1], "| max mass", k[2], "| count", v)
