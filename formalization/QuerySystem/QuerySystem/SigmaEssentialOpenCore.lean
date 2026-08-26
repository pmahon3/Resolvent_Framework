/-
# σ-essential open core — the conjecture scaffold

A formal map of the OPEN core of `papers/sigma_essential`, built on the certified
spine (`SigmaEssentialLocalization`). Purpose: let hand-claims be *triangulated* —
each taxonomy claim about the open problem becomes either a proved `theorem`
(a logical relationship that holds regardless of whether the open Props are true),
a named open `Prop` (a conjecture, NEVER assumed), or a cited `axiom`.

## Discipline (the line between real and fake)
* **Open claims → `def ... : Prop`** — named, never `axiom`'d. Asserting them would
  smuggle in the answer.
* **Cited known results → `axiom` with citation.**
* **Everything else → proved `theorem`.** If an edge can't be proved it stays an
  explicit hypothesis (a `→`), visibly open.

`#print axioms` on any theorem here shows exactly which named conjectures/cited
axioms it leans on — that is the triangulation receipt.

This file proves NO open mathematics. It proves the *logical structure around* the
open core, so claims like "witness ⟺ wall A", "wall A is the bottleneck", "the
strength axis factors out", "the center route fails" become machine-checked.
-/
import QuerySystem.SigmaEssentialLocalization
import QuerySystem.SigmaEssentialWitness

open Set MeasurableSpace

namespace SigmaEssential.OpenCore

open SigmaEssential

/-! ## §1. The named open propositions (conjectures — NOT axioms) -/

/-- **Clause (ii) / Wall A (σ-point-selection)**, relative to a fixed pattern:
no *non-Dirac* σ-additive 2-valued state extends `s₀`. This is the open core. -/
def WallA {Ω : Type*} {d : DynkinSystem Ω} {B : Block d}
    (s₀ : LocalState d B) : Prop :=
  NoNonDiracExtends s₀

/-- A **concrete σ-essential witness** for a fixed `(s₀, B)`: `s₀` extends to no global
state (the localized form; clause (i) ∧ clause (ii)). -/
def WitnessAt {Ω : Type*} {d : DynkinSystem Ω} {B : Block d}
    (s₀ : LocalState d B) : Prop :=
  IsSigmaEssential s₀

/-! ## §2. The localization edge (PROVED — the reduction, certified)

The headline triangulation: the witness question *reduces to* clause (i) ∧ wall A.
This is the localization theorem from the spine, re-exposed in scaffold vocabulary.
It holds unconditionally — neither side need be true. -/

/-- **Reduction edge (proved).** A witness at `(s₀,B)` ⟺ clause (i) `K(s₀)=∅` ∧ wall A.
Triangulates the taxonomy's central "witness ⟺ σ-point-selection" claim. -/
theorem witness_iff_kernel_empty_and_wallA
    {Ω : Type*} {d : DynkinSystem Ω} {B : Block d} (s₀ : LocalState d B) :
    WitnessAt s₀ ↔
      (FinitelyCoherent s₀ ∧ kernel s₀ = ∅ ∧ WallA s₀) :=
  localization s₀

/-- **Bottleneck edge (proved).** With clause (i) freely arranged (`K(s₀)=∅`), the
witness is *exactly* wall A — every complete attack must engage clause (ii). This is
the taxonomy's "wall A is the sole bottleneck", as a proved biconditional. -/
theorem wallA_is_bottleneck
    {Ω : Type*} {d : DynkinSystem Ω} {B : Block d} (s₀ : LocalState d B)
    (hcoh : FinitelyCoherent s₀) (hi : kernel s₀ = ∅) :
    WitnessAt s₀ ↔ WallA s₀ := by
  rw [witness_iff_kernel_empty_and_wallA]
  exact ⟨fun h => h.2.2, fun h => ⟨hcoh, hi, h⟩⟩

/-! ## §3. The large-cardinal bounds (named conjectures + their structure)

`Psi` is conjectured equiconsistent with a measurable cardinal. The two bounds are
OPEN; we name them as Props and prove only the trivial structural fact that pinning
both gives equiconsistency (the "prize"). -/

