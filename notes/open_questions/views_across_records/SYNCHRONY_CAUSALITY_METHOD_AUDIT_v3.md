# Audit: SYNCHRONY_CAUSALITY_METHOD.md v3 (mode: full, skill v2.1). Re-audit

reviewed: false. 2026-11-06. Auditor: opus agent running `/audit full`. The target was not edited. No new computations were run.
Every numeric claim below was checked against the folder's result files. Web reads are marked [snip] (snippet or abstract) or [mem]
(from memory, not checked).

## Audit: `notes/open_questions/views_across_records/SYNCHRONY_CAUSALITY_METHOD.md` (mode: full)

### Declared contribution type(s): 7 (methodology), 6 (exposition/translation), 3 (unifying framework: cones over hypergraphs of centres)
The types are declared in the audit request, not in the note. The note's §6 says "a methods-and-synthesis contribution, not new
theorems". That matches Types 7, 6 and 3. It still states no per-type bar it commits to clearing (carried over from v2).

**Bearing on WHY.md:** this is the programme's most direct test of "order without a centre". v3 can now say how wide a centre must
be (reach, radius), and whether it acts at one time or builds up through history (innovations). Hidden idealisation: "same time"
means "faster than the sampling interval". Loop: a centre beyond pairs shows only on frustrated cycles, the programme's parity twist
again. That is composition, not circle.

---

### Status of the v2 blocking fixes

| fix | status | evidence in v3 |
|---|---|---|
| **B1** stationarity | **RESOLVED** | §3 lists stationarity and geometric mixing as conditions; §3 failure modes give regime shifts 0.50 raw and 0.09 detrended (`ASSUMPTION_BREAKERS.md`); §7 "Stationarity is assumed". The binarised median test that B1 targeted has been replaced by the rank-correlation cone test. Per-site transforms are covered in §2. Residue (non-blocking): say in one line that a shared trend or step *is* a common cause in the pooled data (the calendar acts as a centre), which is why the null fails. |
| **B2** OLS conditioning step | **PARTLY RESOLVED (one blocking residue, B8)** | OLS residualisation is no longer a test of "the centre is gone". The "accounts for the common cause" and "what a centre looks like" sentences are gone. The cue-vs-placebo comparison is still an inference, though. v2 B2 required an **R²-matched** placebo, because a time-permuted placebo (R² ≈ 1/n) is biased *in the driver's favour*. v3 §5's beech claim "the known cue is special against placebo" rests on exactly that unmatched permutation placebo (`BEECH_POSITIVE_CONTROL.md`: 200 permutations, one shared across sites). So it is the claim v2 warned about. The PDO verdict "not special" survives, because the bias favoured the driver and it still lost. |
| **B3** owned vs new | **PARTLY RESOLVED** | §6 now puts the closure and innovation methodology and the ecological mechanisms under "Owned", and the Goldstein sentence is gone. **Still missing in v3:** named credit for ecology's existing tools for the same questions: matrix regression / partial Mantel (Bogdziewicz 2021 is cited only for the mechanism), wavelet Moran (Sheppard 2016; Walter 2017), the synchrony–distance function `ncf` (Bjørnstad et al. 1999), MARSS Q-structure comparison (Ward et al. 2010, cited only in `DYNAMIC_CLOSURE_PRIOR_ART.md`), and the classical common-ancestor tests (Steudel–Ay; Chaves et al. 2014). See new B7. |
| **B4** Poland disclosure | **PARTLY RESOLVED (by reframing)** | Poland is now called a *positive control*, and the top-triple E range is gone. But §5 is headed "pre-registered gates", and Poland's level violation (+4.95) was already seen in `GAUSSIAN_PAIRWISE_MODEL.md` before the validated test was declared. That test was in turn chosen after the 1047-triple family. One sentence is owed: "Poland was selected after it was seen; it is a positive control, not a confirmation". Non-blocking now that the framing is honest. |

---

### Pure Verdict: UNCLEAR (components OWNED; the assembly NOT FOUND; nearest econometric and ecological neighbours read only at snippet level)

