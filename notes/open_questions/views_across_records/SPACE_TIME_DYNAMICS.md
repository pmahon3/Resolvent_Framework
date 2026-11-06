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
