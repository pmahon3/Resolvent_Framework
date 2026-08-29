/-
Copyright (c) 2026. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Patrick S. Mahon
-/
import QuerySystem.OrthomodularMO2
import QuerySystem.SigmaEssentialLocalization
import QuerySystem.ConcreteOMLBlocks

/-!
# MO₂ on four points: the smallest concrete non-Boolean σ-class

`OrthomodularMO2` gives MO₂ as an abstract lattice; the σ-essential lane works
with concrete σ-classes, i.e. `DynkinSystem`s of sets. This file realizes MO₂ as
one, on four points, which puts the two developments in the same category
without adding any new notion to either.

The carrier is the **horizontal sum of two four-element Boolean blocks** — the
description `OrthomodularMO2` already gives of MO₂ — sharing only `∅` and
`univ`:

```
Ω = Bool × Bool     A = {p | p.1}     B = {p | p.2}
L = {∅, Aᶜ, A, univ} ∪ {∅, Bᶜ, B, univ}
```

## What it exhibits

* `mo2Class` is a `DynkinSystem`: the only disjoint pairs it contains are the
  complementary ones, so every countable disjoint union lands back inside.
* `mo2Class_not_interClosed` — it is **not** intersection-closed: `A ∩ B` is a
  single point, which is not in `L`. Four points suffice for the failure that
  `carrier_not_interClosed` establishes for `L₁` over `ω₁`.
* `mo2Class_meet_eq_bot` — the greatest carrier element below both `A` and `B`
  is `∅`, while `A ∩ B ≠ ∅`. Lattice meet and set intersection come apart here,
  which is the concrete content of `MO2.gap`.

So the pivot `TwoValuedState.val_inter` turns on is visible at four points: its
hypothesis `InterClosed` fails, and it fails because the meet is not the
intersection.
-/

namespace QuerySystem
namespace ConcreteMO2

open Set MeasurableSpace

/-- Four points. -/
abbrev P := Bool × Bool

/-- The first block's generator. -/
def A : Set P := {p | p.1 = true}

/-- The second block's generator. -/
def B : Set P := {p | p.2 = true}

instance : DecidablePred (· ∈ A) := fun p => inferInstanceAs (Decidable (p.1 = true))
instance : DecidablePred (· ∈ B) := fun p => inferInstanceAs (Decidable (p.2 = true))

/-- Membership in the horizontal sum: one of the two Boolean blocks. -/
def Fam (S : Set P) : Prop :=
  S = ∅ ∨ S = univ ∨ S = A ∨ S = Aᶜ ∨ S = B ∨ S = Bᶜ

lemma fam_empty : Fam ∅ := Or.inl rfl
lemma fam_univ : Fam univ := Or.inr (Or.inl rfl)

lemma fam_compl {S : Set P} (h : Fam S) : Fam Sᶜ := by
  rcases h with rfl | rfl | rfl | rfl | rfl | rfl
  · exact Or.inr (Or.inl (by simp))
  · exact Or.inl (by simp)
  · exact Or.inr (Or.inr (Or.inr (Or.inl rfl)))
  · exact Or.inr (Or.inr (Or.inl (by simp)))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr rfl))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inl (by simp)))))

/-! ### The four cross-pairs are never disjoint

This is the whole reason the horizontal sum is not a σ-algebra: a member of one
block and a member of the other always share a point, so they can never appear
together in a disjoint family, and the union case below never has to mix them. -/

lemma not_disjoint_AB : ¬ Disjoint A B := by
  rw [Set.not_disjoint_iff]
  exact ⟨(true, true), rfl, rfl⟩

lemma not_disjoint_ABc : ¬ Disjoint A Bᶜ := by
  rw [Set.not_disjoint_iff]
  exact ⟨(true, false), rfl, by simp [B]⟩

lemma not_disjoint_AcB : ¬ Disjoint Aᶜ B := by
  rw [Set.not_disjoint_iff]
  exact ⟨(false, true), by simp [A], rfl⟩

lemma not_disjoint_AcBc : ¬ Disjoint Aᶜ Bᶜ := by
  rw [Set.not_disjoint_iff]
  exact ⟨(false, false), by simp [A], by simp [B]⟩

lemma A_ne_empty : A ≠ ∅ := by
  intro h
  have : ((true, true) : P) ∈ A := rfl
  rw [h] at this; exact this

