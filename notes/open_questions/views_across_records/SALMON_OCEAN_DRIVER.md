# Bristol Bay: a slow shared ocean driver, or rivers influencing each other? (pre-registered 2026-11-06, before running)

reviewed: false. Follows `SALMON_FLOW.md`: in Bristol Bay a common cause is required in levels (reach beyond ~100 km), but it is not
demonstrable in VAR innovations, which is ambiguous between a persistent shared driver absorbed by own lags and interaction.
Established practice (from memory): ocean conditions in the first summer at sea (brood year + 2 for Bristol Bay sockeye) drive productivity
covariation (Mueter, Peterman & Pyper 2002; PDO: Mantua et al. 1997).

## Data
- Productivity residuals as in `SALMON_FLOW.md` (Ricker residuals, 9 rivers, brood years 1959–2005).
- Covariate: PDO_t = mean NOAA ERSST v5 PDO, May–September of year t + 2 (the first marine summer).

## Tests
- **(a) Does the measured driver account for the common cause?** V_G test (as validated) on residuals after per-river OLS on PDO_t.
  - **Placebo:** PDO years permuted (one permutation for all rivers), 200 permutations, point V_G. Is the real drop larger than the placebo drops?
  - Report V_G before and after, and the verdict.
- **(b) Interaction beyond the shared driver?** Per river, OLS of y_i,t on [1, y_i,t−1, PDO_t] (restricted) vs adding the two nearest rivers' y_{t−1}
  (full). F-test for the neighbour terms; Holm across the 9 rivers. Secondary: the same with own lags 4 and 5 added (the cohort echo).

## Predictions
- (a) PDO explains part of the shared variation: V_G drops more than every placebo, but the common cause **remains required** (PDO is a basin-scale
  index; local ocean conditions matter more for Bristol Bay).
- (b) Neighbour lags are not significant (0–1 rivers after Holm): little across-year interaction between rivers, consistent with salmon life history
  (homing; no between-river exchange within a generation).

## Result (2026-11-06). Script `verification/salmon_ocean_driver.py`
- corr(PDO at the first marine summer, mean productivity) = +0.29.
- **(a)** V_G: +2.36 with no covariate → **+2.30 with PDO** (T = 15.8 vs 10.6, still REJECT). The real drop (+0.056) is **not special**: 18.5% of placebos
  drop as much (placebo 95th percentile +0.18). **The basin-scale PDO does not account for the common cause.** Prediction: half wrong (still required ✓;
  "drops more than every placebo" ✗).
- **(b)** Neighbour-lag terms: Holm-significant **0/9** (lag 1), and **0/9** with own lags 4 and 5 added (cohort echo). Smallest p = 0.03–0.05 before Holm.
  No evidence of across-year interaction between rivers. Prediction held.
- **Reading:** Bristol Bay's common cause is **not** across-year interaction between rivers, and **not** the basin-scale PDO. A shared driver at the
  bay/sub-regional scale remains (local ocean or freshwater conditions at entry, or the shared ADF&G protocol), unidentified by this index. The earlier
  innovation null is then best read as a persistent shared driver absorbed by own lags, or as low power, not as interaction.
- **Next principled candidate (not run):** a *local* driver, e.g. Bristol Bay / eastern Bering Sea SST in the entry summer (ERA5 SST via Open-Meteo
  or NOAA OISST). Basin indices are known to be weaker for local stocks.
