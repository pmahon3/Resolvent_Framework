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

**Center hybrid FAILS on a dichotomy ⟦HAND, advisor-pending — load-bearing, confirm when
advisor is back⟧:**
- *Trivial center* (`{∅,Ω}`): the witness is REQUIRED irreducible (`rem:offcenter`,
  Def). But trivial center ⟹ Gleason exceptionality ⟹ geometry forces σ-additivity ⟹ NO
  obstruction to route. (This is why L(H), a factor, is σ-additively "easy".)
- *Non-trivial center*: hosts the obstruction, BUT the carrier is then **segregated**
  (`rem:segregated`) — contextuality routed through a central Boolean factor, σ-states
  concentrate at points ⟹ NO witness, EXCLUDED.
- **Both horns kill it.** The place the hybrid would put the strength (the center) is exactly
  the place the witness requirement forces to be either trivial (no obstruction) or
  disqualifying (segregated). No inhabited middle.

**RESIDUE (the genuine gain, not consolation).** The center analysis SHARPENS the target: the
witness's non-distributivity can be neither central (segregated, excluded) nor absent
(Gleason, no obstruction) — so the σ-obstruction must live in the **irreducible, non-central
part**. That is exactly `open.intrinsic_K` (the unbuilt frontier carrier). The center hybrid,
by failing, CONFIRMS the obstruction is irreducibly non-central — narrowing the target rather
than hitting it. Standing stop-condition unchanged: needs a genuinely NEW object, not a
strength supplier (which the hybrid shows is correctly factored out).

**⚠ TO CONFIRM WITH ADVISOR (overloaded this turn):** the center dichotomy rests on (a)
Gleason-exceptionality applying to ALL trivial-center OMLs (not just L(H)/Hilbert factors —
if it's L(H)-specific, a trivial-center NON-Hilbert OML might escape and reopen the hybrid),
and (b) `rem:segregated` excluding ALL non-trivial-center carriers. Both are in-paper but the
"Gleason generalizes to all factors" step is the one to pressure-test.

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
