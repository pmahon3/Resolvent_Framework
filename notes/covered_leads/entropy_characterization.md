# Covered Lead: Entropy Characterization of Reconstruction

## Status (updated 2026-05-14)

**DEAD.** The claimed equivalence δ(L) → 0 iff H₂(ν_L) → ∞
depended on the bridge theorem (Corollary 4.2 of the bridge note),
which is false. The bridge identity has a disintegration error
(p_z vs p_z² weighting). See papers/archive/paper_fibre_mixing/verification_checklist.md
and notes/covered_leads/fibre_mixing.md for details.

## What was claimed

  δ(L) → 0  iff  H₂(ν_L) → ∞

where δ(L) is the Rokhlin distance and H₂ is the Rényi-2 entropy
of the delay-vector distribution.

## Why it's false

The equivalence required both directions of the bridge theorem:
  δ → 0 ⟹ collision → 0  (easy direction, claimed unconditional)
  collision → 0 ⟹ δ → 0  (hard direction, claimed under fibre mixing)

The easy direction is itself false. The skew-product counterexample
(X = A^Z × B^Z, h(a,b) = a₀) has collision → 0 but δ = 1/4.
So H₂ → ∞ does NOT imply δ → 0.

The one true direction is trivial: δ → 0 ⟹ O_L generates B
⟹ fibres are singletons ⟹ collision = 0 ⟹ H₂ → ∞.

## Disposition

Move to covered_leads or archive. The entropy characterization
is not an active research direction.