The note, with its vocabulary stripped:
(i) Under latent sources that are independent as whole processes, each touching a set S ∈ H, with any per-site responses, the
population Spearman matrix lies in FW_H = {D + Σ_S C_S}. This is Kela et al. 2020 Prop. 1, owned.
(ii) A test of R ∈ FW_H: √n·V_H(R̂) against a block-bootstrap quantile of V_H(Z*). Its validity is proved by subadditivity plus owned
copula-bootstrap theorems, which is routine composition.
(iii) Two nested families of hypotheses: reach ≤ m (FW_m) and radius ≤ d (H(d)).
(iv) The same tests applied to VAR innovations.
(v) Frustration: antibalanced supports give FW₂ = PSD (Boman et al. 2005 L5 + T9, owned).

- **Cone, structural facts and closure: OWNED and correctly credited** (Kela; Boman; Agler et al.; Evans 2016; the trek rule;
  Lande et al. 1999; Ripa 2000).
- **The ecological question "how far does a common driver reach?": owned in substance, parametrically.** Ecology has the
  synchrony–distance function (Bjørnstad et al. 1999 [mem]), wavelet Moran attribution, synchrony networks (Walter 2017 [PDF, per
  `HYPERGRAPH_CENTRES_PRIOR_ART.md`]), and MARSS Q structures (Ward 2010). **Econometrics has a direct parametric analogue of "reach",
  not cited anywhere in the folder:**
  - factor strength and the exponent of cross-sectional dependence: a factor loading on ≍ N^α units; Bailey, Kapetanios & Pesaran,
    *J. Appl. Econometrics* 2016 [snip]; the residual version uses counts of non-zero pairwise correlations, with resampling bounds
    (2019) [snip];
  - weak vs strong factors (Chudik, Pesaran & Tosetti, *Econometrics J.* 2011 [mem]);
  - factors with spatial (local) correlation (Pesaran & Tosetti, *J. Econometrics* 2011 [mem]);
  - detection of pervasive units (Kapetanios, Pesaran & Reese [snip]);
  - block or multilevel dynamic factor models (Hallin & Liška 2011; Ando & Bai [mem]).

  - Approximate factor structure (Chamberlain–Rothschild 1983; Forni–Hallin–Lippi–Reichlin GDFM 2000) [mem]: common = divergent
    eigenvalues, idiosyncratic = bounded. This is the classical "pervasive vs local" split. FW_H differs: its blocks are not
    rank-limited and it is not eigenvalue-based. A local block of arbitrary rank is allowed, and a k-site factor is tested by
    membership, not by eigenvalue growth as N → ∞. With k = 10 fixed, the N → ∞ theory does not even apply.
  - **Spatial latent-factor models, the parametric owners of the *radius* question:** spatial dynamic factor analysis (Lopes, Salazar
    & Gamerman, *Bayesian Analysis* 3 (2008) 759–792 [snip]: dependence in time through factors, in space through loadings modelled
    as Gaussian random fields with a range parameter; Strickland et al. 2009 [snip]). In ecology, HMSC-type joint models carry
    spatially structured latent factors with an estimated range (Ovaskainen et al. [mem]; search did not surface it). A fitted range
    is the parametric counterpart of d̂.

  These answer "pervasive vs local common component" in linear, rank-limited models. The repo's object differs: inequality-only,
  PSD blocks of arbitrary rank, and validity under any nonlinear response. So this is **not a renaming**. But the question is owned,
  and a statistician referee will cite these papers.
- **Testing R ∈ FW_H as a calibrated statistical test, on real data: NOT FOUND.** The folder's scouts (Q4 in
  `HYPERGRAPH_CENTRES_PRIOR_ART.md`; `SOURCE_REACH_SCOUT.md` §3; `DYNAMIC_CLOSURE_PRIOR_ART.md` (b)) and this audit's searches found
  none. A search for "factor width" in statistics returned only factor-number tests and Drton-type finiteness results [snip].
  Neuroscience tests "higher-order synchrony beyond pairwise" with maximum entropy [snip]. That is a *different* notion: interaction
  order, not common-cause reach. The repo's own R-maxent region notes that pairwise maximum entropy always fits. Name it once so a
  reader does not conflate the two.
