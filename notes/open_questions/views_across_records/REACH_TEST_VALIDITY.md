# Validity of the ε = ∞ reach test for every m: proof and finite-sample check

reviewed: false. 2026-11-05. ⟦HAND⟧ by the main session. An independent check is pending (below).

## Proposition
Let V_m(R) = min{t : R + tI ∈ FW_m} and h_m(Z) = V_m(I + Z) + 1 = max_{X ∈ FW_m*, tr X = 1} −⟨X, Z⟩ (the recession / support function).
Test: reject H₀(m) : R ∈ FW_m when T = √n·V_m(R̂) > ĉ, where ĉ is the bootstrap (1−α)-quantile of h_m(√n(R̂* − R̂)). Then, under H₀(m), lim sup P(reject) ≤ α,
for every m and every null R, provided the bootstrap is consistent for √n(R̂ − R).

## Proof
1. **Exact domination.** V_m is convex and finite on symmetric matrices (a maximum of linear functionals), with recession function h_m.
   Convexity gives V_m(x + y) ≤ V_m(x) + h_m(y) for all x, y. With x = R and y = R̂ − R: V_m(R̂) ≤ V_m(R) + h_m(R̂ − R) ≤ h_m(R̂ − R) under H₀.
   h_m is positively homogeneous, so T ≤ h_m(√n(R̂ − R)) =: W **for every sample**.
2. **Bootstrap.** h_m is continuous (it is Lipschitz, as a support function of a bounded set) and does not depend on R. If √n(R̂* − R̂) → G
   conditionally, in probability, and √n(R̂ − R) → G, then by continuous mapping the bootstrap law of h_m(·) converges to the law of h_m(G),
   so ĉ → c₁₋α(h_m(G)). Under the same conditions W → h_m(G).
3. P(T > ĉ) ≤ P(W > ĉ) → P(h_m(G) > c₁₋α) ≤ α (at a continuity point of the law of h_m(G)). ∎
- The kink of V_m never enters: step 1 is an exact inequality.
- The test is conservative wherever V_m(R) < 0, or where the bound in step 1 is slack.

## Assumptions to check (open)
- Consistency of the moving-block bootstrap for √n(R̂ − R) under weak dependence: Künsch (1989); Lahiri (2003), for smooth functions of
  means. **Gap:** R̂ uses normal scores (ranks) and detrended residuals. Rank correlations are asymptotically linear (Hájek projection),
  and detrending removes a √n-estimable parametric part. Whether the joint pipeline is covered by an existing theorem has not been checked.
- Stationarity after detrending; mixing (the AR worlds satisfy it).
- Asymptotic statement only. Finite-sample size is checked by simulation: m = 2 validated (`VG_TEST_VALIDATION.md`); m = 3 below.

## Finite-sample check at m = 3 (declared before running)
World: 10 sites on a ring with one latent per consecutive triple {i, i+1, i+2} (10 latents), linear loadings, no local noise. Population R,
then R_s = I + s(R − I) with s chosen by bisection so that V₃(R_s) = 0 (on the boundary; the same structure, sparse). Data: stationary Gaussian VAR,
correlation R_s, common AR coefficient φ ∈ {0, 0.5}, n = 53. 100 simulations × 300 resamples. Pass: rejection rate of H₀(3) ≤ 0.10 (100 simulations).

## Independent check (2026-11-05, `REACH_TEST_VALIDITY_CHECK.md`): survives, with fixes
- Step 1 is correct and simpler: V_m is sublinear (a support function), so h_m = V_m, and domination is subadditivity. Holds for m ≥ 2.
- Step 2 is correct with a no-atom condition at the (1−α) quantile (Tsirelson, cited from memory). The result is **pointwise**, not uniform.
- Bootstrap consistency for this exact pipeline is covered by no single theorem: Berghaus–Bücher–Volgushev 2017 give a CLT for normal
  scores without a bootstrap; Bücher–Ruppert 2013 bootstrap the empirical copula. **Cited gap, stays open.**
- **Break: rank-then-detrend.** A real trend leaves spurious shared correlation, so the order must be detrend-then-rank (or Y stationary).
- Power: for m ≥ 3 the critical value is effectively that of −λ_min(Z*), the same for every m ≥ 3 (7.65 in Poland). Power for m ≥ 3 is low by construction.

## Corrected pipeline and Poland re-runs (declared 2026-11-05, before running)
prep2 = log1p, then OLS detrend on year, then per-site normal scores (inside every resample too). Re-run with prep2:
(a) the validated V_G test (m = 2), detrended and with ΔT added to the detrending regression; (b) the reach sequence m = 2…9. The same
seeds, resample counts and rules as before. Earlier results stand only if these reproduce them.

## Results (2026-11-05)
- **Finite-sample check at m = 3** (sparse ring-of-triples boundary world, V₃ = 0, V₂ = +0.97, n = 53): size **0.00** at φ = 0 and at φ = 0.5
  (100 simulations each). Conservative, as the power analysis predicts. `verification/reach_m3_validation.py`.
- **Poland re-run with the corrected pipeline** (log1p → detrend → normal scores), `verification/poland_rerun_prep2.py`:
  - V_G test: T = 35.1 vs crit 9.0 (detrended); 31.5 vs 9.5 (+ ΔT). Both REJECT, as before.
  - Reach: H₀(2) rejected (35.1 vs 8.95); **H₀(3) rejected (13.9 vs 8.01)**; H₀(4…9) not rejected. **m̂\* = 4 reproduced.**
  - All conclusions reproduce under the corrected order. The trends were weak.
- **Status:** Poland's "a common cause reaching ≥ 4 of 10 stands is required" now rests on:
  1. the proved domination bound;
  2. asymptotic validity, modulo the cited bootstrap gap for normal scores (closable via Spearman + Bücher–Ruppert 2013, proposed);
  3. finite-sample size checks at m = 2 (grid) and m = 3 (one hard world).

  The "provisional" label is downgraded to "validated on the tested worlds; one cited gap open".
