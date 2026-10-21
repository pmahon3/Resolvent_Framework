"""Problem 4 shape (2026-10-21): size and dimension of C' \\ R at 3x4x4 for the hidden family's P01, P12.
T = all P02 with the right single-variable marginals (6-dim transportation polytope). Hit-and-run samples of T;
for each: in R? (LP) in C'? (MILP min over V01 >= 0). Then local probe around the hidden law q_h."""
import itertools, numpy as np, sys
exec(open('composition_R_vs_C.py').read().split('rng = np.random.default_rng(0)')[0])
from scipy.linalg import null_space
Aeq_ = np.array(Aeq); beq_ = np.array(beq)
Nd = null_space(Aeq_)            # directions within T's affine hull
print("dim T =", Nd.shape[1])
def inR(q):
    q20 = np.array([q[[i for i,k in enumerate(k20) if (cells[k][1],cells[k][2])==(c,a)][0]] for c in range(4) for a in range(3)])
    r = linprog(np.zeros(N), A_eq=np.vstack([A01, A12, A20]), b_eq=np.concatenate([P01.ravel(), P12.ravel(), q20]), bounds=(0, None), method="highs")
    return r.status == 0
def inC(q):
    mu = mu_fixed.copy(); mu[k20] = q; w = Mp.T @ mu
    sep = milp(c=w, constraints=[LinearConstraint(Nl, 0, 0)], integrality=np.ones(N), bounds=Bounds(0, 1))
    return w @ np.round(sep.x) >= -1e-9
rng = np.random.default_rng(3)
# start: Markov composite (in R, interior-ish)
P1 = P01.sum(0)
mk = np.array([sum(P01[a, y] * P12[y, cells[k][1]] / P1[y] for y in range(4)) if (a := cells[k][2]) is not None else 0 for k in k20])
x = mk.copy(); counts = {"R": 0, "C'\\R": 0, "neither": 0}
for t in range(0):
    d = Nd @ rng.normal(size=Nd.shape[1])
    lo, hi = -np.inf, np.inf
    for xi, di in zip(x, d):
        if di > 1e-12: lo = max(lo, -xi / di)
        elif di < -1e-12: hi = min(hi, -xi / di)
    x = x + rng.uniform(lo, hi) * d; x[np.abs(x) < 1e-13] = 0
    if inR(x): counts["R"] += 1
    elif inC(x): counts["C'\\R"] += 1
    else: counts["neither"] += 1
print("hit-and-run over T (1500 samples):", counts)
# local probe around the hidden law
s20 = {0: {0, 1}, 1: {0, 2}, 2: {0, 1, 2}, 3: {1, 2}}
q_h = np.array([1/9 if cells[k][2] in s20[cells[k][1]] else 0 for k in k20])
probe = {"C'\\R": 0, "R": 0, "outside C'": 0}
for t in range(300):
    d = Nd @ rng.normal(size=Nd.shape[1]); d /= np.abs(d).max()
    for eps in [0.004]:
        q = q_h + eps * d
        if (q < -1e-12).any(): continue
        if inR(q): probe["R"] += 1
        elif inC(q): probe["C'\\R"] += 1
        else: probe["outside C'"] += 1
print("random feasible perturbations of the hidden law (step 0.004):", probe)
