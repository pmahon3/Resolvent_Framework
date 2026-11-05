#!/usr/bin/env python3
"""Pre-registered mast conditional gate (notes/open_questions/views_across_records/MAST_CONDITIONAL_GATE.md).
Usage: python3 -I mast_conditional_gate.py <MASTREE csv> <weather dir with PL008.json ... DE006.json>"""
import sys, json, math, importlib.util, collections
from pathlib import Path
import numpy as np
sp = importlib.util.spec_from_file_location("m", Path(__file__).with_name("mast_ceiling_gate.py"))
m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
TRIPLES = {"Poland D00013": [("008", "PL008"), ("009", "PL009"), ("010", "PL010")],
           "Germany D06207": [("001", "DE001"), ("003", "DE003"), ("006", "DE006")]}
NB = 100_000


def junjul(wfile):
    d = json.load(open(wfile))["daily"]; acc = collections.defaultdict(list)
    for t, v in zip(d["time"], d["temperature_2m_mean"]):
        if v is not None and t[5:7] in ("06", "07"): acc[int(t[:4])].append(v)
    return {y: float(np.mean(v)) for y, v in acc.items()}


def resid(y, Xcols):
    X = np.column_stack([np.ones(len(y))] + Xcols)
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    r = y - X @ beta
    return r, 1 - r.var() / y.var()


def boot_lb(X, rng, q=2.5):
    n = len(X); nb = math.ceil(n / 3); out = []
    for chunk in range(0, NB, 10_000):
        starts = rng.integers(0, n, (10_000, nb))
        idx = ((starts[:, :, None] + np.arange(3)) % n).reshape(10_000, -1)[:, :n]
        out.append(m.V16(X[idx])[0])
    Vb = np.concatenate(out)
    return float(np.percentile(Vb, q)), float(np.mean(Vb <= 0))


def main(csvp, wdir):
    rng = np.random.default_rng(0); S = m.load(csvp)
    for name, tri in TRIPLES.items():
        T = {w: junjul(Path(wdir) / f"{w}.json") for _, w in tri}
        yrs = sorted(set.intersection(*[set(S[s][0]) for s, _ in tri]))
        yrs = [y for y in yrs if all((y - 1) in T[w] and (y - 2) in T[w] for _, w in tri)]
        Y = np.array([[S[s][0][y] for s, _ in tri] for y in yrs])
        dT = np.array([[T[w][y - 1] - T[w][y - 2] for _, w in tri] for y in yrs])
        T1 = np.array([[T[w][y - 1] for _, w in tri] for y in yrs]); T2 = np.array([[T[w][y - 2] for _, w in tri] for y in yrs])
        print(f"\n== {name}: n = {len(yrs)} years ({yrs[0]}-{yrs[-1]})")
        V1, E1 = m.V16(Y); lb1, p1 = boot_lb(Y, rng)
        print(f"  stage 1 unconditional: E={[round(e,2) for e in E1]} V={float(V1):+.3f} lb97.5={lb1:+.3f} p={p1:.4f}")
        R = np.empty_like(Y); r2 = []
        for j in range(3):
            R[:, j], rr = resid(Y[:, j], [dT[:, j]]); r2.append(rr)
        V2, E2 = m.V16(R); lb2, p2 = boot_lb(R, rng)
        print(f"  stage 2 | dT: R2 per site={[round(x,2) for x in r2]}  E={[round(e,2) for e in E2]} V={float(V2):+.3f} lb97.5={lb2:+.3f} p={p2:.4f}")
        R3 = np.empty_like(Y); r23 = []
        for j in range(3):
            R3[:, j], rr = resid(Y[:, j], [T1[:, j], T2[:, j]]); r23.append(rr)
        V3, E3 = m.V16(R3); lb3, p3 = boot_lb(R3, rng)
        print(f"  secondary | T(t-1),T(t-2): R2={[round(x,2) for x in r23]}  E={[round(e,2) for e in E3]} V={float(V3):+.3f} lb97.5={lb3:+.3f} p={p3:.4f}")
        v = "NO-BASE" if lb1 <= 0 else ("PERSISTS" if lb2 > 0 else "VANISHES")
        print(f"  VERDICT: {v}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
