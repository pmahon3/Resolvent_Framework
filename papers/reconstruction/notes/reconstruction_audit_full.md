# Audit: reconstruction (mode: full) — hostile prior-art referee

**Method.** Every claim below was resolved against the OpenAlex citation graph
(works/authors/citations) and arXiv, not web-search snippets. Citation anchors
verified by title→author→year resolution; survivor-novelty claims tested by
hostile forward/relevance search under every plausible name. Where a cited work
is not indexed by OpenAlex, that is recorded as *not indexed* — distinct from
*does not exist*.

---

## Declared contribution type(s)

Per `notes/STATUS.md`: **Type 6** (bridge/translation) as the floor, **clearing
Type 3** (unifying framework) *only if* parity/winding are unobtainable without
the EA/PR framework. The trichotomy also implicitly asserts a **Type 5**
(impossibility) result. The paper's own §"What is new, and what is borrowed"
already concedes the polyhedral core is classical. This audit tests whether that
self-positioning survives the citation graph.

---

## Pure verdict: **KNOWN** (polyhedral core) / **NOVEL** (dynamical layer + winding criterion)

The paper is honestly positioned and the positioning holds. Splitting by result:

### Confirmed KNOWN — cited correctly
- **Prop. (commensurability is C=R)** = local/marginal polytope gap.
  Wainwright–Jordan (OpenAlex W2120340025, doi:10.1561/9781601981851,
  indexed year 2007; tree-exactness). Correct.
- **Thm (acyclic ⟹ tame)** = **Vorob'ev 1962** (resolved,
  doi:10.1137/1107014, W2059858750; regularity ⇔ α-acyclicity), with the DB mirror
  Beeri–Fagin–Maier–Yannakakis 1983 and the cross-field identification via
  Abramsky (2013). Correct and disclaimed ("claim no novelty").
- **Thm (variety-typed ⟹ universal)** = De Loera–Onn 2004 + Průša–Werner 2015 +
  Pitowsky 1991 NP-completeness floor + Avis–Imai–Ito–Sasaki 2005 covariance
  map. All four resolve with correct authorship. This is a **Type 5 impossibility
  that is already in the literature** — it is cited as such, not claimed novel.
- **Parity mechanism** = stable-set integrality: Nemhauser–Trotter 1974,
  Chvátal 1975, Hoffman–Kruskal 1956. All resolve, correct.

### KNOWN obstruction the paper UNDER-cites — mandatory addition
- **The parity theorem's obstruction is the n-cycle noncontextuality
  inequality.** Araújo, Quintino, Budroni, Terra Cunha & Cabello, *All
  noncontextuality inequalities for the n-cycle scenario*, **Phys. Rev. A 88,
  022118 (2013)**, doi:10.1103/physreva.88.022118 (162 citations). This paper
  gives the complete H-description of the noncontextual polytope for n dichotomic
  observables with consecutive joint measurability, of which **KCBS (n=5) is one
  case and the even/odd split is the organizing dichotomy**. The reconstruction
  paper cites only KCBS 2008 (the n=5 witness) and the pentagon remark; it does
  **not** cite the general n-cycle characterization that most directly owns the
  odd/even parity phenomenon. **This is the single most important missing
  citation.** The parity theorem's *mathematical* content (golden-mean ring
  commensurable iff L even) is a special-language instance of a known
  characterization; what remains the paper's own is the **dynamical route**
  (recurrence on a subshift, odd-period orbits) — which the paper itself frames
  as "distinct observational routes to one polyhedral obstruction"
  (Remark, dynamical reading). That framing is exactly right and must now carry
  the Araújo et al. citation to be defensible.

### Genuine survivors — NOVEL, no prior art found
- **Winding / primitive-orbit criterion + covering-space proof**
  (Thm, winding characterisation; Lemma, layer-injectivity discriminant).
  Hostile search across {winding number, covering space, cohomology} ×
  {contextuality, marginal polytope, global section} returned the cohomological-
  obstruction neighbours — Abramsky–Barbosa *Contextuality, Cohomology and
  Paradox* (2015), Carù (2019, topological contextuality), Montanhano (2021,
  semi-module Čech cohomology of contextuality) — but **none states a
  winding-number / layer-injective-simple-cycle decidability criterion** for the
  marginal obstruction over a layered ring. The covering-space reading of a
  cyclic protocol as an unresolved cover of time is not in the
  marginal-problem, contextuality-cohomology, or CSP literatures I searched.
  **This survives as the paper's real theorem.** The Lean-certified discriminant
  (WindingInjectivity.lean, 0 sorry) is a correctness credential, not a
  novelty claim, and is appropriately scoped.
- **Circuit-Localization assembly** (loopless symmetric case, proved). The
  assembly of the taming catalogue into a localisation structure theory has no
  single owner. But see the Type-3 caveat below on the tightness line.

---

## Applied verdict: not evaluated
This is a pure-mathematics / foundations contribution; the `applied` bar
(computational comparison on N systems) is not the relevant gate. The paper's
"decidable criterion" claim is a complexity statement, adjudicated under Type 5,
not a practitioner-tool claim.

---

## Contribution-type verdicts

