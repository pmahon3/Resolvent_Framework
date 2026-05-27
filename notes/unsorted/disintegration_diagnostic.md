# Disintegration as Diagnostic: The Structured-Noise/Noisy-Structure Obstruction

**Status:** PARKED (2026-05-26, updated 2026-05-27). Phase 2 audit:
identifiability obstruction is published (Bergna et al. 2026,
Heckman–Singer 1984, Allahverdyan 2020); monotonicity is textbook
(Blackwell 1951); stratified Patra–Sen is Deb et al. (JASA 2022).
No theorem or methods novelty survives. Framework adopted by MITACS
missing\_content\_memo as interpretive structure; P1 (stratified
Patra–Sen localization) settled R-A with hour\_of\_week binding.  
**Date:** 2026-05-21 (rewritten 2026-05-26, parked 2026-05-26,
updated 2026-05-27)  
**Parent material:** Paper I (companion note), withdrawn Paper II,
MITACS qualifier\_exhaustion\_memo.tex, MITACS missing\_content\_memo.tex

---

## The open question from Paper I

Paper I's companion note establishes that σ-additivity is not
first-order axiomatizable. The implicit question: *what does
σ-additivity actually buy?*

The standard answer is "Rokhlin disintegration exists." This note
asks what that answer *forces* about concrete analytic decisions.

## The framework-level object: conditional Bayes risk

Given a probability space (Ω, F, μ), observable Y, loss L, and a
conditioning sub-σ-algebra Q ⊂ F, the conditional Bayes risk is:

> R\*(Q) := inf\_{f measurable w.r.t. Q} E[L(Y, f(Q))]

This is a property of (μ, Q, L) alone — no model class, no estimator,
no kernel family. It exists because σ-additivity guarantees the
conditional expectation (and hence the infimum over measurable
predictors) is well-defined.

The total risk of any estimator decomposes as:

> Risk(estimator) = R\*(Q) + model-class gap + estimation error

## The monotonicity theorem (tower property)

For Q ⊂ Q' ⊂ F:

