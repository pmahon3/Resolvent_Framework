# Seam A scout: triangle network vs interactions vs centre

reviewed: false. 2026-11-05.

Scope: binary triangle consensus ceiling; static pairwise sources (S) vs interactions (I) vs centre (C); feedback/time; use outside physics; ecology. Read levels: [abstract] [skim] [methods] [full]. Tool limits: the fetcher summarises pages with a small model and could not read PDFs (2303.09954, 2503.16654 PDF, 2605.00981 gave raw bytes). Quotes below are the fetcher's paraphrase or snippet unless marked; none verified verbatim against the PDF. Treat "read" as partial.

Already recorded (not new): Fritz 2012, Wolfe–Spekkens–Fritz 2019, Navascués–Wolfe, Rosset–Gisin–Wolfe, Renou et al. (incl. Finner), Gisin et al. 1906.06495, Steudel–Ay Thm 10 (`centre_vs_relations_owned_map.md` S1, S2, rows 12-17), Moran/Liebhold/Vasseur–Fox/Sheppard (row 30; ecology scouts).

## 1. Verdict table

| | Claim | Verdict | Decisive source | Read |
|---|---|---|---|---|
| (a) | Binary triangle consensus ceiling with uniform margins is (3sqrt2-2)/4 = 0.5607 | PARTLY OWNED (value implicit in a conjectured, numerically found boundary; not stated as a consensus bound by anyone found) | da Silva–Pozas-Kerstjens–Parisio, arXiv:2503.16654, E1=0 plane boundary | [methods, partial, via HTML] |
| (b) | S vs I comparison (triangle-local set vs pairwise MRF/Ising) | NOT FOUND as a comparison. Components owned separately. | Kruis–Maris 2016 (Ising has equivalent latent-cause form); Steudel–Ay Thm 10 caveat; Perrone–Ay 2016 | [skim] / [abstract] |
| (c) | Feedback/time: interaction unrolled creates common ancestors ("centre in time") | PARTLY OWNED as a general remark (unrolling removes cycles, DBN survey); the triangle-vs-consensus version NOT FOUND | Bongers–Forré–Peters–Mooij 2021 (AoS); Mooij–Janzing et al. | [abstract/snippet] |
| (d) | Network causal-compatibility tests used outside physics | NOT FOUND (no empirical use of inflation or Steudel–Ay in biology, ecology, neuroscience, genetics, epidemiology). Adjacent: latent common input in neural Ising models; hidden-common-cause DBNs | Macke–Opper–Bethge 2011; Lo et al. 2015 | [abstract] |
| (e) | Test that 3+ site synchrony REQUIRES a regional driver | NOT FOUND. Pairwise/wavelet Moran-vs-dispersal tests are owned; no triplet statistic or compatibility test found | Walter et al. wavelet Moran theorem; Castorani et al. 2022; Bjørnstad et al. review | [abstract/snippet] |

### (a) Detail
- Arithmetic (mine, ±1 outputs, uniform margins): P(all equal) = (1+3·E2)/4, E2 = pairwise correlator. 0.5607 <=> E2 = sqrt2-1 = 0.4142.
- 2503.16654 gives, on the E1=0 plane, a one-variable boundary in E2, E3 (u=(3+E2-|E3|)/2). I solved it numerically: the root reaches E2 = 0.41421 at |E3| = 2-sqrt2, exactly our value. The paper separately mentions sqrt2 as the threshold E3 <= -2+sqrt2 where local models saturate the no-signalling+independence inequality. So our 0.5607 coincides with the endpoint of their conjectured tight boundary. Whether that is the global max of E2 at E1=0 is my reading, not their statement; the fetcher says the paper "does not state a maximum of E2".
- Status of their boundary: found by exhaustive numerical local-model search, conjectured tight; sources of cardinality 333/322/422/332 suffice ("GHZ-boundary model uses cardinality 3"). So larger alphabets than binary are used and do not beat 0.5607 on this boundary. Our binary-source AND rule attains it, consistent.
- Upper bounds proven: Finner-type, P(000) <= sqrt(P_A P_B P_C)-style, gives only <= 1/2 for the 3-4-outcome symmetric all-agree probability in 2405.08939 (different setting: probability of equal outputs s111, not binary consensus). For binary consensus the proven ceiling is weaker than 0.5607 as far as found (not checked: whether Finner on P(000)+P(111) gives 0.5 or more; with margins 1/2, Finner gives P(000) <= 1/2^(3/2)=0.354, so P(all equal) <= 0.707; mine, unchecked).
- Noisy-GHZ critical visibility: da Silva–Parisio 2023 (arXiv:2303.09954, PRA 108, 052602) conjecture values that are roots of quartic polynomials; snippets say ~0.362 for three-outcome and 1/3 or 1/4 for smaller cases (snippet-level, conflicting; [abstract]). Quantum inflation excludes quantum realisation of noisy Mermin-GHZ above visibility sqrt(2/3) (Quantum Inflation, arXiv:1909.10519, snippet).
- Binary quantum network nonlocality: Don et al., arXiv:2605.00981 (2026), "The minimal example of quantum network Bell nonlocality" [title only; PDF unreadable]. Could affect the classical-vs-quantum gap framing; not our question.
- Perfect GHZ not classical-triangle-possible: Fritz 2012 (recorded); consensus ceiling < 1 is the quantitative version, closest to 2503.16654.

