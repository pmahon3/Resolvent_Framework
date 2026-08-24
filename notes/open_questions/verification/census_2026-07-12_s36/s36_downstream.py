#!/usr/bin/env python3
"""Finite relay-girth and adjacent-master geometry for s36 survivors."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
VERIFY = HERE.parent
sys.path.insert(0, str(VERIFY))
from verify_s35_survivor_girth import master_gaps, window_ok  # noqa: E402


def main():
    src = HERE / 's36_k4_results.json'
    data = json.loads(src.read_text())
    if not data.get('complete'):
        raise SystemExit('census checkpoint is incomplete')
    rows = []
    for target, counts in data['targets'].items():
        for survivor in counts['survivors']:
            port = tuple(tuple(x) for x in survivor['port'])
            windows = {str(n): window_ok(port, n) for n in (2, 3, 4, 6)}
            gaps = master_gaps(port, int(target), gaps=range(1, 16))
            rows.append({
                'target': int(target), 'port': survivor['port'],
                'exact_complement': survivor['exact_complement'],
                'windows': windows, 'master_gaps': gaps,
                'passes_six_cell_girth': all(windows.values()),
                'passes_adjacent_master_distance': gaps[1] is not None and gaps[1] >= 4,
            })
    out = {
        'source': src.name,
        'reflection_targets': {'1': 13, '2': 12, '4': 10},
        'rows': rows,
        'summary': {
            'operative_representatives': len(rows),
            'passes_three_cell_girth': sum(r['windows']['3'] for r in rows),
            'passes_six_cell_girth': sum(r['passes_six_cell_girth'] for r in rows),
            'passes_adjacent_master_distance': sum(
                r['passes_adjacent_master_distance'] for r in rows),
        },
    }
    path = HERE / 's36_downstream_results.json'
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps(out['summary'], sort_keys=True))


if __name__ == '__main__':
    main()
