# The κ_Q characterisation ladder: limit of definiteness on missing/exogenous Z

**Date:** 2026-05-30  
**Status:** Companion to `disintegration_diagnostic.md` (PARKED 2026-05-26).
This note articulates a four-level decomposition the parked note's
"resolution paths" section implies but does not enumerate. Levels 1, 2,
and 4 are present implicitly; level 3 (necessary-condition extraction
from within-stratum residual structure) is not.

**Literature scout verdict (2026-05-30, converged):** PARTIALLY PUBLISHED.
Level-3 components are scattered across 5 traditions:
(1) Cinelli-Hazlett 2022 — scalar sensitivity (partial R²);
(2) Shape-constrained deconvolution (Efron 2016, Kiefer-Wolfowitz);
(3) Heckman-Singer 1984 / Bonhomme-Manresa 2015 — support-point structure;
(4) Bi-Zhang-Calhoun 2023 — spectral bounds on latent dimensionality;
(5) Diggle 1988 / DHLZ 2002 — three-component covariance decomposition
(τ² nugget + σ²ρ(u) serial + ν² random intercept).

**Diggle resolution:** Diggle's framing is *forward* (covariance-structure
modelling), NOT inferential inversion. The entire forward citation network
(Verbeke-Lesaffre 1998, Heagerty 1999/2002, Sherlock et al. 2020) confirms
this. Diggle provides *machinery* for level 3 but does not pose the
*inverse question* (what necessary conditions on Z does the residual
structure imply?).

**Surviving novelty scope:** (a) inferential inversion as framing
(residual structure → necessary conditions on Z, not Z → covariance
model); (b) four-level hierarchy with theorem-bounded limits at levels
1 and 4; (c) unification of scattered components into a single
characterisation programme.

**Claimed type(s):** Type 6 (exposition/translation) + Type 7 (methodology).
**Type 4 (vocabulary): AUDITED, FAIL** — three-statements test not met;
"circumlocution" admission binding; statements stateable in standard
language. See `kappa_q_characterisation_ladder_audit.md`.
**Type 6 bar:** (a) Name target audience; (b) cite scattered literature
they cannot currently access; (c) translation requires non-trivial
conceptual work (not just notation change).
**Type 7 bar:** Demonstrated advantage — the decision logic (level 2 →
level 3 inversion → level 4 pivot) generates a pre-registered
prediction (T1 within-cell lag-1 ACF drop) that wouldn't be writeable
without the framing. Prospective-only; T1 not yet executed.  
**Parent material:** `disintegration_diagnostic.md`,
`disintegration_diagnostic_audit_correction.md`  
**Triggering applied evidence:** MITACS S9+S10+S11+S12+S13+S14 corpus +
within-stratum residual diagnostic (2026-05-29). Cross-link:
`~/Research/Dynamics/MITACS/notes/seeds/kappa_q_limits_applied.md`.

---

## The question

What is the limit of definiteness to which one can characterise a
missing/exogenous Z from κ_Q-observable structure alone — before
auxiliary information is brought in?

`disintegration_diagnostic.md` gives the *upper bound*: from κ_Q's
marginal alone you cannot distinguish structured noise (regime a) from
noisy structure (regime b). That is a theorem (Bergna et al. 2026
Prop 1; Heckman–Singer 1984; Allahverdyan 2020; Andrews–Mallows 1974).

But the obstruction theorem is a statement about *one specific
discrimination* (regime a vs regime b). It leaves open what *other*
characterisations of Z are κ_Q-attainable. The parked note's "What
resolves the ambiguity" section lists three auxiliary-information types
that break the tie at level 4 (identity of Z) — it does not address
intermediate levels.

This note enumerates a four-level ladder for what κ_Q-observable
structure permits.

## The ladder

