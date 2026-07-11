#!/usr/bin/env python3
"""Claim C logical steps that are finitely instantiable (from scratch, s13).

(A) EQUIVALENCE of the two readings of "non-principal" for a two-valued f.a.
    state nu on a field A over X:
       (exists omega in X: nu = delta_omega restricted to A)
       <=>  intersection of {F in A : nu(F) = 1} is nonempty,
    and the set of representing omega EQUALS that intersection.
    Checked exhaustively over all fields (= partitions) on |X| <= 4 and all
    two-valued f.a. states on them.  Also demonstrates the coarseness
    subtlety: on a field whose minimal measure-one element is a block of
    size >= 2, the representing omega is NON-unique (so "non-principal" must
    be read as "not delta_omega RESTRICTED TO the field, for any omega").

(B) THRESHOLD LEMMA used in C's P-leg reduction: in the truncated
    ctble/co-ctble model with decomposition mu = sum a_i delta_i + c*flag,
    for every element K with countable flag: mu(K) <= 1 - c; and for every
    co-countable F and K <= F with mu(K) > mu(F) - c, K is co-flagged.
    (This is the arithmetic behind: "(8.1) for mu with diffuse mass c > 0
    forces (8.1) for the two-valued co-countable component", whose
    topological conclusion via Claim R is NOT finitely instantiable.)
"""
import sys, itertools, random
from fractions import Fraction

random.seed(13131)
PASS = 0
FAIL = 0
def check(cond, msg):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print("FAIL:", msg)

# ---------- (A) equivalence of non-principality readings ----------
def partitions(elems):
    if not elems:
        yield []
        return
    first, rest = elems[0], elems[1:]
    for p in partitions(rest):
        for i in range(len(p)):
            yield [blk | {first} if j == i else set(blk) for j, blk in enumerate(p)]
        yield [set(b) for b in p] + [{first}]

saw_nonunique_representative = False
for n in range(1, 5):
    X = frozenset(range(n))
    for part in partitions(list(range(n))):
        blocks = [frozenset(b) for b in part]
        k = len(blocks)
        field = sorted(
            {frozenset().union(*(blocks[i] for i in range(k) if mask >> i & 1))
             for mask in range(1 << k)},
            key=lambda s: (len(s), sorted(s)))
        idx = {A: i for i, A in enumerate(field)}
        dis_pairs = [(A, B) for A in field for B in field if not (A & B)]
        for bits in itertools.product((0, 1), repeat=len(field)):
            if bits[idx[X]] != 1:
                continue
            if any(bits[idx[A | B]] != bits[idx[A]] + bits[idx[B]]
                   for A, B in dis_pairs):
                continue
            nu = {A: bits[idx[A]] for A in field}
            reps = {w for w in X
                    if all((nu[F] == 1) == (w in F) for F in field)}
            core = X
            for A in field:
                if nu[A] == 1:
                    core = core & A
            check(reps == core, f"representing set != intersection of 1-sets (n={n})")
            check((len(reps) > 0) == (len(core) > 0), "equivalence of readings fails")
            if len(reps) >= 2:
                saw_nonunique_representative = True
check(saw_nonunique_representative,
      "never saw a coarse field with non-unique delta representative")

# ---------- (B) threshold lemma in the truncated ctble/co-ctble model ----------
for m in range(1, 5):
    NAMED = frozenset(range(m))
    field = [(frozenset(S), f)
             for r in range(m + 1)
             for S in itertools.combinations(range(m), r)
             for f in (0, 1)]
    def leq(e, g):
        return e[0] <= g[0] and e[1] <= g[1]
    for _ in range(40):
        w = [Fraction(random.randint(0, 8)) for _ in range(m + 1)]
        if sum(w) == 0:
            w[-1] = Fraction(1)
        s = sum(w)
        w = [x / s for x in w]
        a, c = w[:m], w[m]
        def mu(e):
            return sum((a[i] for i in e[0]), Fraction(0)) + (c if e[1] else 0)
        for K in field:
            if K[1] == 0:
                check(mu(K) <= 1 - c, f"countable K with mu(K) > 1-c: {K}")
        for F in field:
            if F[1] != 1:
                continue
            for K in field:
                if leq(K, F) and mu(K) > mu(F) - c:
                    check(K[1] == 1,
                          f"K <= F with mu(K) > mu(F)-c but K countable-flagged: {K} {F}")

print(f"c_nonprincipal_equiv: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
