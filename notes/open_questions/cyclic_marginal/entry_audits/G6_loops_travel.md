# G6 entry audit: loops travel, forced functional, cut-the-loop, "pointless ⟺ not a forest"

`/audit pure`, THEORY-ITEMS mode (SKILL v2.1, entry-level cap). Date 2026-10-27. Auditor: Claude
(opus subagent), hostile and cross-field. reviewed: false. Nothing in the taxonomy or the note was
edited; every change below is a **proposal**.

Declared contribution types: none declared for these entries. Theory items are evaluated against
Type 3 and Type 4 only.

---

## 0. Headline (a reversal; read first)

**The dividing line "forest vs not" is not new. Its proof architecture is also owned, step for
step.** What is new, if anything, is only the *semantics*: two-valued, finitely additive states on
the Dynkin carrier over an infinite alphabet.

- **Two-line reduction.** With pair windows the scheme is a 2-uniform hypergraph. For it:
  - conformal ⟺ every triangle lies inside a hyperedge ⟺ triangle-free;
  - chordal ⟺ no induced cycle of length ≥4.
  
  So α-acyclic ⟺ conformal and chordal (BFMY Thm 3.4) ⟺ forest.
- **The line is owned in three semantics.** Vorob'ev 1962 (probability), Beeri–Fagin–Maier–Yannakakis 1983 (relations) and
  Atserias–Kolaitis (positive-semiring K-relations, arXiv:2009.09488 Thm 3/4) each prove
  local-to-global consistency ⟺ acyclic. For pair windows, that is ⟺ forest.
- **The proof is the same proof.** Atserias–Kolaitis' proof of Thm 3 (pp. 27–31, read in full
  for this audit) runs in four steps:
  - **Lemma 12.** Acyclic ⇒ glue along a join tree. This is our `thm.path` via `thm.amalgamation`.
  - **Lemma 13 and Lemma 14.** A minimal non-acyclic scheme is either minimal non-conformal or
    minimal non-chordal. Minimal non-conformal is `{V∖{Aᵢ}}`, which for graphs is **the triangle**.
    Minimal non-chordal is **an induced cycle of length ≥4**. These are exactly the note's two
    base cases.
  - **Lemma 15.** Delete an attribute A by **fixing it at a constant u₀** and padding the
    relations. An obstruction on the induced sub-scheme H[W] then lifts to H. This is `ψ` in
    `thm:travel`, line for line.
  - **Lemma 16.** Drop hyperedges covered by others. These are the cycle-to-outside windows that
    shrink to one-coordinate questions.

  Their closing remark goes further. If H is not acyclic, one uniform family of ordinary relations
  is a counterexample for every positive semiring at once.
- **Places that understate the overlap** (proposed fixes in §6):
  - The note says "the line now falls between trees and everything else" (§Why loops; §Triangle,
    "The dividing line").
  - The coda says "None of them covers finitely additive answers on the full glued board".
  
  The second sentence is true of the *semantics*, but the coda places Vorob'ev only under "Lines"
  and never says that the converse (cycles ⇒ obstruction) and its reduction to triangle +
  induced C_L are owned. The coda should say both.

**Bearing on WHY.md.**
- **Loop?** Yes. The line "trees glue, loops can fail" was already a theorem in probability and
  databases. The programme's version says the same about *idealised*, infinitely fine answer
  patterns.
- **Circle, or composition?** Composition, but the transport and reduction are owned. The
  programme's own contribution is the two base witnesses.

---

## 1. Sources checked (with read level)

| Source | What it gives | Read level |
|---|---|---|
| Atserias–Kolaitis, arXiv:2009.09488 (shelf) | Thm 3/4: K-relations, local-to-global ⟺ acyclic. Lemmas 13–16: reduction to triangle-type / induced C_{n≥4} plus constant-padding transport. Uniform counterexample remark | **primary, pp. 25–31 read** (shelf index says "abstract"; upgrade owed) |
| BFMY 1983 Thm 3.4 (as reproduced in A–K Thm 2) | acyclic ⟺ conformal + chordal ⟺ pairwise ⇒ global (relations) | secondary (A–K restatement) |
| Vorob'ev 1962 | regular complexes ⟺ every consistent family of probability laws extends | secondary (A–K §5; note's coda) |
| Abramsky–Brandenburger 2011 (shelf) | Thm 5.9: no-signalling ⟺ realisation with signed ("negative") probabilities; Prop 5.8 | **primary (Thm 5.9 text quoted below)** |
| Xu–Cabello, PRA 99 020103 (2019), arXiv:1805.02032 | quantum contextuality possible ⟺ compatibility graph non-chordal (contexts = cliques) | abstract / search snippet |
| Kharoof–Ipek–Okay 2024; Araújo et al. 2013 (shelf, owned regions) | n-cycle scenarios, finite outcomes, σ-additive | read (existing regions) |
| Abramsky–Mansfield–Barbosa 2011; Abramsky et al. 2015 (shelf) | Čech cocycle obstructions to global sections | grep only: "cocycle" yes; "ultrafilter", "finitely additive", "infinite" no hits |
| nLab "taut functor" | the ultrafilter functor β preserves weak pullbacks (= `thm.amalgamation`) | search snippet; the linked proof not read |
| Basile–Bhaskara Rao–Shortt, PAMS 121 (1994) 137–143; Shortt 1983 | common extensions of two consistent charges | **unread** (search snippet) |
| Tukey/Fubini ultrafilter-product literature (Dobrinen–Todorcevic; arXiv:2312.15261) | p·q ≠ q·p (Rudin–Keisler) | snippet; already under own.ultrafilter_products |

