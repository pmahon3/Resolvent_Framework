# Verification Checklist

Per tool stacking discipline: every proof in this paper was
drafted by an LLM and must be manually verified before
submission. LLMs hallucinate freely in mathematics.

## Lemma 3.1: Conditional variance identity

**Claim:** E[Var(1_S | O)] = ∫ p_z · μ_z(S) · μ_z(Sᶜ) dν(z)

**LLM proof sketch:** Var(1_S | O)(x) = E[1_S|O](x)(1-E[1_S|O](x))
= μ_z(S)μ_z(Sᶜ) on fibre C_z. Integrate against μ using
disintegration.

**Status:** ⬜ NOT VERIFIED

**Concern level:** Low. This is the law of total variance for
indicators. Standard. But verify the disintegration step: does
∫ μ_z(S)μ_z(Sᶜ) dμ(x) = ∫ p_z μ_z(S)μ_z(Sᶜ) dν(z)?  Yes, by
μ = ∫ μ_z p_z dν. Should be correct.

## Inequality (3.4): α(1-α) ≤ min(α, 1-α)

**Claim:** For α ∈ [0,1], α(1-α) ≤ min(α, 1-α).

**Status:** ⬜ NOT VERIFIED

**Check:** If α ≤ 1/2: min = α, and α(1-α) ≤ α since 1-α ≤ 1. ✓
If α ≥ 1/2: min = 1-α, and α(1-α) ≤ 1-α since α ≤ 1. ✓
**Correct.**

## Theorem 3.2: Easy direction

**Claim:** δ(O) = 0 implies (μ⊗μ)(R) = 0.

**LLM proof:** δ = 0 means O = B mod μ. A fibre of positive mass
would give μ_z(S) ∈ (0,1) for some S, contradicting O = B.

**Status:** ⬜ NOT VERIFIED

**Concern:** The argument that "a fibre of positive mass
contradicts O = B" needs care. If C_z has positive mass and O = B,
then C_z ∈ O (since C_z = Φ⁻¹(z) ∈ O), so C_z is both O-measurable
and B-measurable. This doesn't immediately contradict anything.
The issue is: if C_z has positive mass, take S = any measurable
subset of C_z with μ(S) ∈ (0, μ(C_z)). Then μ_z(S) ∈ (0,1). But
S should be O-measurable (since O = B), which means S = Φ⁻¹(A)
for some A. But S ⊂ C_z = Φ⁻¹(z), so S = Φ⁻¹(A) ∩ Φ⁻¹(z) =
Φ⁻¹(A ∩ {z}). Since z is a single point, A ∩ {z} is either {z}
or ∅, giving S = C_z or S = ∅. Contradiction with μ(S) ∈ (0, μ(C_z)).

**This argument IS correct** but needs the step "S ⊂ C_z and
S ∈ O implies S ∈ {∅, C_z}" to be made explicit.

## Remark after Theorem 3.2

**Claim:** The converse (collision → 0 implies δ → 0) is false
without fibre mixing.

**Status:** ⬜ NOT VERIFIED — need a counterexample

**Concern:** Is there actually a sub-σ-algebra where collision
probability is 0 but Rokhlin distance is positive? If all fibres
have p_z = 0, then the fibre decomposition is essentially
continuous — this seems like it should give δ = 0 too. The claim
might be wrong. Need to check: can (μ⊗μ)(R) = 0 with δ > 0?

Actually (μ⊗μ)(R) = ∫ p_z² dν. If this is 0, then p_z = 0
ν-a.e. But if the quotient is atomless (continuous), p_z = 0
for all z and the fibres are singletons, giving O = B. So
(μ⊗μ)(R) = 0 DOES imply δ = 0.

**The remark is about SEQUENCES:** (μ⊗μ)(R_L) → 0 does not imply
δ(O_L) → 0. The collision probability going to 0 means fibres
are shrinking, but δ going to 0 means the σ-algebra is generating.
These are different for a SEQUENCE of sub-σ-algebras even though
they agree for a single one.

