# Seed Note: CE as Sheaf Condition on Query System Category

## Phase: 1 (seed) — needs Phase 2 audit before development

## The claim

Collective exhaustion (CE) may be equivalent to a sheaf-completeness
condition on the natural Grothendieck topology of the query system
category. Specifically: the subcanonical condition (every representable
presheaf is a sheaf) may rule out exactly the "phantom sections"
(non-principal ultrafilters) that CE forbids.

## Why it might be new

- Reformulating CE in sheaf-theoretic language would connect the
  measure extension problem to topos theory
- The key insight: first-order conditions can't imply CE (Łoś), but
  covering conditions (inherently infinitary) break the ultraproduct
  argument and might work
- No known sheaf-theoretic reformulation of σ-additivity conditions
  in this specific directed-system setting

## Why it's probably hard / stalled

A previous investigation (directedness_interpolation branch) attempted
this and hit a wall:
- The naive topology J (witnessing-by-emptiness) was too coarse —
  can't detect CE failure for cofinite sequences
- The revised topology J' (witnessing-by-charge-decay) circularly
  invokes the charge
- Options A and C (first-order MI conditions) killed by CE
  irreducibility (Łoś)
- Option B (covering condition) remains live but no successful
  formulation achieved

## What would need to happen

A fresh angle that avoids the circularity of J'. Possible approaches:
1. Use the Stone space topology directly (compact Hausdorff) and
   define covering in terms of convergence of indicator functions
2. Work with the dual category (Stone spaces, continuous maps) where
   compactness gives non-first-order structure for free
3. Look at Caramello's "Theories, Sites, Toposes" for analogous
   situations where a model-theoretic condition becomes a sheaf condition

## Key terms for audit

- Grothendieck topology and σ-additivity
- Sheaf condition and measure extension
- Topos-theoretic probability (Vickers, Henry, Jackson-Meslier)
- Stone space and Grothendieck topologies on Boolean algebras
- Subcanonical topology and representable presheaves

## Source files

- `archive/notes_archived_artifacts/directedness_interpolation_branch/`
  - directedness_interpolation.md (main investigation)
  - query_system_as_site.md (category construction)
  - q4_finite_cofinite_sheaf_check.md (where it stalled)

## Disposition

Stalled seed. The question is well-posed and interesting but the
previous attempt failed. Needs either:
(a) Fresh approach avoiding the circularity, OR
(b) Literature search showing this reformulation already exists
    (topos-theoretic probability is active — check Henry 2014,
    Jackson-Meslier, Vickers)

Medium priority. This connects directly to the programme's core
(CE is the irreducible condition for Paper I) and could give a
conceptual unification. But tractability is uncertain.
