# Step B: The Precise Problem

## Setup

Standard probability space (X, B, μ), sub-σ-algebra O ⊆ B,
quotient map Φ: X → Z with O = σ(Φ), pushforward ν = Φ*μ,
Rokhlin disintegration (μ_z, p_z).

α_z(S) := μ_z(S) for any S ∈ B.

## What's proved (Step A)

**Theorem (Positive-fraction balance).** If δ(O) > ε + 2η and
S* is an ε-maximiser of δ, then:

  ∫_{G(η)} p_z dν > 0

where G(η) = {z : p_z ≥ ε, α_z(S*) ∈ [η, 1-η]}.

In words: a positive μ-mass of large fibres is η-balanced for
any near-maximiser.

## What's needed (Step B)

**Conjecture.** Let (X, B, μ, T) be ergodic. If δ(O_L) > 0,
then for any ε-maximiser S* of δ(O_L), the set of ε-large
monochromatic fibres has zero ν-mass:

  ν({z : p_z ≥ ε, α_z(S*) ∈ {0, 1}}) = 0.

Equivalently: ν-a.e. large fibre is non-monochromatic with
respect to every near-maximiser.

## Why this is hard

Step A gives: "some positive μ-fraction of large fibres straddle
the near-maximiser."

Step B needs: "ALL (a.e.) large fibres straddle the near-maximiser."

The gap: a near-maximiser could, in principle, align with most
large fibres (making them monochromatic) while straddling just
enough to achieve δ > 0. Step A rules out COMPLETE alignment but
not DOMINANT alignment.

## The key heuristic (from Step 6)

Near-maximisers are adversarially mis-aligned with fibres:

1. A monochromatic fibre (α_z ∈ {0,1}) contributes ZERO to
   μ(S* △ E_{S*}). It is perfectly approximated by the
   majority-vote set.

2. To MAXIMISE δ, S* must straddle fibres — crossing as many
   as possible.

3. In an ergodic system, there are no non-trivial T-invariant
   sets. If S* were approximately T-invariant, the ergodic
   theorem would give α_z ≈ μ(S*) for a.e. z, hence
   α_z(1-α_z) ≈ μ(S*)(1-μ(S*)) > 0 uniformly — fibre mixing.

4. The question is whether near-maximisers of δ can be
   "adversarially structured" to align with fibres in an
   ergodic system.

## Possible proof strategies

### Strategy 1: Ergodic theorem on conditional measures

Show that for ergodic T and any S with μ(S) ∈ (0,1):

  μ_z(S) → μ(S) as the fibre C_z becomes "typical"

This would use: in an ergodic system, the orbit of a typical
point visits S with frequency μ(S), so the conditional measure
on the fibre through a typical point should reflect this.

Problem: μ_z is the conditional measure on C_z, which is a
spatial (fibre) condition, not a temporal (orbit) condition.
The orbit of x visits different fibres at different times.
Connecting the spatial disintegration to the temporal ergodic
theorem requires additional structure.

### Strategy 2: Contraposition via T-invariance

Assume ν(monochromatic large fibres) > 0 for some near-maximiser
S*. Show this forces S* to be approximately T-invariant,
contradicting ergodicity.

Sketch: if large fibres are monochromatic w.r.t. S*, then S*
is approximately a union of complete fibres. If the fibre
structure is compatible with T (fibres map to fibres), then
S* is approximately O-measurable, contradicting S* being a
near-maximiser.

Problem: fibres of Φ_L are NOT generally T-invariant. The
delay map Φ_L intertwines with the shift, not with T directly.

### Strategy 3: Direct analysis of the maximiser

Characterise the ε-maximisers of δ(O_L) explicitly. Show that
in an ergodic system, the maximiser cannot be a union of fibres
plus a small perturbation.

This is the most direct approach but requires understanding
the structure of the Rokhlin-distance maximiser, which may be
difficult.

### Strategy 4: Counterexample search

Look for an ergodic system where fibre mixing fails at some
L with δ(O_L) > 0. Candidates:

- Irrational rotation with binary observable: reconstruction
  fails (δ ↛ 0), so fibre mixing question is moot.
- Skew product with thin fibres: possible?
- Anosov diffeomorphism with bad observable: unlikely (Anosov
  systems have very good reconstruction properties).

## What you need to decide

1. Do you believe Step B is true (derivable from ergodicity)?
2. If yes: which proof strategy is most promising?
3. If unsure: try the counterexample search to build intuition.

## What the paper does WITHOUT Step B

The paper is submittable with Step B as an open question:
- Bridge theorem (§3): proved under fibre mixing
- Positive-fraction balance (§4): proved, no dynamics
- Entropy characterization (§6): corollary
- Irrational rotation example (§7): computed
- Step B as open Question 5.1

This is a legitimate research paper: two novel results (bridge
theorem, entropy characterization) + a novel condition (fibre
mixing) + a well-posed open question. Solving Step B would
elevate it significantly.
