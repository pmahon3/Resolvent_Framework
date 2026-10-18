"""Is the circle's cyclic set buildable on the finite triangle board? (2026-10-18, gate.finite_staircase_carrier)
Cyc_A = {d01' + d12 + d20 = A}, with d01' = (x1-x0) mod A in 1..A and d12, d20 mod A in 0..A-1. It is a 0/1 sum
of window functions; under F_A (x_{k+1} = x_k + 1 mod A) its forced value is 2 - 3/A.
Certified search: from the empty set, moves are 'add a window cell disjoint from X', 'remove a window cell
contained in X' (a proper difference of buildable sets) and 'complement'. Every reached set is buildable.
Beam search toward Cyc_A or its complement. A hit is a construction certificate; a miss is inconclusive.
"""
import itertools, sys, time
A = int(sys.argv[1]) if len(sys.argv) > 1 else 4
BEAM = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
pts = list(itertools.product(range(A), repeat=3)); ix = {p: i for i, p in enumerate(pts)}; full = (1 << len(pts)) - 1
def mask(pred): return sum(1 << ix[p] for p in pts if pred(p))
def d01p(p): d = (p[1] - p[0]) % A; return d if d else A
cyc = mask(lambda p: d01p(p) + (p[2] - p[1]) % A + (p[0] - p[2]) % A == A)
W = [(0, 1), (1, 2), (2, 0)]
cells = [mask(lambda p, i=i, j=j, a=a, b=b: p[i] == a and p[j] == b) for (i, j) in W for a in range(A) for b in range(A)]
pc = lambda m: bin(m).count('1')
def h(m): return min(pc(m ^ cyc), pc(m ^ (full ^ cyc)))
parent = {0: None}; frontier = [0]; t0 = time.time()
for depth in range(200):
    cand = set()
    for X in frontier:
        nxt = [full ^ X] + [X | c for c in cells if X & c == 0] + [X ^ c for c in cells if X & c == c]
        for Y in nxt:
            if Y not in parent: parent[Y] = X; cand.add(Y)
    if not cand: print("exhausted"); break
    if cyc in parent or (full ^ cyc) in parent:
        hit = cyc if cyc in parent else full ^ cyc
        path = []; y = hit
        while y is not None: path.append(y); y = parent[y]
        print(f"A={A}: Cyc_A {'reached' if hit == cyc else 'complement reached'} at depth {depth+1} "
              f"(certified construction, {len(path)-1} moves); |Cyc_A| = {pc(cyc)}"); break
    frontier = sorted(cand, key=h)[:BEAM]
    if depth % 10 == 0: print(f"  depth {depth}: best distance {h(frontier[0])}, explored {len(parent)}, {time.time()-t0:.0f}s", flush=True)
else:
    print(f"A={A}: not reached within depth bound (inconclusive)")

