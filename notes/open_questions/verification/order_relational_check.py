"""gate.order_relational (2026-10-20). Relational carrier for order: on the 13 weak orders of (x0,x1,x2),
the Dynkin closure R_ord of pairwise comparison events. Family: no ties, P(x0<x1)=P(x1<x2)=P(x2<x0)=q.
Is the forced comparison functional a state on R_ord when q > 2/3 (no random ranking)?
Exact rationals.
"""
import itertools
from fractions import Fraction as F
W = sorted({tuple(sorted(set(r)).index(x) for x in r) for r in itertools.product(range(3), repeat=3)})
assert len(W) == 13
N = len(W); full = (1 << N) - 1
P3 = [(0, 1), (1, 2), (2, 0)]
def cmp(a, b): return 0 if a < b else (1 if a == b else 2)       # 0:<, 1:=, 2:>
cells = [(k, o) for k in range(3) for o in range(3)]
def cell(k, o): i, j = P3[k]; return sum(1 << t for t, w in enumerate(W) if cmp(w[i], w[j]) == o)
gens = {sum(cell(k, o) for o in range(3) if S >> o & 1) for k in range(3) for S in range(8)}
D = gens | {0, full}; fr = list(D)
while fr:
    new = set(); L = list(D)
    for a in fr:
        if full ^ a not in D: new.add(full ^ a)
        for b in L:
            if a & b == 0 and (a | b) not in D: new.add(a | b)
    D |= new; fr = list(new)
print("|R_ord| =", len(D), "of", 2 ** N, "subsets")
# exact linear algebra: express each set in span of the 9 cells
M = [[F((cell(*c) >> t) & 1) for c in cells] for t in range(N)]
def solve(target):
    A = [M[t][:] + [F(target[t])] for t in range(N)]; piv = []; r = 0
    for col in range(9):
        p = next((i for i in range(r, N) if A[i][col] != 0), None)
        if p is None: continue
        A[r], A[p] = A[p], A[r]; A[r] = [x / A[r][col] for x in A[r]]
        for i in range(N):
            if i != r and A[i][col] != 0: A[i] = [a - A[i][col] * b for a, b in zip(A[i], A[r])]
        piv.append(col); r += 1
    if any(A[i][-1] != 0 for i in range(r, N)): return None, None
    c = [F(0)] * 9
    for i, col in enumerate(piv): c[col] = A[i][-1]
    nulls = []
    for fcol in [k for k in range(9) if k not in piv]:
        v = [F(0)] * 9; v[fcol] = F(1)
        for i, col in enumerate(piv): v[col] = -A[i][fcol]
        nulls.append(v)
    return c, nulls
def mu(q): return [q if o == 0 else (F(0) if o == 1 else 1 - q) for (k, o) in cells]
_, nulls = solve([0] * N)
for q in [F(2, 3), F(3, 4), F(9, 10), F(1)]:
    m = mu(q); assert all(sum(v[i] * m[i] for i in range(9)) == 0 for v in nulls)
    worst = min((sum(c[i] * m[i] for i in range(9)), s) for s in D for c in [solve([(s >> t) & 1 for t in range(N)])[0]])
    pts = [W[t] for t in range(N) if worst[1] >> t & 1]
    print(f"q = {q}: min forced value on R_ord = {worst[0]}  witness (ranks) = {pts}")