- **Why UNCLEAR, not NOVEL** (entry-level cap): the nearest neighbours were read only at snippet or memory level. These are
  Bailey–Kapetanios–Pesaran 2016/2019, Pesaran–Tosetti 2011, the MARSS Q-structure literature beyond Ward 2010's methods, and Chaves
  et al. 2014's real-data section. The v2 unread list (Bogdziewicz 2021 full text; forward citations of Kela 2020 and Gisin 2020)
  is also still unread.

---

### Validity checks (hostile check 1)

**V1. "Proved ... for every H" is overstated. The proof needs H to cover every pair (BLOCKING as wording; the applications are unaffected).**
- The domination and Lipschitz steps need V_H to be finite and 1-Lipschitz. That needs the dual set C_H = {X ∈ FW_H*, tr X = 1}
  to be compact. The bound |X_ij| ≤ √(X_ii X_jj) holds only for pairs {i,j} contained in some hyperedge (or in the 2-section of H).
- If a pair is uncovered, X_ij is unconstrained in the dual. Then V_H = +∞ at every R̂ with r̂_ij ≠ 0, which is almost surely. The
  test then rejects with probability → 1 even when R_ij = 0 holds exactly.
- **Numeric check [audit computation, `~/.claude/jobs/26482d7b/tmp/v1_uncovered.py`, cvxpy]:** take 3 sites, H = {01, 12}, and
  r̂₀₂ = 0.05.
  - The problem is **infeasible (V_H = ∞)**.
  - With H = pairs: V = −0.55.
  - With H = {01, 12} and r₀₂ = 0 exactly: V = −0.58.
  So the claim is ⟦hand + numeric⟧.
- So the statement is correct for **H whose 2-section is complete** (H ⊇ pairs, or every pair inside some hyperedge). That covers
  FW_m for m ≥ 2 and H(d) = pairs ∪ cliques, so every application is unaffected.
- `HYPERGRAPH_METHOD.md` already writes "FW_H ⊇ PSD diagonals" as the reason, but the reason that matters is pair coverage. The
  `REACH_TEST_VALIDITY_CHECK.md` "m ≥ 2" fix is the same point for FW_m.
- **Fix:** in §3, replace "every H" with "every H containing all pairs". In §2, add that a sparse hypothesis that leaves some pairs
  uncovered cannot be tested this way: it claims exact zeros, and those need a different (equality) test.

**V2. The procedure that is "proved" is not the procedure that is "validated" (BLOCKING as wording).**
- The proof (`REACH_TEST_SPEARMAN.md`; check doc) covers MBB without wrap, a **deterministic** block length l → ∞ with
  l = O(n^{1/2−ε}), **raw stationary levels**, and continuous margins with no sample ties (A2′), obtained by jitter.
- v3 §3 names the **Politis–White data-driven block length, clipped to [2, n/3]**, in the same sentence as "Proved". Bücher–Ruppert
  Thm 2 does not cover a random block length, and the n/3 cap is outside O(n^{1/2−ε}).
- The fixed n^{1/3} version that the proof does cover **fails size at a = 0.95** (0.55–0.60, `SPACE_TIME_DYNAMICS.md` run 2).
- So: proved means asymptotically valid with fixed blocks. Validated in finite samples means PW blocks on the tested worlds. The two
  are different procedures. This is honest in the source files and conflated in §3.
- **Not covered by the proof at all**, only by simulation:
  - the **innovation** tests (estimated VAR residuals; `SPEARMAN_PROOF_SOURCES.md` §2 says the residual-copula route is not provable
    from what was read);
  - the **detrended** variant (ibid. gap 3).

  Yet §4 and §5 rest the beech "within a year" reading and the salmon innovation null on the innovation test. That test was validated
  on 4 worlds (P2, M2, Lc, Rg), all linear VARs with independent shocks.
- **Fix:** split §3 into "proved (fixed blocks, raw levels)" and "validated by simulation (PW blocks; innovations; detrended)", each
  with its own scope.

