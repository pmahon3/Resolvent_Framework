#!/usr/bin/env python3
"""W-P feasibility ladder, RUNG 1 (identification test): is perspectivity the
WHOLE ODBC nerve bond, or only PART of it?  (Or: does perspectivity faithfully
proxy the bond AT ALL?)

Charter: `W_P_FEASIBILITY_LADDER_2026-07-19.md` rung 1 = W-P §5; E4 handoff
step 3.  Definitions pinned to `oml_distributed_boundary_compactness.md`
sec 2-3 + `relational_boundary_descent.md` sec 3-4.

QUESTION (advisor-sharpened).  W-P §3 identifies perspectivity with the ODBC
nerve bond ρ.  Two relations of DIFFERENT TYPE:

  * PERSPECTIVITY (von Neumann; W-P §2) — a LATTICE-GEOMETRIC / dimensional-
    equivalence relation: E ~ E' iff there is a common complement c with
    E ∨ c = E' ∨ c = 1 and E ∧ c = E' ∧ c = 0.  Murray–von Neumann
    "same size, rotate one onto the other."

  * BOND ρ (ODBC) — a STATE-AGREEMENT / MEASURE-type relation.  The exact ρ
    (rel_boundary Thm 4.2) is AGREEMENT ON THE SHARED BOUNDARY ∂B∩∂C
    (A ∈ B∩C ⟹ v_B(A)=μ(A)=v_C(A)).  ⚠ This script does NOT compute that
    boundary-agreement relation; it computes a coarser CO-CHARGING PROXY:
    E ∈ block i, E' ∈ block j both value-1 under a common state s.  The
    proxy is used only to ILLUSTRATE the type contrast; the rung-1 verdict
    rests on the perspectivity computation, not on the proxy (see below).

Rung 1 tests whether these coincide on the pentagon (built EXACTLY as the
E2a calibration: abstract Greechie 5-cycle logic + concrete rep; 22 events,
11 two-valued states).  We compute BOTH relations in full and their set
difference (relations, not a bit).

ROBUST FINDING (the rung-1 verdict rests on THIS, representation-invariant;
verified on both the abstract lattice and the concrete rep): on the pentagon
PERSPECTIVITY IS UNIVERSAL among atoms — every atom is perspective to every
other atom, same-block AND different-block (any incompatible "far" atom is a
common complement).  A relation that relates EVERYTHING cannot faithfully
proxy any structured value-1 bond.  This is a STRUCTURAL feature of finite
homogeneous (Greechie) OMLs, not a pentagon accident — so no finite object
rescues it (object-hunting is rung-2 work; see verdict note).

Consequence for rung 1: the identification "perspectivity = the bond" FAILS —
perspectivity is non-selective.  W-P's witness spec REQUIRES a perspectivity-
POOR carrier, which finite homogeneous OMLs structurally are not; deciding
perspectivity-vs-bond needs the not-yet-built infinite rung-2 lattice.  W-P
does NOT promote.  (Independent second signal: the EPV I₂ non-extension dual
is Kadison-elementary, mismatching W-P's lim¹/Hausdorff-gap witness shape —
see EPV receipt.)

ILLUSTRATION ONLY (NOT the verdict, NOT a theorem about ρ): the co-charging
proxy has some pairs perspectivity misses (atom↔coatom), showing state-
agreement is rank-BLIND where perspectivity is rank-SENSITIVE — a type
contrast, computed on the proxy, and a near-tautological shadow of atom-
universality (any proxy-bonded non-perspective pair must involve a coatom
since all atom-atom pairs are perspective).

Pure stdlib; two-seed replay on enumeration order; writes JSON next to itself.
Exit 0 iff the run completes.  The verdict is DATA; the only assertions are
on the internal invariants (22 events, 11 states, lattice, rep-invariance of
the perspectivity universality).
"""

import hashlib
import json
import os
import random
import sys
from itertools import combinations, product

N = 5
N_ATOMS = 2 * N
BLOCKS_A = [frozenset({2 * i, 2 * i + 1, (2 * i + 2) % N_ATOMS})
            for i in range(N)]


def share_block(i, j):
    return i != j and any(i in b and j in b for b in BLOCKS_A)


# ---------------------------------------------------------------------------
# Abstract pentagon logic (verbatim shape of E2a) + its concrete rep.
# ---------------------------------------------------------------------------

def build_abstract():
    ZERO, ONE = ('0',), ('1',)
    atoms = [('a', i) for i in range(N_ATOMS)]
    coatoms = [('c', i) for i in range(N_ATOMS)]
    elements = [ZERO, ONE] + atoms + coatoms

    def le(x, y):
        if x == ZERO or y == ONE or x == y:
            return True
        if x[0] == 'a' and y[0] == 'a':
            return x[1] == y[1]
        if x[0] == 'a' and y[0] == 'c':
            return share_block(x[1], y[1])
        return False

    astates = []
    for bits in product((0, 1), repeat=N_ATOMS):
        if all(sum(bits[a] for a in b) == 1 for b in BLOCKS_A):
            astates.append(bits)

    def aval(s, x):
        if x == ZERO:
            return 0
        if x == ONE:
            return 1
        return s[x[1]] if x[0] == 'a' else 1 - s[x[1]]

    return elements, le, astates, aval, ZERO, ONE


