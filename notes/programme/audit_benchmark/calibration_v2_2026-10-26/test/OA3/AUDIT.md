## Audit: seed.md, graph invariants as bounds for Bell/noncontextuality scores (mode: full)

**Audit date (AS_OF.md): 2014-01-27.** Only sources dated on or before that day count. The seed's own text is the submission. Preprints, talks or versions of the seed's own work (e.g. any 2010 arXiv preprint carrying this result, or a QIP 2011 abstract of it) are ignored as prior art. Search date: 2026-10-26. Read levels: **[P]** primary text read this session; **[A]** abstract or metadata only, read this session; **[S]** a secondary description seen in search results; **[R]** recalled from background knowledge, not re-read this session (the PDF text could not be extracted).

### Declared contribution type(s): Type 3 (unifying framework), Type 4 (vocabulary)
The types are declared. The per-type bars the seed commits to clearing are **not** stated, as framework §"Phase 1 requirement" asks. This is a procedural gap, not a fatal one.

### Pure Verdict: NOVEL (ingredients owned)
The audited statement is the seed's claim about the scores of physical theories, not a graph equality. Its mathematical core is KNOWN: every equality is Lovász/GLS/Knuth restated. The identification has no pre-2014 owner outside the seed's own work.

**Stripped statement.** Let G be a graph on events, with edges for exclusivity, and let w ≥ 0 be weights.
(i) max Σ wᵢ pᵢ over deterministic {0,1} assignments with no two adjacent events both true = α(G,w).
(ii) max Σ wᵢ ⟨ψ|Πᵢ|ψ⟩ over projectors with Πᵢ ⊥ Πⱼ on edges = ϑ(G,w).
(iii) max over pᵢ ≥ 0 with Σ_{i∈C} pᵢ ≤ 1 for every clique C = α*(G,w), the fractional packing number (an LP).
(iv) For every G, the set {(⟨ψ|Πᵢ|ψ⟩)ᵢ} over such projectors is TH(G).

**What is owned:**
- (i) is immediate. The noncontextual deterministic assignments are exactly the indicator vectors of independent sets, so this is folklore.
- (ii) is, once rank-1 projectors are reduced to unit vectors, literally Lovász's characterisation of ϑ: the maximum of Σ (c·uᵢ)² over orthonormal representations, with a "handle" c. Source: Lovász, "On the Shannon capacity of a graph", IEEE Trans. Inf. Theory 25 (1979) [R; 1979, predates]. The weighted form and the projector form come from Grötschel–Lovász–Schrijver, "Relaxations of vertex packing", JCTB 40 (1986), and GLS, *Geometric Algorithms and Combinatorial Optimization* (1988), Ch. 9 [S: TH(G) introduced in GLS 1986, confirmed by search; theorem numbers R].
- (iv) is the GLS/Knuth description of TH(G) through orthonormal labelings and a unit cost vector, read physically: ψ is the handle and Πᵢ the labeling. Source: Knuth, "The Sandwich Theorem", Electron. J. Combin. 1 (1994) #A1, arXiv math/9312214 [A: date and contents confirmed; the exact lemma is R, because the PDF text could not be extracted]. Two points need checking. Is the set exactly TH(G), or its convex hull / down-closure? Is "exists an experiment" doing the work of choosing the dimension?
- (iii) α* is the classical fractional relaxation, QSTAB in GLS. The same three-tier pattern already appears in zero-error information theory:
  - unassisted capacity uses α;
  - entanglement-assisted capacity is bounded by ϑ: Beigi 2010, arXiv 1002.2488 [R]; Duan–Severini–Winter, arXiv 1002.2514, IEEE IT 2013 [R];
  - no-signalling-assisted capacity is given by linear programs. Cubitt–Leung–Matthews–Winter, arXiv 1003.3195, IEEE IT 2011 [A: submitted 16 Mar 2010; abstract gives "linear programming formulas" and ties them to Shannon's feedback-assisted zero-error capacity, which is Shannon's 1956 fractional-packing quantity (R)].
  - KS sets are used as graph gadgets in Cubitt–Leung–Matthews–Winter, "Improving zero-error classical communication with entanglement", arXiv 0911.5300, PRL 2010 [A].
