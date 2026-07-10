"""Machine corroboration of the parity theorem (design session, 2026-07-07)
and the pre-registered P9-P12.

Theorem: golden-mean ring C_L is commensurable iff L even. Mechanism:
C = FSTAB(C_L), R = STAB(C_L) in vertex-marginal coordinates (reduction
lemma); parity via det(incidence C_L) = 1-(-1)^L with all proper square
submatrices forest-TU; odd case has EXACTLY ONE fractional vertex u = 1/2.

Checks:
 1. Determinant identity, L = 3..8.
 2. Forest-TU: every proper square submatrix of the ring incidence matrix
    has det in {-1,0,1}, L = 3..7.
 3. P12 + even-integrality: exact vertex enumeration of FSTAB(C_L):
    L=3: 4+1, L=5: 11+1 (the half-point, UNIQUE fractional), L=4,6: all
    integral.
 4. P11 (EA-fidelity at L=5): the harness's own EA equality system for the
    golden-mean C5 scope protocol has rank exactly #cells - 5 = 10, and the
    affine lift q(u) [q_i(1,0)=u_i, q_i(0,1)=u_{i+1}, q_i(0,0)=1-u_i-u_{i+1}]
    satisfies it identically => C ~ FSTAB exactly (cell-nonneg <-> FSTAB
    inequalities structurally).
 5. P9 (XOR): even rings L=4,6 commensurable (V = the two colorings);
    odd rings degenerate (V empty) - reported, not scored.
 6. P10 (implication): all rings L=3..6 commensurable (V = two constants).
    NOTE: harness tests the V-INDUCED cell structure (the empty (0,1) cell is
    not reportable); the design derivation's relation-level C agrees here.
 7. CF = 1 for the odd half-model (strong contextuality): its edge zeros
    force any noncontextual component to dominate an exactly-one-per-edge
    config = 2-coloring of an odd cycle = nonexistent (support argument).
"""
import sys
sys.path.insert(0, '.')
from fractions import Fraction as F
from itertools import product, combinations
from commensurability_harness import build_protocol, rref
from ring_commensurability import commensurable, ring_variety, scope_contexts

def det(M):
    M = [list(map(F, row)) for row in M]
    n = len(M); d = F(1)
    for c in range(n):
        pr = next((i for i in range(c, n) if M[i][c] != 0), None)
        if pr is None: return F(0)
        if pr != c: M[c], M[pr] = M[pr], M[c]; d = -d
        d *= M[c][c]
        inv = 1 / M[c][c]
        for i in range(c+1, n):
            if M[i][c] != 0:
                f0 = M[i][c] * inv
                M[i] = [a - f0*b for a, b in zip(M[i], M[c])]
    return d

def ring_incidence(L):
    return [[1 if j in (i, (i+1) % L) else 0 for j in range(L)] for i in range(L)]

# ---- 1. determinant identity ----
for L in range(3, 9):
    d = det(ring_incidence(L))
    assert abs(d) == (0 if L % 2 == 0 else 2), (L, d)
print("1 PASS: det(incidence C_L) = 0 (even) / +-2 (odd), L=3..8")

# ---- 2. forest-TU on proper submatrices ----
for L in range(3, 8):
    M = ring_incidence(L)
    for r in range(1, L):
        for rows in combinations(range(L), r):
            for cols in combinations(range(L), r):
                sub = [[M[i][j] for j in cols] for i in rows]
                assert det(sub) in (F(-1), F(0), F(1)), (L, rows, cols)
print("2 PASS: every proper square submatrix has det in {-1,0,1}, L=3..7 (forest-TU)")

# ---- 3. FSTAB vertex census ----
def fstab_vertices(L):
    # constraints: -u_i <= 0 (i<L); u_i + u_{i+1} <= 1
    rows = [[(-1 if j == i else 0) for j in range(L)] for i in range(L)]
    rhs = [F(0)]*L
    for i in range(L):
        rows.append([1 if j in (i, (i+1) % L) else 0 for j in range(L)])
        rhs.append(F(1))
    verts = set()
    for S in combinations(range(2*L), L):
        A = [rows[s] for s in S]; b = [rhs[s] for s in S]
        if det(A) == 0: continue
        # solve A u = b
        M = [list(map(F, A[i])) + [b[i]] for i in range(L)]
        R, piv = rref(M)
        if len(R) < L: continue
        u = [F(0)]*L
        for row, pc in zip(R, piv):
            u[pc] = row[-1]
        if all(x >= 0 for x in u) and all(u[i]+u[(i+1) % L] <= 1 for i in range(L)):
            verts.add(tuple(u))
    return verts

