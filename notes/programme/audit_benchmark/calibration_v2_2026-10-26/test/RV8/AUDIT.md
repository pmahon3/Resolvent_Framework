## Audit: seed.md — expository article on the solution of sphere packing in dimensions 8 and 24 (mode: full)

Audit date (per AS_OF.md): **2016-11-04**. Only sources dated on or before that day count as prior art. The seed is the submission, so any later version of it is ignored.

### Declared contribution type(s): Type 6 (exposition / translation)
The seed names a type. It does not spell out the per-type bars it commits to. It does name an audience ("a general mathematical audience"), an intended use ("read before the technical papers") and a distinctive angle ("which ingredients are new and which are classical"). That is enough to evaluate.

### Sources consulted (read level, date)
- M. Viazovska, "The sphere packing problem in dimension 8", arXiv:1603.04246, March 2016. Read level: abstract and main theorem, from recall plus search snippet. Predates audit date.
- H. Cohn, A. Kumar, S. D. Miller, D. Radchenko, M. Viazovska, "The sphere packing problem in dimension 24", arXiv:1603.06518, March 2016. Read level: abstract, from recall and search snippet. Predates.
- H. Cohn, N. Elkies, "New upper bounds on sphere packings I", Ann. of Math. 157 (2003). This is the linear programming bound. Read level: known statement, from recall. Predates.
- D. de Laat, F. Vallentin, "A breakthrough in sphere packing: the search for magic functions", arXiv:1607.02111, submitted 2016-07-07, for Nieuw Archief voor Wiskunde. It is expository and includes interviews with Cohn, Kumar, Miller and Viazovska. Read level: arXiv abstract page fetched 2026-10-26. **Predates; this is the closest prior exposition.**
- E. Klarreich, "Sphere packing solved in higher dimensions", Quanta Magazine, 2016-03-30. It is popular-level, not for a mathematical audience. Read level: from recall only; I did not re-fetch it in this run. I am confident of the March 2016 date.
- Blog expositions from spring 2016 (e.g. Kalai, Baez). Read level: recall only, not verified in this run. They are informal and scattered.
- Not usable: post-2016 sources returned by the search, such as arXiv:2207.06913 and 2604.23468. They were ignored under AS_OF.

### Pure Verdict: KNOWN (not a Type 1 claim)
No new theorem is claimed. The content is Viazovska (2016), CKMRV (2016) and Cohn–Elkies (2003), all in print or preprint before the audit date. This is correct and expected for a Type 6 seed, and it is not a defect.

**Correctness:** I found no problem in the seed's statements. Dimension 8 (E8) came first and dimension 24 (Leech) a week later. The method is the LP bound, Fourier analysis and a modular-form magic function. All of this matches the sources. The seed is one paragraph, so its accuracy can only be checked at this level.

### Applied Verdict: not evaluated
The seed makes no methodology claim, so the applied check does not apply.

### Contribution Type Verdicts
**Type 6 (exposition / translation): FAIL under the programme bar (narrowly). It would PASS at the right venue under community standards.**
- (a) Audience: named. It is general mathematicians who are not specialists in modular forms or discrete geometry. **Met.**
- (b) Inaccessible literature: the technical papers need modular forms (quasimodular forms, Eisenstein series, Laplace-transform tricks) together with Fourier analysis of radial Schwartz functions. That is real prerequisite depth for the named audience. **However**, de Laat–Vallentin (July 2016) already gives an English exposition of the same two results for a general mathematical readership, with the magic-function framing and author interviews. Quanta covers the lay level. The programme's park clause, "the existing literature is already accessible to the target audience", is therefore partly triggered. The seed does not say how it differs from de Laat–Vallentin. **Partly met.**
- (c) Non-trivial conceptual work: the stated angle, separating the new ingredient (building the eigenfunction from modular forms) from the classical ones (LP bound, Poisson summation), is real organisational work. It goes beyond changing notation. The seed asserts this but does not demonstrate it. **Plausibly met.**

The programme bar is strict: an accessible prior exposition to the same audience means park. On that reading the seed fails on (b), unless it shows added value over de Laat–Vallentin.

### Cross-reference
Every component is known (pure KNOWN), as it should be for an exposition. The only live type is 6. It turns on differentiation from one existing exposition that appeared four months earlier. Nothing here is a Type 3 or Type 4 claim.

### Recommendation
**Redirect to an expository venue.** For the programme's purposes, park this as a programme contribution: it was evaluated on Type 6, and bar (b) failed because the de Laat–Vallentin exposition already exists. If pursued, it should cite de Laat–Vallentin explicitly and state what it adds: the new-versus-classical ledger, and a read-first route through the LP bound.

Bearing on WHY.md (one line): there is none directly. It is a case of local certificates (an auxiliary function) proving a global optimum, which is at most a lens.

### Referee estimate: ACCEPT-LIKELY
Venue class: expository (Notices / Bulletin / Monthly-type)
Value carried by: factor 4 (exposition that makes a fresh, technical result usable for a neighbouring audience. An expert who knows which ingredients are new can give an organisation that the earlier piece lacks.)
Main risk a referee would raise: overlap with de Laat–Vallentin (arXiv:1607.02111, July 2016), which must be credited and differentiated from. A secondary risk is the accuracy and fair credit in the "new versus classical" attributions (Cohn–Elkies, earlier LP work, the modular-forms tools).