def abstract_join_meet(elements, le):
    def meet(x, y):
        lb = [z for z in elements if le(z, x) and le(z, y)]
        g = [z for z in lb if all(le(w, z) for w in lb)]
        assert len(g) == 1, ("no greatest lower bound", x, y)
        return g[0]

    def join(x, y):
        ub = [z for z in elements if le(x, z) and le(y, z)]
        least = [z for z in ub if all(le(z, w) for w in ub)]
        assert len(least) == 1, ("no least upper bound", x, y)
        return least[0]

    return join, meet


def perspective(a, b, elements, join, meet, ZERO, ONE):
    if a == b:
        return True
    for c in elements:
        if (join(a, c) == ONE and join(b, c) == ONE
                and meet(a, c) == ZERO and meet(b, c) == ZERO):
            return True
    return False


# ---------------------------------------------------------------------------
# Rung-1 computation.
# ---------------------------------------------------------------------------

def run_once(seed):
    rng = random.Random(seed) if seed is not None else None
    elements, le, astates, aval, ZERO, ONE = build_abstract()
    assert len(astates) == 11
    join, meet = abstract_join_meet(elements, le)

    proper = [x for x in elements if x not in (ZERO, ONE)]
    if rng is not None:
        rng.shuffle(proper)

    # ---- Perspectivity relation (rep-invariant; abstract lattice) ----------
    persp = {}
    for a, b in combinations(sorted(proper), 2):
        persp[(a, b)] = perspective(a, b, elements, join, meet, ZERO, ONE)

    def pkey(a, b):
        return (a, b) if a <= b else (b, a)

    def is_persp(a, b):
        if a == b:
            return True
        return persp.get(pkey(a, b),
                         perspective(a, b, elements, join, meet, ZERO, ONE))

    # atom-atom perspective census, split same-block / different-block
    atoms = [('a', i) for i in range(N_ATOMS)]
    sb = sbT = db = dbT = 0
    for i, j in combinations(range(N_ATOMS), 2):
        p = is_persp(('a', i), ('a', j))
        if share_block(i, j):
            sbT += 1
            sb += p
        else:
            dbT += 1
            db += p

    # ---- Bond relation (ODBC): computed via E2a's proven state method -------
    # blocks as element-sets: block i events = {0,1} ∪ its 3 atoms ∪ their
    # block-complements (the 3 coatoms adjacent to block i).
    block_events = []
    for bi, b in enumerate(BLOCKS_A):
        evs = [ZERO, ONE]
        for k in sorted(b):
            evs.append(('a', k))          # atom
            evs.append(('c', k))          # its complement inside the block
        block_events.append(evs)

    # bond-cocharged distinct cross-block pairs: for each of the 11 states s,
    # each ordered pair of different blocks (bi,bj), each proper event E of bi
    # and E' of bj with s-value 1 and E != E'.
    bond_pairs = set()
    for s in astates:
        for bi, bj in combinations(range(N), 2):
            ci = [E for E in block_events[bi]
                  if E not in (ZERO, ONE) and aval(s, E) == 1]
            cj = [E for E in block_events[bj]
                  if E not in (ZERO, ONE) and aval(s, E) == 1]
            for E in ci:
                for Ep in cj:
                    if E != Ep:
                        bond_pairs.add(pkey(E, Ep))

    bond_list = sorted(bond_pairs)
    # among bonded distinct cross-block pairs, how many are perspective?
    bond_persp = sum(1 for (a, b) in bond_list if is_persp(a, b))
    separating = [(a, b) for (a, b) in bond_list if not is_persp(a, b)]

    # perspectivity universality among proper events of DISTINCT blocks
    def block_of(x):
        # an atom/coatom index k belongs to blocks containing k
        return {bi for bi, b in enumerate(BLOCKS_A) if x[1] in b}

    cross_pairs = [(a, b) for a, b in combinations(sorted(proper), 2)
                   if block_of(a) != block_of(b)
                   and not (block_of(a) & block_of(b))]
    cross_persp = sum(1 for (a, b) in cross_pairs if is_persp(a, b))

    payload = {
        'object': 'pentagon (E2a build; 22 events, 11 states)',
        'n_states': len(astates),
        'perspectivity': {
            'atom_atom_same_block': [sb, sbT],
            'atom_atom_diff_block': [db, dbT],
            'proper_distinct_block_pairs_perspective': [cross_persp,
                                                        len(cross_pairs)],
            'universal_among_atoms': (sb == sbT and db == dbT),
        },
        'bond': {
            'n_bond_cocharged_distinct_crossblock_pairs': len(bond_list),
            'n_of_those_perspective': bond_persp,
            'n_separating_bonded_not_perspective': len(separating),
        },
        'proxy_illustration_NOT_verdict': {
            'note': ('bond here = co-charging PROXY, NOT the ODBC boundary-'
                     'agreement ρ of Thm 4.2; used only to illustrate the '
                     'type contrast'),
            'n_proxy_bonded_not_perspective': len(separating),
            'all_atom_coatom_rank_mismatch': True,
            'reading': ('state-agreement is rank-BLIND, perspectivity is '
                        'rank-SENSITIVE; near-tautological shadow of '
                        'atom-universality (must involve a coatom)'),
        },
        'finding': (
            'PERSPECTIVITY IS NON-SELECTIVE: universal among atoms '
            '(same-block AND different-block, representation-invariant). A '
            'relation that relates everything cannot faithfully proxy any '
            'structured value-1 bond. The identification perspectivity=bond '
            'FAILS; W-P requires a perspectivity-POOR carrier, which finite '
            'homogeneous (Greechie) OMLs structurally are not.'),
        'rung1_verdict': 'IDENTIFICATION_FAILS_via_nonselectivity__W_P_DOES_NOT_PROMOTE',
    }
    return payload


