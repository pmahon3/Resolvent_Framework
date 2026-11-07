# Does coordination need a centre, and what shape is it? Model-free tests across sites

reviewed: false. v3, 2026-11-06 (re-audit fixes B4, B5, B7 + non-blocking wording applied; B6, B8 open). A working note: raw material for the author's own-words write-up, not for circulation. v2 was audited
REJECT-LIKELY as written (`SYNCHRONY_CAUSALITY_METHOD_AUDIT.md`); v3 rebuilds it on validated pieces. A re-audit is owed. Folder index:
`README.md`. Collection: `../cyclic_marginal/views_across_records_taxonomy.json`.

**Terms (added 2026-11-06; reviewed: false; see `../../programme/TERMINOLOGY_CROSSWALK.md`).** A **centre** is a common cause: a latent common ancestor of ≥ 3 sites (Reichenbach, The Direction of Time, 1956; shared driver = Moran effect). A **ceiling** is a network-local (NSI) bound (Gisin et al. 2020; Kela et al. 2020). FW₂ is **scaled diagonal dominance** (Boman et al. 2005). V₂ (written V_G in some files here; same quantity) is the generalized diagonal dominance (H-matrix) margin (Boman et al. 2005; Varga [unverified]). The size m of a centre is its **cause arity** (factor width m; formerly "reach" in this repo). H(d) is the **Vietoris–Rips complex** at scale d [unverified]. **Sign convention:** a cycle is **not antibalanced** when its correlation signs do not multiply to (−1)^{length}. This repo used to call such cycles "frustrated"; that is frustration of −R. A signed-graph reader calls product −1 "frustrated", which reads the other way on triangles.

## 1. A worked case
Three ponds, each pair sharing its own stream; the streams have good and bad years independently, and nothing is shared by all three.
- Best arrangement: a pond has frogs iff both its streams are good, each good with probability 1/√2.
- Then all three agree in (3√2 − 2)/4 ≈ **56%** of years (scope: each pond has frogs half the time, i.e. uniform margins; the general-margin bound is Gisin et al. eq. 16).
- No arrangement of independent pairwise causes does better, whatever the mechanism, in any physics (Gisin et al. 2020).
- More agreement needs a **centre**: something reaching all three.

## 2. Ceilings and cones (all owned)
- **Yes/no, three sites:** (1 − |E_k|)² ≥ Σ_{others} E² (Gisin et al. 2020, ineqs. 13/16).
- **Continuous, any number of sites:** pairwise sources force R ∈ FW₂ (scaled diagonal dominance; formerly a "correlation budget" per site in this repo). Equivalently V₂ = ρ(|R − I|) − 1 ≤ 0
  (Kela et al. 2020, Prop. 1; proof independently checked). It holds for any responses, local noise and per-site transforms.
- **Any hypothesis about the centres:** a hypergraph H of candidate centres gives the cone FW_H = {D + Σ_{S∈H} C_S} (Kela et al.; factor width, Boman et
  al. 2005). Special cases:
  - "cause arity ≤ m" (formerly "reach ≤ m") = FW_m;
  - "local centres within radius d" = H(d), the Vietoris–Rips complex at scale d (Vietoris 1927).
- **Which structures can show a centre at all:** from correlations, a centre beyond pairs can be revealed only on cycles that are **not antibalanced** (signs not
  multiplying to (−1)^{length}; formerly "frustrated" in this repo, see Terms). Antibalanced structure is always pairwise-explainable (Boman et al. 2005). The maximal excess on an odd L-cycle is
  sec(π/L) − 1. Chordal patterns: their cliques suffice (Agler et al. 1988).
- **Non-identifiability:** the minimal sufficient hypergraph need not be unique (K₄ example). Full distributions can separate more (Evans 2016).

## 3. Inference (ours: assembly and validation)
- **Test:** T_H = √n·V_H(R̂) against the 95% quantile of V_H(√n(R̂* − R̂)) (moving-block bootstrap with re-ranking, no wrap, Politis–White automatic
  block length).
- **Proved, pointwise asymptotic validity for every H that covers every pair** (an uncovered pair makes V_H = ∞; re-audit B5): exact domination T_H ≤ V_H(√n(R̂ − R)) under H₀, from sublinearity. Plus Bücher–Volgushev 2013
  (copula limit) and Bücher–Ruppert 2013 Thm 2 (block bootstrap). Conditions: Spearman correlations, jitter for ties, stationarity + geometric mixing,
  Segers' condition, Cov(G) ≠ 0. Hand links independently checked. **Scope of the proof (B5):** it covers raw levels with a fixed-rate block bootstrap. Politis–White automatic blocks, detrending,
  innovations and the hypergraph radius families are validated by **simulation only**.