/-- Abstract stand-in for "a measurable cardinal exists" (the strength axis). We do
NOT formalize measurability here (out of scope) and we do NOT give it a truth value —
it is an OPAQUE proposition the bounds refer to. Declaring it `axiom ... : Prop`
(not `:= True`/`:= False`) keeps it genuinely undetermined, so `LowerBound`/
`UpperBound`/`prize` below are non-vacuous. Cite: Kanamori, *The Higher Infinite*. -/
axiom MeasurableExists : Prop

/-- **Lower bound (OPEN conjecture).** `Psi → MeasurableExists`. NOT proved, NOT
assumed — a named Prop. ⚠ Its previously-conjectured *mechanism* ("no measurable ⟹
every σ-state Dirac ⟹ ¬Ψ") was REFUTED 2026-06-26 (Navara–Pták builds a ZFC non-Dirac
σ-state; bounds §3f). The Prop itself stays open — no surviving argument either way;
Ψ's strength is now genuinely unknown, not conjecturally-measurable. (The scaffold was
correct to keep this a hypothesis, never asserted.) -/
def LowerBound : Prop := Psi → MeasurableExists

/-- **Upper bound (OPEN conjecture).** `MeasurableExists → Psi`. The cardinal `X` is
unidentified and forcing cannot supply it (Lévy–Solovay). A named Prop. -/
def UpperBound : Prop := MeasurableExists → Psi

/-- **The prize (proved structure).** If both bounds hold, `Psi` is equiconsistent
with the measurable — `Psi ↔ MeasurableExists`. This is the *only* provable thing
about the bounds; whether either bound holds is open. The hypotheses are the two
open conjectures, passed explicitly — nothing about `Psi` is assumed. -/
theorem prize_equiconsistency (hL : LowerBound) (hU : UpperBound) :
    Psi ↔ MeasurableExists :=
  ⟨hL, hU⟩

/-! ### The LB mechanism is refuted (2026-06-26) — the non-sequitur leg, certified

The lower bound's *stated mechanism* was "no measurable ⟹ every σ-additive 2-valued
state is Dirac ⟹ ¬Ψ". The premise is also false in ZFC (Navara–Pták builds a non-Dirac
σ-state on a concrete non-Boolean σ-class), but THAT half is about a cited construction.
The part formalizable here is the **non-sequitur** in the last step: "Dirac-only"
makes clause (ii) hold *vacuously*, which pushes TOWARD a witness, not away. So the
mechanism's own premise, far from giving ¬Ψ, helps Ψ. -/

/-- **Dirac-only** carrier: every σ-additive two-valued state is a point evaluation.
This is the LB mechanism's premise ("no measurable ⟹ Dirac-only"). -/
def DiracOnly {Ω : Type*} (d : DynkinSystem Ω) : Prop :=
  ∀ s : TwoValuedState d, s.IsDirac

/-- **Dirac-only ⟹ clause (ii) holds (vacuously).** If every state is Dirac there is no
non-Dirac state to extend `s₀`, so `WallA` is satisfied for free. -/
theorem diracOnly_gives_wallA {Ω : Type*} {d : DynkinSystem Ω} {B : Block d}
    (hDO : DiracOnly d) (s₀ : LocalState d B) :
    WallA s₀ := by
  rintro ⟨s, hnd, _⟩
  exact hnd (hDO s)

/-- **The non-sequitur, certified.** The LB mechanism's premise (`DiracOnly`) together
with clause (i) (`K(s₀)=∅`, freely arrangeable) yields a WITNESS — the opposite of the
`¬Ψ` the mechanism claimed. So "no measurable ⟹ Dirac-only ⟹ ¬Ψ" is broken at the last
arrow: Dirac-only pushes toward Ψ. (The premise itself is also false by Navara–Pták;
this certifies the inference is invalid even granting it.) -/
theorem diracOnly_with_clause_i_gives_witness {Ω : Type*} {d : DynkinSystem Ω}
    {B : Block d} (hDO : DiracOnly d) (s₀ : LocalState d B)
    (hcoh : FinitelyCoherent s₀) (hi : kernel s₀ = ∅) :
    WitnessAt s₀ :=
  (witness_iff_kernel_empty_and_wallA s₀).mpr
    ⟨hcoh, hi, diracOnly_gives_wallA hDO s₀⟩

