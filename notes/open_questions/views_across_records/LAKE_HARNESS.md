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