lemma B_ne_empty : B ≠ ∅ := by
  intro h
  have : ((true, true) : P) ∈ B := rfl
  rw [h] at this; exact this

/-! ### Two nonempty members that are disjoint are complementary

The horizontal sum has no disjoint pairs beyond the complementary ones, which is
what makes the countable-union case finite. -/

lemma disjoint_fam_compl {S T : Set P} (hS : Fam S) (hT : Fam T)
    (hd : Disjoint S T) (hSne : S ≠ ∅) (hTne : T ≠ ∅) : T = Sᶜ := by
  rw [Set.disjoint_left] at hd
  rcases hS with rfl | rfl | rfl | rfl | rfl | rfl <;>
    rcases hT with rfl | rfl | rfl | rfl | rfl | rfl <;>
      first
        | exact absurd rfl hSne
        | exact absurd rfl hTne
        | exact absurd hd (by decide)
        | (rw [Set.ext_iff]; decide)

/-- **MO₂ as a concrete σ-class.** The horizontal sum of the two Boolean blocks
is a Dynkin system on four points. -/
def mo2Class : DynkinSystem P where
  Has := Fam
  has_empty := fam_empty
  has_compl := fun h => fam_compl h
  has_iUnion_nat := by
    intro f hdisj hf
    classical
    by_cases huniv : ∃ i, f i = univ
    · -- a `univ` member forces every other to be empty
      obtain ⟨i, hi⟩ := huniv
      have : (⋃ j, f j) = univ := by
        refine Set.eq_univ_of_univ_subset ?_
        rw [← hi]; exact Set.subset_iUnion f i
      rw [this]; exact fam_univ
    · by_cases hall : ∀ i, f i = ∅
      · have : (⋃ j, f j) = ∅ := by
          simp only [Set.iUnion_eq_empty]; exact hall
        rw [this]; exact fam_empty
      · push_neg at hall
        obtain ⟨i₀, hi₀⟩ := hall
        by_cases hcomp : ∃ j, j ≠ i₀ ∧ f j = (f i₀)ᶜ
        · -- the block is completed: the union is everything
          obtain ⟨j, _, hj⟩ := hcomp
          have : (⋃ k, f k) = univ := by
            refine Set.eq_univ_of_forall (fun x => ?_)
            by_cases hx : x ∈ f i₀
            · exact Set.mem_iUnion.mpr ⟨i₀, hx⟩
            · exact Set.mem_iUnion.mpr ⟨j, by rw [hj]; exact hx⟩
          rw [this]; exact fam_univ
        · -- every other member is empty, so the union is `f i₀`
          push_neg at hcomp
          have hrest : ∀ j, j ≠ i₀ → f j = ∅ := by
            intro j hj
            by_contra hne
            exact hcomp j hj (disjoint_fam_compl (hf i₀) (hf j) (hdisj (Ne.symm hj)) (Set.nonempty_iff_ne_empty.mp hi₀) hne)
          have : (⋃ k, f k) = f i₀ := by
            refine Set.Subset.antisymm ?_ (Set.subset_iUnion f i₀)
            intro x hx
            obtain ⟨k, hk⟩ := Set.mem_iUnion.mp hx
            by_cases hki : k = i₀
            · rwa [hki] at hk
            · rw [hrest k hki] at hk; exact hk.elim
          rw [this]; exact hf i₀


/-! ## §2. The correspondence with `MO₂`

`rep` is an order isomorphism from the abstract lattice `MO2` onto the carrier,
carrying `ᗮ` to set complement. It is what makes "this σ-class *is* MO₂" a
theorem rather than a reading of the picture. -/

/-- The six carrier elements, indexed by `MO₂`. -/
def rep : MO2 → Set P
  | .bot => ∅
  | .top => univ
  | .a   => A
  | .a'  => Aᶜ
  | .b   => B
  | .b'  => Bᶜ

theorem rep_mem (x : MO2) : mo2Class.Has (rep x) := by
  cases x
  exacts [fam_empty, Or.inr (Or.inr (Or.inl rfl)),
          Or.inr (Or.inr (Or.inr (Or.inl rfl))),
          Or.inr (Or.inr (Or.inr (Or.inr (Or.inl rfl)))),
          Or.inr (Or.inr (Or.inr (Or.inr (Or.inr rfl)))), fam_univ]

