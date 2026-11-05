#!/usr/bin/env python3
"""Pre-registered delay-aligned gate on CHB-MIT chb01 (notes/open_questions/neuro_critical/DELAY_GATE.md).

Usage: python3 -I neuro_eps_delay_chbmit.py <dir with chb01_*.edf and seizures.txt>
seizures.txt lines: "<file.edf> <onset_s> <end_s>".
eps*_delay per triangle = V/3 (binary triangle theorem, eps_star_triangle.py), V = max violation of the
metric inequalities on the three delay-aligned disagreement rates.
"""
import sys, itertools
from pathlib import Path
import numpy as np
from scipy.ndimage import uniform_filter1d
from scipy.stats import mannwhitneyu

FS, NCH = 256, 8
WIN, STEP = 10 * FS, 5 * FS
MAXLAG = int(0.2 * FS)                     # 200 ms -> 51 samples
BASE = 600 * FS                            # minutes 0-10
PAIRS = list(itertools.combinations(range(NCH), 2))
TRIS = list(itertools.combinations(range(NCH), 3))
TRIS = [t for c in TRIS for t in (c, (c[0], c[2], c[1]))]   # 56 = 28 triples x 2 orientations
# (orientation changes nothing for V; kept so the count matches the spec's 56 and the holonomy has a sign)


def read_edf(path, nch):
    with open(path, "rb") as f:
        h = f.read(256)
        nrec, dur, ns = int(h[236:244]), float(h[244:252]), int(h[252:256])
        sh = f.read(256 * ns)
    def field(off, w):
        return [sh[off * ns + i * w: off * ns + (i + 1) * w].decode().strip() for i in range(ns)]
    # offsets in units of ns: label16, transducer80, dim8, pmin8, pmax8, dmin8, dmax8, prefilt80, nsamp8
    o = 0; labels = field(o, 16); o += 16 * ns
    o += 80 * ns + 8 * ns
    pmin = [float(v) for v in [sh[o + i * 8:o + i * 8 + 8].decode() for i in range(ns)]]; o += 8 * ns
    pmax = [float(v) for v in [sh[o + i * 8:o + i * 8 + 8].decode() for i in range(ns)]]; o += 8 * ns
    dmin = [float(v) for v in [sh[o + i * 8:o + i * 8 + 8].decode() for i in range(ns)]]; o += 8 * ns
    dmax = [float(v) for v in [sh[o + i * 8:o + i * 8 + 8].decode() for i in range(ns)]]; o += 8 * ns
    o += 80 * ns
    nsamp = [int(sh[o + i * 8:o + i * 8 + 8].decode()) for i in range(ns)]
    assert all(n == FS for n in nsamp) and dur == 1.0, (nsamp[:3], dur)
    raw = np.memmap(path, dtype="<i2", mode="r", offset=256 + 256 * ns, shape=(nrec, ns * FS))
    X = np.empty((nch, nrec * FS))
    for c in range(nch):
        g = (pmax[c] - pmin[c]) / (dmax[c] - dmin[c])
        X[c] = (raw[:, c * FS:(c + 1) * FS].reshape(-1).astype(float) - dmin[c]) * g + pmin[c]
    return labels[:nch], X


def shifted(a, b, tau):
    """aligned arrays (a[t], b[t - tau]) over the t for which both exist."""
    if tau >= 0:
        return a[tau:], b[:len(b) - tau]
    return a[:len(a) + tau], b[-tau:]


def estimate_delays(Y):
    T = np.zeros((NCH, NCH), int)
    Z = Y[:, :BASE]
    Z = (Z - Z.mean(1, keepdims=True)) / Z.std(1, keepdims=True)
    for i, j in PAIRS:
        best, bt = -1, 0
        for tau in range(-MAXLAG, MAXLAG + 1):
            a, b = shifted(Z[i], Z[j], tau)
            r = abs(np.mean(a * b))
            if r > best:
                best, bt = r, tau
        T[i, j], T[j, i] = bt, -bt
    return T


def win_means(seq, starts):
    cs = np.concatenate([[0.0], np.cumsum(seq, dtype=float)])
    return (cs[starts + WIN] - cs[starts]) / WIN


def V_of(dab, dbc, dca):
    return np.maximum.reduce([np.zeros_like(dab), dca - dab - dbc, dab - dbc - dca, dbc - dab - dca,
                              dab + dbc + dca - 2])


