#!/usr/bin/env python3
"""Exhaustive finite test of Gate-N core saturation modulo columns."""
import hashlib, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))
from typed_graph_core_census import CELLS, data  # noqa: E402

def sections(x, n):
    return [[CELLS[i] for i in range(6) if x >> (6*c+i) & 1] for c in range(n)]

def run(n):
    types, full, _, _, closure = data(n)
    masks = [63 << (6*c) for c in range(n)]
    surviving_checks = erasing_checks = 0
    first_erasing_failure = None
    for exceptional in range(1 << n):
        erases = [k for k in (1,2,3)
                  if all(exceptional >> c & 1 for c,t in enumerate(types) if t == k)]
        outside = full ^ sum(masks[c] for c in range(n) if exceptional >> c & 1)
        projections = {z & outside for z in closure}
        for x in closure:
            for y in closure:
                if x & y & outside:
                    continue
                if erases: erasing_checks += 1
                else: surviving_checks += 1
                target = (x | y) & outside
                if target not in projections:
                    if not erases:
                        raise AssertionError((n, exceptional, x, y))
                    if first_erasing_failure is None:
                        first_erasing_failure = {
                          "exceptional_mask": exceptional, "erased_types": erases,
                          "left": sections(x,n), "right": sections(y,n),
                          "target_outside": sections(target,n)}
    digest = hashlib.sha256(','.join(map(str,closure)).encode()).hexdigest()
    return {"n_columns": n, "type_word": ''.join(map(str,types)),
      "core_count": len(closure), "core_sha256": digest,
      "type_surviving_admissible_pairs_checked": surviving_checks,
      "type_surviving_failures": 0,
      "type_erasing_admissible_pairs_checked": erasing_checks,
      "first_type_erasing_failure": first_erasing_failure}

def main():
    ns = [int(x) for x in sys.argv[1:]] or [3,6,9]
    out = {"claim": "For every core pair and exceptional-column set in each stated balanced finite quotient, if the cores are disjoint off the exceptional set and every type survives, their union off that set is the restriction of a core.",
      "scope": "Exhaustive finite quotients only; does not prove arbitrary-base or countable-family splicing.",
      "runs": [run(n) for n in ns]}
    path = Path(__file__).with_name("splicing_saturation_certificate.json")
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(path)

if __name__ == '__main__': main()
