# Audit: kappa_q_characterisation_ladder (mode: full)

**Date:** 2026-05-28  
**Auditor:** Phase 2 formal audit (opus, with web search)  
**Target:** `notes/covered_leads/kappa_q_characterisation_ladder.md`  
**Input documents:** Seed note; `contribution_evaluation.md`; MITACS-side type-declaration input (2026-05-30)

---

## Declared contribution type(s): Type 4 (vocabulary) + Type 7 (methodology)

---

## Type 4 Verdict: CONDITIONAL FAIL

### Three-statements test evaluation

The seed offers three candidate statements claimed to be "cleanly stateable in the four-level/inversion vocabulary but not in standard mixed-effects or sensitivity-analysis language." Evaluated individually:

**Statement 1: "Z's action is localisable to Q' \ Q."**

The seed's own gloss admits this is stateable in standard mixed-effects language — it "requires circumlocution" ("the random effect has non-trivial variance component along the covariate partition refinement"). Circumlocution is not non-stateability. The standard variance-component decomposition along a partition refinement is well-understood in the random effects literature. The κ_Q language is *terser*, but terseness is not the bar; the bar is "not cleanly stateable in standard vocabulary." A sentence requiring a relative clause is still a clean statement. **Does not pass.**

**Statement 2: "Z satisfies timescale τ ∈ [a, b]."**

The seed identifies the forward statement ("if Z has correlation length τ, the marginal ACF decays as ρ(k) ~ exp(-k/τ)") as standard, and claims the inverse ("observed ACF decay requires any Z to have τ ∈ [a,b]") is the novel direction. However, the contrapositive of a well-defined forward model is logically equivalent to it and stateable without new vocabulary: "any process whose correlation length lies outside [a,b] is inconsistent with the observed ACF decay rate." This is a stance shift (asking the inverse question rather than the forward question), not a vocabulary contribution. The statement is perfectly stateable in standard time-series language — it is simply not habitually asked. **Does not pass** the "not cleanly stateable" criterion; it passes "not habitually stated," which is a weaker condition.

**Statement 3: "Z has between-stratum systematic effect."**

