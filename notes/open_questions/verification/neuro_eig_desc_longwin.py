import sys, itertools, importlib.util, numpy as np
from pathlib import Path
from scipy.ndimage import uniform_filter1d
spec = importlib.util.spec_from_file_location("eg", sys.argv[1]); eg = importlib.util.module_from_spec(spec); spec.loader.exec_module(eg)
dg = eg.dg; d = Path(sys.argv[2])
for f, on, en in [l.split() for l in open(d/"seizures.txt") if l.strip()]:
    _, X = dg.read_edf(d/f, 7)
    Y = X - uniform_filter1d(X, dg.FS, axis=1, mode="nearest"); T = dg.estimate_delays(Y)
    out = []
    for lo, hi, nm in [(0, 600, "base0-10"), (float(on)-300, float(on), "pre5"), (float(on), float(en), "ictal")]:
        if hi <= lo or lo < 0: out.append(f"{nm} n/a"); continue
        Z = Y[:, int(lo*256):int(hi*256)]
        R = np.eye(7)
        for i, j in dg.PAIRS:
            a, b = dg.shifted(Z[i], Z[j], T[i, j]); R[i, j] = R[j, i] = np.corrcoef(a, b)[0, 1]
        ev = np.linalg.eigvalsh(R)
        tri = min(np.linalg.eigvalsh(R[np.ix_(c, c)])[0] for c in itertools.combinations(range(7), 3))
        out.append(f"{nm} lmin {ev[0]:+.3f} (min3x3 {tri:+.3f})")
    print(f, " | ".join(out))
