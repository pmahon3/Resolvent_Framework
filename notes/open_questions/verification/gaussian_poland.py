#!/usr/bin/env python3
"""Step 3 of GAUSSIAN_PAIRWISE_MODEL.md: Poland 10 beech sites, V_G with/without the dT cue; posterior, bootstrap, placebo.
Usage: python3 -I gaussian_poland.py <MASTREE csv> <weather dir>"""
import sys, math, itertools, importlib.util
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from scipy.stats import invwishart
here = Path(__file__).parent
def mod(n, f):
    sp = importlib.util.spec_from_file_location(n, here / f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
m = mod("m", "mast_ceiling_gate.py"); c = mod("c", "mast_conditional_gate.py"); g = mod("g", "gaussian_pairwise.py")


class FastVG:
    def __init__(self, k):
        self.k = k; self.pairs = np.array(list(itertools.combinations(range(k), 2))); self.w = np.zeros(len(self.pairs))
    def __call__(self, R):
        I, J = self.pairs.T; a = np.abs(R[I, J]) + 1e-12; k = self.k
        def loads(w):
            L = np.zeros(k); np.add.at(L, I, a*np.exp(w)); np.add.at(L, J, a*np.exp(-w)); return L
        w = self.w.copy()
        for beta in (20., 100., 400.):
            def f(w):
                L = loads(w); z = beta*(L-1); mx = z.max(); e = np.exp(z-mx); s = e/e.sum()
                val = (mx + np.log(e.sum()))/beta
                grad = s[I]*a*np.exp(w) - s[J]*a*np.exp(-w)
                return val, grad
            w = minimize(f, w, jac=True, method="L-BFGS-B").x
        self.w = w
        return float(loads(w).max() - 1)


def corr(Sig):
    d = np.sqrt(np.diag(Sig)); return Sig / np.outer(d, d)


def main(csvp, wdir):
    rng = np.random.default_rng(4); S = m.load(csvp)
    sites = sorted(s for s, (ser, meta) in S.items() if meta[1] == "D00013" and len(ser) >= 30)
    T = {s: c.junjul(Path(wdir) / f"PL{s}.json") for s in sites}
    yrs = sorted(y for y in set.intersection(*[set(S[s][0]) for s in sites]) if y >= 1942 and all(y-1 in T[s] and y-2 in T[s] for s in sites))
    n, k = len(yrs), len(sites); print(f"sites {k}, years {n} ({yrs[0]}-{yrs[-1]})")
    Y = np.log1p(np.array([[S[s][0][y] for s in sites] for y in yrs]))
    dT = np.array([[T[s][y-1] - T[s][y-2] for s in sites] for y in yrs]); t = np.array(yrs, float)
    vg = FastVG(k); vg(np.corrcoef(Y.T))

    def residuals(dTmat):
        E = np.empty_like(Y)
        for j in range(k):
            cols = [t] + ([dTmat[:, j]] if dTmat is not None else [])
            E[:, j], _ = c.resid(Y[:, j], cols)
        return E

    for label, D in (("detrended, no cue", None), ("detrended + own dT", dT)):
        E = residuals(D); p_reg = 2 + (D is not None)
        Vpt = vg(np.corrcoef(E.T))
        Sm = E.T @ E; post = [vg(corr(invwishart.rvs(df=n - p_reg, scale=Sm, random_state=rng))) for _ in range(2000)]
        post = np.array(post)
        b = 3; nb = math.ceil(n/b); boots = []
        for _ in range(2000):
            st = rng.integers(0, n-b+1, nb); idx = (st[:, None] + np.arange(b)).ravel()[:n]
            boots.append(vg(np.corrcoef(E[idx].T)))
        boots = np.array(boots)
        print(f"\n== {label}: point V_G = {Vpt:+.3f}")
        print(f"   posterior (inv-Wishart): P(V_G>0) = {np.mean(post>0):.3f}, median {np.median(post):+.3f}, 2.5% {np.percentile(post,2.5):+.3f}")
        print(f"   bootstrap (model-free):  5% lower bound {np.percentile(boots,5):+.3f}, P*(V_G<=0) = {np.mean(boots<=0):.3f}")
        if D is not None: Vcue = Vpt
        else: Vraw = Vpt
    plac = []
    for _ in range(200):
        perm = rng.permutation(n); plac.append(vg(np.corrcoef(residuals(dT[perm]).T)))
    plac = np.array(plac)
    print(f"\nplacebo (dT years permuted, 200): point V_G median {np.median(plac):+.3f}; fraction <= real-cue V_G ({Vcue:+.3f}): {np.mean(plac <= Vcue):.3f}")
    print(f"drop due to real cue: {Vraw - Vcue:+.3f}; placebo drops median {Vraw - np.median(plac):+.3f}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
