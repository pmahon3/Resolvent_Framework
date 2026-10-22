"""Atom at larger sizes (2026-10-21). Sample non-binary extreme rays of V+ (LP + extremality filter), bucket them by a
symmetry invariant (value multiset; per-variable sorted slice sums, sorted across variables when sizes allow), and for one
representative per bucket compute the extremal hidden twist (min Lambda(g), MILP cuts over all 0/1 span vectors).
Report: number of ray classes found; for each, the hidden twist's support sizes, uniformity, and how many values of
each variable it actually uses (an embedded 3x4x4 pattern uses 3,4,4)."""
import itertools, sys, numpy as np, sympy as sp
from scipy.optimize import linprog, milp, LinearConstraint, Bounds
sz = tuple(map(int, sys.argv[1].split(","))); trials = int(sys.argv[2]); rng = np.random.default_rng(int(sys.argv[3]) if len(sys.argv) > 3 else 0)
E = [(0, 1), (1, 2), (2, 0)]; pts = list(itertools.product(*[range(s) for s in sz])); N = len(pts)
cells = [(e, a, b) for e in range(3) for a in range(sz[E[e][0]]) for b in range(sz[E[e][1]])]
M = np.array([[1.0 if (p[E[e][0]] == a and p[E[e][1]] == b) else 0.0 for (e, a, b) in cells] for p in pts])
rM = np.linalg.matrix_rank(M); Mp = np.linalg.pinv(M)
Nl = np.array([[float(x) for x in v] for v in sp.Matrix(M.astype(int)).T.nullspace()])
def invariant(g):
    per = []
    for v in range(3):
        sums = sorted(round(sum(g[i] for i, p in enumerate(pts) if p[v] == a), 6) for a in range(sz[v]))
        per.append((sz[v], tuple(sums)))
    return (tuple(sorted(np.round(g, 6))), tuple(sorted(per)))
classes = {}
for t in range(trials):
    w = rng.normal(size=N) if t % 2 else rng.exponential(size=N) * (rng.random(N) < 0.3) - 0.05
    r = linprog(w @ M, A_ub=-M, b_ub=np.zeros(N), A_eq=[np.ones(N) @ M], b_eq=[1.0], bounds=[(None, None)] * len(cells), method="highs")
    if r.status: continue
    g = M @ r.x; g[np.abs(g) < 1e-9] = 0; nz = g[g > 0]; Z = np.where(g == 0)[0]
    if rM - np.linalg.matrix_rank(M[Z]) != 1 or np.allclose(nz, nz[0]): continue
    g = g / nz.min(); classes.setdefault(invariant(g), g)
print(f"{sz}: non-binary ray classes found (by invariant): {len(classes)}", flush=True)
Aeq, beq = [], []
for e in range(3): Aeq.append([1.0 if c[0] == e else 0 for c in cells]); beq.append(1.0)
for v in range(3):
    es = [(e, E[e].index(v)) for e in range(3) if v in E[e]]; (e1, s1), (e2, s2) = es
    for val in range(sz[v]):
        Aeq.append([(1.0 if (c[0] == e1 and (c[1], c[2])[s1] == val) else 0) - (1.0 if (c[0] == e2 and (c[1], c[2])[s2] == val) else 0) for c in cells]); beq.append(0)
cuts = []
for key, g in classes.items():
    obj = Mp @ g
    for it in range(600):
        Aub = [-(Mp @ f) for f in cuts]
        r = linprog(obj, A_ub=Aub or None, b_ub=[0] * len(cuts) or None, A_eq=Aeq, b_eq=beq, bounds=(0, None), method="highs")
        mu = r.x; wv = Mp.T @ mu
        s = milp(c=wv, constraints=[LinearConstraint(Nl, 0, 0)], integrality=np.ones(N), bounds=Bounds(0, 1))
        f = np.round(s.x)
        if wv @ f >= -1e-9: break
        cuts.append(f)
    sup = [int(sum(1 for k, c in enumerate(cells) if c[0] == e and mu[k] > 1e-7)) for e in range(3)]
    nz = mu[mu > 1e-7]; used = []
    for v in range(3):
        e = [e for e in range(3) if E[e][0] == v][0]
        used.append(len({c[1] for k, c in enumerate(cells) if c[0] == e and mu[k] > 1e-7}))
    print(f"  ray values {sorted(set(np.round(g, 4)))}: min Lambda {r.fun:.5f} | supports {sup} | uniform {np.allclose(nz, nz[0], atol=1e-6)} | values used per variable {used}", flush=True)
