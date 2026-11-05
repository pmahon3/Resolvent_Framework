#!/usr/bin/env python3
"""Pre-registered beech mast synchrony-ceiling gate (notes/open_questions/views_across_records/MAST_CEILING_GATE.md).
Usage: python3 -I mast_ceiling_gate.py <MASTREEplus_2024-06-26_V2.csv>"""
import csv, sys, itertools, collections, math
import numpy as np

PREF = {"seed": 0, "fruit": 1, "flower": 2}


def load(path):
    ser = collections.defaultdict(dict); meta = {}
    for r in csv.DictReader(open(path, encoding="utf-8", errors="replace")):
        if r["Species"] != "Fagus sylvatica" or r["Value"] in ("", "NA"): continue
        key = (r["Site_number"], r["Variable_number"])
        try: ser[key][int(r["Year"])] = float(r["Value"])
        except ValueError: continue
        meta[key] = (r["Variable"], r["Study_ID"], float(r["Latitude"]), float(r["Longitude"]))
    best = {}
    for (site, vn), s in ser.items():
        rank = (PREF.get(meta[(site, vn)][0], 3), -len(s))
        if site not in best or rank < best[site][0]: best[site] = (rank, s, meta[(site, vn)])
    return {site: (s, m) for site, (_, s, m) in best.items()}


def km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[2], a[3], b[2], b[3]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 12742 * math.asin(math.sqrt(h))


def V16(X):                     # X: (..., n, 3) values; returns V per leading index
    B = X > np.median(X, axis=-2, keepdims=True)
    S = np.where(B, 1.0, -1.0)
    Ei = np.abs(S.mean(-2))                                     # (..., 3)
    Eab = (S[..., 0] * S[..., 1]).mean(-1); Ebc = (S[..., 1] * S[..., 2]).mean(-1); Eac = (S[..., 0] * S[..., 2]).mean(-1)
    rhs = 6 * (1 + Ei[..., 0]) * (1 + Ei[..., 1]) * (1 + Ei[..., 2])
    best = None
    for sab, sbc, sac in [(1, 1, 1), (-1, 1, -1), (-1, -1, 1), (1, -1, -1)]:   # relabelings (product of pair signs = +1)
        lhs = ((1 + Ei[..., 0] + Ei[..., 1] + sab * Eab) ** 2 + (1 + Ei[..., 0] + Ei[..., 2] + sac * Eac) ** 2
               + (1 + Ei[..., 1] + Ei[..., 2] + sbc * Ebc) ** 2)
        v = lhs - rhs; best = v if best is None else np.maximum(best, v)
    return best, (Eab, Ebc, Eac)


def holm(ps, alpha=0.05):
    order = np.argsort(ps); rej = np.zeros(len(ps), bool)
    for r, i in enumerate(order):
        if ps[i] <= alpha / (len(ps) - r): rej[i] = True
        else: break
    return rej


def main(path):
    rng = np.random.default_rng(0)
    S = load(path); sites = [s for s, (ser, m) in S.items() if len(ser) >= 30]
    print(f"beech sites with >= 30 years: {len(sites)} (of {len(S)})")
    rows = []
    for a, b, c in itertools.combinations(sites, 3):
        yrs = sorted(set(S[a][0]) & set(S[b][0]) & set(S[c][0]))
        if len(yrs) < 30: continue
        X = np.array([[S[s][0][y] for s in (a, b, c)] for y in yrs])
        ms = [S[s][1] for s in (a, b, c)]
        d = [km(ms[0], ms[1]), km(ms[1], ms[2]), km(ms[0], ms[2])]
        studies = {m[1] for m in ms}
        V, E = V16(X)
        n = len(yrs); nb = math.ceil(n / 3)
        starts = rng.integers(0, n, (1000, nb))
        idx = ((starts[:, :, None] + np.arange(3)) % n).reshape(1000, -1)[:, :n]
        Vb, _ = V16(X[idx])
        rows.append(dict(tri=(a, b, c), n=n, V=float(V), E=[float(e) for e in E], p=float(np.mean(Vb <= 0)),
                         dmin=min(d), dmax=max(d), primary=len(studies) == 3, samestudy=len(studies) < 3))
    print(f"triples with >= 30 common years: {len(rows)}")
    classes = {"primary": [r for r in rows if r["primary"]],
               "far (>100 km all pairs)": [r for r in rows if r["primary"] and r["dmin"] > 100],
               "near (<20 km all pairs)": [r for r in rows if r["primary"] and r["dmax"] < 20],
               "same-study (confound check)": [r for r in rows if r["samestudy"]]}
    for nm, rs in classes.items():
        if not rs: print(f"\n{nm}: none"); continue
        rej = holm(np.array([r["p"] for r in rs]))
        Vs = np.array([r["V"] for r in rs]); Em = np.array([np.mean(r["E"]) for r in rs])
        print(f"\n{nm}: {len(rs)} triples | V>0 (point) {np.mean(Vs>0):.2f} | Holm-significant {rej.sum()} ({rej.mean():.2f}) | median mean-E {np.median(Em):.2f} | median n {np.median([r['n'] for r in rs]):.0f}")
        top = sorted(zip(rs, rej), key=lambda t: -t[0]["V"])[:3]
        for r, rj in top:
            print(f"   {r['tri']} n={r['n']} E={[round(e,2) for e in r['E']]} V={r['V']:+.2f} p={r['p']:.3f} d={r['dmin']:.0f}-{r['dmax']:.0f} km {'SIG' if rj else ''}")


if __name__ == "__main__":
    main(sys.argv[1])
