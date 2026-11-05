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
