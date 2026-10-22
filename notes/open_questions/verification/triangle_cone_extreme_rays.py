"""Priority 1, exact (2026-10-18). Triangle over {0..A-1}, span V of window functions.
By LP duality, every probability state on the board is a mixture of points iff every non-negative g in V is
a non-negative combination of indicators of board sets. When the board is exactly the 0/1 elements of V
(machine-known at A=3), it suffices that every EXTREME RAY of the cone C = {g in V : g >= 0} is a multiple
of a 0/1 vector.
V is parametrised by the values y on the face points (some coordinate 0); an inner point's value is the
anchor-0 expansion. C = {y >= 0 on the face, expansion >= 0 inside}. Exact double description: start from the
orthant (rays = unit vectors) and add the inner inequalities one at a time, in integer arithmetic, with the
combinatorial adjacency test.
"""
import itertools, sys
from math import gcd
from functools import reduce

A = int(sys.argv[1]) if len(sys.argv) > 1 else 3
pts = list(itertools.product(range(A), repeat=3))
face = [x for x in pts if 0 in x]; inner = [x for x in pts if 0 not in x]
fi = {p: i for i, p in enumerate(face)}; d = len(face)
def expansion(p):
    a, b, c = p
    coef = [0] * d
    for q, s in (((a, b, 0), 1), ((a, 0, c), 1), ((0, b, c), 1), ((a, 0, 0), -1), ((0, b, 0), -1), ((0, 0, c), -1), ((0, 0, 0), 1)):
        coef[fi[q]] += s
    return coef
ineqs = [[1 if j == i else 0 for j in range(d)] for i in range(d)] + [expansion(p) for p in inner]
def dot(u, v): return sum(x * y for x, y in zip(u, v))
def norm(v):
    g = reduce(gcd, (abs(x) for x in v if x), 0)
    return tuple(x // g for x in v) if g else tuple(v)
def rank(rows):
    M = [list(r) for r in rows]; rk = 0; ncol = d
    for col in range(ncol):
        piv = next((i for i in range(rk, len(M)) if M[i][col]), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        for i in range(len(M)):
            if i != rk and M[i][col]:
                f, g_ = M[i][col], M[rk][col]
                M[i] = [x * g_ - y * f for x, y in zip(M[i], M[rk])]
        rk += 1
    return rk
rays = [tuple(1 if j == i else 0 for j in range(d)) for i in range(d)]
used = list(range(d))
for k in range(d, len(ineqs)):
    h = ineqs[k]
    pos = [r for r in rays if dot(h, r) > 0]; neg = [r for r in rays if dot(h, r) < 0]; zer = [r for r in rays if dot(h, r) == 0]
    zsets = {r: frozenset(i for i in used if dot(ineqs[i], r) == 0) for r in rays}
    new = []
    for rp in pos:
        for rn in neg:
            Z = zsets[rp] & zsets[rn]
            if len(Z) < d - 2: continue
            # adjacency: no other ray's zero set contains Z (combinatorial test)
            if any(Z <= zsets[r] for r in rays if r != rp and r != rn): continue
            a, b = dot(h, rp), -dot(h, rn)
            new.append(norm([b * x + a * y for x, y in zip(rp, rn)]))
    rays = pos + zer + list(set(new)); used.append(k)
    print(f"  added inequality {k + 1}/{len(ineqs)}: {len(rays)} rays", flush=True)
def full_values(y):
    vals = {}
    for p in face: vals[p] = y[fi[p]]
    for p in inner: vals[p] = dot(expansion(p), y)
    return vals
bad = []
for y in rays:
    v = list(full_values(y).values()); m = max(v)
    if any(x not in (0, m) for x in v): bad.append(v)
print(f"A={A}: extreme rays of C = {len(rays)}; not proportional to a 0/1 vector: {len(bad)}")
if bad: print("  example:", sorted(set(bad[0])))
