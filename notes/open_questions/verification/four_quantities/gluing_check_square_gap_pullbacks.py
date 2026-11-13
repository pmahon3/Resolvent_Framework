# Independent check (2026-11-13, GLUING_LEMMA_CHECK.md item 6). Are the 72 gap sets of the square C4 at (2,2,3,3)
# and (2,3,2,3) exactly the pullbacks of the 8 gap sets of C4(2) along coordinatewise maps merging values?
# Gap sets are read from the .npy files saved by gluing_check_exact_D_vs_V01_any_shape.py (bitmask over
# itertools.product order). The 8 two-valued gap sets are recomputed here by brute force closure.
import itertools, numpy as np
def closure_gap_2222():
    pts = list(itertools.product(range(2), repeat=4)); N = 16; E = [(0, 1), (1, 2), (2, 3), (0, 3)]
    gens = set()
    for (i, j) in E:
        cells = [sum(1 << k for k, p in enumerate(pts) if (p[i], p[j]) == ab) for ab in itertools.product(range(2), repeat=2)]
        for m in range(16): gens.add(sum(c for k, c in enumerate(cells) if m >> k & 1))
    D = set(gens)
    while True:
        new = {65535 ^ x for x in D} | {x | y for x in D for y in D if x & y == 0}
        if new <= D: break
        D |= new
    # V01 by brute force over all 65536 subsets: in the span iff orthogonal to its orthogonal complement
    cols = [[1 if (p[i], p[j]) == ab else 0 for p in pts] for (i, j) in E for ab in itertools.product(range(2), repeat=2)]
    A = np.array(cols, dtype=float).T
    U, S, _ = np.linalg.svd(A); r = int((S > 1e-9).sum()); K = U[:, r:]          # orthogonal complement (16x16, tiny)
    V = {x for x in range(1 << 16) if np.abs(np.array([(x >> k) & 1 for k in range(16)], float) @ K).max() < 1e-9}
    assert D <= V
    return pts, sorted(V - D)
pts2, gap2 = closure_gap_2222(); print('C4(2): gap sets', len(gap2))
for n, fn in [((2, 2, 3, 3), 'gluing_check_gap_square_2233.npy'), ((2, 3, 2, 3), 'gluing_check_gap_square_2323.npy')]:
    pts = list(itertools.product(*[range(k) for k in n])); gap = set(int(z) for z in np.load(fn))
    maps = [[m for m in itertools.product(range(2), repeat=k) if len(set(m)) == 2] for k in n]   # surjections onto {0,1}
    pull = set()
    for g in gap2:
        S = {p for k, p in enumerate(pts2) if g >> k & 1}
        for ms in itertools.product(*maps):
            pull.add(sum(1 << k for k, p in enumerate(pts) if tuple(ms[i][p[i]] for i in range(4)) in S))
    print(n, 'gap sets', len(gap), 'distinct pullbacks of the 8', len(pull), 'pullbacks that are gap sets', len(pull & gap),
          'gap sets that are not pullbacks', len(gap - pull))