**The remark as stated is misleading.** Fix: it should say
"for a sequence O_L" not "in general."

## Theorem 3.3: Hard direction

**Claim:** Under fibre mixing, c((μ⊗μ)(R) - ε) ≤ δ(O).

**LLM proof:** Fibre mixing gives μ_z(S*)μ_z(S*ᶜ) ≥ c·p_z for
large z. Multiply by p_z, integrate. Left side ≤ δ by (3.4).
Right side = c(collision - small fibres) ≥ c(collision - ε).

**Status:** ⬜ NOT VERIFIED

**Concerns:**
1. The proof uses "Let S* be any set in B" but then applies
   fibre mixing with S*. Fibre mixing (Def 2.3) requires the
   condition to hold for ALL S. So this is correct: for any S*,
   the inequality holds.

2. The bound ∫_{p_z < ε} p_z² dν ≤ ε: since p_z < ε on this
   set, p_z² < ε·p_z, so ∫ p_z² dν < ε ∫ p_z dν = ε. ✓

3. The left side ∫_{p_z ≥ ε} p_z μ_z(S*)μ_z(S*ᶜ) dν is
   bounded by ∫ p_z μ_z(S*)μ_z(S*ᶜ) dν ≤ δ by (3.4).
   Wait — (3.4) bounds the SUP over S, not for a specific S*.
   For a specific S*, the integral equals E[Var(1_{S*}|O)] which
   is ≤ sup_S E[Var(1_S|O)] ≤ δ. ✓

4. The bound gives δ ≥ c(collision - ε) for EACH fixed ε. As
   a function of the sequence O_L: if collision_L → 0, then for
   any ε > 0, eventually collision_L < ε, giving δ_L ≥ 0. This
   is trivial. The bound should give δ_L → 0 from collision_L → 0.
   Rearranging: collision_L ≤ δ_L/c + ε. Taking ε → 0:
   collision_L ≤ δ_L/c. So collision → 0 implies δ → 0 (since
   collision ≤ δ/c). Wait, that's the WRONG direction — we want
   collision → 0 ⟹ δ → 0.

   The bound says: δ ≥ c(collision - ε). So collision ≤ δ/c + ε.
   This gives collision BOUNDED BY δ, which is the easy direction
   again.

   **THE HARD DIRECTION BOUND IS BACKWARDS IN THE PAPER.**

   The hard direction should say: δ ≤ f(collision), not δ ≥ g(collision).
   We need: if collision → 0 then δ → 0, i.e., δ ≤ something
   involving collision.

   **THIS IS A SERIOUS ERROR IN THE DRAFT.**

   The bridge note's actual argument is different from what's in
   the LaTeX. Need to re-derive from the bridge note source.

## Theorem 4.1: Positive-fraction balance

**Status:** ⬜ NOT VERIFIED — proof has acknowledged issues with
the I_S bound. The statement was weakened to ∫_{G(η)} p_z dν > 0.
Needs careful derivation from Step 7 notes.

## Corollary 6.1: Entropy characterization

**Claim:** δ → 0 iff H₂ → ∞.

**Status:** ⬜ NOT VERIFIED — depends on the bridge theorem being
correct, which has the direction error above.

## Proposition 7.1: Irrational rotation

**Status:** ⬜ NOT VERIFIED — proof sketch only ("follows from
three-distance theorem"). The actual computation is in the
archived notes.

## CRITICAL ISSUE

**The hard direction proof (Theorem 3.3) has the inequality
pointing the wrong way.** The bound δ ≥ c(collision - ε) says
"if collision is large then δ is large" — that's the easy
direction dressed up. The hard direction needs "if collision is
small then δ is small," which requires a bound δ ≤ f(collision).

**Action required:** Go back to the bridge note source material
and re-derive the hard direction carefully. The LLM proof is
wrong. This is exactly why tool stacking matters.
