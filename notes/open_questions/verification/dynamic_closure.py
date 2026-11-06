#!/usr/bin/env python3
"""Dynamic closure validation (DYNAMIC_CLOSURE.md)."""
import math
import numpy as np
from scipy.stats import rankdata
from scipy.linalg import solve_discrete_lyapunov
from arch.bootstrap import optimal_block_length
K, A, D = 10, 0.95, 0.15
NB = [((i - 1) % K, (i + 1) % K) for i in range(K)]


def rho(M): return float(np.max(np.abs(np.linalg.eigvalsh(M))))
def spear(Y): return np.corrcoef(np.apply_along_axis(rankdata, 0, Y).T)
def vg(R): return rho(np.abs(R - np.eye(len(R)))) - 1


def system(name):
    B = A * np.eye(K)
    if name == "Lc":
        for i, (l, r) in enumerate(NB): B[i, l] += D; B[i, r] += D; B[i, i] -= 2 * D
        E = np.zeros((K, K))
        for e in range(K): E[e, e] = 1; E[(e + 1) % K, e] = 1
        Q = E @ E.T
    else:
        Q = np.eye(K) + np.ones((K, K))
    return B, Q


def simulate(name, n, rng):
    B, Q = system(name); L = np.linalg.cholesky(Q + 1e-12 * np.eye(K)); x = np.zeros(K); out = []
    for t in range(n + 300):
        x = B @ x + L @ rng.standard_normal(K)
        if t >= 300: out.append(x.copy())
    return np.array(out)


def resid(P0, P1, kind):
    n = len(P0)
    if kind == "full":
        Z = np.column_stack([np.ones(n), P0]); C, *_ = np.linalg.lstsq(Z, P1, rcond=None); return P1 - Z @ C
    E = np.empty_like(P1)
    for i, (l, r) in enumerate(NB):
        Z = np.column_stack([np.ones(n), P0[:, i], P0[:, l], P0[:, r]]); c, *_ = np.linalg.lstsq(Z, P1[:, i], rcond=None); E[:, i] = P1[:, i] - Z @ c
    return E


def test(X, mode, rng, NBOOT=500):
    if mode == "L":
        n = len(X); R_of = lambda idx: spear(X[idx]); base = X
    else:
        P0, P1 = X[:-1], X[1:]; n = len(P0); kind = "full" if mode == "I_full" else "ring"
        R_of = lambda idx: spear(resid(P0[idx], P1[idx], kind)); base = P1
    R = R_of(np.arange(n)); T = math.sqrt(n) * vg(R)
    b = int(min(max(math.ceil(optimal_block_length(np.apply_along_axis(rankdata, 0, base))['circular'].max()), 2), n // 3)); nbl = math.ceil(n / b)
    Ds = []
    for _ in range(NBOOT):
        st = rng.integers(0, n - b + 1, nbl); idx = (st[:, None] + np.arange(b)).ravel()[:n]
        Z = math.sqrt(n) * (R_of(idx) - R); np.fill_diagonal(Z, 0); Ds.append(rho(np.abs(Z)))
    return T > np.percentile(Ds, 95)


def main():
    rng = np.random.default_rng(24)
    for name in ("Lc", "Rg"):
        B, Q = system(name); S = solve_discrete_lyapunov(B, Q); s = np.sqrt(np.diag(S)); dq = np.sqrt(np.diag(Q))
        print(f"world {name}: rho(B) = {max(abs(np.linalg.eigvals(B))):.3f}; population V_G levels = {vg(S/np.outer(s,s)):+.3f}, innovations = {vg(Q/np.outer(dq,dq)):+.3f}", flush=True)
        for n in (53, 200):
            res = {m: 0 for m in ("L", "I_full", "I_ring")}
            for _ in range(100):
                X = simulate(name, n, rng)
                for m in res: res[m] += test(X, m, rng)
            print(f"   n={n}: " + "  ".join(f"{m} {v/100:.2f}" for m, v in res.items()), flush=True)


if __name__ == "__main__":
    main()
