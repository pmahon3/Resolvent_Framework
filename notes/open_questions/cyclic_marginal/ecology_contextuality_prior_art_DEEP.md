# Ecology x contextuality: deeper prior-art pass (2026-11-04)

reviewed: false. Builds on `ecology_contextuality_prior_art.md` (not repeated). Read levels: full / section / abstract / snippet.
Shelf-first: SHELF_INDEX and taxonomies hold nothing on Pearl, instrumental, Wood-Spekkens, Chaves, Simpson, latent class
(only the earlier data_tests entries and Capotorti 2011 statistical matching). 4 PDFs added (arXiv), entries in SHELF_INDEX.

## Verdicts

| Open item | Verdict |
|---|---|
| (iii) finite-sample test of "a joint exists" | **OWNED** (Berrett-Samworth 2023), under an independence/stationarity assumption that is exactly what ecology lacks |
| (i) observational analogue of random assignment | **PARTLY OWNED** (causal inference: exogeneity of the context variable; IV inequalities test it) |
| (ii) heterogeneity-aware null | **NOT FOUND as a test**; the formal home is selection/transportability + latent-class theory; one logical point below (HAND) |

## (iii) Finite-sample test of joint existence: OWNED
- Berrett & Samworth, arXiv:2205.08627 [section: abstract, intro, Sec 3 statement, Sec 5 skim; proofs unread].
  Quote: "finite-sample Type I error control, and is consistent against all incompatible alternatives" (Sec 1).
  Object: marginals P_S on overlapping index sets S, null H0: Frechet class nonempty. Statistic via Kellerer duality, computed by LP; Monte Carlo
  bootstrap version (Sec 5); R package MCARtest. Case d=3, S={12,13,23}, binary-ish, has a minimax-optimal analysis (Thm 8).
  This is exactly our triangle marginal problem as a hypothesis test.
- Assumption (Sec 3): "independent data (X_{S,i}) ... X_{S,1},...,X_{S,n_S} ~ P_S". One fixed P_S per context, i.i.d. No spatial/temporal
  dependence, no population drift. Disturbance (signalling) is not modelled: marginal inconsistency counts as incompatibility.
- Residue (open, not found): dependent data (spatial autocorrelation); a disturbance-tolerant (CbD-like) version; heterogeneity (below).
- Related, snippet only: D'Orazio-Di Zio-Scanu, *Statistical Matching* (Wiley 2006) and JOS 2006: bounds on the joint of (X,Y,Z) from
  (X,Y),(X,Z) samples; uncertainty displayed, no test of incompatibility found. Capotorti 2011 on the shelf is the same family.
- Earlier-pass Bell p-value papers (Elkouss-Wehner, Gill) stay owned for designed i.i.d.-or-martingale experiments. Gill's
  randomised settings guard against drift: that is the random-assignment device again (snippet).

## (i) Observational analogue of random assignment: PARTLY OWNED
Translation: random assignment of units to context = the context variable C has no latent common cause with the outcomes and is
independent of the unit's type. In causal-inference language this is the **instrumental/Bell scenario**.
- Wood & Spekkens 2015, NJP 17 033002, arXiv:1208.4119 [section: intro, Bell scenario, Sec on hidden common causes; abstract level
  for the rest]. Their setup assumes "the settings S and T are sampled independently" (Sec 4); they apply causal discovery to
  population distributions and say "we needn't worry about" the finite-sample subtlety (Sec 2). So: the Bell-violation-needs-
  fine-tuning argument is population-level only.
- Pearl 1995 instrumental inequality, via Wolfe-Spekkens-Fritz arXiv:1609.00672 [section: intro, Sec on Bell scenario via inflation;
  not full]. Quote: "Pearl later derived the instrumental inequality, which provides a necessary condition for the compatibility"
  (Sec 1). It is the testable fingerprint of "C is as-if random + exclusion". Bell inequalities and it are the same family. The inflation
  technique gives necessary inequalities for latent-variable structures, including three binary variables with pairwise common causes
  (abstract). Population level; no sampling theory.
- Evans, arXiv:1209.2978 [abstract + Sec 3 skim]. Quote: "the observed distribution of a discrete model is always restricted if any
  two observed variables are neither adjacent ... nor share a latent parent". Generalises the instrumental inequality; exact for a binary
  instrument, "insufficient if Z takes three states" (Bonet 2001, UAI, [abstract/snippet]).
- Kitagawa 2015 Econometrica 83(5) 2043-2063, "A test for instrument validity" [abstract/snippet]: a finite-sample variance-weighted
  KS test of the IV testable implication. This is the statistics of the instrumental inequality: **natural experiments = observational
  random assignment, with a sampling-error test, is OWNED in econometrics.**
- Chaves-Majenz-Gross, Nat. Commun. 6 5766 (arXiv:1407.3800) [snippet]: entropic constraints on causal structures. The title
  "Inferring latent structures via information inequalities" could not be confirmed (UAI 2014 attribution unverified).