**V3. Segers' condition and mixing in the applications (NON-BLOCKING; scope note).**
- Jitter at σ = 10⁻³ × the smallest gap makes the copula formally continuous and smooth. Segers' condition then holds formally, but
  the copula is close to a step function. The asymptotic approximation at n = 47–53 rests on the simulations, not the theorem.
- Masting is a threshold and resource-budget mechanism, which is exactly where the check doc says Segers' condition fails. The only
  evidence of robustness is one min-world (`ASSUMPTION_BREAKERS.md` N: size 0.00).
- Salmon: the 4–5-year cohort cycles (e.g. Kvichak) are strong periodic dependence. Geometric mixing is plausible, but the effective
  n is smaller than 47.
- **Fix:** §3 should call Segers' condition "unverifiable for the applications; robustness shown on one singular world".

**V4. Other scope slips (NON-BLOCKING).**
- §1: "No arrangement of independent pairwise causes does better" is true only **at uniform margins** (each pond occupied half the
  years). That is the taxonomy's own R-nsi-consensus scope. Ponds that are always empty agree 100% of the time with no causes at all.
  Add "with each pond occupied half the years".
- §2: the bound sec(π/L) − 1 is proved for equal weights. The supremum over unequal weights is numerical (⟦HAND-numeric⟧ in the
  prior-art file).
- §3: the "Validated" bullet says size ≤ 0.06, but the regime-shift detrended cell is 0.09 > 0.07 (the bar). It is listed under
  failure modes, so it is consistent. Say "size ≤ 0.06 on stationary worlds".
- **The validation grid is mostly linear-Gaussian**, and the worlds are not shown to be least favourable. That is stated in
  `VG_TEST_VALIDATION.md` run 3 but not in v3.

---

### Applications (hostile check 4)

**Polish beech: honest within what was tested, with three corrections.**
- **Checked against the files:**
  - T 35 vs 9;
  - reach ≥ 4 (20/20 jitter draws);
  - d̂ = 397 km (H(368) rejected 5/5);
  - innovations reproduce m̂* = 4 and d̂;
  - circular-shift negative control 0.00;
  - cue special vs placebo (p < 0.005) with ~10% reduction;
  - failed prediction (i) recorded in the file.
- (a) The positive-control attribution (cue vs placebo, ~10%) ran on the **older pipeline**: normal scores, detrended, fixed n^{1/3}
  blocks. The §3 recipe was never re-run, and `SPACE_TIME_DYNAMICS.md` calls that re-run "a consistency check" not done. Say so, or
  re-run it.
- (b) "The same in innovations ⇒ a region-wide cause acting within a year". Two owned caveats from `DYNAMIC_CLOSURE_PRIOR_ART.md`
  appear in §4 only partly. Observation error, and a misspecified linear two-neighbour VAR, both bias *toward* finding a centre, and
  beech dynamics are nonlinear. Add both to §7, and mark the innovation reading as simulation-validated only (V2).
- (c) Poland was selected after being seen (B4 residue).

**Bristol Bay sockeye: mostly within what was tested; one overstatement and one specific confound.**
- **Checked:**
  - T 16.2 vs 10.2, robust to detrending and to the 1977 step;
  - reach ≤ 3 not rejected;
  - radius 98 km rejected, 128 km not;
  - innovations null;
  - PDO drop not special (18.5% of placebos);
  - failed predictions (m̂* ≥ 4, d̂ high, innovations reject) recorded in `SALMON_FLOW.md`.
- "**No across-year river interaction (0/9)**" overstates a null. These are per-river F-tests at n ≈ 46 with no power analysis.
  Write "no evidence of across-year interaction (0/9 after Holm; power not assessed)".
