#!/usr/bin/env python3
"""Beech positive control (BEECH_POSITIVE_CONTROL.md): attribution A0-A3 + placebo, and negative control (circular shifts)."""
import sys, json, math, collections, importlib.util
from pathlib import Path
import numpy as np
here = Path(__file__).parent
def mod(n, f):
    sp = importlib.util.spec_from_file_location(n, here / f); mm = importlib.util.module_from_spec(sp); sp.loader.exec_module(mm); return mm
m_ = mod("m", "mast_ceiling_gate.py"); pv = mod("pv", "vg_poland_validated.py"); pv.ORDER = "detrend_then_rank"; nd = pv.nd


def window_means(wfile, start, end):     # (month, day) inclusive
    d = json.load(open(wfile))["daily"]; acc = collections.defaultdict(list)
    for tt, v in zip(d["time"], d["temperature_2m_mean"]):
        md = (int(tt[5:7]), int(tt[8:10]))
        if v is not None and start <= md <= end: acc[int(tt[:4])].append(v)
    return {y: float(np.mean(v)) for y, v in acc.items()}


def vg_point(Y, cov):
    R = np.corrcoef(pv.prep(Y, cov).T); return nd.rho(np.abs(R - np.eye(len(R)))) - 1


def main(csvp, wdir):
    rng = np.random.default_rng(13); S = m_.load(csvp)
    sites = sorted(s for s, (ser, meta) in S.items() if meta[1] == "D00013" and len(ser) >= 30)
    JJ = {s: window_means(Path(wdir) / f"PL{s}.json", (6, 1), (7, 31)) for s in sites}
    SOL = {s: window_means(Path(wdir) / f"PL{s}.json", (6, 21), (7, 31)) for s in sites}
    yrs = sorted(y for y in set.intersection(*[set(S[s][0]) for s in sites]) if y >= 1942 and all(y-1 in JJ[s] and y-2 in JJ[s] for s in sites))
    Y = np.array([[S[s][0][y] for s in sites] for y in yrs]); t = np.array(yrs, float); n = len(yrs)
    col = lambda W, lag: np.array([[W[s][y - lag] for s in sites] for y in yrs])
    sets = {"A0 year only": [t], "A1 dT Jun-Jul": [t, col(JJ, 1) - col(JJ, 2)],
            "A2 dT solstice": [t, col(SOL, 1) - col(SOL, 2)], "A3 T1,T2 solstice": [t, col(SOL, 1), col(SOL, 2)]}
    print(f"sites {len(sites)}, n = {n} ({yrs[0]}-{yrs[-1]})")
    res = {}
    for name, cov in sets.items():
        T, crit, p = pv.test(Y, cov, rng)
        res[name] = T / math.sqrt(n); print(f"{name:18s} V_G = {T/math.sqrt(n):+.3f}  T = {T:.2f}  crit = {crit:.2f}  {'REJECT' if T > crit else 'no rejection'}", flush=True)
    dsol = col(SOL, 1) - col(SOL, 2); plac = []
    for _ in range(200):
        perm = rng.permutation(n); plac.append(vg_point(Y, [t, dsol[perm]]))
    plac = np.array(plac)
    print(f"placebo (A2 permuted, 200): V_G median {np.median(plac):+.3f}, 5% {np.percentile(plac,5):+.3f}; frac <= A2 ({res['A2 dT solstice']:+.3f}): {np.mean(plac <= res['A2 dT solstice']):.3f}; frac <= A1: {np.mean(plac <= res['A1 dT Jun-Jul']):.3f}")
    # negative control
    rej = 0
    for d in range(50):
        while True:
            off = rng.choice(n, len(sites), replace=False)
            if all(abs(a - b) >= 5 and n - abs(a - b) >= 5 for i, a in enumerate(off) for b in off[i+1:]): break
        Ysh = np.column_stack([np.roll(Y[:, j], off[j]) for j in range(len(sites))])
        T, crit, p = pv.test(Ysh, [t], rng, NB=1000); rej += T > crit
    print(f"negative control (50 circular-shift draws): rejection rate {rej/50:.2f}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
