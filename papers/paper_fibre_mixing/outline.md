# Paper: The Fibre Mixing Bridge

## Working title

"Algebraic and Geometric Reconstruction: A Bridge via Fibre Mixing"

## One-sentence summary

The Rokhlin distance between a delay observable σ-algebra and the
full σ-algebra controls the collision probability of the delay map
if and only if the conditional measures on delay fibres are
non-degenerate — a condition we call fibre mixing, which is novel,
distinct from temporal mixing, and whose derivability from
ergodicity is the paper's central open question.

## What's proved (from existing work)

### Step A: Positive-fraction balance (proved, no dynamics needed)

**Bridge theorem.** If δ(O) > 2ε + η and S* is an ε-maximizer,
then the set of ε-large fibres on which S* is η-balanced satisfies:

  ν(G(η)) ≥ 2(κ - 2η)

where κ = δ - ε - I_S (the large-fibre contribution). This is a
purely analytic result — no ergodicity required. All of δ comes
from non-monochromatic fibres.

### The bridge theorem itself (proved under fibre mixing)

- Easy direction: δ(L) → 0 ⟹ (μ⊗μ)(R_L) → 0 (unconditional)
- Hard direction: (μ⊗μ)(R_L) → 0 ⟹ δ(L) → 0 (under fibre mixing)

### Entropy characterization (corollary)

δ(L) → 0 iff H₂(ν_L) → ∞ (novel, connecting Rokhlin distance
to Rényi-2 entropy)

## What's open (the paper's target)

### Step B: a.e. balance from ergodicity

**The question.** In an ergodic system with δ(L) > 0, must the
ε-maximizer be η-balanced on ν-a.e. large fibre (not just a
positive fraction)?

**The gap:** Step A gives "positive fraction balanced." Step B
needs "a.e. balanced." The difference is between:
- ν(G(η)) > 0 (proved)
- ν(M₀ ∪ M₁) = 0 (open: no large fibres are monochromatic)

**Evidence for positive answer (derivability):**
- Near-maximizers are adversarially mis-aligned with fibres (by
  definition — aligned events are easy to approximate)
- Monochromatic fibres contribute 0 to δ, so maximizing δ
  requires straddling fibres
- In ergodic systems, the ergodic theorem suggests fibres are
  "representative" of the global measure
- The non-ergodic counterexample (two-component system) shows
  fibre mixing fails without ergodicity

**Evidence against (irreducibility):**
- The a.e. condition is strictly stronger than positive fraction
- Ergodic theorems give time averages, not pointwise control of
  conditional measures at fixed L
- No proof exists despite clear formulation

## Paper structure

### §1. Introduction

Delay embedding reconstructs dynamics from scalar observations.
Reconstruction has two faces:

- **Geometric:** the delay map becomes injective (collision
  probability → 0)
- **Algebraic:** the delay σ-algebra generates the full σ-algebra
  (Rokhlin distance → 0)

These are different conditions. When are they equivalent?

We prove they are equivalent under a novel condition — fibre mixing
— on the disintegration over delay fibres. We characterize the
positive-fraction result analytically (no dynamics) and identify
the a.e. extension as the precise point where ergodicity enters.

### §2. Definitions and setup

- Measure-preserving system (X, B, μ, T)
- Observable h, delay map Φ_L, delay σ-algebra O_L
- Rokhlin distance δ(L) = sup_S inf_{E ∈ O_L} μ(S△E)
- Collision probability (μ⊗μ)(R_L) = ∫ p_z² dν_L
- Rokhlin disintegration: conditional measures μ_z, fibre masses p_z
- **Cite Rokhlin distance by name**

### §3. The bridge theorem

**Theorem.** (Easy direction) δ(L) → 0 ⟹ (μ⊗μ)(R_L) → 0.
Proof: Cauchy-Schwarz.

**Definition.** Fibre mixing at lag L: for ν-a.e. ε-large fibre z,
μ_z(S)μ_z(Sᶜ) ≥ c·p_z for all S.

**Theorem.** (Hard direction, under fibre mixing)
(μ⊗μ)(R_L) → 0 ⟹ δ(L) → 0.

**Corollary.** Under fibre mixing, algebraic and geometric
reconstruction are equivalent.

### §4. Positive-fraction balance (Step A)

**Theorem.** For any probability space (no dynamics needed): if
δ(O) > 2ε + η and S* is an ε-maximizer, then ν(G(η)) ≥ 2(κ-2η).

Proof: partition fibres into small/monochromatic/balanced, bound
each contribution, use near-maximizer property.

**Corollary.** All of δ comes from non-monochromatic fibres.
Monochromatic fibres contribute 0 to the approximation error.

### §5. The derivability question (Step B)

State precisely: does ergodicity force ν(M₀ ∪ M₁) = 0 for
near-maximizers?

Present the evidence:
- Near-maximizers are adversarially mis-aligned (proved in §4)
- Non-ergodic counterexample (two-component system)
- Heuristic: ergodic theorem suggests fibres are representative

**If resolved positively:** Theorem — fibre mixing is derivable
from ergodicity. The bridge is unconditional for ergodic systems.

**If resolved negatively:** Counterexample — exhibit an ergodic
system where fibre mixing fails at some L with δ(L) > 0.

### §6. Entropy characterization

**Corollary.** δ(L) → 0 iff H₂(ν_L) → ∞.

This is the first information-theoretic characterization of
delay-embedding sufficiency. Cite Rényi, contrast with
Kolmogorov-Sinai (Shannon-type).

### §7. Example: irrational rotation

Binary observable on the circle with irrational rotation.
Three-distance theorem gives fibre structure. Fibre mixing
constants c(α,L) ~ Θ(α_n). But reconstruction fails (δ_L ↛ 0
for binary observable), so the bridge theorem is vacuous here.
This illustrates: fibre mixing is about the transition regime,
not the endpoint.

### §8. Discussion

- Fibre mixing is novel: not temporal mixing, closest to
  Furstenberg relative mixing but different
- The derivability question is the paper's main contribution
  (either answer is a result)
- Relation to Takens genericity (fibre mixing vacuous once Φ_L
  is injective)
- The entropy characterization as a corollary

## Attribution

Must cite:
- Rokhlin (1967) for Rokhlin distance
- Rényi (1961) for collision entropy
- Furstenberg for relative mixing (distinguish)
- Steinhaus/Sós (1958) for three-distance theorem
- Takens (1981), Sauer-Yorke-Casdagli (1991) for geometric reconstruction

Should cite:
- Shields "Ergodic Theory of Discrete Sample Paths"
- Ornstein theory (for context on measure-theoretic reconstruction)
- Botvinick-Greenhouse (2025) for measure-theoretic Takens

## The honest positioning

The bridge theorem (§3) and the positive-fraction result (§4)
are proved. The entropy characterization (§6) follows. The
example (§7) is computed. The derivability question (§5) is open.

The paper can be submitted with §5 as an open question — both
the bridge theorem and the entropy characterization are
publishable results independent of derivability. The derivability
question is the bonus that would elevate the paper significantly.

## Target venue

- Ergodic Theory and Dynamical Systems (Cambridge)
- Journal of Statistical Physics
- Nonlinearity

## What you need to do (that an LLM can't)

Prove or disprove Step B. This is the theorem. Everything else
is infrastructure.
