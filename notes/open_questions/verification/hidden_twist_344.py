"""Problem 2(b) (2026-10-21): explicit candidate hidden twist at sizes 3x4x4.
Pair laws mu (cells >= 0, each edge sums to 1, consistent single-variable marginals), forced functional
Lambda = mu on the span; constraints Lambda(S) >= 0 for every S in a large supply of buildable sets
(pullbacks of exact carriers one size down, plus pair events); objective: minimise Lambda(g) for the exact
non-binary extreme ray g. Lambda(g) < 0 => candidate (hidden on the supply; full-carrier positivity is
guaranteed to exist by separation, not certified for THIS Lambda)."""
import itertools, numpy as np, sys
from scipy.optimize import linprog
from scipy.sparse import csr_matrix
sys.argv = ['x', '2,2,2']
exec(open('cone_D_pullback_lp.py').read().split('sz = tuple')[0])
sz = (3, 4, 4)
pts, rays = rays_of(sz); idx = {p: t for t, p in enumerate(pts)}
_, E, M = setup(sz)
cells = [(e, a, b) for e in range(3) for a in range(sz[E[e][0]]) for b in range(sz[E[e][1]])]
nb = [g for g in rays if not np.allclose(g[g > 0], g[g > 0][0])]
g = nb[0]; print("non-binary rays:", len(nb))
supply = set()
def surjections(n, m):
    # set partitions of {0..n-1} into m blocks, canonically labelled (D is invariant under value relabelling)
    out = []
    for f in itertools.product(range(m), repeat=n):
        if len(set(f)) != m: continue
        firsts = [f.index(b) for b in range(m)]
        if firsts == sorted(firsts): out.append(f)
    return out
bases = [(3, 3, 3), (2, 3, 4), (2, 4, 3), (3, 2, 4), (3, 4, 2), (2, 3, 3), (3, 3, 2), (3, 2, 3)]
for small in bases:
    ptsS, DS = carrier(small); iS = {p: t for t, p in enumerate(ptsS)}
    maps = list(itertools.product(*[surjections(sz[k], small[k]) for k in range(3)]))
    print("  base", small, len(DS), "maps", len(maps), flush=True)
    for fm in maps:
        img = [iS[(fm[0][p[0]], fm[1][p[1]], fm[2][p[2]])] for p in pts]
        for S in DS:
            supply.add(sum(1 << t for t in range(len(pts)) if (S >> img[t]) & 1))
    print("    supply so far", len(supply), flush=True)
supply = [s for s in supply if s]; print("supply", len(supply), flush=True)
Mp = np.linalg.pinv(M)
supply = np.array(supply, dtype=object)
Aeq, beq = [], []
for e in range(3):
    Aeq.append([1.0 if c[0] == e else 0.0 for c in cells]); beq.append(1.0)
for v in range(3):
    es = [(e, E[e].index(v)) for e in range(3) if v in E[e]]
    (e1, s1), (e2, s2) = es
    for val in range(sz[v]):
        Aeq.append([(1.0 if (c[0] == e1 and (c[1], c[2])[s1] == val) else 0.0) - (1.0 if (c[0] == e2 and (c[1], c[2])[s2] == val) else 0.0) for c in cells]); beq.append(0.0)
obj = Mp @ g
def coeff(s): return Mp @ np.array([(int(s) >> t) & 1 for t in range(len(pts))], float)
active = []
for it in range(60):
    A_ub = -np.array([coeff(s) for s in active]) if active else None
    res = linprog(obj, A_ub=A_ub, b_ub=np.zeros(len(active)) if active else None, A_eq=Aeq, b_eq=beq, bounds=[(0, None)] * len(cells), method="highs")
    mu = res.x; worst = []
    for k in range(0, len(supply), 50000):
        chunk = supply[k:k + 50000]
        F = np.array([[(int(s) >> t) & 1 for t in range(len(pts))] for s in chunk], float)
        vals = (F @ Mp.T) @ mu
        bad = np.where(vals < -1e-9)[0]
        worst += [(vals[b], chunk[b]) for b in bad]
    print(f"  iter {it}: Lambda(g) = {res.fun:.6f}, violated supply sets {len(worst)}", flush=True)
    if not worst: break
    worst.sort(key=lambda t: t[0]); active += [w for _, w in worst[:3000]]
print("status", res.status, "min Lambda(g) =", round(res.fun, 6))
mu = res.x
for e in range(3):
    i, j = E[e]
    T = np.zeros((sz[i], sz[j]))
    for k, c in enumerate(cells):
        if c[0] == e: T[c[1], c[2]] = mu[k]
    print(f"pair law (x{i},x{j}):\n", np.round(T, 4))
np.save('hidden_twist_344_mu.npy', mu)
