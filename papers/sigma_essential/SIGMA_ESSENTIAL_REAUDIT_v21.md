# Re-audit (v2.1, mode: full) of the σ-essential paper

reviewed: false. 2026-10-27. Auditor: Claude (Opus), fresh context, `/audit full` v2.1 (SKILL.md with the
REFEREE ESTIMATE and its caps), `contribution_evaluation.md`, `WHY.md`. Only this file was written.
Nothing was committed.

**Target:** `papers/sigma_essential/sigma_essential.tex` + `sigma_essential_body.tex` (15 pp compiled;
built 2026-10-07). The title is "A σ-Essential Contextual State in ZFC: Localization and the Product Ulam
Witness". Lean: `targetA_sharp_ZFC` (`Admissibility.lean`) and `psi_ZFC` (`UlamWitnessMain.lean`).

**Read levels.**
- **[R]** read in this pass;
- **[R-Lean]** Lean source read here, and `#print axioms` run here (`lake env lean`, 20 s, 1.8 GB peak);
- **[S]** a shelf entry or a repo read-record was consulted, but the source was not re-read;
- **[W]** web: abstract or metadata only;
- **[M]** memory or general knowledge, not re-checked;
- **[H]** ⟦HAND⟧ argument by this auditor, not in Lean.

Prose a hostile referee would object to is quoted from the paper.

## Audit: σ-essential paper (`papers/sigma_essential/`) (mode: full)

### Declared contribution type(s)
The paper declares none. Taken from `PHASE2_AUDIT_VERDICT.md`: Type 1 (main theorem), Type 1 (quotient
artifact), Type 5 (Ω₇).

### Pure Verdict: UNCLEAR
- Without essential irreducibility, the witness is a routine consequence of Binder–Navara 1987 Thm 4
  plus the known non-Dirac two-valued state on 4even (U-limit; §2.1).
- The residue (irreducibility mod countable, via the parity normal form) was not found in print.
- The likeliest owners are unread: Binder–Navara 1987, Navara 2000 §17, Pták–Pulmannová 1991.

### Applied Verdict: not evaluated (pure order theory).

### Contribution Type Verdicts
- Type 1 (main): **UNCLEAR**.
- Type 1 (quotient): **FAIL**.
- Type 5 (Ω₇): **FAIL**.
- Types 2/3/4/6, if read in: **FAIL** (§3).

### Cross-reference
Correctness of the witness stands. All of its novelty rests on essential irreducibility, which is
method-forced and unread against its owners. The framing contains false measurable-cardinal claims
(§1).

### Recommendation
**Needs deeper audit.** Shelve and read the three named sources. Apply the §4 fixes, and decide whether
the countable ring witness should replace the headline (§6b). Not dissemination-ready.

### Referee estimate: BORDERLINE
Venue class: research journal (as a short paper, quantum-logic / ordered-structures journals such as
Math. Slovaca, IJTP, Order).
Value carried by: factor 1 (small new theorem), conditional on irreducibility being accepted as the
point.
Main risk a referee would raise: "Binder–Navara carrier with X = 4even plus an ultrafilter limit; only
irreducibility is new, and it is unmotivated." This would be REJECT-LIKELY from a referee who knows
Binder–Navara, unless the paper is reframed.

---

## 0. Bottom line

