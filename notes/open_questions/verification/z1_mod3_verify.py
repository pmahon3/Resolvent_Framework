"""Exact verification of the Z1 mod-3 witness (2026-10-20).
(1) the forced functional is well defined on the span (kills every linear dependency among cell indicators),
(2) exact rational value of the witness, (3) membership of the witness in D (explicit construction trace),
(4) pull back to Z^3 on a box and check that the pulled-back decomposition reproduces the indicator there.
"""
import itertools
from fractions import Fraction as F
n = 3
pts = list(itertools.product(range(n), repeat=3)); N = len(pts); idx = {p: t for t, p in enumerate(pts)}
E3 = [(0, 1), (1, 2), (2, 0)]
cells = [(e, a, b) for e in range(3) for a in range(n) for b in range(n)]
def ind(c):
    e, a, b = c; i, j = E3[e]; return [1 if (p[i] == a and p[j] == b) else 0 for p in pts]
mu = [F(1, n) if ((b == a) if e < 2 else (b == (a + 1) % n)) else F(0) for (e, a, b) in cells]
W = [(0,1,0),(0,2,0),(0,2,1),(1,0,1),(1,0,2),(1,2,1),(2,0,2),(2,1,0),(2,1,2)]
target = [1 if p in W else 0 for p in pts]
# exact solve: augmented system cells^T c = target, plus null space of the cell matrix
A = [[F(ind(c)[t]) for c in cells] + [F(target[t])] for t in range(N)]
rows, piv, r = [row[:] for row in A], [], 0
for col in range(len(cells)):
    p = next((i for i in range(r, N) if rows[i][col] != 0), None)
    if p is None: continue
    rows[r], rows[p] = rows[p], rows[r]; rows[r] = [x / rows[r][col] for x in rows[r]]
    for i in range(N):
        if i != r and rows[i][col] != 0: rows[i] = [a - rows[i][col] * b for a, b in zip(rows[i], rows[r])]
    piv.append(col); r += 1
assert all(all(x == 0 for x in rows[i]) for i in range(r, N)), "target not in span"
c = [F(0)] * len(cells)
for i, col in enumerate(piv): c[col] = rows[i][-1]
assert all(sum(c[k] * ind(cells[k])[t] for k in range(len(cells))) == target[t] for t in range(N))
free = [k for k in range(len(cells)) if k not in piv]
for fcol in free:  # null vector: set free=1, pivots = -rows[i][fcol]
    v = [F(0)] * len(cells); v[fcol] = F(1)
    for i, col in enumerate(piv): v[col] = -rows[i][fcol]
    assert sum(v[k] * mu[k] for k in range(len(cells))) == 0, "functional not well defined"
val = sum(c[k] * mu[k] for k in range(len(cells)))
print("well defined on span: yes (", len(free), "null directions killed); exact value:", val)
# (3) membership: closure with parent pointers, then print a construction depth
full = (1 << N) - 1
gens = {}
for e in range(3):
    i, j = E3[e]
    for S in range(1 << 9):
        m = sum(1 << t for t, p in enumerate(pts) if S >> (p[i] * 3 + p[j]) & 1); gens.setdefault(m, ("gen", e, S))
D = dict(gens); D.setdefault(0, ("empty",)); D.setdefault(full, ("full",)); fr = list(D)
while fr:
    new = {}; L = list(D)
    for a in fr:
        if (full ^ a) not in D and (full ^ a) not in new: new[full ^ a] = ("compl", a)
        for b in L:
            if a & b == 0 and (a | b) not in D and (a | b) not in new: new[a | b] = ("union", a, b)
    D.update(new); fr = list(new)
wm = sum(1 << idx[p] for p in W)
def depth(m, seen={}):
    if m in seen: return seen[m]
    s = D[m]; d = 0 if s[0] in ("gen", "empty", "full") else 1 + max(depth(x) for x in s[1:])
    seen[m] = d; return d
print("witness in D:", wm in D, "| construction:", D[wm][0], "| depth:", depth(wm))
# (4) pull back to Z^3 on a box: decomposition with residues reproduces the indicator
ok = all(sum(c[k] * ind(cells[k])[idx[(x0 % 3, x1 % 3, x2 % 3)]] for k in range(len(cells))) ==
         (1 if (x0 % 3, x1 % 3, x2 % 3) in W else 0) for x0 in range(-4, 5) for x1 in range(-4, 5) for x2 in range(-4, 5))
print("pull-back decomposition consistent on [-4,4]^3:", ok)
