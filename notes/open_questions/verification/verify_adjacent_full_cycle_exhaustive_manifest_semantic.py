#!/usr/bin/env python3
"""Independent semantic verifier for the exhaustive first-round manifest.

The production manifest classifies an event section as empty/full/partial by
recursing over the shape of a reduced MDD.  This verifier instead computes the
exact number of satisfying assignments after fixing one shared-state
coordinate.  Empty means count zero and full means count equal to the complete
remaining fibre cardinality.  Thus it shares the captured old grammar and its
MDD representation, but not the production status-classification primitive.

After classification it independently reconstructs same-U minimal existential
classes, admissible nonempty U families, the canonical join-rich ranking, and
the rank-mod-32 partition.  It compares every resulting list, count, and digest
with the stored production manifest.  It does not execute any kernel fold.
"""
import argparse
import collections
import functools
import hashlib
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import full_cycle_adjacent_rectangle_intersection as inter

SCHEMA = 'adjacent-full-cycle-exhaustive-manifest-semantic-verifier-v1'
SHARDS = 32


def payload():
    manifest_path = os.path.join(
        HERE, 'adjacent_full_cycle_exhaustive_manifest.json')
    manifest = json.load(open(manifest_path))
    assert manifest['schema'] == \
        'adjacent-full-cycle-exhaustive-first-round-manifest-v1'
    assert manifest['schema_version'] == '1.0'

    mx = dict(manifest)
    stored_manifest_payload = mx.pop('payload_sha256')
    recomputed_manifest_payload = hashlib.sha256(
        json.dumps(mx, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()
    assert stored_manifest_payload == recomputed_manifest_payload

    base, b = inter.capture_grammar()
    events = b['all_events']
    macros = b['macros']
    engines = b['engines']
    states = b['states']
    principal = b['principal']
    roots = {ev: r for r, ev in b['root_to_event'].items()}
    n = len(events)
    N = len(states)
    assert (n, N, len(macros)) == (18676, 224, 842)
    assert base['payload_sha256'] == manifest['base_full_cycle_payload_sha256']

    upmap = {u: i for i, u in enumerate(principal)}
    assert len(upmap) == n
    allold = (1 << n) - 1
    zero = upmap[allold]
    nonatomic = 0
    for d, u in enumerate(principal):
        if d != zero:
            nonatomic |= u & ~(1 << d)
    bits = allold & ~nonatomic & ~(1 << zero)
    atoms = []
    while bits:
        z = bits & -bits
        atoms.append(z.bit_length() - 1)
        bits -= z
    assert len(atoms) == 91

    occurrences = [[[] for _ in range(N)] for _ in range(4)]
    for m, (_, ds) in enumerate(macros):
        for pos in range(4):
            for i, s in enumerate(ds[pos]):
                occurrences[pos][s].append((m, i))

    # Exact model count after assigning coordinate `pos` to domain index `i`.
    # The recursion explicitly visits all four variables, multiplying over
    # skipped MDD variables by enumerating their complete domains.
    count_calls = 0

    @functools.lru_cache(None)
    def assigned_count(m, root, pos, i, k):
        nonlocal count_calls
        count_calls += 1
        eng = engines[m]
        if k == 4:
            assert root <= 1
            return int(root)
        if root > 1:
            v, ch = eng.nodes[root]
            assert v >= k
        else:
            v, ch = 10**9, None
        if k == pos:
            child = ch[i] if v == k else root
            return assigned_count(m, child, pos, i, k + 1)
        if v == k:
            return sum(
                assigned_count(m, child, pos, i, k + 1)
                for child in ch)
        return len(eng.domains[k]) * assigned_count(
            m, root, pos, i, k + 1)

    totals = {}
    for m, eng in enumerate(engines):
        for pos in range(4):
            totals[m, pos] = math.prod(
                len(eng.domains[k]) for k in range(4) if k != pos)

    def classify(pos):
        answer = []
        for ev in events:
            E = U = 0
            rr = roots[ev]
            for s, occ in enumerate(occurrences[pos]):
                counts = [
                    assigned_count(m, rr[m], pos, i, 0)
                    for m, i in occ
                ]
                if any(c > 0 for c in counts):
                    E |= 1 << s
                if all(c == totals[m, pos]
                       for c, (m, _) in zip(counts, occ)):
                    U |= 1 << s
            assert not U & ~E
            answer.append((E, U))
        return answer

    left = classify(3)
    right = classify(0)

    def minima(classes):
        groups = collections.defaultdict(list)
        for i, (E, U) in enumerate(classes):
            groups[U].append((E, i))
        result = {}
        for U, xs in groups.items():
            keep = []
            for E, i in sorted(
                    xs, key=lambda x: (x[0].bit_count(), x[0], x[1])):
                if not any(not K & ~E for K, _ in keep):
                    keep.append((E, i))
            result[U] = tuple(keep)
        return result

    def admissible(classes, opposite):
        result = []
        for EA, _ in classes:
            result.append(tuple(sorted(
                (U for U, xs in opposite.items()
                 if any(not EA & E for E, _ in xs)),
                key=lambda u: (u.bit_count(), u))))
        return result

    left_us = admissible(left, minima(right))
    right_us = admissible(right, minima(left))
    assert (sum(map(len, left_us)), sum(map(len, right_us))) == \
        (28023, 27699)

    join_cache = {}

    def joins(A):
        if A not in join_cache:
            join_cache[A] = len({
                upmap[principal[A] & principal[a]]
                for a in atoms if not (principal[a] >> A & 1)
            })
        return join_cache[A]

    def ranked(families):
        xs = []
        for A, us0 in enumerate(families):
            us = [u for u in us0 if u]
            if us:
                j = joins(A)
                xs.append((-(len(us) * j), -j, -len(us), A, len(us)))
        xs.sort()
        return xs

    reconstructed = []
    for name, families in (
            ('left_retained_position11', left_us),
            ('right_retained_position00', right_us)):
        xs = ranked(families)
        assert len(xs) == 4719
        full = [x[3] for x in xs]
        shard_records = []
        for shard in range(SHARDS):
            selected = [x for rank, x in enumerate(xs)
                        if rank % SHARDS == shard]
            evs = [x[3] for x in selected]
            shard_records.append({
                'shard_index': shard,
                'rank_residue_mod_32': shard,
                'retained_event_indices': evs,
                'retained_event_count': len(evs),
                'nonempty_kernel_count': sum(x[4] for x in selected),
                'event_list_sha256': hashlib.sha256(
                    ','.join(map(str, evs)).encode()).hexdigest(),
            })
        assert len({e for s in shard_records
                    for e in s['retained_event_indices']}) == 4719
        reconstructed.append({
            'orientation': name,
            'ranked_retained_event_count': 4719,
            'nonempty_kernel_count': sum(x[4] for x in xs),
            'complete_ranked_event_indices': full,
            'complete_ranking_sha256': hashlib.sha256(
                ','.join(map(str, full)).encode()).hexdigest(),
            'shards': shard_records,
        })

    assert reconstructed == manifest['orientations']
    assert [x['nonempty_kernel_count'] for x in reconstructed] == \
        [9347, 9023]
    assert sum(x['nonempty_kernel_count'] for x in reconstructed) == 18370
    assert manifest['complete_kernel_counts'] == {
        'all': 55722, 'u_empty_tautological': 37352, 'nonempty': 18370}

    def mask_vector_digest(classes):
        h = hashlib.sha256()
        for E, U in classes:
            h.update(E.to_bytes(28, 'little'))
            h.update(U.to_bytes(28, 'little'))
        return h.hexdigest()

    out = {
        'schema': SCHEMA,
        'schema_version': '1.0',
        'verified_manifest_schema': manifest['schema'],
        'verified_manifest_payload_sha256': stored_manifest_payload,
        'base_full_cycle_payload_sha256': base['payload_sha256'],
        'completed_events_each': n,
        'shared_states': N,
        'macrofibres': len(macros),
        'old_atom_count': len(atoms),
        'left_EU_vector_sha256': mask_vector_digest(left),
        'right_EU_vector_sha256': mask_vector_digest(right),
        'assigned_count_cache_entries': assigned_count.cache_info().currsize,
        'assigned_count_recursive_calls': count_calls,
        'orientation_active_retained_events': {
            x['orientation']: x['ranked_retained_event_count']
            for x in reconstructed},
        'orientation_nonempty_kernel_totals': {
            x['orientation']: x['nonempty_kernel_count']
            for x in reconstructed},
        'complete_kernel_counts': manifest['complete_kernel_counts'],
        'complete_ranking_sha256': {
            x['orientation']: x['complete_ranking_sha256']
            for x in reconstructed},
        'rank_mod_32_event_counts': {
            x['orientation']:
                [s['retained_event_count'] for s in x['shards']]
            for x in reconstructed},
        'rank_mod_32_kernel_counts': {
            x['orientation']:
                [s['nonempty_kernel_count'] for s in x['shards']]
            for x in reconstructed},
        'verification_result':
            'Independent exact satisfying-assignment counts reconstruct every '
            'production (E,U) consequence, active-event ranking, kernel total, '
            'ranking digest, and rank-mod-32 shard record.',
        'shared_dependencies':
            'Shares full_cycle_adjacent_rectangle_intersection.capture_grammar, '
            'the captured event ordering, principal upsets, reduced MDD nodes, '
            'and the stored production manifest. It does not use the manifest '
            'producer classification/minima/admissibility/ranking code.',
        'independence_method':
            'Section emptiness/fullness is decided by exact satisfying-model '
            'counts after coordinate assignment, rather than the production '
            'three-valued reduced-MDD status recursion.',
        'quantifier_scope':
            'All 18,676 old events, all 224 shared states, both adjacent '
            'orientations, all admissible universal masks, all 4,719 active '
            'retained events per orientation, and all 32 manifest shards.',
        'scope_not_covered':
            'Kernel folds, shard execution, failure certificates, second-round '
            'closure, latticehood, OML, sigma closure, MBRC, ODBC, and Phi.',
        'verification_independence':
            'Independent verifier over the shared captured grammar; no '
            'independent grammar producer or state enumeration.',
        'evidence_classes': ['Executable verified'],
        'command':
            'python3 notes/open_questions/verification/'
            'verify_adjacent_full_cycle_exhaustive_manifest_semantic.py '
            '--verify',
    }
    out['producer_sha256'] = hashlib.sha256(
        open(__file__, 'rb').read()).hexdigest()
    out['payload_sha256'] = hashlib.sha256(json.dumps(
        out, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return out


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--emit', action='store_true')
    parser.add_argument('--verify', action='store_true')
    args = parser.parse_args()
    result = payload()
    path = os.path.join(
        HERE, 'verify_adjacent_full_cycle_exhaustive_manifest_semantic.json')
    if args.emit:
        with open(path, 'w') as f:
            json.dump(result, f, sort_keys=True, indent=2)
            f.write('\n')
    else:
        assert json.load(open(path)) == result
    print(json.dumps({
        'status': 'PASS',
        'payload_sha256': result['payload_sha256'],
        'active_events_each': 4719,
        'nonempty_kernels': 18370,
    }, sort_keys=True))
