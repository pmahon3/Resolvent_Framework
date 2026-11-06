# The whole flow on Pacific sockeye salmon (pre-registered 2026-11-06, before any statistic is computed)

reviewed: false. Data: NCEAS portfolio-effects compilation (KNB df35b.296.15 spawner–recruit; df35b.300.6 coordinates); sources ADF&G reports and
the Dorner 2008 compilation (DFO data). Scout: `SALMON_DATA_SCOUT.md`. Only the schema, stock list and year coverage were inspected.

## Variable
Productivity residual per stock: y_t = ln(R_t / S_t) − (â − b̂·S_t), from an OLS Ricker fit per stock, indexed by brood year t. This is the standard
covariation variable (Peterman, Pyper et al.).

## Families
- **F1 Bristol Bay** (one programme, ADF&G): Alagnak, Egegik, Igushik, Kvichak, Naknek, Nushagak, Togiak, Ugashik, Wood. Brood years 1959–2014 (56).
- **F2 North Pacific, cross-agency:** Kvichak (Bristol Bay), Black Lake/Chignik River Watershed (Chignik), Kenai (Cook Inlet), Copper River (PWS),
  Frazer Lake (Kodiak) [ADF&G]; Skeena (BC North Coast), Chilko (Fraser) [DFO via Dorner 2008]. Common brood years only (≈ 1968–1998).
  Locations from the coordinate table; Fraser at its river mouth.
- **F3 protocol-free triples:** within F2, every triple with at least one ADF&G and one DFO stock (shared protocol excluded as the common cause).

## Flow (as validated; Spearman, Politis–White blocks, ε = ∞, 1000 resamples for m = 2, 300 for SDP-based tests)
1. **Detect:** V_G test on levels: raw, detrended, and with a 1977 step removed (PDO regime-shift sensitivity, per `ASSUMPTION_BREAKERS.md`).
2. **Reach:** H₀(m) for m = 3, 4, 5 (raw).
3. **Radius:** H(d) on decile radii of the inter-stock distances (raw).
4. **Present vs history:** the same tests on innovations from a restricted VAR (own lag + 2 nearest stocks' lags). Caveat: salmon age structure (4–5 years)
   gives lag-4/5 dependence that a VAR(1) may miss.
5. **F3:** the 3-site V_G test per triple, Holm across triples.

## Predictions (literature: sockeye productivity covaries within ~500 km via shared ocean conditions; weak across regions)
- **F1:** V_G rejects (raw, detrended, step-removed); m̂* ≥ 4; d̂ at a high decile (the whole bay); innovations still reject (same-time ocean driver).
- **F2:** V_G not rejected (cross-region correlations weak; n ≈ 31, low power). A weak null.
- **F3:** 0–1 triples significant.