| Item | Verdict |
|---|---|
| Correctness of the main theorem (items 1–2 of `thm:main`) | **Sound.** [R] by hand, and [R-Lean] `psi_ZFC` / `targetA_sharp_ZFC` use only `[propext, Classical.choice, Quot.sound]`. |
| **Mathematical error in the framing (new, required fix)** | **§2 obstruction (c), `rem:not-measurable` and `rem:strength` are FALSE as stated.** The countable–cocountable σ-algebra on ω₁ carries a non-Dirac σ-additive two-valued measure in ZFC [H]. |
| Pure novelty | **UNCLEAR, leaning "routine consequence".** The witness *without* essential irreducibility follows in a few lines from the Binder–Navara carrier plus the known non-Dirac two-valued state on 4even [H]. The residue is essential irreducibility mod countable. Binder–Navara 1987, Navara 2000 and Pták–Pulmannová 1991 are not on the shelf and were **not read in this pass**. |
| Type 1 (programme bar) | **UNCLEAR.** The bar could be met only by the irreducibility residue, which is modest and unread against its likeliest owners. |
| Type 5 (Ω₇) | **FAIL** (internal hygiene; this agrees with the prior audit). |
| Types 3 / 4 / 6 | not claimed; **FAIL** if read in (see §3). |
| **Referee estimate** | **BORDERLINE** (capped: the pure verdict is UNCLEAR and the nearest neighbour was not read in this pass). Venue class: **short note / research journal of the Czech-school type** (Math. Slovaca, IJTP, Order, Kybernetika-adjacent). **Not** Fund. Math. or Studia Logica. Leans REJECT-LIKELY if the referee knows Binder–Navara, unless the paper is reframed. |
| Dependency on Paper I | **None in the paper.** Three stale cross-references in notes (§5). |
| Dependency on Paper II | **None.** |
| Paper-vs-Lean drift | **Both directions.** (a) "formalized in Lean 4 in full" overclaims: the quotient half of `cor:centre` and the paper's segregation notion are not formalized. (b) **Lean has overtaken the paper:** a countable, *literally irreducible* witness (`WindowGluing.Cyclic.targetA_sharp_countable_literal`, axioms clean [R-Lean]) answers `q:cardinality` and the literal-irreducibility form that the paper and its notes list as open. |

**How it bears on WHY.md (one line).** It is an instance of question 3, a hidden idealisation. The
Specker loop (question 1) coheres for every finite purpose, and only the σ-idealisation turns it
pointless. Applicability distance: none; this is pure order theory.

---

## 1. Correctness [R], [H]

I checked by hand every step of §5:
- `lem:ulam`;
- `lem:rep-rigidity`;
- `lem:table` (all ten pairs; (IV) by the coordinate multiset);
- `lem:trichotomy`;
- `thm:normal-form`;
- `cor:meet-region`, `cor:stripping`, `cor:incompat`, and the first paragraph of `cor:centre`;
- `thm:rigidity`;
- `thm:state` (cases I–III);
- `thm:main`.

**No error found in the witness.** `B = {∅, Ω, Aᵢ, Aᵢ^⊥}` has only complement-pair constraints: each
cross intersection is a full fibre, so it is nonempty.

**Error in the framing (required fix).**
- **§2 (c):** "away from a measurable cardinal, every σ-additive two-valued state on a Boolean σ-algebra
  is Dirac [Sikorski, Jech]". **False.** On ω₁, let Σ be the countable/co-countable σ-algebra and set
  μ(A) = 1 iff A is co-countable. Then μ is σ-additive and two-valued, and it vanishes on every
  singleton [H]. Ulam's theorem concerns **P(κ)** (or σ-algebras that also carry the relevant Ulam
  matrix). It does not cover arbitrary σ-algebras.
- **`rem:not-measurable`:** "For a compatible block family (a single Boolean base 𝓑) … ∃ s ⟹ |Ω|
  measurable". **False** for the same reason. The "Boolean shadow is a measurable cardinal" picture,
  which the remark's title advertises, fails.
- **`rem:strength`:** "reduce-to-Dirac is a σ-*algebra* theorem unavailable on σ-classes". **False as a
  dichotomy.** Reduce-to-Dirac is a theorem about σ-algebras that contain enough of P(κ), for example an
  Ulam matrix and singletons. The paper itself shows (`thm:rigidity`) that it *is* available on
  σ-classes that contain those sets. The repo's own `gate.lb_mechanism` fired "refuted" on 2026-06-26
  (Navara–Pták give a non-Dirac σ-state in ZFC), but the paper's prose was never synced with it.

