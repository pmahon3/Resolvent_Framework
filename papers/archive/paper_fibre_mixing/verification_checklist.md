# Verification Checklist

Per tool stacking discipline: every proof in this paper was
drafted by an LLM and must be manually verified before
submission. LLMs hallucinate freely in mathematics.

## CRITICAL: Bridge Identity (Lemma 2.1) is FALSE

**Status: FALSIFIED (2026-05-14)**

The bridge note claims:

  E[Var(1_S | O_L)] = (1/2) ∫_{R_L} |1_S - 1_S'|² d(μ⊗μ)

This is false. The disintegration error:

  (μ⊗μ)|_{R_L} = Σ_z p_z² · (μ_z ⊗ μ_z)    [correct]

not

  (μ⊗μ)|_{R_L} = Σ_z p_z · (μ_z ⊗ μ_z)      [claimed]

because μ|_{F_z} = p_z · μ_z, so (μ|_{F_z})⊗(μ|_{F_z}) = p_z² · (μ_z⊗μ_z).

Consequence:
  LHS = Σ_z p_z · μ_z(S)μ_z(Sᶜ)         (p_z weighting)
  RHS = Σ_z p_z² · μ_z(S)μ_z(Sᶜ)        (p_z² weighting)

These are genuinely different. The error propagates to BOTH
the easy direction (Thm 3.3) and hard direction (Thm 3.5).

## Skew-product counterexample (falsifies BOTH directions)

X = A^Z × B^Z, T = σ×σ, h(a,b) = a₀, iid uniform.
S = {b₀ = 0}.

  μ_z(S) = 1/2 for all z (b ⊥ a-history)
  δ_L = 1/4 for all L
  collision_L = 2^{-(L+1)} → 0

Easy direction claims: δ ≤ (1/2)·collision
  1/4 ≤ (1/2)·2^{-(L+1)} → 0.  FALSE for L ≥ 1.

Hard direction claims: collision ≤ (1/c)·δ + C(c)·ε
  This is TRUE but trivial (large upper bound).
  The hard direction would need δ ≤ f(collision), which is false.

## Items below are MOOT (depend on false lemma)

### Lemma 3.1: Conditional variance identity
The identity E[Var(1_S|O)] = ∫ p_z μ_z(S)μ_z(Sᶜ) dν is correct
on its own. But it does NOT equal (1/2)∫_{R_L}|1_S-1_S'|²d(μ⊗μ).

### Theorem 3.2: Easy direction — FALSE (see above)

### Theorem 3.3: Hard direction — WRONG DIRECTION + depends on false lemma

### Corollary 6.1: Entropy characterization — DEAD (depends on bridge)

### All other items: moot pending reconception of the paper.

## Decision (2026-05-14)

Paper pivots from positive bridge theorem to negative/clarification
result: geometric and algebraic reconstruction are inequivalent.
See notes/active_leads/fibre_mixing.md for revised structure.