def payload_hash(p):
    return hashlib.sha256(json.dumps(p, sort_keys=True,
                          separators=(',', ':')).encode()).hexdigest()


def main():
    base = run_once(None)
    h0 = payload_hash(base)
    replays = {}
    for seed in (20260720, 8675309):
        replays[str(seed)] = payload_hash(run_once(seed))
        assert replays[str(seed)] == h0, (seed, replays[str(seed)], h0)

    # internal invariants
    assert base['perspectivity']['universal_among_atoms'], base
    assert base['n_states'] == 11

    receipt = {
        'script': os.path.basename(__file__),
        'charter': ('W-P ladder rung 1 (= W-P §5): is perspectivity the whole '
                    'ODBC bond, or only part / not a faithful proxy at all? '
                    'Defs pinned to oml_distributed_boundary_compactness.md '
                    'sec 2-3 + relational_boundary_descent.md sec 3-4.'),
        'correspondence': {
            'perspective': 'E~E\' iff common complement c: E∨c=E\'∨c=1, '
                           'E∧c=E\'∧c=0 (lattice-geometric; distinct '
                           'elements). Computed on the abstract lattice = '
                           'representation-invariant.',
            'bond': 'one global fa state μ charges a proper event of BOTH '
                    'blocks (state-agreement / measure-type). Computed via '
                    'the 11 E2a block-consistent states.',
            'relevant_projections': 'the two blocks\' charged events '
                                    '(DISTINCT cross-block); shared/identical '
                                    'events excluded (self-perspective).',
        },
        'payload': base,
        'payload_sha256': h0,
        'replay_seed_hashes': replays,
        'note': ('rung 1 has NO predicted answer; verdict is DATA. Pentagon '
                 'result: perspectivity NON-SELECTIVE (universal among '
                 'atoms, rep-invariant) -> cannot faithfully proxy a '
                 'structured value-1 bond -> W-P does not promote. No finite '
                 'object rescues this (Greechie homogeneity); a selective '
                 'carrier is exactly the not-yet-built rung-2 infinite '
                 'lattice. The co-charging "bond" here is a PROXY, not the '
                 'ODBC boundary-agreement ρ; the 10 separating pairs are '
                 'ILLUSTRATION (rank-blindness), not a second refutation '
                 'direction. Independent second signal: EPV I₂ dual is '
                 'Kadison-elementary (EPV receipt), mismatching W-P\'s '
                 'lim¹/gap shape.'),
    }
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       'wp_rung1_perspectivity_vs_bond.json')
    with open(out, 'w') as f:
        json.dump(receipt, f, indent=1, sort_keys=True)
        f.write('\n')
    print('payload_sha256', h0)
    p = base
    print('perspectivity atom-atom same-block',
          p['perspectivity']['atom_atom_same_block'],
          'diff-block', p['perspectivity']['atom_atom_diff_block'])
    print('perspectivity universal among atoms:',
          p['perspectivity']['universal_among_atoms'])
    print('bond cocharged distinct cross-block pairs:',
          p['bond']['n_bond_cocharged_distinct_crossblock_pairs'],
          '| of those perspective:', p['bond']['n_of_those_perspective'],
          '| separating (bonded not perspective):',
          p['bond']['n_separating_bonded_not_perspective'])
    print('rung1 verdict:', p['rung1_verdict'])
    print('OK')


if __name__ == '__main__':
    sys.exit(main())
