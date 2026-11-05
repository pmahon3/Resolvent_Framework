#!/usr/bin/env python3
"""Pre-registered min-eigenvalue gate (notes/open_questions/neuro_critical/EIG_GATE.md).
g = -lambda_min of the delay-aligned correlation matrix (channels 1-7). Reuses neuro_eps_delay_chbmit.py.
Usage: python3 -I neuro_eig_delay_chbmit.py <dir with chb01_*.edf and seizures.txt>"""
import sys, itertools, importlib.util
from pathlib import Path
import numpy as np
from scipy.ndimage import uniform_filter1d
from scipy.stats import mannwhitneyu
spec = importlib.util.spec_from_file_location("dg", Path(__file__).with_name("neuro_eps_delay_chbmit.py"))
dg = importlib.util.module_from_spec(spec); spec.loader.exec_module(dg)
dg.NCH = 7; dg.PAIRS = list(itertools.combinations(range(7), 2))
FS, WIN, STEP, MAXLAG, NCH = dg.FS, dg.WIN, dg.STEP, dg.MAXLAG, 7


def shift(b, tau):          # c[t] = b[t - tau], zero-padded
    c = np.zeros_like(b)
    if tau >= 0: c[tau:] = b[:len(b) - tau]
    else: c[:len(b) + tau] = b[-tau:]
    return c


def wcorr(a, b, starts):
    m = lambda s: dg.win_means(s, starts)
    ma, mb = m(a), m(b)
    return (m(a * b) - ma * mb) / np.sqrt((m(a * a) - ma ** 2) * (m(b * b) - mb ** 2))


def run(edf, onset, end):
    _, X = dg.read_edf(edf, NCH)
    N = X.shape[1]
    Y = X - uniform_filter1d(X, FS, axis=1, mode="nearest")
    T = dg.estimate_delays(Y)
    starts = np.arange(MAXLAG, N - WIN - MAXLAG, STEP)
    Rd = np.repeat(np.eye(NCH)[None], len(starts), 0); Rs = Rd.copy()
    for i, j in dg.PAIRS:
        r1 = wcorr(Y[i], shift(Y[j], T[i, j]), starts)
        r2 = wcorr(Y[j], shift(Y[i], T[j, i]), starts)
        Rd[:, i, j] = Rd[:, j, i] = (r1 + r2) / 2
        Rs[:, i, j] = Rs[:, j, i] = wcorr(Y[i], Y[j], starts)
    g = -np.linalg.eigvalsh(Rd)[:, 0]; gs = -np.linalg.eigvalsh(Rs)[:, 0]
    m1 = np.array([dg.win_means(Y[c], starts) for c in range(NCH)])
    var = np.array([dg.win_means(Y[c] ** 2, starts) for c in range(NCH)]) - m1 ** 2
    lag = np.array([dg.win_means(np.concatenate([Y[c, :-1] * Y[c, 1:], [0.0]]), starts) for c in range(NCH)])
    ac1 = ((lag - m1 ** 2) / var).mean(0)
    xc = np.mean([np.abs(Rs[:, i, j]) for i, j in dg.PAIRS], 0)
    s0, s1 = starts / FS, (starts + WIN) / FS
    inter = s1 <= 600
    if onset < 960: inter &= (s1 <= onset - 60) | (s0 >= end + 60)
    return dict(ind={"g_delay": g, "variance": var.mean(0), "AC1": ac1, "xcorr0": xc}, gs_max=gs.max(),
                inter=inter, pre=(s0 >= onset - 300) & (s1 <= onset), ict=(s0 >= onset) & (s1 <= end),
                usable_pre=onset >= 960, corr_g_xc=np.corrcoef(g, xc)[0, 1], frac_pos=np.mean(g > 0))


def main(d):
    d = Path(d); rows = [l.split() for l in open(d / "seizures.txt") if l.strip()]
    keys = ["g_delay", "variance", "AC1", "xcorr0"]; tally = {k: {"pre": 0, "ict": 0} for k in keys}
    npre = nict = 0
    for f, on, en in rows:
        r = run(d / f, float(on), float(en)); g = r["ind"]["g_delay"]
        print(f"\n== {f}  g_sim max = {r['gs_max']:.2e}  frac(g>0) = {r['frac_pos']:.3f}  corr(g, xcorr0) = {r['corr_g_xc']:.2f}")
        npre += r["usable_pre"]; nict += 1
        for k, v in r["ind"].items():
            a, p, c = v[r["inter"]], v[r["pre"]], v[r["ict"]]
            line = f"   {k:8s} inter {np.median(a):.4g}"
            if r["usable_pre"]:
                pp = mannwhitneyu(p, a, alternative="greater").pvalue; tally[k]["pre"] += pp < 0.01
                line += f" | pre {np.median(p):.4g} p={pp:.2g}{' *' if pp < 0.01 else ''}"
            pc = mannwhitneyu(c, a, alternative="greater").pvalue; tally[k]["ict"] += pc < 0.01
            print(line + f" | ict {np.median(c):.4g} p={pc:.2g}{' *' if pc < 0.01 else ''}")
    print(f"\nTALLY: pre-ictal of {npre}, ictal of {nict}")
    for k, v in tally.items(): print(f"   {k:8s} pre {v['pre']}/{npre}  ict {v['ict']}/{nict}")
    e = tally["g_delay"]
    if e["pre"] > npre / 2 and all(e["pre"] > tally[k]["pre"] for k in keys[1:]): v = "INFORMATIVE"
    elif e["ict"] > nict / 2 and not e["pre"] > npre / 2: v = "ICTAL-ONLY"
    else: v = "REDUNDANT / NULL"
    print("VERDICT:", v)


if __name__ == "__main__":
    main(sys.argv[1])
