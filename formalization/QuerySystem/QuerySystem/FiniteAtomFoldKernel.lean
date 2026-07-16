/-
Copyright (c) 2026. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Patrick S. Mahon
-/
import Mathlib.Order.Lattice

/-!
# Finite atom-fold kernel

This file isolates the order-theoretic fold used by the adjacent full-cycle
streaming scan.  The predicate `good` says that an old element lies below the
external mixed target.  It need not be closed under old joins.

No orthomodular-lattice API is needed here.  Atomisticity enters the executable
argument only through the displayed `hcover` hypothesis: every good old element
is below the fold of the eligible old atoms (and the retained initial event).
-/

namespace QuerySystem
namespace FiniteAtomFoldKernel

universe u

/-- If the initial value and every entry of a finite join fold lie below `g`,
then the result of the fold lies below `g`. -/
theorem foldl_sup_le
    {A : Type u} [SemilatticeSup A]
    (g init : A) (xs : List A)
    (hinit : init ≤ g) (hxs : ∀ x ∈ xs, x ≤ g) :
    xs.foldl (· ⊔ ·) init ≤ g := by
  induction xs generalizing init with
  | nil => exact hinit
  | cons a xs ih =>
      apply ih (init := init ⊔ a)
      · exact sup_le hinit (hxs a (by simp))
      · intro x hx
        exact hxs x (by simp [hx])

/-- Under the atomistic-cover hypothesis `hcover`, the eligible-atom fold is
good exactly when the good old elements possess a greatest member.

In the scan, `xs` is the list of eligible old atoms and `init` is the retained
old event.  Downward closure is inherited from the external order. -/
theorem fold_good_iff_exists_greatest
    {A : Type u} [SemilatticeSup A]
    (good : A → Prop) (init : A) (xs : List A)
    (hdown : ∀ {x y}, x ≤ y → good y → good x)
    (hinit : good init) (hxs : ∀ x ∈ xs, good x)
    (hcover : ∀ x, good x → x ≤ xs.foldl (· ⊔ ·) init) :
    good (xs.foldl (· ⊔ ·) init) ↔
      ∃ g, good g ∧ ∀ x, good x → x ≤ g := by
  constructor
  · intro hfold
    exact ⟨_, hfold, fun x hx => hcover x hx⟩
  · rintro ⟨g, hg, hgreat⟩
    apply hdown (y := g)
    · apply foldl_sup_le g init xs
      · exact hgreat init hinit
      · intro x hx
        exact hgreat x (hxs x hx)
    · exact hg

/-- If a finite eligible-atom fold starts good and ends outside the target,
there is a strict atomic extension whose two inputs are good but whose old join
is not.  The prefix `ys` records the exact provenance of that accumulator. -/
theorem exists_strict_escaping_extension
    {A : Type u} [SemilatticeSup A]
    (good : A → Prop) (init : A) (xs : List A)
    (hinit : good init) (hxs : ∀ x ∈ xs, good x)
    (hfinal : ¬ good (xs.foldl (· ⊔ ·) init)) :
    ∃ ys a zs,
      xs = ys ++ a :: zs ∧
      good (ys.foldl (· ⊔ ·) init) ∧
      good a ∧
      ¬ a ≤ ys.foldl (· ⊔ ·) init ∧
      ¬ good ((ys.foldl (· ⊔ ·) init) ⊔ a) := by
  induction xs generalizing init with
  | nil => exact (hfinal hinit).elim
  | cons a xs ih =>
      have ha : good a := hxs a (by simp)
      by_cases hstep : good (init ⊔ a)
      · have htail : ∀ x ∈ xs, good x := by
          intro x hx
          exact hxs x (by simp [hx])
        obtain ⟨ys, b, zs, hdecomp, hpref, hb, hstrict, hescape⟩ :=
          ih (init := init ⊔ a) hstep htail hfinal
        refine ⟨a :: ys, b, zs, ?_, ?_, hb, ?_, ?_⟩
        · simp [hdecomp]
        · simpa using hpref
        · simpa using hstrict
        · simpa using hescape
      · refine ⟨[], a, xs, rfl, hinit, ha, ?_, hstep⟩
        intro hale
        apply hstep
        have hale' : a ≤ init := by simpa using hale
        rw [sup_eq_left.mpr hale']
        exact hinit

#print axioms foldl_sup_le
#print axioms fold_good_iff_exists_greatest
#print axioms exists_strict_escaping_extension

end FiniteAtomFoldKernel
end QuerySystem