The fix is easy: say "on P(κ), κ below the first measurable". It also deflates the paper's narrative
that "the measurable-cardinal shadow misleads". The "consistency strength, resolved" storyline then has
nothing to resolve: no reasonable referee would expect large-cardinal strength once (c) is stated
correctly.

**Smaller correctness/precision issues.**
- **`q:bare`:** the polarity is muddled. Clause (c) is non-principality, yet the gloss reads "admits no
  selection satisfying (a)–(d) and no principal one either". This was already flagged in
  `VERIFICATION_VERDICT.md` §3, and it is unfixed.
- **`rem:segregated`:** it asserts Φ for every "segregated" carrier, defined informally, but
  `lem:horizontal` proves Φ only for horizontal σ-sums. `prop:adm`'s "non-segregated, as a corollary"
  therefore rests on an unproved generalisation. Lean's `NonSegregated` uses a different notion; see §6.
- **`rem:offcenter` / Wright:** "Wright's theorem … every two-valued state on a finite OML is finitely
  realised, forbids any finite witness". "Finitely realised" is undefined, and the citation is not
  needed. On a finite carrier every finitely additive state is σ-additive, which the intro already says.
  The shelf record attributes a different statement to Wright (convex combinations of two-valued states)
  [S]. Drop or fix the citation.

---

## 2. Pure novelty audit (hostile)

**Stripped statement.** In ZFC there is a set-representable σ-orthoposet L with the following
properties:
- every σ-additive two-valued state on L is Dirac;
- L carries a finitely additive two-valued state that is 1 on three sets with empty common
  intersection;
- L has trivial centre modulo countable sets.

### 2.1 The deflation: the witness minus irreducibility is a few lines [H]

Let 4even be the even-size subsets of {1,2,3,4}. This is a concrete logic with three 4-element blocks.
Its two-valued state t, given by t(12) = t(13) = t(23) = 1, is non-Dirac. It is recorded on the shelf
as known: Burešová–Pták 2024, closing remarks [S, read]; De Simone–Navara–Pták 2007 [S].

Define the Binder–Navara-type carrier

  D := { E ⊆ ω₁ × 4 : the fibre Eˣ ∈ 4even for all but countably many x }.

- D is a σ-class. It contains every singleton, every ξ × F, and the cores Aᵢ (constant fibres 12, 13,
  23).
- Fix an ultrafilter U ⊇ cocountable on ω₁ and set **m(E) = 1 iff {x : t(Eˣ) = 1} ∈ U**. This is the
  U-limit of t. It is a finitely additive two-valued state, and m(Aᵢ) = 1.
- Every σ-additive two-valued state on D restricts to a σ-complete ultrafilter on P(ω₁) via ξ ↦ ξ × F.
  By Ulam that ultrafilter is principal at some x, so {x} × F has value 1, and finite additivity over
  singletons makes the state Dirac. ∩Aᵢ = ∅, so no Dirac extends.
- A₁ ∩ A₂ = ω₁ × {1} has odd fibres, so it is not in D. Hence D is non-Boolean, and the lower bounds of
  A₁, A₂ are countable, so D is not a lattice.

**The paper's carrier L (generated by singletons, cells and cores) is a sub-σ-class of D**, because D
contains the generators. **The paper's vote state is exactly this U-limit restricted to L.** For E with
normalised representation (ξ, κ), the U-typical fibre is κ Δ u(ξ)·1111 = v(E), and t = 1[· ∈ Ŝ].

Consequences:
1. `thm:state` (finite additivity) needs neither the disjointness table nor the trichotomy. It is
   inherited from D.
2. Non-Booleanness and non-latticehood of L are immediate from L ⊆ D.
3. Rigidity is Ulam's theorem, inlined.
4. **The only thing the normal form P̃ buys is essential irreducibility.** D itself has a huge centre:
   every ξ × F is central in D. The parity normal form ties all fibres to one complement pair, and that
   is what kills those central elements in L.