- **The protocol confound has a specific, testable form, which the note does not name** [snip: 5 AAC 06.355 allocates catch by
  district; KDLG reports split the catch by district, Naknek–Kvichak (Naknek and Kvichak set-net sections) and Nushagak (Nushagak and
  Igushik set-net sections, with Wood reported alongside). Alagnak's district membership and the run-reconstruction apportionment
  method are mem, so check them in the ADF&G run-reconstruction reports.] Bristol Bay catch is assigned to rivers *within fishing
  districts*: Naknek–Kvichak (Naknek, Kvichak, Alagnak) and Nushagak (Wood, Igushik, Nushagak). Run reconstruction then shares apportionment error among geographically close rivers. That builds local
  triple-level "centres" of roughly the 100–130 km scale the radius test found. Harvest management (escapement goals) is also shared,
  and it acts on S_t, which enters the Ricker residual.
  - **Suggested probe:** test whether the sub-regional centre is carried by within-district triples. Run H = pairs ∪ district
    cliques, and compare cross-district triples alone.
  - Until that probe is run, §5's "an unidentified local shared driver, or the protocol" should name district apportionment as the
    leading protocol candidate.

**Zooplankton: one overstatement.**
- "Only Trout Lake needs a **community-wide** centre" is wrong. A V_G rejection shows a common cause of **≥ 3 species**, not a
  community-wide one. Reach and radius were not tested there.
- The result is also 1 rejection out of 5 lakes × 2 variants at α = 0.05, with no multiplicity control (T 9.8 vs 8.4; detrended
  10.2 vs 9.6). Say "Trout Lake: a centre of ≥ 3 of the 8 species, unadjusted across lakes".
- The median 79% frustrated and the Crystal Lake guild reading check out (CR: 43% negative pairs, 0 antibalanced triangles).

**North Pacific n = 28 (weak null): honest.**

**Pre-registration discipline overall:** exemplary in the files. Every application file records its failed predictions. v3's §5
header "failed predictions recorded" is accurate as a pointer, but v3 itself lists none. Add a one-line count, e.g. "beech 1/3,
salmon flow 3/6 and ocean driver 1/2 failed; zooplankton 3/3 failed". The note's honesty should not depend on the reader opening
the gate files.

---

### Applied Verdict: CONDITIONAL (programme bar not yet met: no head-to-head comparison)

1. **Decision test.** Improved over v2. The reach and radius tests answer a question practitioners do ask: what is the spatial
   extent of the shared driver, and is it one regional cause or a patchwork of local ones? The innovation split answers "same-year
   shock vs carried-over history". The niche is real.
2. **Computational comparison: still none** (check 2). v3 cites MARSS only for the innovation idea. It compares against none of
   matrix regression / partial Mantel, wavelet Moran, MARSS Q-structure selection, dynamic factor analysis (Zuur et al. 2003 [mem];
   the MARSS DFA module), synchrony–distance (`ncf`), or factor-strength estimation. "No comparison = no paper" still applies.
3. **Regime boundaries: now sharp, and a strength.**
   - Power curves: reach 10, λ² ≳ 0.2–0.3 at n ≈ 50; reach 3 is invisible.
   - Persistence threshold for a centre in time (a ≳ 0.9).
   - Regime-shift failure (0.50 → 0.09).
   - Only ε = ∞ is valid.
   - The frustration criterion for which networks can reveal a centre at all.
4. **Non-obvious insight:**
   - the frustration/antibalance criterion read ecologically: competition scattered across pairs can hide a shared driver at the
     correlation level, while guild-structured competition does not (Crystal Lake);
   - "beech regionality is a same-time cause, not accumulated history";
   - "dispersal-only coordination breaks the pairwise ceiling only near instability". The last is owned (Ripa 2000; Lande et al.
     1999), and v3 credits it.
5. **Reproducibility:** good (scripts in `../verification/`, public data, seeds).

**Practitioner hostility test.** "I fit MARSS with block-structured or unconstrained Q and compare by AIC, or I run DFA and read the
loadings. That tells me whether there is a shared regional trend and which sites load on it. Why use yours?" The answer v3 could give
is that it makes a *necessity* statement ("a centre at least this wide is required") that stays valid under arbitrary nonlinear
responses, where MARSS and DFA assume linear Gaussian dynamics and choose among a finite list. That answer is **plausible but
undemonstrated**. If MARSS and DFA give the same conclusions on Poland and Bristol Bay, and do not mis-size on nonlinear pairwise-only
worlds, the advantage reduces to "model-free" at a large power cost.

---

