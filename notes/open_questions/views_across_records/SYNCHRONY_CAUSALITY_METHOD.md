# Does synchrony need a common cause? A model-free test across sites

reviewed: false. v2, 2026-11-05. A working note, raw material for the user's own write-up and not for circulation. It addresses
audit fixes B1–B4 and N1, N2, N4 (`SYNCHRONY_CAUSALITY_METHOD_AUDIT.md`). A re-audit is owed before any further use. Collection:
`cyclic_marginal/views_across_records_taxonomy.json`.

## 1. A worked case
Three ponds. Each pair shares its own stream, and the streams have good and bad years independently. Nothing is shared by all three,
and each pond responds only to its two streams. If each pond has frogs half the time, how often can all three agree?

The best arrangement: a pond has frogs only when both its streams are good, each good with probability 1/√2.
- All three full: (1/√2)³ ≈ 0.354.
- All three empty, when at least two streams are bad: ≈ 0.207.
- Total ≈ **0.561** = (3√2 − 2)/4.

Independent ponds give 0.25. Gisin et al. 2020 prove that no arrangement of independent pairwise drivers exceeds 0.561 (below). More
coordination needs something shared by all three: a regional driver, shared history, or a shared observer.

## 2. Two versions of the ceiling (both owned)
**(A) Yes/no, three sites.** Split each site's series at its own quantile. With E = agreement − disagreement for a pair, the bound is:
for each pair k, (1−|E_k|)² ≥ Σ_{others} E², in the general-margin form (Gisin, Bancal, Cai, Remy, Tavakoli, Zambrini Cruzeiro, Popescu &
Brunner 2020, *Nat. Commun.* 11:2378, ineqs. 13/16). It bites only when pairs agree in more than ~70% of years (E > √2 − 1).

**(B) Continuous, any number of sites.** For Pearson correlations R, independent pair-sources force a "correlation budget": there are
loads t_ij ≥ 0 with r_ij² ≤ t_ij t_ji and Σ_j t_ij ≤ 1 for each site. Equivalently,
**V_G = (largest eigenvalue of |R − I|) − 1 ≤ 0** (Kela, von Prillwitz, Åberg, Chaves & Gross 2020, *IEEE TIT* 66, Prop. 1; pairwise case).
- It holds for *any* nonlinear response and local noise. The proof is the Hoeffding decomposition plus Cauchy–Schwarz, independently checked.
- It is exact: every R that passes is produced by some linear pairwise world.
- Three equal correlations need r ≤ ½. With three sites a one-factor model is saturated, so this is not a tetrad test.

**What a violation means.** Some common ancestor of ≥ 3 sites exists. **What it does not mean:** which one. And no violation means nothing.

**Conditions (B1):**
- Pair-sources must be *mutually* independent. Dependence between them is itself a shared cause.
- Each site depends only on its own sources and its own noise.
- **Stationarity across years:** a shared trend or regime shift acts as a common cause, because the pairwise-only set is not convex in
  general and mixtures of years can violate. So detrend first; simulated shared trends gave 61% false alarms without it.
- Within-site autocorrelation and per-site transforms (quantile splits, ranks, logs) do *not* invalidate the bound.

## 3. The pipeline
1. **Prepare.** Per-site normal scores (version B) or quantile splits (A). Linear detrend on year.
2. **Detect, with validated inference.**
   - (A) S2 = the largest excess over the 1/3, 1/2 and 2/3 quantile splits. Moving-block bootstrap lower bound, no wrap. Validated:
     size ≤ 0.03, and power ~0.75 for a common cause active in 30% of years at n = 72. That is double the median-split version.
   - (B) Numerical delta method (Hong & Li 2018, *J. Econometrics*; theory in Fang & Santos 2019, *REStud*), with step ε = ∞:
     T = √n·V̂_G, compared with the 95% point of the bootstrap largest eigenvalue of |√n(R̂* − R̂)|. Validated: size ≤ 0.05 across hard
     boundary worlds (rings, tied eigenvalues, φ = ±0.5, n = 30–53). **Power is low** for weak, diffuse common causes.
   - Naive bootstraps are invalid for (B) at 10 sites, with size up to 1.00. Inference on kinked functionals needs this theory.
