#!/usr/bin/env python3
"""V3 (REACH_TEST_SPEARMAN.md): Poland with Spearman; (a) no detrend (provable version), (b) log1p-detrended sensitivity."""
import sys, math, importlib.util
from pathlib import Path
import numpy as np
from scipy.stats import rankdata
here = Path(__file__).parent
def mod(n, f):
    sp = importlib.util.spec_from_file_location(n, here / f); mm = importlib.util.module_from_spec(sp); sp.loader.exec_module(mm); return mm
m_ = mod("m", "mast_ceiling_gate.py"); sr = mod("sr", "source_reach_poland.py"); c = mod("c", "mast_conditional_gate.py")


def spear(Y): return np.corrcoef(np.apply_along_axis(rankdata, 0, Y).T)


def detr(Y, t):
    X = np.column_stack([np.ones(len(t)), t]); L = np.log1p(Y); b, *_ = np.linalg.lstsq(X, L, rcond=None); return L - X @ b


def main(csvp, wdir):
    rng = np.random.default_rng(15); S = m_.load(csvp)
    sites = sorted(s for s, (ser, meta) in S.items() if meta[1] == "D00013" and len(ser) >= 30)
    T_ = {s: c.junjul(Path(wdir) / f"PL{s}.json") for s in sites}
    yrs = sorted(y for y in set.intersection(*[set(S[s][0]) for s in sites]) if y >= 1942 and all(y-1 in T_[s] and y-2 in T_[s] for s in sites))
    Y0 = np.array([[S[s][0][y] for s in sites] for y in yrs]); t = np.array(yrs, float); n, k = Y0.shape; I = np.eye(k)
    b = max(1, round(n ** (1/3))); nbl = math.ceil(n / b)
    for label, Y in (("(a) Spearman, no detrend [provable]", Y0), ("(b) Spearman, log1p-detrended [sensitivity]", None)):
        boots_idx = [(rng.integers(0, n - b + 1, nbl)[:, None] + np.arange(b)).ravel()[:n] for _ in range(1000)]
        def R_of(idx=None):
            if Y is not None: return spear(Y if idx is None else Y[idx])
            return spear(detr(Y0, t) if idx is None else detr(Y0[idx], t[idx]))
        R = R_of(); Zs = []
        for idx in boots_idx:
            Z = math.sqrt(n) * (R_of(idx) - R); np.fill_diagonal(Z, 0); Zs.append(Z)
        print(f"\n== {label}: n = {n}")
        mstar = None
        for m in range(2, k):
            sol = sr.VmSolver(k, m); V = sol(R); T = math.sqrt(n) * V
            crit = np.percentile([sol(I + Z) + 1 for Z in Zs], 95); rej = T > crit
            print(f"   m={m}: V_m = {V:+.3f}  T = {T:+.2f}  crit = {crit:.2f}  {'REJECT' if rej else 'not rejected'}", flush=True)
            if not rej and mstar is None: mstar = m
        print(f"   m-hat* = {mstar}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