- Physics antecedents:
  - Wright, "The state of the pentagon. A nonclassical example", in Marlow (ed.), *Math. Foundations of Quantum Theory*, Academic Press 1978, pp. 255–274 [S]: the pentagon's non-quantum state.
  - Klyachko–Can–Binicioğlu–Shumovsky, PRL 101, 020403 (2008), arXiv 0706.0126 [P, ar5iv HTML, read 2026-10-26]: the pentagram inequality, with quantum value √5 obtained by "a simple calculation" and framed through the marginal problem, the Vorob'ev–Kellerer cone and Fine. It does **not** mention Lovász, ϑ, the independence number, Shannon capacity or orthonormal representations. It is the closest non-seed antecedent, and it does not own the identification.

**What is not owned (at 2014-01-27).** I found no source before 2014-01-27, other than the seed's own work, that identifies the maximum quantum score of a general Bell or noncontextuality test with ϑ of its exclusivity graph. The later works I located build on the seed's preprint and cite it:
- Acín–Fritz–Leverrier–Sainz, arXiv 1212.4084, 17 Dec 2012 [A]. It explicitly "refines the approach by Cabello, Severini and Winter".
- The 2012–13 exclusivity-principle and local-orthogonality papers [R].
These predate the audit date and are by other authors. They cite and refine the seed's own preprint, so under AS_OF ("ignore … citations … of the seed's own work") they are not counted against it. This is a judgement call, flagged here. AFLS is nonetheless the referee's evidence for scope problem 2 below (normalisation and clique exclusivity).

**Hostile reading.** A combinatorial optimiser would call (ii)–(iv) "Lovász/GLS with the words changed". The theorem content is a dictionary entry. The novelty is the dictionary (tests → graphs, behaviours → points of STAB / TH / QSTAB), not a new inequality about graphs.

**Correctness and scope problems a referee would flag:**
1. **"The maximum score is ϑ" needs scoping.** ϑ(G,w) is always an upper bound. It is attained only when the test's physical constraints (fixed parties and locality in a Bell scenario, fixed measurement contexts, fixed dimension) allow the Lovász-optimal orthonormal representation. For a *given* Bell test, ϑ of the exclusivity graph can be a strict upper bound. The seed's own sentence "for every graph there is an experiment" is the correct form; the first sentence overstates it.
2. **GPT = α* depends on an assumption.** The clique constraints Σ_{i∈C} pᵢ ≤ 1 hold only if every clique of pairwise-exclusive events is *jointly* exclusive, i.e. the clique is itself a context. A GPT obeying only pairwise exclusivity gives the weaker edge LP. So "the general-probabilistic-theory bound" is α* under a stated exclusivity axiom, not for GPTs in general. AFLS (Dec 2012) refines exactly this point.
3. **Rank.** Projectors of rank > 1 and mixed states must be shown not to exceed ϑ. This is standard (TH(G) is convex and closed under the projector form) but must be stated.

None of these makes the core identification wrong. All three are scope repairs.

### Applied Verdict: not evaluated (Type 7 not claimed; informal practitioner note below)
Decision test: yes. A practitioner who designs Bell or contextuality tests gets the quantum maximum of any weighted test from one polynomial-time SDP (ϑ), without running the NPA hierarchy or a dimension search. The classical bound comes from α (NP-hard, but small cases are easy), and the gap is visible at once.
Practitioner hostility, "I already use NPA": NPA gives bounds for a *fixed* scenario. ϑ gives a scenario-free bound and tells you which graphs can show any quantum violation at all. No computational comparison is offered in the seed.

### Contribution Type Verdicts (mode=full):

**Type 3 (Unifying framework): PASS (programme bar), carried by what the seed itself states.**
The bar is concrete method transfer. The seed's own claims deliver three transfers:
- (a) **Computation.** "Quantum maximum = ϑ(G,w)" turns the GLS polynomial-time SDP/ellipsoid computation of ϑ into an algorithm for the quantum maximum, over all realisations, of any weighted test. The α* LP gives the GPT bound.
- (b) **Ordering.** The seed's three tiers are exactly the sandwich α ≤ ϑ ≤ α*. Known graph families that separate these invariants therefore separate classical, quantum and GPT.
- (c) **Realisation.** "For every graph, some experiment's quantum behaviours = TH(G)" brings the GLS/Knuth convex geometry of TH(G) in as the exact quantum set.
This is transfer, not analogy. The seed still has to write these out: its closing sentence ("links graph invariants to physically observable quantities") on its own reads as pattern-noting.

