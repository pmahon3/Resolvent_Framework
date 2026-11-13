# Independent recount for FOUR_QUANTITIES_CHECK.md (hostile check, 2026-11-13). Written from scratch.
# For K4 on 2x2x2x2 and 2x2x2x3: brute force over ALL subsets of the grid.
#  - V01 membership by an EXACT integer test: v is in the span of the pair indicators iff K^T v = 0, where the
#    columns of K are an integer basis of the orthogonal complement (sympy exact nullspace).
#  - D4 by closure under complement and disjoint union, run to a FIXPOINT (no early stop), on bitmasks.
#  - irreducible: for every coordinate and every two values, the slice difference is NOT a function of at most one
#    of the other coordinates (definition used directly; T1 is not used).
#  - on 2x2x2x2: compare the irreducible sets with the orbit of A4 as sets.
# Memory: chunks of 2^20 subsets x 24 points, a few hundred MB at most.
import itertools, numpy as np, sympy

def run(n):
    pts = list(itertools.product(*[range(k) for k in n])); N = len(pts); P = np.array(pts)
    gens = [((P[:, i] == a) & (P[:, j] == b)).astype(int)
            for i, j in itertools.combinations(range(4), 2) for a in range(n[i]) for b in range(n[j])]
    G = sympy.Matrix(gens)                       # rows span the pair-sum space
    ns = G.nullspace()                           # exact; vectors v with G v = 0
    K = []
    for v in ns:
        den = sympy.ilcm(*[sympy.fraction(x)[1] for x in v])
        K.append([int(x * den) for x in v])
    K = np.array(K, dtype=np.int64).T            # N x k
    rank = G.rank(); assert rank + K.shape[1] == N
    V = []
    chunk = 1 << 20
    for s in range(0, 1 << N, chunk):
        c = np.arange(s, min(s + chunk, 1 << N), dtype=np.int64)
        bits = ((c[:, None] >> np.arange(N)) & 1)
        ok = ((bits @ K) == 0).all(axis=1)
        V.append(c[ok])
    V = np.concatenate(V); Vset = set(V.tolist())
    # closure to fixpoint
    D = set()
    for i, j in itertools.combinations(range(4), 2):
        cells = [sum(1 << k for k in range(N) if pts[k][i] == a and pts[k][j] == b)
                 for a in range(n[i]) for b in range(n[j])]
        for m in range(1 << len(cells)):
            D.add(sum(cells[k] for k in range(len(cells)) if m >> k & 1))
    FULL = (1 << N) - 1
    while True:
        L = list(D); new = set()
        for x in L:
            if FULL ^ x not in D: new.add(FULL ^ x)
        for x in L:
            for y in L:
                if x & y == 0 and (x | y) not in D: new.add(x | y)
        if not new: break
        D |= new
    # irreducible sets
    arr = ((V[:, None] >> np.arange(N)) & 1).astype(np.int8).reshape((-1,) + tuple(n))
    red = np.zeros(len(arr), bool)
    for ax in range(4):
        rest = [k for k in range(4) if k != ax]
        for a, b in itertools.combinations(range(n[ax]), 2):
            d = np.take(arr, a, axis=ax + 1) - np.take(arr, b, axis=ax + 1)      # (m, three remaining axes)
            for keep in range(3):
                oth = tuple(k + 1 for k in range(3) if k != keep)
                red |= ((d.max(axis=oth) - d.min(axis=oth)) == 0).all(axis=1)   # constant along the two others
    irr = arr[~red]
    print(n, 'span rank', rank, '| |V01| (exact, all %d subsets)' % (1 << N), len(Vset), '| |D4| (fixpoint)', len(D),
          '| D4 == V01 as sets:', D == Vset, '| irreducible', len(irr), flush=True)
    return irr

irr = run((2, 2, 2, 2))
A4 = np.zeros((2, 2, 2, 2), np.int8)
for p, u, v, t in itertools.product(range(2), repeat=4):
    c = (u, v, t) in [(0, 1, 1), (1, 0, 0)]; k = (p, u, v) in [(0, 0, 0), (1, 1, 1)]
    assert not (c and k)                                                          # the two pieces are disjoint
    if c or k: A4[p, u, v, t] = 1
orbit = set(); orbit_nocompl = set()
for perm in itertools.permutations(range(4)):
    q = np.transpose(A4, perm)
    for fl in itertools.product([0, 1], repeat=4):
        r = q
        for ax, f in enumerate(fl):
            if f: r = np.flip(r, axis=ax)
        orbit.add(r.tobytes()); orbit.add((1 - r).tobytes()); orbit_nocompl.add(r.tobytes())
print('A4 worlds', int(A4.sum()), '| orbit (with complement)', len(orbit), '| orbit (without complement)', len(orbit_nocompl),
      '| orbit == irreducible sets on 2222:', orbit == {x.tobytes() for x in irr})
run((2, 2, 2, 3))
