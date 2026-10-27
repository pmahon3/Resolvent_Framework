---
reviewed: false
date: 2026-10-27
audit: /audit pure, THEORY-ITEMS mode, entry level (skill v2.1 entry-level cap)
collection: glued_carriers_taxonomy.json
entries: thm.amalgamation, thm.path, thm.shape_lemma, thm.flat_iff_ideal
---

# G5: the forest side. Entry-level pure audit

**Puzzle (what is audited).** Windows look at pairs of coordinates. Each window gives a yes/no
answer to every question about its pair, and neighbouring windows agree on the coordinate they
share. If the windows form a tree, is there always one ultrafilter "world" that gives all these
answers? And when there is no triangle, does every question you can build from window questions
(by "not" and "either-one") stay local to a star of windows?

**Bottom line.**

| entry | pure verdict | owner(s) | Type 3 | Type 4 | referee estimate |
|---|---|---|---|---|---|
| thm.amalgamation | **KNOWN (OWNED)** | β satisfies Beck–Chevalley (weak-pullback preservation); compatibility theorem for charges, filter case | FAIL | FAIL | REJECT-LIKELY if claimed; fine as a cited lemma |
| thm.path | **PARTLY OWNED** | gluing step = iterated Beck–Chevalley, and Vorob'ev/BFMY in the σ-additive case. Residual = the shape lemma | FAIL | FAIL alone | BORDERLINE (inherits the shape lemma's cap) |
| thm.shape_lemma | **UNCLEAR** (no owner found; nearest sources unread) | neighbours: Greechie loop lemma, Helly/BFMY, σ-class school | FAIL | supporting only | BORDERLINE |
| thm.flat_iff_ideal | **KNOWN (trivial corollary + rename)** | "flat" = global section (Abramsky–Brandenburger; van den Berg–Heunen) | FAIL | FAIL | REJECT-LIKELY if claimed |

The whole forest side reduces to one unowned item: **the star normal form of the Dynkin carrier
on triangle-free window graphs (thm.shape_lemma)**. Everything else is either owned or a
one-line consequence.

---

## 1. thm.amalgamation (ultrafilter gluing over a shared coordinate)

**Stripped statement.** Let u be an ultrafilter on X×Y and v an ultrafilter on Y×Z, with the
same image on Y. Then some ultrafilter w on X×Y×Z projects to u and to v.

**Verdict: KNOWN (OWNED).** Replace the taxonomy's "folklore; not located" record.

**Owners.**
1. *The ultrafilter functor β satisfies the Beck–Chevalley condition*, i.e. it sends pullbacks
   to weak pullbacks. The canonical map β(R ×_Y S) → β(R) ×_{βY} β(S) is surjective. Take
   R = X×Y and S = Y×Z with the projections to Y. Then R ×_Y S = X×Y×Z, and surjectivity is
   exactly this lemma.
   - nLab, "relational β-module", Proposition (BC). Statement and proof read in full (page
     source fetched 2026-10-27). The proof uses the same move as ours: g(A) and h(B) both lie in
     the common image ultrafilter J, so they meet. **Read level: full proof (secondary
     source).**
   - Barr, "Relational algebras", LNM 137 (1970) 39–55. Primary source, OCR text read. Barr
     *uses* the fact (Prop. 5.2: "there is an ultrafilter on … whose projections are …") and sets
     up T(f⁻¹g) versus Tf⁻¹·Tg for pullbacks in §1. In the OCR text he does not *state* it as a
     lemma for β. Credit Barr for the use and the nLab/Monoidal Topology line for the statement.
   - Hofmann–Seal–Tholen (eds.), *Monoidal Topology* (CUP 2014), and Clementino–Hofmann–Tholen
     2004: β satisfies BC. **Read level: search snippet only. Not opened.**
2. *Compatibility theorem for finitely additive measures* (Guy 1961; Bhaskara Rao & Bhaskara Rao
   1983, Ch. 3; Kindler 1988). Two charges on subalgebras B₀ and B₁ extend jointly iff
   a ≤ a′ ⇒ Ξ₀(a) ≤ Ξ₁(a′). Cardona–Mejía–Uribe-Zapata, arXiv:2503.08910, Thm 3.12, give a
   self-contained proof (read). They also remark, of several measures: "The case of filters is easy
   thanks to the finite intersection property" (§3.2, read). Shelah [She00, Prop 1.3(3)] covers
   two compatible measures when one is a filter. **Read level: CMU-Z Thm 3.12 and the remark,
   full text. Bhaskara Rao book body: unread.**

