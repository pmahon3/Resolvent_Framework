/-
Copyright (c) 2026. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Patrick S. Mahon
-/
import Mathlib.Order.Hom.Basic

/-!
# Order-theoretic kernel for conservative full-cycle assembly

The finite-support assembly argument uses a small order fact.  If an old
semilattice `A` embeds into a completed semilattice `C` and has a monotone
retraction whose embedded value lies below every completed element, then the
embedding preserves binary joins.  Thus a new completed upper bound cannot
interpolate below the old join.

The dual statement is included explicitly for binary meets.  In a complemented
setting it can instead be obtained from the join theorem by order duality and
complementation; keeping the order-dual theorem here avoids introducing a new
orthocomplement typeclass.

Both results are generic order theory: no finiteness, distributivity, or OML
axioms are used.
-/

namespace QuerySystem
namespace FullCycleAssemblyKernel

universe u v

/-- A monotone retraction that is deflationary after re-embedding forces an
order embedding to preserve binary suprema. -/
theorem map_sup_of_deflationary_retraction
    {A : Type u} {C : Type v} [SemilatticeSup A] [SemilatticeSup C]
    (i : A ↪o C) (r : C →o A)
    (hri : Function.LeftInverse r i)
    (hdefl : ∀ c, i (r c) ≤ c)
    (a b : A) :
    i (a ⊔ b) = i a ⊔ i b := by
  apply le_antisymm
  · have ha : a ≤ r (i a ⊔ i b) := by
      calc
        a = r (i a) := (hri a).symm
        _ ≤ r (i a ⊔ i b) := r.monotone le_sup_left
    have hb : b ≤ r (i a ⊔ i b) := by
      calc
        b = r (i b) := (hri b).symm
        _ ≤ r (i a ⊔ i b) := r.monotone le_sup_right
    exact (i.monotone (sup_le ha hb)).trans (hdefl (i a ⊔ i b))
  · exact sup_le (i.monotone le_sup_left) (i.monotone le_sup_right)

/-- Order-dual kernel: an inflationary monotone retraction forces preservation
of binary infima. -/
theorem map_inf_of_inflationary_retraction
    {A : Type u} {C : Type v} [SemilatticeInf A] [SemilatticeInf C]
    (i : A ↪o C) (r : C →o A)
    (hri : Function.LeftInverse r i)
    (hinfl : ∀ c, c ≤ i (r c))
    (a b : A) :
    i (a ⊓ b) = i a ⊓ i b := by
  apply le_antisymm
  · exact le_inf (i.monotone inf_le_left) (i.monotone inf_le_right)
  · have ha : r (i a ⊓ i b) ≤ a := by
      calc
        r (i a ⊓ i b) ≤ r (i a) := r.monotone inf_le_left
        _ = a := hri a
    have hb : r (i a ⊓ i b) ≤ b := by
      calc
        r (i a ⊓ i b) ≤ r (i b) := r.monotone inf_le_right
        _ = b := hri b
    exact (hinfl (i a ⊓ i b)).trans (i.monotone (le_inf ha hb))

/-- Complement conjugates a deflationary lower retraction into an inflationary
upper retraction, so the same embedded old lattice also preserves binary meets.

The complements are stated as explicit order-reversing involutions.  This keeps
the kernel independent of a particular orthocomplement/OML typeclass while
recording every complement property used by the argument. -/
theorem map_inf_of_complement_conjugate_deflationary_retraction
    {A : Type u} {C : Type v} [Lattice A] [Lattice C]
    (i : A ↪o C) (r : C →o A)
    (hri : Function.LeftInverse r i)
    (hdefl : ∀ c, i (r c) ≤ c)
    (complA : A → A) (complC : C → C)
    (complA_antitone : Antitone complA)
    (complC_antitone : Antitone complC)
    (complA_involutive : Function.Involutive complA)
    (complC_involutive : Function.Involutive complC)
    (i_compl : ∀ a, i (complA a) = complC (i a))
    (a b : A) :
    i (a ⊓ b) = i a ⊓ i b := by
  let upper : C →o A :=
    { toFun := fun c => complA (r (complC c))
      monotone' := fun _ _ h =>
        complA_antitone (r.monotone (complC_antitone h)) }
  have upper_leftInverse : Function.LeftInverse upper i := by
    intro x
    change complA (r (complC (i x))) = x
    rw [← i_compl, hri, complA_involutive]
  have upper_inflationary : ∀ c, c ≤ i (upper c) := by
    intro c
    have h := complC_antitone (hdefl (complC c))
    rw [complC_involutive] at h
    change c ≤ i (complA (r (complC c)))
    rw [i_compl]
    exact h
  exact map_inf_of_inflationary_retraction i upper upper_leftInverse
    upper_inflationary a b

#print axioms map_sup_of_deflationary_retraction
#print axioms map_inf_of_inflationary_retraction
#print axioms map_inf_of_complement_conjugate_deflationary_retraction

end FullCycleAssemblyKernel
end QuerySystem
