#!/usr/bin/env python3
"""E2b: Psi-witness FIP locator (linearization/extension-screen seed §3).

The amended product-Ulam witness (papers/sigma_essential/witness_candidate/
sigma_essential_witness.md; Lean UlamWitnessMain.lean, psiAmended_ZFC) has
carrier Omega = M x {1,2,3,4} (M uncountable) and cores with fiber-trace
patterns A = 1100, B = 1010, C = 0110 -- i.e. A = M x {1,2}, B = M x {1,3},
C = M x {2,3} exactly (no countable perturbation on the cores as defined).
The witness state m (§6) is a two-valued finitely additive state on L with
m(A) = m(B) = m(C) = 1 (Lemma 6.2).

LOCATOR (direct -- the fallback of seed §3 E2b is NOT needed): the finite
value-1 family {A, B, C} has
    A cap B = M x {1},  A cap C = M x {2},  B cap C = M x {3}
(all nonempty, indeed full fibers), and
    A cap B cap C = EMPTY,
so m's value-1 family fails FIP at stage EXACTLY 3 -- minimal possible by
the pairwise lemma (E1-verified: disjoint value-1 pairs are impossible),
and |V| = 3 matches the s15 §11a optimality remark.  Hence the E-thread's
necessary condition (non-extendability) FIRES on the one known
sigma-essential state: m does not extend to any 0-1 f.a. measure on the
generated field, and lies outside closure(points).  (Independently
consistent with the note's Theorem 5.1 + 7.1(2): all sigma-states on L are
Dirac and K(s_0) = A cap B cap C = empty.)

Machine content of this receipt: the fiber-trace identities above are
verified exhaustively at the trace level ({0,1}^4 -- the fourth coordinate
tracks fiber 4), which is exact for the cores since they are unions of
full fibers: intersections of fiber-unions are computed fiberwise, and M
plays no role beyond nonemptiness.  Also verified: the pairwise lemma at
trace level (no two of A, B, C are disjoint), and stage minimality (no
2-subfamily has empty intersection).  Deterministic, no enumeration order,
two-seed replay trivially satisfied (recorded for protocol uniformity).
Pure stdlib.  Writes psi_witness_fip_locator.json.  Exit 0 iff all pass.
"""

import hashlib
import json
import os
import sys
from itertools import combinations

FIBERS = (1, 2, 3, 4)
CORES = {'A': frozenset({1, 2}), 'B': frozenset({1, 3}),
         'C': frozenset({2, 3})}
REPLAY_SEEDS = (20260719, 8675309)


def run_once():
    A, B, C = CORES['A'], CORES['B'], CORES['C']
    pairwise = {
        'A&B': sorted(A & B), 'A&C': sorted(A & C), 'B&C': sorted(B & C)}
    assert pairwise == {'A&B': [1], 'A&C': [2], 'B&C': [3]}
    assert all(v for v in pairwise.values()), "a pairwise intersection empty"
    triple = sorted(A & B & C)
    assert triple == [], "triple intersection nonempty: locator fails"
    solo = {n: sorted(CORES[n] - set().union(
        *(CORES[m] for m in CORES if m != n))) for n in CORES}
    assert solo == {'A': [], 'B': [], 'C': []}, solo
    outside = sorted(set(FIBERS) - (A | B | C))
    assert outside == [4]
    stages = {}
    fams = list(CORES.values())
    for k in (2, 3):
        stages[k] = sum(1 for c in combinations(fams, k)
                        if not frozenset.intersection(*c))
    assert stages[2] == 0 and stages[3] == 1, stages
    return {
        'cores_as_fiber_sets': {n: sorted(v) for n, v in CORES.items()},
        'pairwise_intersections': pairwise,
        'triple_intersection': triple,
        'solo_regions_empty': True,
        'complement_of_union': outside,
        'empty_intersections_by_stage': {str(k): v
                                         for k, v in stages.items()},
        'min_failing_stage': 3,
        'locator': ['A', 'B', 'C'],
        'state_values_source': ('m(A)=m(B)=m(C)=1: Lemma 6.2 of '
                                'sigma_essential_witness.md; m two-valued '
                                'f.a. state: Theorem 6.3; Lean suite '
                                'UlamWitnessMain.lean (psiAmended_ZFC)'),
    }


def main():
    base = run_once()
    canon = json.dumps(base, sort_keys=True, separators=(',', ':')).encode()
    h0 = hashlib.sha256(canon).hexdigest()
    replays = {}
    for seed in REPLAY_SEEDS:
        again = run_once()
        replays[str(seed)] = hashlib.sha256(
            json.dumps(again, sort_keys=True,
                       separators=(',', ':')).encode()).hexdigest()
        assert replays[str(seed)] == h0
    receipt = {
        'script': os.path.basename(__file__),
        'scope': ('trace-level identities of the product-Ulam cores ONLY; '
                  'state values imported from the machine-checked witness '
                  'note (not re-proved here); locator = {A,B,C}, FIP '
                  'failure at stage exactly 3'),
        'payload': base,
        'payload_sha256': h0,
        'replay_seed_hashes': replays,
        'verdict': ('DIRECT LOCATOR FOUND: value-1 family {A,B,C} of the '
                    'amended product-Ulam witness state fails FIP at stage '
                    '3; necessary condition fires; HAND fallback not needed'),
    }
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       'psi_witness_fip_locator.json')
    with open(out, 'w') as f:
        json.dump(receipt, f, indent=1, sort_keys=True)
        f.write('\n')
    print('payload_sha256', h0)
    print(receipt['verdict'])
    print('OK')


if __name__ == '__main__':
    sys.exit(main())