### Contribution Type Verdicts (mode = full)

**Type 7 (methodology): FAIL at the programme bar, now one step from CONDITIONAL.**
- Bar: a demonstrated advantage on concrete problems, sharp regimes, and a non-obvious consequence confirmed numerically.
- Regimes are sharp, and validity is now well supported (V1/V2 are wording fixes).
- What is missing is the advantage. The **comparison needed** (B6) has two parts.
  - **Synthetic head-to-head**, on worlds with known truth:
    - (W-a) pairwise-only sources with nonlinear threshold responses at the FW₂ boundary (null);
    - (W-b) local triple centres on a ring (polycentric, H(2));
    - (W-c) one regional factor (monocentric);
    - (W-d) local shocks plus dispersal at a = 0.95 (centre in time).

    Competitors:
    - MARSS with Q ∈ {diagonal, banded/local-block, equal-covariance, unconstrained} by AIC;
    - DFA with the number of trends by AIC and loading-pattern reading;
    - synchrony–distance via `ncf`, as a proxy for the radius;
    - a spatial dynamic factor model (Lopes–Salazar–Gamerman), whose fitted loading range is the parametric counterpart of d̂;
    - optionally the Bailey–Kapetanios–Pesaran α̂ as a proxy for reach.

    Metrics: the false "regional centre" rate on W-a and W-b; the power to identify regional vs local; the false "centre in time"
    rate. **The advantage claim survives only if the competitors mis-size on W-a or confuse W-b with W-c, and the cone tests do not.**
  - **Real-data concordance:** MARSS-Q and DFA on Poland and Bristol Bay, reported next to m̂* and d̂.

**Type 6 (exposition/translation): CONDITIONAL (content clears; the expository piece does not yet exist).**
- (a) Audience: spatial and population ecologists, met.
- (b) Inaccessible literature: the Kela et al. covariance cone (IEEE TIT), Boman's factor width (LAA), network nonlocality (Gisin,
  *Nat. Commun.*), and copula-bootstrap theory (Bücher–Ruppert, Bücher–Volgushev). Met.
- (c) Non-trivial conceptual work: now **done, in the folder**:
  - why per-site transforms and whole-process sources keep the null;
  - why a calendar trend or step acts as a centre;
  - the frustration criterion for which networks can show a centre;
  - the levels = interaction-closure of the shocks reading, with its truncated bound;
  - the within-interval caveat;
  - the honest power map.
- But v3 is explicitly "raw material ... not for circulation". It is a telegraphic summary that assumes the reader knows FW_H,
  Segers' condition and Hong–Li ε. Clears once written as an exposition for ecologists that carries those six points with the puzzle.

**Type 3 (unifying framework): UNCLEAR.**
- **Transfer exists in form.** A physics and linear-algebra object (the Kela/Boman cone over a hypergraph) becomes a calibrated test
  in ecology. It yields statements ecology tools do not state as such:
  - (1) "a positively correlated synchrony network can reveal a centre beyond pairs, from correlations, only through odd/frustrated
    cycles; an even ring of truly uncorrelated non-neighbours cannot, however strong";
  - (2) a model-free *lower bound* on driver reach and radius;
  - (3) Polish beech needs a same-year cause binding stands > ~370 km apart.
- **Not a renaming of factor models.** FW_H allows PSD blocks of arbitrary rank and is inequality-only. Rank-limited DFM/MARSS
  models and factor-strength exponents are special or parametric cases, so the hypotheses differ, as the tetrad/one-factor point
  did in v2.
- **But the bar asks for something B could not reach otherwise.** (2) and (3) are untested against parametric routes that may reach
  the same conclusions (B6). Statement (1) is a corollary of owned results (Boman + Harary), and its ecological consequence has not
  been checked against what DFA or MARSS would conclude on such networks. The econometric owners of the "pervasive vs local factor"
  question are uncredited and unread (B7).
- Re-evaluate after B6. If one synthetic world shows the parametric tools wrong where the cone test is right, this clears.

**Implicit Types 1, 4: not claimed.** §6 correctly says "not new theorems".

