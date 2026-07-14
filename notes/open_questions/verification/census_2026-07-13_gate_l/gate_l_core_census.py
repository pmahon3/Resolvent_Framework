#!/usr/bin/env python3
"""Exhaustive Gate-L census for balanced rotating-candidate core quotients."""
import hashlib, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))
from typed_graph_core_census import CELLS, data  # noqa: E402

def sections(x, n):
    return [[CELLS[i] for i in range(6) if x >> (6*c+i) & 1]
            for c in range(n)]

def extrema(cl, a, b, lower):
    if lower:
        candidates = [x for x in cl if not x & ~(a & b)]
        return [x for x in candidates
                if not any(x != y and not x & ~y for y in candidates)]
    candidates = [x for x in cl if not (a | b) & ~x]
    return [x for x in candidates
            if not any(x != y and not y & ~x for y in candidates)]

def run(n):
    types, full, sig, gs, cl = data(n)
    meet_failures = join_failures = 0
    first = None
    for i, a in enumerate(cl):
        for b in cl[i:]:
            ms = extrema(cl, a, b, True)
            js = extrema(cl, a, b, False)
            meet_failures += len(ms) != 1
            join_failures += len(js) != 1
            if first is None and (len(ms) != 1 or len(js) != 1):
                first = {"kind": "meet" if len(ms) != 1 else "join",
                         "left": sections(a,n), "right": sections(b,n),
                         "extrema": [sections(x,n) for x in (ms if len(ms)!=1 else js)]}
    raw = ','.join(map(str,cl)).encode()
    return {"n_columns":n, "type_word":''.join(map(str,types)),
            "core_count":len(cl), "unordered_pairs":len(cl)*(len(cl)+1)//2,
            "core_sha256":hashlib.sha256(raw).hexdigest(),
            "meet_failures":meet_failures, "join_failures":join_failures,
            "first_failure":first}

out = {"scope":"Exhaustive finite global-core quotients; no local modifications.",
       "infinite_consequence":"The n=3 missing-join witness lifts to arbitrary base via the transversal Q invariant; finite quotients alone would not suffice.",
       "runs":[run(n) for n in (3,6,9)]}
Path(__file__).with_name('gate_l_core_certificate.json').write_text(
    json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