Standard mixed-effects language: "the random-intercept variance component ν² is non-zero." The seed acknowledges this decomposition (τ², σ², ν²) exists in standard language but argues the framing as a "necessary condition on an unobserved Z whose identity is unknown" is different. However, in the standard omitted-variable/sensitivity-analysis setting (Cinelli-Hazlett 2020, Franks-D'Amour-Feller 2019), the entire enterprise is characterising what an unobserved confounder must look like without knowing its identity. Cinelli-Hazlett's partial-R² bounds are explicitly necessary conditions on the confounder's strength. The *specific statistic* (ν² > 0) is cleanly stateable without new vocabulary. **Does not pass.**

**Non-trivial result:** The tower monotonicity theorem (R*(Q') ≤ R*(Q)) is attributed in the seed itself to Deb et al. 2022 Section 6. It is not novel to this seed. The seed says "the κ_Q language answers it" — but the theorem precedes the vocabulary, so the vocabulary does not enable the result.

**Summary:** All three statements are stateable (with varying degrees of directness) in existing mixed-effects / sensitivity-analysis / time-series language. The seed correctly identifies that these statements are *not habitually posed together as an inverse programme*, but that is a framing contribution (potentially Type 7 or Type 6), not a vocabulary contribution in the sense of the three-statements test. The calibration anchor is explicit: `residual_structure_inference` is listed in `contribution_evaluation.md` as a Type-4 FAIL. This seed shares substantial content with that earlier parked lead, distinguished by the four-level frame — but the frame does not create genuinely new stateability.

**Condition for future re-evaluation:** If concrete examples emerge where a statement is genuinely *not writable* (not merely longer or less elegant) without the vocabulary — and this is demonstrated on an external reader, not self-assessed by the vocabulary author — the verdict could upgrade. Currently, the self-assessed "circumlocution" framing is the binding admission that standard language suffices.

---

## Type 7 Verdict: CONDITIONAL

### Methodology bar evaluation

The framework bar for Type 7 is: "Demonstrated advantage on concrete problems; sharp regime classification; non-obvious consequence confirmed numerically." Park criterion: "No computational evidence; assembly is taxonomic not constructive; cannot answer 'why not just [standard method]?'"

**What the seed offers:** A decision logic (exhaust level 2 → extract level-3 necessary conditions → pivot to level-4 testing with pre-registered prediction). The MITACS-side input provides a concrete instance: within-stratum diagnostics generated a pre-registered prediction for T1 (lag-1 ACF drop from +0.67 toward 0 if temperature is sufficient; stay > +0.4 under the null). The seed claims this prediction "wouldn't be writeable without the framing."

**Assessment:**

1. *Is there a non-trivial prediction?* Yes. The T1 secondary metric (within-cell lag-1 ACF post-conditioning) is a specific, falsifiable, pre-registered prediction. This is genuine methodological content.

2. *Would the prediction not exist without the framing?* Partially. The observation "residuals have lag-1 ACF +0.67, so conditioning on a slow-varying Z should reduce this" is stateable without the four-level hierarchy — it follows from standard time-series reasoning about omitted slow-varying covariates. What the framing adds is the *systematic candidate-elimination procedure* and the explicit decision logic for when to stop within-data work and pivot to exogenous testing. This is above taxonomic assembly but below demonstrated advantage.

3. *Is the advantage demonstrated?* No. T1 has not run. The seed and MITACS input both acknowledge this explicitly. The evidence is currently "the methodology generated a writeable prediction" — not "the methodology was confirmed to work where alternatives failed."

4. *Can you answer "why not just [standard method]?"* Partially. Standard residual diagnostics + domain-knowledge candidate selection would reach the same operational decision (test temperature next) in this N=1 case. The framework's added value is the *systematic* character of the elimination (ruling out classes of Z by necessary-condition failure) rather than ad hoc domain judgement. But with N=1 applications, this systematic character is not yet distinguishable from post-hoc rationalisation of a domain-knowledge decision.

**Verdict: CONDITIONAL.** The methodology shows genuine structure (decision logic, pre-registered prediction, explicit stop-criterion). It does not yet clear the full bar because:
- T1 has not executed (no demonstrated advantage)
- N=1 application (cannot distinguish systematic from ad hoc)
- "Why not just domain knowledge?" remains answerable only prospectively

**Conditions for PASS:**
1. T1 executes and produces a verdict (either confirmation or falsification demonstrates the methodology's operational utility — the prediction existed and was assessable).
2. Ideally, a second application domain where the inversion generates a prediction that domain knowledge alone would not have prioritised.

---

## Other types assessed

### Type 1 (new theorem): FAIL

The seed's theorem-level content is entirely attributed to existing results:
- Level-1 obstruction: Bergna et al. 2026 Prop 1; Heckman-Singer 1984; Allahverdyan 2020; Andrews-Mallows 1974
- Level-2 monotonicity: Deb et al. 2022 Section 6; tower property (standard conditional expectation)
- No novel theorem is claimed or present

### Type 3 (unifying framework): FAIL

The seed assembles 5 traditions (Cinelli-Hazlett; Efron/deconvolution; Heckman-Singer/Bonhomme-Manresa; Bi-Zhang-Calhoun; Diggle/DHLZ) under one organisational frame. The framework bar requires: "The unification enables *method transfer* between the unified domains — a technique from domain A becomes applicable in domain B via the framework."

The seed does not demonstrate method transfer. It does not show, for example, that Cinelli-Hazlett's partial-R² technique becomes applicable to a Bi-Zhang-Calhoun spectral problem via the four-level hierarchy. The unification is organisational (these traditions address different levels of the same ladder) rather than operative (techniques from one become usable in another). This is "pattern-coincidence" in the framework's terminology: "These look alike" without "and therefore this technique applies here."

### Type 5 (impossibility): FAIL

The impossibility content (level-1 non-discriminability; level-4 non-identification from observables alone) is entirely attributed to existing theorems (Bergna, Heckman-Singer, Allahverdyan, Andrews-Mallows). No novel impossibility is claimed or proved. The boundary between levels 3 and 4 ("limit of definiteness") is a framework assertion, not a proved impossibility — it is not shown that level-3 characterisation is the tightest possible without auxiliary information.

---

## Cross-reference

The verdicts interact as follows:

- **Type 4 CONDITIONAL FAIL + Type 7 CONDITIONAL** leaves the seed without a currently-cleared bar. However, the Type 7 conditional is close to clearable (T1 execution is planned and operationally imminent within the MITACS workflow).
- The Type 4 failure is more structural: the "circumlocution" admission and the `residual_structure_inference` calibration anchor suggest the vocabulary contribution is not present at the level the framework requires. This is unlikely to be rescued by T1 execution.
- The surviving novelty (inferential inversion as a stance; four-level hierarchy as organising frame) is real but fits neither Type 4 (vocabulary enabling genuinely new statements) nor Type 7 (methodology with demonstrated advantage) cleanly. It is closer to **Type 6 (exposition/translation)** — translating scattered results into an operational programme for a specific audience (applied researchers who have exhausted within-data levers and need principled guidance on when to pivot to exogenous testing). However, Type 6 was not declared and has its own bar (named audience; inaccessible literature; non-trivial conceptual work).

---

## Caveats and conditions

1. **Diggle 1988 institutional read not completed.** Both scouts worked from secondary sources (citation network analysis, textbook summaries). Neither has read the Diggle 1988 JRSSB main text via JSTOR. The inversion framing's absence from the forward citation network is two-scouts-deep confirmation but one-institutional-read shallow. If Diggle 1988's discussion section poses anything resembling the inverse question, the surviving novelty narrows further.

2. **Pearl's Causal Hierarchy is a prior art analogue.** The three-rung observational/interventional/counterfactual ladder (Pearl 2000/2009; Bareinboim et al. 2022) and Manski's "what can be learned" partial identification programme (1990–2003) are both well-established "tiered characterisations of what observables reveal about latent/causal structure." The seed's four-level hierarchy is domain-specific (κ_Q-keyed) rather than methodologically novel as a meta-structure. The novelty must rest entirely on the specific statistical content at each level, not on the idea of tiering itself.

3. **N=1 application.** Ontario electricity demand PIT residuals. Vocabulary utility is self-assessed by the vocabulary author on the author's own data.

4. **The "circumlocution" admission is binding.** The seed itself states that statement 1 "requires circumlocution" in standard language — this is an admission that standard language suffices, which is dispositive against the three-statements test.

---

## Recommendation

**PARK with revival triggers.**

Per the framework's "park honestly" rule: no declared type's full bar is currently cleared. Type 4 is a CONDITIONAL FAIL (the "circumlocution" admission is binding; the `residual_structure_inference` calibration anchor applies). Type 7 is CONDITIONAL (T1 not executed; N=1; no demonstrated advantage). Types 1, 3, and 5 all FAIL on attribution of content to existing results.

The seed is not dead — it has genuine methodological structure and a planned falsifiable test. But the Phase 2 gate requires at least one bar cleared to proceed. Currently none is cleared. The honest verdict is PARK.

**Revival triggers (any one suffices to re-enter Phase 2):**

1. **T1 executes with either-sign verdict.** Confirmation or falsification of the pre-registered prediction (within-cell lag-1 ACF drop) demonstrates the methodology's operational utility and clears the Type 7 bar. This is the most likely revival path and is operationally imminent.

2. **Diggle 1988 main text read confirms inversion absence.** If the JSTOR read confirms the inversion framing is genuinely not present in Diggle's own discussion or forward citation network, the surviving novelty is strengthened. (Conversely, if the inversion appears in Diggle, the seed parks permanently.)

3. **Second application domain.** If the inversion + decision logic generates a non-obvious prediction in a domain other than Ontario electricity demand, the N=1 caveat is resolved and Type 7's "demonstrated advantage" bar becomes clearable.

**Note on Type 6 (exposition/translation):** The surviving novelty — assembling scattered traditions into an operational programme with explicit decision logic — may fit Type 6 better than Type 4 or Type 7. This was not declared and is not evaluated here, but if the seed is revived, reassessing contribution type (potentially Type 6 + Type 7) may be appropriate.

---

## Type 6 Audit: kappa_q_characterisation_ladder (Round 2)

**Date:** 2026-05-28
**Auditor:** Phase 2 formal audit (opus, with web search)
**Context:** Round 2 re-declaration as Type 6 (exposition/translation)
+ Type 7 (methodology, carried forward CONDITIONAL from round 1).
Triggered by round 1 recommendation that surviving novelty may fit
Type 6 better than Type 4.

### Type 6 Verdict: FAIL

**(a) Target audience: NARROW BUT REAL**

The seed names "applied researchers/practitioners who have exhausted
within-data diagnostic levers and need principled guidance on when to
stop within-data exploration and pivot to exogenous-Z testing." This
is a real situation -- the MITACS programme is a concrete instance.
The audience is narrow (practitioners at the level-3/level-4 boundary
of a specific kind of latent-variable problem) but not vacuous.

However, the narrowness creates a problem for bar (b): the narrower
the audience, the more specific the inaccessibility claim must be.
The seed must show that *this particular audience* cannot currently
find the assembled content. Assessed below.

**(b) Literature accessibility: NOT MET -- the park criterion applies**

The seed claims 5 traditions scattered across 4 fields, with no
single reference assembling them. Web search confirms the traditions
are indeed published in different literatures. But the Type 6 bar
is not "the traditions are scattered" -- it is "the target audience
cannot currently access them." Two findings undermine the
inaccessibility claim:

1. **The inferential inversion is already the standing stance in
   modern sensitivity analysis.** The seed's claimed non-trivial
   conceptual work -- reversing inference direction from "given Z,
   what covariance?" to "given residual structure, what must Z
   satisfy?" -- is not a translation the seed performs. It is the
   standard framing of the entire modern sensitivity-analysis
   literature:

   - Cinelli-Hazlett (JRSSB 2020): the robustness value is
     explicitly "the minimum strength an unobserved confounder
     would need" -- a necessary condition on the confounder's
     properties, stated without knowing its identity.
   - Franks-D'Amour-Feller (JASA 2020): explicitly separates the
     identified and unidentified parts of the sensitivity model,
     framing the question as "what must the latent variable
     satisfy to alter the conclusion?"
   - Chernozhukov-Cinelli-Newey-Sharma-Syrgkanis, "Long Story
     Short" (Review of Economics and Statistics, 2024; NBER
     w30302; SBE 2024 best paper): a unified framework for
     omitted variable bias across OLS, IV, and ML models,
     explicitly framed around "simple plausibility judgments on
     the maximum explanatory power of omitted variables" -- i.e.,
     the inferential inversion stance applied generally.
   - Manski's partial identification programme (1990--2003):
     the foundational framework for "what can be learned from
     data alone about quantities that are not point-identified,"
     explicitly asking "what must the unobserved satisfy?"

   The inversion is not a translation the seed contributes; it is
   the standard operating posture of the field the target audience
   works in. A causal-inference practitioner who has "exhausted
   within-data levers" has already been trained in Cinelli-Hazlett
   or Chernozhukov et al. and is already reasoning inversely about
   confounders.

2. **Recent practitioner-facing tutorials already exist for the
   named audience.** The seed's target audience (applied
   researchers navigating unmeasured confounding) has access to:

   - Bi et al. (2025), "Navigating Unmeasured Confounding in
     Nonexperimental Psychological Research: A Practical Guide to
     Computing and Interpreting E-Value" (Sage, Advances in
     Methods and Practices in Psychological Science).
   - "Methodological Tutorial Series for Epidemiological Studies:
     Confounder Selection and Sensitivity Analyses" (PMC, 2024).
   - "Real Effect or Bias? Best Practices for Evaluating the
     Robustness of Real-World Evidence through Quantitative
     Sensitivity Analysis" (arXiv 2023/2024).
   - Chernozhukov et al. (2024) itself, which is explicitly a
     practitioner-facing unification.

   These are not scattered across impenetrable prerequisites. They
   are tutorial-level treatments in the target audience's own
   journals.

3. **The 5-tradition scattering is real but reflects different
   problems, not inaccessibility.** The traditions serve different
   practitioner populations:

   - Cinelli-Hazlett / Chernozhukov et al.: causal inference
     practitioners doing sensitivity analysis for confounders
   - Diggle / DHLZ: geostatisticians / biostatisticians modelling
     spatial/temporal covariance structure
   - Heckman-Singer / Bonhomme-Manresa: econometricians estimating
     unobserved heterogeneity in panel data
   - Bi-Zhang-Calhoun: biostatisticians bounding latent
     dimensionality from spectral structure
   - Shape-constrained deconvolution: nonparametric statisticians
     estimating mixing distributions

   The seed does not demonstrate that any single practitioner needs
   all five. A geostatistician reaches for Diggle; a causal-
   inference researcher reaches for Cinelli-Hazlett. The scattering
   is functional, not an accessibility barrier. A review article
   assembling them would need to show method transfer (a technique
   from one tradition becoming applicable in another via the
   assembly) -- but that is the Type 3 bar, which already FAILED
   in round 1.

**The park criterion is met:** "The existing literature is already
accessible to the target audience." The causal-inference side has
Chernozhukov et al. (2024) and multiple practitioner tutorials. The
geostatistical side has Diggle/DHLZ. Each sub-audience has access
to its own tradition's tools. No single audience is shown to need
the cross-tradition assembly.

**(c) Non-trivial conceptual work: NOT MET**

The seed claims two pieces of non-trivial conceptual work:

1. **Inferential inversion** (reversing inference direction). As
   established under (b), this is the standard stance of modern
   sensitivity analysis, not a translation the seed performs. The
   Cinelli-Hazlett robustness value IS the inversion. Franks-
   D'Amour-Feller's identified/unidentified separation IS the
   inversion. The seed applies this stance to Diggle's covariance
   machinery, but applying an existing stance to existing machinery
   is closer to "notation change" than to "non-trivial conceptual
   work."

2. **Four-level hierarchy** (organising the 5 traditions by what
   each addresses). The round 1 audit's caveat 2 already flagged
   Pearl's Causal Hierarchy (observational/interventional/
   counterfactual) as a structural precedent. The principle
   "lower-rung information is insufficient for higher-rung
   questions" maps directly onto the seed's level-1/level-4
   boundary. Manski's "what can be learned" programme has the
   same tiered structure. The four-level hierarchy is a domain-
   specific instance of a well-established meta-structure, not a
   novel organising contribution.

   The first audit stated this precisely: "the novelty must rest
   entirely on the specific statistical content at each level, not
   on the idea of tiering itself." The statistical content at each
   level is attributed to existing results (Bergna, Deb et al.,
   Diggle, Cinelli-Hazlett). The hierarchy provides no new
   statistical content beyond assembly.

