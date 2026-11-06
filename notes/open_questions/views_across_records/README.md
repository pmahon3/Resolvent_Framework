# Views across records: synchrony and common causes (folder index)

reviewed: false. 2026-11-05. Collection: `../cyclic_marginal/views_across_records_taxonomy.json` (streams S0–S3; probes; owned regions).

## Reading order
1. `SYNCHRONY_CAUSALITY_METHOD.md`: working note v2 (example → ceilings → pipeline → results → owned/new → limits).
2. Ceilings and their checks:
   - `COVARIANCE_CEILING_CHECK.md` (proof of the continuous pairwise ceiling; owned by Kela et al. 2020);
   - `GAUSSIAN_PAIRWISE_MODEL.md` (derivation, nonlinear worlds; the early Poland inference there was invalid, its conclusion later confirmed).
3. Inference, in the order it was learned:
   1. `CEILING_TEST_VALIDATION.md` (yes/no test: size, power);
   2. `CEILING_POWER_STATS.md` (S2 adopted);
   3. `VG_INFERENCE_METHODS.md` (literature: Hong–Li, Fang–Santos, GMS);
   4. `VG_TEST_VALIDATION.md` (runs 1–4; ε = ∞ validated; Poland validated result);
   5. `REACH_TEST_VALIDITY.md` and `REACH_TEST_VALIDITY_CHECK.md` (proof for every m; independent check; corrected pipeline);
   6. `SPEARMAN_PROOF_SOURCES.md` (theorem chain for the bootstrap);
   7. `REACH_TEST_SPEARMAN.md` and `REACH_TEST_SPEARMAN_CHECK.md` (the provable version: proposition, check, validation V2, Poland V3).
4. Minimum source reach: `SOURCE_REACH_SCOUT.md` (FW_m, V_m, formal check, Poland m̂* = 4).
   **Positive control (complete):** `BEECH_POSITIVE_CONTROL.md` (known cue vs placebo; negative control).
5. Pre-registered gates, chronologically:
   - lakes: `LAKE_HARNESS.md`, `LAKE_PHYSICS_HARNESS.md`, `SYNCHRONY_CEILING_GATE.md`;
   - beech: `MAST_CEILING_GATE.md`, `MAST_CONDITIONAL_GATE.md`, `MAST_POLAND_POOLED_GATE.md`, `MAST_S2_GATE.md`.
6. Side results:
   - `DETECTION_FAKES.md` (detection error vs fake twists);
   - `synchrony_dataset_scout.md`.
7. Audits: `SYNCHRONY_CAUSALITY_METHOD_AUDIT.md` (v2); `SYNCHRONY_CAUSALITY_METHOD_AUDIT_v3.md` (v3: BORDERLINE; B6 head-to-head and B8 placebo open).
8. Later threads:
   - `HYPERGRAPH_CENTRES.md` (+ `_PRIOR_ART`), `HYPERGRAPH_METHOD.md`;
   - `DYNAMIC_CLOSURE.md` (+ `_PRIOR_ART`), `SPACE_TIME_DYNAMICS.md`, `ASSUMPTION_BREAKERS.md`, `POWER_CURVES.md`, `FINITE_EPS_REVALIDATION.md`;
   - `FRUSTRATION_ZOOPLANKTON.md`;
   - `SALMON_DATA_SCOUT.md`, `SALMON_FLOW.md`, `SALMON_OCEAN_DRIVER.md`.
   - Data: salmon from KNB df35b (spawner–recruit df35b.296.15, coordinates df35b.300.6) and the NOAA ERSST v5 PDO.

Scripts: `../verification/` (lake_*, synchrony_ceiling_gate, mast_*, ceiling_*, gaussian_*, vg_*, source_reach*, reach_m3_validation,
poland_rerun_prep2).

## Data (all public; NOT stored in the repo; re-download to reproduce)
- **MASTREE+** V2 (2024-06-26), CSV `MASTREEplus_2024-06-26_V2.csv`:
  - source: https://raw.githubusercontent.com/JJFoest/MASTREEplus/main/Data/MASTREEplus_2024-06-26_V2.csv (CC-BY-4.0);
  - also Dryad doi:10.5061/dryad.18931zd02.
  - Poland = Study_ID D00013, *Fagus sylvatica*, sites 008–017.
- **ERA5 daily 2 m mean temperature** via the Open-Meteo archive API (no key):
  - `https://archive-api.open-meteo.com/v1/archive?latitude=..&longitude=..&start_date=1940-01-01&end_date=2022-12-31&daily=temperature_2m_mean&timezone=UTC`;
  - at each site's MASTREE+ coordinates; rate-limited (use backoff).
- **NTL-LTER:**
  - zooplankton: knb-lter-ntl.37 rev 42 (`ntl37_v15.csv`);
  - physical limnology: knb-lter-ntl.29 rev 38 (`ntl29_v15.csv`);
  - EDI portal (browser download; Cloudflare check). Zips were saved to `~/Downloads/knb-lter-ntl.{37.42,29.38}.zip`.
- **CHB-MIT** EEG (neuro stream S3): https://physionet.org/files/chbmit/1.0.0/chb01/ (seizure files listed in `../neuro_critical/DELAY_GATE.md`).

## Literature (shelf = `notes/literature_review/literature/`, indexed in SHELF_INDEX.json)
**Shelved:**
- Gisin et al. 2020 (NSI triangle);
- Kela et al. 2020 (semidefinite tests);
- da Silva–Pozas-Kerstjens–Parisio 2025;
- Dzhafarov–Kujala–Cervantes 2020, and other CbD papers;
- Capotorti–Vantaggi 2011;
- Fritz–Chaves 2013;
- Fang–Santos 2019; Hong–Li 2018; Steudel–Ay (arXiv 2010);
- Journé et al. 2024 (solstice cue).

**Cited, not shelved (to fetch):**
- inference: Andrews & Soares 2010 (Econometrica); copula-bootstrap
  sources in `SPEARMAN_PROOF_SOURCES.md`;
- ecology: Kelly et al. 2013 (ΔT cue); Bogdziewicz et al. 2021 *Ecology* (beech synchrony from weather synchrony; owns that conclusion);
  Moran 1953; Liebhold, Koenig & Bjørnstad 2004; Sheppard et al. 2016; Walter et al. 2017; Bjørnstad, Ims & Lambin 1999;
  Reuman et al. 2023; Goldstein, Doser, Pease & Pacifici 2026 (*J. Anim. Ecol.*, read in full via SFU, not saved);
- other: Boman, Chen, Parekh & Toledo 2005 (factor width); Chaves et al. 2014.
