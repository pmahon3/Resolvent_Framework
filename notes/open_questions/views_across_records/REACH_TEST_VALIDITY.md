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
