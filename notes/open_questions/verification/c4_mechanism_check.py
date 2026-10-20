"""Definitions test 1, mechanism check (2026-10-19). C4 at A=2.
(1) Forced value of the parity witness (windows: x0!=x1, x1!=x2, x2==x3, x3!=x0, each uniform on its
    two cells) on every buildable set and on the 8 gap sets (0/1 span elements not buildable).
(2) Exact vertex enumeration of {g in span V : g >= 0, sum g = 1} (extreme rays of the non-negative cone):
    are they all multiples of 0/1 vectors?
Farkas: a probability state on D is a mixture of points iff its forced value is >= 0 on every
non-negative g in V, so a hidden twist must show either on a gap set or on a non-binary extreme ray.
"""
import itertools
import numpy as np
A = 2; V = 4; E = [(0, 1), (1, 2), (2, 3), (3, 0)]
pts = list(itertools.product(range(A), repeat=V)); n = len(pts); full = (1 << n) - 1
gens = set()
for (i, j) in E:
    for S in range(1 << (A * A)):
        m = 0
        for t, p in enumerate(pts):
            if S >> (p[i] * A + p[j]) & 1: m |= 1 << t
        gens.add(m)
D = set(gens) | {0, full}; fr = list(D)
while fr:
    new = set(); L = list(D)
    for a in fr:
        if full ^ a not in D: new.add(full ^ a)
        for b in L:
            if a & b == 0 and (a | b) not in D: new.add(a | b)
    D |= new; fr = list(new)
cells = [(k, a, b) for k in range(len(E)) for a in range(A) for b in range(A)]
B = np.array([[1.0 if (p[E[k][0]] == a and p[E[k][1]] == b) else 0.0 for (k, a, b) in cells] for p in pts])
Bp = np.linalg.pinv(B)
mu = np.zeros(len(cells))
rel = {0: 'ne', 1: 'ne', 2: 'eq', 3: 'ne'}
for c, (k, a, b) in enumerate(cells):
    if (rel[k] == 'ne' and a != b) or (rel[k] == 'eq' and a == b): mu[c] = 0.5
def vec(m): return np.array([(m >> t) & 1 for t in range(n)], float)
def forced(f): return float(mu @ (Bp @ f))
r = np.linalg.matrix_rank(B); Qr = np.linalg.svd(B, full_matrices=False)[0][:, :r]
gap = [m for m in range(1 << n) if np.linalg.norm(vec(m) - Qr @ (Qr.T @ vec(m))) < 1e-9 and m not in D]
print("min forced value over buildable sets D:", round(min(forced(vec(m)) for m in D), 4))
print("forced values on the 8 gap sets:", sorted(round(forced(vec(m)), 4) for m in gap))
# (2) vertices of {z : Qr z >= 0, 1.Qr z = 1}
M = Qr; ones = M.sum(0)
verts = []
for rows in itertools.combinations(range(n), r - 1):
    Aeq = np.vstack([M[list(rows)], ones]); b = np.zeros(r); b[-1] = 1
    if abs(np.linalg.det(Aeq)) < 1e-10: continue
    z = np.linalg.solve(Aeq, b); g = M @ z
    if g.min() > -1e-9:
        g = np.round(g, 9)
        if not any(np.allclose(g, h) for h in verts): verts.append(g)
nonbin = [g for g in verts if len(set(np.round(g[g > 1e-9], 6))) > 1]
print(f"extreme rays: {len(verts)}; not proportional to a 0/1 vector: {len(nonbin)}")
binrays = [g for g in verts if g not in nonbin]
inD = sum(1 for g in binrays if sum(1 << t for t in range(n) if g[t] > 1e-9) in D)
print(f"0/1 extreme rays in D: {inD}; in the gap: {len(binrays) - inD}")
