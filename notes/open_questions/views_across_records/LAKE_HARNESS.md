# Lake calibration harness (S1 × S2): pre-registered 2026-11-05, BEFORE the data was seen

reviewed: false. Collection: `cyclic_marginal/views_across_records_taxonomy.json`.

## Puzzle
Three lakes, each measuring a different pair of {Daphnia, copepods, rotifers}. Can one shared dynamics explain
all three pairs? If not, the lakes must differ by at least ε*, learned without ever comparing the same pair
in two lakes. Here every lake actually records all three groups, so the truth is known. The harness asks
how informative the split-design ε* is against that truth and against noise.

## Data
NTL-LTER zooplankton, Trout Lake area (EDI knb-lter-ntl.37 rev 42, `ntl37_v15.csv`). Lakes: the five drainage/seepage
lakes AL, BM, CR, SP, TR (the bogs CB and TB are excluded as different systems).

## Pipeline (fixed now)
1. Groups: Daphnia = genus *Daphnia*; copepods = calanoid + cyclopoid copepods (adults and copepodids; nauplii
   excluded); rotifers = all Rotifera. The taxon-to-group list is written from the species-name list only, before any
   densities are looked at, and committed with the script.
2. Per lake and sample date: group density = the sum over its taxa; x = log10(density + 1). Rows with several
   stations/depths per date are averaged.
3. Binarise per lake and group: above vs at-or-below that lake's median. The single margins are then ½ in every lake,
   so the visible single-group check passes by construction. The test is about how the groups move together.
4. d_ij(lake) = fraction of that lake's dates on which groups i and j fall on different sides of their medians.
5. Split design (a, b, c) = (lake for pair D–C, lake for pair C–R, lake for pair R–D). ε*_split = V/3 (binary triangle
   theorem). All 5·4·3 = 60 ordered designs.
6. Control: same-lake designs must give V = 0 exactly.
7. Truth: δ_full(a,b,c) = min over Q on {0,1}³ of max_k TV(Q, P_k^full), where P_k^full is that lake's empirical
   three-group joint (LP). Guaranteed: ε*_split ≤ δ_full.
8. Noise floor: pseudo-lakes from one lake. Split its years into three interleaved sets (year mod 3) and form the 6
   ordered designs over those sets. Gives ε*_null (5 lakes × 6 = 30 values), plus δ_full for the pseudo-lakes.

## Outcomes
- **INFORMATIVE:** median ε*_split over the 60 real designs > 95th percentile of ε*_null, AND Spearman(ε*_split, δ_full) > 0.5.
- **LOOSE:** above the null but Spearman ≤ 0.5, i.e. it detects difference without tracking it.
- **TOOTHLESS:** median ε*_split ≤ 95th percentile of ε*_null.
- No p-values (dates are autocorrelated). This is descriptive calibration only.

## Prediction (in advance)
ε*_split small (≤ 0.05) and probably TOOTHLESS or LOOSE. The lakes share one climate and season, and median
binarisation of seasonal series ties the groups mostly through their shared seasonality. δ_full may still be clearly
above the pseudo-lake null, which would mean the lakes differ in ways the loop doesn't see.

## Result (2026-11-05): pre-registered verdict TOOTHLESS (prediction held)
Script `verification/lake_harness.py`. Group map fixed from codes/names before densities were read: Daphnia 51100–51199;
copepods 20000–20999 (not 29900) + 30000–30999; rotifers 60000–63999 or "ROTIFER" in the name. Lakes AL, BM, CR, SP and TR,
with 315–530 dates each, 1981–2025.
- Sanity: same-lake V = 0 in every lake.
- **ε*_split = 0 in all 60 real designs and all 30 pseudo-lake designs.** The bound ε*_split ≤ δ_full held (asserted).
- δ_full (the truth from full data): real median 0.071 (max 0.086); pseudo-lake null median 0.076 (95th percentile 0.136).
  Between-lake full-joint differences are not larger than one lake's year-thirds differ from each other. Caveat: the
  pseudo-lakes have a third of the dates, so their δ_full carries more sampling noise and the two aren't strictly comparable.
- **Why the loop is blind here:** the disagreement rates are all 0.28–0.54, in the slack interior of the triangle. The closest
  design (TR, BM, AL: d = 0.301, 0.308, 0.540) has slack 0.069. A violation needs one pair tied much more strongly than the others,
  i.e. some d near 0 or 1. This is the same failure as the neuro DELAY gate: moderate ties keep the triangle slack.

## Reading
- The sign loop test only has teeth on strongly tied groups. Median-binarised zooplankton groups are not strongly tied,
  even with seasonality.
- **Correction to the closure-phase idea for lakes (⟦HAND⟧).** With a shared calendar, each group's seasonal phase is
  visible in each lake on its own. The annual-frequency loop phase then equals a sum of *visible* single-group phase
  differences (CbD's visible part). It adds nothing invisible. Closure phase helps only when records have **no common
  clock**: paleo cores with independent chronologies, unsynchronised instruments. Lakes on one calendar are not that case.
- What the loop would need here: groups tied strongly *within* lakes, but in different ways across lakes. That is a
  property of the system, not something better analysis can supply.
- The next probe, if any, is a separate pre-registration. Candidates: strongly tied variable triples (e.g. temperature,
  oxygen, chlorophyll in the physical-limnology data, where ties are near-deterministic); or paleo records with no
  common clock.
