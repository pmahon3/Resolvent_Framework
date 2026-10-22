"""Problem 4 (2026-10-21): probabilistic composition on the 3x4x4 triangle.
Fix P01, P12 (the certified hidden family's first two laws). R = realizable P02 (joint worlds); C' = P02 such that
(P01,P12,P02) is >= 0 on every 0/1 vector of the pair span (sufficient for a carrier state, so C' is inside C).
Compare support functions h(d) = max <d, P02> over R and over C' for random directions d.
R: LP over joint tables. C': LP over P02 with cutting planes from a MILP separation oracle (min over V01)."""
import itertools, numpy as np
from scipy.optimize import linprog, milp, LinearConstraint, Bounds
import sympy as sp
sz = (3, 4, 4); E = [(0, 1), (1, 2), (2, 0)]
pts = list(itertools.product(*[range(s) for s in sz])); N = len(pts)
cells = [(e, a, b) for e in range(3) for a in range(sz[E[e][0]]) for b in range(sz[E[e][1]])]
M = np.array([[1.0 if (p[E[e][0]] == a and p[E[e][1]] == b) else 0.0 for (e, a, b) in cells] for p in pts])
s01 = {0: {0, 1, 2}, 1: {0, 1, 3}, 2: {1, 2, 3}}; s12 = {0: {1, 2}, 1: {0, 1, 3}, 2: {0, 2}, 3: {2, 3}}
P01 = np.array([[1/9 if b in s01[a] else 0 for b in range(4)] for a in range(3)])
P12 = np.array([[1/9 if c in s12[b] else 0 for c in range(4)] for b in range(4)])
k01 = [k for k, c in enumerate(cells) if c[0] == 0]; k12 = [k for k, c in enumerate(cells) if c[0] == 1]; k20 = [k for k, c in enumerate(cells) if c[0] == 2]
mu_fixed = np.zeros(len(cells))
for k in k01: _, a, b = cells[k]; mu_fixed[k] = P01[a, b]
for k in k12: _, a, b = cells[k]; mu_fixed[k] = P12[a, b]
Mp = np.linalg.pinv(M)
Nl = np.array([[float(x) for x in v] for v in sp.Matrix(M.astype(int)).T.nullspace()])
# R: joint P >= 0 with (x0,x1) and (x1,x2) margins fixed; objective on (x2,x0) margin
A01 = np.array([[1.0 if (p[0], p[1]) == (a, b) else 0 for p in pts] for a in range(3) for b in range(4)])
A12 = np.array([[1.0 if (p[1], p[2]) == (a, b) else 0 for p in pts] for a in range(4) for b in range(4)])
A20 = np.array([[1.0 if (p[2], p[0]) == (c, a) else 0 for p in pts] for c in range(4) for a in range(3)])
def hR(d):
    r = linprog(-(d @ A20), A_eq=np.vstack([A01, A12]), b_eq=np.concatenate([P01.ravel(), P12.ravel()]), bounds=(0, None), method="highs")
    return -r.fun
# C': variables q = P02 cells (12, ordered as k20), constraints: q >= 0, x2-marginal = P12 column sums, x0-marginal = P01 row sums,
# and Lambda(f) >= 0 for f in V01, separated by MILP. Lambda(f) = (Mp f) . mu with mu = mu_fixed + q on k20.
x0m = P01.sum(1); x2m = P12.sum(0)
Aeq = []; beq = []
for c in range(4): Aeq.append([1.0 if cells[k][1] == c else 0 for k in k20]); beq.append(x2m[c])
for a in range(3): Aeq.append([1.0 if cells[k][2] == a else 0 for k in k20]); beq.append(x0m[a])
def hC(d, cuts):
    for it in range(200):
        Aub = [-(np.array([ (Mp @ f)[k] for k in k20])) for f in cuts]; bub = [ (Mp @ f) @ mu_fixed for f in cuts]
        r = linprog(-d, A_ub=Aub or None, b_ub=bub or None, A_eq=Aeq, b_eq=beq, bounds=(0, None), method="highs")
        q = r.x; mu = mu_fixed.copy(); mu[k20] = q
        w = Mp.T @ mu
        sep = milp(c=w, constraints=[LinearConstraint(Nl, 0, 0)], integrality=np.ones(N), bounds=Bounds(0, 1))
        f = np.round(sep.x)
        if w @ f >= -1e-9: return -r.fun, q
        cuts.append(f)
    return None, None
