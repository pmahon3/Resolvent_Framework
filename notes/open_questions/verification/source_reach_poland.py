#!/usr/bin/env python3
"""Poland minimum source reach (SOURCE_REACH_SCOUT.md, last section)."""
import sys, math, itertools, importlib.util
from pathlib import Path
import numpy as np
import cvxpy as cp
here = Path(__file__).parent
def mod(n, f):
    sp = importlib.util.spec_from_file_location(n, here / f); mm = importlib.util.module_from_spec(sp); sp.loader.exec_module(mm); return mm
m_ = mod("m", "mast_ceiling_gate.py"); c = mod("c", "mast_conditional_gate.py"); pv = mod("pv", "vg_poland_validated.py")


class VmSolver:                      # dual SDP with R as a parameter (compiled once)
    def __init__(self, k, m):
        self.P = cp.Parameter((k, k), symmetric=True); X = cp.Variable((k, k), symmetric=True)
        cons = [cp.trace(X) == 1] + [X[np.ix_(S, S)] >> 0 for S in map(list, itertools.combinations(range(k), m))]
        self.prob = cp.Problem(cp.Maximize(-cp.trace(X @ self.P)), cons); self.X = X
    def __call__(self, R):
        self.P.value = (R + R.T) / 2; self.prob.solve(solver="CLARABEL"); return float(self.prob.value)


def main(csvp, wdir):
    rng = np.random.default_rng(11); S = m_.load(csvp)
    sites = sorted(s for s, (ser, meta) in S.items() if meta[1] == "D00013" and len(ser) >= 30)
    T_ = {s: c.junjul(Path(wdir) / f"PL{s}.json") for s in sites}
    yrs = sorted(y for y in set.intersection(*[set(S[s][0]) for s in sites]) if y >= 1942 and all(y-1 in T_[s] and y-2 in T_[s] for s in sites))
    Y = np.array([[S[s][0][y] for s in sites] for y in yrs]); t = np.array(yrs, float); n, k = Y.shape
    R = np.corrcoef(pv.prep(Y, [t]).T); I = np.eye(k)
    b = max(1, round(n ** (1/3))); nbl = math.ceil(n / b); Zs = []
    for _ in range(1000):
        st = rng.integers(0, n - b + 1, nbl); idx = (st[:, None] + np.arange(b)).ravel()[:n]
        Zs.append(math.sqrt(n) * (np.corrcoef(pv.prep(Y[idx], [t[idx]]).T) - R))
    print(f"sites {k}, n = {n}; lambda_min(R) = {np.linalg.eigvalsh(R)[0]:.3f}")
    mstar = None
    for m in range(2, k):
        sol = VmSolver(k, m); V = sol(R); T = math.sqrt(n) * V
        D = np.array([sol(I + Z - np.diag(np.diag(Z))) + 1 for Z in Zs]); crit = np.percentile(D, 95)
        rej = T > crit
        print(f"m={m}: V_m = {V:+.3f}  T = {T:+.2f}  crit95 = {crit:.2f}  {'REJECT H0(m)' if rej else 'not rejected'}", flush=True)
        if not rej and mstar is None: mstar = m
    print(f"m-hat* (lower bound on minimum source reach) = {mstar}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