Abramsky–Brandenburger Thm 5.9, verbatim: "Probability models have local hidden-variable
realizations with negative probabilities if and only if they satisfy no-signalling."

Shelf-first notes:
- A–K is already cited in `own.merging_existence_gap`, verified by "PDF grep". The finding here
  *extends* that region and `own.vorobev_acyclic`; it is not a new lead.
- The SHELF_INDEX entry for A–K links `own.acyclic_gluing`, an id that appears in no
  `*_taxonomy.json`. The link dangles and should point to `own.vorobev_acyclic`.

---

## 2. thm.loops_travel

**The statement, stripped.** Let G be a graph containing an induced cycle C, |C| ≥ 4. Let
ψ: ℕ^C → ℕ^V fix the off-cycle coordinates at a constant. Pulling back along ψ maps the
Dynkin system generated by G's pair-coordinate algebras into the ring's. So the ring's
non-coherent two-valued charge μ pushes to the non-coherent charge μ∘ψ⁻¹ on G. The same holds for a
triangle.

**Correctness ⟦HAND, re-checked⟧.** I re-checked four points.
- Preimage commutes with complement and disjoint union, so {F : ψ⁻¹F ∈ D_C} is a Dynkin system
  containing G's window events. This needs C induced: a chord's window would pull back to a
  non-ring window.
- Non-coherence: let W fit s and write π for the projection to the cycle coordinates. π∘ψ = id,
  so π_*W fits μ on ring windows and contains every staircase step, whose intersection is empty.
- No σ-additive version: `prop:sigma`.
- The triangle clause: a 3-cycle is always induced.

**Pure verdict: KNOWN (method), PARTLY OWNED.**
- The transport is Atserias–Kolaitis Lemma 15 (fix the deleted attribute at u₀), with Lemma 16
  for edges that shrink to one coordinate. Locating the induced cycle is Lemma 14.
- A–K state the transport for K-relations. Its use here is a direct transposition: preimage
  instead of padding. An expert would call it obvious once the base witness is in hand.
- **Residual:** none beyond the base witness, which is `thm.countable_witness` (ring, Lean,
  audited separately: 3 passes, no owner).

**Type 3:** FAIL. The method is imported, not exported. No technique moves out of the carrier
setting.

**Type 4:** FAIL. The statement is fully expressible in standard words: "if the marginal scheme has
an induced C_{L≥4}, there is a non-coherent two-valued charge on the generated σ-class".

**Referee estimate:** REJECT-LIKELY as a stand-alone item. As a lemma inside a paper whose main
result is the base witness it is fine, provided A–K Lemma 15 is credited.
- Venue class: none (lemma).
- Value carried by: none.
- Main risk a referee would raise: "this is the standard padding reduction (A–K Lemma 15 / BFMY)".

**Proposed `status`:**
> proved-hand (from Lean ring witness). AUDIT G6 2026-10-27: transport = Atserias-Kolaitis arXiv:2009.09488 Lemma 15 (constant padding) + Lemma 16 + Lemma 14 (induced C_{>=4}), primary read; KNOWN as method, residual = base witness thm.countable_witness only. Type 3 FAIL, Type 4 FAIL. Credit A-K when stated.

---

## 3. obs.forced_functional

**The statement, stripped.**
- (i) Finitely built questions have indicators in the span of window functions. This is trivial:
  complement is 1 minus a sum, and a disjoint union is a sum.
- (ii) Λ = Σₖ lim_{uₖ} fₖ is well defined on that span.
- (iii) Any extending state equals Λ there. So Λ ∈ {0,1} is necessary.