def run(edf, onset, end):
    labels, X = read_edf(edf, NCH)
    N = X.shape[1]
    Y = X - uniform_filter1d(X, FS, axis=1, mode="nearest")      # 1 s moving mean removed
    B = Y > 0
    T = estimate_delays(Y)
    starts = np.arange(MAXLAG, N - WIN - MAXLAG, STEP)          # all shifts stay in range
    # disagreement sequences indexed by the first variable's time t
    def dseq(i, j, tau):
        out = np.zeros(N, bool)
        if tau >= 0:
            out[tau:] = B[i, tau:] != B[j, :N - tau]
        else:
            out[:N + tau] = B[i, :N + tau] != B[j, -tau:]
        return out
    Dd, Ds = {}, {}
    for i, j in PAIRS:
        Dd[i, j] = win_means(dseq(i, j, T[i, j]), starts)
        Dd[j, i] = win_means(dseq(j, i, T[j, i]), starts)
        Ds[i, j] = Ds[j, i] = win_means(B[i] != B[j], starts)
    eps_d = np.zeros(len(starts)); eps_s = np.zeros(len(starts)); hol = []
    for i, j, k in TRIS:
        eps_d += V_of(Dd[i, j], Dd[j, k], Dd[k, i]) / 3
        eps_s += V_of(Ds[i, j], Ds[j, k], Ds[k, i]) / 3
        hol.append(T[i, j] + T[j, k] + T[k, i])
    eps_d /= len(TRIS); eps_s /= len(TRIS)
    # baselines
    m1 = np.array([win_means(Y[c], starts) for c in range(NCH)])
    m2 = np.array([win_means(Y[c] ** 2, starts) for c in range(NCH)])
    var = m2 - m1 ** 2
    lag = np.array([win_means(np.concatenate([Y[c, :-1] * Y[c, 1:], [0.0]]), starts) for c in range(NCH)])
    ac1 = ((lag - m1 ** 2) / var).mean(0)
    xc = np.mean([np.abs((win_means(Y[i] * Y[j], starts) - m1[i] * m1[j]) / np.sqrt(var[i] * var[j]))
                  for i, j in PAIRS], 0)
    ind = {"eps_delay": eps_d, "variance": var.mean(0), "AC1": ac1, "xcorr0": xc}
    s0, s1 = starts / FS, (starts + WIN) / FS
    inter = s1 <= 600
    if onset < 960:      # chb01_21 rule (implementation choices section)
        inter &= (s1 <= onset - 60) | (s0 >= end + 60)
    pre = (s0 >= onset - 300) & (s1 <= onset)
    ict = (s0 >= onset) & (s1 <= end)
    return dict(labels=labels, T=T, hol=np.array(hol), ind=ind, eps_sim_max=eps_s.max(),
                inter=inter, pre=pre, ict=ict, usable_pre=onset >= 960)


def main(d):
    d = Path(d)
    rows = [l.split() for l in open(d / "seizures.txt") if l.strip()]
    tally = {k: {"pre": 0, "ict": 0} for k in ["eps_delay", "variance", "AC1", "xcorr0"]}
    npre = nict = 0
    for f, on, en in rows:
        r = run(d / f, float(on), float(en))
        h = r["hol"]
        print(f"\n== {f} onset {on} end {en}  eps_sim max = {r['eps_sim_max']:.2e}")
        print(f"   delays (ms) row0: {np.round(r['T'][0] / FS * 1000).astype(int).tolist()}")
        print(f"   holonomy (samples): nonzero {np.mean(h != 0):.2f}, |h| median {np.median(np.abs(h)):.0f}, max {np.abs(h).max()}")
        if r["usable_pre"]:
            npre += 1
        nict += 1
        for k, v in r["ind"].items():
            a, p, c = v[r["inter"]], v[r["pre"]], v[r["ict"]]
            line = f"   {k:9s} inter {np.median(a):.4g} (n={len(a)})"
            if r["usable_pre"]:
                pp = mannwhitneyu(p, a, alternative="greater").pvalue
                tally[k]["pre"] += pp < 0.01
                line += f" | pre {np.median(p):.4g} p={pp:.2g}{' *' if pp < 0.01 else ''}"
            pc = mannwhitneyu(c, a, alternative="greater").pvalue
            tally[k]["ict"] += pc < 0.01
            line += f" | ict {np.median(c):.4g} (n={len(c)}) p={pc:.2g}{' *' if pc < 0.01 else ''}"
            print(line)
    print(f"\nTALLY (seizures with p<0.01): pre-ictal of {npre}, ictal of {nict}")
    for k, v in tally.items():
        print(f"   {k:9s} pre {v['pre']}/{npre}  ict {v['ict']}/{nict}")
    e = tally["eps_delay"]
    if e["pre"] > npre / 2 and all(e["pre"] > tally[k]["pre"] for k in tally if k != "eps_delay"):
        verdict = "INFORMATIVE"
    elif e["ict"] > nict / 2 and not e["pre"] > npre / 2:
        verdict = "ICTAL-ONLY"
    else:
        verdict = "REDUNDANT / NULL"
    print("VERDICT:", verdict)


if __name__ == "__main__":
    main(sys.argv[1])
