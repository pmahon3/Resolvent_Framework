/-
# The composition law for forward window types

Companion to `notes/open_questions/cyclic_marginal/theory_shape.md` ("the composition law") and
`glued_carriers_taxonomy.json` (`conj.composition_law`).

A *sum* `sum2 p u` (the classical Σ_p u_a) is the ultrafilter on pairs drawn "a from p, then b
from u a". The first window is *forward* if it is a sum and contains a set on which the second
coordinate determines the first up to finitely many choices (`FinBack`).

Main results:
* `glue_unique`: if the (x₀,x₁) window is a forward sum and the (x₁,x₂) window is any sum, then
  every ultrafilter on ℕ³ with these two projections is the natural three-step ultrafilter.
* `glue_proj02`: so its (x₀,x₂) projection is the composite (an iterated sum).
* `triangle_glues_iff`: a third window on (x₀,x₂) glues with the two iff it equals the composite.
  The twist of a triangle with two forward windows is exactly the disagreement of the closing
  window with the composite: the holonomy of composition.

Proof idea: the composite's sets are forced. A large set in the first window reaches each value of
x₁ from only finitely many x₀. So the requirement on x₂ at each x₁ is a finite intersection of
large sets, which is still large.
-/
import Mathlib.Order.Filter.Ultrafilter.Defs
import Mathlib.Order.Filter.Finite
import Mathlib.Data.Set.Finite.Basic

open Set Filter

namespace CompositionLaw

lemma mem_bindU {α β : Type*} {f : Ultrafilter α} {m : α → Ultrafilter β} {s : Set β} :
    s ∈ f.bind m ↔ {a | s ∈ m a} ∈ f := Filter.mem_bind'

/-- The sum Σ_p u_a on pairs: draw `a` from `p`, then `b` from `u a`. -/
noncomputable def sum2 (p : Ultrafilter ℕ) (u : ℕ → Ultrafilter ℕ) : Ultrafilter (ℕ × ℕ) :=
  p.bind fun a => (u a).map (Prod.mk a)

lemma mem_sum2 {p : Ultrafilter ℕ} {u : ℕ → Ultrafilter ℕ} {T : Set (ℕ × ℕ)} :
    T ∈ sum2 p u ↔ ∀ᶠ a in (p : Filter ℕ), ∀ᶠ b in (u a : Filter ℕ), (a, b) ∈ T := by
  unfold sum2; rw [mem_bindU]; rfl

/-- Finite-to-one back: some member reaches each value of the second coordinate from only
finitely many values of the first. -/
def FinBack (w : Ultrafilter (ℕ × ℕ)) : Prop :=
  ∃ F ∈ w, ∀ y, {a | (a, y) ∈ F}.Finite

/-- The natural three-step ultrafilter: `a` from `p`, then `b` from `u a`, then `c` from `v b`. -/
noncomputable def natural3 (p : Ultrafilter ℕ) (u v : ℕ → Ultrafilter ℕ) : Ultrafilter (ℕ × ℕ × ℕ) :=
  p.bind fun a => (u a).bind fun b => (v b).map fun c => (a, b, c)

lemma mem_natural3 {p : Ultrafilter ℕ} {u v : ℕ → Ultrafilter ℕ} {T : Set (ℕ × ℕ × ℕ)} :
    T ∈ natural3 p u v ↔ ∀ᶠ a in (p : Filter ℕ), ∀ᶠ b in (u a : Filter ℕ),
      ∀ᶠ c in (v b : Filter ℕ), (a, b, c) ∈ T := by
  unfold natural3; rw [mem_bindU]
  show {a | T ∈ (u a).bind _} ∈ p ↔ _
  simp only [mem_bindU]; rfl

/-- The composite window on (x₀, x₂): an iterated sum. -/
noncomputable def composite (p : Ultrafilter ℕ) (u v : ℕ → Ultrafilter ℕ) : Ultrafilter (ℕ × ℕ) :=
  p.bind fun a => ((u a).bind v).map (Prod.mk a)

lemma mem_composite {p : Ultrafilter ℕ} {u v : ℕ → Ultrafilter ℕ} {T : Set (ℕ × ℕ)} :
    T ∈ composite p u v ↔ ∀ᶠ a in (p : Filter ℕ), ∀ᶠ b in (u a : Filter ℕ),
      ∀ᶠ c in (v b : Filter ℕ), (a, c) ∈ T := by
  unfold composite; rw [mem_bindU]
  show {a | T ∈ ((u a).bind v).map (Prod.mk a)} ∈ p ↔ _
  simp only [Ultrafilter.mem_map, mem_bindU]; rfl

def pr01 (x : ℕ × ℕ × ℕ) : ℕ × ℕ := (x.1, x.2.1)
def pr12 (x : ℕ × ℕ × ℕ) : ℕ × ℕ := (x.2.1, x.2.2)
def pr02 (x : ℕ × ℕ × ℕ) : ℕ × ℕ := (x.1, x.2.2)

