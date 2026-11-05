# Prior art: epsilon*(t) as a seizure early-warning / "views stop gluing" measure

reviewed: false. 2026-11-04. Scout pass, standard web search plus 4 shelf PDFs. Shelf grep (SHELF_INDEX, taxonomies) for
Jirsa/McIntosh/Epileptor/seizure/Scheffer/Higham/Schneidman: NO hits before this pass.
Read levels: SKIM = abstract + selected paragraphs of downloaded PDF; SNIPPET = search-result summary only (unverified);
NOT READ. Nothing here was read in full.

## 1. Jirsa/McIntosh line
- Jirsa, Stacey, Quilichini, Ivanov, Bernard, Brain 2014 (Epileptor): "established a taxonomy of seizures based on first principles" [SNIPPET].
  Five-variable model; slow permittivity variable z; seizure onset = trajectory meeting separatrix. Checks one model against
  data; no test that windowed/partial views are mutually consistent with one state. NOT FOUND (as such).
- Saggio et al., eLife 2020 (dynamotypes): "evidence of all 16 dynamotypes predicted" in >2000 seizures [SNIPPET]. Classifies
  onset/offset bifurcations per seizure; no cross-window consistency test. NOT FOUND.
- Virtual Epileptic Patient (Jirsa et al. NeuroImage 2017; Hashemi et al. 2021 Bayesian inversion): fits Epileptor networks
  to SEEG with identifiability/posterior-predictive diagnostics [SNIPPET]. Model-fit consistency, not pairwise-view gluing. NOT FOUND.
- Pillai & Jirsa 2017 (structured flows on manifolds), McIntosh/Jirsa 2020s: search returned nothing; NOT READ, status UNKNOWN.
- Meisel & Kuehn 2012 (PLoS ONE, seizures as critical transitions): inverse variance scales linearly near seizure; also compares
  cross-correlation and mean phase coherence between regions [SNIPPET]. Nearest ancestor of a between-channel EWS; not a
  gluing/consistency measure.

## 2. Early-warning signals
- Scheffer 2009 framework [SNIPPET]. Maturana, Meisel et al., Nat Commun 2020: variance/AC1 fluctuate over hours-days, claimed
  forecasting use [SNIPPET].
- Wilkat, Rings, Lehnertz 2019 (shelf): "found no evidence for critical slowing down prior to 105 epileptic seizures" [SKIM,
  abstract]. Surrogate-based sensitivity/specificity. KNOWN FAILURE: any new EWS must pass this surrogate test.
- Channel-pair network EWS (Chaos 2021 seizure-onset transition networks) [SNIPPET, unverified].
- No EWS found built on consistency of pairwise statistics across windows or on non-PSD of assembled matrices. NOT FOUND
  (negative from two searches, not exhaustive; Kuehn's network-EWS papers NOT READ).

## 3. Pairwise consistency in neuroscience
- Non-PSD from pairwise-complete estimation and Higham 2002 nearest-correlation repair: standard numerics [SNIPPET]. No neuro
  paper using the repair DISTANCE as a signal found (one search). Closest owner of the construction: nearest-correlation
  distance = a Frobenius analogue of eps* for the Gaussian/second-moment relaxation. PARTLY (for Gaussian level).
- Liégeois et al. 2017 (shelf): "statistical rejection does not necessarily imply non-stationarity, but can also be due to
  nonlinearity or non-Gaussianity" [SKIM abstract]; HCP: stationary Gaussian null mostly not rejected. dFC non-stationarity
  tests OWN the "windows disagree" question for second moments; any eps*(t) must beat PR/ARR surrogates.
- Schneidman et al. 2006 (shelf): "weak correlations between pairs of neurons coexist with strongly collective behavior" and
  pairwise max-ent models fit retina [SKIM abstract]. Cortex fits worse (Ising model, cat V1, 2012 [SNIPPET]). Pairwise max-ent
  = existence of a joint matching pairwise margins; so max-ent fit quality is the same-context cousin of eps*.
- Higher-order: Rosas et al. 2019 O-information (shelf) [SKIM first page]. Synergy near seizure onset: Granger synergy study
  (arXiv:1403.5156), interaction information in epileptogenic zone (arXiv:1404.6836), O-information in rat TLE (eNeuro 2025),
  Gaussian O-information inaccurate in absence seizure [all SNIPPET]. Higher-order structure near seizures is OWNED as a theme;
  these are same-window joint measures, not cross-context gluing.

## 4. Contextuality / marginal problem on neural data
- Abramsky-Brandenburger sheaf framework, CbD: no application to neural recordings found [SNIPPET, one search]. NOT FOUND.
  Quantum-like cognition literature NOT searched. Marginal-problem / compatible-marginals tests in neuro (Kellerer-type): NOT searched.

## Verdict
Genuinely new as a PACKAGE; each ingredient has an owner: (a) variance/AC1/cross-correlation EWS (Meisel-Kuehn, Maturana),
(b) dFC stationarity surrogates (Liégeois), (c) nearest-correlation distance (Higham) at second-moment level, (d) pairwise
max-ent (Schneidman), (e) distance to marginal polytope (Berrett-Samworth, already noted in the theory file).
Key risk, as flagged: with simultaneous recording a joint exists per window, so eps*(t) > 0 arises only from combining
windows and reduces to a non-stationarity measure, competing with (b). Not claimed.
Non-redundant only if: (i) it uses the FULL binary/categorical marginal polytope (beyond second moments, so it sees what
Higham and Gaussian dFC null cannot, e.g. parity-type twists); (ii) it is compared head-to-head with variance, AC1, cross-
correlation, and a Higham-distance baseline under the Wilkat surrogate protocol (sensitivity/specificity), with eps* calibrated
as a non-stationarity budget, i.e. eps*(t) beyond what stationary surrogates give; (iii) it beats the baselines or captures
a different seizure subset. Otherwise: renamed non-stationarity measure. Honest distance: binary-threshold EEG discards
most information; the V/L bound is for binary cycles only.
