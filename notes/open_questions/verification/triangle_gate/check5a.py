# Checker for §5a analogues on grids n0 x n1 x n2 (2026-11-07).
# N1 = {R ⊔ K : R ∈ R0, K empty or one nondegenerate antipodal pair, disjoint}.
# (i) N1 is closed under disjoint union (tested on every disjoint pair K, K' of nondegenerate pairs:
#     K ⊔ K' ∈ N1 suffices, since R0 is closed under disjoint unions) and contains R0 ∪ co-R0, so N1 = R1 = D¹-form.
# (ii) M = co-N1 ∖ N1 = the sets that need a complement of a D¹ set (first members of D² ∖ D¹).
# (iii) Is every M-set a "cyclic-order set": for some interleaving (strict linear order) of the labelled values
#      X0 ⊔ X1 ⊔ X2, M = {x : (x0, x1, x2) is positively cyclically ordered}?  And which cyclic-order sets are in M?
import itertools, sys, numpy as np
from collections import Counter
n = tuple(int(a) for a in sys.argv[1:4])
pts = list(itertools.product(*[range(k) for k in n])); idx = {p: i for i, p in enumerate(pts)}
N = len(pts); FULL = (1 << N) - 1
mask = lambda pred: sum(1 << idx[p] for p in pts if pred(p))
def win(i, j):
    vals = list(itertools.product(range(n[i]), range(n[j]))); cell = {}
    for p in pts: cell.setdefault((p[i], p[j]), 0); cell[(p[i], p[j])] |= 1 << idx[p]
    cm = [cell[v] for v in vals]; out = []
    for m in range(1 << len(vals)):
        out.append(sum(cm[k] for k in range(len(vals)) if m >> k & 1))
    return sorted(set(out))
W01, W12, W20 = win(0, 1), win(1, 2), win(2, 0)
R0 = set(); B12 = np.array(W12, dtype=np.uint64); C20 = np.array(W20, dtype=np.uint64)
for a in W01:
    a = np.uint64(a)
    for bb in B12[(B12 & a) == 0]:
        ab = a | bb; R0.update((C20[(C20 & ab) == 0] | ab).tolist())
print('|R0|', len(R0), flush=True)
props = [[frozenset(c for c in range(k) if m >> c & 1) for m in range(1, (1 << k) - 1)] for k in n]
Ks = sorted({mask(lambda p, S=S: all(p[i] in S[i] for i in range(3)) or all(p[i] not in S[i] for i in range(3)))
             for S in itertools.product(*props)})
R0a = np.array(sorted(R0), dtype=np.uint64)
N1 = set(R0)
for k in Ks: N1.update((R0a[(R0a & np.uint64(k)) == 0] | np.uint64(k)).tolist())
print('|nondeg K|', len(Ks), '|N1|', len(N1), flush=True)
coR0_ok = all((m ^ FULL) in N1 for m in R0)
pair_bad = sum(1 for a, b in itertools.combinations(Ks, 2) if a & b == 0 and (a | b) not in N1)
print('(i) co-R0 ⊆ N1:', coR0_ok, ' disjoint K⊔K\' not in N1:', pair_bad, flush=True)
M = {m ^ FULL for m in N1} - N1
print('(ii) |M| = |co-N1 \\ N1|', len(M), ' point-count histogram', sorted(Counter(bin(m).count('1') for m in M).items()), flush=True)
# (ii') is N1 ∪ M a Dynkin system (complements + disjoint unions)?  If yes, D3(grid) = N1 ∪ M, i.e. round 2 = closure.
U = np.array(sorted(N1 | M), dtype=np.uint64); allset = N1 | M
comp_ok = all((m ^ FULL) in allset for m in allset)
du_bad = 0
for m in M:
    for u in (U[(U & np.uint64(m)) == 0] | np.uint64(m)).tolist():
        if u not in allset: du_bad += 1
print("(ii') N1∪M closed under complement:", comp_ok, ' disjoint unions M⊔(N1∪M) outside:', du_bad, ' |N1∪M|', len(allset), flush=True)
if len(sys.argv) > 4 and sys.argv[4] == 'nocyc': sys.exit()
# (iii) cyclic-order sets over all interleavings; label order of values within each coordinate is free.
labels = [(i, v) for i in range(3) for v in range(n[i])]
C = Counter(); cyc = set()
P = np.array(pts)
for perm in itertools.permutations(range(len(labels))):
    rank = {labels[t]: perm[t] for t in range(len(labels))}
    y = np.array([[rank[(0, p[0])], rank[(1, p[1])], rank[(2, p[2])]] for p in pts]) if False else None
    r0 = np.array([rank[(0, v)] for v in range(n[0])]); r1 = np.array([rank[(1, v)] for v in range(n[1])])
    r2 = np.array([rank[(2, v)] for v in range(n[2])])
    a, b, c = r0[P[:, 0]], r1[P[:, 1]], r2[P[:, 2]]
    pos = ((a < b) & (b < c)) | ((b < c) & (c < a)) | ((c < a) & (a < b))
    cyc.add(int((pos.astype(np.uint64) << np.arange(N, dtype=np.uint64)).sum()))
print('(iii) distinct cyclic-order sets', len(cyc), ' M ⊆ cyc:', M <= cyc, ' |M ∩ cyc|', len(M & cyc),
      ' cyc ∩ N1', len(cyc & N1), ' cyc outside N1 ∪ M', len(cyc - N1 - M), flush=True)
