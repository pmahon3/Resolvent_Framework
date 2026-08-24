#!/usr/bin/env python3
"""Finite instances of C1, C1', C2, C3, C5 and C12(ii) (T4) on pentagon
representations: the canonical rep plus valid reduced reps.  From scratch."""
from itertools import combinations
from pentagon_core import Rep, STATES, S_EMPTY, inter

checks = 0


def ck(b, msg):
    global checks
    checks += 1
    assert b, msg


def reduce_to_cluster(rep, mu, V, bls, ct, Fset):
    """C3(i)'s procedure: group V by blocks, take in-block meets, then merge
    compatible pairs until pairwise incompatible.  Instance-checks the
    ultrafilter fact and A2/L0 along the way."""
    U = rep.U
    groups = {}
    for X in V:
        bi = next(i for i, B in enumerate(bls) if X in B)
        groups.setdefault(bi, []).append(X)
    Es = []
    for bi, xs in groups.items():
        E = inter(xs, U)
        ck(E in Fset and E in bls[bi], 'in-block meet lands in the block')
        ck(mu[E] == 1, 'ultrafilter fact instance: in-block meet has value 1')
        if E not in Es:
            Es.append(E)
    changed = True
    while changed:
        changed = False
        for i in range(len(Es)):
            for j in range(i + 1, len(Es)):
                X, Y = Es[i], Es[j]
                if ct[(X, Y)]:
                    M = X & Y
                    ck(M in Fset, 'A2/L0 instance: compatible meet stays in L')
                    ck(mu[M] == 1, 'merge preserves value 1')
                    Es = [E for k, E in enumerate(Es) if k not in (i, j)]
                    if M not in Es:
                        Es.append(M)
                    changed = True
                    break
            if changed:
                break
    return Es


def run_on(rep, label, subset_cap=None):
    global checks
    U = rep.U
    Fset = set(rep.F)
    ct = rep.compat_table()
    bls = rep.blocks()
    blsets = [set(B) for B in bls]
    mus = rep.fa_states()
    atoms_of = [Rep.block_atoms(B) for B in bls]

    # C2 (monotonicity), every state, every comparable pair
    for X in rep.F:
        for Y in rep.F:
            if X <= Y:
                for mu in mus:
                    ck(mu[X] <= mu[Y], 'C2 monotonicity')

    # C5 finite instances: on finite Omega every f.a. state is sigma
    # (countable disjoint families are essentially finite), so C5 predicts:
    # every block kernel nonempty and equal to a charged atom.
    for mu in mus:
        for bi, B in enumerate(bls):
            D = inter([X for X in B if mu[X] == 1], U)
            ck(D != frozenset(), 'C5: block kernel nonempty (finite case)')
            charged = [a for a in atoms_of[bi] if mu[a] == 1]
            ck(len(charged) == 1 and charged[0] == D,
               'C5: kernel = the unique charged atom')

    # C1 / C1' / C3 over all value-1 subfamilies V (excluding U: it never
    # changes cap(V), blocks, or extensions)
    clusters = set()
    for mu in mus:
        V1 = [X for X in rep.F if mu[X] == 1 and X != U]
        idxs = range(len(V1))
        for rsize in range(1, len(V1) + 1):
            for c in combinations(idxs, rsize):
                V = [V1[i] for i in c]
                capV = inter(V, U)
                # C1': |V| <= 2 -> Dirac-rescued
                if len(V) <= 2:
                    ck(capV != frozenset(), "C1': |V|<=2 has a common point")
                # C1: V inside a union of two blocks -> Dirac-rescued
                twoblock = any(all((X in blsets[i]) or (X in blsets[j])
                                   for X in V)
                               for i in range(5) for j in range(i, 5))
                if twoblock:
                    ck(capV != frozenset(), 'C1: two-block V has a common point')
                # Dirac-extension lemma (delta_w extends s iff w in cap V),
                # checked directly on small patterns incl. the 0-part
                if len(V) <= 3:
                    patt = {}
                    okp = True
                    for A in V:
                        patt[A] = 1
                        if (U - A) in patt and patt[U - A] == 1:
                            okp = False
                        patt[U - A] = 0
                    if okp:
                        for w in U:
                            ext = all((1 if w in X else 0) == v
                                      for X, v in patt.items())
                            ck(ext == (w in capV),
                               'delta extends pattern iff point in cap V')
                # C3: reduce to cluster and check its advertised properties
                Es = reduce_to_cluster(rep, mu, V, bls, ct, Fset)
                for a in range(len(Es)):
                    for b in range(a + 1, len(Es)):
                        ck(not ct[(Es[a], Es[b])], 'C3: pairwise incompatible')
                        ck(Es[a] & Es[b] != frozenset(),
                           'C3: pairwise intersecting')
                ck(inter(Es, U) == capV, 'C3: cluster kernel = cap V')
                ck(all(mu[E] == 1 for E in Es), 'C3: mu = 1 on the cluster')
                if capV == frozenset():
                    ck(len(Es) >= 3, 'C3: not Dirac-rescued -> m >= 3')
                clusters.add(frozenset(Es))
            if subset_cap and checks > subset_cap:
                break

    # C12(ii) instance (T4 on finite Omega): for every cluster produced above
    # and every block, some atom of the block is jointly f.a.-coherent with it
    for cl in clusters:
        # keep only genuine clusters (mu == 1 on all elements for some mu):
        wits = [mu for mu in mus if all(mu[E] == 1 for E in cl)]
        if not wits:
            continue
        for bi in range(len(bls)):
            found = any(any(all(rho[E] == 1 for E in cl) and rho[D] == 1
                            for rho in mus)
                        for D in atoms_of[bi])
            ck(found, 'C12(ii)/T4: some atom of the block joins the cluster')

    print(f'  [{label}] |Omega|={len(U)}, f.a. states={len(mus)}, '
          f'clusters seen={len(clusters)}')


# canonical rep
canon = Rep(STATES)
ok, why = canon.valid()
ck(ok, why)
print('running canonical rep...')
run_on(canon, 'canonical')

# valid reduced reps (found by the same exhaustive criterion as in
# check_reduced_c6_c7ii; recomputed here independently)
reduced = []
for r in range(1, len(STATES)):
    for sub in combinations(STATES, r):
        rep = Rep(sub)
        if rep.valid()[0]:
            reduced.append(rep)
print(f'running {len(reduced)} valid reduced reps...')
for i, rep in enumerate(reduced):
    tag = 'reduced-' + str(i)
    if rep.U == frozenset(STATES) - {S_EMPTY}:
        tag += ' (= all minus all-odd state)'
    run_on(rep, tag)

print(f'PASS check_c1_c2_c3_c5_pentagon: {checks} checks')
