"""Z1 visibility via the mod-n quotient (2026-10-20). Triangle over Z_n (n = 3), views x1 = x0, x2 = x1,
x0 = x2 + 1 (mod n), each uniform. This is the push-forward of the clock state on Z under s -> s mod n
(transport lemma). Find a buildable set (in D over Z_n^3) with negative forced value; its preimage under
mod n is buildable over Z with the same (negative) value. Exact: rational RREF for the span, explicit
Dynkin closure for membership of the witness.
"""
import itertools
from fractions import Fraction
import sys; n = int(sys.argv[1]); st = tuple(map(int, sys.argv[2].split(",")))
pts = list(itertools.product(range(n), repeat=3)); N = len(pts); full = (1 << N) - 1
E3 = [(0, 1), (1, 2), (2, 0)]
cells = [(e, a, b) for e in range(3) for a in range(n) for b in range(n)]
def cellmask(e, a, b):
    i, j = E3[e]; return sum(1 << t for t, p in enumerate(pts) if p[i] == a and p[j] == b)
# forced view laws: mass 1/n on (s,s), (s,s), and for view (2,0): (x2, x0) = (s, s+1)
mu = {}
for (e, a, b) in cells:
    if e < 2: mu[(e, a, b)] = Fraction(1, n) if b == (a + st[e]) % n else Fraction(0)
    else: mu[(e, a, b)] = Fraction(1, n) if b == (a + st[2]) % n else Fraction(0)
# Dynkin closure D (masks)
gens = set()
for e in range(3):
    i, j = E3[e]
    for S in range(1 << (n * n)):
        gens.add(sum(1 << t for t, p in enumerate(pts) if S >> (p[i] * n + p[j]) & 1))
D = gens | {0, full}; fr = list(D)
while fr:
    new = set(); L = list(D)
    for a in fr:
        if full ^ a not in D: new.add(full ^ a)
        for b in L:
            if a & b == 0 and (a | b) not in D: new.add(a | b)
    D |= new; fr = list(new)
print("|D| =", len(D))
# forced functional: solve 1_E = sum c_cell 1_cell exactly, value = sum c mu
rows = [[(cellmask(*c) >> t) & 1 for t in range(N)] for c in cells]  # cells x points
import numpy as np
M = np.array(rows, float).T  # points x cells
best = None
for m in D:
    f = np.array([(m >> t) & 1 for t in range(N)], float)
    c = np.linalg.lstsq(M, f, rcond=None)[0]; assert np.allclose(M @ c, f)
    val = sum(Fraction(round(ci * 9)) / 9 * mu[cells[k]] for k, ci in enumerate(c)) if False else None
    v = float(sum(ci * float(mu[cells[k]]) for k, ci in enumerate(c)))
    if best is None or v < best[0] - 1e-9: best = (v, m)
v, m = best
print("min forced value on D:", round(v, 6))
print("witness points (x0,x1,x2):", [pts[t] for t in range(N) if m >> t & 1])