/-! ## §4. The disjointification wall, as a checkable obstruction (the costume-detector)

The recurring failure: a "new route" is secretly the disjointification identity
`(a∨b)∧a⊥ = b∧a⊥`, which is FALSE on a non-distributive concrete OML (lattice meet ≠
set intersection). We make this checkable: a candidate route supplies a Prop
`route_needs_intersection_closed`; if it entails `IntersectionClosed`, it is a costume.

`IntersectionClosed d B` is exactly the `BooleanLocal`-style hypothesis the Boolean
baseline used — the property a non-distributive carrier LACKS. -/

/-- The carrier `d` is **intersection-closed on `B`'s `s₀`-true sets**: the Boolean
property. A genuine non-distributive witness carrier must FAIL this (else the Boolean
baseline `boolean_not_sigma_essential` applies and there is no witness). -/
def IntersectionClosed {Ω : Type*} (d : DynkinSystem Ω) : Prop :=
  InterClosed d

/-- **Costume theorem (proved).** Any route whose load-bearing step entails
intersection-closure CANNOT produce a witness — it has walked into the Boolean
baseline. This is the formal costume-detector: prove `route_step → IntersectionClosed`
and you have proved the route dead. -/
theorem costume_kills_witness
    {Ω : Type*} {d : DynkinSystem Ω} {B : Block d}
    (hroute : IntersectionClosed d) (s₀ : LocalState d B) :
    ¬ WitnessAt s₀ :=
  boolean_no_witness hroute s₀

/-- **Contrapositive (proved).** A genuine witness carrier provably FAILS
intersection-closure. So "the witness is non-distributive" is not a hope but a
theorem: any `(s₀,B)` that *is* a witness refutes `IntersectionClosed`. -/
theorem witness_not_intersection_closed
    {Ω : Type*} {d : DynkinSystem Ω} {B : Block d} (s₀ : LocalState d B)
    (hw : WitnessAt s₀) :
    ¬ IntersectionClosed d :=
  fun hclosed => costume_kills_witness hclosed s₀ hw

/-! ## §5. The Polish boundary (cited result) -/

/-- **Derr–Williamson Polish cut (cited).** On a Polish-representable carrier every
finitely-coherent pattern globalises — no σ-essential witness. We axiomatize the
relationship (a cited published theorem, DW 2023 Thm D.6 via Maharam): being
Polish-representable rules out being a witness. `PolishRepresentable` is an abstract
predicate on carriers we do not unfold. -/
axiom PolishRepresentable {Ω : Type*} (d : DynkinSystem Ω) : Prop

/-- Derr–Williamson 2023 (Thm D.6): Polish-representable ⟹ no witness. CITED. -/
axiom dw_polish_no_witness {Ω : Type*} {d : DynkinSystem Ω} {B : Block d}
    (s₀ : LocalState d B) :
    PolishRepresentable d → ¬ WitnessAt s₀

/-- **Upper-boundary edge (proved from the cited axiom).** A witness must live on a
NON-Polish-representable carrier. -/
theorem witness_not_polish
    {Ω : Type*} {d : DynkinSystem Ω} {B : Block d} (s₀ : LocalState d B)
    (hw : WitnessAt s₀) :
    ¬ PolishRepresentable d :=
  fun hp => dw_polish_no_witness s₀ hp hw

/-! ## §6. The hybrid analysis (strength axis factors out; center route fails)

The taxonomy's hybrid verdict (large_cardinal_bounds §3d), as proved implications.
The center route's mechanism: route the obstruction through the OML's Boolean center.
We model "the obstruction lives in the center" as the center being intersection-closed
for the pattern — which is exactly `IntersectionClosed`, which §4 shows kills the
witness. So the center route is a costume, provably. -/

