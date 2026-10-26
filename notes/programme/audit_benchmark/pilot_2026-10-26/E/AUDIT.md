## Audit: seed.md — Livson, Pritam, Prokopenko, "The Non-Orientable Topology of Condorcet's Paradox", arXiv:2601.07283 (mode: full)

Version audited: **v6 (16 Sep 2026)**; v1 was titled "Condorcet's Paradox as Non-Orientability". Paper read level: **full text** for §2.4.2, §3.1–3.4 (incl. Thm 4, Thm 5 proof, Defs 6–7, Lemma 1, Prop 4, Thm 6), §4 related work, bibliography, Appendix A.1–A.2 (Construction A.1, Theorem A.2 and proof). Extraction via `pdftotext` of the arXiv PDF and the arXiv HTML. Appendix A.3 (general |A| ≥ 3 + indifference) was read at summary level only.

Web search was cut off by a session limit partway through the audit. Searches that did complete are listed under Sources. The Candeal–Induráin and Baryshnikov 1993 primary texts were **not** accessed.

### Declared contribution type(s): Type 1 (new theorem), Type 4 (vocabulary: realised/unrealised, valid/contradictory cycles), Type 6 (exposition: topology ↔ social choice)

The seed declares types but no per-type bars ("what I commit to demonstrating"). Per the framework, that is a Phase-1 deficiency. The bars below are the framework defaults.

---

### Correctness finding (internal; reported before novelty because it changes what can be claimed)

**Theorem 5 (realised + contradictory ⇒ RP²) is not established, and as defined it is false.** ⟦HAND — verified against the paper's own text; not Lean⟧

1. **What Def. 5 / Thm 5 actually define.** The proof of Thm 5 (p. 15) says the space is "N(V) … identifying its 2-simplices {12,23,31} and {13,32,21}". Only the two cap triangles are identified.
   - The cap triangles are disjoint. N(V) is the octahedron boundary, and ij is antipodal to ji.
   - Each boundary edge of a cap therefore ends up in three triangles: the merged cap, one annulus triangle from the top side, and one from the bottom side. **The result is not a surface.**
   - Homotopy type: identify the two boundary circles of the annulus N(U) (this gives the Klein bottle K of Thm 4, with the glued circle a as a fibre). Then attach one disc along a.
   - π₁(K) = ⟨a, b | bab⁻¹ = a^{±1}⟩, and killing a leaves **π₁ = ℤ, H₁ = ℤ**. Also χ = 0 + 1 = 1.
   - RP² has π₁ = ℤ/2, so the space is not even homotopy-equivalent to RP².
2. **Appendix A.2 (Construction A.1, Theorem A.2) proves something else, and that proof is broken too.**
   - Eq. (6) is q(θ,t) = (−θ mod 2π, |t|) on the whole cylinder. Its fibres are {(θ,t), (θ,−t)}: a **fold** fixing the circle t = 0. It does not identify only the caps. It is also not free, so it is not a 2-sheeted covering.
   - The proof then asserts different fibres, (θ,b) ↔ (−θ,−b). That involution has fixed points at θ ∈ {0,π}, t = 0. It is a π-rotation of S², so its quotient is S², not RP². The step χ(X) = ½χ(S²) needs a free action.
   - Eq. (7) also does not agree with Eq. (6) on the boundary: top cap (φ,1) ↦ (φ,·), but cylinder (φ,½) ↦ (−φ,½).
   - Only the genuine antipodal map, (θ,t) ↦ (θ+π, −t) with caps φ ↦ φ+π, gives RP². On the octahedron that map sends each strict order to its **reverse** ({12,23,13} ↦ {21,32,31}). The six strict-order triangles become three, which contradicts Cont(3) = Strict(3) ⊔ {c} having six distinct strict orders.
3. **Consequence.** Table 1's "contradictory/realised = RP²" entry, and with it the RP² half of the headline claim, is unsupported.
   - Thm 4 (Klein bottle) survives: χ = 3 − 9 + 6 = 0, and the twist argument is the standard one.
   - Thm 6 / Prop 4 rely on Thm 5 to say "non-orientable". With the space as actually defined, orientability is undefined (it is not a manifold). The reformulation could be repaired by using the Klein-bottle (unrealised) model, which is a surface.

---

### Pure Verdict: KNOWN (the components) / trivial (the Arrow reformulation); RP² claim incorrect

Stripping the vocabulary leaves four statements.