The prior audit (`PHASE2_AUDIT_VERDICT.md`) considered the deflation "Ulam glued to a 4-point fibre, a
Czech-school exercise". It answered that "the content sits in" the parity normal form, which "makes the
incompatibility uncountably deep so the additivity certificate cannot form". **The computation above
answers that rebuttal.** The additivity certificate cannot form in D for a trivial reason (4even is a
horizontal sum), and coherence is inherited. The normal form's real job is irreducibility, and the paper
never says so.

The design could be simplified further: define L := P̃ directly. It is a σ-class by the
`thm:normal-form` argument, which never uses generation. Then cite Ulam's theorem.

### 2.2 Owners and neighbours

| Source | Region | Read level | Status |
|---|---|---|---|
| Binder–Navara, PAMS 100 (1987) Thm 4 | Carrier shape ω₁ × countable logic, cocountably-many bad fibres; every σ-state countably carried (Ulam/Solovay) | **Not read in this pass**; not on shelf; AMS page 403. `GATE_BETA_REPORT.md` claims a full read [S] | **PARTLY OWNED**: carrier + rigidity. With X = 4even, plus the U-limit, it yields the non-irreducible witness in a few lines (§2.1). |
| Navara, "State spaces of orthomodular structures", Rend. Trieste 31 suppl. (2000), §17 | Modern restatement of Binder–Navara | **Not read** (not on shelf) | Unread neighbour. Could already note the f.a./U-limit layer. |
| Pták–Pulmannová 1991 (book), concrete logics and states chapters | Constructions and examples of states on concrete logics | **Not read** | Unread neighbour (gate β downgraded it to due-diligence; still unread). |
| Navara–Pták–Rogalewicz, Pacific J. Math. 135 (1988) "Enlargements of quantum logics" | Enlargements with prescribed centre **and** state space | [W] abstract | Neighbour. A prescribed-centre technique is exactly the tool that would achieve irreducibility; a referee will ask for the comparison. |
| Pták, "Exotic logics" (1987) | Embeddings with prescribed (lack of) states | [S, read] | Adjacent. |
| Navara–Pták 1983; Dravecký–Šipoš 1980; Navara 1984 | Empty-kernel triple with a σ-additive rescuer | [S, read] | Credited, used in the opposite direction. Fine. |
| Burešová–Pták 2024; De Simone–Navara–Pták 2007 | 4even non-Dirac two-valued state | [S] | **Owns the fibre gadget; not cited in the paper.** |
| Navara 1992; DNP 1992 | f.a.-not-σ states on non-concrete logics | [S] | Credited for the quotient remark. |
| Derr–Williamson 2023 D.6 | σ-extension needs a σ-additive input | [S, read] | Correctly scoped in `q:phi`. |

