"""gate.finite_chordal_line (i), 2026-10-18. Triangle over {0,1,2}, where D = 0/1 elements of the span V
(machine count 15,914). Every gauge family: x1 = s0(x0), x2 = s1(x1), x0 = s2(x2) with permutations s_k
and uniform slots. Its monodromy is m = s2.s1.s0, and a joint picture exists iff m = id. Exact MILP: min of
the forced functional Lambda over 0/1 elements of V (= D at A=3). Expect min < 0 iff m != id.
"""
import itertools
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix
A = 3
pts = list(itertools.product(range(A), repeat=3)); ix = {p: i for i, p in enumerate(pts)}; n = len(pts)
W = [(0, 1), (1, 2), (2, 0)]
pr = list(itertools.combinations(range(A), 2))
B = lil_matrix((len(pr) ** 3, n)); r = 0
for (a, a2), (b, b2), (c, c2) in itertools.product(pr, repeat=3):
    for (x0, s0), (x1, s1), (x2, s2) in itertools.product(((a, 1), (a2, -1)), ((b, 1), (b2, -1)), ((c, 1), (c2, -1))):
        B[r, ix[(x0, x1, x2)]] += s0 * s1 * s2
    r += 1
cons = LinearConstraint(B.tocsr(), 0, 0)
cellrows = []
for k, (i, j) in enumerate(W):
    for a in range(A):
        for b in range(A):
            cellrows.append([1.0 if (p[i] == a and p[j] == b) else 0.0 for p in pts])
M = np.array(cellrows); Mp = np.linalg.pinv(M)
perms = list(itertools.permutations(range(A)))
bad = 0; counts = {}
for s0, s1, s2 in itertools.product(perms, repeat=3):
    rhs = []
    for k, s in enumerate((s0, s1, s2)):
        for a in range(A):
            for b in range(A):
                rhs.append(1.0 / A if b == s[a] else 0.0)
    lam = Mp @ np.array(rhs)
    assert np.abs(M @ lam - np.array(rhs)).max() < 1e-9
    res = milp(c=lam, constraints=[cons], integrality=np.ones(n), bounds=Bounds(0, 1))
    mono = tuple(s2[s1[s0[x]]] for x in range(A))
    ident = mono == tuple(range(A))
    neg = res.fun < -1e-9
    counts[(ident, neg)] = counts.get((ident, neg), 0) + 1
    if ident == neg: bad += 1
print("families:", len(perms) ** 3, " (monodromy identity?, min Lambda < 0?) counts:", counts)
print("min Lambda < 0 exactly when monodromy != identity:", bad == 0)
