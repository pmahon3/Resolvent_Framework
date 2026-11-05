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
