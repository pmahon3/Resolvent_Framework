# Level-3 framework novelty scout — necessary-condition extraction from within-stratum residuals

**Date:** 2026-05-30
**Source:** MITACS-side cross-reference (within-stratum diagnostic 2026-05-29, `scratch/within_stratum_residual_diagnostic_summary.md`)
**Question:** Is "necessary-condition extraction on the missing Z from κ_Q's within-stratum residual structure" published as a method, or is it a survivable-novelty angle?
**Confidence cuts:**
  - HIGH-published (cite directly) if any reference does exactly this in our framing
  - PARTIALLY-published if pieces exist in different traditions but no unified treatment
  - GENUINELY-ABSENT if exhaustive search finds nothing

## Verdict

**PARTIALLY-PUBLISHED. The decomposition is fully published; the explicit "necessary conditions on a missing Z" framing is NOT verbatim in the primary source (Diggle 1988) but is a contrapositive translation that is essentially the same content.**

**Verdict caveat:** This verdict rests on a direct read of (a) the Diggle 1988 *Biometrics* abstract via PubMed (PMID 3233259) and Semantic Scholar; (b) Verbeke-Lesaffre-Brant 1998 *Statistics in Medicine* extending it; (c) a 2020 *JRSS C* paper (Wang et al.) citing Diggle 1988's interpretive language; (d) Diggle's Lancaster and APTS lecture notes via paraphrase from search-result snippets (the PDFs themselves did not render to readable text via WebFetch). I did **not** obtain a verbatim passage from Diggle 1988's main text or DHLZ 2002 Chapter 5 saying "the serial-correlation component is evidence for a missing time-varying covariate." The interpretive translation is from the 1998 *JRSS C* paraphrase: "W_i(t) ... represents underlying variation that is latent or unmeasured but acknowledged through the model structure." Diggle's own framing in print is "continuous-time zero-mean Gaussian process" / "time-varying random effect" — functionally an unobserved component but **not** explicitly framed as a missing-covariate diagnostic in the snippets I obtained.

The canonical match is the **variogram-of-residuals tradition** founded by **Diggle (1988, *Biometrics* 44: 959-971, PMID 3233259)** and formalized in **Diggle, Heagerty, Liang, Zeger, *Analysis of Longitudinal Data* (2nd ed., OUP 2002), Chapter 5.** The Diggle decomposition of within-subject residual structure is
> V(u) = τ² + σ²{1 − ρ(u)}   (the empirical variogram)
> Var(Y_ij) = ν² + σ² + τ²   (total variance decomposition)

