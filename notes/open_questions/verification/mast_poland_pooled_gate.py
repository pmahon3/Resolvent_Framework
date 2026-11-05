#!/usr/bin/env python3
"""Pre-registered pooled Poland gate (notes/open_questions/views_across_records/MAST_POLAND_POOLED_GATE.md).
Usage: python3 -I mast_poland_pooled_gate.py <MASTREE csv> <weather dir>"""
import sys, math, itertools, importlib.util
from pathlib import Path
import numpy as np
here = Path(__file__).parent
def mod(n, f):
    sp = importlib.util.spec_from_file_location(n, here / f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
m = mod("m", "mast_ceiling_gate.py"); c = mod("c", "mast_conditional_gate.py")
NB, CH = 100_000, 5_000


def main(csvp, wdir):
    S = m.load(csvp)
    sites = sorted(s for s, (ser, meta) in S.items() if meta[1] == "D00013" and len(ser) >= 30)
    T = {s: c.junjul(Path(wdir) / f"PL{s}.json") for s in sites}
    def common(ss): return sorted(y for y in set.intersection(*[set(S[s][0]) for s in ss]) if y >= 1942 and all(y-1 in T[s] and y-2 in T[s] for s in ss))
    while len(common(sites)) < 50:
        sites.remove(min(sites, key=lambda s: len([y for y in S[s][0] if y >= 1942])))
    yrs = common(sites); n = len(yrs)
    print(f"sites {sites}  years {n} ({yrs[0]}-{yrs[-1]})")
    Y = np.array([[S[s][0][y] for s in sites] for y in yrs])
    R = np.empty_like(Y)
    for j, s in enumerate(sites):
        dT = np.array([T[s][y-1] - T[s][y-2] for y in yrs]); R[:, j], _ = c.resid(Y[:, j], [dT])
    tris = list(itertools.combinations(range(len(sites)), 3))
    meta = {s: S[s][1] for s in sites}
    dmin = [min(m.km(meta[sites[a]], meta[sites[b]]) for a, b in itertools.combinations(t, 2)) for t in tris]
    rng = np.random.default_rng(0); nb = math.ceil(n / 3)
    for stage, X in (("stage 1 raw", Y), ("stage 2 | dT", R)):
        Vobs = np.array([float(m.V16(X[:, list(t)])[0]) for t in tris])
        cnt_le0 = np.zeros(len(tris)); bar = []
        for _ in range(NB // CH):
            starts = rng.integers(0, n, (CH, nb))
            idx = ((starts[:, :, None] + np.arange(3)) % n).reshape(CH, -1)[:, :n]
            Xb = X[idx]                                     # CH x n x sites
            Vb = np.stack([m.V16(Xb[:, :, list(t)])[0] for t in tris], 1)   # CH x tris
            cnt_le0 += (Vb <= 0).sum(0); bar.append(Vb.mean(1))
        bar = np.concatenate(bar); p_bar = float(np.mean(bar <= 0)); ptri = cnt_le0 / NB
        rej = m.holm(ptri)
        print(f"\n== {stage}: V-bar = {Vobs.mean():+.3f}  bootstrap 2.5/5% of V-bar* = {np.percentile(bar,2.5):+.3f}/{np.percentile(bar,5):+.3f}  p = {p_bar:.5f}")
        print(f"   triples: {len(tris)} | point V>0 {np.mean(Vobs>0):.2f} | Holm-significant {int(rej.sum())} | min p {ptri.min():.5f}")
        order = np.argsort(-Vobs)[:5]
        for i in order:
            print(f"   {[sites[k] for k in tris[i]]} V={Vobs[i]:+.2f} p={ptri[i]:.5f} dmin={dmin[i]:.0f} km {'SIG' if rej[i] else ''}")
        d = np.array(dmin); print(f"   corr(V, min distance) = {np.corrcoef(Vobs, d)[0,1]:+.2f}")
        if stage.startswith("stage 1"): p1 = p_bar
        else: p2 = p_bar
    v = "NO-BASE" if p1 > 0.05 else ("RESIDUAL COMMON CAUSE" if p2 <= 0.05 else "CUE SUFFICES (at this power)")
    print("\nVERDICT:", v)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
