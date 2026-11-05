# Audit: SYNCHRONY_CAUSALITY_METHOD.md (mode: full, skill v2.1)

reviewed: false. 2026-11-05. Auditor: opus agent running `/audit full`. The target note was not edited.
Numbers marked **[audit computation]** come from this audit's own scripts (Appendix A). They are not pre-registered and are
diagnostics only.

## Audit: `notes/open_questions/views_across_records/SYNCHRONY_CAUSALITY_METHOD.md` (mode: full)

### Declared contribution type(s): 7 (methodology), 6 (exposition/translation)
Types are declared in the header. The note does not state the per-type bars it commits to. The note implicitly also claims
Type 3 (method transfer from network nonlocality into ecology) and touches Type 1 (the ceiling statement) and Type 4 (the
"centre in space / centre in time" vocabulary). All are assessed below.

**Bearing on WHY.md:** this is the most direct bridge the programme has to the question "order without a centre?" in ecology. It
asks whether local, pairwise relations can produce the observed coordination, or whether a centre is required. It answers only the
coarse half ("a centre exists"). It cannot yet say *which* centre, and the step meant to do that (step 2) does not work as written.

---

### Pure Verdict: UNCLEAR (components KNOWN; the ecological application NOT FOUND; three sources unread)

What the method actually states, with the vocabulary stripped:
(i) Binarise three series at their medians. If the joint law of the three binary variables is triangle-network compatible (three
independent bipartite sources, local responses), then the NSI inequality (Gisin et al. 2020 eq. 13 for uniform margins, eq. 16 in
general) holds. A violation therefore rejects "no common ancestor of all three".
(ii) Residualise on a candidate driver and re-test.
(iii) Read the residual through lags.

