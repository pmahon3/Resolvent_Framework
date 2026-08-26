/-
# Definitional-fidelity lemmas (closing the checklist's caveats in Lean)

`FIDELITY_CHECKLIST.md` identifies the one substantive encoding caveat: the
`LocalState` structure demands only complement-additivity inside `B`, which is
weaker than the paper's Def 1.2 restricted to `B`. This file closes it BOTH
ways, in Lean:

* `coherent_pattern_fully_additive` — clause (0) upgrades for free: a finitely
  coherent local pattern satisfies EVERY Def-1.2 additivity constraint on `B`
  (finite pairwise-disjoint family with union in `B` ⟹ union true iff some
  member true, and no two disjoint true members). So wherever the
  σ-essential definition applies, the pattern is a genuine state on `B`.
* `coreBlock_disjoint_eq_compl` — on the witness's block specifically, the only
  disjoint pairs are the complement pairs (the twelve cross-intersections are
  nonempty), so `LocalState` = Def 1.2-on-`B` exactly there, with or without
  coherence. Machine-checks Cor 6.4's parenthetical.

With these, the fidelity read reduces to pure transcription checks
(`FIDELITY_REVIEW.md`).
-/
import QuerySystem.UlamWitnessMain

open Set Function MeasurableSpace

namespace SigmaEssential

open SigmaEssential

variable {Ω : Type*} {d : DynkinSystem Ω} {B : Block d}

/-- Finite pairwise-disjoint unions of carrier sets are carrier sets. -/
theorem has_sUnion_finset (fam : Finset (Set Ω))
    (hmem : ∀ A ∈ fam, d.Has A)
    (hdisj : ∀ A ∈ fam, ∀ A' ∈ fam, A ≠ A' → Disjoint A A') :
    d.Has (⋃₀ (fam : Set (Set Ω))) := by
  classical
  induction fam using Finset.induction with
  | empty => simpa using d.has_empty
  | @insert A t hA ih =>
    have hUt : d.Has (⋃₀ (t : Set (Set Ω))) :=
      ih (fun C hC => hmem C (Finset.mem_insert_of_mem hC))
        (fun C hC C' hC' hne =>
          hdisj C (Finset.mem_insert_of_mem hC) C' (Finset.mem_insert_of_mem hC') hne)
    have hdisjA : Disjoint A (⋃₀ (t : Set (Set Ω))) := by
      rw [Set.disjoint_sUnion_right]
      intro C hC
      exact hdisj A (Finset.mem_insert_self A t) C
        (Finset.mem_insert_of_mem hC) (fun h => hA (h ▸ hC))
    have : (⋃₀ ((insert A t : Finset (Set Ω)) : Set (Set Ω)))
        = A ∪ ⋃₀ (t : Set (Set Ω)) := by
      simp [Set.sUnion_insert]
    rw [this]
    exact Ulam.DynkinSystem.has_union_disjoint d
      (hmem A (Finset.mem_insert_self A t)) hUt hdisjA

/-- A global finitely additive state is additive over finite pairwise-disjoint
families of carrier sets (`∃`-form; the at-most-one half is
`FinAddState.val_at_most_one`). -/
theorem FinAddState.val_sUnion_finset (μ : FinAddState d) (fam : Finset (Set Ω))
    (hmem : ∀ A ∈ fam, d.Has A)
    (hdisj : ∀ A ∈ fam, ∀ A' ∈ fam, A ≠ A' → Disjoint A A') :
    (μ.Val (⋃₀ (fam : Set (Set Ω))) ↔ ∃ A ∈ fam, μ.Val A) := by
  classical
  induction fam using Finset.induction with
  | empty =>
    simp only [Finset.coe_empty, Set.sUnion_empty]
    exact ⟨fun h => absurd h μ.not_val_empty, fun ⟨A, hA, _⟩ => absurd hA (by simp)⟩
  | @insert A t hA ih =>
    have hmem' : ∀ C ∈ t, d.Has C := fun C hC => hmem C (Finset.mem_insert_of_mem hC)
    have hdisj' : ∀ C ∈ t, ∀ C' ∈ t, C ≠ C' → Disjoint C C' :=
      fun C hC C' hC' hne =>
        hdisj C (Finset.mem_insert_of_mem hC) C' (Finset.mem_insert_of_mem hC') hne
    have hUt : d.Has (⋃₀ (t : Set (Set Ω))) := has_sUnion_finset t hmem' hdisj'
    have hdisjA : Disjoint A (⋃₀ (t : Set (Set Ω))) := by
      rw [Set.disjoint_sUnion_right]
      intro C hC
      exact hdisj A (Finset.mem_insert_self A t) C
        (Finset.mem_insert_of_mem hC) (fun h => hA (h ▸ hC))
    have hins : (⋃₀ ((insert A t : Finset (Set Ω)) : Set (Set Ω)))
        = A ∪ ⋃₀ (t : Set (Set Ω)) := by
      simp [Set.sUnion_insert]
    rw [hins, μ.val_union (hmem A (Finset.mem_insert_self A t)) hUt hdisjA,
      ih hmem' hdisj']
    constructor
    · rintro (h | ⟨C, hC, h⟩)
      · exact ⟨A, Finset.mem_insert_self A t, h⟩
      · exact ⟨C, Finset.mem_insert_of_mem hC, h⟩
    · rintro ⟨C, hC, h⟩
      rcases Finset.mem_insert.1 hC with rfl | hCt
      · exact Or.inl h
      · exact Or.inr ⟨C, hCt, h⟩

