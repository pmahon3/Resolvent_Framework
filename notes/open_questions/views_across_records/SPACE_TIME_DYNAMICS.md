# Centre in space vs centre in time: dynamic synthetic worlds (pre-registered 2026-11-06, before running)

reviewed: false. Tests the interpretive step "a violation is either a shared driver (space) or shared history (time)", which no run so far
has checked.

## Established tool (workflow rule)
Contemporaneous correlation of VAR innovations: common shocks vs dynamics (standard in time-series econometrics, e.g. Lütkepohl 2005,
*New Introduction to Multiple Time Series Analysis*, ch. 2, 9). Fit a VAR(1) by OLS; the residual (innovation) correlation measures same-time
common shocks. Lagged coefficients carry the propagation.

## Two-stage test (both use the provable test: Spearman, ε = ∞, moving-block bootstrap b = round(n^{1/3}), no wrap)
- **L (levels):** the test on raw levels x_t, as in the beech analyses. Reject ⇒ some common ancestor of ≥ 3 sites.
- **I (innovations):** fit a VAR(1) with intercept by OLS on the data (and **re-fit inside every bootstrap resample**, resampling blocks of
  (x_{t−1}, x_t) pairs), then apply the test to the residual Spearman matrix. Reject ⇒ a same-time common shock (centre in space).
- **Reading:** L and I ⇒ centre in space (the same-time shocks are shared). L but not I ⇒ centre in time (coordination through lagged dynamics).
  Neither ⇒ no evidence.

## Worlds (10 sites on a ring; x_{t+1} = a·x_t + coupling + shocks; a = 0.5; 200 burn-in years)
- **M (Moran):** shocks ε_{i,t} = η_t + e_{i,t} (one common η, unit variances). No dispersal.
- **D (dispersal):** x_{i,t+1} = a·x_{i,t} + d·Σ_{j ring-neighbour}(x_{j,t} − x_{i,t}) + e_{i,t}, with d = 0.25 and independent e. No shared shock.
- **P (pairwise null, boundary):** shocks = s_{i−1,i} + s_{i,i+1} (one independent shock per ring edge), no local noise. Innovation and level
  correlations are ½ between neighbours, 0 otherwise, which is on the pairwise boundary (V_G = 0). No dispersal.
- n ∈ {53, 200}; 100 simulations × 500 resamples per cell. The population V_G of levels and innovations is computed from the stationary
  covariance (discrete Lyapunov equation) and reported.

## Predictions
- **M:** L and I both reject (rate ≥ 0.8 at n = 200).
- **D:** if population V_G(levels) > 0, L rejects (power rising with n) and **I does not** (rate ≤ 0.10, since the innovations are independent).
  If population V_G(levels) ≤ 0, dispersal at this strength does not force a violation, and the "centre in time" demonstration fails at these parameters.
- **P:** L and I both ≤ 0.10 (size).

## Run 1 result (2026-11-06). Script `verification/space_time_dynamics.py` (4 min)
| world | population V_G levels / innovations | n = 53: L, I | n = 200: L, I |
|---|---|---|---|
| M Moran | +3.50 / +3.50 | 1.00, 1.00 | 1.00, 1.00 |
| D dispersal | **−0.85** / −1.00 | 0.00, 0.00 | 0.00, 0.00 |
| P pairwise boundary | 0.00 / 0.00 | 0.00, 0.00 | 0.00, 0.00 |
- M and P are as predicted (centre in space detected by both stages; the boundary null silent).
- **D: the pre-registered failure branch.** Population V_G(levels) ≤ 0, so there is no demonstration at these parameters. **Diagnosis:** a = 0.5 and
  d = 0.25 give each site zero weight on its own past (0.5 − 2·0.25 = 0). On an even ring, odd and even sites then decouple at any single time,
  and the same-time neighbour correlation is 0.00. This is a parameter artefact, not evidence that dispersal cannot coordinate.
- **Next (design step, population quantities only, no data):** scan (a, d) with a − 2d > 0 for population V_G(levels) > 0 and V_G(innovations)
  < 0, then pre-register run 2 at a chosen point.

## Parameter scan (population only) and run 2 (declared 2026-11-06, before running)
Scan for the dispersal world D (10-site ring), population V_G(levels):
| a | d | V_G |
|---|---|---|
| 0.5–0.8 | 0.05–0.2 | all **< 0**: neighbour r ≤ 0.25 |
| 0.90 | 0.10 / 0.15 / 0.20 | +0.08 / +0.38 / +0.61 |
| 0.95 | 0.10 / 0.15 / 0.20 | +0.83 / +1.31 / +1.67 |

**Finding (population level):** dispersal-only coordination breaks the pairwise ceiling only with high persistence (a ≳ 0.9) and moderate
dispersal. History must accumulate before a centre in time appears. Short-memory dispersal stays within pairwise reach.

**Run 2:** a = 0.95 in all three worlds.
- D2: dispersal d = 0.15.
- M2: Moran shocks as in M.
- P2: pairwise boundary shocks as in P.

n ∈ {53, 200}; 100 simulations × 500 resamples.

**Predictions:**
- D2: L rejects with power rising in n (high persistence shrinks the effective n, so power may be modest at 53); I ≤ 0.10.
- M2: L and I reject.
- P2: L and I ≤ 0.10 (P2's level correlations equal its innovation correlations, since every site has the same a, so the population is still on the boundary).
