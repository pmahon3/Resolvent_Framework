#!/usr/bin/env python3
"""Claim P0 mechanics on finite truncations (from scratch, s13 proof-read).

Model of the ctble/co-ctble sigma-field truncated to m named points plus a
formal ideal element ("the uncountable remainder"): elements are pairs
(S, f) with S subseteq {0..m-1}, f in {0,1}; f=1 means "co-countable"
(contains the remainder). Complement (S,f) -> (S^c, 1-f); union componentwise
with OR; disjoint iff S cap T = empty AND not both co-flagged.

Checks:
  (1) field axioms on the model;
  (2) no two co-flagged elements are disjoint (the "at most one co-countable
      member in a disjoint family" case-split of P0's sigma-additivity check);
  (3) LINEAR-ALGEBRA verification that EVERY finitely additive assignment on
      the model is atom-determined: the nullspace of the full additivity
      constraint system has dimension exactly m+1 (atoms {i} and the remainder
      atom (empty,1)), and for every element e the relation
      r_e := nu(e) - sum_{atoms a <= e} nu(a) lies in the row space
      (checked as: r_e annihilates the nullspace). This is the finite content
      of P0: mu = sum a_i delta_{x_i} + c * nu with a_i = mu({x_i}),
      c = mu(remainder), nu = co-countable state (indicator of the flag).
  (4) exhaustive brute-force enumeration of all TWO-VALUED f.a. states on the
      model (m <= 3): each is delta at exactly one atom; count = m+1.
  (5) for random Fraction weight vectors (a, c): mu_{a,c} is a f.a. state and
      the decomposition identity holds on every element.

NOT exercised (genuinely infinite): countability of the atom set S of an
abstract measure (uses AC_omega(fin) in ZF for abstract X; eliminable when X
is linearly orderable, e.g. Polish), sigma-additivity over infinite disjoint
unions, and sigma-additivity of the co-countable state itself (countable
union of countable sets countable -- AC_omega).
"""
import sys, itertools, random
from fractions import Fraction

random.seed(131)
PASS = 0
FAIL = 0
def check(cond, msg):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print("FAIL:", msg)

def nullspace(rows, ncols):
    """Exact nullspace basis over Fraction via Gauss-Jordan."""
    mat = [list(map(Fraction, r)) for r in rows if any(x != 0 for x in r)]
    pivots = []
    r = 0
    for c in range(ncols):
        pr = next((i for i in range(r, len(mat)) if mat[i][c] != 0), None)
        if pr is None:
            continue
        mat[r], mat[pr] = mat[pr], mat[r]
        pv = mat[r][c]
        mat[r] = [x / pv for x in mat[r]]
        for i in range(len(mat)):
            if i != r and mat[i][c] != 0:
                f = mat[i][c]
                mat[i] = [a - f * b for a, b in zip(mat[i], mat[r])]
        pivots.append(c)
        r += 1
        if r == len(mat):
            break
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for fc in free:
        v = [Fraction(0)] * ncols
        v[fc] = Fraction(1)
        for i, pc in enumerate(pivots):
            v[pc] = -mat[i][fc] if fc < len(mat[i]) else Fraction(0)
        basis.append(v)
    return basis

for m in range(1, 5):
    NAMED = frozenset(range(m))
    field = [(frozenset(S), f)
             for r in range(m + 1)
             for S in itertools.combinations(range(m), r)
             for f in (0, 1)]
    field = sorted(set(field), key=lambda e: (len(e[0]), sorted(e[0]), e[1]))
    idx = {e: i for i, e in enumerate(field)}
    N = len(field)
    check(N == 2 ** (m + 1), f"model size wrong m={m}")

    def comp(e):
        return (NAMED - e[0], 1 - e[1])
    def union(e, g):
        return (e[0] | g[0], e[1] | g[1])
    def disjoint(e, g):
        return not (e[0] & g[0]) and not (e[1] and g[1])
    def leq(e, g):
        return e[0] <= g[0] and e[1] <= g[1]

    ONE = (NAMED, 1)
    ZERO = (frozenset(), 0)
    # (1) field axioms
    check(all(comp(e) in idx for e in field), "not complement-closed")
    check(all(union(e, g) in idx for e in field for g in field), "not union-closed")
    check(ONE in idx and ZERO in idx, "X or empty missing")
    # (2) two co-flagged elements never disjoint
    check(all(not disjoint(e, g) for e in field for g in field
              if e[1] == 1 and g[1] == 1), "two co-countable sets disjoint")

    atoms = [(frozenset([i]), 0) for i in range(m)] + [(frozenset(), 1)]
    dis_pairs = [(e, g) for e in field for g in field if disjoint(e, g)]

    # (3) additivity constraints -> atom-determined (finite P0)
    rows = []
    for e, g in dis_pairs:
        row = [Fraction(0)] * N
        row[idx[e]] += 1
        row[idx[g]] += 1
        row[idx[union(e, g)]] -= 1
        rows.append(row)
    basis = nullspace(rows, N)
    check(len(basis) == m + 1,
          f"nullspace dim {len(basis)} != m+1 = {m+1} (additivity constraints)")
    for e in field:
        r_e = [Fraction(0)] * N
        r_e[idx[e]] += 1
        for a in atoms:
            if leq(a, e):
                r_e[idx[a]] -= 1
        check(all(sum(x * y for x, y in zip(r_e, v)) == 0 for v in basis),
              f"element {e} not atom-determined by additivity")

    # (4) exhaustive two-valued states, m <= 3
    if m <= 3:
        states = []
        for bits in itertools.product((0, 1), repeat=N):
            if bits[idx[ONE]] != 1:
                continue
            ok = True
            for e, g in dis_pairs:
                if bits[idx[union(e, g)]] != bits[idx[e]] + bits[idx[g]]:
                    ok = False
                    break
            if ok:
                states.append(bits)
        check(len(states) == m + 1, f"two-valued state count {len(states)} != {m+1}")
        for bits in states:
            ones = [a for a in atoms if bits[idx[a]] == 1]
            check(len(ones) == 1, "two-valued state not concentrated on one atom")
            a = ones[0]
            check(all(bits[idx[e]] == (1 if leq(a, e) else 0) for e in field),
                  "two-valued state != delta at its atom")

    # (5) random weighted states: decomposition identity
    for _ in range(30):
        w = [Fraction(random.randint(0, 8)) for _ in range(m + 1)]
        if sum(w) == 0:
            w[-1] = Fraction(1)
        s = sum(w)
        w = [x / s for x in w]           # a_1..a_m, c
        a, c = w[:m], w[m]
        def mu(e):
            return sum((a[i] for i in e[0]), Fraction(0)) + (c if e[1] else 0)
        check(mu(ONE) == 1, "mu(X) != 1")
        check(all(mu(union(e, g)) == mu(e) + mu(g) for e, g in dis_pairs),
              "mu not finitely additive")
        # decomposition: atomic part + c * co-countable state (flag indicator)
        check(all(mu(e) == sum((a[i] for i in e[0]), Fraction(0)) + c * e[1]
                  for e in field), "decomposition identity fails")
        # coefficients recovered from mu itself
        check(all(mu((frozenset([i]), 0)) == a[i] for i in range(m))
              and mu((frozenset(), 1)) == c
              and sum(a) + c == 1, "coefficient recovery fails")

print(f"p0_decomposition_model: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