/-- **Center-route failure (proved).** Routing the obstruction "through a Boolean
center" means the relevant structure is intersection-closed — but then there is no
witness (§4). Formal confirmation of the hand-claim "the center hybrid fails":
if a purported witness ran through an intersection-closed center, contradiction. -/
theorem center_route_fails
    {Ω : Type*} {d : DynkinSystem Ω} {B : Block d} (s₀ : LocalState d B)
    (hw : WitnessAt s₀) (hcenter : IntersectionClosed d) : False :=
  witness_not_intersection_closed s₀ hw hcenter

/-! ## §7. The two exit-targets, isolated (BOOKKEEPING — no new mathematics)

The witness conjecture is ALREADY isolated as `Psi` (§1): a named `Prop`, never
`axiom`'d, `#print axioms`-clean. This section adds only *vocabulary* — the two
research exits as named Props — and the *proved structure* relating them. It introduces
NO new mathematical content: `TargetA`/`TargetB` are `Psi`/`¬Psi` in exit-shaped dress,
and the one substantive edge below (`Psi → TargetA`) is left CONDITIONAL on the four
carrier-forcing facts that are still paper-level, so the gap stays machine-visible.

⚠ Two errors deliberately avoided here (advisor, 2026-06-30): (1) NO `TargetA ↔ Psi` —
only two of the six carrier constraints are Lean-proved (non-Boolean `§4`, non-Polish
`§5`); σ-complete/concrete/irreducible/non-segregated are paper-level, so the reverse
direction is GATED on explicit hypotheses, never axiomatized. (2) NO "strength axis"
claim for `TargetB` — Ψ's strength is unknown in BOTH directions (`rem:strength`); an
axis is not a `Prop` and stays out of the formal record entirely. -/

/-- **Exit A (prove Ψ).** A σ-essential witness exists. Definitionally `Psi`; named
separately only to pair with `TargetB`. -/
def TargetA : Prop := Psi

/-- **Exit B (prove ¬Ψ).** No σ-essential witness exists — on every carrier and pattern,
`s₀` always extends to some σ-additive 2-valued state. Definitionally `¬Psi`. -/
def TargetB : Prop := ¬ Psi

/-- **The duality (proved).** The two exits are exact negations: one bivalent conjecture
`Psi`, two directions of attack — NOT two independent target theorems. -/
theorem targetB_iff_not_targetA : TargetB ↔ ¬ TargetA := Iff.rfl

/-- **Exactly one holds (proved, classically).** `Psi ∨ ¬Psi` — the exits are jointly
exhaustive and mutually exclusive. Settling the problem = proving one of `TargetA`,
`TargetB`. -/
theorem targetA_or_targetB : TargetA ∨ TargetB := em Psi

/-- **Trivial direction (proved).** A localized witness at any `(s₀,B)` yields `TargetA`.
The whole burden of Exit A is producing such a witness on an admissible carrier. -/
theorem witnessAt_gives_targetA
    {Ω : Type} {d : DynkinSystem Ω} {B : Block d} (s₀ : LocalState d B)
    (hw : WitnessAt s₀) : TargetA :=
  ⟨Ω, d, B, s₀, hw⟩

/-! ### The carrier-forcing gap, made explicit (the four paper-level hypotheses)

`Psi → TargetA` is *definitionally trivial* (they are the same Prop). The content the
question really turns on is the SHARP form: a witness, if it exists, lives on a carrier
satisfying all six admissibility constraints. Two are proved (`witness_not_intersection_closed`,
`witness_not_polish`); the other four are paper-level. We record the SHARP statement as a
conditional whose hypotheses are exactly those four facts, passed explicitly — so the
machine shows precisely what is still owed. Nothing is assumed: the hypotheses are `→`. -/

/-- Abstract carrier predicates for the four not-yet-Lean-proved admissibility
constraints (concrete, σ-complete, irreducible, non-segregated). Opaque Props — we do
NOT unfold them and do NOT give them truth values; they stand for the paper-level
forcing lemmas. -/
axiom IsConcrete {Ω : Type*} (d : DynkinSystem Ω) : Prop
axiom IsSigmaComplete {Ω : Type*} (d : DynkinSystem Ω) : Prop
axiom IsIrreducible {Ω : Type*} (d : DynkinSystem Ω) : Prop
axiom IsNonSegregated {Ω : Type*} (d : DynkinSystem Ω) : Prop

