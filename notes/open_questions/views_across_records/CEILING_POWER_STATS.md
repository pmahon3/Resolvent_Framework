# Raising power: alternative common-cause statistics (specified 2026-11-05, before running)

reviewed: false. Follows `CEILING_TEST_VALIDATION.md` (the median-split eq.-16 test: size ≤ 0.02, power ~0.4 at ρ = 0.3, n = 72).

## Statistics (each has population value ≤ 0 under "no common cause of all three")
- **S1 (baseline):** eq.-16 V at the median split.
- **S2:** max over q ∈ {1/3, 1/2, 2/3} of eq.-16 V, all three sites split at their own q-quantile. Every fixed-quantile
  binarisation is local post-processing, so each V_q ≤ 0 under H₀, and so is their max.
- **S3:** max over all 27 per-site combinations of those quantiles.
- **S4:** Steudel–Ay with c = 2 at the median split: I = ½ Σ H(X_i) − H(X₁,X₂,X₃), in bits (plug-in entropies).
- **S5:** Steudel–Ay at tertiles (3-letter alphabets, plug-in).

Test: the one-sided 95% moving-block bootstrap lower bound (b = 3, no wrap, 1000 resamples) is > 0. **Caveats fixed in advance:** maxima
(S2, S3) and plug-in entropies (S4, S5) are biased upward in small samples, so their size must be checked, not assumed.

## Worlds (as in the validation run)
Continuous AND worlds and the common-cause mixture (ρ). n = 72, φ ∈ {−0.5, 0}. Size: AND symmetric and asymmetric. Power:
ρ ∈ {0.2, 0.3, 0.5}. 300 simulations per cell.

## Decision rule (fixed now)
Adopt a statistic over S1 only if its size is ≤ 0.05 in every size cell AND its power at ρ = 0.3 exceeds S1's by ≥ 0.10 in both φ cells.
Otherwise keep S1.

## Result (2026-11-05): ADOPT S2 (by the pre-registered rule)
n = 72, 300 simulations per cell:

| cell | S1 median | **S2 max over 3 quantiles** | S3 max over 27 | S4 SA median | S5 SA tertile |
|---|---|---|---|---|---|
| size, AND symmetric (φ −0.5 / 0) | 0.00 / 0.00 | **0.02 / 0.02** | 0.09 / 0.06 | 0 / 0 | 0 / 0 |
| size, asymmetric | 0.01 / 0.00 | **0.02 / 0.03** | 0.07 / 0.07 | 0 / 0 | 0 / 0 |
| power ρ = 0.2 | 0.18 / 0.20 | **0.42 / 0.48** | 0.60 / 0.66 | 0 / 0 | 0 / 0 |
| power ρ = 0.3 | 0.41 / 0.39 | **0.76 / 0.74** | 0.90 / 0.87 | 0 / 0 | 0 / 0 |
| power ρ = 0.5 | 0.94 / 0.95 | **0.99 / 0.99** | 1.00 / 1.00 | 0 / 0 | 0 / 0 |

- **S2 roughly doubles power at ρ = 0.2–0.3 with size ≤ 0.03: adopted.** S3 is more powerful but its size reaches 0.09 (fails).
  Steudel–Ay (S4, S5) has zero power here: the entropic bound is far looser than the NSI bound for these worlds.
- Scope: the same worlds as the validation run. The power gain is for a common cause acting in a fraction of years.
