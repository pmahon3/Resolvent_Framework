# σ-essential witness — the large-cardinal bounds, mapped

*2026-06-25. Scoping deliverable from "map both bounds first" (the large-cardinal
link). NOT a proof of either bound — a precise statement of the two goalposts, with
the candidate cardinal pinned against primary sources. Companion to
[[sigma_essential_reduction_writeup]] (§1a bare statement) and
[[forcing_programme_status]] (why forcing is the wrong engine). ⟦HAND — scoping; the
two facts below are primary-source verified, the bounds themselves are
unproven targets.⟧*

---

## 0. Why a large cardinal enters (the anchor)

Ψ := "a concrete σ-essential witness exists" (def: [[sigma_essential_reduction_writeup]]
§1a). The bare object is a **2-valued, σ-additive, non-principal** selection. On a
**Boolean** base that is exactly a non-principal countably-complete ultrafilter — i.e.
**a measurable cardinal**. The witness is the *non-distributive* generalization of that
object. So the strength question is real, and the candidate is **measurable**.

## 1. Two primary-source facts that fix the cardinal (verified 2026-06-25)

**Fact 1 — Ulam (standard; web-confirmed).** A two-valued σ-additive non-principal
measure forces its carrier to be a **measurable cardinal** (least carrier is measurable,
hence strongly inaccessible). Crucially: "Ulam-measurable" properly names the
**two-valued / measurable** side. The *weaker* "≤ 𝔠" notion is **real-valued
(atomless) measurable** — a DIFFERENT object, which §1a explicitly excludes (Ψ is
2-valued). *(Earlier scoping error: I had called Ulam-measurable "weaker than
measurable." False for a 2-valued object. Corrected.)*

**Fact 2 — Blecher–Weaver, arXiv:1607.08505, abstract verbatim (primary source).**
> "There is a singular countably additive **pure** state on B(ℓ²(κ)) iff κ is Ulam
> measurable, and there is a singular <κ-additive pure state on B(ℓ²(κ)) iff κ is
> measurable."

Three things this pins:
- The B–W state is **pure, not two-valued** (2-valued states on B(H) generically don't
  exist, Gleason). So B–W is a **pure-state precedent**, looser than Ψ — reinforces that
  nothing transfers automatically (the §8 caveat, now primary-source confirmed).
- The threshold is a clean two-rung ladder: σ-additive ⟺ **Ulam-measurable**;
  <κ-additive ⟺ **measurable**. Both rungs are large-cardinal strength.
- "Ulam-measurable vs measurable" in B–W is a genuine distinction between **additivity
  levels**, NOT the false "weaker-than" I imported.

## 2. The two bounds, as precise (unproven) targets

**Lower bound (¬-side) — the leg with independent in-field evidence.**
> **(LB)** Ψ ⟹ ∃ a measurable cardinal.
> Equivalently: "no measurable cardinal ⟹ every σ-additive 2-valued state on a concrete
> σ-OML is Dirac ⟹ ¬Ψ."
> STATUS: ⚠ **MECHANISM REFUTED 2026-06-26 (see §3f)** — the "no measurable ⟹ every
> σ-state Dirac ⟹ ¬Ψ" mechanism is BROKEN (premise false by Navara–Pták ZFC non-Dirac
> state; last step a non-sequitur). Strength reopened as UNKNOWN. (Old "plausible, not
> proven" withdrawn.)

**LB SHARPENED via primary-source read of B–W's extraction (2026-06-25, `/tmp/bw.txt`
= arXiv:1607.08505 full text).** B–W's whole large-cardinal content is **Prop 2.3**:
projections in `ℓ∞(κ)` correspond to **subsets of κ**, so a singular countably-additive
pure state on `ℓ∞(κ)` ⟺ a {0,1}-valued σ-additive singleton-vanishing measure on κ ⟺ κ
Ulam-measurable. The `B(ℓ²(κ)) → ℓ∞(κ)` step (Thms 3.1/5.3/6.2) is **always a restriction
to the diagonal masa** via conditional expectation `E`. **The cardinal is extracted from
the COMMUTATIVE Boolean σ-algebra `ℓ∞(κ)` — never from the non-commutative lattice
directly.**
> - ⚠ CORRECTED OVER-READ: I had claimed B–W's extraction "survives on orthogonal closure,
>   masa is convenience." FALSE. The "orthogonal additivity only" step (Thm 3.1, `{pn}`
>   mutually orthogonal) runs *inside `ℓ∞(κ)`*, where orthogonal = disjoint subsets = full
>   Boolean structure. It does NOT transplant to a non-distributive OML (that is the
>   disjointification identity `(a∨b)∧a⊥=b∧a⊥`, distributive, false on OMLs — the §7 wall,
>   5th costume). Caught by advisor + primary source.
> - The filter `ℱφ = {p : φ(p)=1}` on the non-commutative algebra is only a **quantum
>   filter** (Farah–Weaver), NOT an ultrafilter (B–W's own text: "not technically an
>   ultrafilter … weaker properties than classical ultrafilters require"). The **masa is
>   the NECESSITY** that upgrades quantum-filter → genuine ultrafilter; that upgrade is
>   exactly what Akemann–Weaver kills for the concrete 2-valued case (no masa).
>
> **∴ (LB, sharpened — the real open target):** B–W get their cardinal from a genuine
> *ultrafilter on the diagonal masa*. A concrete σ-OML supplies only a *quantum filter*
> `ℱs = {A ∈ L : s(A)=1}` with orthogonal-only closure, and no masa (A–W). The open LB is
> precisely: **is there a MASA-FREE route from a 2-valued σ-state's quantum filter
> (orthogonal-only closure) to a genuine countably-complete ultrafilter / measurable
> cardinal?** The σ-class-vs-σ-algebra gap, now stated as a precise extraction question —
> and primary-source-confirmed that B–W's technique cannot supply it.

**Upper bound (Con-side) — the unearned leg.**
> **(UB)** ∃ [large cardinal X] ⟹ Ψ.
> STATUS: **X not identified; implication not established.** The "measurable suffices"
> intuition was inherited from the B–W weld, which is STRUCK (no routing port:
> Akemann–Weaver, pure state on no masa — B–W's pure-state-on-B(H) mechanism does not
> transfer to concrete 2-valued). Forcing CANNOT supply this (strength-preserving;
> Lévy–Solovay — forcing does not create measurables). It would be a **direct
> large-cardinal construction**.

## 3. The honest finding (corrected — the "measurable vs Ulam-measurable" tension was mine)

The exact cardinal is **not** unpinned by a measurable-vs-Ulam confusion — that confusion
was a terminology slip (Fact 1 dissolves it; in the 2-valued world they are the same
strength class). The genuine open question is narrower and cleaner:

> **Is Ψ exactly equiconsistent with a measurable cardinal, or does the
> non-distributivity push strictly above?**

Recorded honestly as: **Ψ is ≥ measurable (conjectured, LB unproven); exact strength
unknown.** §1a licenses only "strictly more than an *ultrafilter*" — NOT "strictly more
than a *measurable cardinal*"; do not upgrade that.

**The prize:** if LB and UB pin the *same* cardinal, Ψ is **equiconsistent** with that
large cardinal — a Blecher–Weaver-style equivalence for the **concrete** sector (which
B–W do NOT cover; theirs is B(H)/pure). That is the unclaimed result. Both bounds are
**set-theorist hand-off targets** (per §8), not solo in-field work.

**Answer-type calibration (2026-06-28, belief-check — NOT a result).** Tempting to bet the
answer is *independence* (the famous neighbours — von Neumann–Maharam, real-valued
measurable — are independence results). **That lean does not survive; the ranking is FLAT.**
Three corrections: (1) those neighbours are two *incompatible* kinds — vN–Maharam is
**forcing-independence** (both directions consistent with ZFC alone), real-valued-measurable
is **consistency-strength** (asymmetric, forcing can't reach it, Lévy–Solovay); bundling them
hides that Ψ has evidence for *neither*. (2) The ONE structural hook for independence was the
Boolean-shadow ⟹ ≥measurable inheritance ⟹ not-ZFC-provable — **§3f refuted exactly that**, so
the basis for the lean is the thing already proved (currently) broken. (3) "Resisted
construction ⟹ probably independent" is the definability-vs-existence error on the MODAL axis:
convergence-on-a-wall is evidence about *methods tried*, not the truth-value's modal status,
and it's symmetric (Ψ was equally not *refuted*). So **answer-type is genuinely unknown** —
construction / impossibility / independence all live, nothing structural favours the third.
**Discriminator:** the independence lean revives *iff* a lower bound (some large cardinal ⟸ Ψ)
is re-proved by a route surviving §3f — a Phase-2 target, not decidable from here.

## 3a. Masa-free direct route — ATTEMPTED + DEAD (2026-06-25, ⟦HAND, advisor-checked⟧)

Tried the sharpened LB directly: is `ℱ_s = {A ∈ L : s(A)=1}` a countably-complete
**ultrafilter** for a 2-valued σ-state `s` on a non-Boolean concrete σ-OML, with no masa?
Checked the axioms on `L`:
- **Upward closure** ✓ (state monotonicity — no distributivity).
- **2-valued dichotomy** (`A` or `A^⊥`, exactly one) ✓ (orthocomplement — no distributivity).
- **Finite meet-closure** ✗ — **and ✗ for EVERY 2-valued state, including Dirac.**

**The discriminating check (MO₂ unit test):** in any concrete `MO₂ ⊆ P(Ω)`, atoms `a,b`
overlap as sets (`a∩b ≠ ∅`, else disjoint = orthogonal, forbidden) while lattice-meet
`a∧b = ∅`. For `ω ∈ a∩b`: `δ_ω(a)=δ_ω(b)=1` but `δ_ω(a∧b)=δ_ω(∅)=0`. So **`ℱ_{δ_ω}` is
not meet-closed — for a POINT state** (which manifestly extends to a global σ-state).

**∴ Meet-closure failure is NOT the contextual signature — it fails for everything**,
because lattice-meet ≠ set-intersection on any non-Boolean concrete OML. This is
`rem:concrete` / the disjointification identity again (intersection-closure = the Floor
→ Boolean) — **the ~6th costume of the same wall, not a new discriminator.** B–W's `ℱ`
works ONLY because `ℓ∞(κ)` is intersection-closed (Boolean).

**Status: ROUTE-DEATH, not a ¬-result.** `ℱ_s` is a filter for NO 2-valued state on a
non-Boolean concrete OML ⟹ the masa-free *direct* route to an ultrafilter is dead. This
does NOT decide `Ψ ⟹ measurable` (the LB sentence stays open) — it kills one attack.

**What this resolves (the honest answer to "why is the LB hand-off?"):** not "expertise
mismatch" but **the carrier structurally lacks the object the LB proof would consume.**
B–W extract a measurable from a genuine ultrafilter; on a concrete non-Boolean σ-OML no
2-valued state's filter is an ultrafilter (not even a point state's). The Ulam-style
proof has nothing to eat. **The only non-costume continuation = a genuinely NEW object**
(e.g. a strength invariant of the *failure* of `ℱ_s` to be a filter — but the
cohomological version of that was already a logged costume, §1a; needs a real new idea).
**Pre-set stop condition hit (per [[sigma_essential_construction_attempt]]): "further
hand-progress needs a NEW OBJECT or new abstract input." Clean stop.**

## 3b. The completeness-language reframe (learning pass, 2026-06-25)

Walked Ulam's theorem + the measurable-cardinal definition from scratch (education, not
a new attack). Two textbook facts, then the reframe they buy. ⟦textbook — verifiable in
Jech/Kanamori; the reframe is a vocabulary change, NOT a foothold.⟧

