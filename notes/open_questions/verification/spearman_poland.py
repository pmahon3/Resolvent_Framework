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


def jitter(Y, rng):
    J = Y.astype(float).copy()
    for j in range(Y.shape[1]):
        u = np.unique(Y[:, j]); gap = np.min(np.diff(u)) if len(u) > 1 else 1.0
        J[:, j] += rng.normal(0, 1e-3 * gap, len(Y))
    return J


def run_once(Y0, t, rng, detrend, ms=(2, 3, 4, 5)):
    n, k = Y0.shape; I = np.eye(k); b = max(1, round(n ** (1/3))); nbl = math.ceil(n / b)
    R_of = (lambda idx: spear(detr(Y0[idx], t[idx]))) if detrend else (lambda idx: spear(Y0[idx]))
    full = np.arange(n); R = R_of(full); out = {}
    idxs = [(rng.integers(0, n - b + 1, nbl)[:, None] + np.arange(b)).ravel()[:n] for _ in range(1000)]
    Zs = []
    for idx in idxs:
        Z = math.sqrt(n) * (R_of(idx) - R); np.fill_diagonal(Z, 0); Zs.append(Z)
    for m in ms:
        sol = sr.VmSolver(k, m); V = sol(R); T = math.sqrt(n) * V
        use = Zs if m == 2 else Zs[:300]
        crit = np.percentile([sol(I + Z) + 1 for Z in use], 95); out[m] = (V, T, crit, T > crit)
    return out


def main(csvp, wdir):
    rng = np.random.default_rng(15); S = m_.load(csvp)
    sites = sorted(s for s, (ser, meta) in S.items() if meta[1] == "D00013" and len(ser) >= 30)
    T_ = {s: c.junjul(Path(wdir) / f"PL{s}.json") for s in sites}
    yrs = sorted(y for y in set.intersection(*[set(S[s][0]) for s in sites]) if y >= 1942 and all(y-1 in T_[s] and y-2 in T_[s] for s in sites))
    Y0 = np.array([[S[s][0][y] for s in sites] for y in yrs]); t = np.array(yrs, float); n, k = Y0.shape
    print(f"sites {k}, n = {n}; tied fraction per site: {[round(1 - len(np.unique(Y0[:, j]))/n, 2) for j in range(k)]}")
    for label, det in (("(a) jittered Spearman, no detrend [provable under A1+Segers]", False), ("(b) jittered Spearman, log1p-detrended [sensitivity]", True)):
        rows = [run_once(jitter(Y0, rng), t, rng, det) for _ in range(20)]
        print(f"\n== {label}")
        for m in (2, 3, 4, 5):
            Ts = [r[m][1] for r in rows]; cs = [r[m][2] for r in rows]; nrej = sum(r[m][3] for r in rows)
            print(f"   m={m}: T range [{min(Ts):.2f}, {max(Ts):.2f}], crit range [{min(cs):.2f}, {max(cs):.2f}], rejected in {nrej}/20", flush=True)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