**The bar requires non-trivial conceptual work (not just notation
change).** Both claimed pieces fall short: the inversion is the
field's existing stance; the hierarchy is a domain-specific
application of an established meta-structure. Together they
constitute a reorganisation of existing ideas under a different
labelling scheme -- closer to notation change than to non-trivial
translation.

### Cross-reference with Type 7 (carried forward)

Type 7 CONDITIONAL from round 1 carries forward unchanged. The
conditions for clearing Type 7 remain:
1. T1 executes with either-sign verdict (primary revival trigger).
2. Second application domain (resolves N=1 caveat).

The Type 6 FAIL does not affect Type 7's conditional status. If T1
executes and demonstrates the methodology's operational utility, the
seed can re-enter Phase 2 under Type 7 alone.

### Venue assessment

The task asks what venue this would target. For a Type 6
contribution, the natural homes would be Statistical Science
(survey/review articles), Annual Review of Statistics and Its
Application, or SIAM Review (survey/tutorial track). All three
venues would expect the cross-field assembly either to demonstrate
genuine method transfer between traditions or to fill a gap the
field has explicitly flagged as needing a review. Neither condition
is currently met:
- No method transfer demonstrated (Type 3 FAIL from round 1).
- No evidence that any field or editorial board has flagged the
  need for this particular cross-tradition assembly.
