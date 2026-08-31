/-
Copyright (c) 2026. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Patrick S. Mahon
-/
import QuerySystem.SigmaEssentialOpenCore
import QuerySystem.ConcreteOMLPatterns
import QuerySystem.UlamWitnessLatticeGap
import QuerySystem.ConcreteDescent

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


/-! ## §5. Irreducibility proper, and why the descent carrier fails it

`EssentiallyIrreducible` is triviality of the centre *modulo the countable
ideal*. On an uncountable carrier that is a real condition — it is what
`cor:centre` establishes for `L₁`. On a COUNTABLE carrier it is vacuous, because
every subset is countable, and a predicate satisfied for that reason is
satisfied for no reason at all. So the plain notion is recorded alongside it,
and the two are kept apart. -/

/-- **Irreducibility proper.** The centre is trivial. Strictly stronger than
`EssentiallyIrreducible`, and not satisfied by `L₁` — every countable set is
central there, which is exactly why the programme works modulo the countable
ideal. -/
def Irreducible (d : DynkinSystem Ω) : Prop :=
  ∀ E, Centre d E → E = ∅ ∨ E = Set.univ

/-- Block `n` of the concrete descent carrier. -/
def descentBlock (n : ℕ) : Set QuerySystem.ConcreteDescent.Blk := {q | q.1 = n}

theorem descentBlock_mem (n : ℕ) :
    QuerySystem.ConcreteDescent.descentClass.Has (descentBlock n) := by
  intro m
  by_cases h : m = n
  · subst h
    have : QuerySystem.ConcreteDescent.fibre (descentBlock m) m = Set.univ := by
      ext x; simp [QuerySystem.ConcreteDescent.fibre, descentBlock]
    rw [this]; exact QuerySystem.ConcreteMO2.fam_univ
  · have : QuerySystem.ConcreteDescent.fibre (descentBlock n) m = ∅ := by
      ext x; simp [QuerySystem.ConcreteDescent.fibre, descentBlock, h]
    rw [this]; exact QuerySystem.ConcreteMO2.fam_empty

/-- **Every block is central.** Meeting a carrier element with a whole block
keeps every fibre inside `mo2Class` — it is that fibre, or empty. -/
theorem descentBlock_central (n : ℕ) :
    Centre QuerySystem.ConcreteDescent.descentClass (descentBlock n) := by
  refine ⟨descentBlock_mem n, fun A hA m => ?_⟩
  by_cases h : m = n
  · subst h
    have : QuerySystem.ConcreteDescent.fibre (descentBlock m ∩ A) m
        = QuerySystem.ConcreteDescent.fibre A m := by
      ext x; simp [QuerySystem.ConcreteDescent.fibre, descentBlock]
    rw [this]; exact hA m
  · have : QuerySystem.ConcreteDescent.fibre (descentBlock n ∩ A) m = ∅ := by
      ext x; simp [QuerySystem.ConcreteDescent.fibre, descentBlock, h]
    rw [this]; exact QuerySystem.ConcreteMO2.fam_empty

/-- **So the concrete descent carrier is NOT irreducible.** Block `0` is central
and is neither empty nor everything: the carrier is a direct sum of blocks, and
its centre is one element per subset of `ℕ`. -/
theorem descentClass_not_irreducible :
    ¬ Irreducible QuerySystem.ConcreteDescent.descentClass := by
  intro h
  rcases h _ (descentBlock_central 0) with he | hu
  · have : ((0, (true, true)) : QuerySystem.ConcreteDescent.Blk) ∈ descentBlock 0 := rfl
    rw [he] at this; exact this
  · have : ((1, (true, true)) : QuerySystem.ConcreteDescent.Blk) ∈ descentBlock 0 := by
      rw [hu]; trivial
    exact absurd this (by simp [descentBlock])

/-- **And `EssentiallyIrreducible` does not see that**, because the carrier is
countable and every subset of a countable type is countable. The predicate holds
VACUOUSLY here and is evidence of nothing. -/
theorem descentClass_essentiallyIrreducible_vacuously :
    EssentiallyIrreducible QuerySystem.ConcreteDescent.descentClass :=
  fun E _ => Or.inl (Set.to_countable E)


/-- **The vacuity does not reach `L₁`.** Its carrier is uncountable, so
"countable or co-countable" is a real dichotomy there and
`L₁_essentiallyIrreducible` has content. This is the guard on
`L₁_admissible`: the same predicate is satisfied by `descentClass` for no
reason at all. -/
theorem L₁_carrier_uncountable :
    ¬ (Set.univ : Set (Ulam.M₁ × Fin 4)).Countable := by
  intro h
  refine Ulam.M₁_uncountable ?_
  have himg := h.image Prod.fst
  rwa [Set.image_univ_of_surjective (fun m => ⟨(m, 0), rfl⟩)] at himg


/-! ## §6. The finite slice is not the Boolean baseline

`Blocks.no_witness_of_finite` gives Φ on every finite carrier. It is worth
checking that this is not `boolean_no_witness` wearing a hat, and the four-point
carrier settles it: `mo2Class` is finite and **not** intersection-closed, so the
Boolean baseline does not reach it, while the finite slice does. -/

/-- **The finite slice strictly extends the Boolean baseline.** `mo2Class` admits
no σ-essential witness, and it is not intersection-closed --- so it lies in the
finite slice and outside the reach of `boolean_no_witness`. -/
theorem mo2Class_finite_slice_beyond_boolean :
    (∀ (B : Block QuerySystem.ConcreteMO2.mo2Class)
        (s₀ : LocalState QuerySystem.ConcreteMO2.mo2Class B),
      ¬ IsSigmaEssential s₀) ∧
    ¬ InterClosed QuerySystem.ConcreteMO2.mo2Class :=
  ⟨fun _ s₀ => Blocks.no_witness_of_finite s₀,
    QuerySystem.ConcreteMO2.mo2Class_not_interClosed⟩

/-! ## Receipts -/

#print axioms L₁_essentiallyIrreducible
#print axioms witness_nonSegregated
#print axioms L₁_admissible
#print axioms targetA_sharp_ZFC
#print axioms L₁_six_conjuncts
#print axioms L₁_carrier_uncountable
#print axioms descentClass_not_irreducible
#print axioms descentClass_essentiallyIrreducible_vacuously
#print axioms mo2Class_finite_slice_beyond_boolean

end Admissibility
end SigmaEssential
