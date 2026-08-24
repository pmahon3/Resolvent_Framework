#!/usr/bin/env python3
"""Classify every s38 stage-three near miss by its absent nonorders."""
import json
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "s38_p3_k1_checkpoint.json").read_text())
CASES = DATA["near_misses"]

def label(i):
    return f"a{i}" if i < 14 else f"a{i-14}^perp"

def pair_label(p):
    return f"{label(p[0])} !<= {label(p[1])}"

def pairsets(case):
    return [set(map(tuple, phase)) for phase in case["missing"]]

def first_bad(case):
    return next(i for i, s in enumerate(pairsets(case)) if s)

def greedy_cover(cases, phase_sensitive=False):
    universe = set(range(len(cases)))
    covers = defaultdict(set)
    for i, case in enumerate(cases):
        for phase, pairs in enumerate(pairsets(case)):
            for pair in pairs:
                covers[(phase, pair) if phase_sensitive else pair].add(i)
    chosen = []
    while universe:
        key, covered = max(covers.items(), key=lambda kv: len(kv[1] & universe))
        hit = covered & universe
        if not hit:
            raise RuntimeError("uncovered near miss")
        chosen.append((key, len(hit)))
        universe -= hit
    return chosen

def summarize(cases):
    first = [pairsets(c)[first_bad(c)] for c in cases]
    common = set.intersection(*first) if first else set()
    freq = Counter(p for s in first for p in s)
    return {
        "count": len(cases),
        "first_bad_phase_counts": dict(sorted(Counter(first_bad(c) for c in cases).items())),
        "first_bad_missing_count_range": [min(map(len, first)), max(map(len, first))],
        "common_first_bad_witnesses": [pair_label(p) for p in sorted(common)],
        "top_first_bad_witnesses": [
            {"witness": pair_label(p), "cases": n} for p, n in freq.most_common(12)
        ],
        "greedy_pair_cover": [
            {"witness": pair_label(k), "new_cases": n} for k, n in greedy_cover(cases)
        ],
        "greedy_phase_pair_cover": [
            {"phase": k[0], "witness": pair_label(k[1]), "new_cases": n}
            for k, n in greedy_cover(cases, True)
        ],
    }

by_target = {t: [c for c in CASES if c["target"] == t] for t in (1, 2, 4)}
result = {
    "schema": 1,
    "semantics": "missing[x,y] means no complement-live state has x=1,y=0",
    "element_encoding": "0..13=a_i; 14..27=a_(i-14)^perp",
    "all_targets": summarize(CASES),
    "targets": {str(t): summarize(cs) for t, cs in by_target.items()},
}
(HERE / "s38_near_miss_classification.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
