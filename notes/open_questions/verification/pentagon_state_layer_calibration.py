#!/usr/bin/env python3
"""E2a: pentagon state-layer calibration (linearization/extension-screen seed §3).

Producer + self-verifying receipt for the E-thread's extension-screen
quantities on the Greechie 5-cycle (pentagon), rebuilt self-contained with
the same conventions as the §9/§11 oracles (blocks {2i, 2i+1, (2i+2) mod 10}
on 10 atoms; 22 abstract elements; 11 abstract states), represented
concretely TWICE:

  canonical rep  -- point set = all 11 abstract-state indices;
  reduced rep    -- the UNIQUE valid proper order-determining subset
                    (re-verified here exhaustively over all 2046 nonempty
                    proper subsets; it is the 10-index set dropping the
                    all-odd state, as banked in s15/s16).

For EACH rep the script:
  * verifies the concrete family is a sigma-class (complement- and
    disjoint-union-closed; carrier finite, so countable = finite) and a
    lattice under inclusion (every pair has a least upper / greatest lower
    bound IN the family) -- i.e. a concrete sigma-class OML;
  * enumerates ALL two-valued finitely additive states on the family
    honestly: 2^10 atom-image assignments, complements forced by
    additivity (A perp A^c, A + A^c = Omega), then EVERY disjoint pair
    (A,B) with A "join" B in the family checked for s(A "join" B) =
    s(A) + s(B); finite carrier, so every fa state is sigma-additive;
  * per state computes: the value-1 family V, the kernel K = int(V),
    FIP status (finite carrier: FIP iff K nonempty), the minimal failing
    stage (least k with some k-subset of V having empty intersection),
    and point-representability (s = delta_omega for some carrier point);
  * asserts the seed §3 predictions:
      P1 canonical: every state has nonempty kernel (all extendable);
      P2 canonical: every state is a point evaluation (Dirac-at-itself);
      P3 reduced:   at least one state has empty kernel / FIP failure --
                    non-extendable yet (trivially) sigma-additive;
      P4 both:      pairwise intersections of value-1 events never empty,
                    so every FIP failure starts at stage exactly >= 3;
      P5 rep-relativity: state counts agree across reps (same abstract
                    logic) while the empty-kernel census differs -- FIP of
                    the value-1 family is a property of the representation;
      P6 the reduced rep IS a lattice (verified above), yet carries a
                    non-extendable state: latticehood does not force FIP.

Determinism / replay: the entire computation runs THREE times -- once in
canonical order, then twice with all enumeration orders shuffled under
PRNG seeds 20260719 and 8675309 -- and the canonical-JSON sha256 of the
payload must be identical across the three runs.  Pure stdlib.  Writes
pentagon_state_layer_calibration.json next to itself.  Exit 0 iff every
check and prediction passes.
"""

import hashlib
import json
import os
import random
import sys
from itertools import combinations, product

N = 5
N_ATOMS = 2 * N
REPLAY_SEEDS = (20260719, 8675309)


def build_abstract():
    blocks_a = [frozenset({2 * i, 2 * i + 1, (2 * i + 2) % N_ATOMS})
                for i in range(N)]

    def share_block(i, j):
        return i != j and any(i in b and j in b for b in blocks_a)

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

    states = []
    for bits in product((0, 1), repeat=N_ATOMS):
        if all(sum(bits[a] for a in b) == 1 for b in blocks_a):
            states.append(bits)

    def val(s, x):
        if x == ZERO:
            return 0
        if x == ONE:
            return 1
        return s[x[1]] if x[0] == 'a' else 1 - s[x[1]]

    return elements, le, states, val


def try_represent(elements, le, states, val, points):
    """Concrete rep of the abstract logic on the state-index set `points`;
    None unless the event map is injective and an order-isomorphism."""
    Im = {x: frozenset(i for i in points if val(states[i], x) == 1)
          for x in elements}
    if len(set(Im.values())) != len(elements):
        return None
    if not all((Im[x] <= Im[y]) == le(x, y)
               for x in elements for y in elements):
        return None
    return Im