for L in (3, 4, 5, 6):
    vs = fstab_vertices(L)
    frac = [v for v in vs if any(x not in (F(0), F(1)) for x in v)]
    integral = len(vs) - len(frac)
    if L % 2 == 1:
        assert len(frac) == 1 and frac[0] == tuple([F(1,2)]*L), frac
        print(f"3 L={L}: {integral} integral + 1 fractional vertex = u==1/2 (UNIQUE)"
              + ("  [P12 PASS: 11+1=12]" if L == 5 else ""))
        if L == 5: assert integral == 11
        if L == 3: assert integral == 4
    else:
        assert not frac
        print(f"3 L={L}: all {integral} vertices integral (TU conclusion)")

# ---- 4. P11: EA-fidelity at L=5 ----
V = ring_variety(5)
ctxs = scope_contexts(V, [(i, (i+1) % 5) for i in range(5)])
cells, ctx_of, E, f, verts = build_protocol(len(V), ctxs)
Rr, Rp = rref([row + [rhs] for row, rhs in zip(E, f)])
rank = len(Rr)
assert len(cells) == 15
print(f"4 P11: rank(EA system) = {rank} (need 10 = 15 cells - 5 dof):",
      "PASS" if rank == 10 else "MISS — EA sees MORE shared events than the lemma")
assert rank == 10
# affine lift satisfies EA identically: check at 6 affinely independent u points
idxV = {p: i for i, p in enumerate(V)}
def q_of_u(u):
    q = [None]*15
    for j, cell in enumerate(cells):
        edge = ctx_of[j]
        # recover the (a,b) key of this cell from any member config
        p0 = V[min(cell)]
        a, b = p0[edge], p0[(edge+1) % 5]
        q[j] = {(1,0): u[edge], (0,1): u[(edge+1) % 5],
                (0,0): 1 - u[edge] - u[(edge+1) % 5]}[(a, b)]
    return q
import random
random.seed(7)
pts = [[F(0)]*5] + [[F(1) if j == i else F(0) for j in range(5)] for i in range(5)]
for u in pts:
    q = q_of_u(u)
    for row, rhs in zip(E, f):
        assert sum(r*x for r, x in zip(row, q)) == rhs, (u, row)
print("4 P11 PASS: affine lift q(u) satisfies the harness EA system identically;"
      " cell-nonneg <-> FSTAB inequalities => C ~ FSTAB(C5) exactly")

# ---- 5. P9: XOR ----
def xor_ring_variety(L):
    return [p for p in product([0,1], repeat=L)
            if all(p[i] != p[(i+1) % L] for i in range(L))]
for L in (4, 6):
    Vx = xor_ring_variety(L)
    assert len(Vx) == 2
    cx = scope_contexts(Vx, [(i, (i+1) % L) for i in range(L)])
    ok, _ = commensurable(len(Vx), cx, f"5 P9 XOR C{L} (n=2)")
    assert ok
for L in (3, 5):
    assert not xor_ring_variety(L)
print("5 P9 note: odd XOR rings have EMPTY variety (degenerate) — reported, not scored")

# ---- 6. P10: implication ----
def imp_ring_variety(L):
    return [p for p in product([0,1], repeat=L)
            if all(p[i] <= p[(i+1) % L] for i in range(L))]
for L in (3, 4, 5, 6):
    Vi = imp_ring_variety(L)
    assert len(Vi) == 2   # the two constants
    ci = scope_contexts(Vi, [(i, (i+1) % L) for i in range(L)])
    ok, _ = commensurable(len(Vi), ci, f"6 P10 implication C{L} (n=2)")
    assert ok

# ---- 7. CF = 1 (strong contextuality) of the odd half-model ----
for L in (3, 5):
    Vg = ring_variety(L)
    # noncontextual component must respect the half-model's zeros: p_i(0,0)=0
    # per edge => support in configs with x_i + x_{i+1} >= 1 for all i
    assert not any(all(p[i] + p[(i+1) % L] >= 1 for i in range(L)) for p in Vg)
    print(f"7 CF=1 at C{L}: no legal config dominates exactly-one-per-edge —"
          " noncontextual part is 0 (strongly contextual)")

print("\nPARITY THEOREM: all machine-checkable joints + P9-P12 CORROBORATED")