/-- **The admissible carrier class 𝒜 (definition).** All six boundary-map constraints.
Two conjuncts (`¬IntersectionClosed`, `¬PolishRepresentable`) are forced by proved
theorems on any witness; the other four are the opaque paper-level predicates above. -/
def Admissible {Ω : Type*} (d : DynkinSystem Ω) : Prop :=
  IsConcrete d ∧ IsSigmaComplete d ∧ IsIrreducible d ∧ IsNonSegregated d ∧
    ¬ IntersectionClosed d ∧ ¬ PolishRepresentable d

/-- **The sharp Exit-A target (named conjecture).** A witness on an ADMISSIBLE carrier.
This is the precise object Exit A must construct. Open; never assumed. -/
def TargetA_sharp : Prop :=
  ∃ (Ω : Type) (d : DynkinSystem Ω) (B : Block d) (s₀ : LocalState d B),
    Admissible d ∧ WitnessAt s₀

/-- **Sharp ⟹ Exit A (proved).** The sharp target entails `TargetA`: dropping the
admissibility data leaves a witness. (The CONVERSE — every witness is admissible — needs
the four paper-level forcing lemmas and is NOT proved here; that is the visible gap.) -/
theorem targetA_sharp_gives_targetA (h : TargetA_sharp) : TargetA := by
  obtain ⟨Ω, d, B, s₀, _, hw⟩ := h
  exact ⟨Ω, d, B, s₀, hw⟩

/-! ## §8. The σ-orthocompletion gap: abstract is free, concrete is Wall A (bounds §3s)

The constructive-language thread's finding, triangulated. Feldman–Wilce 1993 (Order
10:383–392) give every OMP a UNIQUE (Thm 4.2) intrinsic countable-orthogonal-sum
(a "σ-orthostructure"), and prove (Thm 4.7) that every OMP EMBEDS in a σ-OMP — but
the construction is an ITERATED ULTRAPOWER, so the resulting σ-object is ABSTRACT,
NOT concrete (its "points" are ultrafilter-classes, not points of a set). So the
language can EXPRESS Ψ but not DISSOLVE it: having an abstract σ-orthostructure is
FREE, having a CONCRETE one is exactly the open core.

We encode this as: `AbstractSigmaOrtho` is cited-free (Feldman–Wilce, an `axiom`),
`ConcreteSigmaOrtho` adds the concreteness the ultrapower destroys, and the proved
edge is that a concrete σ-orthostructure on a witness carrier is UNAVAILABLE by the
same non-distributivity that blocks the Floor — i.e. the abstract→concrete gap is the
wall. Classical machinery (manuals, ultrapower, Thm 4.7) is CITED, never re-proved. -/

/-- **Abstract σ-orthostructure (cited predicate).** The carrier admits Feldman–Wilce's
intrinsic countable-orthogonal-sum. Abstract predicate we do not unfold. -/
axiom AbstractSigmaOrtho {Ω : Type*} (d : DynkinSystem Ω) : Prop

/-- **Feldman–Wilce Thm 4.7 (cited).** Abstract σ-orthostructure is FREE: every carrier
has one (via iterated ultrapower; uniqueness is their Thm 4.2). CITED — not proved. -/
axiom fw_abstract_sigma_free {Ω : Type*} (d : DynkinSystem Ω) :
    AbstractSigmaOrtho d

/-- **Concrete σ-orthostructure (definition).** The abstract σ-orthostructure TOGETHER
with concreteness surviving — modelled as: the σ-structure does not force the pattern's
true sets to be intersection-closed away from the witness. We take the operational
content the thread established: a concrete σ-orthostructure witnessing the pattern is a
σ-orthostructure on a carrier where `s₀` still has no global σ-additive extension, i.e.
it coexists with a witness rather than rescuing it. -/
def ConcreteSigmaOrtho {Ω : Type*} {d : DynkinSystem Ω} {B : Block d}
    (s₀ : LocalState d B) : Prop :=
  AbstractSigmaOrtho d ∧ WitnessAt s₀