**Hand check ⟦HAND⟧. The entry's scope "triangle and cycles" is needlessly narrow.**
- **Setup.** Take any simple graph and anchor a value a ∈ X. Each window function splits as
  f_e = f̃_e + (single-coordinate terms) + constant, where
  f̃_e = f_e − f_e(a,·) − f_e(·,a) + f_e(a,a) vanishes whenever either coordinate is a.
- **Interactions vanish.** Suppose Σ_e f_e ≡ 0. Fix every coordinate outside e = {i,j} at a. Every
  other edge's interaction term then vanishes. So f̃_e equals a sum of single-coordinate
  functions plus a constant, and since f̃_e vanishes when either coordinate is a, f̃_e ≡ 0.
- **The rest cancels.** What remains is Σᵢ Φᵢ(xᵢ) + C ≡ 0, so each Φᵢ is a constant cᵢ with
  Σcᵢ + C = 0. Single-coordinate limits depend only on the shared marginals pᵢ, so Λ = 0.

Well-definedness therefore holds for any compatible family on any graph. It is the uniqueness of
the pair-interaction (ANOVA / hierarchical log-linear) decomposition, which is folklore. I did not
locate a page reference.

**Pure verdict: KNOWN (trivial consequence of standard techniques).**
- The span-of-contexts linear functional is the infinite-outcome, finitely additive analogue of
  the signed global section of Abramsky–Brandenburger 2011 Thm 5.9: no-signalling ⇒ a signed
  extension exists. On the span of context functions any such extension is unique, and it equals
  Λ.
- The kernel lemma above is folklore. The KNOWN verdict is not subject to the NOVEL cap.

**Type 3:** FAIL. **Type 4:** FAIL. Λ is the expectation under the signed global section,
restricted to the span.

**Referee estimate:** REJECT-LIKELY stand-alone (observation).
- Venue class: none.
- Value carried by: none.
- Main risk a referee would raise: "signed extension / log-linear identifiability; one line".

**Proposed `status`:**
> proved-hand; KNOWN-trivial (AUDIT G6 2026-10-27): Lambda = restriction of the signed global section (Abramsky-Brandenburger 2011 Thm 5.9, primary) to the span of window functions; well-definedness = pair-interaction decomposition uniqueness, holds on ANY graph (hand check in G6 §3), not just triangle/cycles. Widen scope; cite AB 5.9.

---

## 4. obs.cut_the_loop

**The statement, stripped.** Take the cycle with uₖ = p⊗p in cyclic orientation and fix k. Then
Λ − W^{(k)} = δₖ, the commutator lim_a lim_b fₖ − lim_b lim_a fₖ on window k. Hence:
- W^{(j)} − W^{(k)} = δₖ − δⱼ, a coboundary-type relation;
- Λ ∈ {0,1} whenever some window part vanishes.

**What is owned.**
- Non-commutativity of the iterated p-limits (p⊗q ≠ q⊗p; the Fubini failure for charges) is
  `own.ultrafilter_products` (Goldberg; Hindman–Strauss; Dubins; Schervish–Seidenfeld–Kadane).
- Cutting a cycle into a path to glue, and measuring the obstruction on the cut edge, is the
  standard holonomy/Čech picture (Abramsky–Mansfield–Barbosa 2011, cocycle obstructions; Penrose
  1991).