**Pure verdict: UNCLEAR.** No print source was found that states the conjunction (σ-class, all σ-states
Dirac, coherent empty-kernel pattern, *and* essential irreducibility). However:
- (i) the version without irreducibility is an expert-obvious consequence of Binder–Navara + 4even
  (KNOWN-by-routine-consequence in the skill's sense, §2.1);
- (ii) the two most likely owners of the remaining residue, Navara 2000 §17 and PP1991, are unread.
By the v2.1 entry-level cap, this cannot be NOVEL.

---

## 3. Contribution-type verdicts (mode = full)

Declared types (from `PHASE2_AUDIT_VERDICT.md`, since the paper declares none): Type 1 (main),
Type 1 (quotient), Type 5 (Ω₇).

- **Type 1 (main theorem): UNCLEAR.** Without irreducibility it is a routine consequence
  (§2.1). With irreducibility, the residue is "the parity twist kills the centre of the Binder–Navara
  carrier mod countable". That is a real but small step, and it is unread against Navara 2000 and
  PP1991. It also faces the challenge of why irreducibility mod countable is the right demand. The
  paper's own answer is that it is "forced by the method", which is a method-relative motivation, and
  `VERIFICATION_VERDICT.md` §2.3 already notes that the irreducible core lives in a non-concrete
  quotient.
- **Type 1 (quotient artifact): FAIL.** The neighbourhood is crowded (Navara 1992, DNP 1992), and the
  quotient is non-concrete. The paper grades it modestly; keep that.
- **Type 5 (Ω₇): FAIL** (hygiene; refutes the programme's own unpublished statement).
- **Type 2:** **FAIL.** Not a new proof of a known result; rigidity is Ulam inlined.
- **Type 3:** **FAIL.** The localization theorem unfolds the definition, as `rem:localization-scope`
  admits. No method transfer.
- **Type 4:** **FAIL.** "σ-essential contextual state" is a definition. Its three-statements test is
  Ψ, Ψ_lat, Φ-characterisation, and only Ψ has a non-trivial result, which reduces to §2.1.
- **Type 6:** **FAIL.** No named audience, and the literature is accessible.
- **Type 7:** not applicable.

**Applied verdict:** not evaluated (pure order theory; no practitioner).

**Cross-reference.** The edifice's novelty now rests on one load-bearing item: essential irreducibility.
It is (a) method-forced, not field-asked; (b) achieved by the normal form, the paper's only substantial
lemma; (c) unread against the two likeliest owners.

**Recommendation (programme).** Keep the σ-essential thread **closed as a probe outcome** (ZFC witness,
OMP form). Do not count the paper as a contribution until two things happen: Navara 2000 §17 and PP1991
are read (shelf them first), and the paper is reframed around the irreducibility residue. Fold in the
countable ring witness (§6b) before any dissemination. If both stand, it becomes a short note.

---

## 4. Referee estimate (v2.1)

### Referee estimate: **BORDERLINE**
**Venue class:** short note / research journal in the quantum-logic school: Math. Slovaca, IJTP, Order,
Soft Computing (ordered structures), possibly Algebra Universalis as a note. **Not** Fund. Math. or
Studia Logica.

**Value carried by:** factor 1, a small new theorem, *if* irreducibility mod countable is accepted as
the point.

**Main risk a referee would raise:** "This is Binder–Navara's carrier with X = 4even. The finitely
additive state is the ultrafilter limit of the well-known non-Dirac state on 4even. Only the
irreducibility needs the paper's normal form, and the paper neither says so nor motivates
irreducibility independently of its method."

**Caps applied:**
- the pure verdict is UNCLEAR, so the estimate is at most BORDERLINE;
- the nearest prior work (Binder–Navara, Navara 2000 §17, PP1991) was not read beyond abstract or
  metadata in this pass, so the estimate cannot be ACCEPT-LIKELY;
- **unread sources named:** Binder–Navara PAMS 1987; Navara, Rend. Trieste 2000 §17; Pták–Pulmannová
  1991.

The likely referee for this topic is from the Navara/Pták school and knows Binder–Navara. Without
reframing, that referee leans **REJECT-LIKELY** (owner of the main construction in print, credited only
as "lineage"). With the reframing below, a short note is plausible.

### Changes a referee would require (priority order)

1. **Fix the false measurable-cardinal claims** (§2(c), `rem:not-measurable`, `rem:strength`;
   counterexample: countable–cocountable on ω₁). Remove the "consistency strength, resolved" storyline,
   or restate it correctly for P(κ).
2. **State the Binder–Navara + 4even derivation (§2.1) explicitly.** Identify the vote state as the
   U-limit of 4even's non-Dirac state. Cite Burešová–Pták / De Simone–Navara–Pták for 4even. Say
   plainly that the normal form is needed **only** for essential irreducibility, and motivate
   irreducibility on its own terms (why exclude the reducible D?).
3. **Simplify:** define L := P̃ directly and cite Ulam's theorem, or justify the generated presentation.
4. **Demote `thm:localization` to a remark.** It unfolds the definition, as the paper admits.
5. **Cut the abstract's overclaims:**
   - "irreducible to the Hilbert-space dichotomy of Blecher–Weaver, irreducible to a measurable
     cardinal" (`rem:no-bridge` itself says these are not theorems);
   - "what was open is the conjunction" in `rem:sheaf` (no source poses it).
6. **Citation errors:**
   - `AbramskyBarbosaEtAl2022` has the wrong title and authors. arXiv:1905.08267 is Barbosa–Douce–
     Emeriau–Kashefi–Mansfield, "Continuous-variable nonlocality and contextuality", CMP 391 (2022)
     1047–1089 [W, verified]. The bib title "The sheaf-theoretic structure of definite causality"
     belongs to a different paper.
   - **Akemann–Weaver is a CH result.** Under CH, B(H) has a pure state whose restriction to every
     masa is not pure [W, arXiv abstract]. The paper states it unconditionally. A ZFC version (atomic
     masas) is Koszmider 2020 + MSS [W].
   - Wright 1978 ("finitely realised") is undefined or misattributed; drop it.
   - Bib year/venue for Akemann–Weaver: to verify.
7. **Fix the `q:bare` polarity**; restrict the claim in `rem:segregated` to what `lem:horizontal` proves.
8. **Verification paragraph:**
   - change "formalized in Lean 4 in full" to the true scope (§6a);
   - "All mathematical claims are being independently verified by the author" is not acceptable at
     submission;
   - LLM-involvement disclosure is fine but must meet the venue's policy.
9. **Update `q:cardinality` and the open-forms list** for the countable, literally irreducible witness,
   or explain why it is excluded (§6b).

---

## 5. Check 2: Paper I's "σ-LS realization gap" as support

- **The paper:** no citation of Paper I, B2, or any self-citation (all 22 cited keys checked). Its σ-LS
  sentence (§4, "σ-Loomis–Sikorski holds under RDP … OMLs lack RDP (MO₂) … only σ-epimorphic") rests on
  Dvurečenskij 2000 + Pták–Pulmannová 1991 + the elementary failure of RDP in MO₂. **That support stands
  independently of Paper I.** The sentence is in any case only a "route from below is blocked" remark,
  not a load-bearing lemma.
- **The taxonomy:** `wall.no_sigma_ls` and `wall.tribe_vs_points` cite Dvurečenskij and the archive,
  not Paper I. They stand. Note that `wall.no_sigma_ls` is "suggested impossible, not proved".
- **Stale cross-references that still assert the old Paper-I diagnosis** (not edited, per instruction):
  - `notes/open_questions/sigma_essential/sigma_essential_reduction_writeup.md:26`: "(independently)
    the same realization gap that parks Paper I". This is motivation only, and the diagnosis is now
    wrong.
  - `notes/taxonomies_index.json:79`: "Paper I sunk by the σ-Loomis–Sikorski realization gap".
  - `notes/programme/program_overview.md:405` (Paper I banner): "the missing step is the σ-Loomis–Sikorski
    realization gap, the same failure mode that retired the companion note … (Paper II is
    unaffected)". The 2026-10-27 addendum at the top corrects this, but the banner itself does not.
  - (Already corrected in place: `ce_taxonomy.json` lines 7/55/104 carry the 2026-10-27 CORRECTION.)

**Verdict:** the paper has no dependency on Paper I. The programme-level picture of "one realization
gap recurring across Paper I and σ-essential" is now unsupported on the Paper I side; on the σ-essential
side it never mattered to the theorem.

## 6. Check 3: Paper II

There is no use of PR_dual, VDR, EA/PR, McDonald–Bimbó duals, or "non-distributive ⟺ no joint
distribution" [R, grep + full read]. The nearest thing is the slogan in §4 ("each route consumes an
object only distributive structure supplies … one obstruction, met in four forms"). It is rhetoric, not
Paper II's claim, and the theorem does not use it. It is honest to soften it anyway, since §2.1 shows the
actual mechanism is mundane. **No dependency.**

## 6a. Check 4: paper-vs-Lean drift (paper ahead of Lean)

[R-Lean] receipts run here: `targetA_sharp_ZFC`, `psi_ZFC`, `witness_carrier_not_lattice`,
`central_countable_or_cocountable` and `carrier_not_orderIso_measurableSpace` all report exactly
`[propext, Classical.choice, Quot.sound]`. The oleans are newer than their sources. Definitions match:
- σ-class = `DynkinSystem`;
- `TwoValuedState` is σ-additive in the ∃-form; ≤1 is derivable via `val_compl` + relative complement;
- `IsSigmaEssential` = `FinitelyCoherent ∧ ¬∃ σ-extension`;
- carrier = `DynkinSystem.generate` of singletons, cells and cores.

| Paper claim | Lean | Drift? |
|---|---|---|
| "formalized in Lean 4 in full … covers … the centre (Cor. `cor:centre`)" | `central_countable_or_cocountable`: **literal** centre ⊆ countable ∪ co-countable. The **quotient** statement (paragraph 2 of `cor:centre`) is **not formalized**. | **Yes.** The paper's `def:sigma-essential` defines essential irreducibility as a trivial centre *of the quotient*, and Lean's `EssentiallyIrreducible` is the literal-centre condition. The two are close, but they are not the same predicate. |
| Non-segregated "in the sense of `rem:segregated`" | `NonSegregated := ¬ SegregatedStructural` (¬ every f.a. state blockwise pointed) | **Yes.** Different definition from the paper's ("every countable orthogonal family lies in a single block whose σ-states rescue every trace"). |
| Not a lattice (`cor:incompat`) | `witness_carrier_not_lattice`, now a theorem (`slab0_not_mem` proved) | Lean ahead. The paper's verification list omits it. Harmless. |
| Non-Boolean | `carrier_not_interClosed` + `carrier_not_orderIso_measurableSpace` | Matches (Lean is stronger). |
| `thm:localization`, `lem:horizontal`, the quotient remark | `localization` proved; horizontal via `isSigmaOn_of_segregated` (different hypothesis); quotient not formalized | Partly. Not individually claimed in the paper. |
| Stale Lean docstrings | `UlamWitnessLatticeGap.lean` §5 says the centre steps are "not yet written"; `meetsExist_fails_at_cores` says "modulo the one cited fact" | Lean-side hygiene only. |

## 6b. Check 4 (reverse): Lean has overtaken the paper

`WindowGluing.Cyclic` [R-Lean]:
- carrier D₄ = glued 4-ring of windows on Ω₄ = ℕ⁴ (countable);
- `targetA_sharp_countable_literal : Countable Ω₄ ∧ Irreducible D₄ ∧ NonSegregated D₄ ∧
  IsSigmaEssential s₀`;
- axioms `[propext, Classical.choice, Quot.sound]`, run here;
- the same `IsSigmaEssential` / `FinitelyCoherent` as the paper (`WindowGluing.lean:770–824`);
- an L ≥ 4 version: `sL_sigmaEssential`.

This makes the following stale:
- `q:cardinality` ("can a countable Ω carry one?"): **answered yes**, in Lean;
- `rem:offcenter`'s "literal irreducibility … forced by the method": true for carriers with all
  singletons, but the problem's literal-irreducibility form is now inhabited;
- the abstract and §9 open-forms framing, and `VERIFICATION_VERDICT.md`'s "literal-irreducibility form
  OPEN" row.

**Caveats:** this witness is not in the paper, has had no hand audit here, and its prior-art status is
"not found after three passes" (memory), with Bhaskara Rao and Goldberg/Hindman–Strauss bodies unread.
Whether D₄ is a lattice is not settled: `WindowGluing.lean` proves neither `MeetsExist D₄` nor its negation (grep, 2026-10-27). If D₄ were a lattice, it would refute the paper's `q:oml` conjecture, so this check is owed.

**Consequence for the paper.** The ω₁/Ulam construction may no longer be the right headline. A referee
who saw both would ask why the paper presents the weaker (uncountable, essentially-irreducible) witness.
This is the user's call. It is the largest decision point raised by this audit.

---

## 7. Comparison with prior assessments

**Disclosure.** The task asked for an independent verdict before reading the prior documents. I read
`PHASE2_AUDIT_VERDICT.md`, `VERIFICATION_VERDICT.md` (§2.3–§3), `FIDELITY_REVIEW.md` (§5–8) and the
Binder–Navara paragraph of `GATE_BETA_REPORT.md` **after** forming the correctness check and the §2.1
deflation, but **before** writing this file. Those documents did not touch the §1 measurable-cardinal
error or the §6b drift. Treat the independence of §2.2–§4 as reduced, not blind.

| Prior claim | This re-audit |
|---|---|
| PHASE2 (2026-07-06) + Gate β: Type 1 **PASS** ("assembly-novelty, closes the DW beyond-Polish cell") | **Downgraded to UNCLEAR.** The prior rebuttal of the "Czech-school exercise" deflation located the content in the normal form. §2.1 shows the normal form is not needed for coherence, non-Booleanness or non-latticehood; its only job is irreducibility. Gate β cleared Binder–Navara as "no f.a. side", which is true, but the f.a. side is a one-line U-limit of 4even's known state. That check was the wrong one. |
| PHASE2: quotient PASS-weaker; Ω₇ Type-5 FAIL | Quotient FAIL (crowded, non-concrete); Ω₇ FAIL. Agree on Ω₇. |
| VERIFICATION_VERDICT: proofs correct; irreducibility mod countable is "method-forced"; the irreducible core lives in a non-concrete quotient | **Agree.** That observation now carries the whole novelty question. |
| VERIFICATION_VERDICT §3: `q:bare` polarity muddle | **Still unfixed** in the paper. |
| FIDELITY_REVIEW (signed 2026-07-20, SCOPED): `PsiAmended` omits essential irreducibility; `IsIrreducible` an axiom stub | **Partly superseded.** `Admissibility.lean` retired the axiom stubs, and `targetA_sharp_ZFC` carries `EssentiallyIrreducible` proved. Residual gap: the Lean predicate is the literal-centre form, not the paper's quotient-centre definition, and the segregation notions differ (§6a). |
| Memory: "dissemination-ready, 14 pp" | **Not dissemination-ready.** The required fixes are listed in §4. The page count is 15. |
| `gate.lb_mechanism` fired "refuted" 2026-06-26 | Confirmed, and it **propagates into the paper**: §2(c), `rem:not-measurable` and `rem:strength` still assert the refuted mechanism. |

**Anti-oscillation note.** This downgrade is licensed by the prior verdict's own reversal triggers:
- a **located error**: the §1 measurable claims are false;
- a **prior-art deflation with an explicit derivation** (§2.1), rather than a re-reading.

The downgrade does **not** touch correctness of the witness, which stands.

---

## 8. What would settle the open items

1. Shelve and read Binder–Navara 1987 (MR894439), Navara 2000 §17 and PP1991 (concrete-logic states
   chapters). Specific question for each: is the U-limit state on a Binder–Navara carrier with a finite
   non-Dirac fibre logic, or an irreducible (mod countable) variant, already there?
2. Decide the headline: the countable, literally irreducible ring witness or the ω₁ witness (§6b).
3. Apply the §4 fixes, then a re-audit at Phase 7.