### Cross-reference
- Since v2 the instrument is more valid, better scoped, and answers a better question. It moved from the "pairwise-only drivers?"
  null to reach, radius and space/time, with failure modes and power mapped.
- The remaining gap is the same shape as v2's: **novel where untested against the incumbents.** In v2 the step that would have
  helped ecologists was invalid. In v3 the useful steps are valid but not compared with MARSS, DFA and wavelet Moran, which address
  the same practical question parametrically.
- Type 6 is the nearest route to clearing; Types 7 and 3 both wait on the one comparison (B6).

### Recommendation
- **Programme: do not park. Proceed only after B5–B8.** B6 (one head-to-head comparison) is the single item that moves Types 7 and 3.
- **The realistic product is a Type 6 methods-exposition** for ecologists: the puzzle, then the cone, frustration, the validated
  recipe and its power map, with Poland as the positive control.
- Unread sources that could change the pure verdict:
  - Bailey–Kapetanios–Pesaran 2016 (*JAE*) and 2019 (residuals);
  - Pesaran–Tosetti 2011;
  - Hallin–Liška 2011;
  - Ward et al. 2010 beyond methods, and the MARSS Q-structure synchrony literature;
  - Chaves et al. 2014 §real data;
  - Bogdziewicz et al. 2021 full text;
  - forward citations of Kela et al. 2020.

---

### Referee estimate: BORDERLINE
Venue class: research journal, methods track (*Methods in Ecology and Evolution*; *Ecology* Statistical Reports; *Ecography* methods),
or short-note.
Value carried by: factor 3 (a framework that yields new usable statements and a tool) plus factor 4 (translation of the Kela/Boman
cone into ecology).
Main risk a referee would raise: "No comparison with MARSS Q-structure selection or dynamic factor analysis, which already ask
whether synchrony is regional or local. The test is so conservative that only very strong, wide centres are detectable at n ≈ 50.
The 'proved' procedure is not the one used (data-driven blocks; innovations)."
Cap check: pure is UNCLEAR, so the estimate is capped at BORDERLINE. The BORDERLINE is **not cap-only**. Even with the econometric
neighbours read, the missing comparison (B6) would hold a methods referee at BORDERLINE. No uncredited owner of the *main result*
(the calibrated FW_H test) was found, so REJECT-LIKELY does not apply. The uncredited econometric work owns the question, not the
test.

---

## Required fixes (exact locations in the target note)

**Blocking**
- **B5 (§3 "Proved" bullet):** (i) "every H" → "every H whose hyperedges cover all pairs (H ⊇ pairs)", with the reason (V1).
  (ii) Separate the proved procedure (fixed block length l = O(n^{1/2−ε}), raw stationary levels, jittered continuous margins with no
  sample ties) from the validated one (Politis–White blocks clipped to n/3; innovations; detrended). State that innovation and
  detrended tests are simulation-validated only, on linear-VAR worlds (V2).
- **B6 (§3 or a new §3b; affects §6 "Ours"):** one pre-registered head-to-head comparison against MARSS Q-structure AIC and DFA, plus
  `ncf` (and optionally the factor-strength α̂). Use synthetic worlds W-a…W-d and Poland plus Bristol Bay, as specified under Type 7.
  Until it is run, §6 must not imply an advantage over ecology's tools.
- **B7 (§4 and §6):** credit, by name, the existing tools for the same questions:
  - matrix regression / partial Mantel;
  - wavelet Moran (Sheppard 2016; Walter 2017);
  - the synchrony–distance function (Bjørnstad et al. 1999);
  - MARSS Q structures (Ward et al. 2010) and DFA;
  - classical common-ancestor tests (Steudel–Ay; Chaves et al. 2014);
  - econometric factor strength and local vs pervasive dependence (Bailey–Kapetanios–Pesaran 2016; Chudik–Pesaran–Tosetti 2011;
    Pesaran–Tosetti 2011).

  - approximate factor structure (Chamberlain–Rothschild; Forni–Hallin–Lippi–Reichlin), with one line on why FW_H differs;
  - spatial dynamic factor models (Lopes–Salazar–Gamerman 2008) and spatial latent factors in joint species models (HMSC).

  This completes v2 B3.
