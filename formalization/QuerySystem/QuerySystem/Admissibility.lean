/-
Copyright (c) 2026. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Patrick S. Mahon
-/
import QuerySystem.SigmaEssentialOpenCore
import QuerySystem.ConcreteOMLPatterns
import QuerySystem.UlamWitnessLatticeGap

/-!
# Admissibility, with the axioms retired

`SigmaEssentialOpenCore` carried the admissible carrier class as six conjuncts,
two of them opaque `axiom`s (`IsIrreducible`, `IsNonSegregated`). The instruction
recorded in `notes/open_questions/oml_attack/ADMISSIBILITY_SCOPE.md` was:

> Do not touch the four axioms until the corresponding forcing lemma is proved.
> Each should be RETIRED by a theorem about the witness, not DEFINED into
> existence.

Both forcing lemmas now exist, and were sitting unused:

* `Blocks.witness_not_segregated` — a witness carrier is not segregated;
* `Ulam.central_countable_or_cocountable` (`cor:centre`) — every central element
  of `L₁` is countable or co-countable.

So the axioms are retired here rather than defined away. This module lives above
`ConcreteOMLPatterns` and `UlamWitnessLatticeGap` because that is where those two
lemmas are; the open core sits below both and could not see them, which is why
the bundle was stuck as axioms in the first place.

## What the bundle now says

Four of the original six conjuncts said nothing. Concreteness and
σ-completeness hold of *every* `DynkinSystem`, and non-intersection-closure and
non-Polish-representability are *forced* by the witness they are conjoined to
(`OpenCore.witness_not_intersection_closed`, `OpenCore.witness_not_polish`). So
`Admissible` is the two that bite, and both are now definitions with content.

## The capstone

`L₁_admissible` — the ω₁ product-Ulam witness carrier is admissible, both
conjuncts proved, no repo-local axiom. That is the Ψ-fidelity gap
`ADMISSIBILITY_SCOPE.md` describes: `Psi` did not carry essential irreducibility
as a hypothesis, and now the carrier it is witnessed on provably has it.
-/

namespace SigmaEssential
namespace Admissibility

open Set MeasurableSpace SigmaEssential SigmaEssential.Blocks

variable {Ω : Type*} {d : DynkinSystem Ω}

/-! ## §1. The centre, and essential irreducibility -/

/-- **The centre of a carrier.** `E` is central when it lies in the carrier and
is compatible with every carrier element — concretely, every intersection
`E ∩ A` is again in the carrier. This is `Ulam.IsCentral` stated for an
arbitrary carrier. -/
def Centre (d : DynkinSystem Ω) (E : Set Ω) : Prop :=
  d.Has E ∧ ∀ A, d.Has A → d.Has (E ∩ A)

/-- **Essential irreducibility.** Every central element is trivial modulo the
countable ideal. "Modulo the countable ideal" is the programme's own qualifier —
`psi_ZFC` is stated for σ-classes irreducible in exactly this sense — and it is
what makes the notion satisfiable: `L₁`'s centre contains every countable and
every co-countable set, so plain triviality of the centre is too strong. -/
def EssentiallyIrreducible (d : DynkinSystem Ω) : Prop :=
  ∀ E, Centre d E → E.Countable ∨ Eᶜ.Countable

/-- **Non-segregation.** The negation of `Blocks.SegregatedStructural`: not every
finitely additive state is blockwise pointed. On a segregated carrier every
finitely additive state is σ-additive, so no witness can live there. -/
def NonSegregated (d : DynkinSystem Ω) : Prop := ¬ SegregatedStructural d

/-! ## §2. The bundle -/

/-- **The admissible carrier class.** The two conjuncts of the original six that
constrain anything, both now defined rather than assumed. -/
def Admissible (d : DynkinSystem Ω) : Prop :=
  EssentiallyIrreducible d ∧ NonSegregated d

