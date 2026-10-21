"""Certify the 3x4x4 candidate (2026-10-21). D is contained in V01 = {f in {0,1}^pts : f in span of pair cells}.
If min over V01 of Lambda(f) >= 0, then Lambda >= 0 on every buildable set, so Lambda is a carrier state; with
Lambda(g) < 0 for a non-negative g in the span, it is not a mixture: a certified hidden twist.
MILP: binary f, (I - P_V) f = 0 via an integer basis of the orthogonal complement, minimise c.f with c = M^+T mu.
Exact post-check of the optimum and of Lambda(g) in rationals."""
import itertools, numpy as np, sympy as sp
from fractions import Fraction as Fr
from scipy.optimize import milp, LinearConstraint, Bounds
sz = (3, 4, 4); E = [(0, 1), (1, 2), (2, 0)]
pts = list(itertools.product(*[range(s) for s in sz]))
cells = [(e, a, b) for e in range(3) for a in range(sz[E[e][0]]) for b in range(sz[E[e][1]])]
M = sp.Matrix([[1 if (p[E[e][0]] == a and p[E[e][1]] == b) else 0 for (e, a, b) in cells] for p in pts])
s01 = {0: {0, 1, 2}, 1: {0, 1, 3}, 2: {1, 2, 3}}; s12 = {0: {1, 2}, 1: {0, 1, 3}, 2: {0, 2}, 3: {2, 3}}; s20 = {0: {0, 1}, 1: {0, 2}, 2: {0, 1, 2}, 3: {1, 2}}
allow = [s01, s12, s20]
mu = [Fr(1, 9) if b in allow[e][a] else Fr(0) for (e, a, b) in cells]
# Lambda on span: Lambda(f) = mu . c where M c = f; well-defined iff mu kills null(M)
null = M.nullspace()
assert all(sum(sp.Rational(mu[k]) * v[k] for k in range(len(cells))) == 0 for v in null), "not well defined"
# linear form: Lambda(f) = w . f on the span, w = any solution of M^T w = mu restricted... use pseudo-inverse rationally
Mt = M.T
w = (M * (M.T * M).pinv()) * sp.Matrix([sp.Rational(x) for x in mu])  # w = M (M^T M)^+ mu ; then w.f = mu.(M^+ f) on span
W = np.array([float(x) for x in w])
# span membership: f in col(M)  <=>  N f = 0 for a basis N of left null space
Nleft = M.T.nullspace()  # vectors y with y^T M = 0  (left null space of M is null of M^T)
N = np.array([[float(x) for x in v] for v in Nleft])
res = milp(c=W, constraints=[LinearConstraint(N, 0, 0)], integrality=np.ones(len(pts)), bounds=Bounds(0, 1))
f = np.round(res.x).astype(int)
fs = sp.Matrix(list(f)); assert (M.T.nullspace() and all((v.T * fs)[0] == 0 for v in Nleft))
c = M.gauss_jordan_solve(fs)[0]; c = c.subs({s: 0 for s in c.free_symbols})
val = sum(c[k] * sp.Rational(mu[k]) for k in range(len(cells)))
print("MILP status:", res.status, "| min over V01 of Lambda (exact at optimum):", val)
# Lambda(g) for the exact non-binary extreme ray found earlier at 3x4x4
g = [0] * len(pts)
for p in [(0, 0, 0), (2, 3, 1)]: g[pts.index(p)] = 2
for p in [(0, 0, 2), (0, 0, 3), (0, 1, 0), (0, 2, 0), (0, 2, 2), (1, 0, 0), (1, 0, 3), (1, 1, 0), (1, 1, 1), (1, 1, 3), (1, 3, 1), (1, 3, 3), (2, 1, 1), (2, 2, 1), (2, 2, 2), (2, 3, 2), (2, 3, 3)]: g[pts.index(p)] = 1
cg = M.gauss_jordan_solve(sp.Matrix(g))[0]; cg = cg.subs({s: 0 for s in cg.free_symbols})
print("Lambda(g) exact for the verified ray:", sum(cg[k] * sp.Rational(mu[k]) for k in range(len(cells))))
# non-mixture witness: min Lambda(g) over g = M c >= 0, sum g = 1 (LP), then exact re-evaluation
from scipy.optimize import linprog
Mf = np.array(M.tolist(), float); muf = np.array([float(x) for x in mu])
res2 = linprog(muf, A_ub=-Mf, b_ub=np.zeros(len(pts)), A_eq=[np.ones(len(pts)) @ Mf], b_eq=[1.0], bounds=[(None, None)] * len(cells), method="highs")
gg = Mf @ res2.x; gg[np.abs(gg) < 1e-9] = 0; gg = gg / gg[gg > 0].min()
gi = [int(round(x)) for x in gg]; assert np.allclose(gg, gi, atol=1e-6)
cg2 = M.gauss_jordan_solve(sp.Matrix(gi))[0]; cg2 = cg2.subs({s: 0 for s in cg2.free_symbols})
print("witness g (integer, >= 0):", {pts[i]: gi[i] for i in range(len(pts)) if gi[i]})
print("Lambda(witness) exact:", sum(cg2[k] * sp.Rational(mu[k]) for k in range(len(cells))))