- **Validated by simulation:** size ≤ 0.06 on boundary worlds (rings, degenerate roots, ties, zero-inflation, |φ| ≤ 0.5), with persistence up to a = 0.95,
  threshold mechanisms (Segers violated), and m = 3.
- **Failure modes:**
  - regime shifts fool the raw test (0.50); detrending fixes most of it (0.09);
  - fixed short blocks fail under persistence (fixed by automatic blocks);
  - all finite-ε Hong–Li variants fail size. Only the conservative ε = ∞ is valid.
- **Power:** only strong, wide centres are visible at n ≈ 50 (cause arity 10, λ² ≳ 0.2–0.3). An arity-3 centre is invisible. Polycentric vs monocentric is
  separable only for strong violations. **A null rules out little.**

## 4. What a detected centre is
Some common ancestor of ≥ 3 sites:
- **in space**: a shared driver;
- **in time**: accumulated interaction, which needs long memory;
- **in the observer**: a shared protocol, i.e. a method (batch) effect.

**Separating space from time:** test the shocks (VAR innovations) rather than the levels. This is standard (SVAR; Eichler; MARSS); applying the cone
tests to innovations is ours, by composition. Levels show the trek-rule closure of the innovation (shock) common causes (formerly "interaction-closure of the shock centres"). That is owned (trek rule; Lande et al. 1999;
Ripa 2000), and its content is a truncated bound, small unless memory is long. **Caveat:** propagation within one sampling interval looks same-time.

## 5. Applications (pre-registered gates; failed predictions recorded)
- **Lake temperature:** a centre (weather); the control works. **Lake zooplankton across lakes:** none.
- **Zooplankton within lakes:** triangles that are not antibalanced dominate (median 79%). Only Trout Lake needs a centre of ≥ 3 species (no multiplicity control across the 5 lakes). Crystal Lake is guild-structured:
  43% negative correlations but no triangle antibalanced.
- **Polish beech (positive control; chosen after its synchrony had been seen in earlier gates, so a control, not a confirmatory test, B4):**
  - a centre is required (T 35 vs 9), robust to detrending, ties, transform and jitter;
  - cause arity ≥ 4; regional (local centres within 368 km insufficient);
  - the same in innovations, i.e. a region-wide cause acting within a year (weather or the solstice cue, within-year pollen, or the protocol), not
    across-year history;
  - the known cue removes only ~10% linearly; "special against placebo" rests on an unmatched permutation placebo (re-audit B8, to redo with an R²-matched placebo);
  - the negative control (circular shifts) is silent. The literature (Journé et al. 2024; Bogdziewicz et al. 2021) owns the mechanism.
- **Bristol Bay sockeye:**
  - a centre is required (T 16 vs 10), robust to detrending and to the 1977 regime shift;
  - sub-regional (> ~100 km);
  - not demonstrable in innovations;
  - not the basin-scale PDO (not special vs placebo);
  - no evidence of across-year river interaction (0/9 rivers);
  - a specific method (batch) effect to probe: within-district catch apportionment by ADF&G (re-audit; snippet-level).
  - So an unidentified local shared driver, or the protocol.
- **North Pacific across agencies (n = 28):** nothing demonstrable (weak null).

## 6. Owned vs ours
- **Owned:** every ceiling, cone and structural theorem; the closure and innovation methodology; the inference theory; the ecological mechanisms.
  **Nearest existing tools (B7; snippet-level unless noted):** MARSS tests of the shock covariance Q (Ward et al. 2010, read); dynamic factor analysis /
  DFA (Zuur et al.) and generalized dynamic factor models (Forni–Hallin–Lippi–Reichlin); factor strength (Bailey–Kapetanios–Pesaran);
  cross-sectional dependence tests (Pesaran–Tosetti); spatial factor models (Lopes–Salazar–Gamerman); matrix regression / partial Mantel
  (Bogdziewicz et al. 2021); wavelet Moran decomposition (Sheppard et al. 2016); `ncf` spline correlograms (Bjørnstad). **No head-to-head comparison
  has been run yet (re-audit B6): the Type 7 bar is not met.**
- **Ours, as far as scouts found:**
  - the assembly into one framework (cones over hypergraphs of centres) for ecological synchrony;
  - the validity proof for any H and the validated inference recipe;
  - the cause-arity (formerly "reach") and radius tests;
  - the space/time/observer reading on innovations;
  - the applications.
- A methods-and-synthesis contribution, not new theorems.

## 7. Limits
- Low power.
- Attribution is model-conditional.
- Stationarity is assumed: check for regime shifts.
- Within-interval propagation counts as "same time".
- Observer vs nature needs independent programmes, and the only cross-agency family had n = 28.