### (b) Detail
- Kruis & Maris, "Three representations of the Ising model", Sci. Rep. 6:34175 (2016). They call common-cause, reciprocal-affect, common-effect readings "mathematically equivalent." Static; no feedback in time (fetcher). Shows a pairwise MRF can be rewritten with a latent variable, but that latent is a joint (centre-like) variable, not pairwise sources. [skim]
- Perrone & Ay 2016, Front. Robot. AI 3:35: "redundancy (as for example in X=Y=Z) can be described in terms of pairwise interactions, not triple" (snippet). Supports (I) reaching consensus in the exponential-family sense; says nothing about triangle sources. [abstract]
- Ay et al. hierarchy of interactions (MPI preprint 53/2011; review arXiv:1801.03026). [abstract]
- Steudel–Ay Thm 10 caveat (recorded): pure 3-way (XOR-like) dependence needs only pairwise common ancestors.
- Gap: nobody found comparing {triangle-local} with {pairwise MRF closure} on binary triples. The seam A comparison stands.

### (c) Detail
- Bongers et al., "Foundations of SCMs with cycles and latent variables," Ann. Statist. 49 (2021), arXiv:1611.06221. Snippet: cycles arise "when one describes the equilibrium states of these systems"; underlying dynamics acyclic over time. Marginalisation may fail to exist for cyclic SCMs. [abstract+snippets]
- Mooij, Janzing, Schölkopf, "From ordinary differential equations to SCMs" (UAI 2013) and cyclic additive noise models: "unrolling" the model in time removes cycles (snippet). [abstract]
- Dynamic causal networks (Blondel et al., arXiv:1610.05556): static vs dynamic hidden confounders (snippet). [abstract]
- Hidden-common-driver detection in time series: Benkő et al. arXiv:2504.01811; Sauer-style; CCM/LPCMCI (recorded in owned map C). [abstract]

### (d) Detail
- Macke, Opper, Bethge, PRL 106:208102 (2011), arXiv:1009.2855: common input induces higher-order correlations, so pairwise Ising can mistake common input for coupling (snippet). Parametric (Dichotomized Gaussian), no network-compatibility test. [abstract]
- 2015 disordered-Ising study: hidden common input distorts inferred couplings (arXiv:1506.00358 snippet). [abstract]
- Lo et al. 2015, PMC4659244: DBN learning with hidden common causes (gene regulation). [abstract]
- Searched inflation/Steudel–Ay with neuroscience, ecology, genetics, epidemiology: no hits. Wolfe-line applications are quantum/foundations.

### (e) Detail
- Ecology tools are pairwise or regression-based: matrix regression (kelp, Castorani et al. 2022, Ecol. Lett.; PMC9541195), wavelet Moran theorem and timescale decomposition (Sheppard, Reuman, Walter; wsyn package), phase coherence / lagged correlation (Bjørnstad-style review snippet). Snippet: mechanisms "may produce nearly identical signatures" in pairwise synchrony. [abstract]
- Nothing found that uses a three-site statistic to exclude pairwise-only drivers. Caution: "beyond pairwise" literature in neuroscience (higher-order correlations) and network synchrony (Kuramoto higher-order) was not searched deeply.