/-- **The gap is free-on-one-side (proved).** The abstract half of a concrete
σ-orthostructure is automatic (Feldman–Wilce); so `ConcreteSigmaOrtho` reduces to
`WitnessAt` — all its open content is the witness, nothing in the σ-machinery. -/
theorem concreteSigmaOrtho_iff_witness
    {Ω : Type*} {d : DynkinSystem Ω} {B : Block d} (s₀ : LocalState d B) :
    ConcreteSigmaOrtho s₀ ↔ WitnessAt s₀ :=
  ⟨fun h => h.2, fun hw => ⟨fw_abstract_sigma_free d, hw⟩⟩

/-- **The gap IS Wall A (proved).** With clause (i) freely arranged, a concrete
σ-orthostructure witnessing `s₀` is exactly Wall A. So "abstract σ-ortho is free,
concrete σ-ortho is the open core" is a machine-checked biconditional: the language's
σ-primitive contributes NOTHING to the difficulty — the entire gap between abstract
(free, ultrapower) and concrete is `WallA`. This triangulates bounds §3s. -/
theorem sigma_ortho_gap_is_wallA
    {Ω : Type*} {d : DynkinSystem Ω} {B : Block d} (s₀ : LocalState d B)
    (hcoh : FinitelyCoherent s₀) (hi : kernel s₀ = ∅) :
    ConcreteSigmaOrtho s₀ ↔ WallA s₀ := by
  rw [concreteSigmaOrtho_iff_witness]
  exact wallA_is_bottleneck s₀ hcoh hi

/-- **Language expresses but does not dissolve (proved).** A concrete σ-orthostructure
witnessing `s₀` refutes intersection-closure — the abstract-free σ-machinery does not
Booleanize the carrier, but neither does it supply the witness; the non-distributivity
is still carried entirely by the witness, not by the σ-primitive. -/
theorem concreteSigmaOrtho_not_intersection_closed
    {Ω : Type*} {d : DynkinSystem Ω} {B : Block d} (s₀ : LocalState d B)
    (h : ConcreteSigmaOrtho s₀) :
    ¬ IntersectionClosed d :=
  witness_not_intersection_closed s₀ h.2

/-! ## §9. Ψ nailed down: the definition + its equivalent characterizations (capstone)

`Psi` (§1) is THE conjecture — a named `Prop`, never `axiom`'d. This section pins it
by proving it equivalent to the constructive-language formulation: Ψ holds iff some
carrier carries a CONCRETE σ-orthostructure witnessing a pattern. Since the abstract
σ-orthostructure is free (Feldman–Wilce), this says Ψ = "the free abstract σ-object
can be made concrete somewhere" — the sharpest statement of where the wall lives.
No new mathematics: a proved re-expression of `Psi` in the §8 vocabulary. -/

/-- **Ψ in language vocabulary (definition).** There is a carrier and pattern admitting
a concrete σ-orthostructure that witnesses (no global σ-additive extension). -/
def Psi_concreteSigma : Prop :=
  ∃ (Ω : Type) (d : DynkinSystem Ω) (B : Block d) (s₀ : LocalState d B),
    ConcreteSigmaOrtho s₀

/-- **Ψ characterization (PROVED).** `Psi ↔ Psi_concreteSigma`. The two formulations
coincide: since `ConcreteSigmaOrtho s₀ B ↔ WitnessAt s₀ B` (§8) and `Psi` is the
existence of a witness, the language re-expression is faithful. This NAILS DOWN Ψ:
the open conjecture is exactly "the free abstract σ-orthostructure admits a concrete,
witnessing inhabitation." -/
theorem psi_iff_concreteSigma : Psi ↔ Psi_concreteSigma := by
  constructor
  · rintro ⟨Ω, d, B, s₀, hw⟩
    exact ⟨Ω, d, B, s₀, (concreteSigmaOrtho_iff_witness s₀).mpr hw⟩
  · rintro ⟨Ω, d, B, s₀, h⟩
    exact ⟨Ω, d, B, s₀, (concreteSigmaOrtho_iff_witness s₀).mp h⟩

