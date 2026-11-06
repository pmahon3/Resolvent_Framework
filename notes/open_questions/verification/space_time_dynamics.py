#!/usr/bin/env python3
"""Centre in space vs time (SPACE_TIME_DYNAMICS.md)."""
import math
import numpy as np
from scipy.stats import rankdata
from scipy.linalg import solve_discrete_lyapunov
import sys
K = 10
A, D = (0.95, 0.15) if (len(sys.argv) > 1 and sys.argv[1] == "run2") else (0.5, 0.25)


def rho(M): return float(np.max(np.abs(np.linalg.eigvalsh(M))))
def vg(R): return rho(np.abs(R - np.eye(len(R)))) - 1
def spear(Y): return np.corrcoef(np.apply_along_axis(rankdata, 0, Y).T)


def system(name):
    """Return VAR matrix B and shock covariance Q for x_{t+1} = B x_t + eps."""
    B = A * np.eye(K)
    if name == "D":
        for i in range(K):
            for j in ((i - 1) % K, (i + 1) % K): B[i, j] += D; B[i, i] -= D
    if name == "M": Q = np.eye(K) + np.ones((K, K))
    elif name == "P":
        E = np.zeros((K, K))
        for e in range(K): E[e, e] = 1; E[(e + 1) % K, e] = 1   # site i gets edges i-1 (index i-1) and i (index i)
        Q = E @ E.T
    else: Q = np.eye(K)
    return B, Q


def simulate(name, n, rng):
    B, Q = system(name); L = np.linalg.cholesky(Q + 1e-12*np.eye(K)); x = np.zeros(K); out = []
    for t in range(n + 200):
        x = B @ x + L @ rng.standard_normal(K)
        if t >= 200: out.append(x.copy())
    return np.array(out)


def var_resid(X):            # VAR(1) with intercept by OLS; rows of X are consecutive years
    Z = np.column_stack([np.ones(len(X) - 1), X[:-1]]); C, *_ = np.linalg.lstsq(Z, X[1:], rcond=None); return X[1:] - Z @ C


AUTO = len(sys.argv) > 2 and sys.argv[2] == "auto"


def auto_b(X):
    from arch.bootstrap import optimal_block_length
    R = np.apply_along_axis(rankdata, 0, X); b = int(np.ceil(optimal_block_length(R)['b_cb'].max()))
    return int(min(max(b, 2), len(X) // 3))


def test(X, innov, rng, NB=500):
    if innov:                                  # resample blocks of (x_{t-1}, x_t) pairs; refit VAR on pairs
        P0, P1 = X[:-1], X[1:]; n = len(P0)
        def R_of(idx):
            Z = np.column_stack([np.ones(len(idx)), P0[idx]]); C, *_ = np.linalg.lstsq(Z, P1[idx], rcond=None)
            return spear(P1[idx] - Z @ C)
    else:
        n = len(X); R_of = lambda idx: spear(X[idx])
    full = np.arange(n); R = R_of(full); T = math.sqrt(n) * vg(R)
    b = auto_b(X) if AUTO else max(1, round(n ** (1/3))); nbl = math.ceil(n / b); D_ = np.empty(NB)
    for s in range(NB):
        st = rng.integers(0, n - b + 1, nbl); idx = (st[:, None] + np.arange(b)).ravel()[:n]
        Z = math.sqrt(n) * (R_of(idx) - R); np.fill_diagonal(Z, 0); D_[s] = rho(np.abs(Z))
    return T > np.percentile(D_, 95)


def main():
    rng = np.random.default_rng(16)
    if AUTO:
        import importlib.util as iu
        from pathlib import Path
        sp = iu.spec_from_file_location("nd", Path(__file__).with_name("vg_numdelta.py")); nd = iu.module_from_spec(sp); sp.loader.exec_module(nd)
        for w in ("W1", "W3"):
            for phi in (-0.5, 0.5):
                r = np.mean([test(nd.world(w, 53, phi, rng), False, rng) for _ in range(100)])
                print(f"static {w} n=53 phi={phi:+.1f}: L size {r:.2f}", flush=True)
    for name in ("M", "D", "P"):
        B, Q = system(name); S = solve_discrete_lyapunov(B, Q); d = np.sqrt(np.diag(S))
        Rlev = S / np.outer(d, d); dq = np.sqrt(np.diag(Q)); Rinn = Q / np.outer(dq, dq)
        print(f"world {name}: population V_G levels = {vg(Rlev):+.3f}, innovations = {vg(Rinn):+.3f}; neighbour corr levels {Rlev[0,1]:.2f}", flush=True)
        for n in (53, 200):
            rl = ri = 0
            for _ in range(100):
                X = simulate(name, n, rng); rl += test(X, False, rng); ri += test(X, True, rng)
            print(f"   n={n}: L rejection {rl/100:.2f}   I rejection {ri/100:.2f}", flush=True)


if __name__ == "__main__":
    main()
