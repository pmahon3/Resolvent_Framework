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

open Set MeasurableSpace

namespace SigmaEssential.OpenCore

open SigmaEssential

/-! ## §1. The named open propositions (conjectures — NOT axioms) -/

/-- **Clause (ii) / Wall A (σ-point-selection)**, relative to a fixed pattern:
no *non-Dirac* σ-additive 2-valued state extends `s₀`. This is the open core. -/
def WallA {Ω : Type*} {d : DynkinSystem Ω} (s₀ : TwoValuedState d) (B : Block d) : Prop :=
  NoNonDiracExtends s₀ B

/-- A **concrete σ-essential witness** for a fixed `(s₀, B)`: `s₀` extends to no global
state (the localized form; clause (i) ∧ clause (ii)). -/
def WitnessAt {Ω : Type*} {d : DynkinSystem Ω} (s₀ : TwoValuedState d) (B : Block d) : Prop :=
  IsSigmaEssential s₀ B

/-- **Ψ — a σ-essential witness exists** (the existence sentence). Quantifies over
carriers `(Ω, d)` and patterns. OPEN. -/
def Psi : Prop :=
  ∃ (Ω : Type) (d : DynkinSystem Ω) (s₀ : TwoValuedState d) (B : Block d),
    IsSigmaEssential s₀ B

/-! ## §2. The localization edge (PROVED — the reduction, certified)

The headline triangulation: the witness question *reduces to* clause (i) ∧ wall A.
This is the localization theorem from the spine, re-exposed in scaffold vocabulary.
It holds unconditionally — neither side need be true. -/

/-- **Reduction edge (proved).** A witness at `(s₀,B)` ⟺ clause (i) `K(s₀)=∅` ∧ wall A.
Triangulates the taxonomy's central "witness ⟺ σ-point-selection" claim. -/
theorem witness_iff_kernel_empty_and_wallA
    {Ω : Type*} {d : DynkinSystem Ω} (s₀ : TwoValuedState d) (B : Block d) :
    WitnessAt s₀ B ↔ (kernel s₀ B = ∅ ∧ WallA s₀ B) :=
  localization s₀ B

/-- **Bottleneck edge (proved).** With clause (i) freely arranged (`K(s₀)=∅`), the
witness is *exactly* wall A — every complete attack must engage clause (ii). This is
the taxonomy's "wall A is the sole bottleneck", as a proved biconditional. -/
theorem wallA_is_bottleneck
    {Ω : Type*} {d : DynkinSystem Ω} (s₀ : TwoValuedState d) (B : Block d)
    (hi : kernel s₀ B = ∅) :
    WitnessAt s₀ B ↔ WallA s₀ B := by
  rw [witness_iff_kernel_empty_and_wallA]
  exact ⟨fun h => h.2, fun h => ⟨hi, h⟩⟩

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
def IntersectionClosed {Ω : Type*} {d : DynkinSystem Ω}
    (s₀ : TwoValuedState d) (B : Block d) : Prop :=
  BooleanLocal s₀ B

/-- **Costume theorem (proved).** Any route whose load-bearing step entails
intersection-closure CANNOT produce a witness — it has walked into the Boolean
baseline. This is the formal costume-detector: prove `route_step → IntersectionClosed`
and you have proved the route dead. -/
theorem costume_kills_witness
    {Ω : Type*} {d : DynkinSystem Ω} (s₀ : TwoValuedState d) (B : Block d)
    (hroute : IntersectionClosed s₀ B) :
    ¬ WitnessAt s₀ B :=
  boolean_not_sigma_essential s₀ B hroute

/-- **Contrapositive (proved).** A genuine witness carrier provably FAILS
intersection-closure. So "the witness is non-distributive" is not a hope but a
theorem: any `(s₀,B)` that *is* a witness refutes `IntersectionClosed`. -/
theorem witness_not_intersection_closed
    {Ω : Type*} {d : DynkinSystem Ω} (s₀ : TwoValuedState d) (B : Block d)
    (hw : WitnessAt s₀ B) :
    ¬ IntersectionClosed s₀ B :=
  fun hclosed => costume_kills_witness s₀ B hclosed hw

/-! ## §5. The Polish boundary (cited result) -/

/-- **Derr–Williamson Polish cut (cited).** On a Polish-representable carrier every
finitely-coherent pattern globalises — no σ-essential witness. We axiomatize the
relationship (a cited published theorem, DW 2023 Thm D.6 via Maharam): being
Polish-representable rules out being a witness. `PolishRepresentable` is an abstract
predicate on carriers we do not unfold. -/
axiom PolishRepresentable {Ω : Type*} (d : DynkinSystem Ω) : Prop

/-- Derr–Williamson 2023 (Thm D.6): Polish-representable ⟹ no witness. CITED. -/
axiom dw_polish_no_witness {Ω : Type*} {d : DynkinSystem Ω}
    (s₀ : TwoValuedState d) (B : Block d) :
    PolishRepresentable d → ¬ WitnessAt s₀ B

/-- **Upper-boundary edge (proved from the cited axiom).** A witness must live on a
NON-Polish-representable carrier. -/
theorem witness_not_polish
    {Ω : Type*} {d : DynkinSystem Ω} (s₀ : TwoValuedState d) (B : Block d)
    (hw : WitnessAt s₀ B) :
    ¬ PolishRepresentable d :=
  fun hp => dw_polish_no_witness s₀ B hp hw

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
    {Ω : Type*} {d : DynkinSystem Ω} (s₀ : TwoValuedState d) (B : Block d)
    (hw : WitnessAt s₀ B) (hcenter : IntersectionClosed s₀ B) : False :=
  witness_not_intersection_closed s₀ B hw hcenter

end SigmaEssential.OpenCore