/-- `rep` hits every carrier element: the carrier has exactly these six sets. -/
theorem rep_surjective {S : Set P} (hS : mo2Class.Has S) : ∃ x, rep x = S := by
  rcases hS with rfl | rfl | rfl | rfl | rfl | rfl
  exacts [⟨.bot, rfl⟩, ⟨.top, rfl⟩, ⟨.a, rfl⟩, ⟨.a', rfl⟩, ⟨.b, rfl⟩, ⟨.b', rfl⟩]

/-- `rep` reflects and preserves the order: `MO₂`'s order is set inclusion. -/
theorem rep_le_iff (x y : MO2) : x ≤ y ↔ rep x ⊆ rep y := by
  cases x <;> cases y <;>
    simp only [rep, Set.subset_def, Set.mem_empty_iff_false, Set.mem_univ,
      Set.mem_compl_iff, A, B, Set.mem_setOf_eq, LE.le, MO2.leB] <;> decide

/-- `rep` carries the orthocomplement to set complement. -/
theorem rep_ortho (x : MO2) : rep xᗮ = (rep x)ᶜ := by
  cases x
  · show (univ : Set P) = (∅ : Set P)ᶜ; simp
  · show (Aᶜ : Set P) = Aᶜ; rfl
  · show (A : Set P) = Aᶜᶜ; simp
  · show (Bᶜ : Set P) = Bᶜ; rfl
  · show (B : Set P) = Bᶜᶜ; simp
  · show (∅ : Set P) = (univ : Set P)ᶜ; simp

/-- `rep` is injective, so the carrier has exactly six elements. -/
theorem rep_injective : Function.Injective rep := by
  intro x y h
  exact le_antisymm ((rep_le_iff x y).mpr h.subset) ((rep_le_iff y x).mpr h.symm.subset)

/-! ## §3. What fails: intersection-closure, and the poor pair

`A ∩ B` is a single point. It is not in the carrier, so the carrier is not
intersection-closed; and no *nonempty* carrier member sits inside it, so the
lattice meet `A ⊓ B` is `∅` while the intersection is inhabited. That second
statement is `Blocks.PoorPair`, and this is its first model. -/

/-- Every carrier member contained in a single point is empty. -/
theorem fam_subset_singleton {C : Set P} (hC : mo2Class.Has C) (p : P)
    (h : C ⊆ {p}) : C = ∅ := by
  revert h
  rcases hC with rfl | rfl | rfl | rfl | rfl | rfl <;>
    (rw [Set.subset_def, Set.ext_iff]; revert p;
     simp only [Set.mem_empty_iff_false, Set.mem_univ, Set.mem_compl_iff,
       Set.mem_singleton_iff, A, B, Set.mem_setOf_eq]; decide)

theorem inter_AB : A ∩ B = {((true, true) : P)} := by
  rw [Set.ext_iff]
  simp only [Set.mem_inter_iff, Set.mem_singleton_iff, A, B, Set.mem_setOf_eq]
  decide

/-- **The poor pair.** `A ∩ B` is inhabited, yet the only carrier member inside
it is `∅`: the lattice meet is `⊥` while the set intersection is not. -/
theorem mo2Class_poorPair : SigmaEssential.Blocks.PoorPair mo2Class A B := by
  refine ⟨⟨(true, true), rfl, rfl⟩, fun E hE hsub => ?_⟩
  exact fam_subset_singleton hE _ (inter_AB ▸ hsub)

/-- The single point of the overlap is not itself in the carrier — the meet has
nowhere to land. -/
theorem singleton_not_mem : ¬ mo2Class.Has {((true, true) : P)} :=
  mo2Class_poorPair.singleton_notMem ⟨rfl, rfl⟩

/-- `A` and `B` are incompatible in the concrete sense of `Blocks.Compat`. -/
theorem not_compat_AB : ¬ SigmaEssential.Blocks.Compat mo2Class A B :=
  mo2Class_poorPair.not_compat

/-- **The carrier is not intersection-closed.** Four points suffice for the
failure `carrier_not_interClosed` establishes over `ω₁`. -/
theorem mo2Class_not_interClosed : ¬ SigmaEssential.InterClosed mo2Class :=
  fun h => not_compat_AB (h (rep_mem .a) (rep_mem .b))

