## Audit: seed.md, piercing all maximum cliques in uniform hypergraphs (mode: full)

Audit date (per AS_OF.md): **2026-04-22**. Only sources dated on or before that day count as prior art. The seed's own work, under any title or version, is ignored.

### Declared contribution type(s): Type 1 (new theorem), Type 5 (impossibility / counterexample)

The seed declares these types but does not state the per-type bars it commits to clearing (the framework asks for both). This is a minor readiness gap.

**The seed's claim, with the vocabulary stripped out.** In a k-uniform hypergraph G, a *clique* is a vertex set all of whose k-subsets are edges. Hajnal (1965) proved that in a graph, for any family Q of maximum cliques, |∩Q| ≥ 2ω − |∪Q|. Hence ω > n/2 forces a common vertex. The conjecture being refuted says that for each k there is a c_k < 1 such that ω(G) > c_k·n forces all maximum cliques to share a vertex. The seed's claim: for every c < 1, every k ≥ 3 and every t ≥ 1 there is a k-uniform G with ω > cn whose maximum cliques have no transversal of size t.

**Dual form, which is decisive for prior art.** Let H′ be the k-graph of non-edges of G. The cliques of G are exactly the independent sets of H′, so the maximum cliques of G are the complements of the minimum vertex covers (transversals) of H′. In this form:
- ω(G) > cn ⇔ τ(H′) < (1−c)n;
- "no t-set pierces all maximum cliques" ⇔ every t-set of vertices lies in some minimum transversal of H′.

### Pure Verdict: UNCLEAR (the t = 1 case is a short consequence of classical τ-critical hypergraph theory; the bounded-t ≥ 2 strengthening was not found in the literature and was not verified)

**1. The t = 1 case, which is the literal refutation of the conjecture, follows from known results ⟦HAND⟧.**
- *Step 1.* Let H′ be a τ-critical k-graph: deleting any edge lowers τ, and H′ has no isolated vertices. Then every vertex v lies in a minimum transversal. Take an edge e ∋ v and a transversal C of H′ − e with |C| = τ − 1. Then C ∪ {v} is a minimum transversal of H′ that contains v. So in G = complement of H′, the maximum cliques have no common vertex.
- *Step 2.* For k = 2 this is the Erdős–Gallai bound: a τ-critical graph has at most 2τ vertices. That is Hajnal's ½ threshold seen dually.
- *Step 3.* For k ≥ 3, τ-critical k-graphs can have order polynomial in τ:
  - Tuza (1989) bounds the order of a k-uniform τ-critical hypergraph without isolated vertices by C(k+τ−1, k−1) + C(k+τ−2, k−1). The source I read describes this as best possible up to a constant factor.
  - For k = 3, this is the Szemerédi–Petruska problem. The conjectured sharp value is C(τ+2, 2). The upper bounds are Gyárfás–Lehel–Tuza n ≤ 2τ² + τ, then Tuza (¾)τ² + τ + 1, then Kézdy–Lehel C(τ+2, 2) + O(τ^{5/3}).

  So n/τ → ∞ is possible.
- *Conclusion.* Taking such an H′ gives ω(G) = n − τ > cn for every c < 1, with no vertex common to all maximum cliques. **The conjecture, as stated (single-vertex piercing), is refuted by classical 1980s τ-critical theory together with a three-line duality.**
- *Gap.* I have read only secondary sources stating that Tuza's bound is tight up to a constant, and that the C(τ+2, 2) value is attained. I did not read the lower-bound construction in a primary source. If that construction is only quadratic for k = 3, it still suffices: any superlinear order is enough.

**2. The bounded-t ≥ 2 strengthening: residual, not found.**
- The strengthening requires every t-set to lie in a common minimum transversal. τ-criticality gives this only for single vertices.
- The naive fix is a disjoint union of copies of a τ-critical H′. It fails when two vertices of T lie in the same copy and share no minimum transversal there.
- I found no source asserting "every t-set lies in a minimum transversal" for k-graphs with τ = o(n), and I could not settle by hand whether known τ-critical constructions (Szemerédi–Petruska extremal examples, Bollobás set-pair constructions) already have this property.
- This is the only candidate novel content, and it is **UNCLEAR**: it could be a routine extension, or a genuine new construction.

**3. A cap on symmetric constructions ⟦HAND⟧.** Suppose H′ is vertex-transitive, or is a disjoint union of vertex-transitive components. Averaging an optimal fractional cover gives τ*(H′) = n/k, so ω/n = α(H′)/n ≤ (k−1)/k. So symmetric constructions cannot reach c > (k−1)/k.
- Example: disjoint k-blocks taken as non-edges, giving ratio (k−1)/k. It refutes single-vertex piercing only, because two vertices of one block pierce all maximum cliques.

