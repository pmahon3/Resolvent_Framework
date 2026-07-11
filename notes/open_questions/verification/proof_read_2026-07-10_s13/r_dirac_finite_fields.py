#!/usr/bin/env python3
"""Claim R mechanics on exhaustively enumerated finite fields (from scratch, s13 proof-read).

Space X = {0..n-1}, discrete topology (Hausdorff; every subset compact, so (8.1)
is trivially satisfied and the SET/ALGEBRA mechanics of Claim R are exercised):
  - fields of sets on X <-> partitions of X (field = unions of blocks)
  - ALL two-valued f.a. states enumerated by brute force over {0,1}-assignments
  - checks: monotonicity from finite additivity, inclusion-exclusion, complement
    law, K1 := {K : nu(K)=1} nonempty, K1 closed under intersection,
    D := /\\K1 nonempty, nu = delta_omega restricted to the field for EVERY
    omega in D, state count = number of blocks (ultrafilter correspondence).
  - random Fraction-valued f.a. states: monotonicity + inclusion-exclusion.

NOT exercised here (genuinely infinite/topological): the FIP-compactness step
for infinite K1, and Hausdorff-necessity (analytic counterexample: N with the
cofinite topology, finite/cofinite field, cofinite state satisfies (8.1) but is
non-principal -- every subset is compact in a non-Hausdorff way).
"""
import sys, itertools, random
from fractions import Fraction

random.seed(13)
PASS = 0
FAIL = 0
def check(cond, msg):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print("FAIL:", msg)

def partitions(elems):
    if not elems:
        yield []
        return
    first, rest = elems[0], elems[1:]
    for p in partitions(rest):
        for i in range(len(p)):
            yield [blk | {first} if j == i else set(blk) for j, blk in enumerate(p)]
        yield [set(b) for b in p] + [{first}]

for n in range(1, 5):
    X = frozenset(range(n))
    for part in partitions(list(range(n))):
        blocks = [frozenset(b) for b in part]
        k = len(blocks)
        field = sorted(
            {frozenset().union(*(blocks[i] for i in range(k) if mask >> i & 1))
             for mask in range(1 << k)},
            key=lambda s: (len(s), sorted(s)))
        check(len(field) == 1 << k, f"field size wrong n={n} k={k}")
        idx = {A: i for i, A in enumerate(field)}
        # sanity: field closed under complement and union
        check(all(X - A in idx for A in field), "field not complement-closed")
        check(all((A | B) in idx for A in field for B in field), "field not union-closed")

        dis_pairs = [(A, B) for A in field for B in field if not (A & B)]
        states = []
        for bits in itertools.product((0, 1), repeat=len(field)):
            if bits[idx[X]] != 1:
                continue
            ok = True
            for A, B in dis_pairs:
                if bits[idx[A | B]] != bits[idx[A]] + bits[idx[B]]:
                    ok = False
                    break
            if ok:
                states.append({A: bits[idx[A]] for A in field})
        check(len(states) == k, f"two-valued state count {len(states)} != #blocks {k} (n={n})")

        for nu in states:
            check(all(nu[A] <= nu[B] for A in field for B in field if A <= B),
                  "monotonicity fails")
            check(all(nu[A | B] + nu[A & B] == nu[A] + nu[B] for A in field for B in field),
                  "inclusion-exclusion fails")
            check(all(nu[X - A] == 1 - nu[A] for A in field), "complement law fails")
            # discrete topology: every element of the field is compact
            K1 = [K for K in field if nu[K] == 1]
            check(len(K1) > 0, "K1 empty")
            check(all(nu[A & B] == 1 for A in K1 for B in K1), "K1 not intersection-closed")
            D = X
            for K in K1:
                D = D & K
            check(len(D) > 0, "D empty")
            for w in D:
                check(all((nu[F] == 1) == (w in F) for F in field),
                      f"nu != delta_{w} restricted to field")
            # D equals intersection of ALL measure-one sets (principality set)
            M = X
            for A in field:
                if nu[A] == 1:
                    M = M & A
            check(D == M, "D != intersection of measure-1 sets")

        # random Fraction-valued f.a. states (weights on blocks)
        for _ in range(20):
            w = [Fraction(random.randint(0, 10)) for _ in range(k)]
            if sum(w) == 0:
                w[0] = Fraction(1)
            s = sum(w)
            w = [x / s for x in w]
            nu = {A: sum((w[i] for i in range(k) if blocks[i] <= A), Fraction(0))
                  for A in field}
            check(nu[X] == 1, "random state: nu(X) != 1")
            check(all(nu[A | B] == nu[A] + nu[B] for A, B in dis_pairs),
                  "random state: additivity fails")
            check(all(nu[A] <= nu[B] for A in field for B in field if A <= B),
                  "random state: monotonicity fails")
            check(all(nu[A | B] + nu[A & B] == nu[A] + nu[B] for A in field for B in field),
                  "random state: inclusion-exclusion fails")

print(f"r_dirac_finite_fields: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
