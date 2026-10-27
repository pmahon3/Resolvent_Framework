## Audit: seed.md (mode: full)

**Audit date (AS_OF.md): 2011-01-31.** Only sources on or before that date count as prior art. The seed is the submission and is not prior art. Read levels: **A** = abstract or metadata only (this session, 2026-10-26, via web search); **K** = known from background, not re-read this session. All post-2011 search hits were discarded.

### Declared contribution type(s): Type 3 (unifying framework), Type 4 (vocabulary)
The seed declares types but does not state the per-type bars it commits to clearing. The framework requires that statement, so I note the gap here.

### Pure Verdict: UNCLEAR, leaning NOVEL on two items, KNOWN on the frame
Stripped of vocabulary, the seed makes five claims:

1. **"Contextuality = no global section of a presheaf over contexts."** This is KNOWN for Kochen–Specker. Butterfield–Isham, "A topos perspective on the Kochen–Specker theorem I", IJTP 37 (1998) 2669, arXiv quant-ph/9803055 [A, 1998]. That paper shows KS is equivalent to the spectral presheaf having no global elements. The seed has to credit it. What the seed adds is the step from the deterministic, operator-algebraic presheaf to a presheaf of *distributions* on an abstract measurement cover.
2. **"Non-locality is the same obstruction."** The core is KNOWN. Fine, PRL 48 (1982) / J. Math. Phys. 23 (1982) [K] shows that a factorizable LHV model exists iff a global joint distribution reproducing the marginals exists. The marginal problem goes back to Vorob'ev, Theory Probab. Appl. 7 (1962) [K]. Pitowsky, *Quantum Probability – Quantum Logic* (1989) [K] covers correlation polytopes for general compatibility structures. That Bell non-locality is contextuality on a product cover is folklore (Mermin, RMP 65 (1993) [K]). Brandenburger–Yanofsky, J. Phys. A 41 (2008) 425302, arXiv 0711.4650 [A, 2007/2008] already treats EPR, Bell and KS in one abstract probabilistic classification. Abramsky, "Relational hidden variables and non-locality", arXiv 1007.2754 (v1 16 Jul 2010) [A] already has the possibilistic (relational) setting. It is prior art: it is a separate earlier paper, not the seed. Only its v1 counts; later revisions do not.
3. **"Linear-algebraic method for computing the obstruction."** As stated this is KNOWN in substance: deciding LHV existence is an LP or linear system over the marginal map (Pitowsky 1989 [K]; Bell-polytope literature, e.g. Barrett et al., PRA 71 (2005) 022101 [K]). Novelty depends on details the seed does not give.
4. **"Rank Bell, Hardy, GHZ by strength."** The informal distinctions are KNOWN: "without inequalities" (Hardy, PRL 71 (1993) [K]) and "all-versus-nothing" (GHZ 1989; Mermin 1990 [K]). I found no pre-2011 source that defines a formal strict hierarchy (probabilistic ⊋ possibilistic ⊋ strong) for arbitrary scenarios and proves it strict. Potentially NOVEL.
5. **"Negative-probability LHV ⟺ no-signalling."** No pre-2011 statement found. Searches returned only post-2011 work, which is discarded. One later paper attributes an observation to Barrett and Short, but I could not confirm its date: **undetermined whether it predates 2011-01-31.** Spekkens, PRL 101 (2008) 020401 [K] links negativity to preparation/measurement contextuality, a different notion. Potentially NOVEL as a clean theorem. A hostile expert might call it linear-algebra folklore, because compatible marginals always admit a signed extension.

**Correctness.** No problem is visible at seed resolution. Claim 5 is plausible: no-signalling is exactly compatibility of the presheaf, and compatible families have signed global sections. That still needs proof for general covers, not only Bell covers. Claim 3 is under-specified and cannot be checked.

### Applied Verdict: not evaluated (no Type 7 claimed; no computational comparison offered)

### Contribution Type Verdicts (mode=full):
**Type 3 (unifying framework): UNCLEAR, leaning PASS.** The unification of non-locality and contextuality is itself owned (Fine / Butterfield–Isham / folklore). The bar is method transfer, and two transfers are visible:
- (a) Bell-scenario notions (no-signalling, Hardy/GHZ-type arguments) become stateable and testable for arbitrary KS-type covers.
- (b) A single signed-measure theorem covers both.

The seed asserts these and does not demonstrate them. It passes only if the paper shows a technique moving across, e.g. a Hardy- or GHZ-type strength classification of a genuine KS scenario. "These look alike" alone would fail.

**Type 4 (vocabulary): PASS (provisional).** Three-statements test:
1. "Scenario X is possibilistically but not strongly contextual": a support-presheaf condition, uniform across covers.
2. "Strong contextuality: the support presheaf has no global section at all": GHZ yes, Hardy no.
3. "An empirical model is no-signalling iff it has a signed global section", on arbitrary covers.

Standard vocabulary (Fine/Pitowsky) can say "joint distribution exists" but has no uniform names for (1) and (2). The non-trivial results are the strict hierarchy and claim 5. This passes provided both are proved and the central object is credited to Butterfield–Isham and Fine.

### Cross-reference
The components are known: the presheaf obstruction (1998), the joint-distribution criterion (1982), and the LP method (1989). The new content is the assembly into a *graded* vocabulary (probabilistic / possibilistic / strong) plus the signed-measure theorem. Type 4 carries the item and Type 3 depends on demonstration. If the paper claims to have *originated* the global-section view of contextuality, that is a novelty claim the literature contradicts.

### Recommendation
**Proceed to Phase 3, scoped to Type 4** (Type 3 conditional on one demonstrated transfer to a non-Bell scenario). Owed before claiming:
- credit Butterfield–Isham 1998, Fine 1982, Vorob'ev 1962, Pitowsky 1989, Brandenburger–Yanofsky 2008 and Abramsky 2010;
- do not claim the linear-algebraic method as new unless it differs from the LP / marginal-polytope test;
- settle the Barrett–Short attribution for claim 5.

**WHY line.** This is a direct instance of the programme's question. Local views (context marginals), each correct as far as it goes, may fail to glue into one world, and the hierarchy grades how badly. It is a lens on the question, not an answer to it.

### Referee estimate: ACCEPT-LIKELY
Venue class: research journal
Value carried by: factor 3 (organising framework yielding new statements: the strength hierarchy, and signed sections ⟺ no-signalling), with factor 1 secondary
Main risk a referee would raise: the global-section obstruction is already Butterfield–Isham 1998 and Fine 1982. The paper must credit them and show the hierarchy and signed-measure theorem are more than reformulation.
