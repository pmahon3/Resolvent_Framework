# Calibration data scout: >=3 methods, pairwise, loop closure

reviewed: false. 2026-11-06.

Scope: one web-search pass (about 7 queries) plus fetches of Dryad/GitHub pages. Not exhaustive. Only the Oneida files were actually downloaded; everything else was verified from landing pages only.

Main finding: no open dataset found with a true pairwise A-B, B-C, A-C calibration design. Every candidate is either (i) many methods applied to the same system, so pairwise ratios can be derived but share the system, or (ii) two-method calibrations. Loop closure on genuinely independent pairwise factors needs a different source (see Next).

## Ranked table

| # | Dataset | Methods | Pairwise design? | Shared reference? | n | Access / URL | Licence |
|---|---|---|---|---|---|---|---|
| 1 | Oneida Lake fish (Andres et al.) | eDNA, electrofishing, fyke, gillnet, seine (+ historical list) | No pairing. All 5 methods on one lake; ratios derivable per species, not per site | None (no census) | 85 species rows; ef_dat has 16 sites | GitHub (below); Dryad doi:10.5061/dryad.1c59zw3zk is raw FASTQ, 7 GB, do not fetch | Not stated on GitHub; Dryad "licensed for reuse" |
| 2 | Hamilton ON ponds, Dryad doi:10.5061/dryad.w9ghx3g07 | eDNA (2 primers), electrofishing and/or seine, pond drain census | Partly paired by pond | Yes: drain census | 14 ponds, a subset drained | https://datadryad.org/dataset/doi:10.5061/dryad.w9ghx3g07 ; small CSVs (about 1.4 MB), plus 6 GB tar (skip) | Not stated; "licensed for reuse" |
| 3 | Darras et al. 2018 meta-analysis, doi:10.5061/dryad.5nn3hf3 | sound recorders vs point counts | Two methods only, 28 studies | No | 28 studies | https://datadryad.org/dataset/doi:10.5061/dryad.5nn3hf3 (meta-analysis - data.csv) | Not checked |
| 4 | Darras distance-sampling, doi:10.5061/dryad.h0qg353 | recorders vs point counts | Two methods | No | not checked | https://datadryad.org/dataset/doi:10.5061/dryad.h0qg353 | Not checked |
| 5 | Zenodo 16411332 (Dutch agroforestry airborne eDNA) | eDNA, manual survey, acoustic, camera trap | Same site, 3-4 methods per taxon | None | unknown | https://zenodo.org/records/16411332 ; only 16Smam.zip seen, contents unverified | Not checked |
| 6 | NEFSC Bigelow-Albatross 2008 paired tows | two vessels | Paired, but 2 vessels only | No | 636 stations (per search summary) | No raw data link found; NOAA repository has reports only | n/a |
| 7 | Thygesen 2019 (Nansen vs Blue Sea) hake | two vessels | Paired hauls | No | 341 hauls | Paper only (DOI 10.1093/icesjms/fsy191); no data found | n/a |

Not found: any multi-vessel (>=3) paired-tow dataset, CPR vs net, phytoplankton method triples, LiDAR/field pairs. Not searched in depth.

## Recommended: Oneida Lake all-methods table (smallest, loadable now)

Downloaded and checked 2026-11-06 into `/Users/pmahon/.claude/jobs/26482d7b/tmp/calib/oneida/`.

- https://raw.githubusercontent.com/karaandres/Oneida_metabarcoding/master/datasets/all_methods_abundance.csv (3.2 KB, 85 rows)
  Columns: species, historical (0/1), eDNA (normalised reads, non-integer), Electrofishing, Fyke netting, Gill netting, Seining (counts).
- .../all_methods_presence.csv (4.3 KB, same species, presence/absence)
- .../ef_dat.csv, fyke_dat.csv, gillnet_dat.csv, seine_dat.csv (per-site species counts; ef_dat is 16 sites x species). Only ef_dat checked.
- Repo: https://github.com/karaandres/Oneida_metabarcoding (branch is master, not main).

## Caveats

- This is not a calibration design. It gives five unpaired views of one lake. A loop test would compare derived ratios (EF/fyke) x (fyke/seine) vs (EF/seine) per species, but counts are over different effort and gear areas, so the ratios are not independent factors and the loop closes trivially if you use the same species totals. Per-site files could give paired-by-site ratios; check whether site IDs align across gears first.
- Many zeros (rare species). Ratios undefined there.
- eDNA is read-proportional, not count. Treat as a different kind of unit.
- Licence on GitHub unstated. Dryad terms say reuse allowed. Confirm before redistribution.
- Items 3-5 were only read from search summaries and landing pages.

## Next

For a real pairwise-without-reference test: ask NEFSC for the 2008 paired-tow data, or search the ICES WGIBTS gear-comparison reports and Fisheries NZ intercalibration appendices for per-haul tables. Both are two-vessel; a triple needs chaining across separate experiments (Albatross-Bigelow plus Bigelow-third).
