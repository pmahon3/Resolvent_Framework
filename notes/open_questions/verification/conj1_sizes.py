"""Conjecture 1 evidence (2026-10-21): hiding <=> non-compressed, more sizes.
For a size: (i) exact cdd enumeration of extreme rays of V+ (non-binary => hides, by Maharam);
(ii) if all rays binary: cone(D) LP over a supply of buildable sets = pullbacks of exact small carriers (product <= 27
points) through all coordinatewise set-partition maps (up to relabelling). All rays in cone(D) => no hidden twist."""
import itertools, sys, numpy as np, cdd
from scipy.optimize import linprog
from scipy.sparse import csc_matrix
sys.argv_ = sys.argv[:]
sys.argv = ['x', '2,2,2']
exec(open('cone_D_pullback_lp.py').read().split('sz = tuple')[0])
def partitions(n, m):
    out = []
    for f in itertools.product(range(m), repeat=n):
        if len(set(f)) != m: continue
        firsts = [f.index(b) for b in range(m)]
        if firsts == sorted(firsts): out.append(f)
    return out
def check(sz):
    pts, rays = rays_of(sz)
    nb = [g for g in rays if not np.allclose(g[g > 0], g[g > 0][0])]
    if nb: return f"{sz}: {len(rays)} rays, {len(nb)} NON-BINARY -> hides"
    supply = set()
    smalls = [s for s in itertools.product(*[range(1, k + 1) for k in sz]) if np.prod(s) <= 27 and s != sz and min(s) >= 1]
    smalls = [s for s in smalls if all(s[k] <= sz[k] for k in range(3))]
    smalls = sorted(smalls, key=lambda s: -np.prod(s))[:8]
    for small in smalls:
        ptsS, DS = carrier(small); iS = {p: t for t, p in enumerate(ptsS)}
        for fm in itertools.product(*[partitions(sz[k], small[k]) for k in range(3)]):
            img = [iS[(fm[0][p[0]], fm[1][p[1]], fm[2][p[2]])] for p in pts]
            for S in DS: supply.add(sum(1 << t for t in range(len(pts)) if (S >> img[t]) & 1))
    supply = [s for s in supply if s]
    rows, cols = [], []
    for k, s in enumerate(supply):
        for t in range(len(pts)):
            if s >> t & 1: rows.append(t); cols.append(k)
    A = csc_matrix((np.ones(len(rows)), (rows, cols)), shape=(len(pts), len(supply)))
    bad = 0
    for g in rays:
        r = linprog(np.zeros(len(supply)), A_eq=A, b_eq=g, bounds=(0, None), method="highs")
        if r.status != 0 or np.abs(A @ r.x - g).max() > 1e-7: bad += 1
    return f"{sz}: {len(rays)} rays all binary; supply {len(supply)} from bases {smalls}; rays NOT in cone(D): {bad} -> " + ("NO hiding" if bad == 0 else "undecided")
for a in sys.argv_[1:]:
    print(check(tuple(map(int, a.split(",")))), flush=True)
