#!/usr/bin/env python3
"""Finite relational countermodel to distributed-cover => local-cover."""
import json
from pathlib import Path

face = frozenset(range(3))
defects = {
    "B0": frozenset({0}),
    "B1": frozenset({1}),
    "B2": frozenset({2}),
}
assert set().union(*defects.values()) == face
assert all(d != face for d in defects.values())
assert all(set().union(*(d for k, d in defects.items() if k != omit)) != face
           for omit in defects)
good = {b: sorted(face - d) for b, d in defects.items()}
assert not set.intersection(*(set(x) for x in good.values()))

out = {
    "schema": 1,
    "scope": "abstract relational trace atlas; not a concrete sigma-class OML realization",
    "face": sorted(face),
    "defect_loci": {b: sorted(d) for b, d in defects.items()},
    "good_loci": good,
    "union_covers_face": True,
    "no_individual_covers_face": True,
    "cover_irredundant": True,
    "simultaneously_good_state_exists": False,
}
path = Path(__file__).with_name("distributed_trap_audit.json")
path.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