Strengthenings derived by the auditor (the seed does not show them, and should):
- **Imperfection criterion.** G is perfect iff α(G,w) = ϑ(G,w) for all w, iff STAB = TH = QSTAB (GLS 1986). Add the Strong Perfect Graph Theorem (Chudnovsky–Robertson–Seymour–Thomas, Ann. Math. 164, 2006 [R]). Then *some* experiment with exclusivity graph G shows a quantum violation for some weights iff G contains an odd hole or an odd antihole. The pentagon is minimal for structural reasons.
- **Product and Shannon-capacity techniques** (ϑ multiplicativity) for repeated tests. Sketch only.

**Type 4 (Vocabulary / infrastructure): PASS (programme bar), with a priority caveat.**
"Exclusivity graph of a test", together with "score = weighted sum over its vertices", supports these statements:
1. "There exist an experiment and weights with exclusivity graph G that show a quantum violation iff G is imperfect." For a *fixed* test T, only "Ex(T) perfect ⇒ no violation" holds, since ϑ is only an upper bound. This statement is derived by the auditor.
2. "The quantum behaviours of the canonical experiment for G are exactly TH(G)."
3. "The quantum maximum over all realisations of a weighted test on G is computable in polynomial time to any precision, while its classical bound α(G,w) is NP-hard." This is a complexity separation stated at the level of tests.
Before 2014 these could not be stated cleanly in standard foundations vocabulary (Greechie diagrams and orthogonality hypergraphs existed, but without the score/weight-to-graph-invariant map).
Non-trivial result: statement 2, the theta-body realisation, which the seed states. Statement 1 is non-trivial via GLS and the SPGT, but the auditor derived it.
Caveat: orthogonality graphs as such are owned (Kochen–Specker-style graphs; Greechie diagrams; Wright 1978). The new infrastructure is the weighted-score dictionary, not the graph itself.

### Cross-reference
The components are known and the assembly is new. Mathematically, every equality is Lovász (1979), GLS (1986/88), Knuth (1994) or the fractional relaxation. Type 1 therefore fails as a graph-theory theorem. The physical identification and its consequences are new at the audit date. A parallel α/ϑ/LP triad in zero-error information theory (Shannon 1956; Beigi; Duan–Severini–Winter; Cubitt–Leung–Matthews–Winter 2010–11) shows that the pattern was in the air in quantum information. It does not show that it had been transferred to Bell or contextuality scores. Types 3 and 4 clear because the dictionary lets owned theorems (perfect-graph theory, the SDP for ϑ, the sandwich ordering) answer new physics questions.

Bearing on WHY.md: this is the canonical "local views (contexts/cliques) vs. one world (an independent set, i.e. a global assignment)" picture. Its loop structure is the odd-hole/antihole obstruction.

### Recommendation
**Proceed (Phase 3), scoped to Types 3 and 4.** Required before drafting:
- (1) state per-type bars;
- (2) exhibit the transfers (a)–(c) explicitly, and ideally the imperfection criterion;
- (3) scope "maximum = ϑ" as an upper bound attained by some experiment, not by every test;
- (4) state the clique-exclusivity axiom behind α*;
- (5) credit Lovász / GLS / Knuth for the mathematical equalities, and the zero-error triad as precedent;
- (6) verify the exact TH(G) characterisation and its convex-hull/dimension conditions in GLS Ch. 9 or Knuth (read level R here).

### Referee estimate: ACCEPT-LIKELY
Venue class: short-note or letters
Value carried by: factor 3 (a framework that organises known Bell/KS inequalities and yields new tools: an SDP quantum bound, the imperfection criterion, the TH(G) realisation); factor 1 secondarily (the theta-body realisation theorem)
Main risk a referee would raise: "maximum = ϑ" overstated for fixed Bell scenarios, and "GPT = α*" relies on an unstated clique-exclusivity assumption; the mathematics is Lovász/GLS restated, so credit must be explicit. AFLS (Dec 2012) already refines the normalisation point.
