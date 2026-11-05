# Can non-classical structure be tested in commonplace ecological data? Prior art (2026-11-04)

reviewed: false. Literature-scout pass. Shelf first, then ~10 standard web searches. Read levels per item:
full / skim (pdftotext, grep for method sections) / abstract / snippet. Extends, does not replace,
`ecology_contextuality_sweep_2026-10-20.md` (lizards, Barendregt–Thomas, ecological inference).

## Shelf first (already there)
- CbD: `dzhafarov_kujala_2016_cbd_context_content.pdf`, `dzhafarov_kujala_2017.pdf`,
  `dzhafarov_kujala_cervantes_2020_cyclic_systems_cbd.pdf` (SHELF_INDEX questions: `data_tests`).
- Ecology: only `ecology_contextuality_sweep_2026-10-20.md` (Aerts et al. lizards = the one direct hit;
  data check showed Sinervo data are payoffs/regressions, not views).
- Contextual fraction (ABM 2017) and a statistical-test paper were NOT on the shelf; added now (below).

## A. CbD on non-physics data
- Dzhafarov–Zhang–Kujala, "Is there contextuality in behavioural and social systems?", Phil. Trans. R.
  Soc. A 374 (2016) 20150099, arXiv:1504.07422 [abstract + skim]. Reviews polls (Wang–Busemeyer
  question-order data, 72 of 73 pairs obey the QQ equality; chi-square p>0.35 over 72, df 72), visual
  illusions, conjoint choice, word combinations, psychophysical matching. Verdict: NO contextuality in
  any; all context dependence is direct influence (signalling). Offered as a "working hypothesis".
  Scope: cyclic binary systems, where CbD gives a necessary and sufficient criterion.
- Cervantes–Dzhafarov, "True contextuality beats direct influences in human decision making", arXiv:1807.05684
  (J. Exp. Psych. Gen. 2019) [abstract + skim]. Crowdsourced "Snow Queen" design: contextuality found in
  5 experiments, absent in a control (6). Statistics: 6192 participants, 99.99% bootstrap CIs (500k
  resamples) on the CbD statistic, t and Chebyshev p-values. Conclusion reversed the 2016 hypothesis.
- Dzhafarov, Cervantes, Kujala 2017 (canonical systems); Kujala–Dzhafarov 2019 "Measures of contextuality
  and non-contextuality", Phil. Trans. A [snippets]. Book: Dzhafarov–Kujala–Cervantes, *Contextuality in
  Random Variables* (CUP 2026), preface arXiv:2511.01783 [snippet].
- **Conditions they actually use (my reading):** (i) contexts built by RANDOM ASSIGNMENT of respondents
  to question pairs, with groups so large "statistical issues can be ignored"; (ii) the same question
  has a fixed identity across contexts (a design choice); (iii) inconsistent connectedness allowed, and
  that is the point: marginal differences are charged to direct influence, only the residual is
  contextuality; (iv) binary cyclic systems for the closed-form test. Large N, designed experiment.
  Dzhafarov also warns (Oxford seminar abstract, snippet) that averaging over diverse noncontextual
  patterns can produce contextuality trivially, a "serious methodological problem" for social data.

## B. Ecology / biology
- No CbD, Bell, CHSH, marginal-problem or contextual-fraction test on ecological, microbiome,
  epidemiological or field data found (web search snippets, US-only; moderate chance of a miss, non-English
  and paywalled ecology under-covered). Confirms the 2026-10-20 sweep.
- Aerts–Broekaert–Czachor–Kuna–Sinervo–Sozzo 2014 (lizards): modelled, joints not measured, a violated
  marginal law = CbD direct influence. A model, not a rigorous test. See sweep file.
- Khrennikov, Asano, Basieva, Ozawa: quantum-like modelling in biology (E. coli glucose-lactose, gene
  expression, "ecosystems" as a claimed scale), Entropy 25 (2023) 886 review, PMC4843639 (Asano et al.
  glucose preference) [snippets]. These MODEL non-Kolmogorov statistics; no statistical test against data
  found; Khrennikov concedes the tools are weaker than in physics. Not a test.

## C. Testing from noisy finite samples
- Contextual fraction: Abramsky–Barbosa–Mansfield, PRL 119 (2017) 050504, arXiv:1705.07918 [skim].
  Graded LP measure (weight of the non-contextual part). Continuity and noise-robustness: Vallée et al.
  2024 (continuity; relaxed non-disturbance assumptions) [snippet]; non-increasing under classical
  processing incl. binning: Barbosa et al. arXiv:1905.08267 [snippet]. **No finite-sample confidence
  bounds for the contextual fraction found.** It handles signalling only by assuming a no-signalling
  scenario; the CbD route (A) handles inconsistent marginals.
