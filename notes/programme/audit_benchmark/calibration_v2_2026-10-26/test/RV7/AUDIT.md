## Audit: seed.md, expository article on MCMC and convergence rates (mode: full)

Audit date (per AS_OF.md): 2008-01-01. Only sources dated on or before 2008-01-01 count as prior art. The seed's own text is treated as the submission. Searches run 2026-10-26, standard mode.

### Declared contribution type(s): Type 6 (exposition / translation)
The type is declared. The per-type bars the seed commits to are only implicit: the audience is named ("mathematicians who are not specialists in probability"), but the seed is a five-sentence abstract. It does not name the inaccessible literature, and it does not describe the conceptual work of translation. This is a readiness gap for Phase 2.

### Pure Verdict: KNOWN (by design; no theorem claimed)
After stripping the vocabulary, the content is a review of known material:
- how MCMC algorithms work (Metropolis, Gibbs, Glauber-type chains) on examples from statistics, physics and combinatorics;
- known convergence-rate results;
- known techniques for proving them (spectral and Dirichlet-form methods, geometric/Cheeger/canonical-path bounds, coupling, Nash and log-Sobolev inequalities, representation theory).

No new statement is claimed, so there is nothing to kill. Pre-2008 sources covering the material:
- Diaconis, *Group Representations in Probability and Statistics*, IMS Lecture Notes 11, 1988. Read level: known from memory, not re-read. Covers representation-theoretic rates (shuffles, random walks on groups).
- Saloff-Coste, "Lectures on finite Markov chains", Saint-Flour 1996, Springer LNM 1665, 1997. Read level: memory, not re-read. Covers Dirichlet forms, Nash and log-Sobolev inequalities, comparison.
- Diaconis & Saloff-Coste, "What do we know about the Metropolis algorithm?", J. Comput. System Sci. 57 (1998) 20–36; STOC 1995 version. Read level: abstract and bibliographic data via search (https://pi.math.cornell.edu/~lsc/papers/Whatdwk.pdf). It surveys rigorous running-time results for Metropolis across physics, CS, probability and statistics. **This is the closest prior exposition.**
- Montenegro & Tetali, *Mathematical Aspects of Mixing Times in Markov Chains*, Found. Trends TCS 1(3), 2006, 237–354; arXiv math/0410545 (2004). Read level: front matter and abstract via search. Covers spectral, entropy and isoperimetric (conductance, evolving sets) methods and lower bounds. It omits coupling by design and is aimed at theoretical CS.
- Jerrum, *Counting, Sampling and Integrating: Algorithms and Complexity*, Birkhäuser 2003. Read level: memory. Covers the combinatorics and CS side (canonical paths, coupling, approximate counting).
- Aldous & Fill, *Reversible Markov Chains and Random Walks on Graphs*, draft monograph online since the 1990s. Read level: memory. It is an unpublished draft, so accessibility to outsiders is limited.
- Levin, Peres & Wilmer, *Markov Chains and Mixing Times*. Read level: memory. Drafts circulated online before 2008, but the AMS book appeared in late 2008. **I could not confirm that the published version predates 2008-01-01, so it is treated only as a circulating draft.**
- Robert & Casella, *Monte Carlo Statistical Methods*, Springer 1999/2004, and Liu, *Monte Carlo Strategies in Scientific Computing*, Springer 2001. Read level: memory. These cover the statistics-practice side and are largely non-quantitative on rates.

### Applied Verdict: not evaluated (no method, algorithm or computational claim; Type 7 not declared)

### Contribution Type Verdicts (mode=full only):
**Type 6 (Exposition / translation): UNCLEAR**, with a conditional pass on (a) and (b) and (c) undemonstrated.
- **(a) Audience: MET.** Research mathematicians outside probability.
- **(b) Inaccessible literature: PARTLY MET.**
  - The rate results are scattered across four communities: statistics, statistical physics, theoretical CS and probability. Each existing survey is written for one community: Montenegro–Tetali for TCS, Saloff-Coste for Saint-Flour-level probabilists, Jerrum for complexity theorists, Robert–Casella and Liu for statisticians.
  - No pre-2008 source I found is a short, cross-field synthesis for general mathematicians.
  - The partial exception is Diaconis–Saloff-Coste 1998. It is cross-field, but it is limited to Metropolis, it is in a CS journal, and it is ten years older than the submission.
  - Being scattered across sources is an accepted ground under the framework's bar.
- **(c) Non-trivial conceptual work: NOT DEMONSTRATED.**
  - An abstract cannot show it. The test is whether the article organises the techniques by what they buy for a working mathematician (geometry, analysis, algebra, coupling), with worked examples of each, rather than listing results.
  - It must also add something beyond Diaconis–Saloff-Coste 1998 and Montenegro–Tetali 2006.
- **Programme park condition** ("well-explained in [textbook], Chapter N"): **not triggered** for this audience as of 2008-01-01, given the LPW date uncertainty above.

**Undeclared types:** none implied. The phrase "reviews what is known" makes no Type 1–5 claim.

### Cross-reference
All components are known by construction. The contribution, if any, is the synthesis and the reach across fields. The pure KNOWN verdict is expected for a Type 6 seed and does not count against it. The Type 6 verdict depends entirely on (c), which needs the full text.

### Recommendation
**Redirect to an expository venue** (Bulletin of the AMS, SIAM Review survey track, or Notices). The seed is conditional on a full draft showing (c):
- explicit positioning against Diaconis–Saloff-Coste 1998 and Montenegro–Tetali 2006;
- worked examples drawn from all three fields.

For the programme it is not a contribution to proceed with under Types 1–5. If the full text shows only notation-level restatement of the existing surveys, park it as Type 6 FAIL (bar (c)).

How it bears on WHY.md: tangential. MCMC is a lens on how local update rules produce a global distribution with no central sampler, which is order from local relations. This has no bearing on any bar.

### Referee estimate: ACCEPT-LIKELY
Venue class: expository (Bulletin of the AMS, or a survey venue)
Value carried by: factor 4 (it synthesises scattered recent work from statistics, physics and combinatorics/CS, and translates it for a neighbouring audience of non-probabilist mathematicians)
Main risk a referee would raise: overlap with existing surveys (Diaconis–Saloff-Coste 1998, Montenegro–Tetali 2006, Saloff-Coste 1997, the circulating Levin–Peres–Wilmer draft); the article must add organisation and reach, not repeat them.
