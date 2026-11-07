# Independent checks for TRIANGLE_GATE_ATTEMPT.md §3b (2026-11-07, checker script).
# (A) worked case: Ω∖(A ⊔ K(S)) = W'01 ⊔ (W01∖A) ⊔ K(S0,S1,S2^c), random grids/instances.
# (B) normal form at finite grid n: R1 (= disjoint-union closure of R0 ∪ co-R0) equals
#     N = {R ⊔ K1 ⊔ ... ⊔ Kj : R ∈ R0, j ≤ 3, Ki nondegenerate antipodal pairs, all disjoint}.
#     Also reports the least j that suffices for every R1 set.
import itertools, random, sys, numpy as np

def worked_case(trials=2000, seed=1):
    rng = random.Random(seed); bad = 0
    for _ in range(trials):
        n = [rng.randint(2, 5) for _ in range(3)]
        S = []
        for k in n:
            s = set(c for c in range(k) if rng.random() < .5)
            if not s: s = {0}
            if len(s) == k: s.discard(k - 1)
            S.append(s)
        pts = list(itertools.product(*[range(k) for k in n]))
        b = lambda p, i: p[i] in S[i]
        Kset = lambda T: {p for p in pts if all(p[i] in T[i] for i in range(3)) or all(p[i] not in T[i] for i in range(3))}
        W01cells = [(a, c) for a in range(n[0]) for c in range(n[1]) if a not in S[0] and c in S[1]]
        Acells = {cl for cl in W01cells if rng.random() < .5}
        A = {p for p in pts if (p[0], p[1]) in Acells}
        KS = Kset(S)
        lhs = set(pts) - (A | KS)
        Wp = {p for p in pts if b(p, 0) and not b(p, 1)}
        W01mA = {p for p in pts if (not b(p, 0)) and b(p, 1) and (p[0], p[1]) not in Acells}
        K2 = Kset([S[0], S[1], set(range(n[2])) - S[2]])
        rhs = Wp | W01mA | K2
        disj = not (Wp & W01mA) and not (Wp & K2) and not (W01mA & K2) and not (A & KS)
        if lhs != rhs or not disj: bad += 1
    print('(A) worked case: trials', trials, 'failures', bad)

def normal_form(n):
    pts = list(itertools.product(*[range(k) for k in n])); idx = {p: i for i, p in enumerate(pts)}
    N = len(pts); FULL = (1 << N) - 1
    mask = lambda pred: sum(1 << idx[p] for p in pts if pred(p))
    def win(i, j):
        vals = list(itertools.product(range(n[i]), range(n[j]))); out = set()
        for m in range(1 << len(vals)):
            S = {vals[k] for k in range(len(vals)) if m >> k & 1}
            out.add(mask(lambda p: (p[i], p[j]) in S))
        return sorted(out)
    W01, W12, W20 = win(0, 1), win(1, 2), win(2, 0)
    # R0 directly as A ⊔ B ⊔ C (one event per window, pairwise disjoint) -- independent of Uclose
    R0 = set()
    B12 = np.array(W12, dtype=np.uint64); C20 = np.array(W20, dtype=np.uint64)
    for a in W01:
        a = np.uint64(a); bs = B12[(B12 & a) == 0]
        for bb in bs:
            ab = a | bb; cs = C20[(C20 & ab) == 0]
            R0.update((cs | ab).tolist())
    props = [[frozenset(c for c in range(k) if m >> c & 1) for m in range(1, (1 << k) - 1)] for k in n]
    Ks = sorted({mask(lambda p, S=S: all(p[i] in S[i] for i in range(3)) or all(p[i] not in S[i] for i in range(3)))
                 for S in itertools.product(*props)})
    # disjoint unions of j<=3 pairwise-disjoint nondegenerate pairs; record least j
    P = {0: 0}
    for j in range(1, 4):
        for x, jj in list(P.items()):
            if jj != j - 1: continue
            for k in Ks:
                if k & x == 0 and (x | k) not in P: P[x | k] = j
    R0a = np.array(sorted(R0), dtype=np.uint64)
    Nf = {}
    for x, j in P.items():
        for u in (R0a[(R0a & np.uint64(x)) == 0] | np.uint64(x)).tolist():
            if u not in Nf or Nf[u] > j: Nf[u] = j
    # R1 via disjoint-union closure of R0 ∪ co-R0 (same method as kform.py)
    def Uclose(X):
        S = set(X); fr = set(X)
        while fr:
            D = np.array(sorted(S), dtype=np.uint64); new = set()
            for x in fr:
                ys = D[(D & np.uint64(x)) == 0]
                for u in (ys | np.uint64(x)).tolist():
                    if u not in S: new.add(u)
            S |= new; fr = new
        return S
    R1 = Uclose(R0 | {m ^ FULL for m in R0})
    from collections import Counter
    print('(B)', n, '|R0|', len(R0), '|nondeg K|', len(Ks), '|N|', len(Nf), '|R1|', len(R1),
          'N==R1:', set(Nf) == R1, 'least-j histogram', sorted(Counter(Nf.values()).items()), flush=True)
    return pts, FULL, R1

if __name__ == '__main__':
    worked_case()
    for arg in sys.argv[1:]:
        normal_form(tuple(int(c) for c in arg.split('x')))
