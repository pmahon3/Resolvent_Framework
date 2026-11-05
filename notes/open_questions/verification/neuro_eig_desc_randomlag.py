"""Discriminating checks for EIG_GATE: (a) random-lag null (estimated lags shuffled among pairs, sign random,
antisymmetric); (b) zero-lag long-window lambda_min per period (collinearity driver?).
Args: path to neuro_eig_delay_chbmit.py, data dir."""
import sys, importlib.util, numpy as np
from pathlib import Path
from scipy.ndimage import uniform_filter1d
spec = importlib.util.spec_from_file_location("eg", sys.argv[1]); eg = importlib.util.module_from_spec(spec); spec.loader.exec_module(eg)
dg = eg.dg; d = Path(sys.argv[2]); rng = np.random.default_rng(0)
def lmin(Z, T):
    R = np.eye(7)
    for i, j in dg.PAIRS:
        a, b = dg.shifted(Z[i], Z[j], T[i, j]); R[i, j] = R[j, i] = np.corrcoef(a, b)[0, 1]
    return np.linalg.eigvalsh(R)[0]
Z0 = np.zeros((7, 7), int)
for f, on, en in [l.split() for l in open(d/"seizures.txt") if l.strip()]:
    on, en = float(on), float(en)
    _, X = dg.read_edf(d/f, 7)
    Y = X - uniform_filter1d(X, 256, axis=1, mode="nearest"); T = dg.estimate_delays(Y)
    seg = lambda lo, hi: Y[:, int(lo*256):int(hi*256)]
    base = seg(0, 600) if on >= 960 else seg(0, on - 60)
    ic = seg(on, en)
    taus = np.array([T[i, j] for i, j in dg.PAIRS])
    rb, ri = [], []
    for _ in range(20):
        p = rng.permutation(taus) * rng.choice([-1, 1], len(taus)); Tr = np.zeros((7, 7), int)
        for (i, j), t in zip(dg.PAIRS, p): Tr[i, j], Tr[j, i] = t, -t
        rb.append(lmin(base, Tr)); ri.append(lmin(ic, Tr))
    print(f"{f}: zero-lag base {lmin(base, Z0):+.3f} ict {lmin(ic, Z0):+.3f} | est-lag base {lmin(base, T):+.3f} ict {lmin(ic, T):+.3f} | rand-lag base med {np.median(rb):+.3f} ict med {np.median(ri):+.3f} (ict<base in {np.mean(np.array(ri)<np.array(rb)):.2f})")