/-- **The coherence upgrade (fidelity closure).** A finitely coherent local
pattern satisfies every Def-1.2 additivity constraint on `B`: for a finite
pairwise-disjoint family of `B`-members whose union lies in `B`, the union is
`s₀`-true iff some member is, and no two distinct members are both true. So the
weaker `LocalState` structure is faithful wherever the σ-essential
definition (which requires coherence) applies: a coherent pattern IS a state on
`B` in the paper's full sense. -/
theorem coherent_pattern_fully_additive {s₀ : LocalState d B}
    (hcoh : FinitelyCoherent s₀) (fam : Finset (Set Ω))
    (hfam : ∀ A ∈ fam, A ∈ B.sets)
    (hdisj : ∀ A ∈ fam, ∀ A' ∈ fam, A ≠ A' → Disjoint A A')
    (hUnion : ⋃₀ (fam : Set (Set Ω)) ∈ B.sets) :
    (s₀.Val (⋃₀ (fam : Set (Set Ω))) ↔ ∃ A ∈ fam, s₀.Val A) ∧
    (∀ A ∈ fam, ∀ A' ∈ fam, A ≠ A' → s₀.Val A → ¬ s₀.Val A') := by
  obtain ⟨μ, hμ⟩ := hcoh
  have hmem : ∀ A ∈ fam, d.Has A := fun A hA => B.mem_has A (hfam A hA)
  constructor
  · -- transfer the union clause through μ
    rw [← hμ _ hUnion]
    rw [μ.val_sUnion_finset fam hmem hdisj]
    constructor
    · rintro ⟨A, hA, h⟩
      exact ⟨A, hA, (hμ A (hfam A hA)).mp h⟩
    · rintro ⟨A, hA, h⟩
      exact ⟨A, hA, (hμ A (hfam A hA)).mpr h⟩
  · -- at-most-one, through μ
    intro A hA A' hA' hne h h'
    have hμA : μ.Val A := (hμ A (hfam A hA)).mpr h
    have hμA' : μ.Val A' := (hμ A' (hfam A' hA')).mpr h'
    exact μ.val_at_most_one (hmem A hA) (hmem A' hA')
      (hdisj A hA A' hA' hne) hμA hμA'

end SigmaEssential

namespace SigmaEssential.Ulam

open SigmaEssential

variable {M : Type*} [LinearOrder M]

/-- Fiber preimages with a common fiber are not disjoint (given a point of `M`). -/
private theorem not_disjoint_fiber_preimages [Nonempty M]
    {S T : Set (Fin 4)} (f : Fin 4) (hfS : f ∈ S) (hfT : f ∈ T) :
    ¬ Disjoint (Prod.snd ⁻¹' S : Set (M × Fin 4)) (Prod.snd ⁻¹' T) := by
  intro h
  obtain ⟨x⟩ := ‹Nonempty M›
  have h1 : ((x, f) : M × Fin 4) ∈ (Prod.snd ⁻¹' S : Set (M × Fin 4)) := hfS
  have h2 : ((x, f) : M × Fin 4) ∈ (Prod.snd ⁻¹' T : Set (M × Fin 4)) := hfT
  exact Set.disjoint_left.mp h h1 h2

/-- **The witness block has no accidental orthogonality (fidelity closure,
Cor 6.4's parenthetical).** On `coreBlock`, disjoint members are complement
pairs: all twelve cross-intersections among the six core/complement sets are
nonempty. Hence on THIS block the `LocalState` structure captures Def 1.2
restricted to `B` exactly — the complement pairs are the only additivity
constraints that exist inside `B`. -/
theorem coreBlock_disjoint_eq_compl [Nonempty M] (U : UlamMatrix M)
    {A A' : Set (M × Fin 4)}
    (hA : A ∈ (coreBlock U).sets) (hA' : A' ∈ (coreBlock U).sets)
    (hdisj : Disjoint A A') (hne : A ≠ A') : A' = Aᶜ := by
  classical
  have hcompl : ∀ S : Set (Fin 4),
      ((Prod.snd ⁻¹' S : Set (M × Fin 4))ᶜ) = Prod.snd ⁻¹' Sᶜ := by
    intro S; ext p; simp
  simp only [coreBlock, Finset.mem_insert, Finset.mem_singleton] at hA hA'
  -- normalize all six members to fiber-preimage form and dispatch the 36 cases
  rcases hA with rfl | rfl | rfl | rfl | rfl | rfl <;>
    rcases hA' with rfl | rfl | rfl | rfl | rfl | rfl <;>
      simp only [coreA, coreB, coreC, hcompl, compl_compl] at hdisj hne ⊢ <;>
      first
        | rfl
        | exact absurd rfl hne
        | (exfalso
           revert hdisj
           first
             | exact fun h => not_disjoint_fiber_preimages 0 (by decide) (by decide) h
             | exact fun h => not_disjoint_fiber_preimages 1 (by decide) (by decide) h
             | exact fun h => not_disjoint_fiber_preimages 2 (by decide) (by decide) h
             | exact fun h => not_disjoint_fiber_preimages 3 (by decide) (by decide) h)

end SigmaEssential.Ulam
