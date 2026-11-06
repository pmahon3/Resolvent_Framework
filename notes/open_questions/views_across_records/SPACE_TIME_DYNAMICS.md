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

## Run 2 result (2026-11-06): the innovation test separates space from time; the LEVELS test fails size under high persistence
| world (a = 0.95) | population V_G levels / innov. | n = 53: L, I | n = 200: L, I |
|---|---|---|---|
| M2 Moran | +3.50 / +3.50 | 0.90, 1.00 | 0.98, 1.00 |
| D2 dispersal (d = 0.15) | +1.31 / −1.00 | 0.10, 0.00 | 0.37, 0.00 |
| **P2 pairwise boundary** | 0.00 / 0.00 | **0.55**, 0.00 | **0.60**, 0.00 |
- **Validity failure (not predicted):** the levels test L is oversized at a = 0.95, with 55–60% false alarms on the boundary world. Blocks of
  b = round(n^{1/3}) ≈ 4–6 years cannot capture ~20-year memory, so the bootstrap understates the variability of the correlations. The earlier
  validations covered |φ| ≤ 0.5 only. The beech results are unaffected (beech masting has negative lag-1 autocorrelation, covered by the
  φ = −0.5 cells). Persistent systems are not covered.
- **Innovation test I:** valid (0.00 on P2), detects the same-time common shock in M2 (1.00), silent on D2 (0.00). It separates "centre in
  space" from its absence, as predicted.
- **Centre-in-time demonstration: INCONCLUSIVE.** D2's levels rejections (0.37 at n = 200) cannot be read as power, given P2's size.
- **Next, by the established method:** automatic block-length selection for dependent data (Politis & White 2004; Patton, Politis & White 2009
  correction). Read, implement, re-validate L on P2 and D2 (a = 0.95), then retry D2. Until then, **do not apply L to strongly persistent series.**

## Run 3 (declared 2026-11-06, before running): automatic block length
- Method: Politis & White 2004, with the Patton, Politis & White 2009 correction, as implemented in `arch` 8.0.0 `optimal_block_length` (b_cb). The
  moving-block bootstrap and the circular-block bootstrap share the optimal block order.
- Rule: b = ceil(max over sites of b_cb(rank series of that site)), clipped to [2, n/3]. For the innovation test, b is computed on the levels
  (pairs are resampled as blocks of years).
- Worlds: M2, D2, P2 (a = 0.95) at n ∈ {53, 200}. Re-check of the earlier grid with the new rule: W1 and W3 (static, φ = ±0.5, n = 53). 100
  simulations × 500 resamples.
- Pass: P2, W1, W3 size ≤ 0.10 (100 simulations). Then read D2 L as power.
- Prediction: P2 L size falls to ≤ 0.10. D2 L power is modest at n = 53 and higher at n = 200. I is unchanged.

## Run 3 result (2026-11-06): automatic block length fixes size; centre in time detectable with long series
| world | n = 53: L, I | n = 200: L, I |
|---|---|---|
| static W1 (φ = ∓0.5) | L 0.04 / 0.02 | — |
| static W3 ring (φ = ∓0.5) | L 0.01 / 0.00 | — |
| M2 Moran (a = 0.95) | 0.73, 0.98 | 0.87, 1.00 |
| **D2 dispersal (a = 0.95)** | 0.03, 0.00 | **0.20, 0.00** |
| **P2 boundary (a = 0.95)** | **0.06**, 0.00 | **0.03**, 0.00 |
- **Size restored** with Politis–White blocks: P2 0.06 / 0.03 (was 0.55 / 0.60). The static worlds stay valid.
- **Centre in time, demonstrated (weakly):** in the dispersal-only world the levels test rejects 20% at n = 200, against 3% under the boundary null,
  and the innovation test never fires (0.00). Reading: "a common ancestor exists, and it is not a same-time shared shock", i.e. coordination built
  by history. At n = 53 it is essentially undetectable (0.03).
- The price: power for the Moran levels test drops (0.73 at n = 53). The innovation test keeps the Moran detection (0.98–1.00).
- **Adopted rule:** use Politis–White automatic blocks (`arch` `optimal_block_length`, circular column; max over sites; clipped to [2, n/3]) for
  the levels test. The innovation test separates space from time.
- Prediction held (P2 ≤ 0.10; D2 modest at 53, higher at 200; I unchanged).
- The beech results used fixed n^{1/3} blocks on anti-persistent series (validated at φ = −0.5). They are not re-run here; doing so with the new rule
  would be a consistency check.
