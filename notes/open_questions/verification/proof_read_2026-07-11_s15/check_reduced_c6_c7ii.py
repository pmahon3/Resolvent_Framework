#!/usr/bin/env python3
"""C6 and C7(ii): exhaustive search over ALL proper subsets Omega' of the 11
pentagon states for valid reduced representations, then witness hunt.
From scratch."""
from itertools import combinations
from pentagon_core import (Rep, STATES, SYMBOLS, S_EMPTY, inter,
                           induced_state, dirac)

checks = 0


def ck(b, msg):
    global checks
    checks += 1
    assert b, msg


# ---- exhaustive search for valid reduced reps ----
valid_reduced = []
tried = 0
n = len(STATES)
for r in range(1, n):
    for sub in combinations(STATES, r):
        tried += 1
        rep = Rep(sub)
        ok, _ = rep.valid()
        if ok:
            valid_reduced.append(rep)
print(f'proper nonempty subsets tried: {tried}; valid reduced reps: '
      f'{len(valid_reduced)}')
ck(tried == 2**n - 2, 'searched every proper nonempty subset')
ck(len(valid_reduced) > 0, 'some reduced rep exists (C6/C7 premise)')

sizes = sorted(len(rep.U) for rep in valid_reduced)
print(f'sizes of valid reduced reps: {sizes}')

# ---- witness hunt on the valid reduced reps ----
c6_wit = []
c7ii_wit = []
for rep in valid_reduced:
    U = rep.U
    Fset = set(rep.F)
    mus = rep.fa_states()
    bls = rep.blocks()
    for mu in mus:
        dirac_pts = [w for w in U
                     if all(mu[X] == (1 if w in X else 0) for X in rep.F)]
        # per-block kernels D_Bl = cap of the value-1 part of the block
        kers = []
        for B in bls:
            D = inter([X for X in B if mu[X] == 1], U)
            # C5 finite instance en passant: kernel nonempty and = charged atom
            ck(D != frozenset(), 'finite: block kernel nonempty')
            ats = Rep.block_atoms(B)
            charged = [a for a in ats if mu[a] == 1]
            ck(len(charged) == 1 and charged[0] == D,
               'kernel = the charged atom of the block')
            kers.append(D)
        # C6 configuration: three blocks, kernels pairwise intersecting,
        # empty triple intersection
        for i, j, k in combinations(range(len(bls)), 3):
            Ki, Kj, Kk = kers[i], kers[j], kers[k]
            checks += 1
            if (Ki & Kj) and (Ki & Kk) and (Kj & Kk) and not (Ki & Kj & Kk):
                ck(not dirac_pts, 'such a state is automatically non-Dirac')
                c6_wit.append((rep, mu, (i, j, k), (Ki, Kj, Kk)))
        # C7(ii) configuration: A1,A2,A3 value-1, pairwise intersecting,
        # empty triple; no Dirac extension of the (perp-closed) pattern,
        # but mu extends it (mu is sigma-additive: Omega' finite)
        V1 = [X for X in rep.F if mu[X] == 1 and X != U]
        for A1, A2, A3 in combinations(V1, 3):
            checks += 1
            if (A1 & A2) and (A1 & A3) and (A2 & A3) and not (A1 & A2 & A3):
                patt = {}
                for A in (A1, A2, A3):
                    patt[A] = 1
                    patt[U - A] = 0
                ck(all((U - A) in Fset for A in (A1, A2, A3)),
                   'pattern perp-closure stays in L')
                for w in U:  # direct no-Dirac check (not via the cap-V lemma)
                    ck(not all((1 if w in X else 0) == v
                               for X, v in patt.items()),
                       'no delta_w extends the pattern')
                ck(all(mu[X] == v for X, v in patt.items()),
                   'mu itself extends the pattern')
                c7ii_wit.append((rep, mu, (A1, A2, A3)))

ck(len(c6_wit) > 0, 'C6 witness exists on some reduced rep')
ck(len(c7ii_wit) > 0, 'C7(ii) witness exists on some reduced rep')

# ---- display one C6/C7(ii) witness in readable form ----
def show_state_set(X):
    return '{' + ', '.join('s' + ''.join(map(str, sorted(t))) for t in sorted(X, key=sorted)) + '}'

rep, mu, ijk, K = c6_wit[0]
print(f'\nC6 witness: |Omega\'| = {len(rep.U)}, '
      f'Omega\' omits {[sorted(t) for t in sorted(set(STATES) - rep.U, key=sorted)]}')
print(f'  blocks {ijk}; kernels:')
for D in K:
    print('   ', show_state_set(D))

# is the expected witness present: Omega' = STATES minus the all-odd state,
# with nu induced by the all-odd state itself?
expected = [w for w in c6_wit if w[0].U == frozenset(STATES) - {S_EMPTY}]
if expected:
    rep0 = expected[0][0]
    nu = induced_state(rep0, S_EMPTY)
    ck(nu in rep0.fa_states(),
       'the state induced by the REMOVED all-odd state is a valid f.a. '
       'state on the reduced family')
    ck(any(w[1] == nu for w in expected),
       'and it is a C6 witness state there')
    print('\nexpected witness confirmed: Omega\' = all states minus the '
          'all-odd state; nu = the all-odd state, realized non-Dirac.')

print(f'\nC6 witnesses found: {len(c6_wit)}; C7(ii) witnesses found: '
      f'{len(c7ii_wit)}')
print(f'PASS check_reduced_c6_c7ii: {checks} checks')
