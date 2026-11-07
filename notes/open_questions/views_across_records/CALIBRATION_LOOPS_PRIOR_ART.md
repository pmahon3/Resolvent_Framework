# Calibration loops ("holonomy" of pairwise calibrations): prior-art scout

reviewed: false. 2026-11-06.

Read level: web-search snippets/abstracts only unless stated; nothing read past abstract. Shelf: SHELF_INDEX has no calibration/closure entry (only HodgeRank/Saari mention in a preference-cycle entry); taxonomy `views_across_records_taxonomy.json` has R-closure (closure phase, owned by Jennison 1958).

## Owned-region table

| Field | Owner | What it owns | Level |
|---|---|---|---|
| Interferometry | Jennison 1958 (R-closure) | closure phase = gauge-invariant loop sum | taxonomy |
| Geodesy | Gauss-Markov levelling-network adjustment; misclosure per loop, chi-square global test, w-test/Baarda data snooping, minimal-constraint (datum) adjustment | closure test, minimal LS adjustment, per-loop misclosure | textbook knowledge, not re-read |
| Metrology | Cox 2002 (Metrologia, key-comparison data), Cox 2007 (largest consistent subset); Cox-Harris-Woolliams, linked bilateral comparisons; constrained LS w/ KCRV as the constraint | chi-square consistency of linked comparisons, reference-value as gauge choice | abstracts |
| Ranking / decision | Jiang-Lim-Yao-Ye 2011 (Math. Prog., arXiv 0811.1067) HodgeRank | exact decomposition of pairwise flow = gradient (common scale, LS) + curl (local triangle inconsistency) + harmonic (global loop inconsistency); LS regression, incl. incomplete/imbalanced graphs | abstract |
| Decision | Saaty CI/CR; Koczkodaj triad inconsistency; multiplicative (log) consistency of PC matrices | per-matrix/triad inconsistency index | not read |
| Synchronization / vision | Singer 2011 angular synchronization; cycle consistency; group synchronization (Z, SO(2), SE(3)) | group-valued closure, global LS recovery; Z_n/R version = offset case, R_+ = ratio case | not read |
| Time transfer | GPS common-view / two-way triangle closure | closure of clock differences | not read |
| Fisheries | NAFO SCR 99-104 (chained relative fishing power between vessel pairs, with a stated direct-vs-indirect consistency relation); ICNAF res-117 (agreement of RFP vs CPUE ratios); Thygesen et al. 2019 ICES JMS 76:1189 (paired-haul intercalibration, catchability + selectivity) | pairwise relative-efficiency estimation, chain to a standard vessel, consistency check of local vs global factors | snippets |

## Verdicts

(a) Closure test: OWNED, many times over (geodesy, metrology chi-square, AHP, synchronization). Nothing new in "offsets sum to 0, ratios multiply to 1"; ratios = log offsets.

(b) Minimal-adjustment budget: OWNED. Minimal-norm LS correction to make edge data a gradient is the Gauss-Markov adjustment and the HodgeRank projection; its residual norm is the budget. Metrology's constrained LS = same with a datum choice. Only a "budget" naming is ours.

(c) Decomposition of misclosure across loops: OWNED by HodgeRank (curl = triangle-local, harmonic = global cycle space), and by geodesy (per-loop misclosures = cycle-space coordinates). Caveat: HodgeRank is on a clique complex; harmonic part depends on which cycles are filled (2-cells), so "which loops are local" is a modelling choice there too.

(d) Ecological practice: PARTLY OWNED, thin. Fisheries gear/vessel intercalibration already chains pairwise relative-efficiency factors to a standard and states a consistency relation (NAFO SCR 99-104, hearsay-level; not read). Search found no study with camera trap / eDNA / transect calibrated pairwise on >=3 methods with a loop-closure test; existing multi-method work uses co-detection comparisons or joint (integrated) models (e.g. joint models for transect + camera). Absence is from one standard search, not exhaustive.

## Residue (if any)

- Applying the (owned) closure/Hodge machinery to eDNA/camera/transect pairwise calibrations as a diagnostic: plausible Type 6 (translation) at best; not theory. Likely checks: whether integrated/joint models (a single latent abundance) already make closure automatic (they impose a common scale, so closure failure is invisible); a loop test would test that assumption.
- Ecology-specific: pairwise conversions are not constant (depend on density, habitat, season, species detectability), so "closure" is a statement about a covariate-dependent ratio; unaddressed by the owners above (metrology assumes a fixed measurand). Untested whether this is more than a modelling remark.
- Nothing here bears on the programme's theory (pointless coherence); this is an instance of the abelian/cohomological case (H^1 of the graph with R or R_+ coefficients), owned.

## To read before any claim
Jiang et al. 2011 Sec. 3-4; Cox-Harris-Woolliams linked-comparison paper; NAFO SCR 99-104; Singer 2011; a geodesy adjustment text (e.g. Koch or Teunissen) for w-test.