rng = np.random.default_rng(0); cuts = []; gaps = []
for t in range(25):
    d = rng.normal(size=12)
    hr = hR(d); hc, q = hC(d, cuts)
    gaps.append(hc - hr)
# the hidden family's own P02 (uniform 1/9 on allowed): in C' (certified) but not in R
s20 = {0: {0, 1}, 1: {0, 2}, 2: {0, 1, 2}, 3: {1, 2}}
q_h = np.array([1/9 if cells[k][2] in s20[cells[k][1]] else 0 for k in k20])
r = linprog(np.zeros(N), A_eq=np.vstack([A01, A12, A20]), b_eq=np.concatenate([P01.ravel(), P12.ravel(), np.array([q_h[[i for i,k in enumerate(k20) if (cells[k][1],cells[k][2])==(c,a)][0]] for c in range(4) for a in range(3)])]), bounds=(0, None), method="highs")
print("hidden P02 realizable (in R)?", r.status == 0)
print(f"support-function gaps h_C' - h_R over 25 random directions: max {max(gaps):.4f}, mean {np.mean(gaps):.4f}, min {min(gaps):.4f}")
print("cuts used:", len(cuts))
# distance (L-infinity on the 12 cells of P02) from the hidden law to R, and the gap along the separating direction
nv = N + 1
def margin20(P): return A20 @ P
q20 = np.array([q_h[[i for i,k in enumerate(k20) if (cells[k][1],cells[k][2])==(c,a)][0]] for c in range(4) for a in range(3)])
A_ub = np.vstack([np.hstack([A20, -np.ones((12, 1))]), np.hstack([-A20, -np.ones((12, 1))])]); b_ub = np.concatenate([q20, -q20])
Aeq2 = np.hstack([np.vstack([A01, A12]), np.zeros((28, 1))]); beq2 = np.concatenate([P01.ravel(), P12.ravel()])
c = np.zeros(nv); c[-1] = 1
r = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=Aeq2, b_eq=beq2, bounds=[(0, None)] * nv, method="highs")
near = A20 @ r.x[:N]
print(f"L-inf distance from hidden P02 to R: {r.x[-1]:.5f}  (cell masses are 1/9 = {1/9:.5f})")
d_cells = q20 - near; d = np.array([d_cells[[c*3+a for c in range(4) for a in range(3)].index(cells[k][1]*3+cells[k][2])] for k in k20])
hr = hR(np.array([d[[i for i,k in enumerate(k20) if (cells[k][1],cells[k][2])==(cc,aa)][0]] for cc in range(4) for aa in range(3)]))
hc, _ = hC(d, cuts)
print(f"along the separating direction: h_R = {hr:.5f}, h_C' = {hc:.5f}, gap = {hc - hr:.5f}; d.q_hidden = {d @ q_h:.5f}")
# Farkas: {P >= 0 : A01 P = P01, A12 P = P12, A20 P = q20} infeasible <=> exists y: A^T y >= 0, b.y < 0
A = np.vstack([A01, A12, A20]); b = np.concatenate([P01.ravel(), P12.ravel(), q20])
r = linprog(b, A_ub=-A.T, b_ub=np.zeros(N), bounds=[(-1, 1)] * len(b), method="highs")
y = r.x; y01, y12, y20 = y[:12], y[12:28], y[28:]
print(f"Farkas certificate value b.y = {r.fun:.5f} (< 0 confirms q_h not realizable)")
# separating direction for P02: d = -y20 ; for any realizable P02, -y20.P02 <= y01.P01 + y12.P12
dsep = -y20; bound = y01 @ P01.ravel() + y12 @ P12.ravel()
dk = np.array([dsep[cells[k][1]*3 + cells[k][2]] for k in k20])
hc, _ = hC(dk, cuts)
print(f"separating direction: h_R <= {bound:.5f}, h_R exact = {hR(dsep):.5f}, h_C' = {hc:.5f}, gap = {hc - hR(dsep):.5f}")
