#!/usr/bin/env python3
"""CLI for the independent s37 period-two downstream oracle.

Input is a JSON list (or an object containing `rows`) whose rows have
`p0`, `p1`, and integer `target`.  Output is a JSON list of oracle reports.
"""
import argparse
import json
from pathlib import Path

from audit_s37_downstream_oracle import audit


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('input', type=Path)
    ap.add_argument('-o', '--output', type=Path)
    ap.add_argument('--maxpos', type=int, default=12)
    args = ap.parse_args()
    raw = json.loads(args.input.read_text())
    rows = raw if isinstance(raw, list) else raw.get('rows', raw.get('survivors'))
    if rows is None:
        raise SystemExit('input must be a list or contain rows/survivors')
    reports = []
    for n, row in enumerate(rows):
        print(f'auditing {n+1}/{len(rows)}', flush=True)
        reports.append(audit([row['p0'], row['p1']], int(row['target']), args.maxpos))
    text = json.dumps({'source': str(args.input), 'rows': reports}, indent=2) + '\n'
    if args.output: args.output.write_text(text)
    else: print(text, end='')


if __name__ == '__main__': main()