**Hostile check.** Is our lemma more than the BC instance? No. It is the BC instance for product
projections, and its proof is the same FIP argument.

**Type 3: FAIL.** It is an ingredient; no method moves between domains. **Type 4: FAIL.** It
introduces no vocabulary.

**Referee estimate.** REJECT-LIKELY if presented as new. As a cited lemma it is fine.
Venue class: none. Value carried by: none. Main risk a referee would raise: "β preserves weak
pullbacks (Barr 1970 / BC); cite it."

**Proposed `status`:** `"proved-hand; OWNED (beta satisfies Beck-Chevalley: nLab relational
beta-module Prop BC, Barr 1970, Hofmann-Seal-Tholen 2014; filter case of the charge
compatibility theorem, CMU-Z 2025 Thm 3.12) - cite, do not claim"`

**Replace the entry's `owned_by` with:**
```json
"owned_by": {
  "cite": "Barr, Relational algebras, LNM 137 (1970) 39-55 (uses it); nLab 'relational beta-module', Prop (BC) (statement+proof); Hofmann-Seal-Tholen, Monoidal Topology (CUP 2014); filter case of the charge compatibility theorem (Guy 1961; Bhaskara Rao 1983 Ch. 3; Cardona-Mejia-Uribe-Zapata arXiv:2503.08910 Thm 3.12 and Sec. 3.2 remark)",
  "region": "gluing two ultrafilters with a common marginal = beta sends pullbacks to weak pullbacks",
  "verified": "nLab proof read in full; Barr OCR read (use, not stated as a lemma); CMU-Z Thm 3.12 read; HST and Bhaskara Rao body NOT opened",
  "detail": "entry_audits/G5_forest_side.md §1"
}
```

**WHY line.** Two views that agree on what they share always fit one world, even under finite
additivity. A gluing needs no centre, only an overlap. This is owned and is the base case of
"local views add up".

---

## 2. thm.path (forest window graph ⇒ every state is an ideal point)

**Stripped statement.** Ω = X^V with V finite. D is the Dynkin closure of the pair-window cylinder
algebras on a forest. Every finitely additive {0,1}-valued s on D equals E ↦ [E ∈ W] for some
ultrafilter W on Ω.

**Proof anatomy.**
- (a) Glue the window ultrafilters along the tree order. This is thm.amalgamation, iterated.
- (b) Show that s is determined by window ultrafilters on all of D. This is thm.shape_lemma.

**Verdict: PARTLY OWNED.** Residual: step (b), i.e. the shape lemma (§3).
- (a) is owned. Iterating BC along a tree order gives a weak limit for tree-shaped diagrams.
  The σ-additive analogue is Vorob'ev 1962 and BFMY 1983 (`own.vorobev_acyclic`). The semiring
  version (pairwise consistent ⇒ globally consistent iff acyclic) is Atserias–Kolaitis
  arXiv:2009.09488 (shelf; abstract level). The **charge** version also follows from the
  compatibility theorem, applied one window at a time ⟦HAND⟧:
  - a ∈ (algebra generated by the earlier windows), a′ a cylinder on {p, new} with p old, and
    a ≤ a′;
  - then a ⊆ {ω_p ∈ C}, where C = {y : {y}×X_new ⊆ B′};
  - so Ξ₀(a) ≤ m_p(C) ≤ Ξ₁(a′), given equal p-marginals.

  So **every compatible family of window charges on a forest extends to a charge on the generated
  algebra, hence on P(Ω)**. This pre-empts any future "finitely additive probabilistic forests"
  claim. It is owned through the compatibility theorem, with this reduction ⟦HAND⟧.
- (b) is what makes the result about states on **D**, which is not an algebra, rather than on the
  generated algebra. Without (b), a finitely additive s on D need not agree with W on countable
  disjoint unions. Nothing found owns (b); see §3.

**Type 3: FAIL.** No transfer: (a) is the classical acyclic-gluing technique, applied unchanged.
**Type 4: FAIL alone.** Statable in standard vocabulary: "every two-valued charge on the Dynkin
system generated by the forest's coordinate algebras is coherent / ultrafilter-induced".

