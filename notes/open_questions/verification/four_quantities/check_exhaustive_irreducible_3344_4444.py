# Independent exhaustive check for FOUR_QUANTITIES_CHECK.md (hostile check, 2026-11-13). Written from scratch.
# For a K4 grid n0 x n1 x n2 x n3 (n2*n3 <= 16, n1*n2*n3 <= 64): enumerate ALL pair-sum 0/1 sets by slices along
# coordinate 0 and count the IRREDUCIBLE ones (no coordinate has two values whose slice difference depends on at most
# one other coordinate).  The hand proof predicts 0 unless the size is 2x2x2x2.
#   triangle pair-sum set on n1 x n2 x n3 = (G_0, G_0+e_1, ...), G_0 any subset of n2 x n3, e_i = h2(x2)+h3(x3);
#   K4 pair-sum set = (F_0, F_0+d_1, ...), F_0 a triangle pair-sum set, d_i = h1(x1)+h2(x2)+h3(x3), values in {-1,0,1}.
# Differences are enumerated from the normal form c + sum g_j (g_j >= 0 integer, min 0): T1's shape list is not used.
# A set with two equal slices at coordinate 0 is reducible by definition (difference 0), so only tuples of DISTINCT
# NONZERO differences are tested, each unordered tuple once (reducibility does not depend on the order of the values).
# |V01| = sum over F_0 of c(F_0)^(n0-1) is reported as a count.
# Usage: python3 check_exhaustive_irreducible_3344_4444.py n0 n1 n2 n3
import sys, itertools, time, math, numpy as np
n0, n1, n2, n3 = (int(a) for a in sys.argv[1:5]); t0 = time.time()
N2 = n2 * n3; N3 = n1 * N2; assert N2 <= 16 and N3 <= 64

def gfuncs(k): return np.array([g for g in itertools.product(range(3), repeat=k) if min(g) == 0], dtype=np.int8)
def diffs(shape):
    gs = [gfuncs(k) for k in shape]
    if len(shape) == 2: tot = gs[0][:, None, :, None] + gs[1][None, :, None, :]
    else: tot = gs[0][:, None, None, :, None, None] + gs[1][None, :, None, None, :, None] + gs[2][None, None, :, None, None, :]
    tot = tot.reshape(-1, int(np.prod(shape))); res = []
    for c in (-1, 0, 1):
        d = tot + c; res.append(d[(d.min(1) >= -1) & (d.max(1) <= 1)])
    return np.unique(np.concatenate(res), axis=0)
def masks(D):
    w = (np.uint64(1) << np.arange(D.shape[1], dtype=np.uint64))
    return ((D == 1).astype(np.uint64) * w).sum(1), ((D == -1).astype(np.uint64) * w).sum(1)

# ---- all triangle pair-sum sets on n1 x n2 x n3 as bitmasks (slice s occupies bits s*N2 .. s*N2+N2-1)
E2 = diffs((n2, n3)); p2, m2 = masks(E2); G0 = np.arange(1 << N2, dtype=np.uint64)
adm2 = ((G0[:, None] & p2[None, :]) == 0) & ((G0[:, None] & m2[None, :]) == m2[None, :])
tri = []
for g in range(1 << N2):
    a = np.nonzero(adm2[g])[0]; sl = (np.uint64(g) & ~m2[a]) | p2[a]                 # the admissible other slices
    acc = np.array([g], dtype=np.uint64)
    for s in range(1, n1): acc = (acc[:, None] | (sl[None, :] << np.uint64(s * N2))).reshape(-1)
    tri.append(acc)
tri = np.concatenate(tri); print('sizes', (n0, n1, n2, n3), '| triangle pair-sum sets on %dx%dx%d:' % (n1, n2, n3), len(tri),
                                 '(distinct: %s)' % (len(np.unique(tri)) == len(tri)), '| time %.0fs' % (time.time() - t0), flush=True)
# ---- admissible 3D differences for every triangle set
E3 = diffs((n1, n2, n3)); p3, m3 = masks(E3); zero = int(np.nonzero((E3 == 0).all(1))[0][0])
FULL = np.uint64((1 << N3) - 1) if N3 < 64 else np.uint64(0xFFFFFFFFFFFFFFFF)
cnt = np.empty(len(tri), np.int64); rich = []                                         # rich: (triangle mask, admissible nonzero indices)
CH = 30000
for s in range(0, len(tri), CH):
    f = tri[s:s + CH]; ad = ((f[:, None] & p3[None, :]) == 0) & (((~f & FULL)[:, None] & m3[None, :]) == 0)
    ad[:, zero] = True; c = ad.sum(1); cnt[s:s + CH] = c
    for r in np.nonzero(c >= n0)[0]:                                                 # at least n0-1 distinct nonzero differences
        a = np.nonzero(ad[r])[0]; rich.append((f[r], a[a != zero]))
V01 = sum(int(c) ** (n0 - 1) for c in cnt)
ntup = sum(math.comb(len(a), n0 - 1) for _, a in rich)
print('3D differences', len(E3), '| |V01| =', V01, '| triangle sets with >= %d nonzero admissible differences: %d' % (n0 - 1, len(rich)),
      '| unordered tuples of distinct nonzero differences to test:', ntup, '| time %.0fs' % (time.time() - t0), flush=True)
if ntup > 4e8: sys.exit('too many tuples for this machine; not run')

def reducible(S):                                # S: (m, n0, n1, n2, n3) int8
    m = len(S); red = np.zeros(m, bool)
    for ax in range(4):
        for a, b in itertools.combinations(range(S.shape[ax + 1]), 2):
            d = np.take(S, a, axis=ax + 1) - np.take(S, b, axis=ax + 1)
            for keep in range(3):
                oth = tuple(k + 1 for k in range(3) if k != keep)
                red |= ((d.max(axis=oth) - d.min(axis=oth)) == 0).all(1)
    return red
bitsN = np.arange(N3, dtype=np.uint64); E3i = E3.astype(np.int8)
buf = []; nbuf = 0; tested = 0; nirr = 0; examples = []
def flush():
    global buf, nbuf, tested, nirr
    if not buf: return
    S = np.concatenate(buf).reshape((-1, n0, n1, n2, n3)); assert S.min() >= 0 and S.max() <= 1
    red = reducible(S); tested += len(S); nirr += int((~red).sum())
    if (~red).any() and len(examples) < 3: examples.extend(S[~red][:3])
    buf = []; nbuf = 0
for fm, a in rich:
    F0 = ((fm >> bitsN) & np.uint64(1)).astype(np.int8)
    combos = np.array(list(itertools.combinations(a.tolist(), n0 - 1)), dtype=np.int64)          # (q, n0-1)
    for s in range(0, len(combos), 50000):
        cb = combos[s:s + 50000]
        S = np.concatenate([np.broadcast_to(F0, (len(cb), 1, N3)), F0[None, None, :] + E3i[cb]], axis=1)
        buf.append(S.astype(np.int8)); nbuf += len(S)
        if nbuf > 100000: flush()
flush()
print('RESULT', (n0, n1, n2, n3), '| |V01| =', V01, '| tested (distinct slices at coordinate 0)', tested, '| IRREDUCIBLE:', nirr,
      '| time %.0fs' % (time.time() - t0))
for F in examples: print(' irreducible example:', F.reshape(-1).tolist())
