/-
Copyright (c) 2026. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Patrick S. Mahon
-/
import QuerySystem.FiniteAtomFoldKernel

/-!
# Abstract kernel-closure calculus

These lemmas bank only the order theory used by the second-round assembly
argument.  Predicates stand for old elements lying below an external target.
No concrete-set representation, finiteness, or enumeration of atoms is
asserted here.
-/

namespace QuerySystem
namespace KernelClosureCalculus

universe u

/-- Greatest lower kernels intersect by lattice infimum, provided their
membership predicates are downward closed. -/
theorem greatest_intersection
    {A : Type u} [SemilatticeInf A]
    (p q : A → Prop) (gp gq : A)
    (p_down : ∀ {x y}, x ≤ y → p y → p x)
    (q_down : ∀ {x y}, x ≤ y → q y → q x)
    (hgp : p gp ∧ ∀ x, p x → x ≤ gp)
    (hgq : q gq ∧ ∀ x, q x → x ≤ gq) :
    (p (gp ⊓ gq) ∧ q (gp ⊓ gq)) ∧
      ∀ x, p x ∧ q x → x ≤ gp ⊓ gq := by
  constructor
  · exact ⟨p_down inf_le_left hgp.1, q_down inf_le_right hgq.1⟩
  · intro x hx
    exact le_inf (hgp.2 x hx.1) (hgq.2 x hx.2)

/-- An order-reversing involution carries a greatest member of `p` to a least
member of the complement-pulled predicate `fun x => p (compl x)`. -/
theorem least_complement_of_greatest
    {A : Type u} [Preorder A]
    (p : A → Prop) (g : A) (compl : A → A)
    (compl_antitone : Antitone compl)
    (compl_involutive : Function.Involutive compl)
    (hg : p g ∧ ∀ x, p x → x ≤ g) :
    p (compl (compl g)) ∧
      ∀ x, p (compl x) → compl g ≤ x := by
  constructor
  · simpa [compl_involutive g] using hg.1
  · intro x hx
    have h := compl_antitone (hg.2 (compl x) hx)
    simpa [compl_involutive x] using h

/-- Explicit complement duality: existence of a greatest `p`-member is
equivalent to existence of a least member of its complement pullback. -/
theorem exists_greatest_iff_exists_least_complement
    {A : Type u} [Preorder A]
    (p : A → Prop) (compl : A → A)
    (compl_antitone : Antitone compl)
    (compl_involutive : Function.Involutive compl) :
    (∃ g, p g ∧ ∀ x, p x → x ≤ g) ↔
      ∃ u, p (compl u) ∧ ∀ x, p (compl x) → u ≤ x := by
  constructor
  · rintro ⟨g, hg⟩
    exact ⟨compl g, least_complement_of_greatest p g compl
      compl_antitone compl_involutive hg⟩
  · rintro ⟨u, hu, hleast⟩
    refine ⟨compl u, hu, ?_⟩
    intro x hx
    have h := compl_antitone (hleast (compl x) (by simpa [compl_involutive x] using hx))
    simpa [compl_involutive u, compl_involutive x] using h

/-- Cover-fold criterion for an intersection kernel.  The finite list is an
explicit atomistic-cover witness: every element satisfying both predicates is
below its fold. -/
theorem intersection_cover_fold_good_iff_exists_greatest
    {A : Type u} [SemilatticeSup A]
    (p q : A → Prop) (init : A) (xs : List A)
    (p_down : ∀ {x y}, x ≤ y → p y → p x)
    (q_down : ∀ {x y}, x ≤ y → q y → q x)
    (hinit : p init ∧ q init)
    (hxs : ∀ x ∈ xs, p x ∧ q x)
    (hcover : ∀ x, p x ∧ q x → x ≤ xs.foldl (· ⊔ ·) init) :
    (p (xs.foldl (· ⊔ ·) init) ∧ q (xs.foldl (· ⊔ ·) init)) ↔
      ∃ g, (p g ∧ q g) ∧ ∀ x, p x ∧ q x → x ≤ g := by
  exact FiniteAtomFoldKernel.fold_good_iff_exists_greatest
    (fun x => p x ∧ q x) init xs
    (fun hxy hy => ⟨p_down hxy hy.1, q_down hxy hy.2⟩)
    hinit hxs hcover

/-- When the two component kernels already have greatest elements and the
listed cover generators cover their intersection, their fold is exactly the
infimum of those greatest elements. -/
theorem intersection_cover_fold_eq_inf
    {A : Type u} [Lattice A]
    (p q : A → Prop) (gp gq init : A) (xs : List A)
    (p_down : ∀ {x y}, x ≤ y → p y → p x)
    (q_down : ∀ {x y}, x ≤ y → q y → q x)
    (hgp : p gp ∧ ∀ x, p x → x ≤ gp)
    (hgq : q gq ∧ ∀ x, q x → x ≤ gq)
    (hinit : p init ∧ q init)
    (hxs : ∀ x ∈ xs, p x ∧ q x)
    (hcover : ∀ x, p x ∧ q x → x ≤ xs.foldl (· ⊔ ·) init) :
    xs.foldl (· ⊔ ·) init = gp ⊓ gq := by
  apply le_antisymm
  · apply le_inf
    · apply FiniteAtomFoldKernel.foldl_sup_le gp init xs
      · exact hgp.2 init hinit.1
      · intro x hx
        exact hgp.2 x (hxs x hx).1
    · apply FiniteAtomFoldKernel.foldl_sup_le gq init xs
      · exact hgq.2 init hinit.2
      · intro x hx
        exact hgq.2 x (hxs x hx).2
  · exact hcover (gp ⊓ gq)
      (greatest_intersection p q gp gq p_down q_down hgp hgq).1