**(S1) The nerve of the pairwise cover of Strict(3) is an annulus, and its two boundary 3-cycles are the two Condorcet cycles. KNOWN.**
- Chia 2015, Prop 2.8 (read: **full text**, pp. 4–5): "the simplicial complex N_P generated from choice set X where |X| = 3 is homotopy equivalent to S¹". The two "impossible" vertex sets {12,23,31} and {32,21,13} are unfilled. "The generator of H₁ … corresponds to a set of choices which are cyclic … a phenomenon that underlies the Con[dor]cet paradox."
- Chia attributes the general S^{n−2} statement to Baryshnikov 1993 (Adv. Appl. Math. 14:404–415; **not accessed**, 403 error; cited via Chia and via the paper).
- The paper itself credits both (Prop 1; "Chia's observation", §3.2).
- The paper adds only the homeomorphism type (annulus rather than "≃ S¹"). That is immediate from the 6-triangle picture.

**(S2) Realised valid cycles give a sphere (Prop 3). FOLKLORE / trivial.** ⟦HAND⟧
- Valid(3) is the 8 tournaments on 3 vertices, i.e. the sign vectors {±}³.
- In the nerve of the pairwise-preference cover, a 2-simplex is a choice of one vertex from each antipodal pair {ij, ji}. That is the boundary of the 3-dimensional cross-polytope (octahedron) ≅ S², with 6 vertices, 12 edges and 8 faces.
- Its dual is the ±1 cube on which Saari places pairwise outcomes, with the two cycles at antipodal vertices. Saari's representation cube is known here only at **snippet** level (search result: Klamler/Eckert slides and papers using "Saari's representation cubes"; Saari, *Basic Geometry of Voting*, 1995, not read).
- An expert would call this obvious.