**Other searches** (standard web search, 2026-10-26). Hajnal's clique-collection lemma has graph descendants only:
- Levit–Mandrescu, arXiv:1101.4564 (2011). Read level: snippet.
- arXiv:0907.3705 (2009). Read level: snippet.
- arXiv:1109.3092 (2011). Read level: snippet.
- arXiv:2103.05998 (2021). Read level: snippet.
- arXiv:2403.19737 (2024-03-28). Read level: abstract fetched.

None of these is a hypergraph version or a refutation.

**Conjecture provenance.** The conjecture is attributed to Jung–Keszegh–Pálvölgyi–Yuditsky only in the seed's own paper and in post-date material (a UNAM seminar abstract dated 2026-05-06, and an online review), all of which are excluded. **I could not locate any written statement of it dated on or before 2026-04-22.** It is probably unpublished or oral.

**Correctness.** The seed is an abstract only, with no proof. The t = 1 case is correct via the τ-critical argument above. The t ≥ 2 case is unverified.

### Applied Verdict: not evaluated (no applied or methodology claim; Type 7 not declared)

### Contribution Type Verdicts (mode=full only):

**Type 1 (new theorem): UNCLEAR.**
- Bar: not known, not folklore, not a trivial consequence.
- The t = 1 statement fails the bar. It is a trivial consequence of known results: the τ-critical duality plus superlinear-order τ-critical k-graphs (Tuza 1989; the Szemerédi–Petruska line).
- The t ≥ 2 statement may clear the bar, if it is not a routine consequence of the same constructions. That was not determined.

**Type 5 (impossibility / counterexample): UNCLEAR.**
- (a) Closing an active direction: the literal conjecture is closed, but by known means. The direction's activity is documented only by an unpublished conjecture.
- (b) Sharpening non-trivially: the passage from a common vertex to a bounded transversal, uniform in c and t, is a genuine strengthening *if* it is not automatic from τ-critical constructions.
- Fail condition met for t = 1 ("trivial consequence of known results"); open for t ≥ 2.

**Undeclared material.** The "related questions" and the geometric (Helly-type) variant are not claimed as a contribution type and are not evaluated.

### Cross-reference
- The verdicts collapse onto one question: **is "every t-set lies in a minimum transversal, with τ = o(n)" new, or routine from τ-critical hypergraph theory?**
- The single-vertex refutation is classical in dual form, and the seed (as an abstract) does not credit the τ-critical connection or the Szemerédi–Petruska connection.
- The novelty, if any, is in the uniform bounded-piercing statement.

### Recommendation
**Needs deeper audit** before proceeding. Do these in order:
1. Read primary sources: Tuza 1989 and the Szemerédi–Petruska constructions (Gyárfás–Lehel–Tuza; Kézdy–Lehel). Check whether their extremal τ-critical k-graphs already have every t-set inside a minimum transversal.
2. Search the τ-critical and "t-critical / vertex-critical transversal" literature (Lovász, Bollobás 1965 "On generalized graphs", Tuza's set-pair surveys) for this property.
3. Verify the seed's t ≥ 2 construction independently, by hand or in Lean.
4. Find a citable source for the conjecture.

Possible outcomes:
- If the t ≥ 2 case is routine: **park** (Type 1 known or trivial; Type 5 trivial).
- If it is not routine: proceed scoped to Type 1/5 on the bounded-t statement only, crediting the τ-critical route for t = 1.

**Bearing on WHY.md.** This is a lens only: whether large overlapping local agreements (maximum cliques) must share a centre (a common vertex or bounded core). For k ≥ 3 no centre is forced, a pattern of order without a centre. There is no method transfer to the programme.

### Referee estimate: BORDERLINE
Venue class: research journal (combinatorics; short-note if the t ≥ 2 case is light)
Value carried by: factor 1 (strong-form refutation of a stated conjecture), conditional on the bounded-t part being new
Main risk a referee would raise: the single-vertex case follows from classical τ-critical hypergraph theory (Erdős–Gallai dual; Tuza 1989; Szemerédi–Petruska), which is uncredited; is the bounded-t extension more than routine?

---
Sources (all read 2026-10-26):
- Prior art (all pre-date 2026-04-22):
  - arXiv:2208.11573 (2022; Kézdy–Lehel asymptotic resolution of Szemerédi–Petruska). Read level: abstract fetched.
  - arXiv:1904.04921 (2019) and arXiv:2204.02859 (2022). Read level: search snippets, as the secondary source for Tuza 1989 and for Gyárfás–Lehel–Tuza.
  - arXiv:1101.4564 (2011), arXiv:0907.3705 (2009), arXiv:1109.3092 (2011), arXiv:2103.05998 (2021). Read level: snippets.
  - arXiv:2403.19737 (2024). Read level: abstract.
- Primary 1980s papers (Tuza 1989; Gyárfás–Lehel–Tuza; Bollobás 1965; Erdős–Gallai 1961): NOT read; known via the secondary sources above.
- Excluded as the seed's own work or post-date: arXiv:2604.21588; the matem.unam.mx seminar page (2026-05-06); the themoonlight.io review.
