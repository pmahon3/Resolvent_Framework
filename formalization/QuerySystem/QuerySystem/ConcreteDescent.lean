/-
Copyright (c) 2026. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Patrick S. Mahon
-/
import QuerySystem.ConcreteMO2

/-!
# The descent witness, made concrete

`star_infinite` proves `(⋆)` at infinity on Navara's `L₂`, and pays eleven cited
axioms for the carrier. `ConsistencyModel.model_star` proves the same `(⋆)` with
no axioms at all, but on the abstract product `ℕ → MO₂`. What the axioms were
still buying is the word **concrete** in the statement of `thm:star-infinite`:
`L₂` is asserted to be a concrete, σ-orthocomplete, non-Boolean OML.

`ConcreteMO2` makes MO₂ itself concrete, and concreteness is inherited
fibrewise. So take countably many disjoint copies of the four-point space:

```
Ω = ℕ × (Bool × Bool)      L = {S | every fibre of S lies in mo2Class}
```

Every clause of `thm:star-infinite` then holds of `L`, proved:

* `descentClass` is a `DynkinSystem` — σ-complete, and concrete by construction,
  its order being inclusion and its orthocomplement set complement.
* `descentClass_not_interClosed` — non-Boolean.
* `aW_pairwise_ne`, `aW_ortho` — `{aWₙ}` is an infinite orthogonal family.
* `meet_pW_aW` — `pW ⊓ aWₙ = ∅`, the meet taken in the carrier.
* `not_pW_ortho` — yet `pW ⊄ aWₙᶜ`, so `pW` is orthogonal to no member.

Nothing here is assumed: no Navara axiom is imported, and the receipts at the
end are the standard three.
-/

namespace QuerySystem
namespace ConcreteDescent

open Set MeasurableSpace ConcreteMO2

/-! ## §1. The carrier and its fibres -/

/-- Countably many disjoint copies of the four-point space. -/
abbrev Blk := ℕ × P

/-- The fibre of `S` over block `n`, as a subset of the four-point space. -/
def fibre (S : Set Blk) (n : ℕ) : Set P := (fun x => (n, x)) ⁻¹' S

@[simp] lemma fibre_empty (n : ℕ) : fibre ∅ n = ∅ := rfl

@[simp] lemma fibre_compl (S : Set Blk) (n : ℕ) : fibre Sᶜ n = (fibre S n)ᶜ := rfl

lemma fibre_iUnion (f : ℕ → Set Blk) (n : ℕ) :
    fibre (⋃ i, f i) n = ⋃ i, fibre (f i) n := by
  ext x; simp [fibre]

lemma fibre_mono {S T : Set Blk} (h : S ⊆ T) (n : ℕ) : fibre S n ⊆ fibre T n :=
  fun _ hx => h hx

/-- A set is empty exactly when all its fibres are. -/
lemma eq_empty_of_fibres {S : Set Blk} (h : ∀ n, fibre S n = ∅) : S = ∅ := by
  ext ⟨n, x⟩
  constructor
  · intro hq
    have hx : x ∈ fibre S n := hq
    rw [h n] at hx
    exact hx.elim
  · intro hq; exact hq.elim

/-! ## §2. The σ-class

Concreteness is inherited fibrewise, and so is every Dynkin closure property:
complements and countable disjoint unions are computed blockwise, and
`mo2Class` is closed under both. -/

/-- Membership: every fibre lies in `mo2Class`. -/
def Blockwise (S : Set Blk) : Prop := ∀ n, mo2Class.Has (fibre S n)

/-- **The concrete descent carrier.** A σ-class of sets whose blocks are
copies of MO₂. -/
def descentClass : DynkinSystem Blk where
  Has := Blockwise
  has_empty := fun n => by rw [fibre_empty]; exact mo2Class.has_empty
  has_compl := fun {S} h n => by rw [fibre_compl]; exact mo2Class.has_compl (h n)
  has_iUnion_nat := by
    intro f hdisj hf n
    rw [fibre_iUnion]
    refine mo2Class.has_iUnion_nat ?_ (fun i => hf i n)
    intro i j hij
    exact Disjoint.preimage _ (hdisj hij)

/-! ## §3. The witness and the orthogonal family -/

/-- The witness: `b` in every block. -/
def pW : Set Blk := {q | q.2 ∈ B}

/-- The family: `a` in block `n`, empty elsewhere. -/
def aW (n : ℕ) : Set Blk := {q | q.1 = n ∧ q.2 ∈ A}

@[simp] lemma fibre_pW (n : ℕ) : fibre pW n = B := rfl

@[simp] lemma fibre_aW_self (n : ℕ) : fibre (aW n) n = A := by
  ext x; simp [fibre, aW]

