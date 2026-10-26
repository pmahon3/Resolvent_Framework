## Audit: seed.md — "the peeling lemma for coherent views" (mode: full)

### Declared contribution type(s): Type 1 (new theorem); Type 4 (vocabulary: views, peelability)

Types are declared, but no per-type bar is stated ("the per-type bars I commit to clearing" is missing). The seed is therefore only partly ready for Phase 2. The audit proceeds anyway.

---

### Pure Verdict: KNOWN (classical, 1962 / 1983; the explicit probability-plus-RIP form appears in 2021)

**Stripped statement.** The views form a hypergraph H on vertex set V with edges W. View laws are finite marginal distributions, and coherence is pairwise consistency. "Peelable" is word for word the **running intersection property** (RIP): there is an ordering such that each edge's intersection with the union of the earlier edges lies inside one earlier edge. For reduced hypergraphs (no edge contained in another), RIP is equivalent to **α-acyclicity**, as are a join tree existing and the GYO/Graham reduction succeeding. The claim then reads: *every pairwise-consistent family of marginals on H has a global joint iff H is α-acyclic.* This is exactly the classical local-to-global consistency theorem for probability distributions.

**Owners (most damaging first).**

1. **Atserias & Kolaitis, "Consistency, Acyclicity, and Positive Semirings", arXiv:2009.09488** (read level: **full text, partial**. I read the HTML through §4.2 / Thm 4. Three fetch attempts did not reach §4.3, so the probability-case statement there is cited from the paper's introduction only. The verified anchors are the §4.1 RIP definition, Thm 2(c) and Cor. 2.)
   - §4.1 defines the running intersection property in exactly the seed's words ("for each i ≥ 2, X_i ∩ (X_1 ∪ … ∪ X_{i−1}) ⊆ X_j for some j < i"). Theorem 2(c) lists it as equivalent to acyclicity.
   - Corollary 2: H is acyclic iff H is Vorob'ev-regular, via Lemmas 17–18.
   - §4.3, "Consistency of Probability Distributions and Vorob'ev's Theorem": the probability case. A family of distributions has the local-to-global property iff H is acyclic.
   - The cyclic direction uses a generalised **Tseitin parity/modular-counting construction**. This is precisely the seed's "parity-twisted laws on a cycle" proof idea, carried out for *arbitrary* cyclic hypergraphs, not only graph cycles. Its special case on the 4-cycle is the PR box.
   - Main theorem (introduction and §4): for every positive semiring K, pairwise consistency implies global consistency iff H is acyclic. Probability distributions are the case K = ℝ≥0, normalised.
   - **This single source states the seed's lemma, its definition, and both halves of its proof idea.**

2. **N. N. Vorob'ev, "Consistent families of measures and their extensions", Teor. Veroyatn. Primen. 7(2) (1962) 153–169; Theory Probab. Appl. 7 (1962) 147–163, doi:10.1137/1107014** (read level: **abstract**, MathNet page).
   - Setting: the vertices of a finite complex carry finite outcome sets, and measures sit on the faces.
   - Main theorem: every consistent family is extendable iff the complex is *regular*. Regular means it can be reduced to the empty complex by repeatedly removing an "extreme face" (a maximal face with proper vertices) together with those vertices.
   - This is the GYO ear-removal in other words, so it is the seed's peeling. It is the original owner of the seed's theorem.

3. **Beeri, Fagin, Maier & Yannakakis, "On the desirability of acyclic database schemes", J. ACM 30(3) (1983) 479–513** (read level: **abstract/snippet**, via IBM and HUJI pages and citing works).
   - This is the relational (Boolean-semiring) version: pairwise-consistent relations are globally consistent iff the schema is acyclic.
   - It also proves that acyclicity is equivalent to the join-tree and running-intersection conditions, which are the seed's "peelable".

4. **Abramsky, "Relational databases and Bell's theorem", arXiv:1208.6416** (read level: **snippet**). It links Vorob'ev's condition, database acyclicity and contextuality. It credits Barbosa with acyclicity ⇒ the local-to-global property in the sheaf framework.

5. **Textbook/folklore** (read level: **not verified, recalled**; no theorem numbers claimed). The sufficiency direction is the standard decomposable-model / junction-tree construction: the joint is ∏ p(C) / ∏ p(S) over cliques C and separators S. See Lauritzen, *Graphical Models* (1996), ch. 2–3, on decomposable hypergraphs and their marginals, and Koller & Friedman (2009), clique-tree calibration. The seed's "condition on the overlap and multiply" is exactly this formula. Experts would call this direction routine.

**Is it a restatement?** Yes. "View" = hyperedge / context / face; "coherent" = pairwise consistent; "peelable" = running intersection property = α-acyclic = Vorob'ev-regular. The seed adds no hypothesis and no conclusion beyond Vorob'ev 1962 and Atserias–Kolaitis §4.

**Correctness flag on the seed as stated** ⟦HAND⟧. As written, the "only if" direction is false when value sets may be singletons. If every variable has exactly one value, every coherent family is trivially the restriction of the unique joint, whatever the shape of W, cyclic or not. The classical statements quantify over all finite domains. Safe fix: quantify the "only if" over all finite value sets. A "|value set| ≥ 2" fix is ⟦HAND — unverified⟧ in general, because the Atserias–Kolaitis construction uses values in {0,…,d−1} with d set by the hyperedge structure. Binary values do suffice for the tetrahedron boundary {abc, abd, acd, bcd} ⟦HAND⟧: put uniform laws of even parity on three faces and odd parity on the fourth. All pair marginals are uniform, so the laws agree, but summing the four face constraints gives 0 ≡ 1 (mod 2). The "if" direction is fine. A second, smaller point: the converse must cover every non-acyclic reduced hypergraph, including ones whose obstruction is not a graph cycle, e.g. the boundary of a tetrahedron {abc, abd, acd, bcd}. "Parity-twisted laws on a cycle" understates what is needed there. Atserias–Kolaitis handle this with a modular-counting modulus d ≥ 2 that depends on the hyperedge structure.

**Search record.** Searched for: Vorob'ev consistent families / regular complex; BFMY acyclic schemes; local-to-global consistency for K-relations; running intersection / GYO / join tree equivalences; contextuality–database links (Abramsky). Fields covered: probability/measure extension, database theory, graphical models, quantum contextuality/sheaves. All of them point to the same theorem.

---

### Applied Verdict: not evaluated (seed claims no Type 7)

Practitioner test, for completeness: "I already use junction-tree / acyclic-join checks (GYO reduction, linear time) to decide whether local marginals glue." The seed offers no new method beyond that.

---

### Contribution Type Verdicts (mode=full):

**Type 1 (New theorem): FAIL — KNOWN.** The statement is Vorob'ev 1962 (main theorem, regular complexes). It appears in today's vocabulary, with the seed's exact RIP definition and the parity (Tseitin) counterexample method, in Atserias–Kolaitis arXiv:2009.09488, §4.1 (RIP definition, Thm 2(c)), Cor. 2 (acyclic ⇔ Vorob'ev-regular) and §4.3 (probability case). The sufficiency half is textbook junction-tree folklore. Also, the seed as stated is incorrect for fixed small (e.g. singleton) value sets. The correct form quantifies over all finite value sets (see above).