- The formula itself is a two-line subtraction (the note's proof is two lines).

**Not found.** An explicit "Λ = glued ultrafilter + one-window commutator" formula for charges.
The cohomology papers on the shelf have no infinite or finitely additive content (grep).

**Pure verdict: UNCLEAR, leaning KNOWN (folklore-level computation).**
- The ingredients are owned. The formula is a direct consequence once Λ is defined.
- Unread nearest sources:
  - Hindman–Strauss on iterated limits (already on the triangle audit's unread list);
  - the body of Abramsky–Mansfield–Barbosa 2011 (grep only).
- The cap applies: it cannot be NOVEL.

**Type 3:** UNCLEAR, and its value is internal. This is the one item in the batch with
method-transfer *potential*: holonomy/cocycle language becomes a computable gauge-invariant δₖ on
charges. `thm.ring_conceptual` uses it to explain `mu_cases`. That is transfer inside the
programme, not between fields. FAIL until a use outside the programme exists.

**Type 4:** PASS-pending on the three-statements test, as statements:
- "δ is a cocycle";
- "Λ ∈ {0,1} iff no window has a same-sign twist on every window";
- "rings: cut where the question is not looking".

The one non-trivial result is `thm.ring_conceptual`. The vocabulary is standard (holonomy,
commutator of limits), so this is FAIL as vocabulary but PASS as statements. That matches the
triangle audit's verdict.

**Referee estimate:** BORDERLINE (capped by UNCLEAR) as an explanatory device inside a paper.
- Venue class: none stand-alone.
- Value carried by: factor 3, organising, if the ring proof is presented through it.
- Main risk a referee would raise: "routine once Λ is defined".

**Proposed `status`:**
> proved-hand; UNCLEAR-leaning-KNOWN (AUDIT G6 2026-10-27): ingredients = own.ultrafilter_products + Cech/holonomy cut (Abramsky-Mansfield-Barbosa 2011, grep-level); explicit charge formula not found; unread: Hindman-Strauss iterated limits, AMB 2011 body. Value = internal explanation of mu_cases (thm.ring_conceptual). Type 3 FAIL (internal only), Type 4 statements PASS-pending.

---

## 5. Combined statement "pointless ⟺ window graph not a forest" (note §Triangle, App. status)

**Assembly check ⟦HAND, re-checked⟧. Correct as stated** (pair windows, X = ℕ).
- **⇐.** A non-forest has a cycle. Its shortest cycle is induced, of length 3 or ≥ 4. Use the
  triangle witness (Lean) or the ring witness (Lean), then `thm.loops_travel`.
- **⇒.** On a forest, every state is an ideal point (`thm.path` = locality (`thm.shape_lemma`) +
  ultrafilter gluing).

**Pure verdict: PARTLY OWNED, residual UNCLEAR.**

Owned:
- the line, forest vs not ≡ α-acyclic for 2-uniform schemes (Vorob'ev; BFMY Thm 3.4; A–K
  Thm 3/4);
- the reduction to the two minimal obstructions, triangle and induced C_{≥4} (A–K Lemmas 13, 14);
- the transport (A–K Lemmas 15, 16);
- the tree direction's gluing step, which is β preserving weak pullbacks (nLab "taut functor",
  snippet; the linked proof is unread). This also covers `thm.amalgamation`, recorded as "folklore,
  not located".

Residual, in the two-valued finitely additive Dynkin semantics:
- (a) the ring base witness (`thm.countable_witness`, Lean; no owner in 3 passes);
- (b) the triangle base witness (`thm.triangle_pointless`, Lean; UNCLEAR, with an unread list:
  Bhaskara Rao body, Gudder SIAM Rev 1984, Hindman–Strauss, Blass, Pták–Pulmannová,
  Ovchinnikov PAMS 1999);
- (c) the tree direction's lift from window families to *states on the whole carrier*, which
  needs the locality lemma (`thm.shape_lemma`, hand + finite-alphabet machine check). This step
  has no K-relation analogue, because A–K work with families, not carriers.

**Why UNCLEAR rather than NOVEL.** The cap applies. Residual (b) inherits the triangle audit's
unread list. The charge-extension literature nearest to (c), Basile–Bhaskara Rao–Shortt 1994 and
Shortt 1983, is unread.

**A structural observation worth keeping** (theory content, not novelty).
- Xu–Cabello's line is chordal vs not because their contexts are cliques: a triangle of pairwise
  compatible measurements counts as one context. Our line is forest vs not because pair windows
  are *non-conformal* on a triangle.
- The difference between the two lines is exactly A–K's non-conformal case, which is also the
  note's "a window covering the whole triangle makes the carrier Boolean". So the triangle column
  of the note's table is precisely the conformality column.

**Type 3: UNCLEAR, the one live candidate.**
- The A–K architecture (acyclic ⟺ local-to-global) transfers to a semantics that is *not* a
  semiring annotation: compatible ultrafilters / two-valued charges, where β replaces the
  K-relation functor.
- A genuine transfer would export the result. One form: "for any Set-functor F preserving weak
  pullbacks, with obstructions on the triangle and C_L, local-to-global ⟺ forest". Another: a
  monoid in the sense of Atserias–Kolaitis' consistency-monoids follow-up where acyclicity
  *fails* to suffice.
- Not demonstrated, so currently FAIL. Flip condition: state and prove the functorial version, or
  place β relative to A–K's monoid characterisation (the consistency-monoids paper is unread).

**Type 4:** FAIL as vocabulary. Standard form: "a non-coherent two-valued charge on the σ-class
generated by pair-coordinate σ-algebras exists ⟺ the marginal scheme is not α-acyclic".

**Referee estimate:** BORDERLINE (capped).
- Venue class: short note / letters, as "Vorob'ev's theorem for two-valued charges".
- Value carried by: factor 1 (base witnesses) + factor 3.
- Main risk a referee would raise: "the line and the reduction are Vorob'ev/BFMY/Atserias–Kolaitis;
  only the base witnesses are new, and the triangle witness's novelty is not settled".

---

## 6. Proposed taxonomy changes (not applied)

**New / extended `owned_regions` entry:**
```json
{
  "id": "own.acyclic_line_and_reduction",
  "name": "Forest/acyclic dividing line and its reduction to triangle + induced C_{>=4} with constant-padding transport",
  "status": "OWNS the line, the minimal-obstruction reduction and the transport; NOT the two-valued finitely additive base witnesses (audit G6 2026-10-27)",
  "one_line": "For pair windows, alpha-acyclic = conformal + chordal = forest. Local-to-global consistency holds iff acyclic for probability (Vorob'ev 1962), relations (BFMY 1983 Thm 3.4) and positive-semiring K-relations (Atserias-Kolaitis Thm 3/4). The converse proof reduces to minimal non-conformal (graphs: triangle; Lemma 13) or minimal non-chordal (induced cycle >= 4; Lemma 14) and transports by fixing deleted attributes at a constant (Lemma 15) and dropping covered edges (Lemma 16) = thm.loops_travel's psi. One uniform ordinary-relation counterexample works for all positive semirings. Neighbour: Xu-Cabello 2019 (contexts = cliques, so the line is chordality; the gap is A-K's non-conformal case = our triangle).",
  "detail": "entry_audits/G6_loops_travel.md",
  "owned_by": {
    "cite": "Atserias-Kolaitis arXiv:2009.09488, Thm 3, Thm 4, Lemmas 12-16; Beeri-Fagin-Maier-Yannakakis JACM 30 (1983) Thm 3.4; Vorob'ev, Theory Probab. Appl. 7 (1962); neighbour Xu-Cabello PRA 99 020103 (2019)",
    "region": "local-to-global consistency vs hypergraph acyclicity; reduction and padding transport",
    "verified": "A-K pp. 25-31 primary (2026-10-27); BFMY and Vorob'ev via A-K; Xu-Cabello abstract",
    "detail": "entry_audits/G6_loops_travel.md"
  }
}
```

**Optional region for gluing** (owns `thm.amalgamation`; the cap says it should be checked
first):
```json
{
  "id": "own.beta_weak_pullbacks",
  "name": "ultrafilter functor preserves weak pullbacks (= two-window ultrafilter gluing)",
  "status": "LIKELY OWNS thm.amalgamation (snippet level)",
  "owned_by": {
    "cite": "nLab 'taut functor' (beta is taut; preserves weak pullbacks, proof linked); Gumm, Functors for Coalgebras (filter functor, neighbour); charges: Basile-Bhaskara Rao-Shortt PAMS 121 (1994) 137-143 (unread)",
    "region": "gluing of ultrafilters / charges along a shared marginal",
    "verified": "search snippet only; linked proof unread"
  }
}
```

**Status lines:** as in §2–4.

**Further proposals:**
- `conj.invariant_any_cycle`: the status is stale. It still reads "open (evidence withdrawn
  2026-10-16)", but the triangle is Lean-checked (2026-10-17). Proposed status:
  "PROVED-hand assembly from Lean triangle + Lean ring + thm.loops_travel + thm.path; line and
  reduction OWNED (own.acyclic_line_and_reduction); residual = base witnesses."