/-- **The sharp Exit-A target.** A witness on an admissible carrier. -/
def TargetA_sharp : Prop :=
  ∃ (Ω : Type) (d : DynkinSystem Ω) (B : Block d) (s₀ : LocalState d B),
    Admissible d ∧ IsSigmaEssential s₀

/-- Dropping the admissibility data leaves a witness. -/
theorem targetA_sharp_gives_targetA (h : TargetA_sharp) : OpenCore.TargetA := by
  obtain ⟨Ω, d, B, s₀, _, hw⟩ := h
  exact ⟨Ω, d, B, s₀, hw⟩

/-! ## §3. The forcing lemmas, applied

Non-segregation is forced by the witness on any carrier. Essential
irreducibility is not — it is a genuine constraint, and `L₁` satisfies it by
`cor:centre`. -/

/-- **Non-segregation is forced.** Any witness carrier is non-segregated. -/
theorem witness_nonSegregated {B : Block d} {s₀ : LocalState d B}
    (hw : IsSigmaEssential s₀) : NonSegregated d :=
  witness_not_segregated hw

/-- **`L₁` is essentially irreducible**, by `cor:centre`. -/
theorem L₁_essentiallyIrreducible : EssentiallyIrreducible Ulam.L₁ := by
  intro E hE
  exact Ulam.central_countable_or_cocountable Ulam.M₁_uncountable Ulam.U₁ hE

/-- **The witness carrier is admissible.** Both conjuncts proved, on the standard
axioms alone. -/
theorem L₁_admissible : Admissible Ulam.L₁ :=
  ⟨L₁_essentiallyIrreducible, witness_nonSegregated Ulam.product_ulam_witness_ZFC⟩

/-- **So the sharp target is inhabited by the ω₁ witness.** `TargetA_sharp` is not
merely entailed by `Psi`; the object the programme already built satisfies it. -/
theorem targetA_sharp_ZFC : TargetA_sharp :=
  ⟨Ulam.M₁ × Fin 4, Ulam.L₁, Ulam.coreBlock Ulam.U₁, Ulam.s₀,
    L₁_admissible, Ulam.product_ulam_witness_ZFC⟩

/-! ## §4. The full six conjuncts, with nothing hidden by the trim

`Admissible` above keeps only the two conjuncts that constrain. That is a
redefinition, and a redefinition can flatter a result, so the original six are
recorded here for `L₁` with the one clause that is *not* unconditional carried
as a hypothesis. Five hold outright; non-Polish-representability needs the cut,
which is open (`OpenCore.DWPolishCut`). -/

/-- **All six original admissibility conjuncts for `L₁`.** Concreteness and
σ-completeness are automatic, essential irreducibility is `cor:centre`,
non-segregation is forced by the witness, non-intersection-closure is forced by
the witness, and non-Polish-representability is conditional on the cut. -/
theorem L₁_six_conjuncts (hcut : OpenCore.DWPolishCut.{0}) :
    OpenCore.IsConcreteCarrier Ulam.L₁ ∧ OpenCore.IsSigmaCompleteCarrier Ulam.L₁ ∧
      EssentiallyIrreducible Ulam.L₁ ∧ NonSegregated Ulam.L₁ ∧
      ¬ InterClosed Ulam.L₁ ∧ ¬ OpenCore.PolishRepresentable Ulam.L₁ :=
  ⟨OpenCore.isConcreteCarrier _, OpenCore.isSigmaCompleteCarrier _,
    L₁_essentiallyIrreducible,
    witness_nonSegregated Ulam.product_ulam_witness_ZFC,
    Ulam.carrier_not_interClosed,
    Ulam.carrier_not_polish hcut⟩

/-! ## Receipts -/

#print axioms L₁_essentiallyIrreducible
#print axioms witness_nonSegregated
#print axioms L₁_admissible
#print axioms targetA_sharp_ZFC
#print axioms L₁_six_conjuncts

end Admissibility
end SigmaEssential
