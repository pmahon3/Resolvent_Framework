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

## Result (2026-11-06). Script `verification/salmon_flow.py` (90 s)
**F1 Bristol Bay** (9 rivers, brood years 1959–2005, n = 47, recruits complete; mean |r| = 0.41):
| test | levels | innovations (own + 2 nearest lags) |
|---|---|---|
| V_G (pairwise only) | **REJECT** raw 16.2 vs 10.2; detrended 13.1 vs 10.1; 1977-step removed 14.8 vs 10.5 | 8.3 vs 9.7: not rejected |
| reach ≤ 3 / 4 / 5 | 4.7 vs 8.4 / not / not | not / not / not |
| radius ≤ 29 / 85 / 98 km | **REJECT** (15.6, 14.9, 11.8 vs ~9–10) | not |
| radius ≤ 128 / 194 km | not | not |
**F2 North Pacific, cross-agency** (7 stocks, 1969–1996, n = 28, mean |r| = 0.15): nothing rejected (raw, detrended, step-removed, reach, radius, innovations).
**F3 protocol-free triples** (ADF&G + DFO, 25 triples): 0 significant (min p = 1.0).

**Against predictions:**
- F1 detect: ✓ (robust to the 1977 regime shift).
- F1 m̂* ≥ 4: ✗. "Reach ≤ 3" is not rejected, so nothing beyond the triangle-level centre is demonstrated.
- F1 d̂ at a high decile: ✗. d̂ ≈ 128 km (the network spans 29–194 km decile range). Local centres within ~100 km cannot carry the synchrony;
  centres within ~130 km could.
- F1 innovations still reject: ✗ (not demonstrable).
- F2 null: ✓. F3 0–1: ✓.

**Reading:**
- Bristol Bay sockeye productivity requires a common cause of ≥ 3 rivers, reaching beyond ~100 km. That is robust to detrending and to the
  1977 regime shift. It is a **sub-regional** centre, not necessarily bay-wide.
- **The innovation null is ambiguous, not evidence of history.** A *persistent* shared driver (e.g. a slowly varying ocean condition) is partly
  predicted by each river's own lagged value, so its same-time residual shrinks. The VAR then assigns it to own-lag dynamics, not to interaction
  between rivers. Telling "slow common driver" from "accumulated interaction" needs the cross-lag terms, or a measured driver. Salmon age structure
  (4–5 years) adds lag dependence a VAR(1) misses. And n = 46 has low power.
- Across regions (BB ↔ Fraser ↔ Skeena ↔ Alaska Gulf), no common cause is demonstrated at n = 28 (weak null; mean |r| 0.15). With independent agencies
  no protocol-free common cause is found, but power at n = 28 is very low.
- The protocol confound for F1 remains (one agency).