- `conj.invariant_cycle_ge4` is then refuted (triangles carry pointless states). Mark it as
  REFUTED by `thm.triangle_pointless`.
- `obs.forced_functional` scope: widen to "any graph; finitely built questions (all questions on
  triangle-free graphs)".
- `pointless_coherence.tex` (author's call). In the coda, add a bullet saying that the converse
  (cycle ⇒ obstruction), its reduction to triangle + induced C_{≥4}, and the padding transport are
  Vorob'ev/BFMY/Atserias–Kolaitis. In §Why loops, "Loops travel", credit A–K Lemma 15. Narrow
  "None of them covers…" to "none covers the two-valued finitely additive *base cases*".
- SHELF_INDEX (owed): set the A–K `summary_basis` to "read (pp. 25–31: Thm 3 proof, Lemmas
  13–16)". Fix the dangling `own.acyclic_gluing` link to the new region id.

## 7. Unread sources that block any upgrade
- Basile–Bhaskara Rao–Shortt, PAMS 121 (1994), and Shortt 1983: charge common extensions, the
  nearest to residual (c).
- Atserias–Kolaitis, "Consistency of relations over monoids" (cs.upc.edu/~atserias): where
  acyclicity fails to suffice. This is the Type 3 flip.
- The nLab-linked proof that β preserves weak pullbacks.
- Everything on the triangle audit's unread list, for residual (b).