### Type 6 (bridge / exposition-translation): **PASS**
Named audience (symbolic-dynamics / ergodic-theory readers who do not read the
marginal-problem, contextuality, or CSP-tightness literatures); the translation
does non-trivial conceptual work (EA/PR framing of symbolic-dynamical protocols;
recurrence-as-cyclic-time). This bar is cleared cleanly. **It is the paper's
secure floor.**

### Type 3 (unifying framework enabling method transfer): **CONDITIONAL PASS**
The STATUS.md self-test — "are parity + winding re-derivable directly in
stable-set / graphical-models language?" — splits:
- **Parity: YES, re-derivable.** The paper's own proof runs through
  FSTAB(C_L)/STAB(C_L) and total unimodularity — pure stable-set language — and
  the obstruction is the known n-cycle inequality (Araújo et al.). Parity alone
  ⟹ Type 6, not Type 3.
- **Winding: NO obvious re-derivation.** The covering-space criterion is where a
  method genuinely transfers (algebraic-topology winding number → decidable
  contextuality criterion) and where nothing equivalent was found. This is the
  one component that can carry Type 3.
**Verdict:** Type 3 clears *on the strength of the winding criterion only*, and
only for the proved (loopless / odd-golden-mean) scale. The universal version
rests on the **open** universal-impossibility + pruning conjectures (§open, with
the named k=2 phase gap) and must not be counted toward Type 3 until proved.

### Type 5 (impossibility / counterexample): **FAIL as novelty**
The proved impossibility (variety-typed universality ⟹ no finite facet taxonomy,
NP-complete at 3 contexts) is **De Loera–Onn + Průša–Werner + Pitowsky**,
correctly cited. It does not clear Type 5 as a *new* impossibility. The
*conjectured* universal impossibility is unproved. No Type 5 novelty credit.

---

## Cross-reference

Known components (polyhedral core, n-cycle obstruction) + genuinely novel
assembly and winding criterion + honest conjecture fencing. The Type 6 bridge
clears independently; Type 3 clears narrowly through the winding criterion at
proved scale. This matches the paper's own headline — the audit **confirms** the
self-positioning rather than overturning it, and hardens it with two citation
requirements.

---

## Mandatory citation actions (from the citation graph)

1. **ADD Araújo, Quintino, Budroni, Terra Cunha, Cabello 2013**, *All
   noncontextuality inequalities for the n-cycle scenario*, Phys. Rev. A 88,
   022118, doi:10.1103/physreva.88.022118. The parity theorem must cite the
   general n-cycle characterization, not only KCBS (n=5). Without it the parity
   result reads as more novel than it is and a referee will catch it.
2. **DIFFERENTIATE from Weller 2016**, *Characterizing Tightness of LP
   Relaxations by Forbidding Signed Minors* (doi:10.17863/cam.162) and Weller,
   Rowland, Sontag 2016, *Tightness of LP Relaxations for Almost Balanced
   Models*. These characterize local-marginal-polytope tightness by graph
   structure (forbidden signed minors) — the same territory as Circuit
   Localization / signability. The paper cites Barto–Kozik and Thapper–Živný but
   **not Weller**; the signable/TU tamings are plausibly Weller's balanced-model
   / signed-minor conditions in dynamical dress. Differentiate explicitly or the
   Type-3 method-transfer claim for the tamings is exposed.
3. **OPTIONAL, worth a line:** Choudhary & Barbosa 2024, *Exclusivity principle,
   Ramsey theory, and n-cycle PR boxes* (arXiv:2411.09773) — current work on
   n-cycle PR boxes, directly adjacent to the odd-ring PR-box corollary.

## Citation-hygiene confirmations

- **Anchor resolution:** 14 of 17 references resolve on OpenAlex with matching
  first-author surname; the other 3 are real but not indexed (see next bullet).
  All 17 are correctly attributed. Of the 14 resolved, 4 show OpenAlex's indexed
  year differing from the bib year (WainwrightJordan 2007 vs 2008; PrusaWerner
  2013 vs 2015; HoffmanKruskal 2009-reprint vs 1956; ThapperZivny 2013-preprint
  vs 2016) — these are preprint/reprint/index-year differences, **not** bib
  errors; the bib years are the correct publication years. The attribution
  landmine flagged in STATUS.md is
  **handled correctly** in the draft: signability⇒TU is attributed to the
  **Hoffman–Gale appendix to Heller–Tompkins 1956**, not the main text.
- **Not indexed in OpenAlex (real references, not errors):** Abramsky 2013
  (*Relational databases and Bell's theorem*, Festschrift chapter,
  arXiv:1208.6416); Heller–Tompkins 1956 (*Ann. Math. Stud.* 38); Ghouila-Houri
  1962 (*C. R. Acad. Sci.* 254). All three are standard, correctly attributed,
  and simply absent from OpenAlex's index (book chapter / old French note). Do
  not "fix" these — they are correct.

---

## Recommendation

**PROCEED to full proofs (Phase 4→5), with the self-positioning kept explicit in
the paper and two citations added.** The paper already states its verdict
honestly; the citation graph confirms it. Required before drafting proofs:
(1) add Araújo et al. 2013 to the parity theorem; (2) add a Weller
differentiation paragraph to the tamings / Circuit-Localization section. The
winding criterion is the defensible core — prioritize its complete proof and
keep it independent of the §open conjectures (as the draft already does). Do not
let the universal-impossibility conjecture harden into a Type-5 claim until the
k=2 phase gap in the pruning lemma is closed.
