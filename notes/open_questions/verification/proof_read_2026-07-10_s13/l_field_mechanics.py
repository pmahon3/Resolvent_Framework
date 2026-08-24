#!/usr/bin/env python3
"""Claim L set/algebra mechanics on a finite truncation (from scratch, s13).

Model: Omega = m named points + ideal element rB ("the uncountable core of
B"); B = {rB} union B0 for each B0 subseteq named points.  In the truncation:
  A cap B "countable"  <-> rB not in A;   B \\ A "countable" <-> rB in A.
The relative ctble/co-ctble field A_B is then ALL subsets of Omega (every A
gets exactly one flag), and the co-countable-in-B state is
nu_B(A) = [rB in A].

Checks:
  (1) exactly one flag holds per A (well-definedness needs B "uncountable",
      i.e. rB in B: a variant with B = B0 finite produces flag CONFLICTS --
      detected);
  (2) A_B is a field; nu_B is a two-valued f.a. state; complement law;
  (3) non-principality over every CONCRETE point: for each named omega,
      A = Omega \\ {omega} has nu_B(A) = 1 and omega not in A, so
      nu_B != delta_omega restricted to A_B for any actual point omega
      (in the truncation nu_B = delta_{rB}; rB is an IDEAL point standing
      for "an uncountable co-countable core", which in the real setting is
      not a point -- that is exactly the non-instantiable content);
  (4) monotonicity + inclusion-exclusion for nu_B.

NOT exercised: existence of a Cantor set inside an uncountable Borel B
(perfect set property), compact co-countable-in-B in-field sets containing
that Cantor set, and the resulting concrete (8.1) failure at F = Omega\\{x},
x in the Cantor core; also the R-contrapositive route (nu_B non-principal =>
fails (8.1) under EVERY Hausdorff topology).
"""
import sys, itertools
from fractions import Fraction

PASS = 0
FAIL = 0
def check(cond, msg):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print("FAIL:", msg)

for m in range(1, 5):
    named = list(range(m))
    rB = "rB"
    Omega = frozenset(named) | {rB}
    subsets = []
    pts = sorted(named) + [rB]
    for r in range(len(pts) + 1):
        for S in itertools.combinations(pts, r):
            subsets.append(frozenset(S))

    for B0bits in range(1 << m):
        B0 = frozenset(i for i in range(m) if B0bits >> i & 1)
        B = B0 | {rB}   # uncountable B (contains the ideal core)
        # (1) exactly one flag per A
        for A in subsets:
            flag_ctble = rB not in A        # A cap B countable (truncation)
            flag_co    = rB in A            # B \ A countable  (truncation)
            check(flag_ctble != flag_co, "flags not mutually exclusive/exhaustive")
        # (2) field + state axioms;  nu_B(A) = [rB in A]
        nu = {A: (1 if rB in A else 0) for A in subsets}
        check(nu[Omega] == 1, "nu_B(Omega) != 1")
        dis_pairs = [(A, C) for A in subsets for C in subsets if not (A & C)]
        check(all(nu[A | C] == nu[A] + nu[C] for A, C in dis_pairs),
              "nu_B not finitely additive")
        check(all(nu[Omega - A] == 1 - nu[A] for A in subsets),
              "nu_B complement law fails")
        check(all(v in (0, 1) for v in nu.values()), "nu_B not two-valued")
        # (4) monotonicity + inclusion-exclusion
        check(all(nu[A] <= nu[C] for A in subsets for C in subsets if A <= C),
              "nu_B monotonicity fails")
        check(all(nu[A | C] + nu[A & C] == nu[A] + nu[C]
                  for A in subsets for C in subsets),
              "nu_B inclusion-exclusion fails")
        # (3) non-principality over every concrete point
        for w in named:
            A = Omega - {w}
            check(nu[A] == 1 and w not in A,
                  f"cofinite-avoidance witness fails at {w}")
            check(not all((nu[F] == 1) == (w in F) for F in subsets),
                  f"nu_B == delta_{w} unexpectedly")
        # ideal-point artifact, documented: in the truncation nu_B = delta_rB
        check(all((nu[F] == 1) == (rB in F) for F in subsets),
              "truncation artifact check (nu_B = delta at ideal point)")

    # (1') countable-B variant: B = B0 with no ideal core.  Countability in
    # the truncation = "does not contain rB".  Then for EVERY A both
    # "A cap B countable" and "B \ A countable" hold (neither contains rB),
    # so the two clauses defining nu_B assign both 0 and 1: ill-defined.
    for B0bits in range(1 << m):
        B = frozenset(i for i in range(m) if B0bits >> i & 1)  # rB not in B
        for A in subsets:
            flag_ctble = rB not in (A & B)   # A cap B countable
            flag_co    = rB not in (B - A)   # B \ A countable
            check(flag_ctble and flag_co,
                  "countable-B ill-definedness not detected (some flag failed)")

print(f"l_field_mechanics: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
