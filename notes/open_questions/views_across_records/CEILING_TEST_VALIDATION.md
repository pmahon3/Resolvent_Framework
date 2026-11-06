# Validating the ceiling test: size and power by simulation (specified 2026-11-05, before running)

reviewed: false. Responds to audit defect V3 (`SYNCHRONY_CAUSALITY_METHOD_AUDIT.md`): it is unknown whether the bootstrap
lower-bound test has honest error rates near the boundary, at small n, with autocorrelation.

## Test under study
V = eq.-16 excess (as in `mast_ceiling_gate.py`) on median-split series. Reject "no common cause of all three" when the one-sided
95% bootstrap lower bound of V is > 0. Moving-block bootstrap **without wrap-around**, block length b ∈ {1, 3, 5}; 1000 resamples.

## Worlds
Each year, three pair-sources S_AB, S_BC, S_CA are AR(1) Gaussian (coefficient φ), independent across pairs. Site A = 1 iff
S_AB > τ_AB and S_CA > τ_CA (the AND rule), and similarly for B and C.
- **Boundary (size), symmetric:** all thresholds at P(S > τ) = 1/√2. This is the AND point, where V_pop = 0.
- **Boundary-near (size), asymmetric:** source probabilities (0.62, 0.71, 0.80). Pairwise-only, so V_pop ≤ 0.
- **Power:** each year, with probability ρ, all three sites copy one common coin (a common cause); otherwise the symmetric AND
  world. ρ ∈ {0.1, 0.2, 0.3, 0.5}.
- Grid: φ ∈ {−0.5, 0, 0.5}; n ∈ {45, 72}; 400 simulated datasets per cell.

## Outputs
- Rejection rates: size should be ≤ 0.05; power, by cell.
- A block-length rule: the smallest b that holds size at φ = −0.5 and φ = +0.5.
- Not a hypothesis test, so no verdict rule. It decides whether and how the instrument can be used.

## Run 1 (invalid, recorded): simulation artefact
v1 generated 0/1 site values and broke ties with 1e-6 noise. When a sample's share of 1s was below ½, the median fell inside the
0-cluster and the noise split that cluster at random, destroying correlations. Result: power ≈ 0.28 even at ρ = 0.5, which is
implausible given V_pop ≈ 2.7. **Lesson for real data:** median splits of heavily tied (ordinal or zero-inflated) series must not
break ties at random. [CORRECTED 2026-11-05: the claim "real beech seed counts are continuous" was FALSE. Polish D00013 series are
integers with 58–79% tied values (`REACH_TEST_SPEARMAN_CHECK.md`). The gate scripts split with a deterministic strict ">" at the quantile, never
random tie-breaking, so the yes/no gate runs are unaffected. Ties do matter for the continuous-copula theory.]

## Run 2 (valid, 2026-11-05): continuous worlds (site value = min of its two pair-driver margins; median split = AND exactly)
Rejection rates, 400 simulations per cell, resamples without wrap-around:

| world | n = 45 | n = 72 |
|---|---|---|
| size: AND symmetric (V_pop = 0) | 0.00–0.01 | 0.00–0.02 |
| size: asymmetric pairwise-only | 0.00–0.01 | 0.00–0.01 |
| power ρ = 0.1 | 0.01–0.04 | 0.03–0.05 |
| power ρ = 0.2 | 0.03–0.10 | 0.10–0.17 |
| power ρ = 0.3 | 0.16–0.23 | 0.31–0.41 |
| power ρ = 0.5 | 0.60–0.70 | 0.85–0.93 |

(Ranges are over φ ∈ {−0.5, 0, 0.5} and b ∈ {1, 3, 5}.)
- **Size is honest and conservative:** ≤ 0.02 in every boundary cell, including strong negative autocorrelation. Block length barely
  matters, so b = 3 is fine.
- **Power is low except for strong common causes.** At n = 72 a common cause active in half the years is detected ~90% of the time,
  in 30% of years ~40%, and in 20% of years ~15%.
- **Consequence for Poland:** a residual common cause of moderate strength (e.g. pollen coupling acting in a minority of years) is
  essentially undetectable with ~70 years at three sites. Absence of a demonstrated residual says almost nothing. Detecting
  ρ ≈ 0.2–0.3 needs either many more years or a more powerful statistic (classical rather than NSI bounds, audit V5; less
  information lost than a median split).
- Scope: AND-boundary worlds and one common-coin alternative only. Other boundary points are not covered.