**Type 4 (Vocabulary: views, peelability): FAIL — three-statements test not met.**
- "View" renames hyperedge / context / schema attribute set / face.
- "View law" renames marginal / local section / empirical-model context distribution.
- "Coherent" renames pairwise consistent / no-signalling (in the contextuality setting).
- "Peelable" renames running intersection / α-acyclic / Vorob'ev-regular / GYO-reducible.

The seed names no statement that is cleanly stateable in this vocabulary but not in the standard one. Its single theorem is the known one. This is failure mode #2, rediscovery as synthesis. The terms are not even more general than the standard ones: Atserias–Kolaitis already work over arbitrary positive semirings.

**Undeclared types considered:** Type 2 (new proof) would also fail. The glue-by-conditioning and parity-twist proofs are the standard ones (junction tree; Tseitin, as generalised by Atserias–Kolaitis). Type 6 (exposition) is not claimed and has no named audience. The literature is accessible (Atserias–Kolaitis is open-access and self-contained).

---

### Cross-reference

Both declared types fail for the same reason: the theorem and the vocabulary are owned. Atserias–Kolaitis (2021) shows that one framework covers probability distributions (Vorob'ev), relations (BFMY) and all positive semirings, with the RIP definition verbatim. The seed sits strictly inside it. No surviving component, assembly or novel framing was found.

**Bearing on the why** (local views → one world?). This seed *is* the canonical answer to the tree-shaped part of the question: on acyclic shapes, local agreement always adds up to one world, and on every cyclic shape some coherent views fail to. Its value to the programme is as an `owned_region` marking where the seam is *not*.

**owned_by (for the seam map):**
- *Region:* pairwise-consistent finite marginals ⇒ global joint ⟺ α-acyclic (RIP) view hypergraph, including the cyclic-direction parity counterexamples.
- *Owned by:* Vorob'ev 1962 (main theorem, abstract read); Atserias–Kolaitis arXiv:2009.09488 §4.1/Thm 2, Cor. 2, §4.3 (full text read through §4.2; §4.3 per the paper's introduction); BFMY 1983 (relational case, abstract).
- *How verified:* primary-source pages fetched 2026-10-26.

---

### Recommendation

**PARK.** Evaluated: Type 1 (FAIL — known: Vorob'ev 1962; Atserias–Kolaitis 2021 §4) and Type 4 (FAIL — every term renames a standard concept, and no new statements are enabled). Types 2 and 6 were considered and fail. Record it in covered_leads as an owned region, and fix the singleton-domain hypothesis in any reuse. Open-question status does not apply, because the question is answered in the literature.
