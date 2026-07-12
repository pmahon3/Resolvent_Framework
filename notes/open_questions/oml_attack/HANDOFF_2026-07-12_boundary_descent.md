# OML lattice attack — relational boundary-descent handoff

**Date:** 2026-07-12. **Branch:**
`oml-descent-sigma-essential-reduction`. **Controlling note:**
`relational_boundary_descent.md`.

## Review verdict

Keep the result. Independent hand review cleared the main arguments:
compatible block-state gluing, common-trace boundary surgery, exact
GSD $\Longleftrightarrow\Phi$, finite-interface quarantine, the boundary
Stone-closure formula, the stated Baire and metrizable-tail slices, and
Sasaki closure of state-one sets.

The receipt for the new tame theorem is now:

> **Finite-interface quarantine:** ⟦LEAN, `BoundaryDescent.lean`;
> independent review cleared⟧.

No proof of $\Psi_{\mathrm{OML}}$, B′(i), B′(ii), a rooting theorem, or a
relay/master normal form is claimed.

## Banked mathematical gain

For a concrete σ-class OML, let $\partial B$ be the Boolean algebra
generated under finite Boolean operations by all maximal-block overlaps.
Then

\[
 \boxed{\forall B\in\mathfrak B(L),\ |\partial B|<\infty
        \quad\Longrightarrow\quad\Phi(L).}
\]

Given a coherent finite pattern and finitely additive extension $\mu$,
augment each finite boundary by its local pattern event. The restricted
ultrafilter selects a nonzero atom, hence a nonempty concrete carrier cell.
A point in that cell gives a local Dirac replacement preserving the pattern
and every shared value. All replacements match the same $\mu$ on overlaps,
so they glue; certified blockwise σ-additivity then gives a global σ-state.

Interpretation: arbitrary nonprincipal behaviour private to a block is
harmless when that block communicates through a finite Boolean interface.
Every counterexample must have infinite relational adhesion somewhere.

GSD is separately banked as an **exact reformulation**, not progress on
universal truth: the correct object is σ-liftability of shared traces, not
principality of entire block interiors.

## Correct two-axis scope

Local block complexity and global atlas size are independent:

| Local block axis | Global atlas axis |
|---|---|
| Fine blocks: local σ-states are point-realized | Countably many blocks: Baire combines hereditary local escape |
| Coarse blocks: characterize $T_B^\sigma(E)$ without points | Uncountably many blocks: simultaneous selection remains open |

Therefore B′(i) still contains simultaneous selection over possibly
uncountably many fine blocks. B′(ii) adds non-point local σ-lifting on coarse
boundaries. Arbitrary-atlas selection cuts across both factors.

Terminology guard: “countably generated boundary gives metrizable Stone
space” means countably generated **as a Boolean algebra under finite
operations**. Countable generation merely as a σ-field does not imply that
the underlying Boolean algebra is countable.

## What remains open

1. **Fine local selection:** show each relevant boundary trace reaches a
   point shadow while preserving the finite face.
2. **Arbitrary-atlas selection:** combine local choices over possibly
   uncountably many blocks; the Baire theorem handles only countably many.
3. **Coarse local lifting:** characterize and select
   $T_B^\sigma(E)$ when σ-states need not be point-realized.
4. **Distributed trapping:** failure may cover a face by block-dependent
   defects without one block trapping the whole face.
5. **Rooting:** no theorem compresses a minimal higher-arity boundary defect
   into a binary nonorder. A local rooting theorem would not by itself solve
   an uncountably distributed failure.

## Next sequence

1. **Lean formalization — DONE:** `BoundaryDescent.lean` introduces local
   block σ-states, overlap-compatible gluing, finite augmented-trace Dirac
   lifts, boundary-preserving replacement, and finite-interface quarantine.
   The receipt is `[propext, Classical.choice, Quot.sound]`, with no `sorryAx`.
2. **Rooting falsification — DONE for s38:** the schema-2 census classifies
   all 1,165 near misses.  Every target loses the same root-phase nonorder
   `a3 ≰ a1`; `a3` is already a face premise, so the bounded Sasaki audit
   hits at depth zero.
3. **Distributed-trap search — partial, boundary problem remains open:** an
   executable three-state relational atlas proves that the cover equation
   alone need not localize.  For a finite fine-block atlas, Baire localizes
   **full-block non-σ failure** after finite face refinement, not boundary
   non-liftability.  Boundary localization additionally needs relative
   openness of the σ-liftable trace/point-shadow locus.  Establishing that
   interface regularity, or finding a concrete failure, is the next
   structural question.
4. Return to larger relay classes only after the rooted-separation data have
   produced a theorem or counterexample.

## Repository status

- `relational_boundary_descent.md`: corrected two-axis scope and receipt.
- `oml_lattice_taxonomy.json`: adds
  `oml.reduction.general_boundary_descent` and
  `oml.tame.finite_interface`; headline count updated.
- `taxonomies_index.json`: advanced through s38 and boundary descent.
- `frontier_map.md`: advanced through s38 and records the cross-cutting
  arbitrary-atlas issue.
- Lean: existing block/σ certificates build; the new boundary theorem is
  certified for finite raw overlap families.  The equivalence with the
  finite generated Boolean-boundary formulation remains an elementary hand
  step.