**Referee estimate.** BORDERLINE (capped: the residual's pure verdict is UNCLEAR). Venue class:
short note at best, together with the shape lemma. Value carried by: factor 1, if (b) survives.
Main risk a referee would raise: "acyclic gluing is Vorob'ev/BFMY/Barr; the only content is the
Dynkin normal form; is that in the concrete-logic literature?"

**Proposed `status`:** `"proved-hand; PARTLY OWNED: gluing = iterated Beck-Chevalley for beta
(own.beta_beck_chevalley) / Vorob'ev-BFMY (sigma) / charge compatibility (finitely additive,
HAND reduction); residual = thm.shape_lemma (UNCLEAR)"`

**WHY line.** No loop, no twist: along a tree, local agreement always adds up to one (ideal)
world, even at finite additivity. That half is classical. The new part is only that the
buildable questions themselves stay local.

---

## 3. thm.shape_lemma (triangle-free ⇒ star normal form of D)

**Stripped statement.** V is finite, Ω = X^V, and the pair-window graph G is triangle-free
(equivalently, the 2-element windows form a Helly family). Then the Dynkin system generated by
the window cylinder algebras equals
G* = {disjoint unions of at most one cylinder per window, with the non-empty pieces on a star}.
Hence every finitely additive {0,1} state is s(E) = Σᵢ u_{wᵢ}(Eᵢ).

**Proof check (entry level).** I checked the hand proof ⟦HAND — re-checked by auditor, not
Lean⟧:
- **Rigidity.** Non-empty cylinders on disjoint windows meet. Pairwise-intersecting edges in a
  triangle-free graph form a star.
- **Slicing.** On a star at c, the slices at x_c = a are cylinders in distinct leaf
  coordinates. Disjoint non-empty cylinders in independent coordinates are impossible, so at
  most one slice is non-empty. The complement therefore slices into one leaf cylinder.
- **Closure.** Countable disjoint unions regroup window by window, and a union of cylinders on
  one window is again a window cylinder (A ⊆ X² is arbitrary).
- **Finiteness.** V is finite, so a state's sum is finite.

The proof is sound. The scope is pair windows with V finite. The script
`../verification/glued_helly_check.py` agrees on 8 graphs; I did not re-run it.

**Verdict: UNCLEAR.** No owner found. Under the entry-level cap, NOVEL is not available because
the nearest sources are unread.
- **Searched (web, standard):** "Dynkin system / λ-system generated by union of (independent)
  σ-algebras" with disjoint-union structure; Dynkin/marginal/ultrafilter/Vorob'ev combinations.
  Only textbook π-λ material came back.
- **Searched (shelf, by grep):** Pták, Pulmannová, Navara, Tkadlec, Gudder, Keleti, "pasting",
  "horizontal sum". Hits: `navara_1984` (full text read earlier, `own.navara_two_of_three`:
  describes C_{f,g} for two generators, a different regime); `tkadlec_1998`,
  `muller_ptak_tkadlec_1992` (covering properties; read); `buresova_ptak_sevic_2026` (states on
  two Boolean subalgebras extend simultaneously; Thm 2.3 for Boolean L is the compatibility
  theorem; statements grepped only).
- **Nearest neighbours (cite):**
  - Greechie loop lemma (Kalmbach 1983 §4 L9; read), via `own.greechie_loop`: pastings are OMPs
    iff no loop of order 3. Same shape, but for atoms shared between blocks, not for coordinate
    subalgebras.
  - Helly/conformal/BFMY combinatorics (`own.helly_hypergraphs`; read).
  - The σ-class school (`own.sigma_class_integral_additivity`; read).
  - The horizontal-sum fact for independent algebras is the rigidity step's ancestor.
- **Unread, would decide it:**
  - Pták–Pulmannová, *Orthomodular Structures as Quantum Logics* (book, 1991), chapters on
    concrete logics and pastings;
  - Gudder, SIAM Rev. 1984, Ex. 3.1;
  - Ovchinnikov, PAMS 1999;
  - Bhaskara Rao & Bhaskara Rao 1983, body;
  - Dvurečenskij–Neubrunn–Pulmannová 1992 (on shelf, `dvurecenskij_neubrunn_pulmannova_1992.pdf`,
    not grepped for this).

  These are exactly the gaps the taxonomy already lists.
- **Hostile "obvious" test.** An expert in concrete logics might call the rigidity step obvious.
  The full statement, that the Dynkin closure equals G* exactly and fails as soon as there is a
  triangle (70 vs 66 on the binary triangle), is a short but non-trivial normal form. It is
  folklore-risk MEDIUM.

**Type 3: FAIL.** Helly for 2-sets is a one-line fact, and "Helly ⇒ locality" is a lemma, not a
transfer of method. (`conj.helly_transfer_bfmy` is where a transfer would have to live.)
**Type 4: supporting only.** It is a theorem, not vocabulary. It is what makes the collection's
statements possible: D-states on triangle-free graphs correspond to compatible window-ultrafilter
families passing the extension test; this gives Λ on rings (thm.ring_conceptual) and the
loops-travel transport. Those statements, and the non-trivial ring result, are the collection's
Type-4 case. Score them at collection level, not here.

**Referee estimate.** BORDERLINE (cap: pure verdict UNCLEAR). Venue class: short note, inside a
paper whose main result is the ring/triangle side. Value carried by: factor 1 (small). Main risk
a referee would raise: "standard pasting / horizontal-sum argument from concrete-logic theory;
check Pták–Pulmannová."

**Proposed `status`:** `"proved-hand (auditor re-check 2026-10-27); machine-checked on finite
alphabets (8 graphs); pure UNCLEAR - no owner found, nearest unread: Ptak-Pulmannova 1991 book,
Gudder SIAM Rev 1984 Ex 3.1, Ovchinnikov PAMS 1999, Bhaskara Rao body; folklore risk MEDIUM;
this is the forest side's only unowned item"`

**Proposed neighbour region** (records the search, so it is not repeated):
```json
{
  "id": "own.dynkin_star_normal_form_search",
  "name": "Dynkin closure of coordinate-pair algebras: star normal form (searched, not found)",
  "status": "NEIGHBOURS ONLY (pass 2026-10-27); owner not found; nearest sources unread",
  "one_line": "No source found stating that the Dynkin system generated by pair-window cylinder algebras on a triangle-free graph is the family of star-shaped disjoint unions. Same shape as Greechie's loop lemma (order-3 loops) and the horizontal-sum fact for independent algebras; different objects.",
  "detail": "entry_audits/G5_forest_side.md §3",
  "owned_by": {
    "cite": "Greechie 1971 via Kalmbach 1983 §4 L9 (read); Navara 1984 (read; C_{f,g}, two generators); Tkadlec 1998, Muller-Ptak-Tkadlec 1992 (read); Buresova-Ptak-Sevic arXiv:2609.10770 (statements grepped)",
    "region": "pasting/concrete-logic neighbours of the star normal form",
    "verified": "neighbours read; UNREAD: Ptak-Pulmannova 1991 book, Gudder SIAM Rev 1984, Ovchinnikov PAMS 1999, Bhaskara Rao body, Dvurecenskij-Neubrunn-Pulmannova 1992"
  }
}
```

**WHY line.** With no triangle, every question you can build is local to one shared coordinate
and its neighbours: order needs no centre beyond a hub. A triangle is the first shape where a
buildable question escapes every star, and that is where pointlessness can enter.

---

## 4. thm.flat_iff_ideal (ideal point ⇔ flat window family)

**Stripped statement.** On a triangle-free graph, s is ultrafilter-induced iff some ultrafilter
on Ω projects to every window ultrafilter.
- (⇒) Restrict W to the windows.
- (⇐) W and s agree on window cylinders, hence on all of D by the shape lemma and finite
  additivity.

**Verdict: KNOWN (trivial corollary + rename).** The forward direction is the definition, and
the converse is one line from §3. "Flat family" means the compatible family has a **global
section**, which is a standard notion:
- Abramsky–Brandenburger, NJP 13 (2011) Thm 8.1 (on shelf, read), in the sheaf language;
- van den Berg–Heunen 2012 Prop 8 (read, via `own.stone_space_of_logic`), for compatible families
  of local Stone points.

So the content of the entry is "D-states on triangle-free graphs are non-contextual iff they are
ideal points", and that is just the shape lemma.

**Type 3: FAIL. Type 4: FAIL.** "Flat/twisted" renames "has / lacks a global section" (of
ultrafilters) and enables no new statement. Keep "flat" only as an alias, with the standard name
first.

**Referee estimate.** REJECT-LIKELY if claimed (central notion = an existing notion under a new
name). Venue class: none. Value carried by: none. Main risk a referee would raise: "this is the
global-section criterion."

**Proposed `status`:** `"proved-hand; KNOWN as a trivial corollary of thm.shape_lemma; 'flat' =
global section of the window-ultrafilter presheaf (Abramsky-Brandenburger 2011 Thm 8.1; van den
Berg-Heunen 2012 Prop 8) - alias only"`

```json
"owned_by": {
  "cite": "Abramsky-Brandenburger, NJP 13 (2011) 113036, Thm 8.1; van den Berg-Heunen 2012 Prop 8",
  "region": "'flat' window family = global section of compatible local data",
  "verified": "both read (shelf / own.stone_space_of_logic)",
  "detail": "entry_audits/G5_forest_side.md §4"
}
```

**WHY line.** "Adds up to one world" is the global-section condition. Naming it "flat" adds
nothing; the question lives in when sections exist, not in what they are called.

---

## 5. Proposed new owned regions (snippets for `owned_regions`)

```json
{
  "id": "own.beta_beck_chevalley",
  "name": "Ultrafilter gluing over a shared coordinate = beta preserves weak pullbacks",
  "status": "OWNS thm.amalgamation (pass 2026-10-27)",
  "one_line": "The canonical map beta(R x_Y S) -> beta(R) x_{beta Y} beta(S) is surjective (Beck-Chevalley for the ultrafilter functor). With R = XxY, S = YxZ this is thm.amalgamation; iterated along a tree order it is the gluing step of thm.path.",
  "detail": "entry_audits/G5_forest_side.md §1-2",
  "owned_by": {
    "cite": "Barr, LNM 137 (1970) 39-55; nLab 'relational beta-module' Prop (BC); Hofmann-Seal-Tholen, Monoidal Topology (CUP 2014); Clementino-Hofmann-Tholen 2004",
    "region": "joint ultrafilters with prescribed projections over a pullback",
    "verified": "nLab proof read in full; Barr OCR read (uses it in Prop 5.2, not stated as a lemma); HST/CHT not opened"
  }
}
```

```json
{
  "id": "own.charge_compatibility",
  "name": "Compatibility theorem for finitely additive measures (and its forest iteration)",
  "status": "OWNS finitely additive gluing along forests on the generated algebra (pass 2026-10-27; tree reduction HAND)",
  "one_line": "Two charges on subalgebras extend jointly iff a <= a' implies Xi0(a) <= Xi1(a'); the filter case is easy by FIP. For window cylinder algebras along a tree order the condition reduces to equal shared marginals (HAND), so compatible window charges on a forest extend to a charge on P(Omega). Says nothing about states on the Dynkin carrier D (that is thm.shape_lemma).",
  "detail": "entry_audits/G5_forest_side.md §2",
  "owned_by": {
    "cite": "Guy 1961; Bhaskara Rao & Bhaskara Rao, Theory of Charges (1983) Ch. 3; Kindler 1988; Cardona-Mejia-Uribe-Zapata arXiv:2503.08910 Thm 3.12 and Sec. 3.2; Shelah 2000 Prop 1.3(3) (filter case)",
    "region": "joint extension of finitely additive measures from two (or tree-many) subalgebras",
    "verified": "CMU-Z Thm 3.12 + remark read in full text; Bhaskara Rao body, Guy, Kindler, Shelah NOT opened"
  }
}
```

**Housekeeping flag.** `SHELF_INDEX.json` (Atserias–Kolaitis entry) links to
`own.acyclic_gluing`, but no region with that id exists in `glued_carriers_taxonomy.json`. The
nearest is `own.vorobev_acyclic`. Either add the id or repoint the link. I edited neither file.

## Sources consulted this pass
- nLab, relational β-module (source text): https://ncatlab.org/nlab/show/relational+beta-module
- nLab, taut functor: https://ncatlab.org/nlab/show/taut+functor
- Barr 1970 PDF: https://www.math.mcgill.ca/barr/papers/relalgs.pdf
- Cardona–Mejía–Uribe-Zapata, arXiv:2503.08910
- Atserias–Kolaitis, arXiv:2009.09488 (shelf entry; abstract)
- Hansel–Troallic, PTRF 71 (1986) 357–366 (marginal problem for charges; located, unread)
- Shelf: SHELF_INDEX.json, glued_carriers_taxonomy.json owned_regions,
  buresova_ptak_sevic_2026 (grepped)

Downloaded copies (Barr, CMU-Z) are in /tmp/g5dl and are not on the shelf. If kept, each needs a
SHELF_INDEX entry in the same commit.
