#!/usr/bin/env python3
"""SALMON_OCEAN_DRIVER.md. Usage: python3 salmon_ocean_driver.py <sr.csv> <coords.csv> <pdo.dat>"""
import sys, math, importlib.util
from pathlib import Path
import numpy as np
from scipy.stats import f as fdist
here = Path(__file__).parent
def mod(n, f):
    sp = importlib.util.spec_from_file_location(n, here / f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
sf = mod("sf", "salmon_flow.py"); m_ = mod("m", "mast_ceiling_gate.py")


def pdo_summer(path):
    out = {}
    for line in open(path):
        p = line.split()
        if len(p) == 13 and p[0].isdigit():
            v = [float(x) for x in p[5:10]]
            if all(abs(x) < 90 for x in v): out[int(p[0])] = float(np.mean(v))
    return out


def vg(R): return sf.rho(np.abs(R - np.eye(len(R)))) - 1


def main(srp, cop, pdop):
    rng = np.random.default_rng(27); d, loc = sf.load(srp, cop); P = pdo_summer(pdop)
    res = {s: sf.ricker_resid(d[s]) for s in sf.F1}
    yrs = [y for y in sorted(set.intersection(*[set(res[s]) for s in sf.F1])) if (y + 2) in P]
    Y = np.array([[res[s][y] for s in sf.F1] for y in yrs]); n, k = Y.shape; pdo = np.array([P[y + 2] for y in yrs])
    print(f"Bristol Bay: {k} rivers, n = {n} ({yrs[0]}-{yrs[-1]}); corr(PDO_t, mean productivity) = {np.corrcoef(pdo, Y.mean(1))[0,1]:+.2f}")
    def resid_cols(cols):
        def f_(idx):
            X = np.column_stack([np.ones(len(idx))] + [c[idx] for c in cols]); b, *_ = np.linalg.lstsq(X, Y[idx], rcond=None); return sf.spear(Y[idx] - X @ b)
        return f_
    for lab, cols in (("no covariate", []), ("PDO_t (BY+2)", [pdo])):
        T, crit = sf.run_test(resid_cols(cols), n, vg, rng, 1000, Y)
        print(f"(a) V_G | {lab:14s}: V_G = {T/math.sqrt(n):+.3f}  T = {T:+.2f} vs {crit:.2f}  {'REJECT' if T > crit else 'not rejected'}", flush=True)
    v0 = vg(resid_cols([])(np.arange(n))); v1 = vg(resid_cols([pdo])(np.arange(n)))
    plac = np.array([vg(resid_cols([pdo[rng.permutation(n)]])(np.arange(n))) for _ in range(200)])
    print(f"    drop real {v0 - v1:+.3f}; placebo drops median {np.median(v0 - plac):+.3f}, 95th {np.percentile(v0 - plac, 95):+.3f}; frac placebo >= real drop {np.mean(v0 - plac >= v0 - v1):.3f}")
    Dm = np.array([[sf.km(loc[a], loc[b]) for b in sf.F1] for a in sf.F1]); nbr = [list(np.argsort(Dm[i])[1:3]) for i in range(k)]
    for lab, extra in (("lag 1", [1]), ("lags 1,4,5 (cohort echo)", [1, 4, 5])):
        L = max(extra); ps = []
        for i in range(k):
            yv = Y[L:, i]; base = [np.ones(n - L), pdo[L:]] + [Y[L - l:n - l, i] for l in extra]
            nb = [Y[L - 1:n - 1, j] for j in nbr[i]]
            X0 = np.column_stack(base); X1 = np.column_stack(base + nb)
            r0 = yv - X0 @ np.linalg.lstsq(X0, yv, rcond=None)[0]; r1 = yv - X1 @ np.linalg.lstsq(X1, yv, rcond=None)[0]
            q, dfr = X1.shape[1] - X0.shape[1], len(yv) - X1.shape[1]
            F = ((r0 @ r0 - r1 @ r1) / q) / (r1 @ r1 / dfr); ps.append(1 - fdist.cdf(F, q, dfr))
        rej = m_.holm(np.array(ps))
        print(f"(b) neighbour-lag terms ({lab}): Holm-significant {int(rej.sum())}/{k}; p = {[round(p,3) for p in ps]}")


if __name__ == "__main__":
    main(*sys.argv[1:4])
