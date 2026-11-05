# Mast-seeding synchrony ceiling (beech): pre-registered 2026-11-05, BEFORE any seed values were read

reviewed: false. Data: MASTREE+ V2 (2024-06-26, GitHub JJFoest/MASTREEplus, CC-BY-4.0). Only the schema (columns,
Variable/Unit/VarType counts, species counts) was inspected before this file.

## Question
Beech masts in synchrony over large areas. The cause is contested: a weather cue (centre in space) versus pollen
coupling between stands (relations, i.e. a centre in time). Is the synchrony beyond what pairwise drivers can make, and does
that hold even for triples too far apart for pollen coupling?

## Series
- Species *Fagus sylvatica*. One series per Site_number. If a site has several, prefer Variable = seed, then fruit, then
  flower, then the rest; ties broken by longest length. Both VarTypes (C continuous, O ordinal).
- Years with a Value. Triples need ≥ 30 common years.

## Statistic
Median-split each site within the triple's common years ("above median" vs "at or below"). Ordinal ties can make the
margins unequal, so use the **general** NSI inequality (Gisin et al. 2020, eq. 16), valid for any margins:
(1+|E_A|+|E_B|+E_AB)² + (1+|E_A|+|E_C|+E_AC)² + (1+|E_B|+|E_C|+E_BC)² ≤ 6(1+|E_A|)(1+|E_B|)(1+|E_C|), taking the max over the 8
output relabelings. V = LHS − RHS; V > 0 is a violation (a common ancestor of all three is required).

## Inference
Moving-block bootstrap over years (block 3, 1000 resamples). One-sided p = fraction of resamples with V ≤ 0.
Holm across all triples in a class (family α = 0.05).

## Classes (fixed now)
- **Primary:** all three sites from different Study_IDs (removes shared-observer/protocol common causes).
- **Far:** primary triples with every pairwise distance > 100 km (pollen coupling negligible; a violation ⇒ a regional
  driver, not pollen history).
- **Near:** primary triples with every pairwise distance < 20 km (both mechanisms possible).
- Same-study triples are reported separately, as a measurement-confound check.

## Prediction (in advance)
Beech masting is strongly synchronous over hundreds of km, so violations in a clear majority of far triples, implicating
a regional (weather) driver. Near triples violate at least as often. Same-study triples violate more often (protocol shared).

## Result (2026-11-05): prediction FAILED for far triples; and a design flaw in the pre-registered inference
Script `verification/mast_ceiling_gate.py`. 23 beech sites have ≥ 30 years (of 307), giving 1468 triples with ≥ 30 common years.
- **Primary (three different studies): 421 triples, all of them also "far" (> 100 km; no near triples exist).** Weak synchrony:
  median mean-E 0.11, median n = 33. Point V > 0 in 3%. **0 Holm-significant.** Different-study sites 300–900 km apart do
  not mast together strongly enough to need a common ancestor. The prediction ("clear majority violate") was wrong.
- **Same-study (confound check): 1047 triples.** Stronger synchrony: median mean-E 0.37, median n = 69. Point V > 0 in 41%.
  The top triples (sites 009/012/013 etc., 100–360 km apart, n ≈ 70, E = 0.7–0.86) give V ≈ 3.4–3.7, bootstrap p = 0.002–0.009.
  **0 Holm-significant.**
- **Design flaw (pre-registered, so it stands):** with 1000 resamples the smallest attainable p is 0.001. Holm across 421 or
  1047 triples needs p < 5×10⁻⁵, so **nothing in a large family could ever pass**. The rule was unable to detect anything
  at this family size. This is recorded, not patched.
- Reading (descriptive): strong, ceiling-breaking synchrony appears only *within* studies, i.e. regional monitoring programmes
  over 100–400 km. There, regional weather, pollen history and a shared protocol are all live common causes, and this design
  cannot separate them. Across studies, at larger distances, the synchrony falls below the ceiling.
- A follow-up needs its own pre-registration: a resolution matched to the family (e.g. 10⁵ resamples, or FDR, or one
  pre-chosen triple per region); within-study triples split by distance; and a weather series as an explicit candidate centre
  (condition on it and see whether the violation disappears).
