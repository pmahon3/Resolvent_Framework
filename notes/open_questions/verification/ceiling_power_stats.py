#!/usr/bin/env python3
"""Compare common-cause statistics by simulation (notes/open_questions/views_across_records/CEILING_POWER_STATS.md)."""
import importlib.util, itertools, math
from pathlib import Path
import numpy as np
here = Path(__file__).parent
def mod(n, f):
    sp = importlib.util.spec_from_file_location(n, here / f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
v = mod("v", "ceiling_test_validation.py"); m = v.m
NSIM, NB, Q = 300, 1000, (1/3, 1/2, 2/3)


def V16_thr(X, qs):          # X: (..., n, 3); qs: per-site quantiles
    B = np.stack([X[..., i] > np.quantile(X[..., i], qs[i], axis=-1, keepdims=True) for i in range(3)], -1)
    return m.V16(B.astype(float) + 0.0)[0] if False else _V16B(B)


def _V16B(B):                # eq.16 V on booleans (..., n, 3)
    S = np.where(B, 1.0, -1.0); Ei = np.abs(S.mean(-2))
    Eab = (S[..., 0]*S[..., 1]).mean(-1); Ebc = (S[..., 1]*S[..., 2]).mean(-1); Eac = (S[..., 0]*S[..., 2]).mean(-1)
    rhs = 6*(1+Ei[..., 0])*(1+Ei[..., 1])*(1+Ei[..., 2]); best = None
    for a, b, c in [(1, 1, 1), (-1, 1, -1), (-1, -1, 1), (1, -1, -1)]:
        lhs = (1+Ei[..., 0]+Ei[..., 1]+a*Eab)**2 + (1+Ei[..., 0]+Ei[..., 2]+c*Eac)**2 + (1+Ei[..., 1]+Ei[..., 2]+b*Ebc)**2
        best = lhs-rhs if best is None else np.maximum(best, lhs-rhs)
    return best


def H(counts):
    p = counts / counts.sum(-1, keepdims=True)
    return -(np.where(p > 0, p*np.log2(np.where(p > 0, p, 1)), 0)).sum(-1)


def SA(X, k):                # Steudel-Ay c=2 with k-quantile bins
    edges = [np.quantile(X[..., i], np.arange(1, k)/k, axis=-1) for i in range(3)]
    L = np.stack([sum((X[..., i] > np.expand_dims(edges[i][j], -1)).astype(int) for j in range(k-1)) for i in range(3)], -1)
    code = L[..., 0]*k*k + L[..., 1]*k + L[..., 2]
    joint = np.stack([(code == c).sum(-1) for c in range(k**3)], -1).astype(float)
    marg = [np.stack([(L[..., i] == c).sum(-1) for c in range(k)], -1).astype(float) for i in range(3)]
    return 0.5*sum(H(mg) for mg in marg) - H(joint)


STATS = {"S1 median V": lambda X: _V16B(X > np.median(X, axis=-2, keepdims=True)),
         "S2 max_q V": lambda X: np.max([V16_thr(X, (q,)*3) for q in Q], 0),
         "S3 max 27 V": lambda X: np.max([V16_thr(X, qs) for qs in itertools.product(Q, repeat=3)], 0),
         "S4 SA median": lambda X: SA(X, 2),
         "S5 SA tertile": lambda X: SA(X, 3)}


def rejects(X, rng):
    n = len(X); b = 3; nb = math.ceil(n/b)
    starts = rng.integers(0, n-b+1, (NB, nb)); idx = (starts[:, :, None] + np.arange(b)).reshape(NB, -1)[:, :n]
    Xb = X[idx]
    return {k: np.percentile(f(Xb), 5) > 0 for k, f in STATS.items()}


def main():
    rng = np.random.default_rng(2); sym = (2**-0.5,)*3; asym = (0.62, 0.71, 0.80)
    cells = [("size AND sym", sym, 0), ("size asym", asym, 0)] + [(f"power rho={r}", sym, r) for r in (0.2, 0.3, 0.5)]
    print(f"{'cell':16s} {'phi':>5s} " + " ".join(f"{k:>14s}" for k in STATS))
    for name, probs, rho in cells:
        for phi in (-0.5, 0.0):
            acc = {k: 0 for k in STATS}
            for _ in range(NSIM):
                r = rejects(v.world(72, phi, probs, rho, rng), rng)
                for k in acc: acc[k] += r[k]
            print(f"{name:16s} {phi:+5.1f} " + " ".join(f"{acc[k]/NSIM:14.2f}" for k in STATS), flush=True)


if __name__ == "__main__":
    main()