- Transportability: Pearl-Bareinboim selection diagrams, data-fusion PNAS 2016 [snippet]: formal language for "populations differ
  across datasets", used to transfer effects, not (found) to test joint existence.
- **What remains open for ecology:** these give conditions under which "context assigned as if random" is testable or assumed; in a
  plot/season survey no instrument exists and context (survey, season, protocol) is typically confounded with site. Nothing found that
  asks what the joint-existence test means when the context is itself a latent-confounded variable. Plausible route: stratify on observed
  covariates (conditional exchangeability) and test within strata; unverified.

## (ii) Heterogeneity-aware null: NOT FOUND as a test
- Searches for Simpson's paradox + contextuality/Bell found only: Shi, "Quantum Simpson's paradox and high-order Bell-Tsirelson
  inequalities", arXiv:1203.2675 [snippet] (a quantum reversal exceeding the classical bound; the converse direction, classical
  heterogeneity faking quantum, is not what it treats); selection-bias papers arXiv:2012.07285 and 2508.13431 [snippets]: post-selection
  or collider bias can produce Bell-type "violations" with classical models (a related fake-violation mechanism, not mixtures across
  contexts); Kupczynski, Entropy 23 1104 (arXiv:2104.11555) [snippet]: Bell-test variables are inconsistently connected, sampling
  matters. None formalises "context-dependent mixture weights of classical populations".
- Dzhafarov's seminar abstract (Oxford, snippet): contextuality "can be obtained trivially by averaging over sufficiently diverse
  patterns of noncontextual responses". Owned in outline, no theorem or test located.
- Berrett-Samworth's null is a single P_S per context; mixtures inside a context cause no problem (a mixture of joints is a joint).
  The problem arises only across contexts, which they do not model.
- Latent class / mixture models with context-dependent weights exist as modelling tools (not searched deeply); I found none used as the null
  of a compatibility test.
- HAND (unverified): with unrestricted weights pi_c(k) the null is vacuous, because each context table is already the margin of a
  classical joint (take one subpopulation per context); so a heterogeneity-aware test must restrict the weight shifts (observed
  covariates, bounded total-variation between context sampling distributions, or a shared latent-class set with at most K classes). This is
  where a small piece of new, testable theory could sit: the polytope of "mixtures of K classical classes with weight shift <= delta"
  is a Minkowski sum of the marginal polytope with a ball, the same construction Berrett-Samworth already use for the noise ball
  (MCARtest: Minkowski sum of marginal polytope and consistency ball). Prior-art gate not run on this.

## Net
The test machinery for the triangle (existence of joint under sampling) is OWNED and ready-made (MCARtest, d=3). IV/Bell/inflation own the
causal reading of "random assignment". The ecology-specific residue is the pair: (a) dependence structure of field samples, (b) a
constrained-heterogeneity null. Neither found. Coverage caveat: US-only search snippets, ecology and non-English literature under-covered;
ecological "data integration consistency" tests (earlier file, section D) remain unread beyond snippets.
Bearing on WHY.md: this is the loop question in field form: do three local surveys glue to one landscape, or is the failure just
differing populations (hidden idealisation: that the context did not change what was sampled)?

## Addendum (main session, 2026-11-04): is the heterogeneity-aware null vacuous? No — sharp threshold

⟦HAND, LP-checked⟧ (`notes/open_questions/verification/eps_star_triangle.py`, scipy linprog, float).
- Null H_ε: each context k sampled a classical world Q_k with TV(Q_k, Q) ≤ ε for one common classical Q.
  Equivalent to: ∃ classical Q with TV(marg_k Q, P_k) ≤ ε for every context (marginalising contracts TV;
  conversely, replace Q's k-margin by P_k keeping the conditional — moves Q by exactly that TV).
- So ε*(data) := min ε for which H_ε holds is an LP, computable for any dataset: the smallest between-context
  population shift a classical account needs.
- Binary triangle, faked parity contradiction (A=B, B=C, A≠C uniform): ε* = 1/3 exactly (facet
  P(A=B)+P(B=C)+P(A≠C) ≤ 2 violated by 1; each context can move its agreement by ≤ ε; achieved by the
  equal mixture of the three one-failure worlds). LP: 0.333333.
- Margin-consistent binary families: sampled max 0.238 (4000 families), parity case = 1/3 ⇒ conjecture:
  sup ε* = 1/3, and ε* = (max facet violation)/3. Inconsistent (signalling) families reach ≈0.62 (sampled);
  signalling is separately visible in the marginals (CbD direct influence).
- Verdict: H_ε is vacuous only for ε ≥ sup ε* (here 1/3); below that it has content. "Unrestricted weights"
  = ε = 1 is the vacuous end. Likely owned in substance: ε*(P) is a distance to the marginal polytope, close
  to Berrett–Samworth's incompatibility statistic (metric to be checked); the contextual fraction is a different
  (mixture-weight) measure. The heterogeneity-budget reading tied to a biologically calibrated ε is the lens.
