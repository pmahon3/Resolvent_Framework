# Assumption breakers for the levels test (pre-registered 2026-11-06, before running)

reviewed: false. Test under study: Spearman + jitter, ε = ∞, Politis–White automatic blocks (adopted rule, `SPACE_TIME_DYNAMICS.md` run 3).
Two variants: **raw** (the provable version, no detrend) and **detrended** (log-free OLS detrend on time, then ranks).

## Worlds: 10-site ring, pairwise-only mechanism in every year (sources on ring edges; site = f(its two edge sources) + nothing shared by 3)
- **T (pair-specific trends):** edge source s_e(t) = β_e·(t/n) + AR(1) noise (φ = 0.5), with β_e ~ N(0, 2²) independent per edge.
  Mechanistically pairwise, but the calendar t is shared by all edges, so pooling years can manufacture correlation between non-adjacent
  sites. Expected: raw rejects often (the calendar acts as a centre); detrending removes it.
- **S (regime shift):** s_e(t) = γ_e·1[t > n/2] + AR(1) noise, γ_e ~ N(0, 2²). A step change at mid-series. Expected: raw rejects; linear
  detrending only partly removes a step.
- **N (Segers breaker, min-world):** site = min(s_{i−1,i}, s_{i,i+1}), stationary AR(1) sources (φ ∈ {−0.5, 0.5}). This copula has a singular
  component (P(A_i = A_{i+1}) > 0), so Segers' condition fails. Pairwise-only and stationary, so population V_G ≤ 0. Expected size ≤ 0.10
  (would show robustness beyond the proof's assumptions).
- **Control C:** the stationary linear ring at the boundary (the earlier W3), φ = 0.5.
- n = 53; 100 simulations × 500 resamples; jitter (σ = 10⁻³ × smallest gap) before ranking in every variant.

## Reporting
The rejection rate per world and variant. These are false-alarm rates *relative to the mechanistic, per-year causal structure*. For T and S
the calendar is a legitimate common cause in the pooled data, so rejection there means "the test reads a shared trend or shift as a common
cause" (the audit's V1 point), and the stationarity assumption is what rules it out.
