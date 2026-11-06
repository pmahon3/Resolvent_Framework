#!/usr/bin/env python3
"""Poland with the validated eps=inf numerical-delta test (VG_TEST_VALIDATION.md, last section)."""
import sys, math, importlib.util
from pathlib import Path
import numpy as np
from scipy.stats import norm, rankdata
here = Path(__file__).parent
def mod(n, f):
    sp = importlib.util.spec_from_file_location(n, here / f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
m = mod("m", "mast_ceiling_gate.py"); c = mod("c", "mast_conditional_gate.py"); nd = mod("nd", "vg_numdelta.py")


ORDER = "rank_then_detrend"   # set to "detrend_then_rank" for the corrected pipeline (REACH_TEST_VALIDITY.md)


def prep(Y, cov):            # per site: residualise on [1, covariates...] and normal-score transform, in ORDER
    n, k = Y.shape
    def ns(A): return norm.ppf((np.apply_along_axis(rankdata, 0, A) - 0.5) / n)
    def resid(A):
        out = np.empty_like(A)
        for j in range(k):
            X = np.column_stack([np.ones(n)] + [cv[:, j] if cv.ndim == 2 else cv for cv in cov])
            b, *_ = np.linalg.lstsq(X, A[:, j], rcond=None); out[:, j] = A[:, j] - X @ b
        return out
    if ORDER == "detrend_then_rank": return ns(resid(np.log1p(Y)))
    return resid(ns(Y))


def test(Y, cov, rng, NB=10_000):
    n, k = Y.shape; I = np.eye(k); R = np.corrcoef(prep(Y, cov).T); T = math.sqrt(n) * (nd.rho(np.abs(R - I)) - 1)
    b = max(1, round(n ** (1/3))); nbl = math.ceil(n / b); D = np.empty(NB)
    for s in range(NB):
        st = rng.integers(0, n - b + 1, nbl); idx = (st[:, None] + np.arange(b)).ravel()[:n]
        Rs = np.corrcoef(prep(Y[idx], [cv[idx] for cv in cov]).T); Z = math.sqrt(n) * (Rs - R)
        D[s] = nd.rho(np.abs(Z - np.diag(np.diag(Z))))
    crit = np.percentile(D, 95)
    return T, crit, float(np.mean(D >= T))


def main(csvp, wdir):
    rng = np.random.default_rng(8); S = m.load(csvp)
    sites = sorted(s for s, (ser, meta) in S.items() if meta[1] == "D00013" and len(ser) >= 30)
    T_ = {s: c.junjul(Path(wdir) / f"PL{s}.json") for s in sites}
    yrs = sorted(y for y in set.intersection(*[set(S[s][0]) for s in sites]) if y >= 1942 and all(y-1 in T_[s] and y-2 in T_[s] for s in sites))
    Y = np.array([[S[s][0][y] for s in sites] for y in yrs]); t = np.array(yrs, float)
    dT = np.array([[T_[s][y-1] - T_[s][y-2] for s in sites] for y in yrs])
    print(f"sites {len(sites)}, n = {len(yrs)} ({yrs[0]}-{yrs[-1]})")
    for label, cov in (("(a) detrended", [t]), ("(b) detrended + own dT", [t, dT])):
        T, crit, p = test(Y, cov, rng)
        print(f"{label}: T = {T:.2f} (V_G = {T/math.sqrt(len(yrs)):+.3f}), 95% crit = {crit:.2f}, p = {p:.4f}, {'REJECT (common cause required)' if T > crit else 'no rejection'}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
