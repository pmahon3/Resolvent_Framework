# 2026-11-10 (D3 = D_fin reversal check). Independent code, finite grids only: evidence, never a proof over N.
#  (A) |B| (box sets, by brute parametrisation) and |D3| (worklist Dynkin closure from window events)
#      on a grid given on the command line (keep it <= 3x3x3: pure-python closure).
#  (B) The Step-4 reduction run as a procedure on EVERY box set of the grid:
#      - some dimension is 1                      -> window event, stop;
#      - some pair of slices is not K-related     -> delete one of the two slices, recurse;
#      - every pair at every coordinate K-related -> ASSERT |X0|=|X1|=|X2| and F = E_< for an explicit total
#        order on the disjoint union of the three alphabets (the claim "step 1's chain forces a circular
#        arrangement"), and ASSERT that one adjacent swap of differently coloured elements toggles one full
#        window line.
# usage: python3 reversal_check_step4.py n0 n1 n2 [noclosure]
import sys, itertools
import numpy as np
n0, n1, n2 = (int(a) for a in sys.argv[1:4])
shape = (n0, n1, n2)
N = n0 * n1 * n2
pts = list(itertools.product(range(n0), range(n1), range(n2)))
idx = {p: i for i, p in enumerate(pts)}

def is_box(F):
    f = F.astype(int)
    d = f - f[:1]; d = d - d[:, :1]; d = d - d[:, :, :1]
    return not d.any()

# ---- box sets: base slice G, other slices G + additive difference
cells = list(itertools.product(range(n1), range(n2)))
adds = set()
for al in itertools.product(range(-1, 2), repeat=n1):
    for be in itertools.product(range(-2, 3), repeat=n2):
        d = tuple(al[i] + be[j] for i, j in cells)
        if all(-1 <= v <= 1 for v in d): adds.add(d)
adds = [np.array(d).reshape(n1, n2) for d in adds]
boxsets = []
for bits in itertools.product((0, 1), repeat=n1 * n2):
    G = np.array(bits).reshape(n1, n2)
    valid = [G + d for d in adds if ((G + d) >= 0).all() and ((G + d) <= 1).all()]
    for combo in itertools.product(valid, repeat=n0 - 1):
        boxsets.append(np.stack([G] + list(combo)).astype(bool))
print('grid', shape, '|B| =', len(boxsets), 'distinct', len({F.tobytes() for F in boxsets}))
assert all(is_box(F) for F in boxsets[:2000])

# ---- (A) closure
if len(sys.argv) < 5:
    full = (1 << N) - 1
    gens = set()
    for (i, j) in [(0, 1), (1, 2), (2, 0)]:
        pairs = sorted({(p[i], p[j]) for p in pts})
        for r in range(1 << len(pairs)):
            sel = {pairs[t] for t in range(len(pairs)) if r >> t & 1}
            gens.add(sum(1 << idx[p] for p in pts if (p[i], p[j]) in sel))
    S = set(); work = list(gens)
    while work:
        x = work.pop()
        if x in S: continue
        cur = list(S)
        S.add(x)
        c = full & ~x
        if c not in S: work.append(c)
        for y in cur:
            if x & y == 0:
                u = x | y
                if u not in S: work.append(u)
    Bmasks = {sum(1 << idx[p] for p in pts if F[p]) for F in boxsets}
    print('|D3| =', len(S), ' D3 == B:', S == Bmasks)

# ---- (B) Step-4 reduction
def nonK(d):  # d a 2D integer array (difference of two slices); True iff a function of one coordinate alone
    return (d == d[:, :1]).all() or (d == d[:1, :]).all()

stats = {'window': 0, 'merge': 0, 'allK': 0}
def reduce(F):
    if 1 in F.shape:
        stats['window'] += 1; return
    f = F.astype(int)
    for ax in range(3):
        g = np.moveaxis(f, ax, 0)
        for a in range(g.shape[0]):
            for b in range(a):
                if nonK(g[a] - g[b]):
                    stats['merge'] += 1
                    reduce(np.delete(F, a, axis=ax)); return
    # all pairs K-related at every coordinate
    stats['allK'] += 1
    m0, m1, m2 = F.shape
    assert m0 == m1 == m2, ('all-K but unequal sizes', F.shape)
    n = m0 - 1
    U = {}; V = {}
    for i in range(1, m0):
        d = f[i] - f[0]
        Ui = frozenset(y for y in range(m1) if d[y].max() == 1)
        Vi = frozenset(z for z in range(m2) if d[:, z].max() == 1)
        assert all(d[y, z] == (y in Ui) + (z in Vi) - 1 for y in range(m1) for z in range(m2))
        U[i] = Ui; V[i] = Vi
    order = sorted(range(1, m0), key=lambda i: len(U[i]))
    for s, t in zip(order, order[1:]):
        assert U[s] < U[t] and V[s] > V[t], 'not a strict anti-ordered chain'
    rank = {0: 0}; rank.update({i: r + 1 for r, i in enumerate(order)})
    lam = {y: min([rank[i] for i in range(1, m0) if y in U[i]] + [n + 1]) for y in range(m1)}
    mu = {z: max([rank[i] for i in range(1, m0) if z in V[i]] + [0]) + 1 for z in range(m2)}
    assert sorted(lam.values()) == list(range(1, n + 2)) and sorted(mu.values()) == list(range(1, n + 2))
    pos = {}
    for a in range(m0): pos[(0, a)] = 3 * rank[a]
    zof = {mu[z]: z for z in range(m2)}
    for y in range(m1):
        z = zof[lam[y]]
        if f[0, y, z] == 1: pos[(2, z)] = 3 * lam[y] - 2; pos[(1, y)] = 3 * lam[y] - 1   # z before y
        else:               pos[(1, y)] = 3 * lam[y] - 2; pos[(2, z)] = 3 * lam[y] - 1
    def E(pos):
        G = np.zeros(F.shape, dtype=int)
        for (a, y, z) in itertools.product(range(m0), range(m1), range(m2)):
            G[a, y, z] = (pos[(2, z)] < pos[(1, y)]) + (pos[(1, y)] < pos[(0, a)]) + (pos[(0, a)] < pos[(2, z)]) - 1
        return G
    G = E(pos)
    assert (G == f).all(), 'all-K set is not the order set of the arrangement'
    # one adjacent swap: the x0-value of rank 0 with its right neighbour (position 1)
    a0 = [a for a in range(m0) if rank[a] == 0][0]
    nb = [e for e in pos if pos[e] == 1][0]
    pos2 = dict(pos); pos2[(0, a0)] = 1; pos2[nb] = 0
    G2 = E(pos2); D = G2 - G
    line = np.zeros(F.shape, dtype=bool)
    ix = [slice(None)] * 3; ix[0] = a0; ix[nb[0]] = nb[1]; line[tuple(ix)] = True
    assert ((D != 0) == line).all() and (len(set(D[line])) == 1) and set(G2.flatten()) <= {0, 1}

for F in boxsets: reduce(F)
print('Step-4 reduction ran on every box set with no assertion failure; calls:', stats)
