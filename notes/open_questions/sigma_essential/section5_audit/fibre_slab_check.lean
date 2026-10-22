import QuerySystem.UlamWitnessLatticeGap

open Set

namespace SigmaEssential.Ulam

variable {M : Type*} [LinearOrder M]

theorem trace_slabAt (g f : Fin 4) :
    trace (Prod.snd ⁻¹' ({g} : Set (Fin 4))) f
      = (if f = g then (Set.univ : Set M) else ∅) := by
  ext x
  simp only [trace, Set.mem_setOf_eq, Set.mem_preimage, Set.mem_singleton_iff]
  split <;> simp_all

theorem slabAt_codes_differ (huncount : ¬ (Set.univ : Set M).Countable)
    (ξ : Set M) (κ : Fin 4 → Bool) {g f : Fin 4} (hf : f ≠ g)
    (h : Represents (Prod.snd ⁻¹' ({g} : Set (Fin 4))) ξ κ) :
    κ g ≠ κ f := by
  intro hEq
  have h0 := h g; have hg := h f
  rw [trace_slabAt] at h0 hg
  rw [if_pos rfl] at h0
  rw [if_neg hf] at hg
  rw [hEq] at h0
  unfold CEq at h0 hg
  apply huncount
  refine Set.Countable.mono ?_ (h0.union hg)
  intro x _
  by_cases hx : x ∈ sel ξ (κ f)
  · right; simp [Set.mem_symmDiff, hx]
  · left;  simp [Set.mem_symmDiff, hx]

/-- Every fibre slab `M × {g}` is outside the carrier; `g = 3` is the paper's
`M × {4}` (Lean fibres are `0..3`). -/
theorem slabAt_not_mem (U : UlamMatrix M)
    (huncount : ¬ (Set.univ : Set M).Countable) (g : Fin 4) :
    ¬ (carrier U).Has (Prod.snd ⁻¹' ({g} : Set (Fin 4))) := by
  intro hmem
  obtain ⟨ξ, κ, hEven, _hκ3, hrep⟩ := nrep_exists huncount hmem
  unfold EvenCode at hEven
  have d := fun f (hf : f ≠ g) => slabAt_codes_differ huncount ξ κ hf hrep
  revert hEven d
  fin_cases g <;>
    cases h0 : κ 0 <;> cases h1 : κ 1 <;> cases h2 : κ 2 <;> cases h3 : κ 3 <;>
    simp_all [Fin.forall_fin_succ]

/-- The joint-failure region of the triple is a pairwise meet region of any two
core complements. -/
theorem slab3_eq_compl_inter :
    (coreA M)ᶜ ∩ (coreB M)ᶜ = Prod.snd ⁻¹' ({3} : Set (Fin 4)) ∧
    (coreA M)ᶜ ∩ (coreC M)ᶜ = Prod.snd ⁻¹' ({3} : Set (Fin 4)) ∧
    (coreB M)ᶜ ∩ (coreC M)ᶜ = Prod.snd ⁻¹' ({3} : Set (Fin 4)) := by
  refine ⟨?_, ?_, ?_⟩ <;> ext ⟨x, f⟩ <;> fin_cases f <;> simp [coreA, coreB, coreC]

end SigmaEssential.Ulam

#print axioms SigmaEssential.Ulam.slabAt_not_mem
#print axioms SigmaEssential.Ulam.slab3_eq_compl_inter
