"""Conjecture 2 test (2026-10-21): on the triangle, a twist is visible iff some coordinatewise coarsening onto <= 3 values
per variable is twisted. Sample twisted families at 3x4x4 (vertices of the local polytope via random LPs, keep those with
no joint). Classify: (A) some coarsening twisted  => visible (transport) ; (B) all coarsenings untwisted and Lambda >= 0
on every 0/1 span vector => certified hidden ; (C) all coarsenings untwisted but Lambda < 0 on some 0/1 span vector =>
candidate counterexample (witness buildability to be checked)."""
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
def has_joint(mu):
    r = linprog(np.zeros(N), A_eq=M.T, b_eq=mu, bounds=(0, None), method="highs"); return r.status == 0
def partitions(n, m):
    out = []
    for f in itertools.product(range(m), repeat=n):
        if len(set(f)) == m and [f.index(b) for b in range(m)] == sorted(f.index(b) for b in range(m)): out.append(f)
    return out
coarse = [fm for fm in itertools.product(partitions(3, 3), partitions(4, 3), partitions(4, 3))]
def coarse_twisted(mu):
    for fm in coarse:
        small = (3, 3, 3)
        ptsS = list(itertools.product(range(3), repeat=3))
        MS = np.array([[1.0 if (q[E[e][0]] == a and q[E[e][1]] == b) else 0 for (e, a, b) in [(e, a, b) for e in range(3) for a in range(3) for b in range(3)]] for q in ptsS])
        nu = np.zeros(27)
        for k, (e, a, b) in enumerate(cells):
            i, j = E[e]; nu[e * 9 + fm[i][a] * 3 + fm[j][b]] += mu[k]
        r = linprog(np.zeros(27), A_eq=MS.T, b_eq=nu, bounds=(0, None), method="highs")
        if r.status != 0: return True
    return False
def v01_min(mu):
    w = Mp.T @ mu
    s = milp(c=w, constraints=[LinearConstraint(Nl, 0, 0)], integrality=np.ones(N), bounds=Bounds(0, 1))
    return w @ np.round(s.x), np.round(s.x)
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
counts = {"A visible via coarsening": 0, "B certified hidden": 0, "C candidate counterexample": 0, "world": 0}
examples = []
for t in range(int(sys.argv[2]) if len(sys.argv) > 2 else 200):
    r = linprog(rng.normal(size=len(cells)), A_eq=Aeq, b_eq=beq, bounds=(0, None), method="highs")
    mu = r.x
    if t % 3 == 1:  # mix with the known hidden family to explore near it
        s01 = {0: {0, 1, 2}, 1: {0, 1, 3}, 2: {1, 2, 3}}; s12 = {0: {1, 2}, 1: {0, 1, 3}, 2: {0, 2}, 3: {2, 3}}; s20 = {0: {0, 1}, 1: {0, 2}, 2: {0, 1, 2}, 3: {1, 2}}
        hid = np.array([1/9 if b in [s01, s12, s20][e][a] else 0 for (e, a, b) in cells]); lam = rng.uniform(0.6, 1.0)
        mu = lam * hid + (1 - lam) * mu
    if has_joint(mu): counts["world"] += 1; continue
    if coarse_twisted(mu): counts["A visible via coarsening"] += 1; continue
    val, f = v01_min(mu)
    if val >= -1e-9: counts["B certified hidden"] += 1
    else: counts["C candidate counterexample"] += 1; examples.append((mu, f, val))
print(counts)
if examples:
    np.save('conj2_candidates.npy', np.array([np.concatenate([m, f, [v]]) for m, f, v in examples]))
    print("saved", len(examples), "candidates; first V01 value", examples[0][2])
