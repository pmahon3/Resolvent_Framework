"""Gap check (2026-10-20). With no non-binary extreme rays, a hidden twist at sizes sz exists iff some 0/1 extreme
ray of V+ is not in cone(D). Sufficient for 'no hidden twist': every 0/1 extreme ray set is BUILDABLE.
Test: a 0/1 set invariant under swapping two values of one coordinate is the pullback of a set on a smaller
triangle (merge the two values); pullbacks of buildable sets are buildable (transport). Recurse down to a base size
where D = V01 is known exactly by direct closure (computed here for the base sizes)."""
import itertools, sys, functools
import numpy as np, cdd
def setup(sz):
    pts = list(itertools.product(*[range(s) for s in sz])); E = [(0, 1), (1, 2), (2, 0)]
    cells = [(e, a, b) for e in range(3) for a in range(sz[E[e][0]]) for b in range(sz[E[e][1]])]
    M = np.array([[1 if (p[E[e][0]] == a and p[E[e][1]] == b) else 0 for (e, a, b) in cells] for p in pts])
    return pts, E, M
def binary_rays(sz):
    pts, E, M = setup(sz); cols = []
    for j in range(M.shape[1]):
        if np.linalg.matrix_rank(M[:, cols + [j]]) > len(cols): cols.append(j)
    B = M[:, cols]
    P = cdd.polyhedron_from_matrix(cdd.matrix_from_array([[0] + list(map(int, r)) for r in B], rep_type=cdd.RepType.INEQUALITY))
    out = []
    for row in cdd.copy_generators(P).array:
        if row[0] != 0: continue
        g = B @ np.array(row[1:]); g[np.abs(g) < 1e-9] = 0; nz = g[g > 0]
        assert np.allclose(nz, nz[0]), "non-binary ray present"
        out.append(frozenset(pts[i] for i in range(len(pts)) if g[i] > 0))
    return out
@functools.lru_cache(None)
def D_equals_V01(sz):
    pts, E, M = setup(sz); N = len(pts); full = (1 << N) - 1
    gens = set()
    for (i, j) in E:
        for S in range(1 << (sz[i] * sz[j])):
            gens.add(sum(1 << t for t, p in enumerate(pts) if S >> (p[i] * sz[j] + p[j]) & 1))
    D = gens | {0, full}; fr = list(D)
    while fr:
        new = set(); L = list(D)
        for a in fr:
            if full ^ a not in D: new.add(full ^ a)
            for b in L:
                if a & b == 0 and (a | b) not in D: new.add(a | b)
        D |= new; fr = list(new)
    r = np.linalg.matrix_rank(M); U = np.linalg.svd(M, full_matrices=False)[0][:, :r]
    # count V01 by pivot enumeration is heavy; instead test: every binary extreme ray is in D (sufficient for exactness)
    rays = binary_rays(sz)
    masks = [sum(1 << pts.index(p) for p in R) for R in rays]
    return all(m in D for m in masks), len(D)
def buildable(sz, S, base):
    if sz in base: return base[sz](S)
    for i in range(3):
        if sz[i] <= 1: continue
        for v, w in itertools.combinations(range(sz[i]), 2):
            sw = lambda p: tuple((w if p[k] == v else v if p[k] == w else p[k]) if k == i else p[k] for k in range(3))
            if all((sw(p) in S) == (p in S) for p in itertools.product(*[range(s) for s in sz])):
                mp = lambda x, v=v, w=w: v if x == w else (x if x < w else x - 1)   # merge w into v, relabel
                small = list(sz); small[i] -= 1
                S2 = frozenset(tuple(mp(p[k]) if k == i else p[k] for k in range(3)) for p in S)
                pre = frozenset(p for p in itertools.product(*[range(s) for s in sz]) if tuple(mp(p[k]) if k == i else p[k] for k in range(3)) in S2)
                assert pre == frozenset(S), "pullback mismatch"
                if buildable(tuple(small), S2, base): return True
    return False
if __name__ == "__main__":
    sz = tuple(map(int, sys.argv[1].split(",")))
    base_sizes = [tuple(map(int, b.split(","))) for b in sys.argv[2:]]
    base = {}
    for b in base_sizes:
        ok, nD = D_equals_V01(b); print(f"base {b}: |D| = {nD}, all binary rays in D: {ok}", flush=True)
        pts_b, _, _ = setup(b)
        if ok:
            # buildable test at base: membership in D of the set itself
            pts, E, M = setup(b); N = len(pts); full = (1 << N) - 1
            gens = set()
            for (i, j) in E:
                for S in range(1 << (b[i] * b[j])):
                    gens.add(sum(1 << t for t, p in enumerate(pts) if S >> (p[i] * b[j] + p[j]) & 1))
            D = gens | {0, full}; fr = list(D)
            while fr:
                new = set(); L = list(D)
                for a in fr:
                    if full ^ a not in D: new.add(full ^ a)
                    for c in L:
                        if a & c == 0 and (a | c) not in D: new.add(a | c)
                D |= new; fr = list(new)
            base[b] = (lambda D, pts: (lambda S: sum(1 << pts.index(p) for p in S) in D))(D, pts)
    rays = binary_rays(sz); fails = [R for R in rays if not buildable(sz, R, base)]
    print(f"sizes {sz}: binary extreme rays {len(rays)}, shown buildable by pullback {len(rays) - len(fails)}, undecided {len(fails)}")