- **(i) The bound: KNOWN.** Gisin et al. 2020, *Nat. Commun.* 11:2378, eqs. 13–16, read for this audit from the shelved PDF
  (`pdftotext`). Eq. 13 is stated for E_A = E_B = E_C = 0 ("and its symmetries under relabeling of the parties and of the
  outputs"). The note's |E_k| form is the correct closure under output relabeling. The symmetric threshold E₂ ≤ √2 − 1 is stated
  verbatim. The consensus value (3√2 − 2)/4 follows by Cauchy–Schwarz; it is attained by the AND model (da Silva–Pozas-Kerstjens–Parisio
  2025, App. E, already OWNED in `seam_A_scout.md` addendum). The worked case in §1 checks out: P(frogs) = (1/√2)² = ½;
  P(all empty) = P(≥ 2 of 3 streams bad) = 3q²(1−q) + q³ = 0.2071 with q = 1 − 1/√2; total 0.5607.
- **(i) as a classical causal-inference test: KNOWN in statistics/ML.** Steudel–Ay (Entropy 2015, arXiv:1010.5720) is the
  information-theoretic common-ancestor test. Chaves, Luft, Maciel, Gross, Janzing & Schölkopf, "Inferring latent structures via
  information inequalities" (UAI 2014, arXiv:1407.2256) [abstract/snippet]: entropic tests that three correlated variables cannot come
  from pairwise common ancestors, with the triangle as a worked example. Wolfe–Spekkens–Fritz inflation (J. Causal Inference 2019).
  A referee will say the classical, model-free "does this need a common ancestor of all three" test exists in the causal-discovery
  literature. What is new is only its use on ecological synchrony and the binarised NSI form.
- **Not a tetrad test renamed.** With three observed variables a one-factor model is saturated (no vanishing tetrad exists; tetrads need
  ≥ 4 indicators: Silva et al. JMLR 2006; Kummerfeld–Ramsey FOFC). Tetrads test "exactly one factor". The triangle bound tests "no
  factor shared by all three". The hypotheses differ, so this is not a renaming. The note should say this, because a statistician
  referee will ask.
- **Parametric analogue a referee will raise.** ⟦HAND⟧ In a linear-Gaussian model with pair-specific factors,
  X_A = a₁S_AB + a₂S_AC + e_A with unit variance gives ρ_AB = a₁b₁. In the symmetric case this forces ρ ≤ ½. A linear "pairwise-factors"
  check therefore exists and is elementary. The model-free version earns its place only because it allows **arbitrary nonlinear
  responses and non-Gaussian drivers**. That is the selling point, and the note does not state it.
- **(ii) Condition on a named centre: KNOWN in substance in ecology.** Synchrony explained by a measured driver is standard:
  - matrix regression / partial Mantel on synchrony matrices (Bogdziewicz et al. 2021, *Ecology*, European beech [snippet]: "proximity
    played no apparent role ... after controlling for synchrony in environmental variation"; weather synchrony explains masting
    synchrony up to ~1500 km);
  - the wavelet Moran theorem and the "synchrony explained by driver" decomposition (Sheppard et al. 2016 *Nat. Clim. Change*;
    Walter et al. 2017; `wsyn`);
  - Vacchiano et al. 2017 *New Phytol.* and Ascoli et al. 2017 *Nat. Commun.* on beech weather cues and continental synchronisation
    (from memory, unread).
  The note lists this step as **new** in §6. It is not.
- **(iii) Space versus time via lags: KNOWN / folklore.** Lagged cross-correlation to separate dispersal from Moran is textbook
  (Bjørnstad, Ims & Lambin 1999 *TREE*; Ranta et al.). `seam_A_scout.md` (c) already records "centre in time" as immediate from unrolling,
  "high risk of being obvious". The note lists it as **new** in §6. It is not.
- **(i) applied to ecological synchrony: NOT FOUND.** Two scouts (`seam_A_scout.md` (d)/(e); `ecology_owner_scout_DEEP.md`) and this
  audit's searches found no network-nonlocality, inflation or entropic common-ancestor test applied to ecology, and no ecology paper with
  a three-site statistic excluding pairwise-only drivers. The network-nonlocality papers searched mention no ecological or
  classical-synchrony application.
- **Why UNCLEAR rather than NOVEL** (entry-level cap):
  - the nearest ecology neighbour, Bogdziewicz et al. 2021, was read only at snippet level;
  - Chaves et al. 2014 (does it apply the triangle test to real data?) was read only at abstract level;
  - forward citations of Steudel–Ay, Gisin 2020 and Wolfe–Spekkens–Fritz were not traversed.

  The citation in §6 to Goldstein et al. 2026 (J. Anim. Ecol.) is **misapplied**. That paper is about concordance between data sources
  for one species (integrated SDMs). It is not about synchrony or common causes, so it cannot support "ecology lacks model-free
  synchrony tests".

---

### Validity defects (hostile checks 1, 2 and 4)

**V1. Stationarity is required, and the note never states it (BLOCKING).**
- **Within-site autocorrelation is fine, and the note should say so.** Take each "source" to be a whole driver trajectory. Each site's
  history is then a function of its two pairwise source trajectories plus local noise, including feedback from its own past. So for every
  fixed year t, the law of (X_A,t, X_B,t, X_C,t) is triangle-compatible. Per-site median thresholds are fine for the same reason: each
  depends only on that site's own series, so the binarisation is a local post-processing step.
- **Pooling years is not fine without stationarity.** The empirical E's estimate the *year-averaged* law, which is a mixture of per-year
  laws. The triangle-compatible set is **not convex** (well known; Fritz 2012; Gisin 2020 intro). The eq. 13 region is a second-order
  cone and is convex at fixed uniform margins. Under nonstationarity the per-year margins move, however, and a mixture of compatible laws
  can violate. The year index then acts as a shared variable.
- **Demonstration [audit computation]:** a stationary boundary model (AND of AR(1) Gaussian pair-sources, population V = 0) was compared
  with the same model plus one common linear time trend added to each of the three independent pair-sources.
  - Stationary, n = 72: rejections at α = 0.05 were **0.3% (φ = 0) and 0.7% (φ = 0.5)**.
  - With the trend: **61%** rejections, mean point V = +1.93.
- **Correct reading:** a violation implies a common ancestor *where a shared trend, regime shift or protocol drift counts as one*. The
  bound is not wrong; the calendar is a common cause. But an ecologist will read "common ancestor" as a regional driver, so the pipeline
  needs an explicit detrend or stationarity step before step 1.
- **The Poland case survives:** linear detrending *raises* V from 2.97 to 4.50. This is a scope fix, not a kill of the worked case.

**V2. Step 2 ("condition by OLS residualisation") is not conditioning, and its one demonstration fails a placebo (BLOCKING).**
- **Not conditioning.** Under H₀ "the only common cause is the cue", X_A = f(ΔT_A, S_AB, S_AC, noise). The residual X_A − b̂ΔT_A is free
  of the cue only if f is additive and linear in ΔT. Masting cues are threshold-like, so residuals keep cue dependence, and a persisting
  violation is uninterpretable. A *vanishing* violation is a non-violation. By the note's own §2 rule, "no violation ⇒ nothing", so
  §3 step 2's "the candidate accounts for the common cause, as far as the data can show" contradicts §2.
- **The bootstrap ignores the generated regressor.** b̂ is fitted once and not re-estimated inside resamples (`mast_conditional_gate.py`
  `resid` called outside `boot_lb`). This is minor at two parameters per site.
- **Placebo [audit computation], Poland 008-009-010, n = 72, raw V = 2.97, residual on real ΔT = 1.27:**
  - residualise on ΔT with the years permuted, using one permutation for all three sites (this keeps ΔT's 0.90–0.97 cross-site
    correlation): median V = 1.83, and **17%** of 2000 placebos give V ≤ 1.27;
  - independent permutation per site: median V = 0.92, and **67%** give V ≤ 1.27;
  - this placebo is *conservative in ΔT's favour*: permuted ΔT has R² ≈ 1/n ≈ 0.014, against 0.05–0.09 for the real cue. A placebo
    matched on R² would probably cut V further.
- **Corroborating sensitivity [audit computation / gate file]:**
  - rank-residualisation on ΔT gives V = 0.93; the two-regressor version gives 0.93 (gate file);
  - genuine stratification by regional ΔT tercile (n = 24 each) gives V = −0.94, **+2.45**, −0.22 (the middle stratum still violates
    at point level);
  - in Germany, conditioning *raised* V (0.35 → 0.66).
- **Conclusion:** linear residualisation followed by a median split moves V by amounts no larger than a meaningless regressor does.
  The §4 sentences "removes most of what the sites share" and "A weak signal every stand hears is what a centre looks like" are
  **unsupported**. The gate file's own reading ("no longer demonstrable at n = 72") was correct. The note's summary drifted stronger.

**V3. Bootstrap inference for V > 0: plausibly conservative at one boundary point, unproven elsewhere (NON-BLOCKING for a draft;
blocking for a methods paper).**
- V is a max over three pairs and four relabelings of functions of |E_i|. It is non-differentiable on the null boundary, and the
  percentile block bootstrap is not generally consistent there (Andrews 2000; Fang–Santos 2019).
- The size simulation above covers **one** boundary point, the symmetric AND model. There the test is very conservative, because
  median-split V̂ is biased downward (mean point V −0.23 to −0.51 at V = 0). No guarantee follows for asymmetric boundary points or
  heavy-tailed / ordinal margins.
- Block length 3 is unjustified. Beech masting has strong negative lag-1 autocorrelation (resource depletion).
- The circular wrap in the block bootstrap (`% n`) joins 2022 to 1951.
- Required: a size and power simulation over a grid of boundary models (asymmetric E, AR φ ∈ {−0.5, 0, 0.5}, n ∈ {45, 72}), and a
  stated block-length rule.

**V4. Eq. 13 used with non-uniform margins (NON-BLOCKING).** The lake script uses the uniform-margin form (13). With odd n or ties,
margins are not exactly ½. Use eq. 16 everywhere, as the mast scripts already do. The lake violations are far from the boundary, so
nothing flips.

**V5. NSI rather than classical bounds (NON-BLOCKING, power).** Ecology is classical. The "any physics" generality buys nothing there,
and the classical triangle-local set is strictly smaller than the NSI set away from the symmetric AND point. Classical inflation or
entropic bounds (Wolfe et al.; Chaves et al.) could reject more. They should be compared, not just cited.

**Honesty of reporting (check 4).**
- The gates are exemplary:
  - pre-registered before the data;
  - failed predictions recorded (MAST_CEILING far triples; conditional "persists"; pooled "residual");
  - the Holm-resolution design flaw recorded and not patched;
  - the Poland stage-1 value disclosed as already seen;
  - the circular-shift error corrected in place.
- The **note's §4 is less honest than its gates**:
  - (a) Poland p = 0.008 is shown without saying it was seen first in a 1047-triple family where nothing survived Holm, and that
    stage 1 is therefore a replication, not a confirmation;
  - (b) "within regional programmes synchrony is strong (E 0.7–0.86)" gives the *top* triples. The median same-study mean-E was 0.37;
  - (c) the drift in the conditioning claim (V2).
- §5 is internally inconsistent: rule 3 recommends "a pooled statistic (mean V over triples)", and rule 5 says "don't pool by averaging".

---

### Applied Verdict: FAIL (programme bar)

1. **Decision test.**
   - Ecologists' live question is Moran vs dispersal, plus *which* driver. The test answers a different question, "pairwise-only
     drivers?". No ecologist holds that null for regional synchrony, and dispersal plus feedback itself creates common ancestors.
   - Step 1 therefore changes no practitioner decision. Step 2, which would, is invalid as written (V2). Step 3 is standard lag
     analysis.
   - The one honest niche is the *spatial extent of a driver*: does anything span all three sites, beyond overlapping pairwise
     neighbourhoods, under arbitrary nonlinear response? That niche is real but untested against the standard tool for it, Bjørnstad's
     nonparametric spatial covariance function (`ncf`).
2. **Computational comparison.** There is none against matrix regression / partial Mantel, wavelet Moran (`wsyn`), the linear-Gaussian
   ρ ≤ ½ analogue, or entropic/inflation triangle tests. "No comparison = no paper."
3. **Regime boundaries.** Partly sharp: the E > √2 − 1 bite threshold is correct and useful. The design rules about bootstrap resolution
   are standard multiple-testing arithmetic.
4. **Non-obvious insight.**
   - The demonstrated results are a positive control (lake temperature, which is shared weather) and nulls (zooplankton, cross-study
     beech, pooled Poland).
   - The one candidate insight, "a weak cue removes the common part", fails the placebo.
   - The zooplankton result restates known low temporal coherence.
5. **Reproducibility.** Good: scripts, seeds and public data (NTL-LTER, MASTREE+ V2, ERA5 via Open-Meteo).

**Practitioner hostility test.** "I already regress synchrony on environmental synchrony (MRM / wavelet Moran) and get Moran vs
dispersal directly. Why use yours?" The note's only answer is that it is model-free. That answer holds for step 1, which answers a
question practitioners don't ask. It does not hold for step 2, which is linear and is the step that would matter.

---

### Contribution Type Verdicts (mode = full)

**Type 7 (methodology): FAIL.** Bar: demonstrated advantage on concrete problems; sharp regimes; non-obvious consequence confirmed
numerically.
- No advantage was demonstrated against any standard method.
- The distinctive inferential step (2) fails a placebo control (V2).
- Stationarity is not stated (V1).
- Size is checked at one point only (V3).
- Path to CONDITIONAL: fixes B1–B4 below plus one head-to-head comparison.

**Type 6 (exposition/translation): CONDITIONAL / UNCLEAR.**
- (a) Audience: population and spatial ecologists. Met.
- (b) Inaccessible literature: network-nonlocality NSI bounds and inflation (physics, *Nat. Commun.*, *PRL*, J. Causal Inference). Met
  for ecologists, although Steudel–Ay and Chaves et al. are already pitched at statisticians.
- (c) Non-trivial conceptual work: the work *needed* is non-trivial, but the note does not yet do it:
  - why per-year compatibility holds under autocorrelation (trajectory-level sources);
  - why per-site median splits are admissible local post-processing;
  - why pooling across years needs stationarity (non-convexity);
  - what "conditioning" must mean (stratification, or an additive model stated as an assumption).

  As written, the translation is close to "here is the inequality; apply it to medians". With those four points added, (c) would clear.

**Type 3 (unifying framework, implicit): UNCLEAR.** A technique from domain A (network nonlocality) does become *computable* in domain B
(ecology), which is method transfer in form. The bar asks that the transfer yield something B can use. Step 1 yields only a conclusion B
already accepts, and step 2 is not valid. Re-evaluate after the fixes, with one result that standard ecology tools could not reach
(e.g. a nonlinear case where MRM and the Gaussian ρ ≤ ½ check both fail to reject and the binarised bound does).

**Type 1 (new theorem, implicit in §1–§2): FAIL (KNOWN).** Gisin et al. 2020 eqs. 13–16; da Silva–Pozas-Kerstjens–Parisio 2025 App. E.
The note credits these correctly.

**Type 4 (vocabulary, implicit: "centre in space / centre in time"): FAIL.** No three new statements. "Centre in time" is unrolling of
feedback (Bongers et al. 2021 *AoS*; folklore per `seam_A_scout.md`), and "centre in space" is the Moran effect.

**Type 2, Type 5:** not claimed, not applicable.

### Cross-reference
- The components are known: the bound (physics), common-ancestor testing (causal ML), conditioning on drivers and lag analysis
  (ecology). The assembly is novel only at step 1 (NOT FOUND in ecology).
- The one step that would make the assembly useful to ecologists (named-centre conditioning) is both owned in substance (MRM / wavelet
  Moran) and invalid in this implementation.
- So: novel where it isn't useful, useful where it isn't novel. Type 6 is the realistic route, provided the validity conditions become
  the content of the translation.

### Recommendation
- **For the programme: redirect to an expository / short methods note (Type 6). Do not share as a methods contribution (Type 7) until
  B1–B4 are fixed.**
- Do not park the instrument: step 1 is sound under stationarity, and the zooplankton nulls and the bite threshold are honest, usable
  facts.
- Unread sources that could change the pure verdict:
  - Bogdziewicz et al. 2021 *Ecology*, full text;
  - Chaves et al. 2014 UAI, Sec. on common ancestors (any real-data application?);
  - forward citations of Gisin 2020, Steudel–Ay and Wolfe–Spekkens–Fritz.

---

### Referee estimate: REJECT-LIKELY (as written); BORDERLINE after fixes B1–B4
Venue class: short-note or letters (e.g. *Methods Ecol. Evol.* Application/Forum, *Oikos* Forum, *Ecology* Statistical Report).
Value carried by: factor 4 (translation into ecology), weakly. Factor 1 or 2 is absent: the bound is owned.
Main risk a referee would raise: the conditioning step, listed as new in §6, is a linear residualisation whose effect is indistinguishable
from a placebo regressor, and the remaining test rejects a null ("pairwise-only drivers") no ecologist holds, with no comparison with
matrix regression or wavelet Moran.

Cap check: pure UNCLEAR ⇒ at most BORDERLINE. REJECT-LIKELY here comes from the "wrong or unverifiable central claim" clause (step 2
and §4's reading). It does not come from the cap. Bogdziewicz et al. 2021 is uncredited, but it owns the Poland *conclusion* (weather
synchrony drives beech synchrony), not the test, so the "owner uncredited" clause applies only to that conclusion.

---

## Required fixes (exact locations in the target note)

**Blocking**
- **B1 (§2 and §3 step 1, §7):** state stationarity as an assumption. Add a detrend / stationarity step before Detect, explain that a
  shared trend is itself a common ancestor (non-convexity of the triangle set), and add the positive statement that within-site
  autocorrelation and per-site median thresholds do *not* invalidate the bound.
- **B2 (§3 step 2, §4 Poland bullet, §6 "New"):**
  - Rewrite step 2. Either use genuine conditioning (stratify on the candidate, with V within strata and a combined test), or state
    the additive-linear model as an explicit assumption.
  - Make a **placebo-regressor control** mandatory: a time-permuted candidate matched on R².
  - Delete "the candidate accounts for the common cause" and replace it with "no longer demonstrable" (the gate's own wording).
  - Delete "removes most of what the sites share" and "what a centre looks like".
- **B3 (§6):** move the condition-on-a-centre step and the space/time-by-lags reading from "New" to "Owned". Cite matrix regression /
  partial Mantel (Bogdziewicz et al. 2021), the wavelet Moran decomposition (Sheppard 2016; Walter 2017), lag analysis (Bjørnstad et
  al. 1999), and Chaves et al. 2014 for classical common-ancestor tests. Remove or re-scope the Goldstein et al. 2026 sentence, which
  concerns data concordance, not synchrony.
- **B4 (§4):**
  - Disclose that the Poland stage-1 p = 0.008 is a replication of a value seen in a 1047-triple family where nothing passed Holm.
  - Give the median same-study E (0.37) alongside the top-triple range (0.7–0.86).

**Non-blocking**
- N1 (§2): add the linear-Gaussian analogue (pair-specific factors force ρ ≤ ½ in the symmetric case ⟦HAND⟧) and say the model-free
  version's value is nonlinear and non-Gaussian response. Add one line saying that with three series a one-factor model is saturated,
  so this is not a tetrad test.
- N2 (§3 step 1): add a size/power simulation over asymmetric boundary models and AR(φ), and justify the block length (masting has
  negative lag-1 autocorrelation). Drop the circular wrap or justify it.
- N3 (scripts): use eq. 16 in `synchrony_ceiling_gate.py` (margins are not exactly ½ at odd n), and re-estimate the residualisation
  inside each bootstrap resample.
- N4 (§5): reconcile rule 3 ("pooled statistic, mean V") with rule 5 ("don't pool by averaging").
- N5 (§6/§7): compare NSI against classical inflation / entropic bounds for power. In ecology "any physics" is a free generality that
  costs power.

---

## Appendix A: audit computations (reproducible description; scripts were in a scratch dir)

Data: MASTREE+ V2 (2024-06-26) CSV and the ERA5 Open-Meteo JSONs used by `mast_conditional_gate.py` (job tmp dir
`~/.claude/jobs/26482d7b/tmp/mast/`). Statistic: `V16` imported unchanged from `verification/mast_ceiling_gate.py`.

1. **Poland 008-009-010** (study D00013; VarType C, "% individuals reproducing"; 72 years; up to 8 ties at the median).
   - raw V = 2.972, E = (0.72, 0.75, 0.69);
   - OLS residual on own ΔT: V = 1.265, E = (0.61, 0.50, 0.56);
   - cross-site corr(ΔT) = 0.90–0.97.
2. **Placebo** (2000 draws, seed 1):
   - ΔT with years permuted, one permutation shared by all sites → median V 1.83 (5–95%: 0.77–2.90); P(V ≤ 1.265) = 0.17;
   - independent permutations per site → median V 0.92; P(V ≤ 1.265) = 0.67;
   - random 1e-9 tie-break jitter of the raw data → median V 2.72 (5–95%: 2.34–3.29), so tie-breaking alone does not explain the drop.
3. **Other adjustments:**
   - linear detrend on year: V = 4.50, E = (0.83, 0.83, 0.94); rank correlations with year 0.19–0.31;
   - rank-residualisation on ΔT: V = 0.93;
   - strata by tercile of the site-mean ΔT (n = 24 each): V = −0.94, +2.45, −0.22.
4. **Size simulation** (seed 7):
   - model: three independent AR(1) Gaussian pair-sources; site = min of its two sources (the continuous AND model, at the eq. 13
     boundary after median split);
   - test: circular block bootstrap (block 3, 2000 resamples), p = P(V* ≤ 0), 400 replications;
   - results:

     | n | φ | trend | rejection rate (α = 0.05 / 0.01) | mean point V |
     |---|---|---|---|---|
     | 72 | 0 | none | 0.003 / 0 | −0.23 |
     | 72 | 0.5 | none | 0.007 / 0.003 | −0.34 |
     | 45 | 0.5 | none | 0 / 0 | −0.51 |
     | 72 | 0.5 | common linear, slope 1.5 SD over the record, added to each of the three independent sources | **0.61 / 0.235** | +1.93 |

## Sources consulted
- Primary, read: Gisin et al. 2020 (shelved PDF, pp. 1–4, eqs. 1–16); the gate files and scripts in this folder;
  `seam_A_scout.md`; `ecology_owner_scout_DEEP.md`.
- Web, snippet/abstract level:
  - Chaves et al. 2014 (arXiv:1407.2256);
  - Steudel–Ay (arXiv:1010.5720);
  - Wolfe–Spekkens–Fritz (arXiv:1609.00672);
  - Bogdziewicz et al. 2021 *Ecology* (beech synchrony; livrepository.liverpool.ac.uk/3122460);
  - FOFC/tetrad documentation (Kummerfeld–Ramsey; arXiv:2009.08606);
  - general searches for network-nonlocality applications to ecology and for higher-order synchrony tests (no hits).
