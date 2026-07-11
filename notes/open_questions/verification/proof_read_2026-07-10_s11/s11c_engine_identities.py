#!/usr/bin/env python3
"""Fresh-context adversarial re-derivation, receipt (c): the set-theoretic
engine identities used by A2 and T3, plus T3 on random finite sigma-fields.

Checks:
  1. Decreasing-intersection identity (A2):
       for decreasing F_1 >= F_2 >= ... :  cap_n F_n = F_1 \\ U_n (F_n \\ F_{n+1})
     fuzzed over random decreasing sequences.
  2. T3's disjoint decomposition:  F_1 = D  |_|  |_|_n (F_n \\ F_{n+1}),
     pieces pairwise disjoint (fuzzed, same sequences).
  3. T3 on random finite sigma-fields on a 10-point universe:
     random generating families; every two-valued additive state nu:
       - exactly one of nu(G), nu(G^c) is 1
       - F_n = intersection of value-1 sides has nu(F_n) = 1
       - D = cap F_n is nonempty, nu(D) = 1
       - {A : D <= A or D cap A = 0} is a field containing the generators
         hence everything
       - nu = delta_w restricted to the field, for EVERY w in D
  4. The 'S is a sigma-subfield' argument of T3 (complement + union closure
     of {A : D <= A or D cap A = 0}) checked directly on the same fields.
"""
import random
import sys
from itertools import combinations

random.seed(20260710)
fails = []
def check(name, cond, detail=""):
    print(("PASS: " if cond else "FAIL: ") + name + (f" [{detail}]" if detail else ""))
    if not cond:
        fails.append(name)

U = frozenset(range(12))

# ---- 1 & 2: decreasing-intersection identities ----
ok1 = ok2 = True
for trial in range(500):
    F = [frozenset(x for x in U if random.random() < 0.8)]
    for _ in range(7):
        F.append(frozenset(x for x in F[-1] if random.random() < 0.75))
    D = frozenset.intersection(*F)
    diffs = [F[k] - F[k + 1] for k in range(len(F) - 1)]
    if D != F[0] - frozenset().union(*diffs):
        ok1 = False
    pieces = diffs + [D]
    if frozenset().union(*pieces) != F[0]:
        ok2 = False
    for P, Q in combinations(pieces, 2):
        if P & Q:
            ok2 = False
check("A2 identity: cap F_n = F_1 \\ U(F_n \\ F_n+1) for decreasing F (500 fuzz)", ok1)
check("T3 decomposition: F_1 = D disjoint-union of the differences (500 fuzz)", ok2)

# ---- 3 & 4: T3 on random finite sigma-fields ----
V = list(range(10))
ok_side = ok_F = ok_D = ok_S = ok_dirac = True
for trial in range(200):
    # random partition of V into atoms
    k = random.randint(2, 6)
    labels = [random.randrange(k) for _ in V]
    atoms = [frozenset(v for v in V if labels[v] == lab) for lab in set(labels)]
    # the sigma-field: all unions of atoms
    field = set()
    for mask in range(1 << len(atoms)):
        field.add(frozenset().union(*([frozenset()] +
                  [atoms[i] for i in range(len(atoms)) if (mask >> i) & 1])))
    field = sorted(field, key=lambda s: (len(s), sorted(s)))
    W = frozenset(V)
    # random generating family: keep adding random members until the
    # generated field is everything
    gens = []
    def gen_field(gs):
        Fm = {frozenset(), W} | set(gs)
        changed = True
        while changed:
            changed = False
            for S in list(Fm):
                if (W - S) not in Fm: Fm.add(W - S); changed = True
            for S in list(Fm):
                for T in list(Fm):
                    if (S & T) not in Fm: Fm.add(S & T); changed = True
        return Fm
    while gen_field(gens) != set(field):
        gens.append(random.choice(field))
    # every two-valued additive state = atom indicator
    for a_sel in atoms:
        nu = {S: int(a_sel <= S) for S in field}
        Fn = W
        for G in gens:
            if nu[G] + nu[W - G] != 1:
                ok_side = False
            side = G if nu[G] == 1 else W - G
            Fn = Fn & side
            if nu.get(Fn, None) != 1:
                ok_F = False
        D = Fn
        if not D or nu[D] != 1:
            ok_D = False
        S_fam = {A for A in field if D <= A or not (D & A)}
        if S_fam != set(field):
            ok_S = False
        for A in S_fam:
            if (W - A) not in S_fam:
                ok_S = False
        for A, Bb in combinations(S_fam, 2):
            if (A | Bb) in field and (A | Bb) not in S_fam:
                ok_S = False
        for w in D:
            if any(nu[A] != int(w in A) for A in field):
                ok_dirac = False
check("T3: nu two-valued => exactly one side of each generator has value 1", ok_side)
check("T3: nu(F_n) = 1 all along the intersection chain", ok_F)
check("T3: D nonempty with nu(D) = 1", ok_D)
check("T3: {A : D <= A or D cap A = 0} is complement/union-closed and = whole field", ok_S)
check("T3: nu = delta_w on the field for EVERY w in D", ok_dirac)

print()
print("ALL CHECKS PASS" if not fails else f"{len(fails)} FAILURES")
sys.exit(len(fails))