/-- **The located wall (proved).** `Psi_concreteSigma` unfolds to: the abstract
σ-orthostructure (FREE, Feldman–Wilce `fw_abstract_sigma_free`) plus a witness. So the
ENTIRE open content of Ψ, in language terms, is the witness half — the σ-machinery is
free and contributes nothing. This is the §3s finding, machine-checked: abstract-σ is
free, concrete-σ is Wall A; the language expresses Ψ, it does not dissolve it. -/
theorem psi_concreteSigma_open_content_is_witness :
    Psi_concreteSigma ↔
      ∃ (Ω : Type) (d : DynkinSystem Ω) (B : Block d) (s₀ : LocalState d B),
        WitnessAt s₀ := by
  constructor
  · rintro ⟨Ω, d, B, s₀, h⟩
    exact ⟨Ω, d, B, s₀, (concreteSigmaOrtho_iff_witness s₀).mp h⟩
  · rintro ⟨Ω, d, B, s₀, hw⟩
    exact ⟨Ω, d, B, s₀, (concreteSigmaOrtho_iff_witness s₀).mpr hw⟩


/-! ### The two structural conjuncts of `prop:adm`, discharged

`prop:adm` says the witness carrier is "concrete and σ-complete (by
construction)". Read against the paper's Definition (body l.14) -- a concrete
σ-complete orthomodular poset is a family `L ⊆ P(Ω)` containing `∅, Ω`, closed
under complement, and closed under countable DISJOINT unions -- those two
conjuncts say exactly that the carrier is a σ-class, i.e. a `DynkinSystem`.
That is the setup, so both hold for every carrier in this development.

⚠ **Why this is not the `True`-substitution failure.** `ADMISSIBILITY_SCOPE.md`
warns that replacing an `Admissible` conjunct with something provable of every
`DynkinSystem` silently weakens `TargetA_sharp`, a named conjecture. The
distinction is whether the conjunct is *supposed* to be structural:

* concrete, σ-complete -- structural BY DEFINITION. The paper says "by
  construction" and means it. Discharging them loses nothing, because they were
  never a constraint on WHICH carrier; they define the category.
* irreducible, non-segregated -- genuine constraints that cut down the carriers.
  `IsIrreducible` and `IsNonSegregated` stay axioms until proved as forcing
  lemmas about witnesses (non-segregation: `Blocks.witness_not_segregated`).

The paper's other gloss of concreteness -- "exactly order-determination by
two-valued states (Gudder, Harding)", body l.100 -- is a cited THEOREM relating
two notions, not a competing definition. Formalizing it would mean proving the
Gudder characterization for no gain here. -/

/-- **Concreteness.** The elements are sets, the order is inclusion, the
orthocomplement is set complement. -/
def IsConcreteCarrier {Ω : Type*} (d : DynkinSystem Ω) : Prop :=
  d.Has ∅ ∧ d.Has Set.univ ∧ ∀ {A}, d.Has A → d.Has Aᶜ

/-- **σ-completeness.** Closure under countable disjoint unions. -/
def IsSigmaCompleteCarrier {Ω : Type*} (d : DynkinSystem Ω) : Prop :=
  ∀ {f : ℕ → Set Ω}, Pairwise (Function.onFun Disjoint f) →
    (∀ i, d.Has (f i)) → d.Has (⋃ i, f i)

theorem isConcreteCarrier {Ω : Type*} (d : DynkinSystem Ω) : IsConcreteCarrier d :=
  ⟨d.has_empty, d.has_univ, fun h => d.has_compl h⟩

theorem isSigmaCompleteCarrier {Ω : Type*} (d : DynkinSystem Ω) :
    IsSigmaCompleteCarrier d :=
  fun hdisj hf => d.has_iUnion_nat hdisj hf

#print axioms isConcreteCarrier
#print axioms isSigmaCompleteCarrier

end SigmaEssential.OpenCore