- The closest existing unification (Chernozhukov et al. 2024)
  already occupies the "unified sensitivity analysis" space at
  the target audience's level.

### Caveats

1. **The Diggle-side inversion question remains one-read shallow.**
   If Diggle 1988's main text (JSTOR read, not yet done) contains
   NO discussion of the inverse question, and if a domain expert
   confirms that geostatisticians genuinely do not think in
   inversion terms about missing covariates, the (b) assessment
   could shift -- but only for a geostatistical audience, not for
   the causal-inference audience the seed currently targets.

2. **The MITACS-side input's strongest evidence (the section 7-to-8
   bridge paragraph) is self-assessed.** The input itself states
   the paragraph "is writeable with the implicit-bridge framing
   currently in place" and that the inversion makes it "cleanly
   writeable" -- i.e., the inaccessibility is stylistic, not
   structural. Stylistic improvement does not clear the Type 6 bar.

3. **If the seed were re-scoped to a strictly geostatistical
   audience** ("biostatisticians using Diggle-style longitudinal
   models who have not encountered the sensitivity-analysis
   literature's inversion stance"), the inaccessibility claim
   might strengthen -- but this would be a different seed with a
   different target audience, and it would need its own literature
   check to confirm the gap exists.

### Recommendation

**PARK.** Type 6 FAIL + Type 7 CONDITIONAL (carried forward) = no
bar currently cleared. Combined with round 1's Type 4 CONDITIONAL
FAIL, the seed has now been evaluated against Types 1, 3, 4, 5, 6,
and 7. None clears its bar.

The seed is not dead -- Type 7 remains conditionally clearable via
T1 execution. But the Phase 2 gate requires at least one bar
cleared to proceed. The honest verdict is PARK.

**Revival triggers (updated from round 1; supersede the round 1
list):**

1. **T1 executes with either-sign verdict.** This remains the
   primary and most likely revival path. Clears Type 7 if the
   prediction was assessable and the decision logic demonstrably
   guided the test design.

2. **Second application domain.** Resolves N=1 caveat for Type 7.

3. ~~**Diggle 1988 main text read.**~~ Downgraded: even if the
   inversion is absent from Diggle, this does not rescue Type 6
   because the inversion is present in Cinelli-Hazlett and
   Chernozhukov et al. The Diggle read may refine the surviving-
   novelty scope but does not by itself clear any bar.

**Type 6 is closed for this seed.** The inferential inversion is the
standing stance of modern sensitivity analysis; the four-level
hierarchy is a domain-specific instance of Pearl/Manski-type tiering;
recent practitioner tutorials cover the target audience. Re-declaring
Type 6 would require a fundamentally different target audience and a
new inaccessibility demonstration.
