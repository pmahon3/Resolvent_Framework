#!/usr/bin/env python3
"""C7(i) + C7(iv) + grounding checks on the CANONICAL pentagon rep
(Omega = all 11 two-valued states).  From scratch."""
from itertools import combinations
from pentagon_core import (Rep, STATES, SYMBOLS, sval, inter, dirac)

checks = 0


def ck(b, msg):
    global checks
    checks += 1
    assert b, msg


rep = Rep(STATES)
ok, why = rep.valid()
ck(ok, why)  # injective + order-iso + complement/disjoint-union closed
             # + lattice + OM law: this grounds "canonical rep = pentagon"

# structure: 22 distinct elements; five blocks, each the 2^3 on 3 atoms;
# adjacent blocks share exactly one atom
ck(len(rep.F) == 22, 'element count 22 (0,1,10 atoms,10 coatoms)')
bls = rep.blocks()
ck(len(bls) == 5, 'exactly five blocks')
atom_sets = []
for B in bls:
    ck(len(B) == 8, 'each block is 2^3 (8 elements)')
    ats = Rep.block_atoms(B)
    ck(len(ats) == 3, 'three atoms per block')
    un = frozenset().union(*ats)
    ck(un == rep.U and sum(len(a) for a in ats) == len(rep.U),
       'block atoms partition Omega (pairwise disjoint, cover)')
    atom_sets.append(frozenset(ats))
share = 0
for i in range(5):
    for j in range(i + 1, 5):
        common = atom_sets[i] & atom_sets[j]
        ck(len(common) <= 1, 'blocks share at most one atom')
        share += len(common)
ck(share == 5, 'five adjacent pairs each sharing one atom')

# L0 cross-check on the whole family (finite instance of the assumed fact)
Fset = set(rep.F)
ct = rep.compat_table()
for X in rep.F:
    for Y in rep.F:
        c = ct[(X, Y)]
        ck(c == ((X & Y) in Fset), 'L0: A<->B iff A&B in L')
        if c:
            ck(rep.meet(X, Y) == (X & Y), 'L0: then meet = intersection')

# C7(iv) finite instance: every delta_w is a two-valued (sigma=)f.a. state
mus = rep.fa_states()
for w in rep.U:
    ck(dirac(rep, w) in mus, 'delta_w is an f.a. state')

# C7(i): EVERY two-valued f.a. state on the canonical rep is Dirac at its
# own point (the abstract state it corresponds to)
ck(len(mus) == 11, 'exactly 11 two-valued f.a. states on canonical rep')
for mu in mus:
    pts = [w for w in rep.U
           if all(mu[X] == (1 if w in X else 0) for X in rep.F)]
    ck(len(pts) == 1, 'each state is Dirac at exactly one point')
    w = pts[0]
    ck(all(mu[rep.imgs[s]] == sval(s, w) for s in SYMBOLS),
       'Dirac point = its own abstract state')
    # consequently: no coherent pattern/cluster has empty kernel here --
    # w lies in EVERY value-1 set, hence in cap(V) for every V
    for X in rep.F:
        if mu[X] == 1:
            ck(w in X, 'kernel point lies in every value-1 set')

# explicit scan: no three value-1 elements of any state have pairwise
# nonempty intersections with empty triple intersection (the C6/C7(ii)
# configuration is IMPOSSIBLE on the canonical rep)
cfg = 0
for mu in mus:
    V1 = [X for X in rep.F if mu[X] == 1 and X != rep.U]
    for A1, A2, A3 in combinations(V1, 3):
        if (A1 & A2) and (A1 & A3) and (A2 & A3) and not (A1 & A2 & A3):
            cfg += 1
    checks += len(list(combinations(V1, 3)))
ck(cfg == 0, 'no empty-kernel triple configuration on canonical rep')

print(f'PASS check_canonical_c7i: {checks} checks')
