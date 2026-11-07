# Beech (Poland) as the positive control: attribution and negative controls. Pre-registered 2026-11-05, before running

reviewed: false. Known answer from the literature: beech masting synchrony is driven by solstice-anchored summer temperature cues
(Journé et al. 2024, *Nature Plants*, shelved: T1 = summer t−1 positive, T2 = summer t−2 negative, window opening at June 21), plus
weather synchrony (Bogdziewicz et al. 2021) and tail-dependent synchrony.

**Name (added 2026-11-06, terminology pass).** V_G here is the same quantity as V₂ = ρ(|R − I|) − 1 (proved in `COVARIANCE_CEILING_CHECK.md`): the generalized diagonal dominance (H-matrix) margin. R ∈ FW₂ (scaled diagonal dominance) iff V₂ ≤ 0. New text says V₂; script and file names keep V_G.

## Already established (validated)
- Common cause of ≥ 3 stands required: V_G test T = 35.1 against crit 9.0.
- Minimum reach ≥ 4 of 10 stands.

## Data and pipeline
10 Polish sites (D00013), 53 years (1951–2019), ERA5 daily mean temperature at site coordinates. Corrected pipeline prep2: log1p → OLS on
[1, year, covariates] → normal scores. Validated ε = ∞ V_G test, 10 000 resamples (block n^{1/3}, no wrap; full prep in each resample).

## 1. Attribution control (does the known cue do what the theory says?)
Covariate sets, each site's own values:
- **A0:** none (year only), as before.
- **A1:** the old cue, ΔT_JJ = mean(Jun 1–Jul 31, t−1) − mean(Jun 1–Jul 31, t−2).
- **A2:** the solstice cue, ΔT_sol = mean(Jun 21–Jul 31, t−1) − mean(Jun 21–Jul 31, t−2).
- **A3:** the solstice cue as two regressors, T1_sol and T2_sol.
- **Placebo:** A2 with its years permuted, one permutation for all sites; 200 permutations; point V_G.

Report the point V_G, T, critical value and verdict for A0–A3, and V_G's placebo distribution.

**Predictions:**
- (i) V_G(A2) < V_G(A1), i.e. the solstice cue removes more of the common cause than the old window.
- (ii) Real-cue reductions are far below the placebo distribution (real cue special).
- (iii) The common cause is still required after A3: linear conditioning on a threshold-like cue cannot remove it all, and tail dependence
  is nonlinear.

## 2. Negative control (does the test stay silent without shared timing?)
Shift each site's series circularly by its own random offset (offsets distinct, ≥ 5 years apart), destroying cross-site alignment but
keeping each site's own dynamics. 50 shift draws; the V_G test on each (1000 resamples). **Expected rejection rate ≤ 0.10.**

## Result (2026-11-05). Script `verification/beech_positive_control.py` (63 min; pipeline prep2 with normal scores, as declared)
| covariates | V_G | T | crit | verdict |
|---|---|---|---|---|
| A0 year only | +4.82 | 35.07 | 9.02 | REJECT |
| A1 ΔT Jun 1–Jul 31 | +4.32 | 31.46 | 9.56 | REJECT |
| A2 ΔT solstice (Jun 21–Jul 31) | +4.32 | 31.45 | 9.15 | REJECT |
| A3 T1_sol, T2_sol | +4.29 | 31.21 | 10.23 | REJECT |
- **Placebo** (A2 years permuted, 200): V_G median +4.84, 5th percentile +4.70. **None** is as low as A2 or A1, so the real cue is special (p < 0.005).
  Prediction (ii) held.
- **Negative control** (50 circular-shift draws): rejection rate **0.00**. The test is silent when cross-site timing is destroyed. Passes.
- Prediction (i) **failed**: the solstice window removes no more than the full June–July window (difference < 0.01). June 1–20 adds little,
  so the two cues are nearly the same variable here.
- Prediction (iii) held: a common cause is still required after every linear cue adjustment. The known cue, entered linearly, removes ~10% of
  V_G. Either the cue acts nonlinearly or with thresholds (masting; tail dependence) or a further shared cause exists (other weather, protocol).
  Model-free inference cannot separate these.
- **Positive-control verdict:** the detection step finds the known common cause; the negative control is silent; the known cue is special against
  placebo. Attribution by linear adjustment is weak, consistent with a threshold-like cue. The instrument behaves as it should on a known case.
