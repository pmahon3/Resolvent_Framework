# Beech (Poland) as the positive control: attribution and negative controls. Pre-registered 2026-11-05, before running

reviewed: false. Known answer from the literature: beech masting synchrony is driven by solstice-anchored summer temperature cues
(Journé et al. 2024, *Nature Plants*, shelved: T1 = summer t−1 positive, T2 = summer t−2 negative, window opening at June 21), plus
weather synchrony (Bogdziewicz et al. 2021) and tail-dependent synchrony.

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
