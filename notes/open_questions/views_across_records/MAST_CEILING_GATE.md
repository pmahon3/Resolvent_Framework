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