| Level | Object | κ_Q-attainable? | Framework basis | Example method |
|---|---|---|---|---|
| **1** | Existence regime (a vs b) | **NO** (theorem-level not discriminable) | Bergna 2026 Prop 1; H-S 1984; Allahverdyan 2020; Andrews-Mallows 1974 | None possible from κ_Q alone |
| **2** | Localisation of Z's action — which σ-algebra refinements Q' ⊃ Q drop R*(Q) | **YES** | Tower property + monotonicity (R*(Q') ≤ R*(Q)); stratified Patra-Sen as discrete proxy | Deb et al. NPMLEmix (JASA 2022); per-stratum α̂_L (P1) |
| **3** | Necessary conditions on Z's shape — timescale, continuity, dispersion direction, between-stratum systematic effect | **YES** (this note's contribution candidate) | Within-stratum residual structure analysis: autocovariance, dispersion ratio, between-stratum component | Within-stratum lag-k ACF; per-stratum variance ratio; per-day mean variation; structural-time-series-style residual diagnostics (lit scout pending) |
| **4** | Identity of Z — which specific variable Z is | **NO from κ_Q alone** | Requires auxiliary info type 1 (candidate Z + test), type 2 (richer model class — equivalent at the model level), or type 3 (structural assumption) | T1-style direct test; synthetic-DGP calibration (Bergna); structural noise prior |

The boundary is between levels 3 and 4. **Levels 1–3 are
κ_Q-attainable; level 4 is not.** This is the framework's "limit of
definiteness."

## Level-by-level

### Level 1 — Existence regime: NOT attainable

The identifiability obstruction theorem (parked note, §"The
obstruction") is the statement that level 1 is not κ_Q-attainable.
This is the framework's strongest negative result. Cannot be
sharpened.

### Level 2 — Localisation: attainable

The tower property R*(Q') ≤ R*(Q) for Q' ⊃ Q (parked note, §"The
monotonicity theorem") is the framework's strongest positive guarantee.
Equality holds iff Y is conditionally independent of Q' \ Q given Q.
This means observing R*(Q') < R*(Q) is *direct evidence* that the
information in Q' \ Q is non-trivially conditioning Y — Z's action
"lives" (partially or wholly) on Q' \ Q.

Implementation: Deb, Saha, Guntuboyina, Sen (JASA 2022) NPMLEmix
provides the canonical tuning-parameter-free joint NPMLE of the
covariate-dependent two-groups mixture proportion π*(x). Its discrete
specialisation (per-stratum α̂_L over a fixed stratification) is
stratified Patra-Sen — Deb et al. Section 6 explicitly poses the
σ-algebra adequacy question this targets.

**Applied evidence**: MITACS P1 / S11 — hour_of_week is the binding
axis at α̂_L range 0.575 [0.448, 0.648] across 5 candidate stratifying
axes. Saturday-daytime cells reach α̂_L 0.55–0.61; Monday-daytime cells
collapse to α̂_L 0.035. Z's action is concentrated on a social-weekly
cycle, not seasonal.

### Level 3 — Necessary conditions on Z's shape: attainable (claim)

**Claim.** Conditional on a binding stratification identified at
level 2, the *within-stratum* residual structure of κ_Q's residuals
permits extraction of necessary conditions on any Z that could
account for the remaining residual heterogeneity, even though Z
itself is unobserved.

Specifically, the following within-stratum statistics each constrain Z:

- **Within-stratum autocovariance** at lag k. If lag-k ACF is far from
  zero, any Z whose action explains the remaining structure must vary
  on timescales matching the ACF decay rate. Z must be slow-varying if
  short-lag ACF is high; fast-varying if only long-lag autocorrelation
  is present.

- **Within-stratum dispersion ratio** (observed vs implied variance
  under Q-conditioning). If observed within-stratum variance is
  *smaller* than implied by full-process Σ_Q, the remaining residual
  variance lives in *between-stratum* structure — i.e., any Z must
  have a systematic between-stratum effect (not a stratum-specific
  variance multiplier).

- **Per-stratum mean structure.** If per-stratum residual means vary
  systematically (e.g., per-day SD of per-day means well above
  sampling-noise floor), Z's action includes a *location-shifting*
  component, not just dispersion modulation.

- **Higher-frequency residual structure.** Periodograms / wavelet
  decomposition of within-stratum residuals constrain whether Z's
  spectral content is broadband (e.g., temperature) or narrowband
  (e.g., a missed deterministic cycle).

**What level 3 gives you.** A *necessary-but-not-sufficient*
characterisation of Z's properties — Z's timescale, smoothness,
between-vs-within stratum structure, and broadband-vs-narrowband
content. Any candidate Z that fails these necessary conditions can
be ruled out. Any Z that passes is *consistent with* the observed
κ_Q residual structure, but is not uniquely identified.

**What level 3 does NOT give you.** Z's identity. Multiple distinct
Z's can satisfy the same necessary conditions (e.g., temperature,
solar irradiance, and humidity all share "slow-varying continuous
within-day-correlated weak-week-tie" — they would all pass the
necessary conditions extracted from within-stratum ACF + dispersion +
mean-shape analysis). Disambiguating among them requires level 4
(auxiliary information).

**Framework status of level 3.** *Not explicitly enumerated* in the
parked `disintegration_diagnostic.md`. The note's "What resolves the
ambiguity" section lists three resolution paths (candidate Z;
comparison model class; structural noise assumption) — all of which
operate at level 4 (resolve the obstruction at the identity level).
Level 3 sits between localisation (level 2) and identification (level 4):
it characterises Z *narrowly enough* to inform candidate selection but
*not narrowly enough* to identify Z.

**Literature scout verdict (converged 2026-05-30): PARTIALLY PUBLISHED
(outcome (b)).** The components exist scattered across 5 traditions
(see status header). No unified treatment exists. The surviving
contribution is:
- **Inferential inversion:** framing the question as "what does the
  residual structure *require* of Z?" rather than "given Z, what
  covariance structure results?" Diggle 1988 / DHLZ 2002 ch. 5 is the
  canonical *machinery* (three-component decomposition, serial
  covariance estimation); the *inversion framing* — using that
  machinery to extract necessary conditions on an unobserved Z — is
  not present in the forward citation network.
- **Four-level hierarchy:** theorem-bounded at levels 1 and 4, with
  the "limit of definiteness" boundary between 3 and 4 as a framework
  claim.
- **Unification:** assembling Cinelli-Hazlett (sensitivity), Diggle
  (covariance), Heckman-Singer/Bonhomme-Manresa (support), Bi-Zhang-
  Calhoun (spectral), and shape-constrained deconvolution into a single
  operational programme.

This scoping means the level-3 contribution is NOT "residual
diagnostics are novel" (they are not) but "the inferential inversion
reading of existing diagnostics, organised by the four-level hierarchy,
is novel as a unified programme."

### Level 4 — Identity of Z: NOT attainable from κ_Q alone

The parked note's three auxiliary-information types are exhaustive at
this level:

1. **Candidate Z + test.** Test whether conditioning on Z reduces
   residual risk. Identifies Z if R*(Q ∨ σ(Z)) < R*(Q).
2. **Comparison model class.** Equivalent at the model level: if a
   richer kernel family doesn't close the gap at the same Q, level
   4 is required.
3. **Structural noise assumption.** Domain knowledge constraining the
   innovation distribution. Converts the obstruction into a hypothesis
   test, with the assumption doing the work.

The MITACS resolution-paths-thread is currently routing to level 4
via path 1: T1 (temperature) as candidate Z. Within-stratum diagnostic
findings (lag-1 ACF +0.67; under-dispersion; per-day mean variation)
generated level-3 necessary conditions that *temperature plausibly
satisfies*; T1 will test whether temperature is *sufficient*. If T1
falsifies, level 3's necessary conditions still hold and route
candidate selection to alternative slow-varying continuous Z's
(solar irradiance; effective humidity; economic-activity proxies).

## Consequences of the ladder

### For framework-side work

The parked note's PARK verdict is *not* affected — the obstruction
theorem and its applied evidence (Bergna, H-S, Allahverdyan, A-M) are
the level-1 content, and they remain established. The level-2 content
(monotonicity + Patra-Sen lineage) is the parked note's positive
side. **The level-3 content is the candidate addition.** If the
literature scout (in flight) finds the within-stratum-necessary-
conditions reading already published, level 3 collapses into level 2
extended and the parked note's verdict is reinforced. If level 3 is
partially or genuinely novel, the parked note may merit revival —
but only after second-pass audit.

### For applied work that wants κ_Q-side closure

The limit of definiteness is level 3. **The κ_Q corpus cannot identify
Z; it can only characterise Z's necessary properties.** Applied
programmes that have empirically exhausted within-data levers (as
MITACS has via S9+S10+S11+S12+S13+S14) are at the framework's
upper bound. Further within-data work cannot tighten this; only
auxiliary information (level 4) can.

This is the **framework-prescribed** justification for pivoting to
exogenous-Z testing once levels 2 and 3 are exhausted. The pivot is
not impatience; it is the framework's own diagnosis of where κ_Q stops.

### For the resolution-paths discipline

Levels 1 and 4 are theorem-bound (no method choice). Level 2 has a
canonical method (Deb et al. NPMLEmix; stratified Patra-Sen as
discrete proxy). **Level 3 has canonical machinery** — Diggle 1988 /
DHLZ 2002 ch. 5 (three-component decomposition: τ² nugget + σ²ρ(u)
serial + ν² random intercept) provides the computational substrate.
**What is novel is the inferential inversion:** using that machinery
not to fit a covariance model given Z, but to extract necessary
conditions on Z given the residual structure. The workflow gap is not
"what tools?" but "in what order and with what decision logic does the
inversion proceed?"

---

## Cross-references

- **Theorem-level (level 1):** Bergna et al. 2026 (arXiv:2605.06413
  Prop 1); Heckman-Singer 1984 (Econometrica); Allahverdyan 2020
  (arXiv:2002.07884); Andrews-Mallows 1974 (JRSSB).
- **Level 2 canonical method:** Deb, Saha, Guntuboyina, Sen 2022 (JASA
  117(540), arXiv:1810.07897); R package NPMLEmix.
- **Level 3 lit scout (converged 2026-05-30):**
  `literature/2026-05-30_kappa-q-level-3-necessary-conditions-scout.md`
  Components mapped: Cinelli-Hazlett 2022 (JRSSB); Efron 2016 (JASA);
  Heckman-Singer 1984 (Econometrica); Bonhomme-Manresa 2015 (Econometrica);
  Bi-Zhang-Calhoun 2023 (Biometrika); Diggle 1988 (JRSSB) + DHLZ 2002
  ch. 5; Verbeke-Lesaffre 1998; Heagerty 1999/2002; Sherlock et al. 2020.
  Verdict: PARTIALLY PUBLISHED — inversion framing is surviving novelty.
- **Level 4 prescribed paths:** parked
  `disintegration_diagnostic.md` §"What resolves the ambiguity"
- **Applied evidence corpus (MITACS):**
  `~/Research/Dynamics/MITACS/notes/seeds/kappa_q_limits_applied.md`
  (companion to this note; level-by-level S9–S14 mapping)

## What this note does NOT do

- Does not claim novelty for level-3 *components* — the scout confirms
  these are published. Claims novelty only for inferential inversion +
  four-level hierarchy + unification.
- Does not modify the parked note's PARK verdict — that decision was
  about Patra-Sen-conditional being killed by Deb et al. 2022, and
  this note neither revives nor overturns that audit.
- Does not provide a unified level-3 method specification — that
  remains premature (no second-pass audit; applied evidence is
  INSPECTION-ONLY on MITACS data, not a confirmed experiment).
- Does not register as a `freeze.py`-style locked specification — this
  is a framework-side comprehension note, not an experiment.
- Does not declare contribution type — that declaration is pending
  below, awaiting cross-session alignment.

---

## Application-side evidence for type declaration

**Source:** MITACS S9+S10+S11+S12+S13+S14 corpus; within-stratum
residual diagnostic (2026-05-29); level-by-level mapping in
`~/Research/Dynamics/MITACS/notes/seeds/kappa_q_limits_applied.md`.

### Evidence map by level

| Level | MITACS evidence | Status |
|-------|----------------|--------|
| 2 | hour_of_week binding axis; α̂_L range 0.575 [0.448, 0.648]; Saturday-daytime 0.55–0.61 vs Monday-daytime 0.035 | Confirmed (S11) |
| 3 | Within-stratum lag-1 ACF +0.67; under-dispersion (within < full Σ_Q); per-day mean SD well above sampling floor | Inspection-only (S12–S14) |
| 4 | T1 (temperature) as candidate Z; necessary conditions from level 3 plausibly satisfied | Planned, not executed |

### Three-statements test candidates (Type 4 vocabulary)

If the four-level hierarchy functions as vocabulary:

1. **"Z's action is localisable to Q' \ Q"** — stateable as
   R*(Q') < R*(Q) via tower monotonicity. Clean in κ_Q language;
   requires circumlocution in standard mixed-effects ("the random
   effect has non-trivial variance component along the covariate
   partition refinement").

2. **"Z satisfies timescale τ ∈ [a, b]"** — stateable as a
   necessary condition extracted from within-stratum ACF decay under
   inferential inversion. Standard covariance modelling states the
   *forward* version ("if Z has correlation length τ, the marginal
   ACF decays as ρ(k) ~ exp(-k/τ)"); the *inverse* statement
   ("observed ACF decay *requires* any Z to have τ ∈ [a,b]") is
   the level-3 inversion.

3. **"Z has between-stratum systematic effect"** — stateable as
   within-stratum dispersion < full-process Σ_Q. Standard
   mixed-effects separates variance components (τ², σ², ν²) but
   does not frame the decomposition as a *necessary condition* on
   an unobserved Z whose identity is unknown.

**Non-trivial result about statement 1:** The tower monotonicity
theorem (R*(Q') ≤ R*(Q)) provides a falsifiable test — if
R*(Q') = R*(Q), Z's action does NOT live on Q' \ Q. This is
Theorem-level content (Deb et al. 2022 Section 6 poses the
question; the κ_Q language answers it).

### Methodology evidence (Type 7)

- MITACS S9–S14 demonstrates operational need: the programme hit
  the level 2/3 boundary and could not proceed without the
  framework's diagnosis of *where κ_Q stops*.
- Diggle 1988 / DHLZ 2002 provides canonical computational
  machinery for level 3.
- The decision logic (level 2 → level 3 → level 4 pivot) is
  the methodological contribution: when to stop within-data
  exploration and pivot to exogenous-Z testing.

### Type declaration history

**Round 1 (2026-05-30): Type 4 + Type 7 declared.**
Type 4 (vocabulary) CONDITIONAL FAIL at formal audit — three-statements
test not met; "circumlocution" admission binding; all three candidate
statements stateable in standard mixed-effects / sensitivity-analysis /
time-series language. See `kappa_q_characterisation_ladder_audit.md`.
Type 7 (methodology) CONDITIONAL — T1 not executed; N=1; no
demonstrated advantage yet.

**Round 2 (2026-05-30): Type 6 + Type 7 declared.**
Audit flagged Type 6 (exposition/translation) as better fit for
surviving novelty (inferential inversion + hierarchy assembling
5 scattered traditions into operational programme).

- **Type 6 primary:** (a) Target audience: applied researchers who
  have exhausted within-data levers and need principled guidance on
  when to stop and what to test externally. (b) Literature scattered
  across 5 traditions in 4 fields (econometrics, geostatistics,
  biostatistics, causal inference) — no single reference assembles
  them. (c) Non-trivial conceptual work: inferential inversion
  reverses inference direction; four-level hierarchy provides
  organising structure.
- **Type 7 secondary:** unchanged from round 1.

**Acknowledged caveats:**
- Inversion novelty is two-scouts-deep but one-institutional-read
  shallow (Diggle 1988 main text via JSTOR not yet checked).
- N=1 application (Ontario electricity demand PIT residuals).
- Type 6 "non-trivial conceptual work" claim is self-assessed.