/-- `A` and `B` lie in no common maximal block: the horizontal sum really is
split into two blocks. -/
theorem not_mem_common_block {M : Set (Set P)}
    (hM : SigmaEssential.Blocks.IsMaxBlock mo2Class M)
    (hA : A ∈ M) (hB : B ∈ M) : False :=
  mo2Class_poorPair.not_mem_common_block hM hA hB


/-! ## §4. Meets exist — the gap is not caused by their absence

Every pair of carrier elements *does* have a greatest carrier element below both
(`Blocks.MeetsExist`), so this model satisfies the latticehood hypothesis that
gates §7–§8 of `ConcreteOMLBlocks`. The poor pair above therefore is not an
artifact of missing meets: `A ⊓ B` exists and equals `∅`, while `A ∩ B` does
not. Meet and intersection simply differ. -/

/-- Every nonempty carrier element has at least two points, so a carrier element
inside a subsingleton is empty. -/
theorem fam_subset_subsingleton {C U : Set P} (hC : mo2Class.Has C)
    (hU : U.Subsingleton) (h : C ⊆ U) : C = ∅ := by
  rcases hC with rfl | rfl | rfl | rfl | rfl | rfl
  · rfl
  · exact absurd (hU (h (mem_univ ((true, true) : P))) (h (mem_univ ((false, false) : P))))
      (by decide)
  · exact absurd (hU (h (by simp [A] : ((true, true) : P) ∈ A))
      (h (by simp [A] : ((true, false) : P) ∈ A))) (by decide)
  · exact absurd (hU (h (by simp [A] : ((false, true) : P) ∈ Aᶜ))
      (h (by simp [A] : ((false, false) : P) ∈ Aᶜ))) (by decide)
  · exact absurd (hU (h (by simp [B] : ((true, true) : P) ∈ B))
      (h (by simp [B] : ((false, true) : P) ∈ B))) (by decide)
  · exact absurd (hU (h (by simp [B] : ((true, false) : P) ∈ Bᶜ))
      (h (by simp [B] : ((false, false) : P) ∈ Bᶜ))) (by decide)

/-- **Meets exist.** Comparable pairs meet at the smaller one; every other pair
meets at `∅`, because what their intersection contains is at most one point and
no nonempty carrier element is that small. -/
theorem mo2Class_meetsExist : SigmaEssential.Blocks.MeetsExist mo2Class := by
  intro S T hS hT
  by_cases hst : S ⊆ T
  · exact ⟨S, ⟨hS, subset_rfl, hst⟩, fun C hC => hC.2.1⟩
  by_cases hts : T ⊆ S
  · exact ⟨T, ⟨hT, hts, subset_rfl⟩, fun C hC => hC.2.2⟩
  refine ⟨∅, ⟨mo2Class.has_empty, empty_subset _, empty_subset _⟩, fun C hC => ?_⟩
  refine le_of_eq (fam_subset_subsingleton hC.1 ?_ (subset_inter hC.2.1 hC.2.2))
  revert hst hts
  rcases hS with rfl | rfl | rfl | rfl | rfl | rfl <;>
    rcases hT with rfl | rfl | rfl | rfl | rfl | rfl <;>
      (simp only [Set.Subsingleton, Set.subset_def, Set.mem_inter_iff,
        Set.mem_empty_iff_false, Set.mem_univ, Set.mem_compl_iff, A, B,
        Set.mem_setOf_eq]; decide)

/-- The meet of `A` and `B` is `∅`, but their intersection is not: at four
points, lattice meet and set intersection come apart. This is `MO2.gap` made
concrete. -/
theorem meet_AB_ne_inter :
    IsGreatest {C | mo2Class.Has C ∧ C ⊆ A ∧ C ⊆ B} ∅ ∧ (A ∩ B).Nonempty := by
  refine ⟨⟨⟨mo2Class.has_empty, empty_subset _, empty_subset _⟩, fun C hC => ?_⟩,
    mo2Class_poorPair.1⟩
  exact le_of_eq (mo2Class_poorPair.2 C hC.1 (subset_inter hC.2.1 hC.2.2))


/-! ## Receipts -/

#print axioms mo2Class
#print axioms rep_le_iff
#print axioms rep_ortho
#print axioms rep_injective
#print axioms mo2Class_poorPair
#print axioms mo2Class_not_interClosed
#print axioms mo2Class_meetsExist
#print axioms meet_AB_ne_inter

end ConcreteMO2
end QuerySystem
