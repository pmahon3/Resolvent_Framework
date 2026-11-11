# 2026-11-10 (TRIANGLE_CONSEQUENCES_CHECK.md, C2(d)).  Exact integer check, no LP/MILP, no closure.
# The 3x4x4 pair laws of definitions_draft.md section 18 (uniform 1/9 on 9 allowed pairs per window) are
# evaluated on EVERY box set (0/1 vector of the pair span; 1,299,250 sets) of the grid 3x4x4.
# Lambda(F) is computed from the seven-term box formula with base point (0,0,0); it splits as
#   9*Lambda(F) = phi(G) + sum_{a>=1} psi_a(F_a),  G = F_0,
# so min/max over box sets = min/max over G of phi(G) + sum_a min/max over valid slices.  Integers only.
# Also: exact search for the mixture question is NOT done here (recorded elsewhere as exact).
import itertools
n0, n1, n2 = 3, 4, 4
A01 = {0: {0, 1, 2}, 1: {0, 1, 3}, 2: {1, 2, 3}}                 # x0 -> allowed x1
A12 = {0: {1, 2}, 1: {0, 1, 3}, 2: {0, 2}, 3: {2, 3}}            # x1 -> allowed x2
A20 = {0: {0, 1}, 1: {0, 2}, 2: {0, 1, 2}, 3: {1, 2}}            # x2 -> allowed x0
m01 = lambda a, b: int(b in A01[a]); m12 = lambda b, c: int(c in A12[b]); m20 = lambda c, a: int(a in A20[c])
p0 = [sum(m01(a, b) for b in range(n1)) for a in range(n0)]
p1 = [sum(m01(a, b) for a in range(n0)) for b in range(n1)]
p2 = [sum(m12(b, c) for b in range(n1)) for c in range(n2)]
assert p0 == [sum(m20(c, a) for c in range(n2)) for a in range(n0)]
assert p1 == [sum(m12(b, c) for c in range(n2)) for b in range(n1)]
assert p2 == [sum(m20(c, a) for a in range(n0)) for c in range(n2)]
assert sum(p0) == 9
print('marginals x0, x1, x2 (ninths):', p0, p1, p2)
cells = [(b, c) for b in range(n1) for c in range(n2)]; M = len(cells)
bit = {bc: k for k, bc in enumerate(cells)}
# per-slice weights (ninths): slice a contributes  sum_c m20(c,a) F(a,0,c) + sum_b m01(a,b) F(a,b,0) - p0(a) F(a,0,0)
def psi_w(a):
    w = [0] * M
    for c in range(n2): w[bit[(0, c)]] += m20(c, a)
    for b in range(n1): w[bit[(b, 0)]] += m01(a, b)
    w[bit[(0, 0)]] -= p0[a]
    return w
# base slice G = F_0: sum_{b,c} m12(b,c) G(b,c) - sum_c p2(c) G(0,c) - sum_b p1(b) G(b,0) + 9*G(0,0)  (+ psi_0)
phi_w = [m12(b, c) for (b, c) in cells]
for c in range(n2): phi_w[bit[(0, c)]] -= p2[c]
for b in range(n1): phi_w[bit[(b, 0)]] -= p1[b]
phi_w[bit[(0, 0)]] += 9
w0 = [x + y for x, y in zip(phi_w, psi_w(0))]
def val(w, mask): return sum(w[k] for k in range(M) if mask >> k & 1)
V0 = [val(w0, G) for G in range(1 << M)]
V = {a: [val(psi_w(a), G) for G in range(1 << M)] for a in (1, 2)}
# self-test of the formula against direct evaluation on point masses and on window events is implicit in:
# Lambda(Omega) must be 9, Lambda(empty) 0.
adds = set()
for al in itertools.product(range(-1, 2), repeat=n1):
    for be in itertools.product(range(-2, 3), repeat=n2):
        d = tuple(al[b] + be[c] for b, c in cells)
        if all(-1 <= v <= 1 for v in d): adds.add(d)
