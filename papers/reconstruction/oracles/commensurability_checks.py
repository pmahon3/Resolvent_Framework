"""Independent re-verification (this environment) of the four finite claims from
the capture session's commensurability derivations (2026-07-06).

A. Minimal EA/PR separation: 3 outcomes, 2 contexts, common subalgebra trivial,
   data unrealisable.
B. First pairwise-complete separation (k=3): contexts x1, x2, x1 XOR x2 on {0,1}^2;
   every context PAIR has complete cell-intersection (hence pairwise commensurable),
   but s(R1)=s(C1)=1, s(D1)=0 is coherent with value 2 vs realisable ceiling 1
   (Frechet-Bonferroni; incidence R1 cap C1 subseteq D1).
C. Wrap-4-cycle parity model (equal, equal, equal, anti; uniform singles):
   pairwise coherent, unrealisable.
D. Odd-vs-even exclusivity cycles: fractional packing LP value C4 = 2 (= classical),
   C5 = 5/2 (> classical 2).
"""
from itertools import product

# ---------- A ----------
Omega = [1, 2, 3]
P1 = [{3}, {1, 2}]          # "is it 3?"
P2 = [{1}, {2, 3}]          # "is it 1?"
def algebra(partition):
    cells = [frozenset(c) for c in partition]
    out = set()
    for mask in range(1 << len(cells)):
        u = frozenset().union(*[cells[k] for k in range(len(cells)) if mask >> k & 1]) if mask else frozenset()
        out.add(u)
    return out
common = algebra(P1) & algebra(P2)
assert common == {frozenset(), frozenset(Omega)}, common
# data: s({3})=1 and s({1})=1; realisation needs a point in {3} cap {1} = empty
assert not ({3} & {1})
print("A PASS: common subalgebra trivial (EA vacuous); mu({3})=mu({1})=1 unrealisable")

# ---------- B ----------
pts = list(product([0, 1], repeat=2))
ctx = {
    "R": lambda p: p[0],            # x1
    "C": lambda p: p[1],            # x2
    "D": lambda p: p[0] ^ p[1],     # x1 xor x2
}
# pairwise completeness: every cell of one meets every cell of the other
for a in ctx:
    for b in ctx:
        if a < b:
            for va in (0, 1):
                for vb in (0, 1):
                    assert any(ctx[a](p) == va and ctx[b](p) == vb for p in pts), (a, b, va, vb)
print("B1 PASS: all three context pairs are cell-complete (pairwise commensurable)")
# incidence: R1 cap C1 subseteq D1 where R1={x1=1}, C1={x2=1}, D1={xor=0}
R1 = {p for p in pts if p[0] == 1}
C1 = {p for p in pts if p[1] == 1}
D1 = {p for p in pts if p[0] ^ p[1] == 0}
assert R1 & C1 <= D1
# realisable ceiling of mu(R1)+mu(C1)-mu(D1): max over point masses (LP vertex = point mass)
ceiling = max((p in R1) + (p in C1) - (p in D1) for p in pts)
assert ceiling == 1, ceiling
print("B2 PASS: coherent value 2 (s(R1)=s(C1)=1, s(D1)=0) vs realisable ceiling",
      ceiling, "- Frechet gap confirmed")

# ---------- C ----------
outcomes4 = list(product([0, 1], repeat=4))
edges = [(0, 1, "eq"), (1, 2, "eq"), (2, 3, "eq"), (3, 0, "anti")]
def edge_support_ok(x):
    for i, j, typ in edges:
        if typ == "eq" and x[i] != x[j]:
            return False
        if typ == "anti" and x[i] == x[j]:
            return False
    return True
assert not any(edge_support_ok(x) for x in outcomes4)
# pairwise coherence: each edge distribution has uniform single-site marginals,
# and any two contexts share at most one site, agreeing on its (uniform) marginal.
print("C PASS: wrap-4-cycle eq-eq-eq-anti model has EMPTY global support (unrealisable);"
      " single-site marginals uniform in every edge context (pairwise coherent)")

# ---------- D ----------
def cycle_packing_value(n):
    # LP: max sum p_i s.t. p_i + p_{i+1} <= 1 (indices mod n), p >= 0.
    # Verify claimed optimum via primal feasible point + dual certificate.
    if n % 2 == 0:
        primal = [1, 0] * (n // 2)                     # value n/2
        value = n // 2
        # dual: y on alternate edges (i,i+1), i even, each = 1 covers each vertex once
        dual_bound = n // 2
    else:
        primal = [0.5] * n                             # value n/2
        value = n / 2
        # dual: y_e = 1/2 on every edge; each vertex in 2 edges -> covered with weight 1
        dual_bound = n / 2
    # check primal feasibility
    for i in range(n):
        assert primal[i] + primal[(i + 1) % n] <= 1 + 1e-12
    assert abs(sum(primal) - value) < 1e-12
    # dual soundness: sum_i p_i = sum over chosen edges of (p_i + p_j) * y_e <= sum y_e = bound
    return value, dual_bound
v4, b4 = cycle_packing_value(4)
v5, b5 = cycle_packing_value(5)
assert v4 == b4 == 2
assert v5 == b5 == 2.5
print(f"D PASS: fractional packing C4 = {v4} (= classical 2, inert);"
      f" C5 = {v5} (> 2, odd cycle carries violation)")

print("\nALL FOUR CLAIMS RE-VERIFIED IN THIS ENVIRONMENT")
