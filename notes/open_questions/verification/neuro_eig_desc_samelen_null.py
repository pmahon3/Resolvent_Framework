import sys, importlib.util, numpy as np
from pathlib import Path
from scipy.ndimage import uniform_filter1d
spec = importlib.util.spec_from_file_location("eg", sys.argv[1]); eg = importlib.util.module_from_spec(spec); spec.loader.exec_module(eg)
dg = eg.dg; d = Path(sys.argv[2])
def lmin(Z, T):
    R = np.eye(7)
    for i, j in dg.PAIRS:
        a, b = dg.shifted(Z[i], Z[j], T[i, j]); R[i, j] = R[j, i] = np.corrcoef(a, b)[0, 1]
    return np.linalg.eigvalsh(R)[0]
for f, on, en in [l.split() for l in open(d/"seizures.txt") if l.strip()]:
    on, en = float(on), float(en)
    _, X = dg.read_edf(d/f, 7)
    Y = X - uniform_filter1d(X, 256, axis=1, mode="nearest"); T = dg.estimate_delays(Y)
    L = int((en - on) * 256); ict = lmin(Y[:, int(on*256):int(en*256)], T)
    null = [lmin(Y[:, s:s+L], T) for s in range(0, 600*256 - L, 5*256)
            if on >= 960 or (s + L)/256 <= on - 60]
    null = np.array(null)
    print(f"{f}: ictal {ict:+.3f} | baseline same-length windows n={len(null)}: median {np.median(null):+.3f}, 1st pct {np.percentile(null,1):+.3f}, frac below ictal {np.mean(null <= ict):.3f}")
