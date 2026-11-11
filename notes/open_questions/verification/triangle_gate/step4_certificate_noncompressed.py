# 2026-11-10 (TRIANGLE_CONSEQUENCES_CHECK.md, item C2).  Evidence only, finite grids.
# Step 4 of TRIANGLE_D3_DFIN_REVERSAL_CHECK.md run as a CERTIFICATE-PRODUCING procedure, no Dynkin closure:
# certify(F) returns True only if F is derived from window events by steps that are each verified on the
# concrete arrays and are each legitimate in a Dynkin system:
#   base   : a grid with a one-point coordinate (every set is a window event);
#   merge  : slices a, b at one coordinate differ by a function h of ONE other coordinate.  Verified:
#            Fhat := (F with slice a replaced by slice b) is the pullback of F minus slice a (certified
#            recursively on the smaller grid); A := {x=a, h=-1} is a window event inside Fhat;
#            Bs := {x=a, h=+1} is a window event disjoint from Fhat; F = (Fhat \ A) ⊔ Bs.
#   order  : all pairs at coordinate 0 are K-related.  Build the total order of Fix 2, verify F = E_<,
#            do two adjacent swaps (Fix 3), verify each toggles exactly one full window line that was
#            entirely inside or entirely outside, then certify the result (which must have a merge).
# Box sets are enumerated from the pair-sum parametrisation (base slice + additive slice differences),
# uniformly at random: P(G) proportional to v(G)^(n0-1).  Negative control: non-box sets must be rejected.
# usage: python3 step4_certificate_noncompressed.py n0 n1 n2 nsamples [seed]     (memory: small)
import sys, itertools, random
import numpy as np
n0, n1, n2 = (int(a) for a in sys.argv[1:4]); NS = int(sys.argv[4])
seed = int(sys.argv[5]) if len(sys.argv) > 5 else 1
rng = random.Random(seed); nrng = np.random.default_rng(seed)

def is_box(F):
    f = F.astype(int)
    d = f - f[:1]; d = d - d[:, :1]; d = d - d[:, :, :1]
    return not d.any()

def is_window_event(S):  # depends on at most two coordinates
    return any((S == S.take([0], axis=ax)).all() for ax in range(3))

stats = {'base': 0, 'merge': 0, 'order': 0, 'memo': 0}
memo = {}

def find_merge(F):
    f = F.astype(np.int8)
    for ax in range(3):
        g = np.moveaxis(f, ax, 0)
        for a in range(g.shape[0]):
            for b in range(a):
                d = g[a] - g[b]
                if (d == d[:, :1]).all(): return ax, a, b, 0, d[:, 0]   # function of first other coordinate
                if (d == d[:1, :]).all(): return ax, a, b, 1, d[0, :]   # function of second other coordinate
    return None

def certify(F, must_merge=False):
    key = (F.shape, F.tobytes())
    if key in memo: stats['memo'] += 1; return memo[key]
    if len(memo) > 400000: memo.clear()
    ok = _certify(F, must_merge)
    memo[key] = ok
    return ok

def _certify(F, must_merge):
    if 1 in F.shape:
        stats['base'] += 1; return is_window_event(F)
    m = find_merge(F)
    if m is not None:
        ax, a, b, which, h = m
        g = np.moveaxis(F, ax, 0)                      # view
        hat = g.copy(); hat[a] = g[b]
        hfull = (h[:, None] if which == 0 else h[None, :]) * np.ones(g.shape[1:], dtype=int)
        A = np.zeros_like(g); A[a] = (hfull == -1)
        Bs = np.zeros_like(g); Bs[a] = (hfull == 1)
        Am, Bm = np.moveaxis(A, 0, ax), np.moveaxis(Bs, 0, ax)
        if not (is_window_event(Am) and is_window_event(Bm)): return False
        if (A & ~hat).any() or (Bs & hat).any(): return False
        if not (((hat & ~A) | Bs) == g).all(): return False
        small = np.delete(F, a, axis=ax)               # hat = pullback of small along a -> b (by construction)
        stats['merge'] += 1
        return certify(np.ascontiguousarray(small))
    if must_merge: return False
    # ---- all pairs K-related at every coordinate: order set
    stats['order'] += 1
    f = F.astype(int); m0, m1, m2 = F.shape
    if not (m0 == m1 == m2): return False
    n = m0 - 1; U = {}; V = {}
    for i in range(1, m0):
        d = f[i] - f[0]
        Ui = frozenset(y for y in range(m1) if d[y].max() == 1)
        Vi = frozenset(z for z in range(m2) if d[:, z].max() == 1)
        if not all(d[y, z] == (y in Ui) + (z in Vi) - 1 for y in range(m1) for z in range(m2)): return False
        U[i] = Ui; V[i] = Vi
    order = sorted(range(1, m0), key=lambda i: len(U[i]))
    if not all(U[s] < U[t] and V[s] > V[t] for s, t in zip(order, order[1:])): return False
    rank = {0: 0}; rank.update({i: r + 1 for r, i in enumerate(order)})
    lam = {y: min([rank[i] for i in range(1, m0) if y in U[i]] + [n + 1]) for y in range(m1)}
    mu = {z: max([rank[i] for i in range(1, m0) if z in V[i]] + [0]) + 1 for z in range(m2)}
    if sorted(lam.values()) != list(range(1, n + 2)) or sorted(mu.values()) != list(range(1, n + 2)): return False
    pos = {}
    for a in range(m0): pos[(0, a)] = 3 * rank[a]
    zof = {mu[z]: z for z in range(m2)}
    for y in range(m1):
        z = zof[lam[y]]
        if f[0, y, z] == 1: pos[(2, z)] = 3 * lam[y] - 2; pos[(1, y)] = 3 * lam[y] - 1
        else:               pos[(1, y)] = 3 * lam[y] - 2; pos[(2, z)] = 3 * lam[y] - 1
    def E(pos):
        G = np.zeros(F.shape, dtype=int)
        for (a, y, z) in itertools.product(range(m0), range(m1), range(m2)):
            G[a, y, z] = (pos[(2, z)] < pos[(1, y)]) + (pos[(1, y)] < pos[(0, a)]) + (pos[(0, a)] < pos[(2, z)]) - 1
        return G
    cur = E(pos)
    if not (cur == f).all(): return False
    a0 = [a for a in range(m0) if rank[a] == 0][0]
    for step in (1, 2):                                # two adjacent swaps: a0 moves right past y_1 and z_1
        nb = [e for e in pos if pos[e] == pos[(0, a0)] + 1][0]
        if nb[0] == 0: return False
        pos2 = dict(pos); pos2[(0, a0)], pos2[nb] = pos[nb], pos[(0, a0)]
        new = E(pos2)
        if not set(new.flatten()) <= {0, 1}: return False
        line = np.zeros(F.shape, dtype=bool)
        ix = [slice(None)] * 3; ix[0] = a0; ix[nb[0]] = nb[1]; line[tuple(ix)] = True
        if not is_window_event(line): return False
        D = new - cur
        if not ((D != 0) == line).all() or len(set(D[line])) != 1: return False   # line was wholly in or wholly out
        pos, cur = pos2, new
    return certify(cur.astype(bool), must_merge=True)

