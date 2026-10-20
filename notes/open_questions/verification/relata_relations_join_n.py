"""Critical test of the relations/relata partition (2026-10-20). Clock core Z1 reduced mod 2:
x1 = x0, x2 = x1, x0 = x2 + 1 (mod 2), each clock uniform. Three question algebras on Z_2^3:
  R  = relations only: Dynkin closure of single-difference events (parity of x1-x0, x2-x1, x0-x2)
  S  = relata only:    Dynkin closure of single-clock events (parity of x0, x1, x2 each alone)
  J  = Dynkin closure of R u S (both kinds of question, combined only by 'not' and 'either one')
  F  = full triangle carrier (all pair events)
For each: min forced value. Hidden = min >= 0. Exact rationals.
"""
import itertools
from fractions import Fraction as Fr
import sys; n = int(sys.argv[1])
pts = list(itertools.product(range(n), repeat=3)); N = len(pts); full = (1 << N) - 1
def mask(pred): return sum(1 << t for t, p in enumerate(pts) if pred(p))
def closure(gens):
    D = set(gens) | {0, full}; fr = list(D)
    while fr:
        new = set(); L = list(D)
        for a in fr:
            if full ^ a not in D: new.add(full ^ a)
            for b in L:
                if a & b == 0 and (a | b) not in D: new.add(a | b)
        D |= new; fr = list(new)
    return D
diffs = [lambda p: (p[1] - p[0]) % n, lambda p: (p[2] - p[1]) % n, lambda p: (p[0] - p[2]) % n]
R = closure({mask(lambda p, f=f, v=v: f(p) == v) for f in diffs for v in range(n)})
S = closure({mask(lambda p, i=i, v=v: p[i] == v) for i in range(3) for v in range(n)})
J = closure(R | S)
E3 = [(0, 1), (1, 2), (2, 0)]
F = closure({mask(lambda p, i=i, j=j, a=a, b=b: p[i] == a and p[j] == b) for (i, j) in E3 for a in range(n) for b in range(n)})
# forced functional: pair-cell laws (x1=x0, x2=x1, x0=x2+1), uniform
cells = [(k, a, b) for k in range(3) for a in range(n) for b in range(n)]
mu = [Fr(1, n) if ((b == a) if k < 2 else (b == (a + 1) % n)) else Fr(0) for (k, a, b) in cells]
import numpy as np
M = np.array([[1.0 if (p[E3[k][0]] == a and p[E3[k][1]] == b) else 0.0 for (k, a, b) in cells] for p in pts])
def val(m):
    f = np.array([(m >> t) & 1 for t in range(N)], float)
    c = np.linalg.lstsq(M, f, rcond=None)[0]; assert np.allclose(M @ c, f)
    return float(sum(ci * float(mu[k]) for k, ci in enumerate(c)))
for name, A in [("R relations", R), ("S relata", S), ("J closure(R u S)", J), ("F full", F)]:
    v, m = min((val(m), m) for m in A)
    print(f"{name:18s} |A| = {len(A):4d}  min forced value = {v:+.3f}  witness = {[pts[t] for t in range(N) if m >> t & 1]}")
print("J == F:", J == F, "| R subset J:", R <= J, "| S subset J:", S <= J)