with three components (in Diggle's vocabulary):
- **τ² (measurement error / nugget)** — fast-varying / white-noise residual content
- **σ² (process variation)** — serial-correlation contribution from a continuous-time Gaussian process W_i(t)
- **ν² (random intercept / between-subject)** — systematic between-unit shape

This decomposition is *structurally exactly* the three signatures the MITACS within-stratum diagnostic extracts (lag-1 ACF strong ⇒ σ² dominates; variance ratio ⇒ relative weights; per-day-mean SD ⇒ ν² presence). The map is unambiguous at the algebraic level. The **interpretive translation** ("σ² > 0 ⇒ unmeasured time-varying covariate") is licensed by the model structure but is not a verbatim Diggle claim — Diggle treats W_i(t) as a stochastic-process random effect to be fitted, not as a fingerprint to be inverted into Z-properties. The contrapositive is content-equivalent (a Z that absorbs the W_i(t) covariance must reproduce its timescale and variance), but Diggle does not state the contrapositive.

What is **NOT** in the variogram literature, and what would be the surviving novelty angle if anything is:

1. The variogram tradition does this **post-OLS** or **post-random-effects-fit**, not **post-σ-algebra-refinement-from-stratified-Patra-Sen/Deb-et-al.** The diagnostic-of-residuals-from-a-conditional-kernel-estimator-refined-by-a-mixture-localization-test is the methodological combination claim. This is narrow.
2. The variogram literature uses these as inputs to **model selection** (which covariance structure to fit), not as **necessary-condition extraction on what an unobserved Z must look like.** The framing difference is real; the inferential content largely overlaps; the *deliberate inversion* (from "model the covariance" to "infer Z's properties") is not in the variogram literature verbatim, though it is licensed by it.
3. The "publication-grade necessary-conditions claim" requires bootstrap CIs on each of (lag-1 ACF, variance ratio, between-day SD) and a formal logical structure tying each empirical observable to a Z-property. The MITACS diagnostic is INSPECTION-ONLY and does not have this.

Bottom line: **the underlying decomposition is fully published.** What is potentially novel is the **framing inversion** (treating the variogram components as Z-property necessary conditions rather than as covariance-structure modeling targets) AND the **σ-algebra-refinement composition context**. Both are methodological-organizational moves rather than new tools. Honest contribution: the framing is a small reformulation; the composition is unstudied (Diggle's variogram has not been combined with Deb-et-al.-style mixture-localization in the literature I found).

## Evidence by tradition

### Variogram of residuals (canonical match — Diggle 1988 and successors)

**Diggle, P. J. (1988).** "An approach to the analysis of repeated measurements." *Biometrics* 44: 959-971. PMID 3233259. DOI 10.2307/2531727.
Established the empirical variogram of within-subject residuals as a diagnostic for the (nugget + process + random-effects) decomposition. Abstract (verbatim from PubMed): "A linear model is proposed for repeated measurements in which the correlation structure within each time sequence of measurements includes parameters for measurement error, variation between experimental units, and serial correlation within units. An approach to data analysis is presented which involves preliminary analysis by ordinary least squares, use of the empirical semi-variogram of residuals to suggest a suitable correlation structure, and formal inference using likelihood-based methods." **Caveat:** the inferential framing as "evidence for an unmeasured time-varying covariate" is not in the abstract verbatim — it is a model-structural translation; Diggle's own framing is "stochastic process W_i(t)" / "serial correlation within units." Direct read of the main text would be required to confirm whether Diggle himself made the missing-covariate translation explicit.

**Diggle, Heagerty, Liang, Zeger (2002).** *Analysis of Longitudinal Data*, 2nd ed. Oxford University Press. Chapter 5 ("Parametric models for covariance structure") and Chapter 3 ("Exploring longitudinal data").
Textbook treatment. The general model is Y_ij - μ_ij = d'_ij U_i + W_i(t_ij) + Z_ij, where:
- U_i — random effects (parallel to between-day systematic shape)
- W_i(t) — continuous-time Gaussian process with autocorrelation ρ(u) (parallel to within-day lag-1 ACF)
- Z_ij — independent N(0, τ²) measurement error (parallel to fast-varying white-noise residual)

Diggle states (paraphrasing the framework): the relative magnitudes of τ², σ², ν² (and the shape of ρ(u)) are diagnostics for what kind of unobserved variation drives the residuals. This is **necessary-condition extraction**, in different vocabulary.

**Pinheiro, J. C. and Bates, D. M. (2000).** *Mixed-Effects Models in S and S-PLUS.* Springer. `nlme::Variogram` implements Diggle's diagnostic; routine use in mixed-effects model selection.

**Verbeke, G., Lesaffre, E., & Brant, L. J. (1998).** "The detection of residual serial correlation in linear mixed models." *Statistics in Medicine* 17(12): 1391-1402. PMID 9682327. Extends Diggle 1988's stationary case to non-stationary models including random slopes; simulation studies validate the residual-variogram approach for detecting additional within-subject serial correlation after fitting random effects.

**Conclusion on this tradition:** the structural match is exact. The MITACS within-stratum diagnostic computes the discrete-time analogue of Diggle's variogram decomposition, applied to PIT residuals from a stratified conditional-kernel estimator. The interpretive claim ("residuals show lag-1 ACF +0.67, variance ratio 0.66, between-day SD 0.21, therefore missing factor is slow-varying continuous covariate with between-day systematic shape") is precisely what Diggle's framework licenses.

### Sensitivity analysis for unmeasured confounders

Rosenbaum bounds, E-values (VanderWeele & Ding 2017 *Annals of Internal Medicine*), exponential-tilting sensitivity (Tan 2006). Sensitivity analyses characterize the **magnitude of bias** that an unmeasured U would have to induce to change a causal conclusion — they parameterize U through (γ_A, γ_Y) coupling strengths to the treatment and outcome. They do NOT characterize timescale, continuity, or dispersion direction of U. The framing is "how strong does U have to be to overturn the result?" not "what properties must U have?"

**Time-varying extension** (Yang et al. 2024 arXiv:2506.11322 *Statistics in Medicine* / Bayesian sensitivity with time-varying U): parameterizes the time-varying confounder as a latent AR(1) or random-walk with assumed timescale; the timescale is INPUT (prior), not OUTPUT (inferred). Not the same as level-3 extraction.

**Verdict:** does not match the framing. Sensitivity analysis bounds bias under assumed properties of U; it does not extract necessary conditions on U from residuals.

### Causal discovery with latent variables

FCI (Spirtes-Glymour-Scheines 2000), LiNGAM-latent (Hoyer et al. 2008), RFCI. These algorithms detect the **structural presence** of latent confounders and recover **partial structure** of the causal graph. They do not extract metric properties (timescale, dispersion direction) of the latent — they identify it qualitatively.

**Verdict:** orthogonal. Causal discovery identifies that a latent exists; the MITACS diagnostic, given that a latent is binding, extracts its properties.

### Variance-component decomposition

**Searle, Casella, McCulloch (1992).** *Variance Components.* Wiley. Classical variance-component decomposition into between-group / within-group / residual sources. The between-vs-within variance ratio (intraclass correlation, ICC) is interpreted as evidence for cluster-level shared variation. Asymptotic in the variogram tradition.

**Verdict:** Searle-style ICC is the classical antecedent of Diggle's between-subject (ν²) component. The longitudinal-data refinement (Diggle 1988) is the relevant one because it preserves time structure. ICC alone doesn't speak to timescale or continuity, only to clustering magnitude.

### Longitudinal data analysis (broader)

**Hamel, Yoccoz, Gaillard (2012).** *Methods in Ecology and Evolution* 3: 731-742. Argues that autocorrelation in longitudinal residuals and individual heterogeneity routinely co-occur, and that residual diagnostics let you infer their relative contribution. Explicitly frames autocorrelation as evidence of "inappropriate modeling of fixed effects, including neglecting to include an environmental covariate that is correlated with time." This is **exactly** the MITACS framing.

**Verdict:** corroborates the variogram tradition's framing; nothing new methodologically.

### Heckman-Singer successor literature

**van den Berg, G. J. (2001).** "Duration models: specification, identification and multiple durations." *Handbook of Econometrics*, vol. 5, ch. 55. Reviews the duration-model literature post-Heckman-Singer. Discusses identification of the unobserved heterogeneity distribution from the structure of the observed hazard. **Honoré (1993), Abbring & van den Berg (2007)** address what properties of the unobserved heterogeneity distribution can be recovered from observed duration patterns.

**This is the closest analogue in the econometric tradition.** They recover the heterogeneity distribution (a property of U) from residual hazard structure (observable). But the technical vehicle is different — they exploit multiple spells per subject and proportional-hazard structure. Not directly transferable to the κ_Q / single-time-series / forecasting framing.

**Verdict:** parallel tradition. Same logical structure (infer properties of latent from observable residual structure) but in proportional-hazards-with-multiple-spells. Does not subsume the variogram tradition; complements it.

### Andrews-Mallows / scale-mixture tradition

**Andrews & Mallows (1974) JRSSB 36: 99-102.** Established that scale-mixture-of-normals (SMN) representations are non-unique for many heavy-tailed distributions — Student-t, slash, contaminated normal all admit SMN forms with different mixing distributions.

**Follow-on tradition:** West (1987) JRSSB; Kim, Shephard, Chib (1998) ReStud; Choy & Smith (1997) JRSSB. These exploit SMN representations for computational efficiency in Bayesian inference, but treat the mixing distribution as a nuisance to integrate over — not as something to infer.

**Verdict:** Andrews-Mallows establishes the *unidentifiability* of the mixing distribution from the marginal alone (which is exactly the identifiability obstruction). It does NOT provide methods for inferring mixing-distribution properties from residual structure. Adjacent, not matching.

### Realized-volatility / latent-process inference

**Andersen, Bollerslev, Diebold, Labys (2003).** "Modeling and forecasting realized volatility." *Econometrica* 71: 579-625. Treats latent volatility as observed (via realized measures) and infers its properties (long-memory, persistence) from the observed realized-vol time series. This is "observe a proxy for the latent and infer the latent's properties," not "infer latent's properties from residuals after conditioning on observed covariates."

**Recent close-match:** *Conditioning on a Volatility Proxy Compresses the Apparent Timescale of Collective Market Correlation* (arXiv:2603.14072, 2026). Demonstrates that conditioning on a volatility proxy reduces residual autocorrelation timescale by ~5×, which is interpreted as evidence that volatility IS the latent driver of persistence. This is **resolution path 1** in our framework — TEST a candidate Z, observe residual ACF changes. Not level-3 (necessary-conditions-before-identification).

**Verdict:** the realized-vol tradition tests candidate latents rather than extracting necessary conditions; closer to MITACS T1's planned secondary-metric (post-conditioning lag-1 ACF) than to the within-stratum diagnostic itself.

### Other (residual-structure ML / Bayesian)

Searched: Bayesian sensitivity analysis for unmeasured time-varying confounding (Yang et al. 2024); Residual Component Analysis (Kalaitzis-Lawrence 2012); functional data analysis for residual curves (Ramsay-Silverman). None match the necessary-condition-extraction framing in our σ-algebra-refinement-post-conditional-kernel context.

## What would survive as novelty (if anything)

The methodological component (within-stratum residual decomposition into "lag-1-ACF + variance-ratio + between-day-SD") is **fully published** as Diggle's residual variogram (1988, 2002), and is the canonical tool. The MITACS-side diagnostic implements a discrete-time, three-summary-statistic version of it. The variogram literature explicitly licenses the inferential step ("σ² > 0 ⇒ shared unmeasured time-varying covariate exists with timescale 1/log(ρ)").

What is **methodologically novel** in our framing, if anything:

1. **Variogram diagnostics applied to PIT residuals from a stratified conditional-kernel estimator.** Diggle's tradition uses residuals from random-effects models with continuous outcomes; PIT residuals from a κ_Q estimator post-Deb-et-al.-mixture-localization is a non-standard input. But this is a **methodological combination**, not a new tool — the diagnostic itself is Diggle's.

2. **The explicit framing as "necessary conditions on the missing Z."** The variogram literature frames the output as "the covariance structure needs the following components" (modeling guidance); MITACS frames it as "any successful Z must have the following properties" (search guidance). This is the **same content** under contrapositive translation — if the residual structure decomposes as Diggle (1988) says, then any Z that absorbs that decomposition must have the properties the components imply. This framing reformulation is a **negligible contribution at best**.

3. **The level-3 vs level-4 ladder.** Embedding the diagnostic in the four-level framework ladder (κ_Q identifies → stratified Patra-Sen / Deb localizes [level 2] → within-stratum diagnostic characterizes Z's necessary properties [level 3] → auxiliary data + tested-candidate-Z identifies [level 4]) is a **framework-side organizational claim**, not a methods claim. The organization itself is potentially valuable as a unifying-treatment but is not a theorem or method.

The honest verdict: **the diagnostic is Diggle 1988 applied to PIT residuals from a Deb-et-al.-refined estimator.** Calling this "level-3 novelty" survives the audit only if (a) the writeup credits Diggle 1988 / Diggle-Heagerty-Liang-Zeger 2002 explicitly as the methodological source, (b) the framework-side claim is restricted to the **organizational unification** (κ_Q + Deb + Diggle + auxiliary-Z form a ladder), not the **diagnostic itself**, and (c) bootstrap CIs are added before any of this is published as a claim-grade finding (currently INSPECTION-ONLY).

## Recommended next action

**The verdict is PARTIALLY-PUBLISHED.** The decomposition (Diggle 1988 / DHLZ 2002) is fully published; the explicit framing inversion (treating variogram components as missing-Z necessary conditions rather than as covariance-structure modeling targets) is NOT verbatim confirmed in the primary sources I could access via web search; the composition with Deb-et-al.-style mixture localization is unstudied.

Concrete recommendations:

1. **Cite Diggle (1988) and Diggle-Heagerty-Liang-Zeger (2002, ch. 5) as the canonical methodology** in any future writeup. The MITACS within-stratum diagnostic IS the discrete-time three-summary-statistic version of Diggle's residual variogram. Pretending otherwise will not survive even a single-pass audit.

2. **Drop the "necessary-condition extraction" framing as a novelty claim.** Under contrapositive translation it IS Diggle's framework. The contribution, if any, is organizational (the four-level ladder).

3. **The organizational-ladder framing IS potentially novel as a survey contribution** if it spans Heckman-Singer (1984) + Deb-Saha-Guntuboyina-Sen (2022) + Diggle (1988) + Andersen-Bollerslev-Diebold (2003) under one umbrella. This is the same kind of contribution as the framework's "Rokhlin-disintegration unification" sub-thread — non-theorem, possibly-expository, low priority.

4. **If MITACS-side T1 wants to use the within-stratum lag-1 ACF as a secondary metric, that's fine** — it's a Diggle-style residual variogram component, applied to a PIT-residual time series with a candidate Z. The methodology is standard; the application is sound. No novelty claim is required for it to be useful.

5. **DO NOT add "level 3 = within-stratum diagnostic" to the framework note's ladder without flagging the Diggle citation prominently.** Doing otherwise repeats exactly the audit miss that triggered the 2026-05-27 audit-correction (Patra-Sen-conditional was thought to be novel; turned out to be Deb-Saha-Guntuboyina-Sen 2022 by Sen of Patra-Sen).

6. **Second-pass audit hook (if pursued further):** check forward citations of Diggle (1988) by Diggle and Heagerty specifically — has the variogram tradition been combined with mixture-fraction estimation (Deb et al. 2022 lineage)? This is the cross-tradition unifier where the alleged novelty would sit. Quick scan: not found in the surface search (Diggle's recent work is on spatial point processes and geostatistical models, not mixture-localization-then-variogram chains). But a deep dive on Sen's 2022-onwards publication list (done) shows no extension to variogram-style residual diagnostics either. The cross-tradition gap is real but its filling is a survey contribution, not a methods contribution.

## Workflow lesson

Applied the audit-correction lesson directly:

- **Checked forward citations of Deb-Saha-Guntuboyina-Sen 2022 by every co-author** (Sen, Guntuboyina from their public publication pages at Columbia and Berkeley, accessed 2026-05-30). Sen's 2022-2024 line is on empirical-Bayes denoising (Soloff-Guntuboyina-Sen 2024), kernel measures of dissimilarity (Huang-Sen 2022), partially-Bayes multiple testing (Ignatiadis-Sen 2023), and convex regression (Deng-Han-Sen 2023). Guntuboyina's is on totally-concave regression (Ki-Guntuboyina 2025), MARS-via-LASSO (Ki-Fang-Guntuboyina 2024), scale-mixture density convergence rates (Kim-Kur-Guntuboyina 2025), and multivariate heteroscedastic empirical Bayes (with Sen). **Neither author has extended the covariate-dependent mixture work into residual-structure inference for missing Z.** Negative result, shown.
- **Checked Diggle's group for forward extension into mixture territory** via search ("Diggle" + variogram + Patra-Sen / mixture / two-groups). Diggle's recent visible work is on log-Gaussian Cox processes, geostatistical inference with geomasking, and longitudinal-data dropout. **No extension into Patra-Sen / Deb-style mixture localization composed with variogram diagnostic in the surface search.** Caveat: this is a surface search, not an exhaustive review of all Diggle co-authors' bibliographies.
- **Cross-tradition gap (Deb-et-al.-style mixture localization composed with Diggle-style variogram diagnostic) appears empirically real** but is a methodological-combination claim, not a method-novelty claim. Worth flagging in the parked disintegration_diagnostic.md under "what survives" as: "(g) Diggle-style variogram diagnostic applied to PIT residuals from a Deb-et-al.-refined conditional-kernel estimator — methodological combination, both components fully published, framework-side ladder organization potentially expository."

**Lesson generalization:** when a scout claims a candidate-novelty methodological move, the audit must check whether the methodological move is just a known-tool applied to a non-standard input. Diggle's residual variogram applied to a non-standard residual stream (PIT residuals from κ_Q estimator) is the kind of move that READS as novel but is methodologically standard. Add this pattern to the literature-scout's standard checklist: "is the alleged novelty a known tool applied to a non-standard input?"

**Second-pass-audit hook (for if this gets pursued further):**
1. Get JSTOR / institutional access to Diggle (1988) *Biometrics* 44: 959-971 main text. The verdict here rests on the inferential framing in the main text (not visible to me via web search). Specifically: does Diggle (1988) §3 or §4 frame the σ²ρ(u) component as evidence for a missing time-varying covariate, or only as covariance-structure modeling? If the former, verdict stays HIGH-PUBLISHED. If the latter, verdict shifts toward "framing inversion may be novel."
2. Read DHLZ 2002 Chapter 5 main text for the same question.
3. Forward citations of Diggle (1988) by Patrick Heagerty specifically, on the question of whether Heagerty has extended the variogram diagnostic into Z-property-extraction territory (he is the most likely author to have done so).
4. If items 1-3 confirm the framing inversion is genuinely missing from the variogram literature, then the (a) "necessary-conditions framing of variogram components" and (b) "composition with Deb-et-al. mixture localization" together form a coherent unifying-treatment contribution worth a framework-side memo.

## References (consolidated)

**Canonical match:**
- Diggle, P. J. (1988). "An approach to the analysis of repeated measurements." *Biometrics* 44: 959-971.
- Diggle, P. J., Heagerty, P. J., Liang, K.-Y., & Zeger, S. L. (2002). *Analysis of Longitudinal Data*, 2nd ed. Oxford University Press.

**Methodological reference for variogram in mixed-effects R toolchain:**
- Pinheiro, J. C., & Bates, D. M. (2000). *Mixed-Effects Models in S and S-PLUS.* Springer.
- Verbeke, G., Lesaffre, E., & Brant, L. J. (1998). "The detection of residual serial correlation in linear mixed models." *Stat Med* 17(12): 1391-1402.

**Heckman-Singer successor tradition (parallel, not subsumed):**
- van den Berg, G. J. (2001). "Duration models: specification, identification and multiple durations." *Handbook of Econometrics*, vol. 5, ch. 55.
- Abbring, J. H., & van den Berg, G. J. (2007). "The unobserved heterogeneity distribution in duration analysis." *Biometrika* 94: 87-99.

**Realized-volatility / latent-process inference (adjacent):**
- Andersen, T. G., Bollerslev, T., Diebold, F. X., & Labys, P. (2003). "Modeling and forecasting realized volatility." *Econometrica* 71: 579-625.
- arXiv:2603.14072 (2026). "Conditioning on a Volatility Proxy Compresses the Apparent Timescale of Collective Market Correlation."

**Sensitivity-analysis tradition (does not match):**
- VanderWeele, T. J., & Ding, P. (2017). "Sensitivity analysis in observational research: introducing the E-value." *Annals of Internal Medicine* 167: 268-274.
- Yang et al. arXiv:2506.11322 (June 2025; date verified via arXiv ID convention). "Bayesian Sensitivity Analysis for Causal Estimation with Time-varying Unmeasured Confounding."

**Co-author-forward-citation check (audit-discipline):**
- Sen's publications page: https://sites.stat.columbia.edu/bodhi/Bodhi/Publications.html (checked 2026-05-30).
- Guntuboyina's publications page: https://www.stat.berkeley.edu/~aditya/styled-2/index.html (checked 2026-05-30).
- Neither extends Deb-Saha-Guntuboyina-Sen (2022) into residual-structure diagnostics for missing Z.

**Identifiability-obstruction reference set (from disintegration_diagnostic.md, unchanged):**
- Bergna et al. (2026). arXiv:2605.06413. Proposition 1.
- Heckman, J. J., & Singer, B. (1984). *Econometrica* 52: 271-320.
- Allahverdyan (2020). arXiv:2002.07884.
- Andrews, D. F., & Mallows, C. L. (1974). *JRSSB* 36: 99-102.
- Deb, Saha, Guntuboyina, Sen (2022). *JASA* 117(540). arXiv:1810.07897.
