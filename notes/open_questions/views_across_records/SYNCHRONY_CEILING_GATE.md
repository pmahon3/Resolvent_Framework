# Synchrony-ceiling gate (seam A applied): pre-registered 2026-11-05, BEFORE computing any synchrony statistic

reviewed: false. Owner of the bound: Gisin et al. 2020, Nat. Commun. 11:2378, ineq. (13) (shelved).

## Test
Binarise each site's series at its own median, so every site is "on" half the time (E_i = 0). Let E_k be the ±1 correlations of the three pairs.
Triangle/NSI bound (13): for each pair k, (1 − |E_k|)² ≥ Σ_{j≠k} E_j². This holds for any model in which each pair shares
its own independent driver and nothing is shared by all three, under any physics. **V = max_k [Σ_{j≠k} E_j² − (1−|E_k|)²]**.
- V > 0 ⇒ a common ancestor of all three sites exists: a regional driver (centre in space) or shared history (centre in time).
- V ≤ 0 says nothing.

## Data (NTL-LTER, already downloaded; lakes AL, BM, CR, SP, TR; 10 triples)
- **Positive control:** water temperature at 1 m (ntl29; same depth rule as LAKE_PHYSICS_HARNESS). Summer mean (Jun–Aug) per lake-year.
- **Test:** zooplankton groups Daphnia, copepods, rotifers (ntl37; the same group map as LAKE_HARNESS). Summer mean of
  log10(density+1) per lake-year, one group at a time.
- Only years with data in all three lakes of the triple. One sample = one year (interannual synchrony; within-year seasonality removed by the summer mean).

## Inference
- For each triple: V and a one-sided 95% lower bound from a moving-block bootstrap over years (block length 3, 2000 resamples).
- **Violation** = lower bound > 0. Holm correction across the 10 triples within each variable (family α = 0.05).
- Small samples (~40 years): low power is expected. A null is weak evidence.

## Outcomes
- **Control passes** if temperature violates in ≥ 6/10 triples. If it fails, the test is too weak at n ≈ 40 and the zooplankton results are uninterpretable.
- **Zooplankton:** report violations per group. A violation in an isolated-lake triple = evidence of a regional driver of interannual abundance (Moran).
- Prediction (in advance): the control passes (shared weather, E ≈ 0.8+). Zooplankton shows 0–2 violations per group (weak interannual synchrony).
