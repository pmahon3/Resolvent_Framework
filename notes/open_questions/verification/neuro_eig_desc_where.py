import sys, itertools, importlib.util, numpy as np
from pathlib import Path
from scipy.ndimage import uniform_filter1d
spec = importlib.util.spec_from_file_location("eg", sys.argv[1]); eg = importlib.util.module_from_spec(spec); spec.loader.exec_module(eg)
dg = eg.dg; d = Path(sys.argv[2])
for f, on, en in [l.split() for l in open(d/"seizures.txt") if l.strip()]:
    _, X = dg.read_edf(d/f, 7); N = X.shape[1]
    Y = X - uniform_filter1d(X, dg.FS, axis=1, mode="nearest"); T = dg.estimate_delays(Y)
    starts = np.arange(dg.MAXLAG, N - dg.WIN - dg.MAXLAG, dg.STEP)
    R = np.repeat(np.eye(7)[None], len(starts), 0)
    for i, j in dg.PAIRS:
        r = (eg.wcorr(Y[i], eg.shift(Y[j], T[i,j]), starts) + eg.wcorr(Y[j], eg.shift(Y[i], T[j,i]), starts))/2
        R[:, i, j] = R[:, j, i] = r
    full = np.linalg.eigvalsh(R)[:, 0] < 0
    tri = np.zeros(len(starts), bool); quad = np.zeros(len(starts), bool)
    for c in itertools.combinations(range(7), 3):
        tri |= np.linalg.eigvalsh(R[:, c][:, :, c])[:, 0] < 0
    for c in itertools.combinations(range(7), 4):
        quad |= np.linalg.eigvalsh(R[:, c][:, :, c])[:, 0] < 0
    # which chains: 0-3 temporal chain, 4-6 parasagittal; adjacent bipolar channels share an electrode
    print(f"{f}: full non-PSD {full.mean():.3f} | some 3x3 non-PSD {tri.mean():.3f} | some 4x4 {quad.mean():.3f} | full-but-no-3x3 {np.mean(full & ~tri):.3f}")