3. **Candidate centres (model-conditional; B2).** Model-free tests establish *that* a common cause exists, not *which*. To probe a named
   candidate, add it as a regressor, state the linear-additive assumption explicitly, re-test, and run a **placebo** (the candidate with its
   years permuted). A violation that disappears means "no longer demonstrable", not "accounted for".
4. **Space or time.** A regional driver acts at once. Shared history (dispersal) shows lags along dispersal paths. This step is owned
   (Bjørnstad, Ims & Lambin 1999; Sheppard et al. 2016; Walter et al. 2017).
5. **Measurement centres.** A shared observer, protocol or calibration is also a common cause. Compare independent programmes.

## 4. Worked results (pre-registered gates in this folder)
- **Lake summer temperature** (5 Wisconsin lakes, ~45 years): E = 0.73–0.91, 10/10 triples violate (A). Regional weather; the control works.
- **Lake zooplankton:** 0/10 triples per group (A). Matches the known low temporal coherence of biological variables.
- **Beech, across programmes** (300–900 km, ~30 common years): no violations (median E 0.11). Weak null; power is low at n ≈ 30.
- **Beech, within the Polish programme:** median E 0.37 across same-study triples, top triples 0.7–0.86 (B4).
  - (A, S2, detrended): 40/120 triples significant after Holm.
  - (B, 10 sites jointly, validated): T = 34.9 against a critical value of 8.8. With each site's ΔT cue added: 29.7 against 9.2.
  - **A common cause of ≥ 3 sites is required.**
  - The ΔT cue lowers V_G by 0.50, where 200 placebo cues lower it by 0.003, so the cue is special. But most of the common cause remains
    after linear adjustment. Weather (other channels, or a nonlinear cue), history and protocol cannot be separated within one programme.
  - Bogdziewicz et al. 2021 (*Ecology*) already attribute beech synchrony to weather synchrony. The weather conclusion is theirs.
  - Disclosure (B4): the first Poland triple result (p = 0.008) came from a 1047-triple family where nothing passed Holm. It was later
    replicated by S2 and by (B).

## 5. Design rules learned
- Only strong synchrony is testable (A: E > ~0.41). Weak synchrony is never evidence against a common cause.
- Validate inference by simulation at the boundary before using it. Choose established methods over ad-hoc fixes.
- Resampling resolution must beat the multiple-testing threshold: resamples ≫ 20·(tests)/α.
- Don't average V over overlapping triples, and don't force one year window across many sites (N4: this replaces the earlier
  "pooled mean V" advice). Use per-triple windows with Holm, or the joint 10-site test (B).
- Median splits of heavily tied data must not break ties at random.
- Same-programme sites mix real and protocol common causes.

## 6. What is owned and what may be new
**Owned:**
- the bounds (Gisin et al. 2020; Kela et al. 2020) and the triangle-network literature (Fritz 2012; Wolfe–Spekkens–Fritz; Rosset–Gisin–Wolfe);
- classical common-ancestor tests (Steudel–Ay; Chaves et al. 2014);
- inference for kinked functionals (Fang–Santos 2019; Hong–Li 2018; Andrews–Soares 2010);
- synchrony science and its tools: Moran 1953; Liebhold, Koenig & Bjørnstad 2004; matrix regression / partial Mantel (Bogdziewicz et
  al. 2021); the wavelet Moran decomposition (Sheppard et al. 2016; Walter et al. 2017); lag analysis (Bjørnstad et al. 1999);
- conditioning on a candidate driver;
- masting cues (Kelly et al. 2013);
- the temporal coherence of lakes (Magnuson, Kratz et al.).

**Possibly new (not found in scouts; not yet claimed):**
- applying these causal-compatibility bounds to ecological synchrony, as a model-free test that synchrony *requires* a shared cause;
- the validated many-site version for time series.

Not compared yet: classical (not "any physics") inflation bounds, which may have more power (N5), and power against matrix-regression
and wavelet approaches.

## 7. Limits
- Low power at ecological sample sizes: only strong common causes are detectable.
- Attribution is model-conditional.
- Stationarity is assumed after linear detrending.
- Validation covers the simulated grid only (not extremely heavy tails, and not n < 30).
