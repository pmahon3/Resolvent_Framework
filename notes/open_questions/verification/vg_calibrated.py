#!/usr/bin/env python3
"""Calibrated boundary test for V_G (VG_TEST_VALIDATION.md run 3) + validation."""
import math, importlib.util
from pathlib import Path
import numpy as np
from scipy.stats import norm, rankdata
sp = importlib.util.spec_from_file_location("v", Path(__file__).with_name("vg_test_validation.py")); v = importlib.util.module_from_spec(sp); sp.loader.exec_module(v)


def prep(Y):
    n = len(Y); Z = norm.ppf((np.apply_along_axis(rankdata, 0, Y) - 0.5) / n); return v.detrend(Z)


def perron(R): return float(np.max(np.abs(np.linalg.eigvalsh(np.abs(R - np.eye(len(R)))))))


def calibrated(Y, rng, nsim=1000, return_details=False):
    E = prep(Y); n, k = E.shape; R = np.corrcoef(E.T); rho = perron(R); Vobs = rho - 1
    if rho <= 1: return (False, Vobs, None) if return_details else False
    R0 = np.eye(k) + (R - np.eye(k)) / rho
    phis = [np.corrcoef(E[1:, j], E[:-1, j])[0, 1] for j in range(k)]; phi = float(np.clip(np.mean(phis), -0.9, 0.9))
    L = np.linalg.cholesky(R0 + 1e-10*np.eye(k)); sims = np.empty(nsim)
    for s in range(nsim):
        eps = rng.standard_normal((n + 50, k)) @ L.T; X = np.empty_like(eps); X[0] = eps[0]
        for t in range(1, n + 50): X[t] = phi*X[t-1] + math.sqrt(1 - phi**2)*eps[t]
        sims[s] = perron(np.corrcoef(prep(X[50:]).T)) - 1
    crit = np.percentile(sims, 95)
    return (Vobs > crit, Vobs, crit) if return_details else Vobs > crit


def main():
    rng = np.random.default_rng(6)
    print(f"{'world':6s} {'n':>3s} {'phi':>5s} {'C rate':>7s}")
    for name in ("W1", "W4", "W2", "W3", "P1", "P2"):
        for n in (30, 53):
            for phi in (-0.5, 0.5):
                r = np.mean([calibrated(v.world(name, n, phi, rng), rng, nsim=400) for _ in range(300)])
                print(f"{name:6s} {n:3d} {phi:+5.1f} {r:7.2f}", flush=True)


if __name__ == "__main__":
    main()