- Finite-sample p-values for Bell inequalities: Elkouss–Wehner, "(Nearly) optimal P values for all Bell
  inequalities", npj Quantum Inf. 2 (2016), arXiv:1510.07233 [abstract]; Gill, "Optimal statistical
  analyses of Bell experiments", AppliedMath 2023 (Wilks LRT) [snippet]; Bierhorst (supermartingale
  exact p-values) [snippet]. All assume trial independence (memory loophole); built for designed
  experiments.
- CbD: bootstrap CIs and p-values on the statistic in Cervantes–Dzhafarov (above); multiple-testing
  inflation noted in DZK (73 pairs at 0.01 gives 0.52 chance of a false rejection).
- Corrected Bell/noncontextuality inequalities for realistic experiments, arXiv:2310.19383 [snippet]:
  relax idealisations (imperfect non-disturbance, finite statistics).
- Noise direction check: Patrick's claim ("noise blurs toward classical, never fakes non-classical") holds
  for symmetric depolarising-type mixing. It FAILS for (a) signalling/direct influence, which can fake
  violations of Bell-type inequalities (that is exactly why CbD exists), and (b) heterogeneity (E):
  mixing across populations can create a violation of consistent-connectedness-based criteria.

## D. Ecology-side neighbours (all snippets)
- Data integration: Koshkina et al. 2017 (MEE, survey + presence-background); Pacifici et al. 2019
  (Ecology, misaligned spatial data); Isaac et al. 2020 (integrated vs single dataset, Ecography);
  Saunders et al. 2019 (Ecology, conflicting trends via integrated population model); PLOS One 2017
  spatial capture-recapture "model-based test for data inconsistency". Pattern: ecology BUILDS a joint
  (latent field, joint likelihood) or down-weights conflict. It tests consistency of estimates, not
  whether any joint exists. This is the closest working analogue to condition (4).
- JSDMs: a joint is built in (latent factors / Hammersley–Clifford). Ecological inference and Simpson's
  paradox: see sweep file (marginal problem with bounds: Duncan–Davis, Goodman, King).

## E. Heterogeneity rival
- Owned in outline: Dzhafarov (seminar abstract) states averaging across diverse noncontextual patterns
  gives contextuality trivially. The DKC book notes status can flip under modifying any one variable's
  distribution. No worked Simpson-style mixture example found (snippets). Stark–Silber–Krosnick et al.
  2020 (SMR, 11 countries) shows order effects vary by population but is not a contextuality analysis.
- Within CbD this is addressed by design: random assignment makes sub-populations equal across contexts.
  Observational data cannot do that.

## Verdict
- **Asked of ecological data with a rigorous test? No hit.** Only a model-based neighbour (lizards).
  Gap holds, search coverage caveat above.
- **Owned:** the test machinery (CbD criterion for cycles; contextual fraction; Bell p-values; bootstrap),
  the heterogeneity warning, and "direct influence vs contextuality" separation.
- **Open:** (1) the condition list for observational data; (2) what replaces random assignment; (3) a
  finite-sample test of the joint-existence (marginal) problem on field tables with a heterogeneity-aware
  null; (4) whether ecology's own data-integration inconsistency tests are the same object.
- Honest correction to the framing: the psychology precedent says the physics-style version mostly
  finds nothing once direct influences are charged, with one famous reversal (2018). "Non-classical" is
  a conclusion earned after ruling out signalling and heterogeneity, not a default reading.

## What a first test on commonplace ecological data needs
1. Contexts: observation sets sharing species/variables (e.g. surveys A,B,C with species 1-2, 2-3,
   3-1), each with within-context joint counts (presence/absence or binned abundance), binary first.
2. Identity: sites/periods exchangeable across contexts. Random site assignment to protocols is the
   field analogue of random assignment; absent it, stratify on covariates and test stationarity. This
   is the weakest link.
3. Disturbance: CbD-style: allow marginal differences, test the residual. Needs an observation-effect
   model (detectability, effort), not just marginal equality.
4. Statistics: replicate counts per context large enough for bootstrap CIs on the cycle statistic
   (psychology used ~10^3 per context); account for spatial/temporal dependence, which breaks the i.i.d.
   assumption in all the p-value results cited; correct for multiple tests.
5. Null: a heterogeneity-aware null (mixtures of noncontextual site types) so that a rejection is not
   Simpson. A violation is then at best "no single joint across these samples".
Honest distance: no ecological dataset is known to satisfy (2) and (3); published field sets
(lizards) are payoffs, not views. The realistic first step is a simulation with known mixtures,
asking how often a heterogeneous but classical landscape trips the CbD cycle test.

## Shelf additions (PDFs; SHELF_INDEX entries added)
dzhafarov_zhang_kujala_2016_behavioral_social_contextuality.pdf; abramsky_barbosa_mansfield_2017_contextual_fraction.pdf;
elkouss_wehner_2016_optimal_p_values_bell.pdf; cervantes_dzhafarov_2018_true_contextuality_decision.pdf (all arXiv).
