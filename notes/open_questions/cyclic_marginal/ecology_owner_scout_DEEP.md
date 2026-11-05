Ecology-owner scout, DEEP pass: does statistical ecology (or a neighbour) own the model-free cross-method compatibility test?
reviewed: false. 2026-11-05.

Read levels: [methods read] only for Tenan 2017 (WebFetch of PLOS HTML). [skim] Presanis 2013 (PDF text, abstract/intro/grep). Everything else [abstract]/[snippet] (PMC blocked by browser check; Maunder-Piner, Goldstein et al., Besbeas-Morgan, Lu-Ades, Dias paywalled or unreachable). So "NOT FOUND" below = not found in sources reachable; not a proof of absence.

## 1. Verdict table
| Item | Verdict | Decisive source |
|---|---|---|
| (a) Model-free test: does ANY common joint exist for per-method margins? | NOT FOUND (every reachable candidate is type (i)) | Tenan 2017 [methods read]; Presanis 2013 [skim]. Closest adjacent: statistical matching Frechet bounds (D'Orazio et al. 2006, StatMatch) [doc snippet] computes the set of compatible joints but is not used as a test, and has no ecology use found. |
| (b) Pre-registered eps budget from biology | NOT FOUND as a budget. PARTLY OWNED as estimated parameters (method-specific detection, availability, false-positive rates: Nichols 2008, Miller 2011) | Miller et al. 2011 [snippet] |
| (c) Cycle / loop-inconsistency analogue | PARTLY OWNED in NMA (loops of comparisons), but as a linear-scale additivity constraint, not a marginal-polytope constraint. Not ecology. | Lu & Ades 2006 [abstract]; Dias 2010 [abstract] |
| (d) Data shape (methods see different species subsets at shared sites) | REAL and common (cameras/eDNA/acoustic/iDNA papers); always analysed by multi-method occupancy or integrated models, not as a marginal problem | Prior pass snippets; airborne-eDNA vs camera/acoustic/observer species lists "differed substantially" [snippet] |

## 2. Tenan et al. 2017 (PLOS ONE 12(10):e0185588) [methods read]
- It is type (i). Integrated spatial capture-recapture (SCR) for brown bears: structured (hair traps, rub trees) plus unstructured (telemetry, opportunistic) data, one shared set of activity centres.
- The "consistency test" is Bayesian variable selection: stated aim "to formally evaluate whether estimates of sigma vary by data type" [paraphrase of fetch output; goal sentence quoted there]. Model 5 puts a data-type coefficient theta_2 on the spatial scale sigma, multiplied by w, "a latent binary variable with a Bernoulli prior distribution with probability 0.5." Decision = posterior inclusion probability, Pr(w=1)=0.98 reported as support for a data-type effect. No p-value, no threshold, no formal null.
- It tests whether ONE parameter should be shared or split inside an assumed single latent model. Existence of a common joint is presupposed (shared activity centres). Not equivalent to (ii): it can never return "no common joint exists", because the latent model is always fitted.
- Prior-pass caution holds, and is now settled: Tenan is NOT an owner.

## 3. Per area
1. Integrated population models. Besbeas & Morgan 2014 MEE "Goodness-of-fit of integrated population models using calibrated simulation" [abstract]: simulate from component models, compare discrepancy measures per data set. (i). Gap: GOF of an assumed demographic model. Abadi/Schaub/Plard (IPM assumption violation) [snippet]: accuracy depends on model fit. (i).
2. Integrated SDM. Goldstein, Doser & Pease (J Anim Ecol, DOI 10.1111/1365-2656.70210) [abstract]: "explore a priori and a posteriori tests of data concordance"; tests "fail to usefully differentiate" when joint modelling helps. Test definitions UNREAD; this is the single most dangerous unread ecology source (a priori concordance test may be model-free). Simmonds & O'Hara 2020, Isaac 2020, Fletcher 2019, Pacifici 2019 [snippet]: no compatibility diagnostic found. Doser integrated community occupancy models [snippet]: one shared process model plus per-source observation models, (i). Melding Wildlife Surveys (arXiv 2211.12642) [abstract]: Bayesian Markov melding, (i), no consistency test.
3. Evidence-synthesis conflict (cross-field). Presanis, Ohlssen, Spiegelhalter, De Angelis 2013 Stat Sci 28:376 [skim]: conflict p-value splitting a DAG at a node; "the conflict approach tests prior/likelihood compatibility" and "The various data sources are dependent on shared parameters and hence have the potential to conflict." (i): needs a parametric DAG; tests disagreement about a node, not joint existence. Marshall & Spiegelhalter 2007 node-splitting [snippet], same class.
4. NMA. Bucher 1997, Lu & Ades 2006, Dias 2010 [abstracts/snippets]. Lu-Ades: "consistency as a set of linear relations between effect parameters on the log odds ratio scale", relaxed by inconsistency factors. Loop test: direct AB vs indirect AC - BC. See section 4.
5. Fisheries. Maunder & Piner 2017 Fish Res 192:16 [abstract/secondary]: "conflicting data implies model misspecification" (their law); diagnostic algorithm on a fitted assessment model. (i). Francis 2011 [not retrieved; known to be weighting of fitted indices]. Carvalho 2017 not retrieved.
6. False-positive / multi-method occupancy. Royle & Link 2006, Miller et al. 2011 Ecology 92:1422, 2014 Divers Distrib 20:223 (first multi-source application) [snippets/abstract]: latent occupancy assumed; false positives are parameters, identifiable only via "certain" detections. (i). Nichols 2008 [abstract] (i). Field comparisons (Sabah leech iDNA vs cameras; deer/grouse eDNA vs cameras; indigo snake) compare occupancy of SHARED species ("consistent occupancy estimates") [snippets]; no species-set test.
7. Co-occurrence. Veech 2013 [not read]; Chang et al. 2023 PeerJ 15907 (2x2 table per pair from a presence-absence map; 403 on fetch) [snippet]; Blanchet-Cazelles-Gravel 2020; Laroche & Ehlers 2025 (rank-consistency of presence probabilities across sites under neutral theory) [snippet]; copula/JSDM literature. All model a joint from margins; none asks whether margins from different sources are jointly realisable.
8. Statistical matching. D'Orazio, Di Zio, Scanu 2006; R StatMatch Frechet.bounds.cat [doc snippet]: bounds on cells of a cross-table from two files with only common variables. Nearest mathematical relative (the set of compatible joints is the same polytope), but the stated use is uncertainty width, not an incompatibility test, and the files share anchor variables (here: sites). Capotorti 2011 already on shelf.
9. Searches for "marginal problem", "Bell inequality", "contextuality" with ecology/species: nothing ecological (physics/maths only).

## 4. Closest cross-field analogue: NMA loop inconsistency
Same: closed loop of comparisons (A-B, A-C, B-C), each from a different set of studies, never all observed together; question is whether the pieces cohere around the loop; the loop test is local to a cycle; node-splitting separates direct vs indirect evidence.
Different (exactly): NMA consistency is the linear equation d_BC = d_AC - d_AB on a scale (log OR). Compatible means a solution to a linear system in effect parameters; the joint over potential outcomes of A,B,C never enters and is not constrained (true potential-outcome joints always exist given any margins, because the design is about effects, not shared units). Our constraint is on distributions of binary presence vectors: existence of a probability measure on {0,1}^species with prescribed margins, a polytope with Frechet/Bell-type (non-linear-in-parameters, facet) conditions, and the minimal TV distance is an LP. For a triangle of 2-species margins, a pairwise-compatible cycle can still be infeasible with every equation satisfied. NMA also tests with variance (inconsistency is a random-effect residual); ours is a hard polytope distance. So: structural analogy of cycle shape, NOT sameness. Presanis-type conflict p-values are the Bayesian generalisation of the same linear/parametric kind.

## 5. Search terms used
Tenan 2017 consistency (fetched full HTML); NMA inconsistency loop Bucher node-splitting consistency equation; Lu Ades 2006 / Dias 2010; Presanis 2013 conflict diagnostics DAG; Maunder Piner 2017 data conflicts; Frechet bounds species co-occurrence jointly realisable; integrated SDM data conflict / compatibility / concordance (Isaac, Fletcher, Goldstein); marginal problem / Bell inequality species occurrence; statistical matching Frechet ecology; Besbeas Morgan IPM GOF; eDNA camera acoustic incongruent multi-method consistency; false-positive occupancy Royle-Link Miller.

## 6. Unread sources that could flip the verdict
1. Goldstein, Doser & Pease (J Anim Ecol 2026): test definitions of "a priori concordance". Top priority.
2. Markov melding (Goudie et al. 2019 Stat Med; "Melding wildlife surveys", arXiv 2211.12642): melding requires compatible marginals on shared quantity; check whether a compatibility check or pooled-prior conflict is stated model-free.
3. Francis 2011, Carvalho 2017 (fisheries data conflict) full text.
4. Veech 2013/2014; HMSC (Ovaskainen 2017) for any pairwise-table realisability check.
5. Plard-Turek-Schaub IPM review and Schaub-Abadi 2011 IPM: unconditional model-checking.
6. Statistical matching in official statistics: papers using Frechet bounds to test incompatibility of two files (Conti, Marella, Scanu; "uncertainty in statistical matching"), possibly with an eps relaxation (coherence/de Finetti line: Capotorti-Vantaggi). Cross-field owner risk for (a), not ecology.
7. Imprecise-probability "avoiding sure loss" / coherence checks in applied use.

## Addendum 2026-11-05: top-risk sources read (SFU proxy, browser)
- **Goldstein, Doser, Pease & Pacifici 2026, J Anim Ecol, doi:10.1111/1365-2656.70210 [full text, main body; appendices B/C unread].**
  It is NOT an owner. The "a priori" concordance tests are ad hoc summaries: correlations of counts, cross-regression
  slopes, separate GLMs on a covariate. The "a posteriori" tests are posterior predictive checks, cross-validation, and
  joint-vs-single parameter comparison. All of them assume one shared process model (type (i)), and none reliably
  separates concordant from discordant data.
  - Key stance (theirs): concordance "is not meaningful outside of the context of a particular joint model".
  - Their call: "we encourage statistical ecologists to pursue such tests in future work".
  - Structural point (ours, owned mathematics: Vorob'ev 1962; Beeri–Fagin–Maier–Yannakakis 1983). Their setting is
    two datasets on one species. That context hypergraph is acyclic, and for acyclic hypergraphs agreement on shared
    margins already guarantees a joint. So a model-free joint-existence test **has nothing to test** in their setting.
    It becomes informative only with ≥ 3 methods whose species sets overlap round a loop. That is why the ecology
    question needs a design with a loop. It also explains why the ecology literature, which works with two datasets,
    would not have met the question.
- **Markov melding for wildlife surveys (arXiv:2211.12642) [abstract]:** an integration method. The abstract states no compatibility test.
- **Conti–Marella–Scanu (statistical matching) [abstract/snippets]:** measures uncertainty over the Fréchet class.
  They mention no incompatibility test. **Capotorti–Vantaggi 2011 (on shelf) [intro read]:** checks whether
  separately collected sources are jointly coherent and corrects incoherence by distance minimisation. This is a
  cross-field owner of the ε*-type computation, as expected, and is not ecological.
- **Updated verdict:** (a) a model-free cross-method compatibility test in ecology is NOT FOUND. The nearest ecology
  paper read in full explicitly lists such tests as missing future work. The mathematics is owned (CbD/DKC 2020,
  Capotorti–Vantaggi, Vorob'ev). Still unread: Francis 2011 and Carvalho 2017 (fisheries data weighting, almost surely
  type (i)); Goldstein appendices B/C.