/-- **Forcing lemma (uniqueness).** If the (x₀,x₁) window is a forward sum and the (x₁,x₂) window
is a sum (over any marginal `r`), every ultrafilter on ℕ³ with these projections is `natural3`. -/
theorem glue_unique {p r : Ultrafilter ℕ} {u v : ℕ → Ultrafilter ℕ} (hF : FinBack (sum2 p u))
    (U : Ultrafilter (ℕ × ℕ × ℕ)) (h01 : U.map pr01 = sum2 p u) (h12 : U.map pr12 = sum2 r v) :
    U = natural3 p u v := by
  apply Ultrafilter.eq_of_le
  intro T hT
  rw [Ultrafilter.mem_coe, mem_natural3] at hT
  obtain ⟨F, hFm, hfin⟩ := hF
  rw [mem_sum2] at hFm
  -- X: pairs (a,b) in F from which the requirement on c is large
  set X : Set (ℕ × ℕ) := {q | (∀ᶠ c in (v q.2 : Filter ℕ), (q.1, q.2, c) ∈ T) ∧ q ∈ F} with hX
  have hXm : X ∈ sum2 p u := by
    rw [mem_sum2]
    exact (hT.and hFm).mono fun a ⟨h1, h2⟩ => (h1.and h2).mono fun b ⟨h3, h4⟩ => ⟨h3, h4⟩
  -- Y: pairs (y,c) meeting the finitely many requirements at y
  set Y : Set (ℕ × ℕ) := {q | ∀ a, (a, q.1) ∈ X → (a, q.1, q.2) ∈ T} with hY
  have hYm : Y ∈ sum2 r v := by
    rw [mem_sum2]
    refine Filter.Eventually.of_forall fun y => ?_
    have hI : {a | (a, y) ∈ X}.Finite := (hfin y).subset fun a ha => ha.2
    have := (hI.eventually_all (l := (v y : Filter ℕ)) (p := fun a c => (a, y, c) ∈ T)).2
      fun a ha => ha.1
    exact this.mono fun c hc a ha => hc a ha
  have hX' : pr01 ⁻¹' X ∈ U := by rw [← Ultrafilter.mem_map, h01]; exact hXm
  have hY' : pr12 ⁻¹' Y ∈ U := by rw [← Ultrafilter.mem_map, h12]; exact hYm
  rw [Ultrafilter.mem_coe]
  refine Filter.mem_of_superset (Filter.inter_mem hX' hY') ?_
  rintro ⟨a, b, c⟩ ⟨hx, hy⟩
  exact hy a hx

theorem natural3_proj01 (p : Ultrafilter ℕ) (u v : ℕ → Ultrafilter ℕ) :
    (natural3 p u v).map pr01 = sum2 p u := by
  ext T
  rw [Ultrafilter.mem_map, mem_natural3, mem_sum2]
  simp only [pr01, mem_preimage, Filter.eventually_const]

theorem natural3_proj12 (p : Ultrafilter ℕ) (u v : ℕ → Ultrafilter ℕ) :
    (natural3 p u v).map pr12 = sum2 (p.bind u) v := by
  ext T
  rw [Ultrafilter.mem_map, mem_natural3, mem_sum2]
  simp only [pr12, mem_preimage]
  show _ ↔ {b | {c | (b, c) ∈ T} ∈ v b} ∈ p.bind u
  rw [mem_bindU]; rfl

theorem natural3_proj02 (p : Ultrafilter ℕ) (u v : ℕ → Ultrafilter ℕ) :
    (natural3 p u v).map pr02 = composite p u v := by
  ext T
  rw [Ultrafilter.mem_map, mem_natural3, mem_composite]
  simp only [pr02, mem_preimage]

/-- **The (x₀,x₂) projection of any gluing is the composite.** -/
theorem glue_proj02 {p r : Ultrafilter ℕ} {u v : ℕ → Ultrafilter ℕ} (hF : FinBack (sum2 p u))
    (U : Ultrafilter (ℕ × ℕ × ℕ)) (h01 : U.map pr01 = sum2 p u) (h12 : U.map pr12 = sum2 r v) :
    U.map pr02 = composite p u v := by
  rw [glue_unique hF U h01 h12, natural3_proj02]

/-- **Triangle theorem (holonomy).** With a forward (x₀,x₁) window and a summed (x₁,x₂) window over
the consistent marginal, a third window on (x₀,x₂) glues iff it equals the composite. -/
theorem triangle_glues_iff {p : Ultrafilter ℕ} {u v : ℕ → Ultrafilter ℕ} (hF : FinBack (sum2 p u))
    (w : Ultrafilter (ℕ × ℕ)) :
    (∃ U : Ultrafilter (ℕ × ℕ × ℕ), U.map pr01 = sum2 p u ∧ U.map pr12 = sum2 (p.bind u) v ∧
      U.map pr02 = w) ↔ w = composite p u v := by
  constructor
  · rintro ⟨U, h01, h12, h02⟩
    rw [← h02]; exact glue_proj02 hF U h01 h12
  · rintro rfl
    exact ⟨natural3 p u v, natural3_proj01 p u v, natural3_proj12 p u v, natural3_proj02 p u v⟩

end CompositionLaw

#print axioms CompositionLaw.glue_unique
#print axioms CompositionLaw.glue_proj02
#print axioms CompositionLaw.triangle_glues_iff
