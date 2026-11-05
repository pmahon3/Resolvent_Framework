#!/usr/bin/env python3
"""Pre-registered S2 + detrend gate (notes/open_questions/views_across_records/MAST_S2_GATE.md).
Usage: python3 -I mast_s2_gate.py <MASTREE csv>"""
import sys, math, itertools, importlib.util
from pathlib import Path
import numpy as np
here = Path(__file__).parent
def mod(n, f):
    sp = importlib.util.spec_from_file_location(n, here / f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
m = mod("m", "mast_ceiling_gate.py"); ps = mod("ps", "ceiling_power_stats.py")
S2 = ps.STATS["S2 max_q V"]; NB = 20_000


def detrend(X, yrs):
    t = np.asarray(yrs, float); A = np.column_stack([np.ones_like(t), t])
    beta, *_ = np.linalg.lstsq(A, X, rcond=None); return X - A @ beta


def test(S, tri, minyrs, rng):
    yrs = sorted(set.intersection(*[set(S[s][0]) for s in tri]))
    if len(yrs) < minyrs: return None
    X = detrend(np.array([[S[s][0][y] for s in tri] for y in yrs]), yrs)
    obs = float(S2(X)); n = len(X); b = 3; nb = math.ceil(n/b); le0 = 0
    for _ in range(NB // 5000):
        starts = rng.integers(0, n-b+1, (5000, nb)); idx = (starts[:, :, None] + np.arange(b)).reshape(5000, -1)[:, :n]
        le0 += int((S2(X[idx]) <= 0).sum())
    return dict(tri=tri, n=n, S2=obs, p=max(le0, 1) / NB if le0 == 0 else le0 / NB)


def report(name, rows):
    rej = m.holm(np.array([r["p"] for r in rows])) if rows else []
    print(f"\n== {name}: {len(rows)} triples | point S2>0 {np.mean([r['S2']>0 for r in rows]):.2f} | Holm-significant {int(np.sum(rej))}")
    for r, rj in sorted(zip(rows, rej), key=lambda t: t[0]["p"])[:8]:
        print(f"   {r['tri']} n={r['n']} S2={r['S2']:+.2f} p={r['p']:.5f} {'SIG' if rj else ''}")
    big = [r for r, rj in zip(rows, rej) if r["n"] >= 60]
    if big: print(f"   triples with n>=60: {len(big)}, significant {sum(1 for r, rj in zip(rows, rej) if r['n'] >= 60 and rj)}")


def main(path):
    rng = np.random.default_rng(3); S = m.load(path)
    long = {s: v for s, v in S.items() if len(v[0]) >= 30}
    pl = sorted(s for s in long if long[s][1][1] == "D00013")
    F1 = [r for r in (test(S, t, 50, rng) for t in itertools.combinations(pl, 3)) if r]
    report("F1 Poland within-study", F1)
    F2 = []
    for t in itertools.combinations(sorted(long), 3):
        ms = [long[s][1] for s in t]
        if len({x[1] for x in ms}) < 3: continue
        if min(m.km(ms[i], ms[j]) for i, j in itertools.combinations(range(3), 2)) <= 100: continue
        r = test(S, t, 30, rng)
        if r: F2.append(r)
    report("F2 cross-study far", F2)


if __name__ == "__main__":
    main(sys.argv[1])
