#!/usr/bin/env python3
"""Claim P arithmetic step (from scratch, s13 proof-read).

Given the P0 decomposition mu = sum_i a_i delta_{x_i} + c*nu on the
ctble/co-ctble field, x a designated point (either a fresh non-atom point of
the perfect kernel, or one of the atoms), F = X \\ {x}:

  - mu(F) = sum_{atoms != x} a_i + c   (F is co-countable);
  - every COUNTABLE K subseteq F has mu(K) = sum_{atoms in K} a_i;
  - CHECK: mu(K) <= mu(F) - c for all such K;
  - CHECK: sup over countable K subseteq F of mu(K) EQUALS mu(F) - c
    (so the (8.1) gap at F is exactly c, and (8.1)-with-only-countable-
    witnesses holds at F iff c = 0).

Exhaustive over: all K subseteq (atoms minus x); exact Fractions; both an
exhaustive small weight grid and random weight vectors.

NOT exercised (genuinely topological, feeds the premise "every compact
in-field K subseteq F is countable"): compact => closed in Hausdorff; every
closed co-countable subset of Polish X contains the perfect kernel P;
Cantor-Bendixson (P nonempty for uncountable Polish X); x in P load-bearing
(if x were isolated, e.g. X = [0,1] disjoint-union {p}, x = p, then
K = [0,1] is a compact co-countable in-field subset of F and the premise
fails).
"""
import sys, itertools, random
from fractions import Fraction

random.seed(1313)
PASS = 0
FAIL = 0
def check(cond, msg):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print("FAIL:", msg)

def run_instance(a, c, x_is_atom, x_idx=None):
    """a: list of Fractions (atom masses), c: diffuse mass; sum(a)+c == 1."""
    m = len(a)
    atoms_in_F = [i for i in range(m) if not (x_is_atom and i == x_idx)]
    mu_F = sum((a[i] for i in atoms_in_F), Fraction(0)) + c
    best = Fraction(0)
    for r in range(len(atoms_in_F) + 1):
        for K in itertools.combinations(atoms_in_F, r):
            mu_K = sum((a[i] for i in K), Fraction(0))
            check(mu_K <= mu_F - c, f"mu(K) > mu(F)-c: K={K} a={a} c={c}")
            if mu_K > best:
                best = mu_K
    check(best == mu_F - c, f"sup mu(K) != mu(F)-c: a={a} c={c}")
    if c > 0:
        check(best < mu_F, "gap not strict although c > 0")
    else:
        check(best == mu_F, "gap present although c = 0")

# exhaustive grid: m = 2 atoms, denominators 6
D = 6
for i in range(D + 1):
    for j in range(D + 1 - i):
        l = D - i - j
        a = [Fraction(i, D), Fraction(j, D)]
        c = Fraction(l, D)
        run_instance(a, c, x_is_atom=False)
        run_instance(a, c, x_is_atom=True, x_idx=0)
        run_instance(a, c, x_is_atom=True, x_idx=1)

# random instances, m up to 6
for _ in range(200):
    m = random.randint(1, 6)
    w = [Fraction(random.randint(0, 9)) for _ in range(m + 1)]
    if sum(w) == 0:
        w[0] = Fraction(1)
    s = sum(w)
    w = [x / s for x in w]
    a, c = w[:m], w[m]
    if random.random() < 0.5:
        run_instance(a, c, x_is_atom=False)
    else:
        run_instance(a, c, x_is_atom=True, x_idx=random.randrange(m))

print(f"p_arithmetic_gap: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
