#!/usr/bin/env python3
"""Exhaustive period-one width-four census for the s35 seven-loop face."""
import argparse
import json
import os
import sys
from itertools import combinations, permutations
from pathlib import Path

HERE = Path(__file__).resolve().parent
S35 = HERE.parent / 'census_2026-07-12_s35'
sys.path.insert(0, str(S35))
import relay7_core as rc  # noqa: E402

OLD_SETS = tuple(combinations(rc.ATOMS, 4))
NEW_SETS = OLD_SETS
TARGETS = (1, 2, 4)  # reflection gives 13, 12, 10
RAW_PER_OLD = len(NEW_SETS) * 24
TOTAL_RAW = len(OLD_SETS) * RAW_PER_OLD


def pair_key(x, y):
    return tuple(sorted((x, y)))


def valid_pair_table():
    """Exact validity of all 16,562 oriented width-two ports."""
    good = set()
    for old in combinations(rc.ATOMS, 2):
        for new in combinations(rc.ATOMS, 2):
            for image in permutations(new):
                port = tuple(zip(old, image))
                if rc.window_girth_ok([port], 2):
                    good.add(pair_key(*port))
    assert len(good) == 9408
    return good


def pair_prefilter(port, good):
    return all(pair_key(port[i], port[j]) in good
               for i, j in combinations(range(4), 2))


def empty_counts():
    return {
        'schema': 1,
        'scope': '7-loop C={a0,a3,a11}, period 1, oriented injective k=4',
        'total_raw_expected': TOTAL_RAW,
        'completed_old_sets': 0,
        'raw': 0,
        'pair_prefilter': 0,
        'two_cell_valid': 0,
        'three_cell_valid': 0,
        'targets': {str(t): {'screened': 0, 'operative': 0,
                             'exact_complement': 0, 'survivors': []}
                    for t in TARGETS},
    }


def save(path, data):
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + '\n')
    os.replace(tmp, path)


def census(checkpoint, stop_after=None):
    good = valid_pair_table()
    if checkpoint.exists():
        data = json.loads(checkpoint.read_text())
    else:
        data = empty_counts()
    start = data['completed_old_sets']
    end = len(OLD_SETS) if stop_after is None else min(len(OLD_SETS), start + stop_after)
    for oi in range(start, end):
        old = OLD_SETS[oi]
        for new_set in NEW_SETS:
            for image in permutations(new_set):
                port = tuple(zip(old, image))
                data['raw'] += 1
                if not pair_prefilter(port, good):
                    continue
                data['pair_prefilter'] += 1
                if not rc.window_girth_ok([port], 2):
                    continue
                data['two_cell_valid'] += 1
                # Three-cell validity is a downstream gate, not part of the
                # local operative definition. Record it once, independently
                # of target, while still screening every two-cell-valid map.
                if rc.window_girth_ok([port], 3):
                    data['three_cell_valid'] += 1
                for target in TARGETS:
                    out = rc.screen([port], target)
                    d = data['targets'][str(target)]
                    d['screened'] += 1
                    if out['passes']:
                        d['operative'] += 1
                        exact = all(out['exact_complement'])
                        d['exact_complement'] += int(exact)
                        d['survivors'].append({
                            'port': [list(pair) for pair in port],
                            'exact_complement': exact,
                            'three_cell_girth': rc.window_girth_ok([port], 3),
                            'live_mask': out['live'][0],
                            'free_mask': out['free'][0],
                        })
        data['completed_old_sets'] = oi + 1
        save(checkpoint, data)
        print(f"chunk {oi+1}/{len(OLD_SETS)} raw={data['raw']} "
              f"pair={data['pair_prefilter']} valid={data['two_cell_valid']} "
              f"operative={[data['targets'][str(t)]['operative'] for t in TARGETS]}",
              flush=True)
    data['complete'] = data['completed_old_sets'] == len(OLD_SETS)
    save(checkpoint, data)
    return data


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--checkpoint', type=Path, default=HERE / 's36_k4_results.json')
    p.add_argument('--chunks', type=int, help='process only this many new old-sets')
    args = p.parse_args()
    result = census(args.checkpoint, args.chunks)
    print(json.dumps({k: result[k] for k in
                      ('complete', 'completed_old_sets', 'raw',
                       'pair_prefilter', 'two_cell_valid', 'three_cell_valid')},
                     sort_keys=True))


if __name__ == '__main__':
    main()
