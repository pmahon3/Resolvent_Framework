# The reach test with Spearman correlations: proposition, assumptions, validation and Poland re-run (declared 2026-11-05, before running)

reviewed: false. Sources: `SPEARMAN_PROOF_SOURCES.md` (theorem chain); proof skeleton: `REACH_TEST_VALIDITY.md` and its check.

## Procedure (the provable version)
Data Y_t ∈ ℝ^k, t = 1..n, **not detrended**. R̂ = Spearman correlation matrix (Pearson correlation of within-series midranks).
T_m = √n·V_m(R̂). Moving-block bootstrap of time points (block b = round(n^{1/3}), no wrap), **re-ranking inside each resample**;
Z* = √n(R̂* − R̂). Reject H₀(m) : R_S ∈ FW_m when T_m > the (1−α)-quantile of V_m(Z*), where R_S is the population Spearman (grade) correlation matrix.

## Proposition (pointwise asymptotic validity)
Assume:
- (A1) Y is strictly stationary and α-mixing, with Σ_r (r+1)^{16(k+1)} √α(r) < ∞ (e.g. geometric mixing);
- (A2) continuous marginals, and the copula satisfies Segers' condition (Bücher–Volgushev 2013, Cond. 2.3; holds e.g. for full-rank Gaussian copulas);
- (A3) Cov(G) ≠ 0 for the Gaussian limit G of √n(R̂ − R_S).

Then, for every m ≥ 2 and every R_S ∈ FW_m: lim sup P(T_m > ĉ_m) ≤ α.

**Validity of the null itself:** if every latent source touches ≤ m sites, then R_S ∈ FW_m. Ranks are per-site transforms (the grade
transform), so Kela et al. Prop. 1 applies to the grade-transformed variables.

## Proof chain
1. **Domination (exact):** under H₀, T_m ≤ V_m(√n(R̂ − R_S)) (sublinearity of V_m; `REACH_TEST_VALIDITY.md`, independently checked).
2. **Limit:** under (A1)–(A2), the empirical copula process converges (Bücher–Volgushev 2013, Thm 2.4 / Cor 2.5). Spearman is a continuous
   linear functional of the copula (their Ex. 2.7), and the map to all k(k−1)/2 pairs is linear and continuous. So √n(R̂_plugin − R_S) ⇒ G.
3. **Bridge ⟦HAND⟧:** midrank-Pearson R̂ = R̂_plugin + o_p(n^{−1/2}), ties from duplicated bootstrap blocks included.
4. **Bootstrap:** the moving-block bootstrap with re-ranking and no wrap is consistent for the empirical copula process (Bücher–Ruppert 2013,
   Thm 2; block O(n^{1/2−ε})). The continuous mapping and the bridge carry this to √n(R̂* − R̂).
5. **Quantile ⟦HAND⟧:** under (A3) the law of V_m(G) has no atom at its (1−α) quantile (convexity argument in `SPEARMAN_PROOF_SOURCES.md`),
   so ĉ_m → c₁₋α(V_m(G)) and the size bound follows. ∎ (pointwise; not uniform)

**Open in the proof:** the two ⟦HAND⟧ links (3 and 5) need an independent check. Three references (Bühlmann 1993; Kosorok's bootstrap delta
method; van der Vaart's quantile lemma) were seen only via citing papers.

## Declared runs (before running)
- **V1 (independent check):** a fresh agent checks the proposition, links 3 and 5, and the conditions.
- **V2 (finite-sample size, Spearman, no detrend):** m = 2 with V_m(Z*) = ρ(|Z*|) on W1, W2, W3, W4, WD (as in `VG_TEST_VALIDATION.md` run 4;
  n ∈ {30, 53}, φ ∈ {−0.5, 0.5}; 300 simulations × 1000 resamples); m = 3 on the ring-of-triples boundary world (n = 53, φ ∈ {0, 0.5};
  100 × 300). Pass: size ≤ 0.07 (m = 2), ≤ 0.10 (m = 3).
- **V3 (Poland):** 10 sites, 53 years. (a) The provable version: Spearman, no detrend, reach m = 2…9 and V_G. (b) Sensitivity: Spearman on
  log1p-detrended series. Prediction: H₀(2), H₀(3) rejected and m̂* = 4 in both (normal scores and Spearman are nearly linear transforms of each
  other here; the trends were weak).

## Independent check (2026-11-05, `REACH_TEST_SPEARMAN_CHECK.md`) and amendment (before V2/V3 are run)
- The proposition holds under its stated hypotheses. Fixes:
  - link 3 (bridge): correct with a bounded-Lipschitz Slutsky step, and needs no ties in the sample (A2′);
  - link 5 (no-atom): correct; add that the distribution function is strictly increasing on [0, ∞);
  - the cited statements match the sources;
  - the null via Kela holds with ties; latents must be independent as whole processes.
  - Segers' condition can fail for threshold mechanisms.
- **Poland is outside (A2):** integer seed counts, 58–79% tied values per site. "Provable version" does not apply to the raw Polish data.
- **Amendment, the established remedy: jittering** (continuous extension for count data: Denuit & Lambert 2005; caveats in Genest & Nešlehová
  2007). Add independent N(0, σ²) noise to each observation before ranking, with σ = 10⁻³ × the site's smallest positive gap between distinct
  values. This breaks ties without reordering distinct values. Jitter is independent local noise, so H₀(m) is preserved and the jittered data
  have continuous margins, so (A2) holds for the jittered process. Each analysis is repeated over **20 jitter draws**; report the range.
  - **V2:** add a tied-data world (W1 discretised to 5 levels, plus a zero-inflated W2), analysed with jitter.
  - **V3:** (a) jittered Spearman, no detrend (the provable version under (A1) and Segers' condition for the jittered copula); (b) jittered
    Spearman on log1p-detrended series (sensitivity). 20 jitter draws each. Verdicts per draw; adopt the verdict that holds in ≥ 19/20.
- **Compute amendment (before running):** V3 uses m ∈ {2, 3, 4, 5}, with 1000 resamples for m = 2 and 300 for m = 3–5, per jitter draw (20 draws).
  V2 tied worlds: m = 2 only, n = 53, φ ∈ {−0.5, 0.5}, 300 simulations × 1000 resamples, one jitter per simulated dataset.

## V2 result (2026-11-05): PASS in every cell. Script `verification/spearman_validation.py`
| world | size (n = 30 / 53; φ = ±0.5) |
|---|---|
| m = 2, W1 (3 sites, r = ½) | 0.03–0.06 |
| m = 2, W4 spikes | 0.00 |
| m = 2, W2 (10 sites, all pairs) | 0.00 |
| m = 2, W3 ring | 0.00–0.01 |
| m = 2, WD (degenerate root) | 0.01–0.02 |
| m = 2, W1 discretised to 5 levels (jittered) | 0.01 |
| m = 2, W2 zero-inflated (jittered) | 0.00 |
| m = 3, ring of triples | 0.00 (φ = 0, 0.5) |
Max 0.06 ≤ 0.07 (m = 2), 0.00 ≤ 0.10 (m = 3). The Spearman ε = ∞ test, with jitter for ties and without detrending, holds size on all tested worlds.
