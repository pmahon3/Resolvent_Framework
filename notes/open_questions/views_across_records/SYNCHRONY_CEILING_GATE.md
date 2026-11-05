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

## Result (2026-11-05): control PASSES 10/10; zooplankton 0/10 for every group (prediction held)
Script `verification/synchrony_ceiling_gate.py` (n = 44–45 years per triple).
- **Temperature:** E = 0.73–0.91 in every pair. V = +1.14 to +1.48, bootstrap lower bounds +0.33 to +0.75, all 10 triples significant after Holm.
  Summer temperature synchrony across these lakes **cannot come from pairwise drivers under any physics**. A common
  ancestor of all three is required: regional weather, as expected.
- **Zooplankton (summer mean log density):** Daphnia E = −0.27…0.20 (V ≤ −0.52); copepods E = 0.09…0.47 (V ≤ −0.19);
  rotifers E = 0.0…0.64 (one point estimate V = +0.17 for CR-SP-TR, lower bound −0.29). **0 violations in every group.**
- Reading: the instrument works (the control is clear at n ≈ 45). The regional driver that synchronises temperature does not
  propagate into synchronised interannual zooplankton abundance strongly enough to force a common cause. That matches what
  limnologists call low "temporal coherence" of biological variables (Magnuson, Kratz et al., NTL lakes; Rusak et al. 1999,
  from memory, unread), which the bound now gives a causal reading.
- **Design rule:** with median splits and symmetric pairs, the bound bites only when pairwise synchrony E > √2 − 1 ≈ 0.41
  (agreement > 70%). Below that, the triangle (pairwise drivers) can always explain the data.
- What is new is only the reading: "above the ceiling ⇒ a common ancestor of all three, under any physics". The bound
  (Gisin et al. 2020) and the phenomenon (temporal coherence) are both owned.