# ---- uniform sampling of box sets on n0 x n1 x n2
cells = list(itertools.product(range(n1), range(n2))); M = len(cells)
adds = set()
for al in itertools.product(range(-1, 2), repeat=n1):
    for be in itertools.product(range(-2, 3), repeat=n2):
        d = tuple(al[i] + be[j] for i, j in cells)
        if all(-1 <= v <= 1 for v in d): adds.add(d)
adds = sorted(adds)
posm = np.array([sum(1 << k for k, v in enumerate(d) if v == 1) for d in adds], dtype=np.int64)
negm = np.array([sum(1 << k for k, v in enumerate(d) if v == -1) for d in adds], dtype=np.int64)
Gs = np.arange(1 << M, dtype=np.int64)
v = np.zeros(1 << M, dtype=np.int64)
for p, m in zip(posm, negm): v += ((Gs & p) == 0) & ((~Gs & m) == 0)
w = v.astype(object) ** (n0 - 1)
total = int(sum(w))
print('grid', (n0, n1, n2), 'additive differences', len(adds), '|B| =', total, flush=True)
prob = np.array([float(x) / total for x in w])
def unpack(mask): return np.array([(mask >> k) & 1 for k in range(M)], dtype=bool).reshape(n1, n2)
def sample():
    G = int(nrng.choice(1 << M, p=prob))
    ok = np.nonzero(((G & posm) == 0) & ((~G & negm) == 0))[0]
    sl = [G] + [int((G | posm[t]) & ~negm[t]) for t in nrng.choice(ok, size=n0 - 1)]
    return np.stack([unpack(s) for s in sl])

fails = 0; nonbox = 0
for t in range(NS):
    F = sample()
    if not is_box(F): nonbox += 1
    if not certify(F): fails += 1
print('uniform sample of box sets:', NS, ' not box (sampler bug):', nonbox, ' NOT certified:', fails, ' steps', stats, flush=True)

# ---- targeted: order sets of random interleavings of the labelled values (box sets, the hard family)
def order_set(sizes):
    els = [(c, x) for c in range(3) for x in range(sizes[c])]; rng.shuffle(els)
    pos = {e: i for i, e in enumerate(els)}
    F = np.zeros(sizes, dtype=bool)
    for x in itertools.product(*[range(s) for s in sizes]):
        p = [pos[(i, x[i])] for i in range(3)]
        F[x] = ((p[0] < p[1]) + (p[1] < p[2]) + (p[2] < p[0])) == 2
    return F
stats2 = dict(stats); f2 = 0; NO = min(NS, 20000)
for t in range(NO):
    F = order_set((n0, n1, n2))
    if not is_box(F) or not certify(F): f2 += 1
print('random order sets:', NO, ' NOT certified:', f2, ' new steps', {k: stats[k] - stats2[k] for k in stats}, flush=True)

# ---- negative control: flip one point of a sampled box set; the result is (almost always) not box and must be rejected
rej = 0; acc_nonbox = 0; tried = 0
for t in range(min(NS, 5000)):
    F = sample().copy(); x = tuple(rng.randrange(s) for s in F.shape); F[x] ^= True
    if is_box(F): continue
    tried += 1
    memo.clear()
    if certify(F): acc_nonbox += 1
    else: rej += 1
print('negative control (non-box sets):', tried, ' rejected', rej, ' WRONGLY certified', acc_nonbox)
