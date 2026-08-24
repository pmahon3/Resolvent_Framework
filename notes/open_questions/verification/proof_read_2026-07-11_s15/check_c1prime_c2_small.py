#!/usr/bin/env python3
"""C1' and monotonicity on ALL concrete sigma-classes over |Omega| in
{2,3,4}: families containing 0, Omega, closed under complement and disjoint
union -- including NON-lattice ones (C1' claims no lattice hypothesis is
needed; the derivation of C2 below in fact needs none either).
From scratch."""
from itertools import combinations, product

checks = 0


def ck(b, msg):
    global checks
    checks += 1
    assert b, msg


def sigma_classes(n):
    U = frozenset(range(n))
    subsets = [frozenset(s) for r in range(n + 1)
               for s in combinations(range(n), r)]
    pairs, seen = [], set()
    for X in subsets:
        if X in seen or X == frozenset() or X == U:
            continue
        seen.add(X)
        seen.add(U - X)
        pairs.append((X, U - X))
    out = []
    for bits in product((0, 1), repeat=len(pairs)):
        F = {frozenset(), U}
        for b, (X, Y) in zip(bits, pairs):
            if b:
                F.add(X)
                F.add(Y)
        good = True
        for X in F:
            for Y in F:
                if not (X & Y) and (X | Y) not in F:
                    good = False
                    break
            if not good:
                break
        if good:
            out.append((U, frozenset(F)))
    return out


def fa_states(U, F):
    """All two-valued f.a. states: full disjoint-subfamily additivity."""
    Fs = sorted(F, key=lambda X: (len(X), sorted(X)))
    nz = [X for X in Fs if X]
    cons = []

    def rec(start, chosen, un):
        if len(chosen) >= 2 and un in F:
            cons.append((tuple(chosen), un))
        for i in range(start, len(nz)):
            Xi = nz[i]
            if un & Xi:
                continue
            rec(i + 1, chosen + [Xi], un | Xi)

    rec(0, [], frozenset())
    reps, seen = [], set()
    for X in Fs:
        if X in seen or X == frozenset() or X == U:
            continue
        seen.add(X)
        seen.add(U - X)
        reps.append(X)
    out = []
    for bits in product((0, 1), repeat=len(reps)):
        mu = {frozenset(): 0, U: 1}
        for b, X in zip(bits, reps):
            mu[X] = b
            mu[U - X] = 1 - b
        if all(sum(mu[X] for X in G) == mu[u] for G, u in cons):
            out.append(mu)
    return out


def is_lattice(U, F):
    Fs = list(F)
    for X in Fs:
        for Y in Fs:
            lbs = [Z for Z in Fs if Z <= X and Z <= Y]
            g = max(lbs, key=len)
            if not all(Z <= g for Z in lbs):
                return False
            ubs = [Z for Z in Fs if X <= Z and Y <= Z]
            l = min(ubs, key=len)
            if not all(l <= Z for Z in ubs):
                return False
    return True


families = 0
nonlattice = 0
for n in (2, 3, 4):
    for U, F in sigma_classes(n):
        families += 1
        latt = is_lattice(U, F)
        if not latt:
            nonlattice += 1
        for mu in fa_states(U, F):
            V1 = [X for X in F if mu[X] == 1]
            # C1': |V| <= 2 -> common point (no lattice hypothesis)
            for X in V1:
                ck(X != frozenset(), "C1' size 1: value-1 set nonempty")
            for X, Y in combinations(V1, 2):
                ck(X & Y != frozenset(), "C1' size 2: value-1 pair intersects")
            # monotonicity holds on EVERY sigma-class (lattice or not):
            # mu(E)=1, mu(A)=0, E<=A would give mu(E)+mu(Ac)=2 on E u Ac in F
            for X in F:
                for Y in F:
                    if X <= Y:
                        ck(mu[X] <= mu[Y], 'monotonicity on sigma-class')

print(f'sigma-classes checked: {families} (non-lattice among them: '
      f'{nonlattice}; at |Omega| <= 4 every such family is a lattice)')

# ---- targeted NON-lattice sigma-class: even-cardinality subsets of a
# 6-point set.  Closed under complement and disjoint union; NOT a lattice
# ({0,1} v {0,2} has three minimal upper bounds). ----
U6 = frozenset(range(6))
F6 = frozenset(frozenset(s) for r in (0, 2, 4, 6)
               for s in combinations(range(6), r))
for X in F6:
    ck((U6 - X) in F6, 'even-family complement-closed')
    for Y in F6:
        if not (X & Y):
            ck((X | Y) in F6, 'even-family disjoint-union closed')
ck(not is_lattice(U6, F6), 'even-family is NOT a lattice')

mus6 = fa_states(U6, F6)
ck(len(mus6) > 0, 'even-family has two-valued f.a. states')
for mu in mus6:
    V1 = [X for X in F6 if mu[X] == 1]
    for X in V1:
        ck(X != frozenset(), "C1' size 1 off-lattice")
    for X, Y in combinations(V1, 2):
        ck(X & Y != frozenset(), "C1' size 2 off-lattice")
    for X in F6:
        for Y in F6:
            if X <= Y:
                ck(mu[X] <= mu[Y], 'monotonicity off-lattice')
print(f'even-family f.a. states: {len(mus6)}')
print(f'PASS check_c1prime_c2_small: {checks} checks')