def check_sigma_class_oml(fam, carrier, checks):
    """Verify fam is a concrete sigma-class OML on carrier; count checks."""
    assert frozenset(carrier) in fam and frozenset() in fam
    for A in fam:
        assert (carrier - A) in fam
        checks['complement'] += 1
    for A, B in combinations(fam, 2):
        if not (A & B):
            assert (A | B) in fam, "disjoint union escapes the family"
            checks['disjoint_union'] += 1
    for A, B in combinations(fam, 2):
        uppers = [C for C in fam if A <= C and B <= C]
        lowers = [C for C in fam if C <= A and C <= B]
        join = min(uppers, key=len)
        meet = max(lowers, key=len)
        assert all(join <= C for C in uppers), "no least upper bound"
        assert all(C <= meet for C in lowers), "no greatest lower bound"
        checks['lattice_pairs'] += 1


def enumerate_states(fam, atom_events, carrier, order_rng, checks):
    """All two-valued fa states on fam, honestly: atom assignments extended
    by forced complements, then every additivity instance checked."""
    fam_list = sorted(fam, key=lambda A: (len(A), sorted(A)))
    if order_rng is not None:
        order_rng.shuffle(fam_list)
    disjoint_join = [(A, B, A | B) for A, B in combinations(fam_list, 2)
                     if not (A & B) and (A | B) in fam]
    comp = {A: (frozenset(carrier) - A) for A in fam}
    assignments = list(product((0, 1), repeat=len(atom_events)))
    if order_rng is not None:
        order_rng.shuffle(assignments)
    states = []
    for bits in assignments:
        s = {frozenset(): 0, frozenset(carrier): 1}
        ok = True
        for a, v in zip(atom_events, bits):
            s[a] = v
            s[comp[a]] = 1 - v
        if len(s) != len(fam):
            raise AssertionError("atoms+complements+bounds must exhaust fam")
        for A, B, U in disjoint_join:
            checks['additivity_instances'] += 1
            if s[U] != s[A] + s[B]:
                ok = False
                break
        if ok:
            states.append(s)
    return states


def state_census(fam, states, carrier, checks):
    rows = []
    for s in states:
        V = [A for A in fam if s[A] == 1]
        K = frozenset(carrier)
        for A in V:
            K = K & A
        fip = bool(K)
        stage = None
        if not fip:
            for k in range(2, len(V) + 1):
                if any(not frozenset.intersection(*c)
                       for c in combinations(V, k)):
                    stage = k
                    break
        for A, B in combinations(V, 2):
            assert A & B, "pairwise value-1 intersection empty (refutes P4)"
            checks['pairwise_value1'] += 1
        point = next((w for w in sorted(carrier)
                      if all(s[A] == (1 if w in A else 0) for A in fam)),
                     None)
        rows.append({
            'value1_size': len(V),
            'kernel': sorted(K),
            'kernel_empty': not fip,
            'fip': fip,
            'min_failing_stage': stage,
            'point_representable': point is not None,
            'representing_point': point,
            'state_signature': ''.join(
                str(s[A]) for A in sorted(fam, key=lambda A: (len(A),
                                                              sorted(A)))),
        })
    rows.sort(key=lambda r: r['state_signature'])
    return rows