**Ulam's matrix (why a measure forces a huge cardinal).** A non-trivial (points
negligible, whole = 1) countably-additive 2-valued measure cannot live on a countable
set (the "sum of point-measures" argument bites a countable union). On `ℵ₁` it still
dies via the **Ulam matrix**: an (ℕ rows) × (`ℵ₁` cols) grid `A(n,β) = {α>β : f_α(β)=n}`
built from one injection `f_α : {predecessors of α} ↪ ℕ` per element (exists because
below-α is countable). Injectivity ⟹ rows are **disjoint** families; totality ⟹ columns
**nearly cover** (miss only a countable piece). Squeeze: columns + countable additivity
⟹ a positive entry per column; pigeonhole (uncountable cols → countable rows) ⟹ one
disjoint row carries uncountably many positive-measure sets ⟹ contradiction (disjoint +
positive + uncountable inside mass 1).

**The gap, located precisely (matches the ledger's `¬Ψ FIRST RUN`):** the matrix's
**contradiction step is OML-safe** (a disjoint row = orthogonal family; orthogonal
additivity is exactly what a σ-OML HAS). The break is at **CONSTRUCTION** — forming the
entries `A(n,β)` needs arbitrary property-comprehension + countable **non-orthogonal**
unions (the exceptional countable pieces), which a concrete σ-OML LACKS. Independent
re-derivation of the σ-class-vs-σ-algebra gap, located to the line: *the obstruction is
"can you even build the matrix," not "does the contradiction run."*

**Measurable = dodges every matrix below it.** Generalized matrix (rows indexed by
`λ<κ`) kills `κ` UNLESS the measure is `λ⁺`-additive for no `λ<κ` — i.e. unless it is
**`κ`-complete** (closed under unions of size `<κ`, failing only at `κ`). That survival
property IS measurability. Positive content (Step 5): a `κ`-complete non-principal
ultrafilter `U` ⟹ ultrapower `V^κ/U` ⟹ elementary embedding `j : V → M` with critical
point `κ`. The measure is a **universe-bender**, not just a measure.

**THE REFRAME (what the deep regime buys — vocabulary, not a foothold).** Both walls now
speak ONE language — *which unions/intersections is the structure closed under*:
- **LB:** does *countable-orthogonal* closure force a `κ`-complete ultrafilter? (matrix lens)
- **UB:** a measurable hands you a `κ`-complete `U` on **Boolean** `P(κ)` (intersection-
  closed); transporting it onto orthogonal-only closure is the disjointification wall
  *from the construction side* — `U`'s `κ`-completeness is stated via arbitrary small
  **intersections**, which the carrier doesn't support. The measurable gives a
  magnificent object built for the WRONG closure.

⚠ **The reframe makes the wall LEGIBLE, not PERMEABLE.** Both walls, in completeness-
language, still bottom out at the SAME disjointification identity `(a∨b)∧a⊥=b∧a⊥`. "Use
the embedding `j` to transport `U` onto the σ-OML" is the obvious next move and is
**costume #8** — the disjointification wall in embedding-clothes. NOT done; flagged as the
costume to avoid. Honest next step = keep learning the deep regime (inner model theory)
as EDUCATION past the matrix; let a genuinely new object arrive on its own, not be
manufactured at the point of non-progress.

## 3c. Class-sized Boolean algebras (Takeuti–Zaring Ch. 23) — READ, does NOT unblock (2026-06-26)

Read Takeuti–Zaring, *Axiomatic Set Theory* (GTM 8, 1973), Ch. 23 "Boolean Algebras That
Are Not Sets" (pp. 201–225; library: `takeuti_zaring_axiomatic_set_theory.pdf`).
**Motivation for the read (user's instinct):** Ch. 23 handles unboundedly-growing
cardinality by taking the limit `B` of a tower `B_β` (with `|B_β|` increasing) to be a
**proper class** (or class-of-classes); our problem is set-theoretic and
cardinality-sensitive, so a technique that transcends set-cardinality looked relevant.

**What the chapter actually does:** for a class-sized complete BA `B`, gives conditions
(the **uniform convergence law**, Def 23.10) under which `V^B` still satisfies Replacement
and Powers (without UCL, `V^B` satisfies Separation but may fail Replacement/Powers —
Thm 23.9 remark). The payoff theorems: `V^B ⊨ AC/ACH` (23.23–24, PRESERVES choice);
Easton's main lemma + `(ℵ_α,ℵ_β)`-splittability (23.43–46, controls **cardinal
arithmetic** — which powers `2^{ℵ_α}` you set — under `ℵ_α` assumed regular). The limit
`B` is built as a direct-and-inverse limit of partial-order structures / topological
spaces (23.39–42).

**Why it does NOT unblock wall A (advisor-checked + verified against the text):**
- **Cardinality ≠ consistency strength.** Ch. 23's proper-class limit conquers
  *unbounded set-cardinality* (set powers across all regular cardinals at once). Ψ needs
  *consistency strength* (a measurable cardinal). These are orthogonal axes. **Proof = the
  next chapter:** Ch. 24 (Easton's model) is class forcing, **equiconsistent with ZFC**,
  creating no large cardinals (can even kill measurables). Every Ch. 23 theorem PRESERVES
  ZF/AC and rearranges arithmetic; NONE creates strength (verified: 23.23-46 all
  preserve-and-rearrange).
- **Still forcing ⟹ still the wrong engine** (Lévy–Solovay, §3b / rem:technology): class
  forcing is strength-preserving exactly as set forcing is.
- **`B` is Boolean either way (the pincer).** As the *ambient* forcing algebra: different
  object, but the witness inside `V^B` is still a non-Boolean OML ⟹ disjointification wall
  reappears in the extension. As the *carrier* itself: impossible — Ch. 23 builds complete
  **Boolean** algebras; an OML-as-limit-of-posets is the band-family route, charted-dead.
- **Ψ's witness `L` is a SET** (a σ-OML on a set Ω). `∃L` ranges over a proper class of
  set-candidates, but each witness is a set; class-size is a property of a *forcing notion*,
  not of the witness — so a proper-class `B` has no concrete role to play in `L`'s existence.

**Status: legitimate class-forcing BACKGROUND (the set-theory register the hand-off needs),
NOT the new abstract input. Recorded as education.** The instinct (transcend set-cardinality)
was reasonable; it conflates cardinality (how big) with strength (how strong an axiom) —
Ch. 23 buys the first, Ψ needs the second. ⟦read + advisor-checked + text-verified⟧.

## 3d. Hybrid analysis: can Ch.23 (strength axis) pair with a second method for the OTHER axis? (2026-06-26)

**The question (user):** Ch. 23 handles one orthogonal issue — could it be used in a HYBRID
with another method to handle the other? Standard set-theory shape: large cardinal supplies
STRENGTH, then (mild/class) forcing supplies STRUCTURE, cardinal survives (Solovay's RVM
model = measurable + random forcing; Lévy–Solovay run forwards).

**Axis correction (important — fixes the §3c framing).** The two real obstacles were never
"cardinality vs strength." They are **(I) consistency strength** (need a measurable) and
**(II) non-distributivity** (the disjointification wall). Ch. 23 conquers *cardinality*,
which was never one of our two obstacles. So the hybrid:
- **Axis (I) — handled.** Assume a measurable κ → get the κ-complete ultrafilter `U`; force
  mildly; κ survives. Real reframing GAIN: strength is no longer the question.
- **Axis (II) — NOT handled, and forcing-invariant.** `(a∨b)∧a⊥=b∧a⊥` is false on OMLs — a
  ZFC theorem, true in every forcing extension under every large cardinal. The hybrid's
  step-2 "use `U` to seed the witness on the OML" = transport `U` from Boolean `P(κ)` onto
  orthogonal-only closure = **costume #8** (`costume.embedding_transport`, already FORBIDDEN).

**∴ The hybrid is a correct DECOMPOSITION, not a route to a proof.** It factors strength out
and isolates the whole difficulty as the single non-distributivity transport. Cleanest form
of the open problem to date: *given a measurable κ and its `U` on `P(κ)`, is there a concrete
non-Boolean σ-OML + a transport of `U`'s completeness onto its orthogonal-join structure
yielding a σ-essential witness — or is that transport obstructed in ZFC?* Strength assumed
away; transport is the sole wall.

**Taxonomy search for a genuine axis-(II) partner (all 6 collections scanned).** One real
non-costume candidate surfaced: **`ce.concept.oml_center`** (OPEN) — route the σ-state
obstruction through the OML's Boolean **center** `C(L)`, where a measurable/`U` applies
NATIVELY (the center is intersection-closed, no disjointification wall). Pták 1987 "exotic
logics": σ-orthocomplete OMLs with f.a. but no σ-add states, obstruction in `C(L)≅BA` with
no σ-add probability. This is structurally different from costume #8 (acts on the Boolean
center, not the whole non-Boolean lattice).

**Center hybrid FAILS on a dichotomy ⟦HAND, advisor-RESOLVED 2026-06-28⟧:**
- *Trivial center* (`{∅,Ω}`): the witness is REQUIRED irreducible (`rem:offcenter`, Def),
  and the center is then `{∅,Ω}` — **no HOST for `U`** (nowhere Boolean to seed the
  measurable's ultrafilter). The hybrid has nothing to act on.
- *Non-trivial center*: hosts `U`, BUT the carrier is then **segregated**
  (`rem:segregated`) — contextuality routed through a central Boolean factor, σ-states
  concentrate at points ⟹ NO witness, EXCLUDED.
- **Both horns kill it** on no-host / segregated. No inhabited middle: the place the hybrid
  would seed strength (the center) is forced either empty-of-host (trivial) or disqualifying
  (segregated).
- ⚠ **CORRECTION (advisor 2026-06-28): the earlier trivial-center horn — "trivial center ⟹
  Gleason ⟹ σ-additivity forced ⟹ no obstruction" — is WRONG and was SUPERFLUOUS.** It is
  false on the standing unit test: `MO₂` is irreducible (trivial center) yet is the *source*
  of every disjointification failure here — it does NOT force σ-additivity. Had the Gleason
  horn held it would prove ¬Ψ, contradicting the open status established everywhere else. The
  kill stands on no-host/segregated alone; the Gleason step is retired (the prior
  ⟦advisor-pending⟧ flag is hereby resolved: the flagged step was both wrong and unnecessary).

**RESIDUE (the genuine gain, not consolation).** The center analysis SHARPENS the target: the
witness's non-distributivity can be neither central (segregated, excluded) nor absent
(Gleason, no obstruction) — so the σ-obstruction must live in the **irreducible, non-central
part**. That is exactly `open.intrinsic_K` (the unbuilt frontier carrier). The center hybrid,
by failing, CONFIRMS the obstruction is irreducibly non-central — narrowing the target rather
than hitting it. Standing stop-condition unchanged: needs a genuinely NEW object, not a
strength supplier (which the hybrid shows is correctly factored out).

**✅ RESOLVED (advisor 2026-06-28):** the worry was whether Gleason-exceptionality
generalizes to all trivial-center OMLs. It does NOT — and the kill never needed it. The
trivial-center horn is "no host for `U`" (the center is `{∅,Ω}`, nothing Boolean to seed),
not a Gleason argument; `MO₂` refutes the Gleason version outright. The dichotomy stands on
no-host (trivial) / segregated (non-trivial, `rem:segregated`), both in-paper, neither
relying on a Gleason-generalization step. Taxonomy: `strat.center_hybrid` (corrected kill).

## 4. Sources
- Takeuti & Zaring, *Axiomatic Set Theory* (GTM 8, Springer 1973), Ch. 23 — class-sized
  complete Boolean algebras; UCL; Easton splittability. (1st ed.; the Boolean-valued
  forcing volume. NOT the 2nd ed., which is Cohen-style.) Library (gitignored).
- Ulam's theorem: standard; see Jech, *Set Theory*, or Kanamori, *The Higher Infinite*.
- Blecher & Weaver, *Quantum measurable cardinals*, arXiv:1607.08505 (JFA 272, 2017) —
  abstract verified 2026-06-25.
- Lévy–Solovay (forcing preserves measurability / does not create it): standard.
- σ-class-vs-σ-algebra gap: [[sigma_essential_reduction_writeup]] §7 (the ¬Ψ stall).

## 3e. Con-side sharpened to ONE step (2026-06-26) — and we are attempting it

Two independent analyses (the §3d hybrid / strength axis + the construction attack via
the atomless-blocks candidate, Lean `SigmaEssentialConjectures` §1b) CONVERGE on the
positive route and isolate its single open step:

- **Construction barred where constructible.** Atomless measure-algebra blocks +
  countable gluing stay Polish-representable ⟹ DW D.6 kills them. A witness must be
  uncountably generated + NON-Polish-representable = the regime that resists explicit
  hand-construction.
- **Forcing barred** (Lévy–Solovay, §3b/rem:technology).
- **Remaining route = DIRECT large-cardinal construction** (Blecher–Weaver model):
  assume measurable κ, take its κ-complete ultrafilter `U` on `P(κ)`, build carrier +
  pattern from `U`.
- **THE SINGLE OPEN STEP (named exactly):** `U` lives on **Boolean** `P(κ)`; powering a
  witness on a non-distributive concrete σ-OML needs transporting `U`'s completeness
  onto orthogonal-join-only closure — the masa route can't supply it (Akemann–Weaver;
  costume #8 in its obvious form). So: **is there a masa-free construction of a
  non-distributive concrete σ-OML from a measurable's ultrafilter `U`, or a proof none
  exists?** Paper: `rem:consharp`.

**STATUS: NOT a hand-off. We are attempting the masa-free transport.** The harness
(`SigmaEssentialConjectures`) triages any proposed transport instantly (forces
`IntersectionClosed`? → costume). Attempt log continues below / in the Lean file.

## 3f. ⚠ LB MECHANISM REFUTED — strength reopened as UNKNOWN (2026-06-26, advisor-confirmed pending)

While attempting the Con-side, the advisor flagged the LB's direction. A cold four-case
check (no-measurable world, witness?) BROKE it. **This inverts the banked "Ψ ≥ measurable
(conjectured)" status — recorded carefully.**

**The LB as stated (§2):** "no measurable ⟹ every σ-additive 2-valued state on a concrete
σ-OML is Dirac ⟹ ¬Ψ." Both legs fail:

1. **Premise is FALSE (not just unproven).** "no measurable ⟹ every σ-state on a concrete
   σ-OML is Dirac" is refuted by **Navara–Pták 1983 (ZFC)**: their `m` is a NON-Dirac
   σ-additive 2-valued state on the concrete non-Boolean σ-class ℚ² (verified,
   [[navara_ptak_1983_byhand_read]]). No measurable cardinal anywhere. The "Dirac-only"
   premise is an Ulam *σ-algebra* theorem illegitimately applied to σ-*classes* — the
   σ-class-vs-σ-algebra gap is FALSITY here, not a stall.
2. **Last step is a non-sequitur anyway.** Even granting "every σ-state Dirac": that makes
   clause (ii) (no NON-Dirac extension) VACUOUSLY TRUE, and clause (i) (K(s₀)=∅) is
   carrier-dependent and freely arrangeable (N–P device) — so "Dirac-only" pushes toward
   Ψ (witness exists), NOT ¬Ψ. The four-case table: on a non-Boolean carrier with K=∅
   arranged + every σ-state Dirac, BOTH clauses hold ⟹ witness. (On a Boolean carrier
   prop:boolean gives K≠∅ ⟹ clause (i) fails ⟹ no witness — but Boolean carriers were
   never witness candidates.)

**∴ The LB has NO surviving mechanism.** Combined with the UB ("unearned", §2), **measurable-
cardinal strength for Ψ is unsupported in BOTH directions.** Honest status of Ψ's strength:
downgraded from "conjecturally ≥ measurable" to **GENUINELY UNKNOWN**. The "measurable"
candidate rode (a) the struck Blecher–Weaver weld and (b) this now-refuted LB; neither
survives.

**GUARD (do not overclaim):** N–P refutes the *premise*, but N–P is NOT a witness (its
carrier is Polish-representable ⟹ DW rescues; `m` is the rescuer). So this establishes
"the LB mechanism is broken + strength reopened", NOT "Ψ provably needs no large cardinal".
Ψ's strength is unknown, full stop — could be ZFC-decidable, could need some cardinal, no
current evidence either way.

**Consequence for the Con-side (§3e):** "direct construction from a measurable" was built on
the conjecture that measurable is the right strength — now unsupported. The bind "where does
measurability enter the construction?" DISSOLVES: it had no answer because measurability was
never established as required. Con-side reframes to: the strength is unknown, so the
construction target's required hypothesis is itself open. ⚠ ADVISOR-CONFIRM when available
(this is a "X is false" claim inverting a banked result — stronger than "unproven").

## 3g. THE LOCATED FRONTIER — non-Polish, no entering tool (2026-06-26)

Synthesis after the construction attack + LB-refutation. Every tool stops at the Polish
boundary:
- Boolean carriers → FIP → clause (i) fails (prop:boolean). Closed.
- Polish-representable → DW D.6, no witness. Closed.
- Forcing → strength-preserving (Lévy–Solovay). Wrong engine.
- U-as-state → rescuer (polarity gate). Dead.
- U-as-carrier → contributes only κ's SIZE, not strength (Ch.23/Easton). No lever.

By elimination, a witness MUST live in the **non-Polish-representable** regime
(= non-standard-Borel) — confirmed from two independent directions (DW boundary +
construction attack). But that is exactly the regime that resists explicit
hand-construction, AND forcing (the usual non-constructive tool there) is barred, AND
the strength that would justify a large-cardinal construction is now UNKNOWN (§3f).

**∴ The frontier is LOCATED but has NO ENTERING TOOL.** The witness cell is non-Polish;
no current method reaches into it. This is not "a path with a next step" — it is a
precisely-bounded open cell with no tool that enters. The real open question is no
longer "construct in non-Polish" but: **what kind of object or combinatorial principle
could produce a non-Polish, non-standard-Borel concrete σ-OML with an un-threadable
gluing (no global σ-state)?** No candidate principle on the table. STOP-condition:
needs genuinely new abstract input, not another build.

## 3h. Deep-research borrowable-principle hunt — NEGATIVE + one open lead (2026-06-27)

100-agent deep-research workflow (18 primary sources read verbatim, 24/25 claims
survived 3-vote adversarial verification). Question: does any field (DST, non-separable/
Maharam measure theory, Dynkin/σ-class/SOMP lineage, sheaf-theoretic contextuality)
supply a borrowable principle to build the non-Polish concrete σ-OML witness without a
large cardinal?

**VERDICT: NEGATIVE — and informative.** No source supplies it. Every candidate fails
on one of THREE recurring axes = exactly our gates, independently rediscovered:
(1) Boolean not irreducibly-non-central (Maharam, Measure-Recognition, Talagrand);
(2) real-valued not 2-valued (all submeasure / contextual-fraction / barycentric
machinery); (3) finite/Polish/standard-Borel not non-Polish (finite concrete logics,
SOMPs, CV-contextuality over Borel ℝⁿ, Burešová–Pták's POSITIVE Stone-globalization).
External corroboration the gates are real boundaries, not framing artifacts.

**Re-confirms (not new) our σ-LS/RDP wall:** the report independently pinpoints the
structural reason — Loomis–Sikorski σ-additive gluing is gated by the **Riesz
Decomposition Property (RDP)**, which non-Boolean OMLs (MO₂) lack (Dvurečenskij
arXiv:1006.1958: Thm 4.4/4.8 need RDP; the RDP-free Thm 6.1/6.3 is a real-valued
BARYCENTRIC integral, not a {0,1} carrier measure). = our `wall.tribe_vs_points` /
reduction_writeup §3, verbatim. Also independently flagged Gunji "left adjoint"
non-distributivity↔no-global-section as REFUTED 1-2 = our `kill.gunji_dropped`.

**THE ONE OPEN LEAD (not exhausted):** the **descriptive-set-theory sector** rests on a
single survey (Kanovei) — a dedicated sweep of **co-analytic uniformization failure /
non-hyperfinite orbit equivalence / the E0-turbulence zoo, specifically reframed as
2-valued λ-system sections**, was NOT done. The report's own #1 open question. A DST
witness cannot be excluded with the confidence of the Boolean/real-valued/Polish
exclusions. This is the live next probe if pursued. (Note: known DST no-Borel-transversal
results — E0, free-pmp-action orbit ERs — live on STANDARD-Borel 2^ℕ/ℕ^ℕ with REAL-valued
obstructions, so the obvious DST hits are already excluded; the lead is the un-swept
co-analytic/non-hyperfinite corner.)

**DST CORNER SWEPT (targeted scout, 2026-06-27) — NEGATIVE across all 4, negative now
COMPLETE.** (1) Co-analytic Π¹₁ uniformization-failure (Novikov–Kondô, Mauldin–Larson):
standard-Borel/Polish base + real-valued/measurable — EXCLUDED. (2) Non-hyperfinite/
non-treeable CBERs (E∞, Adams–Kechris): the no-section is over the standard-Borel
QUOTIENT X/E, no λ-system, obstruction not irreducibly-non-central — EXCLUDED. (3)
Turbulence (Hjorth): obstruction to classification by countable structures, Polish G-space,
real/structure-valued, never 2-valued — EXCLUDED. (4) Analytic-not-Borel ideals / σ-classes
(Solecki; the Pták school): right object type but base is countable/Polish (P(ℕ),ℚ²) =
DW-killed, and where non-Polish the obstruction is submeasure/real-valued — EXCLUDED.

**⚠ ONE SHAPE-MATCH FLAGGED FOR FOLLOW-UP (not a hit — a bridge to BUILD):** the
Glimm–Effros dichotomy phrasing "**a CBER is non-smooth ⟺ [no/yes] 2-valued [non-atomic
Borel] section on the quotient**" is the SAME LOGICAL SHAPE as our σ-point-selection
failure (non-smooth ⟺ no 2-valued global section). It is NOT a witness (standard-Borel
quotient, no OML structure). But: **if a non-hyperfinite CBER's non-smoothness were
transported onto a Gudder-style concrete logic, that would be the borrowable principle.**
No such transport is published — constructing it would be ORIGINAL work. This is the one
DST item with a possible bridge, distinct from a citable result. **[RESOLVED §3j 2026-06-27:
the bridge is KILLED — a type/strength non-sequitur (non-smoothness = ZFC + definability;
clause (ii) = absolute existence ≥ measurable). Not a borrowable principle. Negative complete.]**

## 3i. RDP-impossibility deep research — VERDICT (c) OPEN, the wall is NOT a theorem (2026-06-27)

98-agent workflow (full-text greps on the key papers, conservative). Question: is
"RDP-failure ⟹ no faithful σ-additive 2-valued representation" a PROVED theorem (would
make the σ-LS wall an impossibility = a ¬Ψ result), FALSE, or OPEN?

**VERDICT: (c) genuinely OPEN/unaddressed — and the wall is NOT an impossibility theorem.**
- RDP appears throughout the σ-LS / effect-tribe literature ONLY as a SUFFICIENT
  hypothesis (Buhagiar–Chetcuti–Dvurečenskij 2006; Dvurečenskij 2000, 2005, 1204.6486
  Thm 3.1; 1006.1958 Thm 4.4/Cor 4.5). NO paper proves RDP necessary; NO paper proves a
  non-representability theorem for RDP-free OMLs. The inference "no RDP ⟹ no
  representation" is simply not in the literature.
- ⚠ DIRECT COUNTER-EVIDENCE the broad obstruction is FALSE: Dvurečenskij 1204.6486
  (verbatim): "E(H) can be represented as an effect-tribe, but RDP fails for it." So
  RDP-failure is not even a universal obstruction to tribe representation.
- CAVEAT (held): E(H)-as-tribe is the WRONG representation notion (isomorphism-to-a-tribe,
  not our σ-epimorphic-image / faithful 2-valued-point-separation). So (b)-FALSE is NOT
  established for our target either; the OML 2-valued σ-LS question is simply UNTREATED.
- Gaps the survey did NOT reach: **Harding / Hamhalter** on σ-complete OML representation
  specifically (named in the query, not located) — the most likely place an OML-specific
  σ-LS statement (either direction) would live. Worth a targeted follow-up if pursued.

**Harding/Hamhalter targeted check (2026-06-27) — confirms (c), structurally.** Neither
settles the RDP-free σ-complete OML σ-additive 2-valued representation question. Harding's
OML work is order-theoretic / categorical / FINITELY-additive (completions, decompositions,
Gudder concrete-logic) — no σ-additive representation. Hamhalter (*Quantum Measure Theory*
2003) studies measures ON a fixed L(H) (the σ-complete-but-NON-concrete cell, Kochen–Specker)
— no Loomis–Sikorski / concrete-logic chapter. **Structural clincher: a lattice effect
algebra has RDP iff it is MV (Bennett–Foulis; Riečanová) — so RDP is exactly the Boolean/MV
dividing line, and the non-Boolean σ-complete OML is the COMPLEMENT of what the σ-LS-with-RDP
machinery can reach.** The gap is structurally excluded, not merely unreached. Independent
confirmation it is open: Harding–Wang (arXiv:2108.09819, 2021) explicitly poses σ-OML
embeddability as an OPEN PROBLEM. ∴ the construction route is NOT closed by any published work.

**CONSEQUENCE FOR THE THREADS:**
- The "turn the wall into a ¬Ψ theorem by citing RDP" hope is DEAD — there is no such
  theorem, and the broad RDP-obstruction is false (E(H)). The wall is an unproven GAP.
- ∴ the CBER bridge is NOT moot: since RDP-failure is not a proved obstruction, NO theorem
  forbids the witness; the construction route stays open. The sequential gate resolves to
  (c) → the CBER bridge was then the live constructive lead **[but was itself KILLED §3j —
  type/strength non-sequitur; see below. Frontier now closed, no entering tool.]**
- ⚠ wording: "RDP-walled" (§3h) means "the off-the-shelf RDP-gated machinery does not reach
  it", NOT "RDP proves it impossible." The wall is a GAP, not a theorem.

**∴ The located-frontier verdict (§3g) STANDS, externally corroborated, negative now
COMPLETE across DST too:** non-Polish, no entering tool, RDP-GAP-walled (the RDP-gated machinery does not reach it — an unproven gap, NOT an impossibility theorem; §3i).

## 3j. CBER → concrete-logic bridge — KILLED by hand (2026-06-27, advisor-checked ×2)

The last flagged constructive lead. The bridge claimed: a non-hyperfinite CBER `E`
non-smooth ⟹ σ-point-selection failure (clause (ii)), transporting Glimm–Effros
non-smoothness onto a Gudder concrete logic. **KILLED — a type/strength non-sequitur,
the same shape as the §3f LB-refutation.**

**The kill (strength mirror of §3f):**
1. Non-smoothness of `E` (E₀, E∞, …) is a **ZFC theorem** — no large cardinal.
2. Clause (ii) *failing* (∃ non-Dirac σ-additive 2-valued state) is **≥ measurable** on
   the Boolean shadow (`rem:not-measurable`).
3. A ZFC fact can neither force nor refute a measurable-strength statement ⟹ non-smoothness
   is **SILENT** on clause (ii). Same non-sequitur certified in §3f (Lean polarity gate).

**The type gap underneath:** Glimm–Effros gives "**no _Borel_ selector**" (transversals
exist by AC — the content is *definability*, not existence). Clause (ii) is "**no
σ-additive 2-valued state, AT ALL**" (absolute non-existence in ZFC+AC). Transport delivers
at most "no _Borel_ σ-state," **never "no σ-state."** A definability obstruction cannot
deliver an existence obstruction. ~10th costume of the same wall, one level out.

**Both sub-outcomes dead:** (a) point at the AC-transversal as rescuer → it need not be
σ-additive; where it is, it is the **Navara–Pták `rem:np` rescuer shape** (kills clause (ii)).
(b) cannot exhibit a state → **silent in ZFC** = §3f shape.

**Two false-kill traps avoided (advisor):** (1) the E₀ *class-partition* is a SINGLE
partition = Boolean = segregated ⟹ clause (ii) fails *vacuously* by `rem:segregated`, a
reason unrelated to the bridge; the discriminating content lives only in **overlapping
non-distributive blocks**, so the bare class-logic test is meaningless — must not rest the
kill on it. (2) "transversal exists by AC" is not yet a clause-(ii) failure — a 2-valued
state must be σ-additive; an AC selector need not commute with countable disjoint unions.
The clean kill rests on NEITHER trap — it is the type/strength non-sequitur, needs no state
exhibited.

**E∞ does not reopen it:** the kill is type/strength, NOT hyperfiniteness. Non-hyperfiniteness
buys *more* non-smoothness, and non-smoothness is precisely what is **orthogonal** to clause
(ii). E∞ (Adams–Kechris) falls identically — non-hyperfiniteness is the wrong axis. ⟦HAND,
advisor-checked ×2; mirrors the §3f Lean-certified non-sequitur.⟧

**∴ NEGATIVE NOW COMPLETE.** Every DST no-section swept (§3h) is definability- or
real-valued; none is absolute 2-valued non-existence. The last flagged lead is the same
costume one level out. **No entering tool remains in any surveyed field; the convergence
IS the finding** (as the ledger predicted). The witness question is open and well-posed
but has no borrowable principle — resolution requires a genuinely new object, built from
scratch in the non-Polish non-distributive regime, not transported from any existing field.

## 3k. GTW non-spatial / whirly Polish-group actions — KILLED (2026-06-30, /audit pure, primary-source verified)

New lead probed: Mackey–Ramsay point-realization (locally compact group ⟹ Boolean action
has a spatial point-model) FAILS for non-locally-compact Polish groups — Glasner–Tsirelson–Weiss
/ Glasner–Weiss ("Spatial and non-spatial actions of Polish groups", ETDS 25.5 (2005) 1521–1538)
build Boolean actions with NO spatial model; Lévy groups give **whirly** actions (ergodic at
the identity) ⟹ no nontrivial spatial factors (Pestov, arXiv:0903.0191). The HOPE: a studied
literature where "no point realization" is a *positive structural* phenomenon, non-Polish by
nature ⟹ maybe the non-Polish witness Ψ needs.

**KILLED — same definability-vs-existence fault line as §3j (CBER), one level earlier.**

1. A Boolean action is a homomorphism `G → Aut(X,μ)`; the σ-additive measure **μ is given as
   data and never threatened**. Whirly precludes a *spatial (Borel point) realization of the
   action* — "whirly ⟺ no nontrivial spatial **factors**" (Glasner–Weiss §1, primary source) —
   NOT the existence of any invariant state. A **representation/definability** obstruction, not
   an **existence** one. Clause (ii) needs ABSOLUTE non-existence (≥ measurable); GTW gives "no
   point model while μ persists." The §3j/§3f non-sequitur, verbatim.

2. **Group mismatch.** The OML carrier is static — no native acting group. Manufacturing one
   relocates "build a new object by hand" into dynamical clothing (rhyme, not transfer —
   cf. [[mixing_barycenter_transfer_rhyme]]).

3. **Wrong witness-type entirely (the decisive corollary).** GTW's carrier is a Boolean
   **atomless** measure algebra, which by atomlessness has **NO σ-additive 2-valued states at
   all**. GTW's world is devoid of the object Ψ is about, independent of the points question;
   non-distributivity is never even reached. On ∏ₙMO₂ the mechanism isn't defined without
   manufacturing structure.

**Flag:** Mackey–Ramsay locally-compact point-realization relied on via GTW's own citation,
not the 1962/66 originals — fine per secondary source, noted. All other statements
(whirly def, "whirly ⟺ no spatial factors," Boolean action = hom into Aut(X,μ), LC = sharp
line, Lévy ⟹ whirly) primary-source verified (Glasner–Weiss + Pestov). File as the **CBER
pattern (§3j), not a disjointification costume** — dies before reaching non-distributivity.
**Negative stays complete; no entering tool.** ⟦HAND/audit — verdict COSTUME, decline to invest.⟧

## 3l. Measured-groupoid native seam (Feldman–Moore / CFW / Gaboriau) — KILLED (2026-06-30, /audit pure, ×4 discriminators)

Probed the seam the §3k group-mismatch left untested: NOT a manufactured Polish group, but
whether a concrete non-Boolean OML's 2-valued-state problem is NATIVELY a measured groupoid —
objects = contexts (Boolean blocks), morphisms = compatibility overlaps, non-distributivity =
a non-trivial groupoid-cohomology class obstructing a global section. Distinct from the dead
X/E-quotient orbit-equivalence item (§3h): a genuinely new seam, NOT a re-derivation.

**KILLED on the two deepest standing walls — disjointification + definability-vs-existence.**

**Sharpest reason — the masa gate (CH-free).** Feldman–Moore (verified: equiv of categories,
countable measured equiv relations ⟺ **Cartan pairs**) is gated on a **Cartan masa = Boolean
`L∞(X,μ)`**. A non-Boolean OML's maximal abelian subalgebras ARE its blocks — many, none a
masa for the whole. To enter the framework you must produce one Boolean masa ⟹ either can't, or
force one and **flatten non-distributivity back to Boolean = ~12th disjointification costume**.
The masa-failure is STRUCTURAL + CH-free (non-distributivity *means* no single Boolean
subalgebra carries the whole). Akemann–Weaver is CH-dependent corroboration only, NOT
load-bearing.

**Four discriminators:** (1) MANUFACTURED at the measured level — combinatorial groupoid real,
but the measured structure (quasi-inv measure, Haar system) + Cartan masa not native; endowing
it smuggles in the σ-additive 2-valued data sought (circular). (2) DEFINABILITY-vs-EXISTENCE,
DECISIVE — measured-groupoid cohomology (Feldman–Moore/Series) is a.e. cocycles up to
*measurable* coboundary ⟹ obstructs a Borel/measurable section, NEVER absolute existence. Same
kill-weapon as §3j/§3k. (3) Unit space + Cartan masa IS Boolean ⟹ translation flattens the OML.
(4) Non-Polish witness needs uncountably many infinite blocks ⟹ outside Feldman–Moore's
countable-fiber regime ⟹ Hahn/Renault uncountable theory, structure theory *weaker* not
stronger, no 2-valued absolute obstruction. No escape hatch.

**⭐ NEW REUSABLE FINDING (the payload, not just a kill):** on ∏ₙMO₂ the "context-groupoid
cohomology" IS the **Abramsky–Mansfield–Barbosa sheaf/Čech cohomology of contextuality** —
finite-cover, **sufficient-not-necessary**, sitting AT the **Wright-1978 finite-contextuality
floor the problem lives strictly ABOVE.** ⟹ a clean general reason the ENTIRE cohomological-
groupoid corner (this + the H¹ costume, reduction_writeup §1a) is **SUB-THRESHOLD**: it can
only ever see finite-witness contextuality, and Ψ is by definition the no-finite-witness part.
Reusable as a one-line dismissal of any future cohomological framing.

**Flag (could not confirm — and that absence IS the point):** no specific *measured*-groupoid-
cohomology theorem delivers absolute (non-measurable) non-existence; the literature uniformly
defines these a.e./measurably. Sources: Feldman–Moore/Cartan survey arXiv:1009.0132; Marks
CFW notes; Akemann–Weaver PNAS 2008; measured bounded cohomology arXiv:2304.07765; Series
arXiv:math/0404257. **Negative stays complete; no entering tool.** ⟦HAND/audit — COSTUME.⟧

## 3m. THE MARRIAGE SYNTHESIS + masa-free-ultrafilter seam — SEAM-CLOSED-ABSENT (2026-06-30, /audit pure)

Synthesis of §3a–§3l into a two-ledger frame, plus an audit of the one seam §3l left
unverified ("masa structurally absent, NOT proven impossible").

### The two sides that must be married

The problem is ONE bridge: a single σ-class `𝒦` must satisfy BOTH halves at once, and
they REPEL at the join — every kill so far = forcing one side collapsed the other.

**SIDE A (set-theoretic / measure-theoretic — "no σ-state threads the gluing"):**
- Objects: a σ-class `𝒦` (closed under complement + countable disjoint union — Dynkin, NOT
  a σ-algebra); a **2-valued σ-additive non-principal selection** = the global section that
  must FAIL to exist. On a Boolean base that object = a countably-complete non-principal
  ultrafilter = **a measurable cardinal** (Ulam). Base must be **non-standard-Borel** (DW).
- Theorems: **Ulam** (2-valued σ-add non-principal ⟹ measurable carrier); **DW D.6 / Maharam
  §8.1** (Polish-representable ⟹ extension succeeds = upper boundary); **Loomis–Sikorski**
  (Boolean σ-rep) AND its **failure for OMLs** (where the mechanism would live, and doesn't).
- Difficulty flavour: consistency-strength (Ulam/large cardinals) + DST (non-standard-Borel).

**SIDE B (order-theoretic / quantum-logic — "carrier is genuinely non-Boolean"):**
- Objects: a concrete σ-complete OML; the **forbidden-intersection spec** `(S∩S′)×{0}∉𝒦`
  (= NOT intersection-closed = the non-distributivity, Lean `IntrinsicK.notIntersectionClosed`,
  forced on any witness by `witness_not_intersection_closed`); **irreducible non-centrality**
  (center-hybrid kill §3d: not central=segregated, not absent=Gleason).
- Theorems: **disjointification identity** `(a∨b)∧a⊥=b∧a⊥` distributive, FALSE on OMLs (faithful
  set-rep forces it ⟹ Boolean = the Floor); **Wright 1978** (finite witnesses always exist ⟹
  problem lives strictly ABOVE the finite floor); **RDP failure** (Dvurečenskij σ-rep needs
  Riesz Decomposition; MO₂ lacks it — the order-theoretic reason Side A's gluing can't import).
- Difficulty flavour: non-distributivity / no faithful Boolean rep. STRUCTURAL + CH-free.

**The marriage = `open.intrinsic_K`:** one `𝒦` carrying both. Lean pins the burden exactly —
`intrinsicK_suffices` (ingredients ⟹ witness, target correctly specified); `intrinsicK_gap_is_wallA`
(strip free clause (i) + structural (c), entire open content = **Wall A**, nothing more).
The missing theorem that WOULD be the marriage: **a non-distributive analogue of Ulam/Loomis–
Sikorski** — a principle producing measurable-strength 2-valued σ-additive NON-existence on a
carrier lacking the Boolean masa/RDP every known such principle requires.

### Is the problem "entirely set-theoretic"? NO — and that's a FENCE (cf. fence.independence_lean,
fence.cardinality_vs_strength). Set-theoretic in DIFFICULTY (non-Polish, possibly LC-flavoured),
order-theoretic in CONTENT (non-distributive gluing). "Non-Polish" is a NECESSARY condition on the
witness, NOT a reduction to pure set theory: the lattice structure is doing the killing (it hasn't
factored out), and the strength-bridge to a cardinal was REFUTED (§3f), so set-theoretic content
is unearned in both directions.

### The seam audit (the one genuinely-unverified piece): SEAM-CLOSED-ABSENT

Probed: can ANY non-Boolean object play the **ultrafilter role** (Side-A engine) WITHOUT a Boolean
masa/RDP — a Farah–Weaver quantum filter, a maximal quantum filter, a vN-side object? Or is the
absence PROVABLE (a "2-valued σ-state ⟹ block-supported" collapse theorem)?

**VERDICT: ABSENT, not PROVABLE.** No masa-free candidate survives, but the absence is *demonstrated
across the surveyed objects, not proven* — the not-impossibility half stays UNEARNED (refuting one
collapse statement kills one route to an impossibility proof, not impossibility). ⚠ EARLIER OVERCLAIM
CORRECTED (advisor, 2026-06-30): do NOT write "impossibility is foreclosed because a collapse would
trivialize Kochen–Specker" — (i) the collapse "2-valued σ-state ⟹ block-supported" is *directly*
false (δ_ω spans all blocks by ω∈A, no KS detour needed) and the KS link is shaky (KS lattice isn't
concrete); (ii) refuting one collapse ≠ foreclosing impossibility. Calibrated claim = rem:frontier's
"neither closed by an impossibility theorem nor reachable by a borrowed construction."

**⚠ THE "ROOT" SHARPENING WAS MIS-STATED — CORRECTED (advisor, 2026-06-30).** The displayed
biconditional "φ two-valued ⟺ φ|masa two-valued on a Boolean masa" is NOT B–W Prop 2.3 and is FALSE
read as a biconditional: Prop 2.3 is about states *on* the abelian algebra ℓ∞(κ) (pure ⟺ {0,1}-valued
THERE), not a masa-restriction characterization of an ambient state's two-valuedness (a pure state on
B(H) restricts to the non-2-valued |ξᵢ|² on the diagonal); and "masa" has no referent in an abstract
concrete OML. **The correct, paper-grade statement of the repulsion was ALREADY in the primary paper
(`sec:boundary` (1)+(3) + rem:no-bridge), stated more elementarily and without importing pure/masa
machinery:** the strength-carrier is an ultrafilter (intersection-closed), which non-distributivity
forbids; B–W's ultrafilter lives on the diagonal masa ℓ∞(κ), while on a concrete non-Boolean σ-OML
`ℱ_s={A:s(A)=1}` is a filter for NO 2-valued state — meet-closure fails already for δ_ω (in MO₂
a∩b≠∅ as sets yet a∧b=0 lattice-wise). That δ_ω computation IS the root, one level down from B–W's
masa. **Genuine session payload (survives): the seam audit confirmed the obvious masa-free surrogate
(Farah–Weaver quantum filters) is PURE-side, not 2-valued — beyond "structurally absent," the specific
surrogate is on the wrong side of the pure/2-valued line.** Strength-carriers masa-bound; non-Boolean
2-valued states built (Navara–Pták) ZFC-cheap; no known object is both.

**Could not confirm (absence corroborates):** no quantum-logic "ultrafilter" theory delivering a
σ-additive 2-valued NON-existence; literature gives only finite/algebraic facts (two-valued-state
logics) or pure-state machinery. No "2-valued σ-state ⟹ one block" theorem exists. Sources: B–W
arXiv:1607.08505 (primary, Prop 2.3 / Thm 2.4 / Lemma 4.3 verified); Farah–Weaver quantum filters;
Akemann–Weaver PNAS 2008. **Strength stays GENUINELY UNKNOWN; resolution still needs a NEW object
built from scratch, not a borrowed engine. The marriage thesis is now sharpened, not a new lead.**
⟦HAND/audit — SEAM-CLOSED-ABSENT; impossibility not earned, not foreclosed.⟧

## 3n. The embedding-frame-change (large-cardinal via j:V→M, quantum set theory V^(Q)) — COSTUME (2026-06-30, /audit coherence)

The strongest lead of the "why can't this be stated" thread: since the ULTRAFILTER face of a
measurable cardinal collapses on an OML (meet-closure vs. incompatibility, §3m/axiom-level), maybe
the EMBEDDING face — `j:V→M`, crit pt κ, equivalent to the ultrafilter ON BOOLEAN MODELS — has a
NON-Boolean incarnation that carries the strength without a Boolean ultrapower. This is the one move
that SWAPS THE PRIMITIVE rather than re-dressing it. Pressure-tested for COHERENCE first (is the
question even well-formed?).

**VERDICT: COSTUME — well-formed, but reduces to the disjointification wall via the COMMUTATOR GATE.**

NOT malformed: the steelman object EXISTS — **Takeuti/Ozawa quantum set theory `V^(Q)`**, a genuine
orthomodular-valued universe of set theory WITH a transfer principle (Ozawa, arXiv:0908.0367,
math/0604349). So "non-Boolean model theory with a transfer principle" is real, not a category error.
(My earlier "nobody has built this" was WRONG — Takeuti–Ozawa built it decades ago.)

**The kill (the third costume of the same wall):** Ozawa's transfer principle has the form
**`com(u₁,…,uₙ) ≤ ⟦φ(u₁,…,uₙ)⟧`** for Δ₀ formulas φ provable in ZFC, where `com` = the **commutator
projection** (degree of mutual commutativity). And **`com=1` (top) ⟺ the elements commute ⟺ they
generate a BOOLEAN subalgebra** (Marsden 1970; Pták–Pulmannová). Measurability — ultrafilter OR
embedding form — is an UNBOUNDED, high-complexity assertion far above Δ₀. Any orthomodular-valued
transfer strong enough to certify it FORCES `com=1` on the relevant constants = lands on the
abelian/Boolean core. **The commutator IS the disjointification obstruction in model-theory clothes.**
The E-face gives nothing the U-face didn't.

**⭐ THE WALL NOW SEEN AT THREE LEVELS (the reusable finding):** (1) axiom-level — ultrafilter
meet-closure collapses on incompatible elements (§3m); (2) the disjointification identity
`(a∨b)∧a⊥=b∧a⊥`; (3) NOW the **commutator gate on model-theoretic transfer** (Ozawa Δ₀ / com≤⟦φ⟧).
Same obstruction, three costumes. Łoś's theorem (elementarity of the ultrapower) uses the ultrafilter's
2-valued Boolean maximality per formula = the "ultra" axiom that collapses; there is NO non-distributive
Łoś theorem recovering full elementarity — only the com-gated Δ₀ fragment.

**Discriminators:** (1) type-error at ground SUPPORTS costume (j:V→M always has domain V, distributive
at ∈; L is just an element inside V) but V^(Q) defeats the PURE category-error reading. (2) distributivity
enters (U)⟺(E) at Łoś = the ultra-axiom. (3) NOT circular (V^(Q) transfer specified independently of any
collapsed ultrafilter — distinct from the Option-C quantum-filter revival). (4) STEELMAN = the decider:
V^(Q) is exactly non-Boolean model theory with a transfer principle, and it comes with a PUBLISHED SHARP
LIMIT (com-gated Δ₀); searches for any measurable/embedding notion INSIDE V^(Q) return nothing —
consistent with the commutator blocking exactly the unbounded assertions large cardinals need.

**Flags:** the "V^(Q) admits no measurable" reduction is UNPUBLISHED — composed here from cited
ingredients (Ozawa transfer + Marsden/PP commutator characterization), decisive as a costume but not a
lifted theorem. The Δ₀ `com≤⟦φ⟧` form is firsthand-verified; "unbounded quantifiers stay com-restricted"
is from search summaries (two arXiv PDFs failed extraction) — monotonicity of transfer makes the costume
hold in the weakest reading regardless. Sources: Ozawa arXiv:0908.0367 + math/0604349 + 2002.06692;
Marsden (Order, commutators); nLab measurable cardinal. **Leans (carefully) toward ¬Ψ: the reason
non-Boolean largeness can't be STATED is the same commutator obstruction — a sharper shape for the
eventual concentration theorem, NOT a proof. Does not escape the wall; file as the model-theory costume.**
⟦HAND/audit — COSTUME, the swap-the-primitive move reduces to the wall at the commutator.⟧

## 3o. Weaken-ultra / per-block-2-valued primitive — COSTUME (block-cover collapse) (2026-06-30, /audit pure)

The LAST untested filter-shaped bend. Every dead candidate kept "2-valued" and weakened
MEET-CLOSURE. This inverts: KEEP countable-meet-closure, WEAKEN ultra/maximality — a functional
2-valued+coherent on each block but not required globally 2-valued across incompatible blocks.
Hope: dodge the meet×ultra collapse while keeping σ-additive non-principal 2-valued-per-block strength.

**VERDICT: COSTUME — dies EARLIER than the predicted real-valued death, on the block cover.**

**The kill (elementary, decisive):** in any OML EVERY element lies in some block (`{0,a,a⊥,1}` → Zorn →
maximal Boolean subalgebra). So for incompatible a,b, both a∨b and a∧b still live in SOME block —
there is NO element "across incompatible blocks" escaping per-block evaluation. Hence any TOTAL
per-block-2-valued functional is 2-valued on ALL of L. The candidate forks with NO middle:
- **total branch** ⟹ globally 2-valued + σ-additive (orthogonal pairs share a block ⟹ per-block
  additivity IS global) + non-principal = **Ψ's original Side-A engine verbatim.** Wall un-dodged.
- **non-total branch** ⟹ (i) Isham–Butterfield topos/presheaf valuation = **Heyting-valued, ZFC-cheap**
  (quant-ph/9803055), or (ii) independent per-block choice = **segregated ∏ₙMO₂**, no strength. Both
  already-logged strength-free deaths.

**⚠ MY PREDICTED KILL WAS WRONG (correction).** I predicted COSTUME-REAL-VALUED ("across-block value
lands in [0,1]"). MIS-SPECIFIED: an ordinary [0,1]-state restricts to a GENERIC probability measure on
each block ⟹ 2-valued on essentially NO block. Per-block-2-valuedness and real-valued are INCOMPATIBLE;
imposing the former makes the real-valued branch UNREACHABLE. The candidate never reaches the real-valued
death — the block cover kills it first.

**⚠ NOT a 4th wall level (declined inflation).** There IS a "per-block-2-valued ⟹ Boolean-or-degenerate"
dichotomy, but via the TRIVIAL total/non-total block-cover split (Kalmbach/Greechie), NOT a deep
Bunce–Wright "must-be-real-valued" theorem. The middle is empty for a mundane covering reason. Do NOT
file as a sharpening of the wall (unlike §3n's commutator gate, which was a genuine 3rd level).

**⭐ THE STANDING RESULT (the real finding):** the FILTER-SHAPED primitive space is now EXHAUSTED. Every
bend — keep-all (§3m axiom), drop-meet (quantum filter §3m), localize-meet (segregated), swap-to-embedding
(§3n commutator), weaken-ultra (§3o block-cover) — reduces to the wall or to a strength-free object. **There
is NO non-Boolean FILTER-SHAPED primitive playing the ultrafilter's role.** The sole remaining move is the
CARRIER-CONSTRUCTION `open.intrinsic_K` (give up filter-shape, build the carrier directly) = the open
problem itself, no entering tool. "Is there a non-Boolean primitive?" is now answered for the filter-shaped
half: no. Facts (block cover, presheaf-is-Heyting) standard/textbook (Kalmbach; Isham–Butterfield
quant-ph/9803055), load-bearing only for a triviality. ⟦HAND/audit — COSTUME, filter-shaped space closed.⟧

## 3p. Frame-shift — reconceive the CARRIER (not the primitive) — COSTUME (2026-06-30, /audit pure)

FRAME-SHIFT SERIES (three untried moves after the filter-space exhaustion, §3o). Move 1:
since the largeness-PRIMITIVE hunt is closed, RECONCEIVE what "concrete OML carrier" MEANS
so the witness is native (the schemes/forcing analogue). Candidates: (A) sheaf/presheaf of
lattices, (B) topos-internal / Bohrification, (C) concreteness-without-faithfulness, (D)
Boolean/Heyting-valued carrier.

**VERDICT: COSTUME — no survivor.** (A/B) = redescription — the spectral presheaf re-presents
the SAME L; global-sections functor drags any witness back to the set-of-subsets, re-triggers
the Floor. (A/B/D) = ZFC-cheap HEYTING zone — KS-as-no-global-section (Isham–Butterfield) and
Bohrification (Heunen–Landsman–Spitters) are ZFC theorems, Heyting/real-valued; the
measurable-strength that makes Ψ interesting is GONE = the logged sub-threshold cohomology death.
(C) = redescription (proof below).

**⚠ MY PRIOR WAS WRONG (correction): (C) concreteness-without-faithfulness has NO teeth.**
I bet the Floor needs FAITHFULNESS while Gudder concreteness is only ORDER-DETERMINATION (weaker).
FALSE — they are IDENTICAL. ⟦HAND, 3-line, textbook-standard, not Lean-verified⟧: given an
order-determining set S of 2-valued STATES, `a ↦ {s∈S : s(a)=1}` IS a set representation (preserves
⊥ via s(a⊥)=1−s(a); preserves orthogonal joins since 2-valued states are additive on orthogonal
pairs ⟹ disjoint images; injective since S order-determining). So "state-concrete but not
set-representable" is EMPTY.

**⭐ THE REUSABLE CLARIFICATION (three notions, kept distinct — primary-source: SEP qt-quantlog +
arXiv:2401.13798 Def 1.1):**
- (i) **set-representable / concrete** = full set of 2-valued **STATES** — WEAK, non-Boolean is FINE
  (MO₂ is concrete). Closure under complement + DISJOINT union, NOT arbitrary union ⟹ imposes NO
  distributivity. = the programme's carrier.
- (ii) **Boolean embedding** = full set of 2-valued **HOMOMORPHISMS** (Zierler–Schlessinger 1965 / KS)
  — forces distributive, fails for QM.
- (iii) **σ-tribe** = concrete + σ-additive / countable unions — the Floor's σ-version.
**The Floor is (iii)-under-σ-additivity ⟹ Boolean, NEVER (i)-forces-Boolean.** The carrier was NEVER
the locus of the wall — ∏ₙMO₂'s existence already proves "concrete" never forced Boolean. There is NO
carrier-Floor for a reconception to liberate; the "faithful forces Boolean" fact is about (ii)/(iii),
not the state-carrier (i). *(Guards against the recurring conflation of state-concreteness with
homomorphism-Boolean-embeddability.)*

**What (C) leaves standing = the pre-existing residue, verbatim:** is there a non-distributive L,
order-determined by 2-valued states (finitely concrete), whose countable orthogonal joins fail to
realize as countable disjoint unions of a set (NOT σ-tribe-representable)? = **Wall A / σ-LS residue.**
So the wall lives NOT at concreteness but at the **finitary→σ gap in the tribe representation** — a
sharpening of location, not a new escape. Flag: the 3-line proof is HAND (textbook Gudder construction),
not Lean-verified; Z–S numbering from secondary sources. ⟦HAND/audit — COSTUME, carrier is not the locus.⟧

## 3q. Frame-shift — reconceive the EXTENSION RELATION (not the state/carrier) — COSTUME (2026-06-30, /audit pure)

Frame-shift 2/3. Ψ is a NON-EXTENSION ("s₀ extends to no global σ-additive 2-valued state"); no
prior move targeted the extension RELATION itself. Reconceive "extends": (A) partial/approximate,
(B) into an enlarged/completed carrier L'⊇L, (C) different morphism category, (D) dualize.

**VERDICT: COSTUME — swept, no survivor.** Pinned by POLARITY: any weakening of "extends" that makes
extensions EASIER supplies a RESCUER (refutes the witness); any restatement preserving the unit-test
verdict is a REDESCRIPTION. No slack between.
- **(A)** COSTUME-RESCUER: finitely-additive/barycentric extensions ALWAYS exist (S_df compact,
  fact.sdf_compact); an always-existing approximate extension = S_df-hull triviality.
- **(B)** REDESCRIPTION: any faithful L'⊇L has its states restrict ⟹ L-non-extension ⟹ L'-non-extension
  trivially; the "forcing-style enlargement to host the state" reading = rescuer / Lévy–Solovay wrong-engine.
- **(C)** REDESCRIPTION: a 2-valued state IS a σ-hom to {0,1}; keep target=2 ⟹ same verdict, change
  target ([0,1]/effect algebra) ⟹ states always exist = rescuer.
- **(D)** REDESCRIPTION of wall.tribe_vs_points: dual of "no global 2-valued state" = "no point of the
  dual space"; non-distributivity blocks the clean duality ⟹ the duality IS the obstruction, not a route.

**⚠ MY PRIOR WAS WRONG AGAIN (correction, primary-source): completions do NOT re-Booleanize.** I predicted
B/D die by the Floor forcing distributivity on the completion. FALSE — the **MacNeille completion of an OML
does NOT force distributivity** (Harding 1991, "OMLs whose MacNeille completions are not OML"; it can fail
to even be an OML). **The Floor bites ONLY for tribe-of-SETS (concrete) representations, NOT for lattice
completions.** (Second time this series over-attributed the Floor — cf. §3p. Floor = concrete-rep-specific.)

**(4) σ-completion-staying-non-distributive — the one branch with teeth — dies on a FORK:** (Horn 1,
vacuous) Wall A's carrier is ALREADY σ-complete ⟹ no completion question inside it = the struck "weld run"
(reduction_writeup #159–181, welded two orthogonal walls, subtracted). (Horn 2, the wall) start from
non-σ-complete L₀ ⟹ "does L₀ embed into a σ-complete non-Boolean CONCRETE OML" IS Harding–Wang Problem 2 /
σ-Loomis–Sikorski (wall.hw2, wall.no_sigma_ls), open, no new tractability; and MacNeille buys σ-completeness
at the cost of possibly LOSING OML-ness + concreteness (both Ψ requires) = extra nails. Does NOT differ from
Wall A / HW2.

**Net:** the extension-relation axis is a GENUINE new direction to have looked, now swept — no witness, no
new tractable statement. Joins the closed frontier. Flags: MacNeille-non-Booleanization from Harding
abstracts/notes (nmsu, ESSLLI5) not full papers — but it only REMOVES a kill, verdict robust; HW "cannot be
regularly embedded into σ-complete OMP" from arXiv:2108.09819 search summary, check if ever load-bearing.
⟦HAND/audit — COSTUME, extension relation swept.⟧

## 3r. Frame-shift — reconceive toward ¬Ψ (the INVARIANT hunt) — NO ATTACKABLE INVARIANT (2026-06-30, /audit)

Frame-shift 3/3, and the DIFFERENT-shaped one: not "is X a costume" but "is there a genuine INVARIANT
Inv(L,s₀) whose computation FORCES extendability uniformly — a ¬Ψ proof as a computation, not a search?"
A survivor would convert 'the programme leans toward ¬Ψ' into 'here is the smaller theorem to prove.'
Candidates: (A) commutator-degree, (B) σ-additive cohomology, (C) definability rank, (D) graded RDP-failure.
Both fences enforced: NOT the refuted LB mechanism (§3f), NOT the independence-lean.

**VERDICT: NO ATTACKABLE INVARIANT — COSTUME across all four. Both fences respected (this is 'no invariant
here', NOT an answer-type ranking).**
- **(A) commutator-degree** — WALL-RENAMED + CIRCULAR (decisive). Marsden commutator is a LATTICE ELEMENT,
  not a scalar; theory gives a BINARY Boolean/non-Boolean decomposition, not a grade (primary: Springer
  BF02034335; Bruns–Greechie; Greechie–Herman). A's formulation requires proving "low-commutator region
  empty of coherent σ-additive 2-valued patterns" = ¬Ψ ITSELF ⟹ circular. Non-Boolean everywhere on ∏ₙMO₂
  yet extends ⟹ no predictive value.
- **(B) σ-additive cohomology** — provably SUFFICIENT-NOT-NECESSARY (primary: arXiv:1111.3620; Oxford diss.
  cs.ox.ac.uk/files/7608 — "not a complete invariant for strong contextuality"). No σ/countable-cover
  refinement exists; vanishing ≠ extension-exists ⟹ can't certify ¬Ψ. Sub-threshold (=fact.cohomology_subthreshold).
- **(C) definability rank** — §3j non-sequitur, now with a COMPLEXITY argument (the reusable addition,
  ⚠ VOCABULARY CORRECTED per advisor): Ψ is a **set-theoretic existential over carriers of UNBOUNDED
  cardinality** (the witness is uncountably generated, ≥2^ℵ₀, non-Polish by construction) — NOT a projective
  statement about a fixed real, so the "Σ²₁/third-order" pin is the WRONG vocabulary (the analytical hierarchy
  + Shoenfield's Σ¹₂ ceiling classify statements over a FIXED real parameter). Honest defensible version: Ψ is
  an unbounded set-theoretic existential, so DST absoluteness theorems simply DO NOT APPLY — a rank bound gives
  "no BOREL/definable section," and nothing promotes it to "no section." Definability-not-existence, because the
  object isn't a fixed-real statement at all.
- **(D) graded RDP-failure** — WALL-RENAMED. RDP is BINARY in the literature (RDP₁/RDP₂ are STRENGTHENINGS,
  not gradations; primary: Dvurečenskij σ-LS). Every admissible non-segregated carrier has FULL RDP failure
  (the disjointification identity IS the failing refinement) ⟹ "degree" constant-maximal everywhere, no
  predictive value.

**⭐ THE ABSOLUTENESS ARGUMENT (reusable, more than a costume; ⚠ vocabulary corrected per advisor):** Ψ is an
existential over carriers of **UNBOUNDED cardinality** (the witness is uncountably generated, ≥2^ℵ₀, non-Polish
by construction) — NOT a projective statement over a fixed real. So it is NOT correctly pinned as "Σ²₁/third-order"
(the analytical hierarchy + Shoenfield's Σ¹₂ ceiling classify FIXED-real statements). The defensible claim: DST
absoluteness theorems simply DO NOT APPLY to an unbounded set-theoretic existential, so the definability route
(C, and §3j CBER) structurally cannot deliver ¬Ψ — "no Borel/definable section" never promotes to "no section."
Not a costume — a structural reason the no-Borel-section approaches can never reach existence non-existence.

**⭐⭐ THE TWO-FAMILY FACTORIZATION (the closing schema — two independent audit runs converged on it):**
EVERY candidate invariant factors into two families, and ¬Ψ lives in the gap between them:
- **Family (I) — finitary non-distributivity measures** (commutator-degree A, RDP-failure D, finite-cover
  Čech H¹ B-finite): ZFC-absolute, local, AT/BELOW the Wright-1978 finite floor. Ψ is DEFINED as the
  no-finite-witness part (strictly above the floor) ⟹ these are SUB-THRESHOLD BY CONSTRUCTION, taking the
  SAME value on ∏ₙMO₂ and on any witness. (Generalizes fact.cohomology_subthreshold from cohomology to all.)
- **Family (II) — σ-level definability ranks** (Borel/projective rank C, measurable-cover cohomology B-measurable):
  reach the σ-level but measure DEFINABILITY ⟹ "no Borel/measurable section," never "no section" (§3j).
A ¬Ψ proof must compute a quantity that is **σ-level AND existence-absolute AND non-distributivity-sensitive**
at once. Family (I) misses σ-level; Family (II) misses existence-absolute; that exact conjunction IS Wall A /
open.intrinsic_K = Ψ renamed. So the INVARIANT-SHAPED space is now CLOSED the same way the filter-shaped space
is (fact.filter_space_exhausted) — a reusable one-line dismissal of future invariant-shaped proposals. The
deep reason Family (II) can't reach existence-absolute: Ψ is an existential over UNBOUNDED-cardinality carriers,
not a fixed-real projective statement, so DST absoluteness theorems do not apply at all (see (C) above).

**Net:** no invariant is a theorem SMALLER than Ψ; each equals ¬Ψ (A circular), certifies the wrong direction
(B), certifies definability-not-existence (C), or is the wall renamed (A/D). The convergence holds: every
invariant route bottoms out at the disjointification identity or the definability/existence gap. Resolving Ψ
still needs a genuinely new object, not a computed invariant. Flag: (D)'s "lattice effect algebra has RDP ⟺ MV"
carried from §3i, not re-verified this pass; the "Σ²₁" complexity pin was corrected to the vaguer-but-defensible
"unbounded set-theoretic existential ⟹ DST absoluteness doesn't apply". ⟦HAND/audit — no survivor; the two-family
schema + the unbounded-existential reason are the keepers.⟧