pos = [sum(1 << k for k, v in enumerate(d) if v == 1) for d in adds]
neg = [sum(1 << k for k, v in enumerate(d) if v == -1) for d in adds]
lo, hi, count, nzero, hist = 10**9, -10**9, 0, 0, {}
full = (1 << M) - 1
for G in range(1 << M):
    sl = [(G | p) & ~m for p, m in zip(pos, neg) if p & G == 0 and m & ~G & full == 0]
    count += len(sl) ** 2
    v1 = [V[1][s] for s in sl]; v2 = [V[2][s] for s in sl]
    lo = min(lo, V0[G] + min(v1) + min(v2)); hi = max(hi, V0[G] + max(v1) + max(v2))
    if G == full: assert V0[G] + V[1][full] + V[2][full] == 9
    if G == 0: assert V0[0] + V[1][0] + V[2][0] == 0
print('box sets:', count, ' min 9*Lambda =', lo, ' max 9*Lambda =', hi)
print('Lambda >= 0 on every 0/1 span vector of 3x4x4 (exact):', lo >= 0 and hi <= 9)

# ---- sanity of the seven-term formula: on the window event {x0=a, x1=b} it must return m01(a,b), etc.
def lam9(F):   # F: dict point -> 0/1, direct seven-term evaluation
    t = sum(m12(b, c) * F[(0, b, c)] for b in range(n1) for c in range(n2))
    t += sum(m20(c, a) * F[(a, 0, c)] for a in range(n0) for c in range(n2))
    t += sum(m01(a, b) * F[(a, b, 0)] for a in range(n0) for b in range(n1))
    t -= sum(p2[c] * F[(0, 0, c)] for c in range(n2)) + sum(p1[b] * F[(0, b, 0)] for b in range(n1))
    t -= sum(p0[a] * F[(a, 0, 0)] for a in range(n0))
    return t + 9 * F[(0, 0, 0)]
pts = list(itertools.product(range(n0), range(n1), range(n2)))
for a in range(n0):
    for b in range(n1): assert lam9({x: int(x[0] == a and x[1] == b) for x in pts}) == m01(a, b)
for b in range(n1):
    for c in range(n2): assert lam9({x: int(x[1] == b and x[2] == c) for x in pts}) == m12(b, c)
for c in range(n2):
    for a in range(n0): assert lam9({x: int(x[2] == c and x[0] == a) for x in pts}) == m20(c, a)
print('seven-term formula reproduces the pair laws on all pair cells: OK')

# ---- not a mixture: exact integer certificate g = sum of pair functions, g >= 0 on all 48 points, Lambda(g) < 0.
# Found by a small float LP, then rounded and VERIFIED IN INTEGERS (the LP is only a search).
try:
    import numpy as np
    from scipy.optimize import linprog
    idx = {}
    for a in range(n0):
        for b in range(n1): idx[('01', a, b)] = len(idx)
    for b in range(n1):
        for c in range(n2): idx[('12', b, c)] = len(idx)
    for c in range(n2):
        for a in range(n0): idx[('20', c, a)] = len(idx)
    cost = np.zeros(len(idx))
    for (w, i, j), k in idx.items(): cost[k] = {'01': m01, '12': m12, '20': m20}[w](i, j)
    Aub = np.zeros((len(pts), len(idx)))
    for r, (a, b, c) in enumerate(pts):
        for key in (('01', a, b), ('12', b, c), ('20', c, a)): Aub[r, idx[key]] = -1
    res = linprog(cost, A_ub=Aub, b_ub=np.zeros(len(pts)), bounds=[(-2, 2)] * len(idx), method='highs')
    for scale in (1, 2, 3, 4, 6):
        cint = [int(round(v * scale)) for v in res.x]
        g = [cint[idx[('01', a, b)]] + cint[idx[('12', b, c)]] + cint[idx[('20', c, a)]] for (a, b, c) in pts]
        L = sum(int(cost[k]) * cint[k] for k in range(len(idx)))
        if min(g) >= 0 and L < 0:
            print('integer certificate: g >= 0 on all 48 points (values', sorted(set(g)), '), 9*Lambda(g) =', L, '< 0  => not a mixture (exact)')
            break
    else: print('no integer certificate found by rounding (LP value', res.fun, ')')
except ImportError: print('scipy not available; mixture certificate skipped')
