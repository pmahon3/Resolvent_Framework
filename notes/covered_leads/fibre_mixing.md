# Active Lead: Geometric vs Algebraic Reconstruction

## Status (updated 2026-05-14)

**PIVOTED.** The original bridge theorem is false. The error is
not merely an inequality direction — the core identity (Lemma 2.1
of the bridge note) has a disintegration error. The paper has
been reconceived as a negative/clarification result.

## The disintegration error

The bridge note claimed:

  E[Var(1_S | O_L)] = (1/2) ∫_{R_L} |1_S - 1_S'|² d(μ⊗μ)

This is false. The left side is Σ_z p_z · μ_z(S)μ_z(Sᶜ). The
right side is Σ_z p_z² · μ_z(S)μ_z(Sᶜ). These differ by a
factor of p_z in each summand. The error: the disintegration of
(μ⊗μ)|_{R_L} gives weight p_z² (not p_z) to fibre z, because
μ|_{F_z} = p_z · μ_z so (μ|_{F_z})⊗(μ|_{F_z}) = p_z² · (μ_z⊗μ_z).

Both directions of the bridge theorem (easy and hard) depended on
this identity. Both are false.

## The skew-product counterexample

X = A^Z × B^Z, T = σ×σ, h(a,b) = a₀, with independent iid
processes. For S = {b₀ = 0}:

  μ_z(S) = 1/2 for every a-block z  (b independent of a-history)
  δ_L = sup_S Σ_z p_z · μ_z(S)μ_z(Sᶜ) = 1/4  for all L
  collision_L = Σ p_z² = 2^{-(L+1)} → 0

Geometric collision convergence occurs while algebraic
reconstruction completely fails. Even the "easy direction"
(δ ≤ (1/2)·collision) is violated: 1/4 > (1/2)·2^{-(L+1)}.

## What the two quantities actually measure

  collision = Σ p_z²
    → how likely two independent samples land in the same fibre
    → measures geometric refinement of the observed factor

  δ_L(S) = Σ p_z · μ_z(S)μ_z(Sᶜ)
    → unresolved algebraic ambiguity after conditioning on O_L
    → measures σ-algebraic generation

Small fibres (collision → 0) do not imply that the observable
captures all σ-algebraic structure. A hidden independent
coordinate remains invisible while visible fibres shrink.

## The replacement paper thesis

> Collision decay of delay fibres measures geometric refinement
> of the observed factor, while Rokhlin/conditional-variance decay
> measures σ-algebraic generation. These are distinct. A delay
> observable may geometrically separate observed histories while
> leaving an independent hidden factor completely unresolved.

## Proposed structure

1. Define delay factor O_L = σ(Φ_L)
2. Define collision mass C_L = Σ_z p_z²
3. Define algebraic defect δ_L(S) = E[Var(1_S | O_L)] = Σ_z p_z μ_z(S)μ_z(Sᶜ)
4. Prove corrected identities (with p_z² vs p_z weighting)
5. Skew-product counterexample: C_L → 0 but δ_L = 1/4
6. Conclude: collision convergence ≠ algebraic reconstruction
7. Ask: what additional conditions make the implication true?

## What IS true

- δ → 0 ⟹ collision → 0 (trivially: if O_L generates B, fibres
  are singletons, collision = 0)
- The converse is false (skew-product)
- The definitions (collision, Rokhlin distance, fibre mixing) are
  well-posed
- Fibre mixing as originally defined is NOT useful: it holds
  trivially in the skew-product (p_z → 0 makes the lower bound
  vacuous) while reconstruction fails

## What is dead

- The bridge theorem (both directions)
- The entropy characterization (H₂ → ∞ ⟺ δ → 0)
- Fibre mixing as a sufficient condition for bridging
- The original paper structure

## Open question for the replacement

What condition on the factor map Φ_L makes collision → 0 imply
δ → 0? The skew-product shows the obstruction is an independent
hidden factor. So the condition likely involves some form of
"h eventually sees everything" — perhaps that O_∞ = B (the
tail σ-algebra generates). But this is exactly the conclusion
(reconstruction), so it would be circular.

A non-circular formulation might involve a rate condition:
uniform decay of μ_z(S)μ_z(Sᶜ) across fibres as collision → 0.
This would be an UPPER bound on conditional variance per fibre,
not the LOWER bound that fibre mixing provides.

## Source files

- Bridge note (contains the error): papers/archive/paper_fibre_mixing/bridge_note_source.tex
- Verification checklist: papers/archive/paper_fibre_mixing/verification_checklist.md
- Steps 1-5: notes/archive/fibre_mixing_investigation/
- Steps 6-7: notes/archive/dynamics_reconstruction_dead/fibre_mixing/