/-- Generic bridge-union fold.  Eligibility of the base join is an explicit
hypothesis: it does not follow from eligibility of `kc` and `kd` under mere
downward closure.  In the concrete assembly this is supplied by the verified
disjoint-union step; classification and disjointness of bridge generators
remain external in `hbridges` and `hcover`. -/
theorem bridge_union_fold_good_iff_exists_greatest
    {A : Type u} [SemilatticeSup A]
    (goodUnion : A → Prop) (kc kd : A) (bridges : List A)
    (good_down : ∀ {x y}, x ≤ y → goodUnion y → goodUnion x)
    (hkc : goodUnion kc) (hkd : goodUnion kd)
    (hbase_join : goodUnion kc → goodUnion kd → goodUnion (kc ⊔ kd))
    (hbridges : ∀ b ∈ bridges, goodUnion b)
    (hcover : ∀ x, goodUnion x →
      x ≤ bridges.foldl (· ⊔ ·) (kc ⊔ kd)) :
    goodUnion (bridges.foldl (· ⊔ ·) (kc ⊔ kd)) ↔
      ∃ g, goodUnion g ∧ ∀ x, goodUnion x → x ≤ g := by
  have hbase : goodUnion (kc ⊔ kd) := hbase_join hkc hkd
  exact FiniteAtomFoldKernel.fold_good_iff_exists_greatest
    goodUnion (kc ⊔ kd) bridges good_down hbase hbridges hcover

/-- If a greatest bridge-union lower is supplied, the covered bridge fold is
exactly that element. -/
theorem bridge_union_fold_eq_greatest
    {A : Type u} [SemilatticeSup A]
    (goodUnion : A → Prop) (kc kd : A) (bridges : List A) (g : A)
    (hkc : goodUnion kc) (hkd : goodUnion kd)
    (hbase_join : goodUnion kc → goodUnion kd → goodUnion (kc ⊔ kd))
    (hbridges : ∀ b ∈ bridges, goodUnion b)
    (hgreat : goodUnion g ∧ ∀ x, goodUnion x → x ≤ g)
    (hcover : ∀ x, goodUnion x →
      x ≤ bridges.foldl (· ⊔ ·) (kc ⊔ kd)) :
    bridges.foldl (· ⊔ ·) (kc ⊔ kd) = g := by
  have hbase : goodUnion (kc ⊔ kd) := hbase_join hkc hkd
  apply le_antisymm
  · apply FiniteAtomFoldKernel.foldl_sup_le g (kc ⊔ kd) bridges
    · exact hgreat.2 (kc ⊔ kd) hbase
    · intro b hb
      exact hgreat.2 b (hbridges b hb)
  · exact hcover g hgreat.1

/-- Fixed-base obstruction: if the exhaustive eligible-generator fold escapes
the target predicate, then the eligible old elements have no greatest member.
The exhaustive-generator content is exactly the explicit `hcover` hypothesis. -/
theorem no_greatest_of_exhaustive_fold_not_good
    {A : Type u} [SemilatticeSup A]
    (good : A → Prop) (init : A) (xs : List A)
    (good_down : ∀ {x y}, x ≤ y → good y → good x)
    (hinit : good init) (hxs : ∀ x ∈ xs, good x)
    (hcover : ∀ x, good x → x ≤ xs.foldl (· ⊔ ·) init)
    (hescape : ¬ good (xs.foldl (· ⊔ ·) init)) :
    ¬ ∃ g, good g ∧ ∀ x, good x → x ≤ g := by
  intro hgreat
  exact hescape ((FiniteAtomFoldKernel.fold_good_iff_exists_greatest
    good init xs good_down hinit hxs hcover).2 hgreat)

/-- Predicate-extensional transfer of the fixed-base obstruction.  Two target
descriptions selecting exactly the same eligible old elements have the same
failure, without asserting equality of their external concrete targets. -/
theorem no_greatest_of_same_eligible_old_set
    {A : Type u} [SemilatticeSup A]
    (good₁ good₂ : A → Prop) (init : A) (xs : List A)
    (hext : ∀ x, good₁ x ↔ good₂ x)
    (good₁_down : ∀ {x y}, x ≤ y → good₁ y → good₁ x)
    (hinit : good₁ init) (hxs : ∀ x ∈ xs, good₁ x)
    (hcover : ∀ x, good₁ x → x ≤ xs.foldl (· ⊔ ·) init)
    (hescape : ¬ good₁ (xs.foldl (· ⊔ ·) init)) :
    ¬ ∃ g, good₂ g ∧ ∀ x, good₂ x → x ≤ g := by
  intro hgreat₂
  apply no_greatest_of_exhaustive_fold_not_good
    good₁ init xs good₁_down hinit hxs hcover hescape
  obtain ⟨g, hg, hgreat⟩ := hgreat₂
  exact ⟨g, (hext g).2 hg, fun x hx => hgreat x ((hext x).1 hx)⟩

#print axioms greatest_intersection
#print axioms least_complement_of_greatest
#print axioms exists_greatest_iff_exists_least_complement
#print axioms intersection_cover_fold_good_iff_exists_greatest
#print axioms intersection_cover_fold_eq_inf
#print axioms bridge_union_fold_good_iff_exists_greatest
#print axioms bridge_union_fold_eq_greatest
#print axioms no_greatest_of_exhaustive_fold_not_good
#print axioms no_greatest_of_same_eligible_old_set

end KernelClosureCalculus
end QuerySystem
