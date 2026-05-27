# Characterising Missing Auxiliary Information from κ_Q

**Status:** Seed note (Phase 1). Not audited.  
**Date:** 2026-05-27  
**Parent material:** `disintegration_diagnostic.md` (parked), MITACS P1
result (S11), Paper I companion note

---

## The question

Given a probability space (Ω, F, μ), observable Y, loss L, and a
conditioning sub-σ-algebra Q ⊂ F, define the conditional Bayes risk
R*(Q) := inf_{f ∈ L⁰(Q)} E[L(Y, f(Q))]. The identifiability
obstruction (`disintegration_diagnostic.md`) shows that κ_Q alone
cannot distinguish structured noise (R*(Q) is floor) from noisy
structure (∃ Z with R*(Q ∨ σ(Z)) < R*(Q)).

**The deductive question:** Is there a way to characterise, from
properties of κ_Q alone, the *type* of auxiliary information that
would reduce R*(Q)?

That is: instead of the abductive strategy (enumerate candidate Z's,
test each — P1's approach), can we *read* the structure of κ_Q and
deduce what kind of Z would help? Not which specific Z, but what
*structural properties* Z must have to reduce the residual risk.

The distinction is between:
- **Abductive:** guess Z, test, iterate (Patra-Sen stratification, SDR,
  ICA — all variations on "try and see")
- **Deductive:** from the conditional law's internal structure, derive
  constraints on what Z can and cannot look like

## Why the question is non-trivial

The identifiability obstruction says you *cannot* determine whether
R*(Q) is the floor. But it does not say you cannot constrain the
*form* of Z if it exists. There is a gap between:

1. "κ_Q cannot tell you whether Z exists" (the obstruction, proved)
2. "κ_Q cannot tell you anything about what Z would look like if it
   existed" (stronger claim, status unknown)

Claim 2 does not follow from claim 1. The obstruction is about
*existence*; the question here is about *structure conditional on
existence*. These are logically independent.

**Motivating evidence (P1, S11).** The periodicity in α̂_L(s) across
hour_of_week bins was visible *in κ_Q's residuals* before anyone
specified hour_of_week as a candidate. The PIT residuals carried
a weekly signature — bin 6 (Sat daytime) at α̂_L = 0.61, bin 0
(Mon daytime) at 0.035. A 17:1 ratio in mixture fraction across
strata. This structure was there to be read. The question is whether
there is a principled way to extract it without pre-specifying the
stratification.

## Prior art: what existing methods access

Three established programmes recover missing structure from residuals.
All work on (Y, X) pairs or multivariate observations, not on κ_Q
directly:

**Sufficient dimension reduction (SDR).** SIR, SAVE, MAVE (Cook, Li,
Xia). Recovers the central subspace E(X | Y) or Var(X | Y). Works
with first and second conditional moments of X given Y. Does not
use the full conditional law — only summary statistics.

**Independent component analysis (ICA).** FastICA (Hyvärinen). Finds
the linear transformation that maximises non-Gaussianity of
components. Uses higher-order cumulants (kurtosis, negentropy) of
the marginal distribution of residuals. Does not condition — works
on the joint.

**Causal discovery.** LiNGAM (Shimizu), FCI (Spirtes). Uses non-
Gaussianity of residuals to infer causal direction. Exploits the
asymmetry: if X → Y with non-Gaussian noise, then Y → X would
require Gaussian noise (Darmois-Skitovitch). Works on bivariate or
multivariate marginals.

## The discriminating question

**Does κ_Q — the full conditional law from Rokhlin disintegration —
contain information that SDR/ICA/causal discovery cannot access?**

κ_Q is strictly richer than what these methods use:

- SDR uses E(X | Y) and Var(X | Y). κ_Q gives the entire conditional
  distribution, including all higher moments, tail behaviour, and
  shape variation across conditioning states.

- ICA uses the marginal distribution of residuals (pooled across
  states). κ_Q gives the state-by-state conditional law — you can see
  *where* the non-Gaussianity lives, not just *that* it exists.

- Causal discovery uses pairwise or low-dimensional marginals. κ_Q
  encodes the full dependence structure of Y on Q.

The P1 result is suggestive: the per-stratum α̂_L variation (a
property of κ_Q's fiber-by-fiber structure) revealed hour_of_week as
the binding axis. SDR/ICA working on pooled residuals might find the
same signal — or might not, because pooling across strata averages
out the variation that P1 detected.

**The precise question:** Is there a functional T of κ_Q (not just of
the marginal residual distribution, not just of conditional moments)
that constrains the structure of any Z satisfying R*(Q ∨ σ(Z)) <
R*(Q)?

## Candidate formalisation directions

### Direction 1: Variation of conditional shape

Define the "shape variation" of κ_Q across its fibers:

> V(κ_Q) := variation of q ↦ shape(κ_Q(· | q))

where "shape" is some normalisation-invariant summary (e.g., tail
index, kurtosis profile, mixture fraction). If V(κ_Q) is large, the
conditional law's shape depends on q, meaning Q is interacting with
some latent structure. If V(κ_Q) is small, the conditional law is
shape-invariant across Q — consistent with either structured noise or
a Z orthogonal to Q.

P1 measured a version of this: the range of α̂_L across strata is a
measure of V(κ_Q) restricted to the mixture-fraction functional.
Could this be made precise and general?

### Direction 2: Conditional characteristic function regularity

κ_Q induces a family of characteristic functions φ_q(t) := E[e^{itY}
| Q = q]. The regularity of q ↦ φ_q(·) encodes how the conditional
law varies. Singularities, non-analyticities, or slow decay in φ_q
constrain what latent structure could produce the observed family.

Connection to ICA: ICA's non-Gaussianity detection is equivalent to
testing whether φ has Gaussian decay. The fiber-by-fiber version
tests this *per conditioning state*, which is strictly more
informative.

### Direction 3: Information-geometric approach

The family {κ_Q(· | q) : q ∈ Q} is a statistical manifold. Its
Fisher geometry (curvature, geodesics, exponential family structure)
encodes how the conditional law deforms across Q. If Z exists and
is informative, conditioning on Z should "flatten" this manifold
(reduce curvature) — the conditional laws become more homogeneous
when you condition on the right thing.

Connection to SDR: the central subspace is the projection of this
manifold onto the X-directions that preserve the conditional
distribution of Y. But SDR typically works with parametric or
semiparametric summaries, not the full information geometry.

### Direction 4: Disintegration tower

σ-additivity gives Rokhlin disintegration: μ = ∫ κ_Q(· | q) dν(q).
If Q ⊂ Q' ⊂ F, we get a tower:

> μ = ∫∫ κ_{Q'}(· | q') dν'(q' | q) dν(q)

The "inner" disintegration ν'(· | q) describes how Q' refines Q.
The question becomes: what properties of κ_Q constrain the possible
inner disintegrations that would reduce R*?

This is the most measure-theoretically natural framing. It uses
σ-additivity essentially (disintegration requires it), which
connects back to Paper I's "what does σ-additivity buy?" question.

## What would constitute a result

Ranked by ambition:

1. **A functional T(κ_Q) that is nonzero iff ∃ Z reducing R*(Q).**
   This would resolve the identifiability obstruction, which we know
   is impossible in general. So T cannot exist — but understanding
   *why* it cannot exist at this level of generality is informative.

2. **A functional T(κ_Q) that, given the existence of Z, constrains
   σ(Z) up to equivalence class.** "If Z exists, it must be
   measurable with respect to some sub-σ-algebra in class C." This
   is weaker than identifying Z but stronger than nothing.

3. **A characterisation of which features of κ_Q are preserved vs
   destroyed by marginalising over Z.** "The following properties of
   κ_Q are invariant under refinement Q → Q ∨ σ(Z); the following
   are not." This tells you where to look in κ_Q for traces of Z.

4. **A proof that (2) or (3) is impossible at some level of
   generality, with a precise statement of what additional structure
   is needed.** This would sharpen the identifiability obstruction
   from "you can't tell" to "you can't tell, and here is the exact
   structural assumption needed to make progress."

## Connections

- **Paper I:** σ-additivity guarantees disintegration exists. This note
  asks what the disintegration's *internal structure* reveals.
  Thematic connection, not derivation.

- **P1 / MITACS:** P1 is the empirical evidence that κ_Q's fiber-by-
  fiber structure carries Z-information. This note asks whether that
  observation can be made systematic.

- **SDR / ICA / causal discovery:** prior art on the abductive
  version. The question is whether the deductive version (using κ_Q
  rather than (Y, X) pairs) adds anything.

- **Identifiability obstruction (Bergna et al., Heckman-Singer):**
  constrains what's possible. This note works in the gap between
  "Z not identifiable" and "Z structure not constrainable."

## Phase 2 audit requirements

Before committing further:

- [ ] Literature scout: "characterising missing covariates from
  conditional distributions," "sufficient statistics for latent
  variable structure," "information geometry of mixture families"
- [ ] Check whether Direction 4 (disintegration tower) reduces to
  known sufficient-statistic theory (Bahadur, Dynkin, Rao-Blackwell)
- [ ] Check whether Direction 3 (information geometry) is covered by
  Amari's framework or the e/m-projection literature
- [ ] Devil's advocate: "this is just asking for a sufficient
  statistic for model misspecification, which is model-dependent
  by definition"
