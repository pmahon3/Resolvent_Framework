# OML lattice attack — boundary-regularity handoff

**Date:** 2026-07-12. **Branch:**
`oml-descent-sigma-essential-reduction`. **Controlling notes:**
`relational_boundary_descent.md` and `oml_boundary_regularity.md`.

## Strategic verdict

Outcome 3, mixed hierarchy. Pairwise OML block intersections are σ-fields,
but this does not force the topology required by (RO-face). General
localization is no longer the primary route; direct simultaneous selection
is. Rooting remains downstream except in regular-interface slices.

## New counterexample

Let `A` be the σ-field of countable-coordinate subsets of `2^I` for
uncountable `I`. The direct product `A × MO2`, represented on a disjoint
union, is a concrete σ-complete OML with exactly two maximal blocks. Their
actual overlap boundary is `A × 2`. For the central event selecting the
`2^I` summand:

- its carrier shadow is dense with empty interior in its Stone closure;
- its actual σ-liftable trace locus is also dense with empty interior;
- the one-event coherent face has the whole relevant Stone component as
  its restriction image, so (RO-face) fails;
- the block is generated over the boundary by one Boolean event.

This is a boundary-regularity counterexample, not a σ-essential OML witness.
Its center is large, so essential irreducibility is the exact residual issue.

## Positive result retained

If, for a fixed pattern, every eligible local σ-state space is compact and
every finite subatlas has compatible eligible local states, Tychonoff plus
closed overlap equations gives a compatible family on the whole atlas;
block-state gluing gives the global σ-state. Compactness is load-bearing:
σ-additive two-valued state sets need not be closed.

Finite-interface quarantine and finite-atlas localization under (RO-face)
remain unchanged. Finite Boolean extension over the boundary is refuted in
the coarse class.

## Validation

Rerun and passed:

```sh
python3 notes/open_questions/verification/distributed_trap_audit.py
python3 notes/open_questions/verification/census_2026-07-12_s38/classify_near_misses.py
python3 notes/open_questions/verification/census_2026-07-12_s38/sasaki_root_audit.py
```

`lake build`, JSON validation, no-sorry scan, and axiom receipts are part of
the final session receipt. No Lean file was changed.

## Next task

Do exactly one of:

1. remove the center while preserving the countable-coordinate boundary
   topology in a concrete σ-complete OML; or
2. prove that trivial center forbids this topology.

Do not resume a broad relay census unless it tests this center-removal
problem. In parallel, sharpen the compact finite-subatlas theorem toward
noncompact σ-state spaces; a bare compactness argument cannot do this.
