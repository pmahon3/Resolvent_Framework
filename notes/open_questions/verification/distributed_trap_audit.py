#!/usr/bin/env python3
"""Finite relational model separating an unrefined distributed cover from localization."""
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

# In the discrete three-point face every nonempty subset is an abstract finite
# refinement.  Thus this model does *not* refute localization after refinement:
# each singleton refinement is contained in its corresponding defect locus.
refinements = [frozenset(x for x in face if mask & (1 << x))
               for mask in range(1, 1 << len(face))]
localized_refinements = {
    tuple(sorted(r)): [b for b, d in defects.items() if r <= d]
    for r in refinements
    if any(r <= d for d in defects.values())
}
assert all((i,) in localized_refinements for i in face)

out = {
    "schema": 2,
    "scope": "finite discrete abstract relational trace atlas; not a concrete sigma-class OML realization",
    "face": sorted(face),
    "defect_loci": {b: sorted(d) for b, d in defects.items()},
    "good_loci": good,
    "union_covers_face": True,
    "no_individual_covers_face": True,
    "cover_irredundant": True,
    "simultaneously_good_state_exists": False,
    "locus_topology": "all defect loci are clopen in the finite discrete face",
    "refinement_model": "all nonempty subsets of the finite face",
    "some_finite_refinement_localizes": True,
    "singleton_localizations": {
        str(i): localized_refinements[(i,)] for i in sorted(face)
    },
    "refutes_unrefined_local_trapping": True,
    "refutes_finite_refinement_localization": False,
}
path = Path(__file__).with_name("distributed_trap_audit.json")
path.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