def run_once(seed):
    rng = random.Random(seed) if seed is not None else None
    checks = {'complement': 0, 'disjoint_union': 0, 'lattice_pairs': 0,
              'additivity_instances': 0, 'pairwise_value1': 0}
    elements, le, states, val = build_abstract()
    assert len(states) == 11

    all_idx = list(range(len(states)))
    all_odd = tuple(1 if i % 2 else 0 for i in range(N_ATOMS))
    all_odd_idx = states.index(all_odd)

    # Exhaustive re-verification of the unique valid proper reduced rep.
    valid_proper = []
    subsets = [c for k in range(1, len(states))
               for c in combinations(all_idx, k)]
    if rng is not None:
        rng.shuffle(subsets)
    for c in subsets:
        if try_represent(elements, le, states, val, list(c)) is not None:
            valid_proper.append(tuple(sorted(c)))
    assert len(valid_proper) == 1, valid_proper
    reduced_points = list(valid_proper[0])
    assert sorted(reduced_points) == sorted(set(all_idx) - {all_odd_idx})

    reps = {}
    for name, points in (('canonical', all_idx), ('reduced', reduced_points)):
        Im = try_represent(elements, le, states, val, points)
        assert Im is not None
        carrier = set(points)
        fam = frozenset(Im.values())
        check_sigma_class_oml(fam, carrier, checks)
        atom_events = sorted((Im[('a', i)] for i in range(N_ATOMS)),
                             key=lambda A: (len(A), sorted(A)))
        sts = enumerate_states(fam, atom_events, carrier, rng, checks)
        rows = state_census(fam, sts, carrier, checks)
        reps[name] = {'points': sorted(carrier), 'n_events': len(fam),
                      'n_states': len(rows), 'census': rows}

    can, red = reps['canonical'], reps['reduced']
    # P1/P2 canonical.
    assert all(not r['kernel_empty'] for r in can['census'])
    assert all(r['point_representable'] for r in can['census'])
    # P3 reduced.
    nonext = [r for r in red['census'] if r['kernel_empty']]
    assert nonext, "P3 fails: no empty-kernel state on the reduced rep"
    # P4: every failure starts at stage >= 3 (pairwise asserted in census).
    assert all(r['min_failing_stage'] is not None
               and r['min_failing_stage'] >= 3 for r in nonext)
    # P5 rep-relativity.
    assert can['n_states'] == red['n_states'] == 11
    assert sum(r['kernel_empty'] for r in can['census']) == 0 < len(nonext)
    predictions = {
        'P1_canonical_all_kernels_nonempty': True,
        'P2_canonical_all_point_representable': True,
        'P3_reduced_nonextendable_sigma_state_count': len(nonext),
        'P4_min_failing_stages': sorted(r['min_failing_stage']
                                        for r in nonext),
        'P5_rep_relativity_confirmed': True,
        'P6_latticehood_does_not_force_FIP': True,
    }
    payload = {'reps': reps, 'predictions': predictions,
               'dropped_state_is_all_odd': True,
               'unique_valid_proper_subsets': 1}
    # `checks` counters are order-sensitive (early break on additivity
    # violations), so they are run statistics, NOT part of the hashed payload.
    return payload, checks


def payload_hash(payload):
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True,
                   separators=(',', ':')).encode()).hexdigest()


def main():
    base, base_checks = run_once(None)
    h0 = payload_hash(base)
    replays = {}
    for seed in REPLAY_SEEDS:
        replays[str(seed)] = payload_hash(run_once(seed)[0])
        assert replays[str(seed)] == h0, (seed, replays[str(seed)], h0)
    receipt = {
        'script': os.path.basename(__file__),
        'scope': ('Greechie 5-cycle only, both banked concrete reps; '
                  'finite carrier so fa = sigma; extendability read off '
                  'via the E1-verified lemma (finite carrier: FIP iff '
                  'kernel nonempty iff point-representable)'),
        'payload': base,
        'payload_sha256': h0,
        'replay_seed_hashes': replays,
        'base_run_check_counts': base_checks,
        'verdict': 'ALL PREDICTIONS CONFIRMED',
    }
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       'pentagon_state_layer_calibration.json')
    with open(out, 'w') as f:
        json.dump(receipt, f, indent=1, sort_keys=True)
        f.write('\n')
    print('payload_sha256', h0)
    print('checks', base_checks)
    print('predictions', json.dumps(base['predictions'], indent=1))
    print('OK')


if __name__ == '__main__':
    sys.exit(main())