- **B8 (§5 beech, "the known cue is special against placebo"):** qualify it as "special against an unmatched time-permutation placebo,
  which is biased in the cue's favour". Alternatively, re-run against an R²-matched surrogate (a phase-randomised cue that keeps its
  autocorrelation and cross-site correlation) and report that instead. This completes v2 B2. The PDO "not special" verdict needs no
  change.

**Non-blocking**
- N1 (§1): add "with each pond occupied half the years" (uniform-margin scope of the 56% ceiling).
- N2 (§2): sec(π/L) − 1 is the proved value for equal weights; the unequal-weight supremum is numerical.
- N3 (§3): Segers' condition is unverifiable for threshold mechanisms such as masting, with one-world robustness evidence. Say the
  validation grid is mostly linear-Gaussian and not shown to be least favourable. "Size ≤ 0.06 on stationary worlds."
- N4 (§5 beech): the cue-vs-placebo attribution ran on the old pipeline (normal scores, fixed blocks); re-run it, or say so. Add
  observation error and restricted-VAR misspecification (both bias toward a centre) to §7. Add "Poland was selected after it was
  seen" (B4 residue).
- N5 (§5 salmon): "no across-year river interaction" → "no evidence (0/9 after Holm; power not assessed)". Name district catch
  apportionment and shared escapement management as the specific protocol candidates ⟦mem: verify⟧, and consider the
  within-district vs cross-district probe.
- N6 (§5 zooplankton): "community-wide centre" → "a centre of ≥ 3 of the 8 species"; note there is no multiplicity control across
  5 lakes × 2 variants.
- N7 (§5 header): list the failed-prediction count per application inline.
- N8 (placebos, general): for any future named-driver comparison, make the R²-matched surrogate placebo the default. The beech case
  is blocking (B8).
- N9 (hygiene): `README.md` still calls the target "working note v2" and the audit "of note v1; re-audit of v2 owed". Update it, and
  link this file.
- N10 (§2, one line): distinguish "centre" (common-cause reach) from the neuroscience and complex-systems "higher-order interaction"
  notions (pairwise maximum entropy; O-information) so a reader does not conflate them.

## Sources consulted
- **Primary, read:** the target v3; v2 audit; `README.md`; `REACH_TEST_VALIDITY(.md, _CHECK)`; `REACH_TEST_SPEARMAN(.md, _CHECK)`;
  `SPEARMAN_PROOF_SOURCES.md`; `VG_TEST_VALIDATION.md`; `FINITE_EPS_REVALIDATION.md`; `ASSUMPTION_BREAKERS.md`; `POWER_CURVES.md`;
  `HYPERGRAPH_CENTRES(.md, _PRIOR_ART)`; `HYPERGRAPH_METHOD.md`; `DYNAMIC_CLOSURE(.md, _PRIOR_ART)`; `SPACE_TIME_DYNAMICS.md`;
  `BEECH_POSITIVE_CONTROL.md`; `SALMON_FLOW.md`; `SALMON_OCEAN_DRIVER.md`; `FRUSTRATION_ZOOPLANKTON.md`; `SOURCE_REACH_SCOUT.md`;
  the taxonomy `owned_regions`.
- **Web, snippet level:**
  - Bailey–Kapetanios–Pesaran (exponent of cross-sectional dependence; econpapers / Cambridge CWPE 1206; residuals version 2019);
  - Kapetanios–Pesaran–Reese (pervasive units, AEA 2020 preliminary);
  - factor-number tests (arXiv:2306.14004); Drton et al. finiteness of small factor models (arXiv:0908.1736);
  - MARSS synchrony application (USGS amber darter);
  - Reuman et al. 2023 (interacting drivers, *Ecography*);
  - neuroscience higher-order synchrony via maximum entropy (PMC3915758).
- **From memory, unchecked:** Chudik–Pesaran–Tosetti 2011; Pesaran–Tosetti 2011; Hallin–Liška 2011; Ando–Bai; Zuur et al. 2003 DFA;
  Bristol Bay fishing-district structure.
