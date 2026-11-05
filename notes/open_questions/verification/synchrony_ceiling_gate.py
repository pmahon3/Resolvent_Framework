#!/usr/bin/env python3
"""Pre-registered synchrony-ceiling gate (notes/open_questions/views_across_records/SYNCHRONY_CEILING_GATE.md).
Usage: python3 -I synchrony_ceiling_gate.py <ntl29_v15.csv> <ntl37_v15.csv>"""
import csv, sys, itertools, collections, importlib.util
from pathlib import Path
import numpy as np
sp = importlib.util.spec_from_file_location("h", Path(__file__).with_name("lake_harness.py"))
h = importlib.util.module_from_spec(sp); sp.loader.exec_module(h)
LAKES = h.LAKES
SUMMER = {6, 7, 8}


def temp_series(path):
    rows = collections.defaultdict(list)
    for r in csv.DictReader(open(path)):
        if r["lakeid"] not in LAKES or r["depth"] == "" or r["wtemp"] in ("", "NA"): continue
        d = float(r["depth"])
        if d > 1 or int(r["sampledate"][5:7]) not in SUMMER: continue
        rows[(r["lakeid"], r["sampledate"])].append((d, float(r["wtemp"])))
    yr = collections.defaultdict(list)
    for (lk, dt), lst in rows.items():
        at1 = [v for d, v in lst if d == 1] or [v for d, v in lst if d == min(x for x, _ in lst)]
        yr[(lk, int(dt[:4]))].append(np.mean(at1))
    return {k: np.mean(v) for k, v in yr.items()}


def zoo_series(path):
    st = collections.defaultdict(lambda: dict(D=0.0, C=0.0, R=0.0))
    for r in csv.DictReader(open(path)):
        if r["lakeid"] not in LAKES or int(r["sample_date"][5:7]) not in SUMMER: continue
        key = (r["lakeid"], r["sample_date"], r["station"]); st[key]
        g = h.group_of(int(r["species_code"]), r["species_name"])
        if g and r["density"] not in ("", "NA"): st[key][g] += float(r["density"])
    by = collections.defaultdict(list)
    for (lk, dt, s), v in st.items(): by[(lk, dt)].append(v)
    out = {g: collections.defaultdict(list) for g in "DCR"}
    for (lk, dt), vs in by.items():
        for g in "DCR":
            out[g][(lk, int(dt[:4]))].append(np.log10(np.mean([v[g] for v in vs]) + 1))
    return {g: {k: np.mean(v) for k, v in out[g].items()} for g in "DCR"}


def V_stat(B):            # B: n x 3 booleans (median-split); E_ij = +-1 correlations
    S = np.where(B, 1.0, -1.0)
    E = [np.mean(S[:, 0] * S[:, 1]), np.mean(S[:, 1] * S[:, 2]), np.mean(S[:, 0] * S[:, 2])]
    return max(sum(E[j] ** 2 for j in range(3) if j != k) - (1 - abs(E[k])) ** 2 for k in range(3)), E


def triple_test(series, tri, rng, nboot=2000, block=3):
    years = sorted(set.intersection(*[{y for (lk, y) in series if lk == l} for l in tri]))
    X = np.array([[series[(l, y)] for l in tri] for y in years])
    B = X > np.median(X, axis=0)
    V, E = V_stat(B)
    n = len(years); nb = int(np.ceil(n / block)); boots = []
    for _ in range(nboot):
        idx = np.concatenate([np.arange(s, s + block) % n for s in rng.integers(0, n, nb)])[:n]
        Xb = X[idx]; boots.append(V_stat(Xb > np.median(Xb, axis=0))[0])
    lb = np.percentile(boots, 5)
    p = np.mean(np.array(boots) <= 0)          # bootstrap one-sided p for V > 0
    return n, V, E, lb, p


def holm(ps, alpha=0.05):
    order = np.argsort(ps); rej = np.zeros(len(ps), bool)
    for r, i in enumerate(order):
        if ps[i] <= alpha / (len(ps) - r): rej[i] = True
        else: break
    return rej


def run(name, series, rng):
    res = [(tri, *triple_test(series, tri, rng)) for tri in itertools.combinations(LAKES, 3)]
    rej = holm(np.array([r[5] for r in res]))
    print(f"\n== {name}")
    for (tri, n, V, E, lb, p), rj in zip(res, rej):
        print(f"  {'-'.join(tri)} n={n:2d} E={[round(e,2) for e in E]} V={V:+.3f} lb95={lb:+.3f} p={p:.3f} {'VIOLATION' if (lb > 0 and rj) else ''}")
    nv = sum(1 for r, rj in zip(res, rej) if r[4] > 0 and rj)
    print(f"  violations: {nv}/10")
    return nv


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    nt = run("CONTROL water temperature (summer, 1 m)", temp_series(sys.argv[1]), rng)
    print("CONTROL", "PASSES" if nt >= 6 else "FAILS (test too weak; zooplankton uninterpretable)")
    z = zoo_series(sys.argv[2])
    for g, nm in zip("DCR", ["Daphnia", "copepods", "rotifers"]):
        run(f"TEST {nm} (summer mean log density)", z[g], rng)
