# Independent check (2026-11-13, GLUING_LEMMA_CHECK.md). Exact integer arithmetic, any shape, any sizes (N <= 62).
# Usage: python3 gluing_check_exact_D_vs_V01_any_shape.py SIZES OBSERVERS [--save FILE]
#   e.g.  ... 2,2,2,2,2 01,02,03,04,12,13,14,23,24      (K5 minus the pair 34)
# V01: a function is in the span of the observers' functions iff it is f(x) = sum_{y <= x, supp(y) inside an observer} c_y
# (y <= x: y agrees with x off the zeros of y). The system is unitriangular on the "information points" (points whose
# support lies inside an observer), so values there determine f by an INTEGER extension matrix E. Enumerate 0/1 values
# on the information points, extend, keep the 0/1 results. No floats.
# D: closure of all observers' events under complement and disjoint union, run to a fixed point (no early stop).
import sys, itertools, time, numpy as np
n = tuple(int(a) for a in sys.argv[1].split(','))
OBS = [tuple(int(ch) for ch in o) for o in sys.argv[2].split(',')]
save = sys.argv[sys.argv.index('--save') + 1] if '--save' in sys.argv else None
m = len(n); pts = list(itertools.product(*[range(k) for k in n])); N = len(pts); assert N <= 62
idx = {p: i for i, p in enumerate(pts)}
t0 = time.time()
supp = lambda p: frozenset(i for i in range(m) if p[i] != 0)
allowed = lambda s: any(s <= frozenset(o) for o in OBS)
info = [p for p in pts if allowed(supp(p))]; r = len(info)
below = lambda y, x: all(y[i] == 0 or y[i] == x[i] for i in range(m))
# M[x][k] = 1 if info[k] <= x ; f = M c.  T = M restricted to info rows (unitriangular after sorting by |supp|).
info.sort(key=lambda p: len(supp(p)))
M = np.array([[1 if below(y, x) else 0 for y in info] for x in pts], dtype=object)
T = np.array([[1 if below(y, x) else 0 for y in info] for x in info], dtype=object)
# integer inverse of lower-unitriangular T by forward substitution
Tinv = np.zeros((r, r), dtype=object)
for k in range(r):
    for j in range(r):
        Tinv[k, j] = (1 if k == j else 0) - sum(T[k, l] * Tinv[l, j] for l in range(k))
assert (T.dot(Tinv) == np.eye(r, dtype=object)).all()
E = M.dot(Tinv).astype(np.int64)            # N x r : f = E v, v = values on the information points
info_rows = np.array([idx[p] for p in info])
assert (E[info_rows] == np.eye(r, dtype=np.int64)).all()
print('sizes', n, 'observers', OBS, 'points', N, 'span dimension', r, flush=True)
w = (np.uint64(1) << np.arange(N, dtype=np.uint64))
V = []; chunk = 1 << 18; ar = np.arange(r)
for s in range(0, 1 << r, chunk):
    c = np.arange(s, min(s + chunk, 1 << r), dtype=np.int64)
    v = ((c[:, None] >> ar) & 1).astype(np.int32)
    f = v @ E.T.astype(np.int32)
    ok = ((f == 0) | (f == 1)).all(axis=1)
    if ok.any(): V.append((f[ok].astype(np.uint64) * w).sum(axis=1))
V = np.unique(np.concatenate(V)); Vset = set(V.tolist())
print('|V01| =', len(Vset), ' (exact)  time %.0fs' % (time.time() - t0), flush=True)
# ---- D by closure to a fixed point
P = np.array(pts); FULL = (1 << N) - 1
gens = set()
for o in OBS:
    cells = {}
    for i, p in enumerate(pts): cells[tuple(p[j] for j in o)] = cells.get(tuple(p[j] for j in o), 0) | (1 << i)
    cl = list(cells.values())
    if len(cl) > 20: sys.exit('observer too wide for generator enumeration')
    for mask in range(1 << len(cl)):
        acc = 0
        for k in range(len(cl)):
            if mask >> k & 1: acc |= cl[k]
        gens.add(acc)
D = set(gens); fr = set(gens); rnd = 0
while fr:
    rnd += 1; Darr = np.fromiter(D, dtype=np.uint64, count=len(D)); new = set()
    for x in fr:
        c = FULL ^ x
        if c not in D: new.add(c)
    for x in fr:
        ux = np.uint64(x); ys = Darr[(Darr & ux) == 0]
        if len(ys): new.update((ys | ux).tolist())
    new -= D; D |= new; fr = new
    print(' round', rnd, 'new', len(new), '|D|', len(D), 'time %.0fs' % (time.time() - t0), flush=True)
gap = sorted(Vset - D, key=lambda z: (bin(z).count('1'), z))
print('RESULT sizes', n, 'observers', sys.argv[2], '|D|', len(D), '|V01|', len(Vset), 'gap', len(gap), 'D subset V01:', D <= Vset)
from collections import Counter
if gap:
    print(' gap sizes (points: count):', dict(sorted(Counter(bin(z).count('1') for z in gap).items())))
    for z in gap[:4]: print('  gap set:', ' '.join(''.join(map(str, p)) for k, p in enumerate(pts) if z >> k & 1))
if save: np.save(save, np.array(gap, dtype=np.uint64))
