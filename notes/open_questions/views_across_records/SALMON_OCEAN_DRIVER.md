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