lemma fibre_aW_ne {n m : ℕ} (h : m ≠ n) : fibre (aW n) m = ∅ := by
  ext x; simp [fibre, aW, h]

theorem pW_mem : descentClass.Has pW := fun n => by
  rw [fibre_pW]; exact rep_mem MO2.b

theorem aW_mem (n : ℕ) : descentClass.Has (aW n) := by
  intro m
  by_cases h : m = n
  · subst h; rw [fibre_aW_self]; exact rep_mem MO2.a
  · rw [fibre_aW_ne h]; exact mo2Class.has_empty

/-- The family is orthogonal: distinct members sit in disjoint blocks. -/
theorem aW_ortho {n m : ℕ} (h : n ≠ m) : aW n ⊆ (aW m)ᶜ := by
  rintro ⟨k, x⟩ ⟨rfl, -⟩ ⟨hk, -⟩
  exact h hk

/-- The family is infinite: its members are pairwise distinct. -/
theorem aW_pairwise_ne {n m : ℕ} (h : n ≠ m) : aW n ≠ aW m := by
  intro he
  have hmem : ((n, (true, true)) : Blk) ∈ aW n := ⟨rfl, rfl⟩
  rw [he] at hmem
  exact h hmem.1

/-! ## §4. `(⋆)`, concretely

Meet-zero against every member of the family, orthogonal to none of them. Both
halves reduce blockwise to `MO2.gap`, exactly as they do at Rung 2 — the block
index is doing all the work of carrying the gap to infinity. -/

/-- The meet of `pW` with any `aWₙ`, taken in the carrier, is `∅`. -/
theorem meet_pW_aW (n : ℕ) :
    IsGreatest {C | descentClass.Has C ∧ C ⊆ pW ∧ C ⊆ aW n} ∅ := by
  refine ⟨⟨descentClass.has_empty, empty_subset _, empty_subset _⟩, fun C hC => ?_⟩
  obtain ⟨hCmem, hCp, hCa⟩ := hC
  refine le_of_eq (eq_empty_of_fibres fun m => ?_)
  by_cases h : m = n
  · subst h
    -- the fibre sits inside `A ∩ B`, a single point, so it is empty
    refine fam_subset_singleton (hCmem m) ((true, true) : P) ?_
    intro x hx
    have hxA : x ∈ A := by
      have := fibre_mono hCa m hx
      rwa [fibre_aW_self] at this
    have hxB : x ∈ B := by
      have := fibre_mono hCp m hx
      rwa [fibre_pW] at this
    have : x ∈ A ∩ B := ⟨hxA, hxB⟩
    rwa [inter_AB] at this
  · have := fibre_mono hCa m
    rw [fibre_aW_ne h] at this
    exact subset_empty_iff.mp this

/-- Yet `pW` is orthogonal to no member: block `n` witnesses the overlap. -/
theorem not_pW_ortho (n : ℕ) : ¬ pW ⊆ (aW n)ᶜ := by
  intro h
  have hmem : ((n, (true, true)) : Blk) ∈ pW := rfl
  exact h hmem ⟨rfl, rfl⟩

/-- **`(⋆)` at infinity, on a concrete carrier, with no cited axiom.** -/
theorem star_concrete (n : ℕ) :
    IsGreatest {C | descentClass.Has C ∧ C ⊆ pW ∧ C ⊆ aW n} ∅ ∧
      ¬ pW ⊆ (aW n)ᶜ :=
  ⟨meet_pW_aW n, not_pW_ortho n⟩

/-! ## §5. The carrier is not Boolean -/

/-- `pW ∩ aWₙ` is a single point of block `n`, which the carrier does not
contain. -/
theorem not_interClosed : ¬ SigmaEssential.InterClosed descentClass := by
  intro h
  have hmem := h pW_mem (aW_mem 0)
  have hfib : fibre (pW ∩ aW 0) 0 = {((true, true) : P)} := by
    ext x
    simp only [fibre, Set.mem_preimage, Set.mem_inter_iff, Set.mem_singleton_iff]
    constructor
    · rintro ⟨hp, -, ha⟩
      have : x ∈ A ∩ B := ⟨ha, hp⟩
      rwa [inter_AB, Set.mem_singleton_iff] at this
    · rintro rfl
      exact ⟨rfl, rfl, rfl⟩
  have := hmem 0
  rw [hfib] at this
  exact singleton_not_mem this

/-! ## Receipts -/

#print axioms descentClass
#print axioms pW_mem
#print axioms aW_mem
#print axioms aW_ortho
#print axioms aW_pairwise_ne
#print axioms meet_pW_aW
#print axioms not_pW_ortho
#print axioms star_concrete
#print axioms not_interClosed

end ConcreteDescent
end QuerySystem
