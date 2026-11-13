# Independent refutation attempt for FOUR_QUANTITIES_CHECK.md (hostile check, 2026-11-13). Written from scratch.
# Sample K4 pair-sum 0/1 sets at sizes not covered by any enumeration (3x3x4x4, 4x4x4x4, ...) and run the certificate
# procedure on each: merge two values whose slices differ through at most one other coordinate (the merge is verified:
# removed event contained, added event disjoint, slices equal afterwards) until
#   (T) some coordinate has one value (triangle theorem applies), or
#   (I) no merge is possible (irreducible).  The hand proof predicts (I) only on 2x2x2x2, as an image of A4.
# Any other (I) outcome would be a candidate counterexample and is printed.
# Generation (exact characterisation, no enumeration of subsets):
#   triangle pair-sum set on n1 x n2 x n3 = (G_0, G_0+e_1, ...) with G_0 ANY subset of n2 x n3, e_i = h2(x2)+h3(x3);
#   K4 pair-sum set = (F_0, F_0+d_1, ...) with F_0 a triangle pair-sum set, d_i = h1(x1)+h2(x2)+h3(x3).
# The difference lists are enumerated from the normal form c + sum g_j (g_j >= 0 integer, min 0), NOT from T1's shapes.
# Usage: python3 check_random_certificates_3344_4444.py n0 n1 n2 n3 M seed      (n2*n3 <= 16)
import sys, itertools, time, numpy as np
n0, n1, n2, n3 = (int(a) for a in sys.argv[1:5]); M = int(sys.argv[5]); rng = np.random.default_rng(int(sys.argv[6]))
t0 = time.time()

def gfuncs(k):                                   # functions X -> {0,1,2} with minimum 0
    return np.array([g for g in itertools.product(range(3), repeat=k) if min(g) == 0], dtype=np.int8)

def diffs(shape):                                # all c + sum_j g_j(x_j) with values in {-1,0,1}
    gs = [gfuncs(k) for k in shape]; out = None
    tot = gs[0]
    for j in range(1, len(shape)):
        tot = tot.reshape(tot.shape + (1,) * 1)[..., None] if False else tot
    if len(shape) == 2:
        tot = gs[0][:, None, :, None] + gs[1][None, :, None, :]
    else:
        tot = gs[0][:, None, None, :, None, None] + gs[1][None, :, None, None, :, None] + gs[2][None, None, :, None, None, :]
    tot = tot.reshape(-1, int(np.prod(shape)))
    res = []
    for c in (-1, 0, 1):
        d = tot + c; res.append(d[(d.min(1) >= -1) & (d.max(1) <= 1)])
    return np.unique(np.concatenate(res), axis=0)

def masks(D):                                    # positive and negative parts as integer bitmasks
    w = (np.uint64(1) << np.arange(D.shape[1], dtype=np.uint64))
    return ((D == 1).astype(np.uint64) * w).sum(1), ((D == -1).astype(np.uint64) * w).sum(1)

# ---- triangle pair-sum sets on n1 x n2 x n3, sampled uniformly
N2 = n2 * n3; E2 = diffs((n2, n3)); p2, m2 = masks(E2)
G0 = np.arange(1 << N2, dtype=np.uint64)
adm2 = ((G0[:, None] & p2[None, :]) == 0) & ((G0[:, None] & m2[None, :]) == m2[None, :])     # (2^N2, |E2|)
cnt2 = adm2.sum(1).astype(object); wts = np.array([int(c) ** (n1 - 1) for c in cnt2], dtype=object)
Ttot = int(wts.sum())
print('sizes', (n0, n1, n2, n3), '| 2D differences', len(E2), '| triangle pair-sum sets on %dx%dx%d: %d' % (n1, n2, n3, Ttot), flush=True)
pw = np.array([float(x) / float(Ttot) for x in wts])
bits2 = ((G0[:, None] >> np.arange(N2, dtype=np.uint64)) & np.uint64(1)).astype(np.int8)
def sample_triangles(m):
    idx = rng.choice(len(G0), size=m, p=pw); out = np.empty((m, n1, N2), np.int8)
    for r, i in enumerate(idx):
        a = np.nonzero(adm2[i])[0]; out[r, 0] = bits2[i]
        for s in range(1, n1): out[r, s] = bits2[i] + E2[rng.choice(a)]
    return out.reshape(m, n1 * N2)

# ---- K4 sets: first slice a uniform triangle set, other slices F_0 + admissible 3D differences
N3 = n1 * N2; E3 = diffs((n1, n2, n3)); print('3D differences', len(E3), flush=True)
E3pos = (E3 == 1); E3neg = (E3 == -1)
zero = int(np.nonzero((E3 == 0).all(1))[0][0])
d4 = E3.reshape(-1, n1, n2, n3)
def dep_one(d):                                  # d depends on at most one coordinate
    r = np.zeros(len(d), bool)
    for keep in range(3):
        oth = tuple(k + 1 for k in range(3) if k != keep); r |= ((d.max(axis=oth) - d.min(axis=oth)) == 0).all(1)
    return r
simple3 = dep_one(d4); print('3D differences: simple', int(simple3.sum()), 'non-simple (K-type)', int((~simple3).sum()), flush=True)