> R\*(Q') ≤ R\*(Q)

This is immediate from iterated conditional expectations. It is not
new mathematics — it is measure theory. But it is the formal backbone
of the framework: σ-algebra refinement is *guaranteed* to reduce the
Bayes-optimal risk (or leave it unchanged). Equality holds iff Y is
already conditionally independent of Q' \ Q given Q.

## The decision the user faces

Given an estimator with unsatisfactory risk, the decomposition offers
two levers:

1. **Reduce the model-class gap** (kernel refinement): use a more
   flexible model family to better approximate the true κ\_Q.

2. **Reduce R\*(Q)** (σ-algebra enrichment): condition on more
   information, moving from Q to some Q' ⊃ Q.

The practical question: *which lever to pull?* The framework forces
this to be the right question. It does not force the answer.

## The obstruction: structured noise vs noisy structure

**Claim (identifiability obstruction).** Given only the conditional
kernel κ\_Q and its residual distribution, the following two data-
generating processes are observationally indistinguishable:

**(a) Structured noise (heavy-tailed innovation).** The true
conditional law κ\_Q(·|q) is heavy-tailed for intrinsic reasons.
R\*(Q) is the irreducible floor. Refining Q is futile; the right
move is kernel refinement (accommodate the heavy tails).

**(b) Noisy structure (latent conditional heterogeneity).** There
exists Z ∉ σ(Q) such that κ\_{Q∨σ(Z)}(·|q,z) is lighter-tailed,
and the observed heavy tails in κ\_Q are a mixture artifact from
marginalising over Z. R\*(Q) is *not* the floor — R\*(Q') < R\*(Q)
for Q' = Q ∨ σ(Z). The right move is σ-algebra enrichment.

**These produce identical κ\_Q.** No diagnostic built from κ\_Q alone
can distinguish them. This is not a practical difficulty — it is a
theorem. The structured-noise/noisy-structure ambiguity is inherent
in the conditional law.

## What resolves the ambiguity

The framework identifies exactly three types of auxiliary information
that break the tie:

1. **A candidate Z.** Test whether conditioning on Z reduces residual
   risk. If it does, you were in regime (b). This is empirically
   checkable but requires having Z in hand.

2. **A comparison model class.** If a strictly richer model class
   (e.g., mixture-of-Gaussians, non-parametric) materially reduces
   risk *at the same Q*, you haven't yet exhausted the model-class
   gap — you're in regime (a) at the model level, regardless of
   whether (a) or (b) holds at the population level.

3. **A structural noise assumption.** If you have domain knowledge
   constraining the innovation distribution (e.g., "innovation noise
   is Gaussian" from physics), then any observed non-Gaussianity is
   evidence for (b). This converts the underdetermined problem into a
   hypothesis test — but the assumption is external to the framework.

## The contribution

The framework's contribution is *not* a diagnostic algorithm. It is:

1. **Making the decomposition precise.** Risk = R\*(Q) + model-class
   gap + estimation error. Each term is well-defined because
   σ-additivity guarantees disintegration.

2. **Proving monotonicity.** R\*(Q') ≤ R\*(Q) is the formal guarantee
   that σ-algebra enrichment cannot hurt (at the population level).

3. **Characterising the obstruction.** The structured-noise/noisy-
   structure ambiguity is *provably* not resolvable from κ\_Q alone.
   The framework tells you *what kind* of auxiliary information is
   required and *why* an intrinsic diagnostic cannot exist.

4. **Identifying the resolution types.** The three auxiliary-
   information types (candidate Z, comparison model class, structural
   noise assumption) are exhaustive at the framework level.

This is the bridge from Paper I ("σ-additivity is invisible to finite
tests") to applied practice ("here is what σ-additivity gives you,
here is where it stops, and here is what you need beyond it").

## Patra–Sen as a specific statistical proxy

The Patra–Sen (2016) mixture decomposition fits into this framework
as an *implementation* of auxiliary-information type 3: it assumes a
Gaussian reference family and estimates the non-Gaussian mixture
fraction α₀. Under that structural assumption:

- α₀ > 0 is evidence for regime (b) (noisy structure), *given* the
  Gaussian innovation assumption.
- The assumption is doing the work — Patra–Sen doesn't resolve the
  ambiguity; it converts the ambiguity into a bet on the noise model.

The MITACS qualifier\_exhaustion\_memo findings (α̂\_L ≥ 0.49–0.74,
orthogonal to z-state) are interpretable as: *under* Gaussian-
innovation assumption, massive non-Gaussian fraction, but it doesn't
covary with the conditioning variable. This is consistent with both
(a) non-Gaussian innovation and (b) latent Z unrelated to the delay
embedding. The framework correctly predicts this is underdetermined.

## Applied evidence (MITACS, updated 2026-05-27)

### Baseline (qualifier\_exhaustion\_memo, 2026-05-21)

- Rebaseline kurtosis 24–33 in κ\_Q residuals.
- Patra–Sen α̂\_L^{95%} ≥ 0.49–0.74.
- K lever (Student-t): ~1.8% deviance improvement.
- S lever (bandwidth): no kurtosis reduction.
- Contamination orthogonal to z-state.

### Q1 (Student-t kernel, 2026-05-26) — S8

Student-t kernel reduces marginal χ² by 16× (22,328 → 1,371) but
does not calibrate. ν̂ per day-type: weekday 4.19, saturday 4.62,
sunday 4.61. D\_RATIO shrinks 10× (28.96 → 2.93). Heavy-tailedness
lives in the κ̂₁ innovation, not the seasonal climatology (M1
outperforms M2). Picture (C) survives the family lift.

### Q2A (richer families, 2026-05-26) — S9

Mixture-2-Gaussian, mixture-3-Gaussian, KDE residual law all
χ²-indistinguishable (~954). KDE marginally worst. M0→M1 = 16×;
M1→Q2A-best = 1.44×. **Kernel-refinement lever exhausted.**
Saturday ~4× weekday across all three families (family-invariant).

### Q2B (non-distributional mechanisms, 2026-05-26) — S10

Mean-bias: +0.109 share (below 0.15 null floor). Variance cap:
−0.114 (sign-determined negative). Seam exclusion: −0.139 (sign-
determined negative). **All three pre-registered same-Q mechanisms
inadequate; two actively worsened calibration.** Under-dispersion
signature (σ²\_iter < σ²\_empirical at virtually every cell) is the
substantive positive: canonical signature of missing exogenous
content.

### P1 (stratified Patra–Sen localization, 2026-05-27) — S11

First applied response to the identifiability obstruction. Per-
stratum α̂\_L on Q1's M1 PIT residuals across five axes. Verdict
R-A at landslide strength. Hour\_of\_week is the binding axis
(range 0.575). Hot zone: Fri 10:00–Sun 23:00 (α̂\_L 0.55–0.61).
Cold zone: Mon 01:00–21:00 (α̂\_L 0.035). **Missing-Z is cyclical/
social-weekly, not seasonal/climatological.**

### Framework interpretation (updated)

S9 + S10 jointly map the boundary of the distributional-class axis:
kernel refinement plateaus AND naive same-Q manipulations fail.
This is applied evidence for the identifiability obstruction. P1
then breaks the tie by introducing auxiliary information (per-
stratum stratifications outside Q) exactly as the framework's
resolution paths prescribe. The localization succeeded where
decomposition failed because P1 introduced information outside
the σ-algebra Q2B was confined to.

The missing\_content\_memo (§"Framework-level interpretation")
explicitly adopts the R\*(Q) decomposition and identifiability
obstruction from this note as its interpretive structure.

## Phase 2 audit result (2026-05-26)

Literature scout found the identifiability obstruction published as a
formal proposition in multiple traditions:

| Component | Status | Reference |
|-----------|--------|-----------|
| Non-identifiability from κ\_Q alone | Published (Prop 1) | Bergna et al. (arXiv:2605.06413, 2026) |
| Same in mixture-model language | Published | Allahverdyan (arXiv:2002.07884, 2020) |
| Same in factor-model language | Published | Hu, Xie, Zhang, Zhou (arXiv:2506.05116, 2026) |
| Same in duration-model language | Published | Heckman–Singer (Econometrica, 1984) |
| Scale-mixture transparency | Published | Andrews–Mallows (JRSSB, 1974) |
| R\*(Q) monotonicity | Textbook | Blackwell (1951); tower property |
| Risk decomposition | Textbook | Standard statistical learning theory |
| Auxiliary info to break tie | Published | Manski (2003); causal inference lit |
| Unified framework paper | Not published | Framing only |
| ~~Patra–Sen conditional diagnostic~~ | ~~Not published~~ | ~~Genuinely absent~~ |
| Patra–Sen with covariate-dependent π\* | **Published** | Deb, Saha, Guntuboyina, Sen (JASA 2022; arXiv:1810.07897) |
| Adequacy-of-conditioning test | **Published** | Deb et al. (2022) Section 6 + distance covariance |

**Verdict:** Park. Theorem contributions are known. The one diagnostic
tool claimed as novel (stratified Patra–Sen) is a discretised special
case of Deb et al. (2022), co-authored by Sen of Patra–Sen. No
methods novelty survives. The *diagnostic value* is unchanged — P1
ran it on Ontario data (2026-05-27) and got a decisive signal
(hour\_of\_week binding axis, R-A at landslide strength).

---

## What survives: applied guidance from the literature

The following references address the structured-noise/noisy-structure
decision *practically* — i.e., they offer methods for breaking the
tie in applied settings like the MITACS electricity-demand problem.

### (a) Patra–Sen conditional extension — DONE BEFORE

**~~This is the novel applied contribution that survives the audit.~~**
**Second-pass audit (2026-05-26): methods novelty killed by Deb et al.
(JASA 2022). Diagnostic value unchanged — P1 ran it and it worked.**

The idea of stratifying Patra–Sen by conditioning state to detect
state-dependent mixture structure is a discretised special case of:

**Deb, Saha, Guntuboyina, Sen (JASA 2022; arXiv:1810.07897).**
"Two-Component Mixture Model in the Presence of Covariates."
Co-authored by Sen of Patra–Sen (2016). Generalises to covariate-
dependent π\*(x) with a tuning-parameter-free NPMLE. Section 6
explicitly poses the σ-algebra adequacy question: "first check that
[the unconditional two-groups model] is inadequate. Only then does
it make sense to model the dependence between Y and X." Reduces to
a distance-covariance independence test (Székely et al. 2007).

The lab's per-stratum α̂\_L(s) is the discretised, less efficient
version of what Deb et al. handle continuously. No methodological
gap. See full scout report at
`MITACS/notes/literature/2026-05-26_stratified-patra-sen-scout.md`.

**What survives: the diagnostic worked empirically (P1, 2026-05-27).**
The MITACS P1 experiment ran per-stratum Patra–Sen on Q1's M1 PIT
residuals (n=12,000, 1000-rep paired-day bootstrap). Results:

| Axis | Range | Binding? |
|------|-------|----------|
| hour\_of\_week | 0.575 [0.448, 0.648] | **YES** |
| time\_of\_day | 0.485 [0.385, 0.578] | |
| day\_type | 0.345 [0.250, 0.430] | |
| season | 0.135 [0.055, 0.240] | |
| demand\_quantile | 0.075 [0.023, 0.173] | |

Verdict R-A at landslide strength (cut at 0.20; binding axis clears
at >2× the cut at the lower CI bound). Hot zone: bins 5/6/7
(Fri 10:00 – Sun 23:00, α̂\_L 0.55–0.61). Cold zone: bin 0
(Mon 01:00–21:00, α̂\_L 0.035).

**Substantive headline:** the missing-Z structure is cyclical/social-
weekly, not seasonal/climatological. The proponent's temperature-
via-season prior was 95%-CI-falsified (season range CI upper 0.240
vs predicted 0.30). The day\_type ranking (saturday 0.6475 > sunday
0.485 > weekday 0.3025) independently corroborates Q2A's finding
S9b and eigenmodes-v1's S2/S3 from a distinct estimator.

**Thread advancement:** P1 routes to Q1A — condition M3 (mixture-2-
Gaussian) on hour\_of\_week and test whether marginal χ² drops below
228 (Q2A's R-A2 gate-derived corroboration cut). Three Z
constructions pre-flagged: binary weekend indicator, 8-level
categorical, continuous mod-168 phase. Q1A is the next experiment.

**Key references:**
- Deb, Saha, Guntuboyina, Sen, "Two-Component Mixture Model in the
  Presence of Covariates," JASA 117(540), 2022. arXiv:1810.07897.
- Patra and Sen, "Estimation of a Two-Component Mixture Model with
  Applications to Multiple Testing," JRSSB 78(4), 2016.
- Scott, Kelly, Smith, Zhou, Kass, "False Discovery Rate Regression,"
  JASA 110(510), 2015. (Earlier covariate-dependent two-groups.)
- Arias-Castro and Jiang, extensions to shape-constrained backgrounds,
  arXiv:2106.13925, 2021. (Unconditional only — confirmed.)

### (a′) Patra–Sen generalization landscape

The Patra–Sen estimator targets the *maximum identifiable proportion*
α\* = sup{α : F − αF₀ is a valid sub-CDF}. This equals the true α₀
iff F₁ is **irreducible** w.r.t. F₀ (Blanchard–Lee–Scott, JMLR 2010):
F₁ cannot itself be decomposed as a mixture involving F₀. Without
irreducibility, no estimator can recover the true α₀ from F alone —
only the lower bound α\*.

**Published generalization frontier:**

| Generality of F₀ | Reference | Guarantees |
|---|---|---|
| Fully known (single distribution) | Patra–Sen (2016) | Distribution-free finite-sample LCB |
| Symmetric, monotone, or log-concave | Arias-Castro–Jiang (2021) | Consistency + confidence bands |
| k-monotone (Bayesian) | Wang–Ghosal (2023) | Posterior contraction rates; no finite-sample LCB |

**Open problems (relevant to MITACS):**

1. **F₀ parametric with unknown parameters.** If the reference is
   Gaussian(μ, σ²) with unknown μ, σ², or Student-t(ν) with unknown ν,
   you must estimate parameters first. The plug-in destroys the
   distribution-free finite-sample property — the distinctive feature
   of Patra–Sen. Nobody has recovered it. This matters because the
   MITACS application is currently locked into a Gaussian reference,
   and the 1.8% Student-t improvement suggests reference choice matters.

2. **General function class / metric formulation.** "What fraction of
   the data lies within TV-distance ε of class C?" — unstudied. Sits
   at the intersection of contamination estimation and robust hypothesis
   testing. No published formulation in these terms.

**Relaxation of irreducibility:** Zhu, Fjeldsted, Holland, Landon,
Lintereur, and Scott (ICML 2023) partially relax the irreducibility
condition with a resampling-based meta-algorithm. The identifiability
barrier is relocated, not eliminated.

**Additional references:**
- Blanchard, Lee, and Scott, "Semi-Supervised Novelty Detection,"
  JMLR 11, 2010 (irreducibility condition).
- Zhu et al., ICML 2023 (relaxed identifiability).
- Meinshausen and Rice, Annals of Statistics, 2006 (precursor:
  LCB for proportion of false nulls in multiple testing).

### (b) Rokhlin-disintegration unification (framing only)

The observation that Heckman–Singer (duration models), Bergna et al.
(Bayesian deep learning), Allahverdyan (mixture models), and
Manski (partial identification) are all instances of the same
measure-theoretic phenomenon — non-identifiability of the
decomposition of κ\_Q into "intrinsic" vs "mixture artifact" — is not
published as a unifying paper. But it's also not a theorem. It's a
survey observation. Filing under "possible expository note if the
traditions haven't noticed each other" but not a research priority.

### (c) How Bergna et al. (2026) break the tie

Their solution: **synthetic priors with known ground-truth
decomposition.** Train a model on synthetic data where you control
the split between aleatoric and epistemic uncertainty. The model
learns to decompose on synthetic data (where the answer is known) and
transfers to real data (where it isn't). This is auxiliary-information
type 3 (structural assumption) — the assumption being that the
decomposition learned from synthetic DGPs transfers to real data.

**Relevance to MITACS:** This is conceptually similar to the "synthetic
calibration" step in the original seed note (step 4 of the diagnostic
chain). Run the estimation pipeline on a known-Gaussian DGP with
matched autocorrelation → measure the α̂\_L floor → attribute excess
to structure. Bergna et al. provide a more sophisticated version of
this idea, but the principle is the same: you need a reference DGP
where the decomposition is known.

### (d) How Heckman–Singer (1984) break the tie

Their solution: **time-varying covariates or repeated spells.** If you
observe the same unit at multiple time points and the "unobserved
heterogeneity" is stable while the "true duration dependence" varies,
you can separate them. This is auxiliary-information type 1 (candidate
Z = time itself, used as an instrument).

**Relevance to MITACS:** The Ontario demand data *is* a time series —
you have repeated observations of the same system. If the heavy-tailed
component is stable across different regimes (seasons, demand levels)
while the conditional structure varies, that's evidence for structured
noise. If the heavy-tailed component varies with regime, that's
evidence for noisy structure. This is exactly what the MITACS memo
found: contamination orthogonal to z-state. Under Heckman–Singer logic,
that's evidence for structured noise (or a Z unrelated to the delay
embedding).

### (e) Practical decision tree for the MITACS problem (updated)

The framework prescribed four resolution paths. As of 2026-05-27,
the first two have been executed and the answer is clear:

1. ~~**Test candidate Z's directly**~~ → **NEXT (Q1A).** P1
   identified hour\_of\_week as the binding axis. Q1A will
   condition M3 on hour\_of\_week and test whether χ² drops below
   228. Three Z constructions pre-flagged.

2. ~~**Stratified Patra–Sen**~~ → **DONE (P1, S11).** R-A at
   landslide strength. α̂\_L varies from 0.035 (Mon daytime) to
   0.61 (Sat daytime). The contamination is *not* orthogonal to
   all conditioning — it's concentrated on the social-weekly cycle.
   This is noisy structure, not structured noise, at least along
   the hour\_of\_week axis.

3. **Synthetic calibration** (Bergna approach): not yet run. On the
   resolution-paths-thread as P2, downstream of Q1A if R-C1A fires.

4. ~~**Comparison model class**~~ → **DONE (Q1 + Q2A, S8 + S9).**
   Student-t reduces χ² 16×; richer families add 1.44× more. Kernel-
   refinement lever exhausted. The remaining ~954 χ² is not
   distributional.

**Current state:** the framework's diagnosis is confirmed. Kernel
refinement is exhausted (S9). Same-Q manipulations fail (S10).
Stratified localization identifies hour\_of\_week as the missing Z
(S11). The next experiment (Q1A) tests whether explicitly
conditioning on hour\_of\_week resolves the residual pathology. If
R-A1A fires, the resolution-paths-thread RESOLVES.

### (f) Data-driven Z-recovery tools (SDR, ICA, causal discovery)

P1 found hour\_of\_week by pre-specifying five candidate axes and
testing each. An alternative approach: let the data surface the
missing Z without pre-specification. Three established programmes
do versions of this, and all are applicable to κ̂\_Q's residuals.

**Sufficient dimension reduction (SDR).** Recovers the *central
subspace* — the minimal sufficient linear reduction of X for
predicting Y — without specifying a regression model. Key methods:

- SIR (sliced inverse regression; Li 1991)
- SAVE (sliced average variance estimation; Cook & Weisberg 1991)
- MAVE (minimum average variance estimation; Xia et al. 2002)

Applied to κ̂\_Q residuals: regress PIT residuals against a candidate
covariate matrix (time features, calendar indicators, lagged demand)
via SIR/SAVE. If the estimated central subspace loads heavily on
hour\_of\_week-like features, that corroborates P1 without pre-
specification. If it finds additional directions P1 missed, those
become candidate Z's for further experiments.

**Key reference:** Cook, *Regression Graphics* (1998); Cook,
*An Introduction to Envelopes* (2018).

**Independent component analysis (ICA).** Decomposes a multivariate
signal into maximally non-Gaussian independent components. Under the
structural-noise/noisy-structure framing: if the residuals have a
latent mixture structure driven by a missing Z, ICA should recover a
component aligned with that Z.

Applied to κ̂\_Q residuals: run FastICA (Hyvärinen & Oja 2000) on a
matrix of (residual, time-feature) pairs. If one IC loads on the
social-weekly cycle, that's independent confirmation of P1's finding
from a non-parametric angle.

**Key reference:** Hyvärinen, Karhunen, and Oja, *Independent
Component Analysis* (2001).

**Causal discovery from non-Gaussianity.** The LiNGAM framework
(Shimizu et al. 2006) exploits non-Gaussianity of residuals to
identify causal direction in linear models. FCI (Spirtes et al. 2000)
handles latent confounders. In the MITACS context: non-Gaussianity in
κ̂\_Q's residuals is the *signal*, not noise — it's the evidence that
a latent common cause (the missing Z) exists.

Applied to κ̂\_Q residuals: run LiNGAM or FCI on (demand, price,
calendar features, PIT residuals). If the algorithm infers a latent
variable feeding into the residuals with a weekly structure, that
identifies the missing confounder.

**Key references:** Shimizu, Hoyer, Hyvärinen, Kerminen, "A Linear
Non-Gaussian Acyclic Model for Causal Discovery," JMLR 7, 2006;
Spirtes, Glymour, Scheines, *Causation, Prediction, and Search*,
2nd ed., 2000.

**The discriminating empirical test.** All three methods work on
(Y, X) pairs or multivariate observations. They do *not* require the
full conditional law κ̂\_Q — they only need residuals plus covariates.
The test: run SDR/ICA on κ̂\_Q's PIT residuals and check whether
hour\_of\_week falls out without being pre-specified. P1 already
found it by brute-force enumeration; if these methods recover it
blindly, that validates the approach for future Z-discovery when the
candidate set is less obvious.

**Relevance to Q1A and beyond.** If Q1A fires R-B1A (hour\_of\_week
insufficient) or the thread eventually reaches P2, these tools become
the next lever: systematic, data-driven Z-recovery rather than
hand-specified candidate axes. Worth running in parallel with Q1A as
a consistency check, not as a replacement for the pre-registered
experiment.
