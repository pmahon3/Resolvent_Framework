#!/usr/bin/env python3
"""Labeled period-1 scaffold for 7-loop ports of cardinality 1 and 2.

This enumerates all maps in the fixed atom labeling. It makes no claim about
symmetry orbit reduction or about which k/period bounds constitute a complete
mathematical search. Incidence counts are independent of the chosen target.
"""
import argparse
import relay7_core as rc


def census(k, dynamic=False):
    raw = valid = 0
    by_target = {target: {'passes': 0, 'exact_complement': 0}
                 for target in rc.COMMON_ZERO_TARGETS}
    for port in rc.two_cell_maps(k):
        raw += 1
        if not rc.window_girth_ok([port], 2):
            continue
        valid += 1
        if dynamic:
            for target in rc.COMMON_ZERO_TARGETS:
                result = rc.screen([port], target)
                by_target[target]['passes'] += int(result['passes'])
                by_target[target]['exact_complement'] += int(
                    result['passes'] and all(result['exact_complement']))
    return raw, valid, by_target


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--k', type=int, choices=(1, 2), action='append',
                        help='port cardinality; repeatable (default: both)')
    parser.add_argument('--dynamic', action='store_true',
                        help='also run all six target-dependent relay screens')
    args = parser.parse_args()
    for k in args.k or (1, 2):
        raw, valid, targets = census(k, args.dynamic)
        print(f'k={k} labeled_raw={raw} two_cell_girth_valid={valid}')
        if args.dynamic:
            for target, counts in targets.items():
                print(f'  target={target} passes={counts["passes"]} '
                      f'exact_complement={counts["exact_complement"]}')


if __name__ == '__main__':
    main()