def admissible(F0):                              # indices of 3D differences d with F0 + d in {0,1}
    f = F0.astype(bool)
    return np.nonzero(~(E3pos & f).any(1) & ~(E3neg & ~f).any(1))[0]

# ---- certificate procedure
A4 = np.zeros((2, 2, 2, 2), np.int8)
for p, u, v, t in itertools.product(range(2), repeat=4):
    if (u, v, t) in [(0, 1, 1), (1, 0, 0)] or (p, u, v) in [(0, 0, 0), (1, 1, 1)]: A4[p, u, v, t] = 1
orbit = set()
for perm in itertools.permutations(range(4)):
    q = np.transpose(A4, perm)
    for fl in itertools.product([0, 1], repeat=4):
        r = q
        for ax, f in enumerate(fl):
            if f: r = np.flip(r, axis=ax)
        orbit.add(r.tobytes()); orbit.add((1 - r).tobytes())

def find_merge(F):
    for ax in range(4):
        for a, b in itertools.combinations(range(F.shape[ax]), 2):
            Fa = np.take(F, a, axis=ax); Fb = np.take(F, b, axis=ax); d = Fa - Fb
            for keep in range(3):
                oth = tuple(k for k in range(3) if k != keep)
                if (d.max(axis=oth) == d.min(axis=oth)).all():
                    delta = d.max(axis=oth); sh = [1, 1, 1]; sh[keep] = -1; dl = delta.reshape(sh) + 0 * d
                    assert (Fa[dl == 1] == 1).all() and (Fa[dl == -1] == 0).all()          # contained / disjoint
                    after = np.where(dl == 1, 0, np.where(dl == -1, 1, Fa)); assert (after == Fb).all()
                    return ax, a
    return None

def certify(F):
    top = True; top_irreducible = False
    while True:
        if min(F.shape) == 1: return 'T', F.shape, top_irreducible
        mg = find_merge(F)
        if mg is None:
            if top: top_irreducible = True
            if F.shape == (2, 2, 2, 2) and np.ascontiguousarray(F).tobytes() in orbit: return 'A4', F.shape, top_irreducible
            return 'IRREDUCIBLE-OTHER', F.shape, top_irreducible
        F = np.delete(F, mg[1], axis=mg[0]); top = False

def pairsum_residual(F):                         # float check that 1_F is a sum of six pair functions
    sh = F.shape; P = np.array(list(itertools.product(*[range(k) for k in sh])))
    cols = [((P[:, i] == a) & (P[:, j] == b)).astype(float) for i, j in itertools.combinations(range(4), 2)
            for a in range(sh[i]) for b in range(sh[j])]
    A = np.array(cols).T; y = F.reshape(-1).astype(float); x = np.linalg.lstsq(A, y, rcond=None)[0]
    return float(np.abs(A @ x - y).max())

Tm = sample_triangles(M); adm = [admissible(f) for f in Tm]; c3 = np.array([len(a) for a in adm])
print('admissible 3D differences per uniform triangle set: min %d median %d mean %.1f max %d' % (c3.min(), np.median(c3), c3.mean(), c3.max()),
      '| time %.0fs' % (time.time() - t0), flush=True)
strata = {}
# A: importance-resampled towards uniform on V01 (weight c3^(n0-1)); other slices uniform admissible
lw = (n0 - 1) * np.log(c3.astype(float)); pA = np.exp(lw - lw.max()); pA /= pA.sum()
strata['A approx-uniform'] = [(i, [rng.choice(adm[i]) for _ in range(n0 - 1)]) for i in rng.choice(M, size=M // 2, p=pA)]
# B: all other slices differ from F_0 by distinct nonzero differences (where enough exist)
B = []
for i in np.argsort(-c3)[:M // 2]:
    a = adm[i][adm[i] != zero]
    if len(a) >= n0 - 1: B.append((i, list(rng.choice(a, size=n0 - 1, replace=False))))
strata['B distinct nonzero differences'] = B
# C: all other slices differ from F_0 by distinct non-simple (K-type) differences
C = []
for i in range(M):
    a = adm[i][~simple3[adm[i]]]
    if len(a) >= n0 - 1:
        for _ in range(3): C.append((i, list(rng.choice(a, size=n0 - 1, replace=False))))
strata['C distinct K-type differences from F_0'] = C
bad = []
for name, items in strata.items():
    res = {}; ntop = 0; maxres = 0.0
    for q, (i, ds) in enumerate(items):
        F = np.stack([Tm[i]] + [Tm[i] + E3[k] for k in ds]).reshape(n0, n1, n2, n3)
        assert F.min() >= 0 and F.max() <= 1
        if q < 40: maxres = max(maxres, pairsum_residual(F))
        kind, shape, topirr = certify(F); res[(kind, shape if kind != 'T' else 'one-valued coordinate')] = res.get((kind, shape if kind != 'T' else 'one-valued coordinate'), 0) + 1
        ntop += topirr
        if kind == 'IRREDUCIBLE-OTHER': bad.append(F.copy())
    print('stratum', name, '| sets', len(items), '| irreducible at the sampled size', ntop, '| pair-sum residual (first 40)', '%.1e' % maxres,
          '| endpoints', res, '| time %.0fs' % (time.time() - t0), flush=True)
print('CANDIDATE COUNTEREXAMPLES (irreducible, not an image of A4):', len(bad))
for F in bad[:3]: print(F.shape, F.reshape(-1).tolist())