**(S3) Contradictory/unrealised gives the Klein bottle (Thm 4). Trivial once posed.**
- Gluing the two boundary circles of an annulus with orientation reversed is the textbook Klein bottle (Hatcher §0 and §1.2, the paper's own reference [22]).
- The only content is the combinatorial check that the "same-orientation" gluing violates the paper's own admissibility criterion (§3.3, App. A.1). That criterion is stipulated by the authors, not derived.

**(S4) Thm 6 (Arrow ⇔ "no SWFC with U, IIA, ND and Orientable Social Choices"). Trivial consequence of the definitions; it is a relabelling.** The three-line derivation:
1. Lemma 1: Unanimity ⇒ im(w) ∈ {Strict(3), Cont(3)}.
2. Defs 6–7: the Arrovian model is the annulus if im(w) = Strict(3) and the "RP²" if im(w) = Cont(3). So "Orientable Social Choices" ⇔ im(w) = Strict(3) ⇔ w never outputs c ⇔ (the paper's) Unrestricted Domain.
3. Substitute this into Arrow's theorem (strict, 3 alternatives).

Orientability is used as a one-bit label for "the output contains a cycle". No topological invariant does any work in the proof. The authors concede it is "a reformulation, not an independent proof" (§3.4).

**Closest neighbours that do real topological work (not owners of S1–S4):**
- Baryshnikov 1993 / Chia 2015 / Rajsbaum–Raventós-Pujol (PODC 2022): Arrow via homology of the nerve and induced maps. Read levels: Baryshnikov not accessed; Chia full text; Rajsbaum–Raventós-Pujol only via the paper's §4.
- Candeal–Induráin, Econ. Lett. 45 (1994) 407–412, "The Moebius strip and a social choice paradox": a social-choice paradox tied to non-retractability of the Möbius strip. Known **only via the paper's §4** (abstract not fetched; search blocked). It is the nearest owner of the generic idea "non-orientability ↔ a social-choice paradox". Its scope as reported is Chichilnisky-type continuous preferences, not ranked choice. It is a precedent for the theme, not for S1–S4.
- Chichilnisky 1980 (Adv. Math. 37:165–176), via the paper's citation: conjectured that the "cyclical element" of Condorcet is topological. The paper claims to answer this. Given (S4), it answers by definition rather than by an invariant.

**Searches run:** "Klein bottle / projective plane preference cycles social choice topology Condorcet"; "Saari representation cube transitive intransitive"; "nerve of tournaments cross-polytope sphere social choice Baryshnikov"; "Arrow orientability Möbius Candeal Induráin". None found an earlier Klein-bottle/RP² model of Condorcet cycles. **The specific surfaces-as-models framing appears new as a framing.** The mathematics in it is textbook (S1–S3) or definitional (S4).

### Applied Verdict: not evaluated
The paper makes no applied or methodological claim. The "money pumps / Dutch books" mention in §4 is future work only.

### Contribution Type Verdicts (mode=full):

**Type 1 (new theorem): FAIL**
- S1 is owned by Chia Prop 2.8 / Baryshnikov 1993.
- S2 and S3 are textbook topology applied to a 6-vertex complex.
- S4 is a 3-line relabelling (above), and the authors concede it.
- The one statement that would be non-trivial and new, "realised contradictory = RP²", is **incorrect as defined** (correctness finding).

**Type 4 (vocabulary): FAIL** (three-statements test)
- "Realised/unrealised" = whether the cycle 2-simplices are present in the complex: filled versus unfilled 3-cycles in the nerve of a cover of Valid(3) versus Strict(3).
- "Valid/contradictory" = whether the two cycles are kept distinct or quotiented to one element c, i.e. the domain Valid(3) versus Cont(3).
- Both are stateable verbatim in standard vocabulary (which domain set, which cover). I could not name three statements that need the new words.
- The only non-trivial result proposed in the vocabulary (Thm 5) is wrong.
- "Orientable Social Choices" is a definitional proxy for "im(w) = Strict(3)" and enables no new statement.
- This is failure mode #2 (renaming).

**Type 6 (exposition/translation): FAIL** (borderline; the closest to passing)
- (a) Audience: social-choice theorists and economists (cs.GT / econ.TH cross-listing). This is named implicitly.
- (b) Inaccessible literature: the Baryshnikov nerve model is already expounded accessibly for exactly this audience by Chia 2015 (an REU paper, full text), Baryshnikov 1997 (Soc. Choice Welf.), and Rajsbaum–Raventós-Pujol 2022. Candeal–Induráin already offered a Möbius picture to economists. The bar's condition "existing literature not accessible" is not met.
- (c) Non-trivial conceptual work: the new conceptual move, "contradiction = orientation-reversing identification", carries no proof weight in Arrow (S4). Its RP² instance is mathematically broken, and a translation that mis-states the topology fails as exposition.
- **A corrected version could plausibly clear Type 6 at a Monthly/Intelligencer-style venue as a picture.** The corrections are: drop RP², use the Klein bottle, and state honestly that orientability is a label. That would be a different object from the paper as it stands.

### Cross-reference
- Known components with an incorrect novel assembly.
- The only seam-shaped idea is "contradictory cycles as a quotient forcing an orientation reversal". It reduces to the standard annulus→Klein-bottle gluing, and the paper stipulates rather than derives the admissibility rule.
- Where the idea is meant to bite (realised cycles, and the Arrow link), the space is either not a surface (Def 5) or, under the appendix's map, not RP². The Arrow link is definitional either way.
- No surviving novel theorem, so no type is rescued by another.

### Recommendation
**Park** (as an audit of this paper's contribution).
- Types evaluated: 1, 4 and 6.
- Type 1 fails: owned (Chia Prop 2.8 / Baryshnikov 1993), trivial (S2, S3), definitional (S4), and incorrect (Thm 5).
- Type 4 fails the three-statements test.
- Type 6 fails bar (b) (Chia/Baryshnikov are accessible) and bar (c) (the RP² translation is wrong).
- Owed if anyone revives this: (i) fix Thm 5 (see the correctness finding); (ii) replace the orientability proxy in Thm 6 with an invariant that does proof work, for example a ℤ/2 class detected by the induced map on the Klein-bottle model; (iii) fetch the Candeal–Induráin 1994 and Baryshnikov 1993 primary texts, which were not accessed here.

### Sources and read levels
- Livson–Pritam–Prokopenko, arXiv:2601.07283 v6. **Full text** (sections listed above; A.3 summary only).
- Chia, W.H., "The Topological Approach to Social Choice", UChicago REU 2015 (math.uchicago.edu/~may/REU2015/REUPapers/Chia.pdf). **Full text, §2–3** (Prop 2.8, Prop 3.4).
- Baryshnikov 1993, Adv. Appl. Math. 14:404–415. **Not accessed** (403). Content via Chia and the paper.
- Baryshnikov 1997, Soc. Choice Welf. 14:199–209. **Snippet** (IDEAS listing in search results).
- Candeal & Induráin 1994, Econ. Lett. 45:407–412. **Not accessed.** Content via the paper's §4 only.
- Rajsbaum & Raventós-Pujol, PODC 2022. **Not accessed.** Via the paper's §4.
- Chichilnisky 1980, Adv. Math. 37. **Not accessed.** Via the paper.
- Saari, *Basic Geometry of Voting* (1995), representation cube. **Snippet** (search results: Klamler/Eckert COMSOC 2008, Klamler slides 2010).
- Okura, arXiv:2408.14263 (topological proof of Terao's generalised Arrow theorem). **Snippet** (search result). A neighbour, not an owner.
- Livson–Prokopenko, arXiv:2510.09076. **Abstract.** Self-prior: a single spanning cycle under Arrow's constraints; no lattice or "c" identification in the abstract.
- Hatcher, *Algebraic Topology* (2002), Klein bottle / RP² constructions. Standard reference, cited from memory (not re-read).
