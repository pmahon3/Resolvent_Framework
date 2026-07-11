#!/usr/bin/env python3
"""Fresh-context adversarial re-derivation, receipt (b): MO_n truncations of
the MO_omega construction of section 9a(i), built independently.

MO_omega: Omega = 2^omega, L = {0, Omega, A_i, A_i^c : i in omega},
A_i = {x : x_i = 0}.  Finite proxy: Omega_n = 2^n, same definition, i < n.
The defining incidence claims ("any two distinct non-complementary members
intersect") depend only on two coordinates at a time, so the n>=2 truncation
checks them faithfully.

Checks per n = 2..6 (n=1 is Boolean, noted and skipped for non-Boolean tests):
  - |L| = 2n + 2, sigma-class axioms
  - the ONLY disjoint pairs of nontrivial elements are complementary ones
    (all four A_i^{+/-} cap A_j^{+/-} nonempty for i != j)
  - lattice: every pair has GLB and LUB; off-block meets are empty
  - non-Boolean (incompatible pair), trivial centre
  - blocks = the n four-element fields {0, A_i, A_i^c, Omega}
  - horizontal sum: pairwise block overlaps = {0, Omega}; no two nonzero
    proper elements of distinct blocks disjoint
  - all 2^n two-valued f.a. states exist and every one is a Dirac
    (=> concrete, and Phi holds trivially at finite scale)
"""
import sys
from itertools import combinations

fails = []
def check(name, cond, detail=""):
    print(("PASS: " if cond else "FAIL: ") + name + (f" [{detail}]" if detail else ""))
    if not cond:
        fails.append(name)

for n in range(2, 7):
    print(f"--- MO_{n} on 2^{n} ---")
    Omega = frozenset(range(1 << n))
    Ai = [frozenset(x for x in Omega if not (x >> i) & 1) for i in range(n)]
    L = [frozenset(), Omega] + Ai + [Omega - a for a in Ai]
    Lset = set(L)
    check(f"n={n}: |L| = 2n+2 distinct", len(Lset) == 2 * n + 2)
    check(f"n={n}: complement-closed, contains 0",
          frozenset() in Lset and all((Omega - S) in Lset for S in L))

    nontriv = [S for S in L if S and S != Omega]
    ok_pairs = True
    only_compl_disjoint = True
    for S, T in combinations(nontriv, 2):
        if not (S & T):
            if T != Omega - S:
                only_compl_disjoint = False
    for i, j in combinations(range(n), 2):
        for U in (Ai[i], Omega - Ai[i]):
            for V in (Ai[j], Omega - Ai[j]):
                if not (U & V):
                    ok_pairs = False
    check(f"n={n}: all four A_i^± cap A_j^± nonempty (i!=j)", ok_pairs)
    check(f"n={n}: only disjoint nontrivial pairs are complementary",
          only_compl_disjoint)
    ok = True
    for S, T in combinations(L, 2):
        if not (S & T) and (S | T) not in Lset:
            ok = False
    check(f"n={n}: closed under disjoint unions (sigma-class, finite scale)", ok)

    def meet(Sa, Sb):
        lows = [C for C in L if C <= Sa and C <= Sb]
        tops = [C for C in lows if all(D <= C for D in lows)]
        return tops[0] if tops else None
    def join(Sa, Sb):
        ups = [C for C in L if Sa <= C and Sb <= C]
        bots = [C for C in ups if all(C <= D for D in ups)]
        return bots[0] if bots else None
    ok_m = all(meet(Sa, Sb) is not None for Sa in L for Sb in L)
    ok_j = all(join(Sa, Sb) is not None for Sa in L for Sb in L)
    check(f"n={n}: lattice (all meets exist)", ok_m)
    check(f"n={n}: all joins exist", ok_j)
    ok = True
    for S, T in combinations(nontriv, 2):
        if T == Omega - S:
            continue
        if not (S <= T or T <= S):
            if meet(S, T) != frozenset():
                ok = False
    check(f"n={n}: off-block meets are 0", ok)

    def compat(Sa, Sb):
        return (Sa & Sb) in Lset
    check(f"n={n}: non-Boolean (incompatible pair exists)",
          any(not compat(S, T) for S, T in combinations(L, 2)))
    centre = [S for S in L if all(compat(S, T) for T in L)]
    check(f"n={n}: trivial centre", sorted(len(s) for s in centre) == [0, 1 << n])

    # blocks: maximal pairwise-compatible families
    blocks = []
    for i in range(n):
        blocks.append(frozenset([frozenset(), Omega, Ai[i], Omega - Ai[i]]))
    ok = True
    for bl in blocks:
        for S in L:
            if S in bl:
                continue
            if all(compat(S, T) for T in bl):
                ok = False           # bl not maximal
        for S, T in combinations(bl, 2):
            if not compat(S, T):
                ok = False
    # and every element is in some block; no compatible cross-block pair
    for S, T in combinations(nontriv, 2):
        same = any(S in bl and T in bl for bl in blocks)
        if compat(S, T) != same and not (S == T):
            ok = False
    check(f"n={n}: blocks are exactly the n four-element fields", ok)

    ok_ov = all(len(b1 & b2) == 2 for b1, b2 in combinations(blocks, 2))
    ok_cross = True
    for b1, b2 in combinations(blocks, 2):
        for S in b1:
            if not S or S == Omega: continue
            for T in b2:
                if not T or T == Omega: continue
                if not (S & T):
                    ok_cross = False
    check(f"n={n}: horizontal sum: block overlaps trivial", ok_ov)
    check(f"n={n}: horizontal sum: no cross-block disjointness", ok_cross)

    # two-valued f.a. states: determined by (mu(A_i))_i; only additivity
    # constraints come from complementary pairs => all 2^n choices legal
    fa = []
    for mask in range(1 << n):
        mu = {frozenset(): 0, Omega: 1}
        for i in range(n):
            mu[Ai[i]] = (mask >> i) & 1
            mu[Omega - Ai[i]] = 1 - mu[Ai[i]]
        good = all(mu[Sa] + mu[Sb] == mu[Sa | Sb]
                   for Sa, Sb in combinations(L, 2)
                   if not (Sa & Sb) and (Sa | Sb) in Lset)
        if good:
            fa.append(mu)
    check(f"n={n}: exactly 2^n two-valued f.a. states", len(fa) == 1 << n)
    diracs = [{S: int(x in S) for S in L} for x in Omega]
    check(f"n={n}: every f.a. state is a Dirac (concrete; Phi trivial)",
          all(any(mu == d for d in diracs) for mu in fa))

print()
print("ALL CHECKS PASS" if not fails else f"{len(fails)} FAILURES")
sys.exit(len(fails))
