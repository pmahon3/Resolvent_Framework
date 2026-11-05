# Mast conditional gate: does the weather cue account for the common cause? Pre-registered 2026-11-05, BEFORE any weather data or conditional statistic

reviewed: false. Follows `MAST_CEILING_GATE.md`. Disclosure: the Poland triple's unconditional V was already seen there
(V = 3.36, p = 0.009), so stage 1 below is a replication, not confirmatory. **Stage 2 is the confirmatory test.**

## Family (rule-chosen, fixed now)
For each MASTREE+ study with ≥ 3 beech sites of ≥ 30 years: the triple with the most common years, if ≥ 30.
- Poland D00013: sites 008, 009, 010 (common years 1951–2022).
- Germany D06207: sites 001, 003, 006 (common years 1869–2022; analysed from 1942, when the weather starts).
- Italy D00022: excluded (28 common years).

## Candidate centre
ΔT(t) = mean June–July air temperature in year t−1 minus that in year t−2 (Kelly et al. 2013 cue), at each site's own location.
Source: ERA5 daily 2 m mean temperature, Open-Meteo archive API, at the site coordinates, 1940–2022.

## Statistic and inference (eq. 16 V as in MAST_CEILING_GATE)
- **Stage 1 (unconditional):** median-split the site series over the analysis years.
- **Stage 2 (conditional, confirmatory):** per site, OLS of the series on its own ΔT; median-split the residuals; V on the residuals.
- **Secondary:** residualise on T(t−1) and T(t−2) as two regressors.
- Moving-block bootstrap over years, block 3, **10⁵ resamples**. Bonferroni over the 2 triples, giving a one-sided 97.5% lower bound.

## Outcomes per triple
- **PERSISTS:** the stage-2 lower bound > 0. A common ancestor of all three remains after removing the ΔT cue (pollen history, another
  weather channel, or protocol).
- **VANISHES:** the stage-1 lower bound > 0 but the stage-2 lower bound ≤ 0. The ΔT cue accounts for the common cause, as far as this test can see.
- **NO-BASE:** the stage-1 lower bound ≤ 0.
- Caveat: residualisation is linear conditioning, so it removes only what a linear ΔT effect explains.

## Prediction (in advance)
Stage 1 violates in both triples. Conditioning on ΔT lowers V, but the violation PERSISTS in at least one triple: ΔT typically explains
only part of masting variance.

## Result (2026-11-05)
Script `verification/mast_conditional_gate.py` (ERA5 via Open-Meteo, nearest grid points within ~5 km; 4 s, 0.3 GB).

| triple | n | stage 1 V (lb97.5, p) | stage 2 \| ΔT: R² | stage 2 V (lb, p) | secondary \| T(t−1), T(t−2) | verdict |
|---|---|---|---|---|---|---|
| Poland 008-009-010 | 72 (1951–2022) | **+2.97** (+0.42, p = 0.008), E ≈ 0.69–0.75 | 0.05–0.09 | +1.27 (−0.38, p = 0.08), E ≈ 0.50–0.61 | +0.93 (−0.19, p = 0.045) | **VANISHES** (by rule) |
| Germany 001-003-006 | 81 (1942–2022) | +0.35 (−1.37, p = 0.42), E ≈ 0.41–0.48 | 0.08–0.19 | +0.66 (−0.79) | −0.31 | **NO-BASE** |

- Prediction ("stage 1 violates in both; persists in ≥ 1") **failed on both counts.** Germany's 1942–2022 synchrony sits at the ceiling,
  not above it.
- **Poland, read honestly:** the ΔT cue explains only 5–9% of each site's variance, yet removing it drops V from 2.97 to 1.27 and
  takes the violation below significance. The point estimate stays positive and residual synchrony (E 0.50–0.61) remains above √2−1.
  So "VANISHES" here means **"no longer demonstrable at n = 72"**, not "weather accounts for all of it". The ΔT cue carries a
  disproportionate share of the *common* part of masting, even though it explains little of each site's own variation. That is
  what a weak but shared cue should look like.
- Owned context: Kelly et al. 2013 (ΔT); Vacchiano/Ascoli et al. on beech masting cues (from memory, unread). The new element is
  only the reading: a causal-compatibility test showing that conditioning on the cue removes the *demonstrable* need for a
  further common cause.


> ⚠ 2026-11-05 audit: a time-permuted placebo ΔT lowers V as much as the real cue in 17% (one shared permutation) to 67%
> (per-site permutations) of draws. The VANISHES verdict stands by its rule, but the reading "a weak shared cue carries the common
> part" is WITHDRAWN. Linear residualisation removes this much V almost regardless of the regressor. See `SYNCHRONY_CAUSALITY_METHOD_AUDIT.md`.