## 3. Is "centre in time" stated anywhere?
Not in the triangle/consensus form. Nearest: (i) Bongers et al. and Mooij et al. say a cyclic/equilibrium model is the limit of an acyclic-in-time model; (ii) Dynamic causal networks note hidden confounders can be static vs dynamic; (iii) Eichler-style Granger with hidden common cause. None states: "feedback among A,B,C makes B_{t-1} a common ancestor of A_t and C_t, hence consensus is no longer capped by independent-source bounds." That follows trivially from unrolling, so expect it to be folklore; no quote found. Verdict: NOT FOUND as a statement; the mathematics is immediate from unrolling (low novelty risk of being "wrong", high risk of being "obvious").

## 4. Search terms used
triangle network binary outputs all equal GHZ visibility; noisy GHZ critical visibility Steudel Ay Gisin; Ising pairwise vs network local causal compatibility; P(000) triangle AND rule Finner; Ay hierarchy of interactions common ancestor synergy; cyclic SCM unrolled feedback latent confounder Bongers; inflation/Steudel-Ay applied to neuroscience/ecology/genetics/epidemiology; spatial synchrony three populations triplet Moran; Reuman wavelet Moran vs dispersal; hidden common driver time series feedback DBN; common input vs pairwise Ising neurons; Glauber Ising triangle network. (Standard/extended web search only; 14 queries; no Google Scholar citing-paper traversal.)

## 5. Unread sources that could flip verdicts
1. da Silva–Pozas-Kerstjens–Parisio 2503.16654 PDF: explicit statement of max E2 / consensus; Eq. (4) region; could make (a) fully OWNED. Also Appendix E.
2. da Silva–Parisio 2303.09954 PDF: critical visibilities, conjectures [PDF unreadable here].
3. Don et al. 2605.00981: binary-triangle quantum gap; may restate local bounds.
4. Fritz 2012 (1206.5115) full text; Wolfe et al. binary-triangle examples (already on owned-map reading list).
5. Pozas-Kerstjens et al. 2305.03745 "Post-quantum nonlocality in the minimal triangle scenario" (relaxation of binary correlation set; analytic outer bounds on E2 may bound consensus).
6. Steudel–Ay full text (does the net allow observed-to-observed edges as non-centre?).
7. Bongers 2021 full text and Mooij–Janzing unrolling: whether latent-confounding-by-feedback is stated.
8. Higher-order synchrony literature in ecology/neuroscience (triplet/3-point statistics), Hugueny–Cazelles extended Moran theory (on owned map).
9. Kruis–Maris full text: equivalence statement is on a single latent variable, check it covers 3 binary nodes.

## Addendum 2026-11-05 (main session read both PDFs): verdict (a) → OWNED
- **Gisin et al. 2020, Nat. Commun. 11, 2378 [statements read].** With uniform margins, every triangle distribution compatible
  with no-signalling and independent sources (classical, quantum, or any GPT) satisfies (1−E_AB)² − E_BC² − E_AC² ≥ 0, hence
  Σ(1+E_ij)² ≤ 6, and in the symmetric case E₂ ≤ √2 − 1. By Cauchy–Schwarz, P(all agree) = (1 + ΣE_ij)/4 ≤ (3√2 − 2)/4 ≈ 0.5607.
- **Our binary AND model attains it.** The point (E1, E2, E3) = (0, √2−1, √2−2) is the x = 0 member of da Silva–Pozas-Kerstjens–Parisio's
  GHZ-boundary family, which they prove equals the NSI bound for E3 ≤ −2+√2 (their App. E).
- **Consequence (owned):** for consensus with uniform margins, pairwise sources cap at (3√2−2)/4 *whatever the physics*. Quantum
  sources give no more consensus than classical ones. Only a centre, or interaction (a centre in time), goes further.
- PDFs shelved: `gisin_et_al_2020_nsi_triangle_networks.pdf`, `da_silva_pozas_parisio_2025_minimal_triangle_local_models.pdf`.
