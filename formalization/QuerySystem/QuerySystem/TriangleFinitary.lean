/-
# The triangle carrier is finitary (`D₃ = D_fin`): machine-checked, no `sorry`

Hand proof: `notes/open_questions/views_across_records/TRIANGLE_D3_DFIN_REVERSAL_CHECK.md`
(original: `TRIANGLE_5DE_CHECK.md` C6). Section numbers below are the hand proof's steps.

STATUS: no `sorry` in this file; axiom receipts at the end (`propext`, `Classical.choice`,
`Quot.sound` only).
* (0) targets: `dfin_mem`, `mem_dfin` (`D₃ = D_fin`: `mem_iff_dfin`), `state_ext`.
* Step 1 (no infinite K-clique): `clique_inP`, `no_infinite_clique`.
* Step 2 (finite labelled cover): `finite_cover`.
* Step 3 (columns and residue, with Fix 1): `residue`, `normal_form`. NOT used by `mem_dfin`.
* Step 3' (not in the hand proof): `collapse0`, `dfin_of_box_cover`. A labelled cover is collapsed
  onto class representatives at the cost of four window events per coordinate; this replaces the
  column analysis of Step 3 in the proof of `mem_dfin`.
* Step 4 (finite grids): `dfin_of_detN`, `dfin_of_box_finDet`; by-product
  `box_iff_dfin_of_finDet`. Departure from the hand proof: the all-K case does not build the total
  order `E_<` (Fix 2) and does not use adjacent swaps (Fix 3). For a fixed base class `b` it takes
  the class `a` with minimal `U`-set (`allK_pair`) and merges `a` into `b` directly (`stepK`).
* Step 5 (assembly): `mem_dfin = dfin_of_box_cover ∘ (box_of_mem, finite_cover)`.

Alphabet: ℕ on each coordinate (`Ω = Fin 3 → ℕ`), as in `TriangleCyclic.lean`.
-/
import QuerySystem.TriangleCyclic
import Mathlib.Order.OrderIsoNat
import Mathlib.Order.Zorn
import Mathlib.Data.Set.Pairwise.Lattice
import Mathlib.Data.Finite.Sum
import Mathlib.Data.Finite.Prod
import Mathlib.Data.Set.Finite.Basic
import Mathlib.Order.Preorder.Finite

open Set MeasurableSpace Function

namespace TriangleCyclic

/-! ## (0) Targets -/

/-- Finitary closure of the window events: complements and binary disjoint unions.
(`∅ ∈ gens`, so no separate clause for `∅` is needed.) -/
inductive Dfin : Set Ω → Prop
  | basic {E : Set Ω} : E ∈ gens → Dfin E
  | compl {E : Set Ω} : Dfin E → Dfin Eᶜ
  | union {E F : Set Ω} : Dfin E → Dfin F → Disjoint E F → Dfin (E ∪ F)

/-- Easy direction: finitary sets are carrier sets. -/
theorem dfin_mem {E : Set Ω} (h : Dfin E) : D₃.Has E := by
  induction h with
  | basic h => exact DynkinSystem.GenerateHas.basic _ h
  | compl _ ih => exact D₃.has_compl ih
  | union _ _ hd ih₁ ih₂ => exact D₃.has_union ih₁ ih₂ hd

/-- TARGET 1 (the theorem `D₃ = D_fin`). Proved at the end as `mem_dfin`. -/
def MemDfinTarget : Prop := ∀ E : Set Ω, D₃.Has E → Dfin E

/-- TARGET 2 (corollary). Two functions on sets that are complement-normalised and additive on
disjoint unions of carrier sets, and agree on the window events, agree on all of `D₃`.
Stated for ℤ-valued functions; {0,1}-valuedness is not needed. Proved at the end as `state_ext`,
from `mem_dfin`. -/
def StateExtTarget : Prop :=
  ∀ s t : Set Ω → ℤ,
    (∀ E, D₃.Has E → s Eᶜ = 1 - s E) →
    (∀ A B, D₃.Has A → D₃.Has B → Disjoint A B → s (A ∪ B) = s A + s B) →
    (∀ E, D₃.Has E → t Eᶜ = 1 - t E) →
    (∀ A B, D₃.Has A → D₃.Has B → Disjoint A B → t (A ∪ B) = t A + t B) →
    (∀ E ∈ gens, s E = t E) → ∀ E, D₃.Has E → s E = t E

/-! ## Pullbacks: coordinatewise maps and the rotation -/

/-- A set whose membership depends only on the coordinates in a window is a window event. -/
lemma gens_of_local {w : Set (Fin 3)} (hw : w ∈ W₃) {E : Set Ω}
    (h : ∀ y z : Ω, (∀ k ∈ w, y k = z k) → y ∈ E → z ∈ E) : E ∈ gens := by
  refine ⟨w, hw, (fun (x : Ω) (k : w) => x k) '' E, (Set.to_countable _).measurableSet, ?_⟩
  ext z
  constructor
  · rintro ⟨y, hy, hyz⟩
    exact h y z (fun k hk => congrFun hyz ⟨k, hk⟩) hy
  · intro hz
    exact ⟨z, hz, rfl⟩

lemma gens01 {E : Set Ω} (h : ∀ x y : Ω, x 0 = y 0 → x 1 = y 1 → x ∈ E → y ∈ E) : E ∈ gens :=
  gens_of_local (w := {0, 1}) (by simp [W₃]) fun y z hk hy =>
    h y z (hk 0 (by simp)) (hk 1 (by simp)) hy

lemma gens12 {E : Set Ω} (h : ∀ x y : Ω, x 1 = y 1 → x 2 = y 2 → x ∈ E → y ∈ E) : E ∈ gens :=
  gens_of_local (w := {1, 2}) (by simp [W₃]) fun y z hk hy =>
    h y z (hk 1 (by simp)) (hk 2 (by simp)) hy

lemma gens20 {E : Set Ω} (h : ∀ x y : Ω, x 2 = y 2 → x 0 = y 0 → x ∈ E → y ∈ E) : E ∈ gens :=
  gens_of_local (w := {2, 0}) (by simp [W₃]) fun y z hk hy =>
    h y z (hk 2 (by simp)) (hk 0 (by simp)) hy

/-- The coordinatewise map `G` of a family `g : Fin 3 → ℕ → ℕ`. -/
def cw (g : Fin 3 → ℕ → ℕ) (x : Ω) : Ω := fun i => g i (x i)

lemma cw_vec (a u v : ℕ → ℕ) (x : Ω) : cw ![a, u, v] x = ![a (x 0), u (x 1), v (x 2)] := by
  funext i; fin_cases i <;> rfl

lemma cw_vec' (g : Fin 3 → ℕ → ℕ) (a b c : ℕ) : cw g ![a, b, c] = ![g 0 a, g 1 b, g 2 c] := by
  funext i; fin_cases i <;> rfl

lemma gens_cw (g : Fin 3 → ℕ → ℕ) {E : Set Ω} (hE : E ∈ gens) : cw g ⁻¹' E ∈ gens := by
  obtain ⟨w, hw, hE⟩ := hE
  refine gens_of_local hw fun y z h hy => ?_
  refine (window_event_local hE (y := cw g y) (z := cw g z) fun k hk => ?_).mp hy
  show g k (y k) = g k (z k)
  rw [h k hk]

/-- **Pullback along coordinatewise maps** (hand proof, "Bridge"). -/
theorem mem_cw (g : Fin 3 → ℕ → ℕ) {E : Set Ω} (hE : D₃.Has E) : D₃.Has (cw g ⁻¹' E) := by
  induction hE with
  | basic t ht => exact DynkinSystem.GenerateHas.basic _ (gens_cw g ht)
  | empty => exact D₃.has_empty
  | @compl s _ ih => rw [preimage_compl]; exact D₃.has_compl ih
  | @iUnion f hd _ ih =>
    rw [preimage_iUnion]
    exact D₃.has_iUnion (fun i j hij => (hd hij).preimage (cw g)) ih

/-- The finitary closure is also stable under coordinatewise pullback (used in Step 5). -/
theorem dfin_cw (g : Fin 3 → ℕ → ℕ) {E : Set Ω} (hE : Dfin E) : Dfin (cw g ⁻¹' E) := by
  induction hE with
  | basic h => exact Dfin.basic (gens_cw g h)
  | compl _ ih => rw [preimage_compl]; exact Dfin.compl ih
  | union _ _ hd ih₁ ih₂ => rw [preimage_union]; exact Dfin.union ih₁ ih₂ (hd.preimage (cw g))

lemma cnt_cw (g : Fin 3 → ℕ → ℕ) (E : Set Ω) (a b c : ℕ) :
    cnt (cw g ⁻¹' E) ![a, b, c] = cnt E ![g 0 a, g 1 b, g 2 c] := by
  show cnt E (cw g ![a, b, c]) = _
  rw [cw_vec']

lemma box_cw (g : Fin 3 → ℕ → ℕ) {E : Set Ω} (hB : Box E) : Box (cw g ⁻¹' E) := by
  intro a a' b b' c c'
  simp only [cnt_cw]
  exact hB _ _ _ _ _ _

/-- Coordinate rotation: `rot ![a, y, z] = ![z, a, y]`. -/
def rot (x : Ω) : Ω := ![x 2, x 0, x 1]

lemma cnt_rot (E : Set Ω) (a b c : ℕ) : cnt (rot ⁻¹' E) ![a, b, c] = cnt E ![c, a, b] := rfl

lemma gens_rot {E : Set Ω} (hE : E ∈ gens) : rot ⁻¹' E ∈ gens := by
  obtain ⟨w, hw, hE⟩ := hE
  rcases hw with rfl | rfl | rfl
  · refine gens_of_local (w := {2, 0}) (by simp [W₃]) fun y z h hy => ?_
    refine (window_event_local hE (y := rot y) (z := rot z) fun k hk => ?_).mp hy
    simp only [Set.mem_insert_iff, Set.mem_singleton_iff] at hk
    rcases hk with rfl | rfl
    · exact h 2 (by simp)
    · exact h 0 (by simp)
  · refine gens_of_local (w := {0, 1}) (by simp [W₃]) fun y z h hy => ?_
    refine (window_event_local hE (y := rot y) (z := rot z) fun k hk => ?_).mp hy
    simp only [Set.mem_insert_iff, Set.mem_singleton_iff] at hk
    rcases hk with rfl | rfl
    · exact h 0 (by simp)
    · exact h 1 (by simp)
  · refine gens_of_local (w := {1, 2}) (by simp [W₃]) fun y z h hy => ?_
    refine (window_event_local hE (y := rot y) (z := rot z) fun k hk => ?_).mp hy
    simp only [Set.mem_insert_iff, Set.mem_singleton_iff] at hk
    rcases hk with rfl | rfl
    · exact h 1 (by simp)
    · exact h 2 (by simp)

/-- Pullback along the rotation. -/
theorem mem_rot {E : Set Ω} (hE : D₃.Has E) : D₃.Has (rot ⁻¹' E) := by
  induction hE with
  | basic t ht => exact DynkinSystem.GenerateHas.basic _ (gens_rot ht)
  | empty => exact D₃.has_empty
  | @compl s _ ih => rw [preimage_compl]; exact D₃.has_compl ih
  | @iUnion f hd _ ih =>
    rw [preimage_iUnion]
    exact D₃.has_iUnion (fun i j hij => (hd hij).preimage rot) ih

lemma box_rot {E : Set Ω} (hB : Box E) : Box (rot ⁻¹' E) := by
  intro a a' b b' c c'
  have := hB c c' a a' b b'
  simp only [cnt_rot]
  omega

/-- `turn i E` presents coordinate `i` of `E` as coordinate 0:
`![a, y, z] ∈ turn 0 E ↔ ![a, y, z] ∈ E`, `![a, y, z] ∈ turn 1 E ↔ ![z, a, y] ∈ E`,
`![a, y, z] ∈ turn 2 E ↔ ![y, z, a] ∈ E`. So in `turn i E` the distinguished value `a` sits at
coordinate `i` of `E`, and `(y, z)` are coordinates `(i+1, i+2)` of `E`, cyclically. -/
def turn : Fin 3 → Set Ω → Set Ω
  | 0, E => E
  | 1, E => rot ⁻¹' E
  | 2, E => rot ⁻¹' (rot ⁻¹' E)

lemma mem_turn_one (E : Set Ω) (a y z : ℕ) : ![a, y, z] ∈ turn 1 E ↔ ![z, a, y] ∈ E := Iff.rfl
lemma mem_turn_two (E : Set Ω) (a y z : ℕ) : ![a, y, z] ∈ turn 2 E ↔ ![y, z, a] ∈ E := Iff.rfl

theorem mem_turn {E : Set Ω} (hE : D₃.Has E) (i : Fin 3) : D₃.Has (turn i E) := by
  fin_cases i
  · exact hE
  · exact mem_rot hE
  · exact mem_rot (mem_rot hE)

lemma box_turn {E : Set Ω} (hB : Box E) (i : Fin 3) : Box (turn i E) := by
  fin_cases i
  · exact hB
  · exact box_rot hB
  · exact box_rot (box_rot hB)

/-! ## Step 1. Slice differences and the K relation -/

/-- Indicator of a set of values, as an integer. -/
noncomputable def ind (S : Set ℕ) (y : ℕ) : ℤ := by
  classical exact if y ∈ S then 1 else 0

lemma ind_pos {S : Set ℕ} {y : ℕ} (h : y ∈ S) : ind S y = 1 := by simp [ind, h]
lemma ind_neg {S : Set ℕ} {y : ℕ} (h : y ∉ S) : ind S y = 0 := by simp [ind, h]

lemma ind_cases (S : Set ℕ) (y : ℕ) : (y ∈ S ∧ ind S y = 1) ∨ (y ∉ S ∧ ind S y = 0) := by
  by_cases h : y ∈ S
  · exact Or.inl ⟨h, ind_pos h⟩
  · exact Or.inr ⟨h, ind_neg h⟩

lemma ind_compl (S : Set ℕ) (y : ℕ) : ind Sᶜ y = 1 - ind S y := by
  by_cases h : y ∈ S
  · have h2 : y ∉ Sᶜ := fun h' => h' h
    rw [ind_pos h, ind_neg h2]; norm_num
  · rw [ind_neg h, ind_pos (show y ∈ Sᶜ from h)]; norm_num

/-- Slice value of `E` at coordinate-0 value `a`, as an integer in {0,1}. -/
noncomputable def sl (E : Set Ω) (a y z : ℕ) : ℤ := (cnt E ![a, y, z] : ℤ)

lemma sl_cases (E : Set Ω) (a y z : ℕ) : sl E a y z = 0 ∨ sl E a y z = 1 := by
  have := cnt_le E ![a, y, z]
  unfold sl; omega

lemma sl_eq_one_iff (E : Set Ω) (a y z : ℕ) : sl E a y z = 1 ↔ ![a, y, z] ∈ E := by
  unfold sl cnt
  by_cases h : ![a, y, z] ∈ E <;> simp [h]

/-- Slice difference `1_{E_a} − 1_{E_b}` as a function of the two remaining coordinates. -/
noncomputable def dif (E : Set Ω) (a b y z : ℕ) : ℤ := sl E a y z - sl E b y z

lemma dif_def (E : Set Ω) (a b y z : ℕ) : dif E a b y z = sl E a y z - sl E b y z := rfl

lemma dif_range (E : Set Ω) (a b y z : ℕ) : -1 ≤ dif E a b y z ∧ dif E a b y z ≤ 1 := by
  have := sl_cases E a y z; have := sl_cases E b y z
  rw [dif_def]; omega

/-- Box identity for slice differences (hand Step 1, "Slice difference"). -/
lemma dif_add {E : Set Ω} (hB : Box E) (a b y y' z z' : ℕ) :
    dif E a b y z + dif E a b y' z' = dif E a b y' z + dif E a b y z' := by
  have := hB a b y y' z z'
  simp only [dif_def, sl]
  omega

/-- **Slice differences split**: for a box set, `1_{E_a} − 1_{E_b} = α(y) + β(z)`. -/
theorem dif_split {E : Set Ω} (hB : Box E) (a b : ℕ) :
    ∃ α β : ℕ → ℤ, ∀ y z, dif E a b y z = α y + β z := by
  refine ⟨fun y => dif E a b y 0, fun z => dif E a b 0 z - dif E a b 0 0, fun y z => ?_⟩
  have := dif_add hB a b y 0 z 0
  simp only
  omega

/-- `a ≃₁ b`: the slice difference is a function of the first remaining coordinate alone. -/
def Eq1 (E : Set Ω) (a b : ℕ) : Prop := ∀ y z z', dif E a b y z = dif E a b y z'

/-- `a ≃₂ b`: the slice difference is a function of the second remaining coordinate alone. -/
def Eq2 (E : Set Ω) (a b : ℕ) : Prop := ∀ y y' z, dif E a b y z = dif E a b y' z

/-- **K-related** (coordinate 0): the slice difference `1_{E_a} − 1_{E_b}`, a function of
`(x₁, x₂)`, is neither a function of `x₁` alone nor a function of `x₂` alone. This is the hand
proof's definition verbatim ("K-related otherwise"). For coordinates 1 and 2 use
`KRelAt i E := KRel (turn i E)` (rotation, see `turn`). -/
def KRel (E : Set Ω) (a b : ℕ) : Prop := ¬ Eq1 E a b ∧ ¬ Eq2 E a b

/-- K-related at coordinate `i`: values `a b` of coordinate `i`, slices taken in coordinates
`(i+1, i+2)` cyclically. `KRelAt 0 E = KRel E` by definition. -/
def KRelAt (i : Fin 3) (E : Set Ω) (a b : ℕ) : Prop := KRel (turn i E) a b

lemma eq1_refl (E : Set Ω) (a : ℕ) : Eq1 E a a := by
  intro y z z'; simp [dif_def]

lemma eq1_symm {E : Set Ω} {a b : ℕ} (h : Eq1 E a b) : Eq1 E b a := by
  intro y z z'
  have := h y z z'
  simp only [dif_def] at *
  omega

lemma eq1_trans {E : Set Ω} {a b c : ℕ} (h : Eq1 E a b) (h' : Eq1 E b c) : Eq1 E a c := by
  intro y z z'
  have := h y z z'; have := h' y z z'
  simp only [dif_def] at *
  omega

lemma eq2_symm {E : Set Ω} {a b : ℕ} (h : Eq2 E a b) : Eq2 E b a := by
  intro y y' z
  have := h y y' z
  simp only [dif_def] at *
  omega

lemma eq2_trans {E : Set Ω} {a b c : ℕ} (h : Eq2 E a b) (h' : Eq2 E b c) : Eq2 E a c := by
  intro y y' z
  have := h y y' z; have := h' y y' z
  simp only [dif_def] at *
  omega

lemma krel_irrefl (E : Set Ω) (a : ℕ) : ¬ KRel E a a := fun h => h.1 (eq1_refl E a)

lemma krel_symm (E : Set Ω) : Symmetric (KRel E) :=
  fun _ _ h => ⟨fun h' => h.1 (eq1_symm h'), fun h' => h.2 (eq2_symm h')⟩

/-! ### The K form `d = [y ∈ U] + [z ∈ V] − 1` -/

/-- The "high" rows of a difference function. -/
def Uof (d : ℕ → ℕ → ℤ) : Set ℕ := {y | ∃ z, d y z = 1}
/-- The "high" columns of a difference function. -/
def Vof (d : ℕ → ℕ → ℤ) : Set ℕ := {z | ∃ y, d y z = 1}

/-- Hand Step 1, dichotomy: an additive `{−1,0,1}`-valued `d` depending on both variables is
`[y ∈ U] + [z ∈ V] − 1`, with `U = Uof d`, `V = Vof d` intrinsic. -/
lemma kform {d : ℕ → ℕ → ℤ}
    (hA : ∀ y y' z z', d y z + d y' z' = d y' z + d y z')
    (hR : ∀ y z, -1 ≤ d y z ∧ d y z ≤ 1)
    (h1 : ¬ ∀ y z z', d y z = d y z') (h2 : ¬ ∀ y y' z, d y z = d y' z) :
    ∀ y z, d y z = ind (Uof d) y + ind (Vof d) z - 1 := by
  push Not at h1 h2
  obtain ⟨y₂, z₂, z₂', hz⟩ := h1
  obtain ⟨y₀, y₀', z₀, hy⟩ := h2
  obtain ⟨yU, zV, yL, zL, hUV, hLL, hUL, hLV⟩ :
      ∃ yU zV yL zL, d yU zV = 1 ∧ d yL zL = -1 ∧ d yU zL = 0 ∧ d yL zV = 0 := by
    have e1 := hA y₂ y₀ z₂ z₂'
    have e2 := hA y₀ y₀' z₀ z₂
    have e3 := hA y₀ y₀' z₂ z₂'
    have r1 := hR y₀ z₂; have r2 := hR y₀ z₂'; have r3 := hR y₀' z₂; have r4 := hR y₀' z₂'
    have hpq : d y₀ z₂ ≠ d y₀ z₂' := by omega
    have hpr : d y₀ z₂ ≠ d y₀' z₂ := by omega
    rcases lt_or_gt_of_ne hpq with h | h <;> rcases lt_or_gt_of_ne hpr with h' | h'
    · exact ⟨y₀', z₂', y₀, z₂, by omega, by omega, by omega, by omega⟩
    · exact ⟨y₀, z₂', y₀', z₂, by omega, by omega, by omega, by omega⟩
    · exact ⟨y₀', z₂, y₀, z₂', by omega, by omega, by omega, by omega⟩
    · exact ⟨y₀, z₂, y₀', z₂', by omega, by omega, by omega, by omega⟩
  have hU : ∀ y, (y ∈ Uof d ↔ d y zL = 0) := by
    intro y
    constructor
    · rintro ⟨z₁, hz₁⟩
      have := hA y yL z₁ zL; have := hA yU yL z₁ zL; have := hA y yU zV zL
      have := hR yL z₁; have := hR yU z₁; have := hR y zL; have := hR y zV
      omega
    · intro h
      refine ⟨zV, ?_⟩
      have := hA y yU zV zL
      omega
  have hV : ∀ z, (z ∈ Vof d ↔ d yL z = 0) := by
    intro z
    constructor
    · rintro ⟨y₁, hy₁⟩
      have := hA yU yL z zV; have := hA y₁ yL z zL; have := hA y₁ yL zV zL
      have := hR yL z; have := hR yU z; have := hR y₁ zL; have := hR y₁ zV
      omega
    · intro h
      refine ⟨yU, ?_⟩
      have := hA yU yL z zV
      omega
  intro y z
  have e0 := hA y yL z zL
  have e1 := hA y yU zV zL
  have e2 := hA yU yL z zV
  have := hR y zV; have := hR y zL; have := hR yL z; have := hR yU z
  rcases ind_cases (Uof d) y with ⟨hy, ey⟩ | ⟨hy, ey⟩ <;>
    rcases ind_cases (Vof d) z with ⟨hz, ez⟩ | ⟨hz, ez⟩
  · have := (hU y).mp hy; have := (hV z).mp hz; omega
  · have := (hU y).mp hy; have : ¬ d yL z = 0 := mt (hV z).mpr hz; omega
  · have : ¬ d y zL = 0 := mt (hU y).mpr hy; have := (hV z).mp hz; omega
  · have : ¬ d y zL = 0 := mt (hU y).mpr hy; have : ¬ d yL z = 0 := mt (hV z).mpr hz; omega

/-- K form of the slice difference of a K-related pair of a box set. -/
lemma krel_form {E : Set Ω} (hB : Box E) {a b : ℕ} (h : KRel E a b) (y z : ℕ) :
    dif E a b y z = ind (Uof (dif E a b)) y + ind (Vof (dif E a b)) z - 1 :=
  kform (dif_add hB a b) (dif_range E a b) h.1 h.2 y z

/-! ### The chain (hand Step 1, "Chain") -/

lemma ex_diff {A B : Set ℕ} (hsub : A ⊆ B)
    (h : ∃ y y', ind A y - ind B y ≠ ind A y' - ind B y') : ∃ y, y ∈ B ∧ y ∉ A := by
  by_contra hcon
  push Not at hcon
  obtain ⟨y, y', hne⟩ := h
  have key : ∀ t, ind A t = ind B t := by
    intro t
    by_cases hA : t ∈ A
    · rw [ind_pos hA, ind_pos (hsub hA)]
    · have hB : t ∉ B := fun hB => hA (hcon t hB)
      rw [ind_neg hA, ind_neg hB]
  apply hne
  rw [key y, key y']
  simp

/-- Two K-type differences whose difference is again K-type are strictly nested, oppositely
in the two variables. -/
lemma chain_cmp {Ua Ub Va Vb : Set ℕ}
    (hR : ∀ y z, -1 ≤ (ind Ua y - ind Ub y) + (ind Va z - ind Vb z) ∧
      (ind Ua y - ind Ub y) + (ind Va z - ind Vb z) ≤ 1)
    (hy : ∃ y y', ind Ua y - ind Ub y ≠ ind Ua y' - ind Ub y')
    (hz : ∃ z z', ind Va z - ind Vb z ≠ ind Va z' - ind Vb z') :
    (Ua ⊂ Ub ∧ Vb ⊂ Va) ∨ (Ub ⊂ Ua ∧ Va ⊂ Vb) := by
  by_cases hex : ∃ y1, y1 ∈ Ua ∧ y1 ∉ Ub
  · right
    obtain ⟨y1, h1, h2⟩ := hex
    have e1 := ind_pos h1; have e2 := ind_neg h2
    have hVsub : Va ⊆ Vb := by
      intro t ht; by_contra hn
      have := hR y1 t; have := ind_pos ht; have := ind_neg hn
      omega
    obtain ⟨z1, hz1, hz1'⟩ := ex_diff hVsub hz
    have e3 := ind_pos hz1; have e4 := ind_neg hz1'
    have hUsub : Ub ⊆ Ua := by
      intro t ht; by_contra hn
      have := hR t z1; have := ind_pos ht; have := ind_neg hn
      omega
    exact ⟨⟨hUsub, fun h => h2 (h h1)⟩, ⟨hVsub, fun h => hz1' (h hz1)⟩⟩
  · left
    push Not at hex
    have hUsub : Ua ⊆ Ub := fun t ht => hex t ht
    obtain ⟨y1, hy1, hy1'⟩ := ex_diff hUsub hy
    have e1 := ind_pos hy1; have e2 := ind_neg hy1'
    have hVsub : Vb ⊆ Va := by
      intro t ht; by_contra hn
      have := hR y1 t; have := ind_pos ht; have := ind_neg hn
      omega
    obtain ⟨z, z', hzz⟩ := hz
    obtain ⟨z1, hz1, hz1'⟩ := ex_diff hVsub ⟨z, z', by omega⟩
    exact ⟨⟨hUsub, fun h => hy1' (h hy1)⟩, ⟨hVsub, fun h => hz1' (h hz1)⟩⟩

/-! ### The sub-grid (hand Step 1, "Sub-grid") -/

/-- Along a sequence with `U` strictly increasing and `V` strictly decreasing, witnesses
`u j ∈ U (j+1) ∖ U j`, `v k ∈ V k ∖ V (k+1)` give the pattern
`h (a i) (u j) (v k) = [k<j] + [j<i] + [i≤k] − 1` for `j ≠ k`. -/
lemma grid_pattern {h : ℕ → ℕ → ℕ → ℤ} (h01 : ∀ a y z, h a y z = 0 ∨ h a y z = 1)
    (q : ℕ) (a : ℕ → ℕ) (Us Vs : ℕ → Set ℕ)
    (hform : ∀ i y z, h (a i) y z = h q y z + ind (Us i) y + ind (Vs i) z - 1)
    (hU : ∀ i, Us i ⊂ Us (i + 1)) (hV : ∀ i, Vs (i + 1) ⊂ Vs i) :
    ∃ u v : ℕ → ℕ, ∀ i j k, j ≠ k →
      h (a i) (u j) (v k) =
        (if k < j then 1 else 0) + (if j < i then 1 else 0) + (if i ≤ k then 1 else 0) - 1 := by
  choose u hu1 hu2 using fun j => Set.exists_of_ssubset (hU j)
  choose v hv1 hv2 using fun k => Set.exists_of_ssubset (hV k)
  have hmono : Monotone Us := monotone_nat_of_le_succ fun i => (hU i).1
  have hanti : Antitone Vs := antitone_nat_of_succ_le fun i => (hV i).1
  have iu : ∀ i j, ind (Us i) (u j) = if j < i then 1 else 0 := by
    intro i j
    by_cases hji : j < i
    · rw [if_pos hji]; exact ind_pos (hmono (Nat.succ_le_of_lt hji) (hu1 j))
    · rw [if_neg hji]; exact ind_neg fun hm => hu2 j (hmono (Nat.le_of_not_lt hji) hm)
  have iv : ∀ i k, ind (Vs i) (v k) = if i ≤ k then 1 else 0 := by
    intro i k
    by_cases hik : i ≤ k
    · rw [if_pos hik]; exact ind_pos (hanti hik (hv1 k))
    · rw [if_neg hik]
      exact ind_neg fun hm => hv2 k (hanti (Nat.succ_le_of_lt (Nat.lt_of_not_le hik)) hm)
  have key : ∀ i j k, h (a i) (u j) (v k) =
      h q (u j) (v k) + (if j < i then 1 else 0) + (if i ≤ k then 1 else 0) - 1 := by
    intro i j k; rw [hform, iu, iv]
  refine ⟨u, v, fun i j k hjk => ?_⟩
  have hq : h q (u j) (v k) = if k < j then 1 else 0 := by
    rcases Nat.lt_or_gt_of_ne hjk with hlt | hgt
    · have e := key k j k
      have := h01 (a k) (u j) (v k); have := h01 q (u j) (v k)
      rw [if_pos hlt, if_pos (le_refl k)] at e
      rw [if_neg (Nat.lt_asymm hlt)]
      omega
    · have e := key j j k
      have := h01 (a j) (u j) (v k); have := h01 q (u j) (v k)
      rw [if_neg (Nat.lt_irrefl j), if_neg (Nat.not_le_of_gt hgt)] at e
      rw [if_pos hgt]
      omega
  rw [key, hq]

lemma compl_ssub {A B : Set ℕ} (h : A ⊂ B) : Bᶜ ⊂ Aᶜ :=
  ⟨Set.compl_subset_compl.mpr h.1, fun h' => h.2 (Set.compl_subset_compl.mp h')⟩

/-! ### Clique ⇒ `InP` (hand Step 1, "Contradiction") -/

/-- **Clique ⇒ InP.** An infinite set of pairwise K-related values of coordinate 0 of a box set
`E` yields a coordinatewise map `G = cw g` with `InP (G ⁻¹' E)`: on triples of distinct indices
the pullback is the anticyclic set (chain increasing) or the cyclic set (chain decreasing),
with `P = univ`. -/
theorem clique_inP {E : Set Ω} (hB : Box E) {C : Set ℕ} (hC : C.Infinite)
    (hK : C.Pairwise (KRel E)) : ∃ g : Fin 3 → ℕ → ℕ, InP (cw g ⁻¹' E) := by
  obtain ⟨q, hq⟩ := hC.nonempty
  have hC' : (C \ {q}).Infinite := hC.diff (Set.finite_singleton q)
  obtain ⟨f, hfC, hfq, hfinj⟩ : ∃ f : ℕ → ℕ, (∀ n, f n ∈ C) ∧ (∀ n, f n ≠ q) ∧
      (∀ m n, m ≠ n → f m ≠ f n) := by
    refine ⟨fun n => (Set.Infinite.natEmbedding _ hC' n : ℕ), fun n => ?_, fun n => ?_,
      fun m n hmn e => ?_⟩
    · exact (Set.Infinite.natEmbedding _ hC' n).2.1
    · exact (Set.Infinite.natEmbedding _ hC' n).2.2
    · exact hmn ((Set.Infinite.natEmbedding _ hC').injective (Subtype.ext e))
  have hKq : ∀ n, KRel E (f n) q := fun n => hK (hfC n) hq (hfq n)
  obtain ⟨Us, hUs⟩ : ∃ Us : ℕ → Set ℕ, ∀ n, Us n = Uof (dif E (f n) q) :=
    ⟨_, fun _ => rfl⟩
  obtain ⟨Vs, hVs⟩ : ∃ Vs : ℕ → Set ℕ, ∀ n, Vs n = Vof (dif E (f n) q) :=
    ⟨_, fun _ => rfl⟩
  have hform : ∀ n y z, sl E (f n) y z = sl E q y z + ind (Us n) y + ind (Vs n) z - 1 := by
    intro n y z
    have := krel_form hB (hKq n) y z
    rw [dif_def] at this
    rw [hUs, hVs]
    omega
  have hcmp : ∀ m n, m ≠ n →
      (Us m ⊂ Us n ∧ Vs n ⊂ Vs m) ∨ (Us n ⊂ Us m ∧ Vs m ⊂ Vs n) := by
    intro m n hmn
    have hKmn : KRel E (f m) (f n) := hK (hfC m) (hfC n) (hfinj m n hmn)
    have key : ∀ y z, dif E (f m) (f n) y z =
        (ind (Us m) y - ind (Us n) y) + (ind (Vs m) z - ind (Vs n) z) := by
      intro y z
      have h1 := hform m y z; have h2 := hform n y z
      rw [dif_def]; omega
    apply chain_cmp
    · intro y z; rw [← key]; exact dif_range _ _ _ _ _
    · have h2 := hKmn.2
      unfold Eq2 at h2
      push Not at h2
      obtain ⟨y, y', z, h⟩ := h2
      rw [key, key] at h
      exact ⟨y, y', fun e => h (by omega)⟩
    · have h1 := hKmn.1
      unfold Eq1 at h1
      push Not at h1
      obtain ⟨y, z, z', h⟩ := h1
      rw [key, key] at h
      exact ⟨z, z', fun e => h (by omega)⟩
  obtain ⟨g, hg⟩ := exists_increasing_or_nonincreasing_subseq'
    (fun m n => Us m ⊂ Us n ∧ Vs n ⊂ Vs m) (id : ℕ → ℕ)
  rcases hg with hinc | hdec
  · -- increasing chain: anticyclic pattern
    obtain ⟨u, v, huv⟩ := grid_pattern (h := sl E) (sl_cases E) q (fun i => f (g i))
      (fun i => Us (g i)) (fun i => Vs (g i)) (fun i y z => hform (g i) y z)
      (fun i => (hinc i).1) (fun i => (hinc i).2)
    refine ⟨![fun i => f (g i), u, v], Set.univ, Set.infinite_univ, Or.inr ?_⟩
    intro x _ hx
    rw [mem_preimage, cw_vec, ← sl_eq_one_iff, huv _ _ _ hx.2.1]
    unfold Dist at hx
    unfold Acy
    split_ifs <;> omega
  · -- decreasing chain: cyclic pattern, via the complement
    have hrev : ∀ i, Us (g (i + 1)) ⊂ Us (g i) ∧ Vs (g i) ⊂ Vs (g (i + 1)) := by
      intro i
      have hne : g i ≠ g (i + 1) := fun e => (Nat.succ_ne_self i) (g.injective e).symm
      rcases hcmp (g i) (g (i + 1)) hne with h | h
      · exact absurd h (hdec i (i + 1) (Nat.lt_succ_self i))
      · exact h
    obtain ⟨u, v, huv⟩ := grid_pattern (h := fun a y z => 1 - sl E a y z)
      (fun a y z => by
        have := sl_cases E a y z
        show 1 - sl E a y z = 0 ∨ 1 - sl E a y z = 1
        omega) q (fun i => f (g i))
      (fun i => (Us (g i))ᶜ) (fun i => (Vs (g i))ᶜ)
      (fun i y z => by
        have := hform (g i) y z
        show 1 - sl E (f (g i)) y z =
          1 - sl E q y z + ind (Us (g i))ᶜ y + ind (Vs (g i))ᶜ z - 1
        rw [ind_compl, ind_compl]; omega)
      (fun i => compl_ssub (hrev i).1) (fun i => compl_ssub (hrev i).2)
    refine ⟨![fun i => f (g i), u, v], Set.univ, Set.infinite_univ, Or.inl ?_⟩
    intro x _ hx
    have e := huv (x 0) (x 1) (x 2) hx.2.1
    rw [mem_preimage, cw_vec, ← sl_eq_one_iff]
    unfold Dist at hx
    unfold Cyc
    split_ifs at e <;> omega

/-- **Step 1, coordinate 0.** A carrier set has no infinite K-clique at coordinate 0. -/
theorem no_infinite_clique₀ {E : Set Ω} (hE : D₃.Has E) {C : Set ℕ} (hC : C.Infinite) :
    ¬ C.Pairwise (KRel E) := by
  intro hK
  obtain ⟨g, hg⟩ := clique_inP (box_of_mem hE) hC hK
  exact not_inP_of_mem (mem_cw g hE) hg

/-- **Step 1.** A carrier set has no infinite K-clique at any coordinate. -/
theorem no_infinite_clique {E : Set Ω} (hE : D₃.Has E) (i : Fin 3) {C : Set ℕ}
    (hC : C.Infinite) : ¬ C.Pairwise (KRelAt i E) :=
  no_infinite_clique₀ (mem_turn hE i) hC

/-! ## Step 2. Finite labelled cover -/

/-- A finite labelled cover of the values of coordinate `i`: finitely many parts, each lying
inside a single `≃₁`-class (`kind = true`; hand label "→ i+1") or a single `≃₂`-class
(`kind = false`; hand label "→ i+2") of `turn i E`. -/
def Cover (i : Fin 3) (E : Set Ω) : Prop :=
  ∃ (n : ℕ) (lab : ℕ → Fin n) (kind : Fin n → Bool), ∀ a b, lab a = lab b →
    (kind (lab a) = true → Eq1 (turn i E) a b) ∧ (kind (lab a) = false → Eq2 (turn i E) a b)

/-- Step 2 at coordinate 0, from "every K-clique is finite" (K-clique = matching; a maximal one
is finite and each value is non-K-related to one of its members). -/
theorem finite_cover₀ {E : Set Ω} (hfin : ∀ C : Set ℕ, C.Pairwise (KRel E) → C.Finite) :
    ∃ (n : ℕ) (lab : ℕ → Fin n) (kind : Fin n → Bool), ∀ a b, lab a = lab b →
      (kind (lab a) = true → Eq1 E a b) ∧ (kind (lab a) = false → Eq2 E a b) := by
  classical
  obtain ⟨M, hM⟩ := zorn_subset {C : Set ℕ | C.Pairwise (KRel E)} (by
    intro c hc hchain
    exact ⟨⋃₀ c, (Set.pairwise_sUnion hchain.directedOn).2 fun s hs => hc hs,
      fun s hs => Set.subset_sUnion_of_mem hs⟩)
  have hMp : M.Pairwise (KRel E) := hM.1
  have hMfin : M.Finite := hfin M hMp
  have key : ∀ a, ∃ m ∈ M, ¬ KRel E a m := by
    intro a
    by_contra hcon
    push Not at hcon
    have hins : (insert a M).Pairwise (KRel E) :=
      (Set.pairwise_insert_of_symmetric (krel_symm E)).2 ⟨hMp, fun b hb _ => hcon b hb⟩
    have haM : a ∈ M := hM.2 hins (Set.subset_insert a M) (Set.mem_insert a M)
    exact krel_irrefl E a (hcon a haM)
  choose m hmM hm using key
  have hm' : ∀ a, ¬ Eq1 E a (m a) → Eq2 E a (m a) := fun a h1 => by
    by_contra h2; exact hm a ⟨h1, h2⟩
  haveI : Finite M := hMfin.to_subtype
  obtain ⟨n, ⟨e⟩⟩ := Finite.exists_equiv_fin (M × Bool)
  refine ⟨n, fun a => e (⟨m a, hmM a⟩, decide (Eq1 E a (m a))), fun l => (e.symm l).2, ?_⟩
  intro a b hab
  have hab' := e.injective hab
  simp only [Prod.mk.injEq, Subtype.mk.injEq] at hab'
  obtain ⟨hmab, hdec⟩ := hab'
  simp only [Equiv.symm_apply_apply, decide_eq_true_eq, decide_eq_false_iff_not]
  constructor
  · intro ha
    have hb : Eq1 E b (m b) := by
      have : decide (Eq1 E b (m b)) = true := by rw [← hdec]; exact decide_eq_true ha
      exact of_decide_eq_true this
    rw [← hmab] at hb
    exact eq1_trans ha (eq1_symm hb)
  · intro ha
    have hb : ¬ Eq1 E b (m b) := by
      intro hb
      have : decide (Eq1 E a (m a)) = true := by rw [hdec]; exact decide_eq_true hb
      exact ha (of_decide_eq_true this)
    have hb2 := hm' b hb
    rw [← hmab] at hb2
    exact eq2_trans (hm' a ha) (eq2_symm hb2)

/-- **Step 2.** Every coordinate of a carrier set has a finite labelled cover. -/
theorem finite_cover {E : Set Ω} (hE : D₃.Has E) (i : Fin 3) : Cover i E :=
  finite_cover₀ fun _ hC => by_contra fun h => no_infinite_clique hE i h hC

/-! ## Step 5 support: closure properties of `Dfin` and of `Box` -/

lemma dfin_empty : Dfin (∅ : Set Ω) :=
  Dfin.basic (gens_of_local (w := {0, 1}) (by simp [W₃]) fun _ _ _ h => False.elim h)

/-- Removing a contained finitary set stays finitary. -/
lemma dfin_diff {A B : Set Ω} (hA : Dfin A) (hB : Dfin B) (h : B ⊆ A) : Dfin (A \ B) := by
  have hd : Disjoint Aᶜ B := Set.disjoint_left.mpr fun x hx hxB => hx (h hxB)
  have : A \ B = (Aᶜ ∪ B)ᶜ := by
    ext x; simp only [mem_diff, mem_compl_iff, mem_union, not_or, not_not]
  rw [this]
  exact Dfin.compl (Dfin.union (Dfin.compl hA) hB hd)

lemma cnt_union {A B : Set Ω} (hd : Disjoint A B) (p : Ω) :
    cnt (A ∪ B) p = cnt A p + cnt B p := by
  by_cases ha : p ∈ A
  · have hb : p ∉ B := Set.disjoint_left.mp hd ha
    simp [cnt, ha, hb]
  · by_cases hb : p ∈ B <;> simp [cnt, ha, hb]

/-- The box identity is cancellative over disjoint unions. -/
lemma box_cancel {A B : Set Ω} (hAB : Box (A ∪ B)) (hA : Box A) (hd : Disjoint A B) : Box B := by
  intro a a' b b' c c'
  have h1 := hAB a a' b b' c c'
  have h2 := hA a a' b b' c c'
  simp only [cnt_union hd] at h1
  omega

/-! ## Step 3. Columns and the residue (normal form; not used by `mem_dfin`) -/

/-- A set that factors through a finite coordinatewise quotient: membership depends only on
finitely many labels per coordinate. (Over ℕ³ this replaces "`R = g⁻¹(F̂)` with `F̂` on a finite
grid": the grid is the set of label triples.) -/
def FinDet (R : Set Ω) : Prop :=
  ∃ (n : ℕ) (lab : Fin 3 → ℕ → Fin n),
    ∀ x y : Ω, (∀ i, lab i (x i) = lab i (y i)) → x ∈ R → y ∈ R

lemma mem_iff_sl (E : Set Ω) (x : Ω) : x ∈ E ↔ sl E (x 0) (x 1) (x 2) = 1 := by
  rw [sl_eq_one_iff, ← eta x]

lemma finDet_of_finite {α β γ : Type} [Finite α] [Finite β] [Finite γ] {R : Set Ω}
    (l0 : ℕ → α) (l1 : ℕ → β) (l2 : ℕ → γ)
    (h : ∀ x y : Ω, l0 (x 0) = l0 (y 0) → l1 (x 1) = l1 (y 1) → l2 (x 2) = l2 (y 2) →
      x ∈ R → y ∈ R) : FinDet R := by
  obtain ⟨n, ⟨e⟩⟩ := Finite.exists_equiv_fin (α ⊕ β ⊕ γ)
  refine ⟨n, ![fun v => e (Sum.inl (l0 v)), fun v => e (Sum.inr (Sum.inl (l1 v))),
    fun v => e (Sum.inr (Sum.inr (l2 v)))], fun x y hxy hx => ?_⟩
  have h0 : e (Sum.inl (l0 (x 0))) = e (Sum.inl (l0 (y 0))) := hxy 0
  have h1 : e (Sum.inr (Sum.inl (l1 (x 1)))) = e (Sum.inr (Sum.inl (l1 (y 1)))) := hxy 1
  have h2 : e (Sum.inr (Sum.inr (l2 (x 2)))) = e (Sum.inr (Sum.inr (l2 (y 2)))) := hxy 2
  exact h x y (Sum.inl_injective (e.injective h0))
    (Sum.inl_injective (Sum.inr_injective (e.injective h1)))
    (Sum.inr_injective (Sum.inr_injective (e.injective h2))) hx

lemma exists_rep {n : ℕ} (lab : ℕ → Fin n) : ∃ rep : Fin n → ℕ, ∀ a, lab (rep (lab a)) = lab a := by
  classical
  refine ⟨fun l => if hl : ∃ a, lab a = l then Classical.choose hl else 0, fun a => ?_⟩
  have hl : ∃ a', lab a' = lab a := ⟨a, rfl⟩
  simp only [dif_pos hl]
  exact Classical.choose_spec hl

/-- **Mutual column** (hand Step 3, first bullet), abstract form. On `P × Q × ℕ`, if differences in
the first argument do not depend on the third, and differences in the second do not depend on the
third, then "member, on a line that is not full" depends on the third argument only. -/
lemma mutual_abs {G : ℕ → ℕ → ℕ → ℤ} (h01 : ∀ a y z, G a y z = 0 ∨ G a y z = 1) {P Q : Set ℕ}
    (hP : ∀ a ∈ P, ∀ a' ∈ P, ∀ y z z', G a y z - G a' y z = G a y z' - G a' y z')
    (hQ : ∀ y ∈ Q, ∀ y' ∈ Q, ∀ a z z', G a y z - G a y' z = G a y z' - G a y' z')
    {a a' y y' z : ℕ} (ha : a ∈ P) (ha' : a' ∈ P) (hy : y ∈ Q) (hy' : y' ∈ Q)
    (h1 : G a y z = 1) (h0 : ∃ z₀, G a y z₀ = 0) : G a' y' z = 1 ∧ ∃ z₀, G a' y' z₀ = 0 := by
  obtain ⟨z₀, hz₀⟩ := h0
  have e1 := hP a ha a' ha' y z z₀
  have e2 := hQ y hy y' hy' a' z z₀
  have := h01 a' y z; have := h01 a' y z₀; have := h01 a' y' z; have := h01 a' y' z₀
  exact ⟨by omega, z₀, by omega⟩

/-- **Cyclic cell** (hand Step 3, "Cells"), abstract form. If on `P × Q × T` differences in the
first argument depend on the second only, in the second on the third only, in the third on the
first only, then on the cell `G` depends on one argument only. -/
lemma cyclic_abs {G : ℕ → ℕ → ℕ → ℤ} (h01 : ∀ a y z, G a y z = 0 ∨ G a y z = 1) {P Q T : Set ℕ}
    (hP : ∀ a ∈ P, ∀ a' ∈ P, ∀ y z z', G a y z - G a' y z = G a y z' - G a' y z')
    (hQ : ∀ y ∈ Q, ∀ y' ∈ Q, ∀ z a a', G a y z - G a y' z = G a' y z - G a' y' z)
    (hT : ∀ z ∈ T, ∀ z' ∈ T, ∀ a y y', G a y z - G a y z' = G a y' z - G a y' z') :
    (∀ a ∈ P, ∀ y ∈ Q, ∀ y' ∈ Q, ∀ z ∈ T, ∀ z' ∈ T, G a y z = G a y' z') ∨
    (∀ y ∈ Q, ∀ a ∈ P, ∀ a' ∈ P, ∀ z ∈ T, ∀ z' ∈ T, G a y z = G a' y z') ∨
    (∀ z ∈ T, ∀ a ∈ P, ∀ a' ∈ P, ∀ y ∈ Q, ∀ y' ∈ Q, G a y z = G a' y' z) := by
  have L1 : ∀ a ∈ P, ∀ a' ∈ P, ∀ y ∈ Q, ∀ y' ∈ Q, ∀ z z',
      G a y z - G a' y z = G a y' z' - G a' y' z' := by
    intro a ha a' ha' y hy y' hy' z z'
    have := hP a ha a' ha' y z z'; have := hQ y hy y' hy' z' a a'; omega
  have L2 : ∀ y ∈ Q, ∀ y' ∈ Q, ∀ z ∈ T, ∀ z' ∈ T, ∀ a a',
      G a y z - G a y' z = G a' y z' - G a' y' z' := by
    intro y hy y' hy' z hz z' hz' a a'
    have := hQ y hy y' hy' z a a'; have := hT z hz z' hz' a' y y'; omega
  have L3 : ∀ z ∈ T, ∀ z' ∈ T, ∀ a ∈ P, ∀ a' ∈ P, ∀ y y',
      G a y z - G a y z' = G a' y' z - G a' y' z' := by
    intro z hz z' hz' a ha a' ha' y y'
    have := hT z hz z' hz' a y y'; have := hP a ha a' ha' y' z z'; omega
  have n12 : ∀ a ∈ P, ∀ a' ∈ P, ∀ y₁ ∈ Q, ∀ z₁ ∈ T, G a y₁ z₁ ≠ G a' y₁ z₁ →
      ∀ y ∈ Q, ∀ y' ∈ Q, ∀ a₂ ∈ P, ∀ z₂ ∈ T, G a₂ y z₂ ≠ G a₂ y' z₂ → False := by
    intro a ha a' ha' y₁ hy₁ z₁ hz₁ hc y hy y' hy' a₂ ha₂ z₂ hz₂ hd
    have := L1 a ha a' ha' y hy y₁ hy₁ z₂ z₁
    have := L1 a ha a' ha' y' hy' y₁ hy₁ z₂ z₁
    have := L2 y hy y' hy' z₂ hz₂ z₂ hz₂ a a₂
    have := L2 y hy y' hy' z₂ hz₂ z₂ hz₂ a' a₂
    have := h01 a y₁ z₁; have := h01 a' y₁ z₁; have := h01 a₂ y z₂; have := h01 a₂ y' z₂
    have := h01 a y z₂; have := h01 a' y z₂; have := h01 a y' z₂; have := h01 a' y' z₂
    omega
  have n13 : ∀ a ∈ P, ∀ a' ∈ P, ∀ y₁ ∈ Q, ∀ z₁ ∈ T, G a y₁ z₁ ≠ G a' y₁ z₁ →
      ∀ z ∈ T, ∀ z' ∈ T, ∀ a₃ ∈ P, ∀ y₃ ∈ Q, G a₃ y₃ z ≠ G a₃ y₃ z' → False := by
    intro a ha a' ha' y₁ hy₁ z₁ hz₁ hc z hz z' hz' a₃ ha₃ y₃ hy₃ he
    have := L1 a ha a' ha' y₁ hy₁ y₁ hy₁ z z₁
    have := L1 a ha a' ha' y₁ hy₁ y₁ hy₁ z' z₁
    have := L3 z hz z' hz' a ha a₃ ha₃ y₁ y₃
    have := L3 z hz z' hz' a' ha' a₃ ha₃ y₁ y₃
    have := h01 a y₁ z₁; have := h01 a' y₁ z₁; have := h01 a₃ y₃ z; have := h01 a₃ y₃ z'
    have := h01 a y₁ z; have := h01 a' y₁ z; have := h01 a y₁ z'; have := h01 a' y₁ z'
    omega
  have n23 : ∀ y ∈ Q, ∀ y' ∈ Q, ∀ a₂ ∈ P, ∀ z₂ ∈ T, G a₂ y z₂ ≠ G a₂ y' z₂ →
      ∀ z ∈ T, ∀ z' ∈ T, ∀ a₃ ∈ P, ∀ y₃ ∈ Q, G a₃ y₃ z ≠ G a₃ y₃ z' → False := by
    intro y hy y' hy' a₂ ha₂ z₂ hz₂ hd z hz z' hz' a₃ ha₃ y₃ hy₃ he
    have := L2 y hy y' hy' z hz z₂ hz₂ a₃ a₂
    have := L2 y hy y' hy' z' hz' z₂ hz₂ a₃ a₂
    have := L3 z hz z' hz' a₃ ha₃ a₃ ha₃ y y₃
    have := L3 z hz z' hz' a₃ ha₃ a₃ ha₃ y' y₃
    have := h01 a₂ y z₂; have := h01 a₂ y' z₂; have := h01 a₃ y₃ z; have := h01 a₃ y₃ z'
    have := h01 a₃ y z; have := h01 a₃ y' z; have := h01 a₃ y z'; have := h01 a₃ y' z'
    omega
  by_cases v2 : ∃ y ∈ Q, ∃ y' ∈ Q, ∃ a₂ ∈ P, ∃ z₂ ∈ T, G a₂ y z₂ ≠ G a₂ y' z₂
  · obtain ⟨y₀, hy₀, y₀', hy₀', a₂, ha₂, z₂, hz₂, hd⟩ := v2
    right; left
    intro y hy a ha a' ha' z hz z' hz'
    have e1 : G a y z = G a' y z := by
      by_contra h
      exact n12 a ha a' ha' y hy z hz h y₀ hy₀ y₀' hy₀' a₂ ha₂ z₂ hz₂ hd
    have e2 : G a' y z = G a' y z' := by
      by_contra h
      exact n23 y₀ hy₀ y₀' hy₀' a₂ ha₂ z₂ hz₂ hd z hz z' hz' a' ha' y hy h
    exact e1.trans e2
  · by_cases v1 : ∃ a ∈ P, ∃ a' ∈ P, ∃ y₁ ∈ Q, ∃ z₁ ∈ T, G a y₁ z₁ ≠ G a' y₁ z₁
    · obtain ⟨a₀, ha₀, a₀', ha₀', y₁, hy₁, z₁, hz₁, hc⟩ := v1
      left
      intro a ha y hy y' hy' z hz z' hz'
      have e1 : G a y z = G a y' z := by
        by_contra h
        exact v2 ⟨y, hy, y', hy', a, ha, z, hz, h⟩
      have e2 : G a y' z = G a y' z' := by
        by_contra h
        exact n13 a₀ ha₀ a₀' ha₀' y₁ hy₁ z₁ hz₁ hc z hz z' hz' a ha y' hy' h
      exact e1.trans e2
    · right; right
      intro z hz a ha a' ha' y hy y' hy'
      have e1 : G a y z = G a' y z := by
        by_contra h
        exact v1 ⟨a, ha, a', ha', y, hy, z, hz, h⟩
      have e2 : G a' y z = G a' y' z := by
        by_contra h
        exact v2 ⟨y, hy, y', hy', a', ha', z, hz, h⟩
      exact e1.trans e2

/-- Full lines of window `{0,1}` over parts labelled `→1` (coordinate 0) and `→0` (coordinate 1). -/
def W0 (E : Set Ω) (κ₀ κ₁ : ℕ → Prop) : Set Ω :=
  {x | κ₀ (x 0) ∧ ¬ κ₁ (x 1) ∧ ∀ z, sl E (x 0) (x 1) z = 1}
/-- Full lines of window `{1,2}` over parts labelled `→2` (coordinate 1) and `→1` (coordinate 2). -/
def W1 (E : Set Ω) (κ₁ κ₂ : ℕ → Prop) : Set Ω :=
  {x | κ₁ (x 1) ∧ ¬ κ₂ (x 2) ∧ ∀ a, sl E a (x 1) (x 2) = 1}
/-- Full lines of window `{2,0}` over parts labelled `→0` (coordinate 2) and `→2` (coordinate 0). -/
def W2 (E : Set Ω) (κ₂ κ₀ : ℕ → Prop) : Set Ω :=
  {x | κ₂ (x 2) ∧ ¬ κ₀ (x 0) ∧ ∀ y, sl E (x 0) y (x 2) = 1}
/-- The residue: what is left of `E` after removing the three families of full lines. -/
def Res (E : Set Ω) (κ₀ κ₁ κ₂ : ℕ → Prop) : Set Ω :=
  {x | sl E (x 0) (x 1) (x 2) = 1 ∧ x ∉ W0 E κ₀ κ₁ ∧ x ∉ W1 E κ₁ κ₂ ∧ x ∉ W2 E κ₂ κ₀}

/-- **Cells** (hand Step 3). In a cell `P × Q × T` of the three covers (`b₀ b₁ b₂` = the kinds of
the three parts), the residue depends on one coordinate only. -/
lemma cell_dep {E : Set Ω} {κ₀ κ₁ κ₂ : ℕ → Prop} {P Q T : Set ℕ} {b₀ b₁ b₂ : Prop}
    (hb₀ : ∀ a ∈ P, (κ₀ a ↔ b₀)) (hb₁ : ∀ y ∈ Q, (κ₁ y ↔ b₁)) (hb₂ : ∀ z ∈ T, (κ₂ z ↔ b₂))
    (c0t : b₀ → ∀ a ∈ P, ∀ a' ∈ P, ∀ y z z',
      sl E a y z - sl E a' y z = sl E a y z' - sl E a' y z')
    (c0f : ¬ b₀ → ∀ a ∈ P, ∀ a' ∈ P, ∀ z y y',
      sl E a y z - sl E a' y z = sl E a y' z - sl E a' y' z)
    (c1t : b₁ → ∀ y ∈ Q, ∀ y' ∈ Q, ∀ z a a',
      sl E a y z - sl E a y' z = sl E a' y z - sl E a' y' z)
    (c1f : ¬ b₁ → ∀ y ∈ Q, ∀ y' ∈ Q, ∀ a z z',
      sl E a y z - sl E a y' z = sl E a y z' - sl E a y' z')
    (c2t : b₂ → ∀ z ∈ T, ∀ z' ∈ T, ∀ a y y',
      sl E a y z - sl E a y z' = sl E a y' z - sl E a y' z')
    (c2f : ¬ b₂ → ∀ z ∈ T, ∀ z' ∈ T, ∀ y a a',
      sl E a y z - sl E a y z' = sl E a' y z - sl E a' y z') :
    (∀ x y : Ω, x 0 ∈ P → x 1 ∈ Q → x 2 ∈ T → y 0 ∈ P → y 1 ∈ Q → y 2 ∈ T → x 0 = y 0 →
      x ∈ Res E κ₀ κ₁ κ₂ → y ∈ Res E κ₀ κ₁ κ₂) ∨
    (∀ x y : Ω, x 0 ∈ P → x 1 ∈ Q → x 2 ∈ T → y 0 ∈ P → y 1 ∈ Q → y 2 ∈ T → x 1 = y 1 →
      x ∈ Res E κ₀ κ₁ κ₂ → y ∈ Res E κ₀ κ₁ κ₂) ∨
    (∀ x y : Ω, x 0 ∈ P → x 1 ∈ Q → x 2 ∈ T → y 0 ∈ P → y 1 ∈ Q → y 2 ∈ T → x 2 = y 2 →
      x ∈ Res E κ₀ κ₁ κ₂ → y ∈ Res E κ₀ κ₁ κ₂) := by
  have h01 := sl_cases E
  by_cases m01 : b₀ ∧ ¬ b₁
  · -- mutual pair {0,1}: depends on coordinate 2
    right; right
    rintro x y hx0 hx1 hx2 hy0 hy1 hy2 e ⟨hE, n0, n1, n2⟩
    have hz : ∃ z₀, sl E (x 0) (x 1) z₀ = 0 := by
      by_contra hcon
      push Not at hcon
      exact n0 ⟨(hb₀ _ hx0).mpr m01.1, fun h => m01.2 ((hb₁ _ hx1).mp h), fun z => by
        have := h01 (x 0) (x 1) z; have := hcon z; omega⟩
    obtain ⟨hy, z₀, hz₀⟩ := mutual_abs (G := sl E) h01 (c0t m01.1) (c1f m01.2)
      hx0 hy0 hx1 hy1 hE hz
    refine ⟨by rw [← e]; exact hy, fun h => ?_, fun h => m01.2 ((hb₁ _ hy1).mp h.1),
      fun h => h.2.1 ((hb₀ _ hy0).mpr m01.1)⟩
    have := h.2.2 z₀
    omega
  by_cases m12 : b₁ ∧ ¬ b₂
  · -- mutual pair {1,2}: depends on coordinate 0
    left
    rintro x y hx0 hx1 hx2 hy0 hy1 hy2 e ⟨hE, n0, n1, n2⟩
    have ha : ∃ a₀, sl E a₀ (x 1) (x 2) = 0 := by
      by_contra hcon
      push Not at hcon
      exact n1 ⟨(hb₁ _ hx1).mpr m12.1, fun h => m12.2 ((hb₂ _ hx2).mp h), fun a => by
        have := h01 a (x 1) (x 2); have := hcon a; omega⟩
    obtain ⟨hy, a₀, ha₀⟩ := mutual_abs (G := fun y z a => sl E a y z) (fun y z a => h01 a y z)
      (c1t m12.1) (c2f m12.2) hx1 hy1 hx2 hy2 hE ha
    have hy' : sl E (x 0) (y 1) (y 2) = 1 := hy
    have ha₀' : sl E a₀ (y 1) (y 2) = 0 := ha₀
    refine ⟨by rw [← e]; exact hy', fun h => h.2.1 ((hb₁ _ hy1).mpr m12.1), fun h => ?_,
      fun h => m12.2 ((hb₂ _ hy2).mp h.1)⟩
    have := h.2.2 a₀
    omega
  by_cases m20 : b₂ ∧ ¬ b₀
  · -- mutual pair {2,0}: depends on coordinate 1
    right; left
    rintro x y hx0 hx1 hx2 hy0 hy1 hy2 e ⟨hE, n0, n1, n2⟩
    have hyy : ∃ y₀, sl E (x 0) y₀ (x 2) = 0 := by
      by_contra hcon
      push Not at hcon
      exact n2 ⟨(hb₂ _ hx2).mpr m20.1, fun h => m20.2 ((hb₀ _ hx0).mp h), fun y => by
        have := h01 (x 0) y (x 2); have := hcon y; omega⟩
    obtain ⟨hy, y₀, hy₀⟩ := mutual_abs (G := fun z a y => sl E a y z) (fun z a y => h01 a y z)
      (c2t m20.1) (c0f m20.2) hx2 hy2 hx0 hy0 hE hyy
    have hy' : sl E (y 0) (x 1) (y 2) = 1 := hy
    have hy₀' : sl E (y 0) y₀ (y 2) = 0 := hy₀
    refine ⟨by rw [← e]; exact hy', fun h => m20.2 ((hb₀ _ hy0).mp h.1),
      fun h => h.2.1 ((hb₂ _ hy2).mpr m20.1), fun h => ?_⟩
    have := h.2.2 y₀
    omega
  -- cyclic cells: no `W` meets the cell
  have hres : ∀ y : Ω, y 0 ∈ P → y 1 ∈ Q → y 2 ∈ T → sl E (y 0) (y 1) (y 2) = 1 →
      y ∈ Res E κ₀ κ₁ κ₂ := by
    intro y hy0 hy1 hy2 h
    refine ⟨h, fun w => ?_, fun w => ?_, fun w => ?_⟩
    · exact m01 ⟨(hb₀ _ hy0).mp w.1, fun h => w.2.1 ((hb₁ _ hy1).mpr h)⟩
    · exact m12 ⟨(hb₁ _ hy1).mp w.1, fun h => w.2.1 ((hb₂ _ hy2).mpr h)⟩
    · exact m20 ⟨(hb₂ _ hy2).mp w.1, fun h => w.2.1 ((hb₀ _ hy0).mpr h)⟩
  by_cases t0 : b₀
  · have t1 : b₁ := by_contra fun h => m01 ⟨t0, h⟩
    have t2 : b₂ := by_contra fun h => m12 ⟨t1, h⟩
    rcases cyclic_abs (G := sl E) h01 (c0t t0) (c1t t1) (c2t t2) with h | h | h
    · left
      intro x y hx0 hx1 hx2 hy0 hy1 hy2 e hx
      apply hres y hy0 hy1 hy2
      rw [← e, ← h (x 0) hx0 (x 1) hx1 (y 1) hy1 (x 2) hx2 (y 2) hy2]
      exact hx.1
    · right; left
      intro x y hx0 hx1 hx2 hy0 hy1 hy2 e hx
      apply hres y hy0 hy1 hy2
      rw [← e, ← h (x 1) hx1 (x 0) hx0 (y 0) hy0 (x 2) hx2 (y 2) hy2]
      exact hx.1
    · right; right
      intro x y hx0 hx1 hx2 hy0 hy1 hy2 e hx
      apply hres y hy0 hy1 hy2
      rw [← e, ← h (x 2) hx2 (x 0) hx0 (y 0) hy0 (x 1) hx1 (y 1) hy1]
      exact hx.1
  · have t2 : ¬ b₂ := fun h => m20 ⟨h, t0⟩
    have t1 : ¬ b₁ := fun h => m12 ⟨h, t2⟩
    rcases cyclic_abs (G := fun a z y => sl E a y z) (fun a z y => h01 a y z)
      (c0f t0) (c2f t2) (c1f t1) with h | h | h
    · left
      intro x y hx0 hx1 hx2 hy0 hy1 hy2 e hx
      apply hres y hy0 hy1 hy2
      have k : sl E (x 0) (x 1) (x 2) = sl E (x 0) (y 1) (y 2) :=
        h (x 0) hx0 (x 2) hx2 (y 2) hy2 (x 1) hx1 (y 1) hy1
      rw [← e, ← k]
      exact hx.1
    · right; right
      intro x y hx0 hx1 hx2 hy0 hy1 hy2 e hx
      apply hres y hy0 hy1 hy2
      have k : sl E (x 0) (x 1) (x 2) = sl E (y 0) (y 1) (x 2) :=
        h (x 2) hx2 (x 0) hx0 (y 0) hy0 (x 1) hx1 (y 1) hy1
      rw [← e, ← k]
      exact hx.1
    · right; left
      intro x y hx0 hx1 hx2 hy0 hy1 hy2 e hx
      apply hres y hy0 hy1 hy2
      have k : sl E (x 0) (x 1) (x 2) = sl E (y 0) (x 1) (y 2) :=
        h (x 1) hx1 (x 0) hx0 (y 0) hy0 (x 2) hx2 (y 2) hy2
      rw [← e, ← k]
      exact hx.1

/-- **Step 3 (hand: "Columns and residue", with Fix 1).** A box set with a finite labelled cover
at each coordinate is a disjoint union of three window events and a residue that factors through a
finite coordinatewise quotient. (`hB` is not used; kept because it is available at the call site.)

`W₀` = full lines of window `{0,1}` over parts labelled `→1` / `→0` (`W0`), `W₁`, `W₂` likewise
(`W1`, `W2`); `R = Res`. Finiteness of `R`: in each cell of the three covers `R` depends on one
coordinate only (`cell_dep`: a mutual pair by `mutual_abs`, a cyclic cell by `cyclic_abs`); the
labels are the cover labels refined by the traces of `R` on lines through class representatives
(Fix 1). -/
theorem residue {E : Set Ω} (hB : Box E) (hc : ∀ i, Cover i E) :
    ∃ W₀ W₁ W₂ R : Set Ω, W₀ ∈ gens ∧ W₁ ∈ gens ∧ W₂ ∈ gens ∧
      Disjoint W₀ W₁ ∧ Disjoint W₀ W₂ ∧ Disjoint W₁ W₂ ∧ Disjoint (W₀ ∪ W₁ ∪ W₂) R ∧
      E = W₀ ∪ W₁ ∪ W₂ ∪ R ∧ FinDet R := by
  obtain ⟨n₀, lab₀, k₀, c0⟩ := hc 0
  obtain ⟨n₁, lab₁, k₁, c1⟩ := hc 1
  obtain ⟨n₂, lab₂, k₂, c2⟩ := hc 2
  obtain ⟨κ₀, hκ₀⟩ : ∃ κ₀ : ℕ → Prop, ∀ a, κ₀ a ↔ k₀ (lab₀ a) = true := ⟨_, fun _ => Iff.rfl⟩
  obtain ⟨κ₁, hκ₁⟩ : ∃ κ₁ : ℕ → Prop, ∀ a, κ₁ a ↔ k₁ (lab₁ a) = true := ⟨_, fun _ => Iff.rfl⟩
  obtain ⟨κ₂, hκ₂⟩ : ∃ κ₂ : ℕ → Prop, ∀ a, κ₂ a ↔ k₂ (lab₂ a) = true := ⟨_, fun _ => Iff.rfl⟩
  refine ⟨W0 E κ₀ κ₁, W1 E κ₁ κ₂, W2 E κ₂ κ₀, Res E κ₀ κ₁ κ₂, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · exact gens01 fun x y h0 h1 hx => by
      unfold W0 at hx ⊢; rw [mem_setOf_eq] at hx ⊢; rw [← h0, ← h1]; exact hx
  · exact gens12 fun x y h1 h2 hx => by
      unfold W1 at hx ⊢; rw [mem_setOf_eq] at hx ⊢; rw [← h1, ← h2]; exact hx
  · exact gens20 fun x y h2 h0 hx => by
      unfold W2 at hx ⊢; rw [mem_setOf_eq] at hx ⊢; rw [← h0, ← h2]; exact hx
  · exact Set.disjoint_left.mpr fun x h h' => h.2.1 h'.1
  · exact Set.disjoint_left.mpr fun x h h' => h'.2.1 h.1
  · exact Set.disjoint_left.mpr fun x h h' => h.2.1 h'.1
  · refine Set.disjoint_left.mpr fun x h h' => ?_
    rcases h with (h | h) | h
    · exact h'.2.1 h
    · exact h'.2.2.1 h
    · exact h'.2.2.2 h
  · ext x
    rw [mem_iff_sl]
    constructor
    · intro h
      by_cases w0 : x ∈ W0 E κ₀ κ₁
      · exact Or.inl (Or.inl (Or.inl w0))
      by_cases w1 : x ∈ W1 E κ₁ κ₂
      · exact Or.inl (Or.inl (Or.inr w1))
      by_cases w2 : x ∈ W2 E κ₂ κ₀
      · exact Or.inl (Or.inr w2)
      exact Or.inr ⟨h, w0, w1, w2⟩
    · rintro (((h | h) | h) | h)
      · exact h.2.2 (x 2)
      · exact h.2.2 (x 0)
      · exact h.2.2 (x 1)
      · exact h.1
  · -- the residue is determined by finitely many labels
    obtain ⟨rep₀, hrep₀⟩ := exists_rep lab₀
    obtain ⟨rep₁, hrep₁⟩ := exists_rep lab₁
    obtain ⟨rep₂, hrep₂⟩ := exists_rep lab₂
    refine finDet_of_finite
      (fun v => (lab₀ v, {j : Fin n₁ × Fin n₂ | ![v, rep₁ j.1, rep₂ j.2] ∈ Res E κ₀ κ₁ κ₂}))
      (fun v => (lab₁ v, {j : Fin n₀ × Fin n₂ | ![rep₀ j.1, v, rep₂ j.2] ∈ Res E κ₀ κ₁ κ₂}))
      (fun v => (lab₂ v, {j : Fin n₀ × Fin n₁ | ![rep₀ j.1, rep₁ j.2, v] ∈ Res E κ₀ κ₁ κ₂}))
      ?_
    intro x y h0 h1 h2 hx
    have e0 : lab₀ (x 0) = lab₀ (y 0) := congrArg Prod.fst h0
    have e1 : lab₁ (x 1) = lab₁ (y 1) := congrArg Prod.fst h1
    have e2 : lab₂ (x 2) = lab₂ (y 2) := congrArg Prod.fst h2
    have s0 : ∀ j : Fin n₁ × Fin n₂, ![x 0, rep₁ j.1, rep₂ j.2] ∈ Res E κ₀ κ₁ κ₂ →
        ![y 0, rep₁ j.1, rep₂ j.2] ∈ Res E κ₀ κ₁ κ₂ := fun j hj => by
      have := congrArg Prod.snd h0
      exact (Set.ext_iff.mp this j).mp hj
    have s1 : ∀ j : Fin n₀ × Fin n₂, ![rep₀ j.1, x 1, rep₂ j.2] ∈ Res E κ₀ κ₁ κ₂ →
        ![rep₀ j.1, y 1, rep₂ j.2] ∈ Res E κ₀ κ₁ κ₂ := fun j hj => by
      have := congrArg Prod.snd h1
      exact (Set.ext_iff.mp this j).mp hj
    have s2 : ∀ j : Fin n₀ × Fin n₁, ![rep₀ j.1, rep₁ j.2, x 2] ∈ Res E κ₀ κ₁ κ₂ →
        ![rep₀ j.1, rep₁ j.2, y 2] ∈ Res E κ₀ κ₁ κ₂ := fun j hj => by
      have := congrArg Prod.snd h2
      exact (Set.ext_iff.mp this j).mp hj
    have key := cell_dep (E := E) (κ₀ := κ₀) (κ₁ := κ₁) (κ₂ := κ₂)
      (P := {a | lab₀ a = lab₀ (x 0)}) (Q := {b | lab₁ b = lab₁ (x 1)})
      (T := {c | lab₂ c = lab₂ (x 2)}) (b₀ := k₀ (lab₀ (x 0)) = true)
      (b₁ := k₁ (lab₁ (x 1)) = true) (b₂ := k₂ (lab₂ (x 2)) = true)
      (fun a ha => by rw [hκ₀, show lab₀ a = lab₀ (x 0) from ha])
      (fun a ha => by rw [hκ₁, show lab₁ a = lab₁ (x 1) from ha])
      (fun a ha => by rw [hκ₂, show lab₂ a = lab₂ (x 2) from ha])
      (fun hk a ha a' ha' y z z' =>
        (c0 a a' (ha.trans ha'.symm)).1 (by rw [show lab₀ a = lab₀ (x 0) from ha]; exact hk) y z z')
      (fun hk a ha a' ha' z y y' =>
        (c0 a a' (ha.trans ha'.symm)).2
          (by rw [show lab₀ a = lab₀ (x 0) from ha]; simpa using hk) y y' z)
      (fun hk b hb b' hb' z a a' =>
        (c1 b b' (hb.trans hb'.symm)).1 (by rw [show lab₁ b = lab₁ (x 1) from hb]; exact hk) z a a')
      (fun hk b hb b' hb' a z z' =>
        (c1 b b' (hb.trans hb'.symm)).2
          (by rw [show lab₁ b = lab₁ (x 1) from hb]; simpa using hk) z z' a)
      (fun hk c hc c' hc' a y y' =>
        (c2 c c' (hc.trans hc'.symm)).1 (by rw [show lab₂ c = lab₂ (x 2) from hc]; exact hk) a y y')
      (fun hk c hc c' hc' y a a' =>
        (c2 c c' (hc.trans hc'.symm)).2
          (by rw [show lab₂ c = lab₂ (x 2) from hc]; simpa using hk) a a' y)
    rcases key with D | D | D
    · have m1 := D x ![x 0, rep₁ (lab₁ (x 1)), rep₂ (lab₂ (x 2))] rfl rfl rfl rfl
        (hrep₁ (x 1)) (hrep₂ (x 2)) rfl hx
      have m2 := s0 (lab₁ (x 1), lab₂ (x 2)) m1
      exact D ![y 0, rep₁ (lab₁ (x 1)), rep₂ (lab₂ (x 2))] y e0.symm (hrep₁ (x 1)) (hrep₂ (x 2))
        e0.symm e1.symm e2.symm rfl m2
    · have m1 := D x ![rep₀ (lab₀ (x 0)), x 1, rep₂ (lab₂ (x 2))] rfl rfl rfl
        (hrep₀ (x 0)) rfl (hrep₂ (x 2)) rfl hx
      have m2 := s1 (lab₀ (x 0), lab₂ (x 2)) m1
      exact D ![rep₀ (lab₀ (x 0)), y 1, rep₂ (lab₂ (x 2))] y (hrep₀ (x 0)) e1.symm (hrep₂ (x 2))
        e0.symm e1.symm e2.symm rfl m2
    · have m1 := D x ![rep₀ (lab₀ (x 0)), rep₁ (lab₁ (x 1)), x 2] rfl rfl rfl
        (hrep₀ (x 0)) (hrep₁ (x 1)) rfl rfl hx
      have m2 := s2 (lab₀ (x 0), lab₁ (x 1)) m1
      exact D ![rep₀ (lab₀ (x 0)), rep₁ (lab₁ (x 1)), y 2] y (hrep₀ (x 0)) (hrep₁ (x 1)) e2.symm
        e0.symm e1.symm e2.symm rfl m2

/-! ## Step 4. Finite grids -/

lemma cnt_cases (E : Set Ω) (p : Ω) : (p ∈ E ∧ cnt E p = 1) ∨ (p ∉ E ∧ cnt E p = 0) := by
  by_cases h : p ∈ E
  · exact Or.inl ⟨h, by simp [cnt, h]⟩
  · exact Or.inr ⟨h, by simp [cnt, h]⟩

lemma cnt_sl (R : Set Ω) (x : Ω) : (cnt R x : ℤ) = sl R (x 0) (x 1) (x 2) := by
  unfold sl; rw [← eta x]

/-- Indicator of a proposition, as an integer. -/
noncomputable def bi (p : Prop) : ℤ := by
  classical exact if p then 1 else 0

lemma bi_pos {p : Prop} (h : p) : bi p = 1 := by simp [bi, h]
lemma bi_neg {p : Prop} (h : ¬ p) : bi p = 0 := by simp [bi, h]

/-- Correcting a finitary set by two window events: remove `S` (contained), then add `T`. -/
lemma dfin_adj1 {R R' S T : Set Ω} (hR' : Dfin R') (hS : S ∈ gens) (hT : T ∈ gens)
    (hid : ∀ x, (cnt R x : ℤ) + cnt S x = cnt R' x + cnt T x) (hSR : S ⊆ R') : Dfin R := by
  have key : ∀ x, x ∈ R ↔ x ∈ (R' \ S) ∪ T := by
    intro x
    have h := hid x
    have hS' : x ∈ S → x ∈ R' := fun h => hSR h
    rcases cnt_cases R x with ⟨h1, e1⟩ | ⟨h1, e1⟩ <;>
    rcases cnt_cases R' x with ⟨h2, e2⟩ | ⟨h2, e2⟩ <;>
    rcases cnt_cases S x with ⟨h3, e3⟩ | ⟨h3, e3⟩ <;>
    rcases cnt_cases T x with ⟨h4, e4⟩ | ⟨h4, e4⟩ <;>
    first
      | (exfalso; omega)
      | (simp only [mem_union, mem_diff]; tauto)
  have hd : Disjoint (R' \ S) T := by
    rw [Set.disjoint_left]
    rintro x ⟨hx, hxS⟩ hxT
    have h := hid x
    have := cnt_le R x
    rcases cnt_cases R' x with ⟨h2, e2⟩ | ⟨h2, e2⟩
    · rcases cnt_cases S x with ⟨h3, e3⟩ | ⟨h3, e3⟩
      · exact hxS h3
      · rcases cnt_cases T x with ⟨h4, e4⟩ | ⟨h4, e4⟩
        · omega
        · exact h4 hxT
    · exact h2 hx
  rw [Set.ext key]
  exact Dfin.union (dfin_diff hR' (Dfin.basic hS) hSR) (Dfin.basic hT) hd

/-- Correcting a finitary set by two window events: add `T` (disjoint), then remove `S`. -/
lemma dfin_adj2 {R R' S T : Set Ω} (hR' : Dfin R') (hS : S ∈ gens) (hT : T ∈ gens)
    (hid : ∀ x, (cnt R x : ℤ) + cnt S x = cnt R' x + cnt T x) (hd : Disjoint R' T) : Dfin R := by
  have hd' : ∀ x, x ∈ R' → x ∈ T → False := fun x h h' => Set.disjoint_left.mp hd h h'
  have key : ∀ x, x ∈ R ↔ x ∈ (R' ∪ T) \ S := by
    intro x
    have h := hid x
    have := hd' x
    rcases cnt_cases R x with ⟨h1, e1⟩ | ⟨h1, e1⟩ <;>
    rcases cnt_cases R' x with ⟨h2, e2⟩ | ⟨h2, e2⟩ <;>
    rcases cnt_cases S x with ⟨h3, e3⟩ | ⟨h3, e3⟩ <;>
    rcases cnt_cases T x with ⟨h4, e4⟩ | ⟨h4, e4⟩ <;>
    first
      | (exfalso; omega)
      | (simp only [mem_union, mem_diff]; tauto)
  have hsub : S ⊆ R' ∪ T := by
    intro x hxS
    have h := hid x
    rcases cnt_cases R' x with ⟨h2, e2⟩ | ⟨h2, e2⟩
    · exact Or.inl h2
    · rcases cnt_cases T x with ⟨h4, e4⟩ | ⟨h4, e4⟩
      · exact Or.inr h4
      · rcases cnt_cases S x with ⟨h3, e3⟩ | ⟨h3, e3⟩
        · omega
        · exact absurd hxS h3
  rw [Set.ext key]
  exact dfin_diff (Dfin.union hR' (Dfin.basic hT) hd) (Dfin.basic hS) hsub

/-- `R` is determined by ℕ-valued labels, one labelling per coordinate, with values in finite
sets `S0 S1 S2`. -/
def LabDet (S0 S1 S2 : Finset ℕ) (l0 l1 l2 : ℕ → ℕ) (R : Set Ω) : Prop :=
  (∀ x, l0 x ∈ S0) ∧ (∀ x, l1 x ∈ S1) ∧ (∀ x, l2 x ∈ S2) ∧
    ∀ x y : Ω, l0 (x 0) = l0 (y 0) → l1 (x 1) = l1 (y 1) → l2 (x 2) = l2 (y 2) → x ∈ R → y ∈ R

/-- `R` is determined by labels with at most `N` label values in total. -/
def DetN (N : ℕ) (R : Set Ω) : Prop :=
  ∃ (S0 S1 S2 : Finset ℕ) (l0 l1 l2 : ℕ → ℕ),
    LabDet S0 S1 S2 l0 l1 l2 R ∧ S0.card + S1.card + S2.card ≤ N

section Grid

variable {S0 S1 S2 : Finset ℕ} {l0 l1 l2 : ℕ → ℕ} {R : Set Ω}

lemma labdet_sl (hD : LabDet S0 S1 S2 l0 l1 l2 R) {a a' y y' z z' : ℕ}
    (h0 : l0 a = l0 a') (h1 : l1 y = l1 y') (h2 : l2 z = l2 z') :
    sl R a y z = sl R a' y' z' := by
  unfold sl
  congr 1
  exact cnt_congr ⟨hD.2.2.2 ![a, y, z] ![a', y', z'] h0 h1 h2,
    hD.2.2.2 ![a', y', z'] ![a, y, z] h0.symm h1.symm h2.symm⟩

lemma labdet_rot (hD : LabDet S0 S1 S2 l0 l1 l2 R) : LabDet S1 S2 S0 l1 l2 l0 (rot ⁻¹' R) :=
  ⟨hD.2.1, hD.2.2.1, hD.1, fun x y h0 h1 h2 hx => hD.2.2.2 (rot x) (rot y) h2 h0 h1 hx⟩

/-- The collapse map: send the `l0`-class of `a` to the value `b`. -/
def coll (l0 : ℕ → ℕ) (a b : ℕ) (x : ℕ) : ℕ := if l0 x = l0 a then b else x

/-- **Merge, induction side.** Collapsing one label class of coordinate 0 onto a value of another
class gives a box set with fewer labels, finitary by the induction hypothesis. -/
lemma merged_dfin {N : ℕ} (IH : ∀ R : Set Ω, Box R → DetN N R → Dfin R) (hB : Box R)
    (hD : LabDet S0 S1 S2 l0 l1 l2 R) (hN : S0.card + S1.card + S2.card ≤ N + 1) {a b : ℕ}
    (hab : l0 a ≠ l0 b) : Dfin (cw ![coll l0 a b, id, id] ⁻¹' R) := by
  apply IH _ (box_cw _ hB)
  refine ⟨S0.erase (l0 a), S1, S2, fun x => l0 (coll l0 a b x), l1, l2,
    ⟨?_, hD.2.1, hD.2.2.1, ?_⟩, ?_⟩
  · intro x
    rw [Finset.mem_erase]
    refine ⟨?_, hD.1 _⟩
    show l0 (coll l0 a b x) ≠ l0 a
    unfold coll
    split_ifs with h
    · exact fun e => hab e.symm
    · exact h
  · intro x y h0 h1 h2 hx
    rw [mem_preimage, cw_vec] at hx ⊢
    exact hD.2.2.2 ![coll l0 a b (x 0), id (x 1), id (x 2)]
      ![coll l0 a b (y 0), id (y 1), id (y 2)] h0 h1 h2 hx
  · have := Finset.card_erase_of_mem (hD.1 a)
    have := Finset.card_pos.mpr ⟨_, hD.1 a⟩
    omega

/-- **Merge, correction side.** If the slices of `a` and `b` differ by `[q] − [p]`, where `p`
and `q` give window events over the class of `a`, and the `b`-slice is full on `p` or empty on
`q`, then `R` is recovered from the collapsed set by removing and adding two window events. -/
lemma merge_apply (hD : LabDet S0 S1 S2 l0 l1 l2 R) {a b : ℕ}
    (hR' : Dfin (cw ![coll l0 a b, id, id] ⁻¹' R)) {p q : ℕ → ℕ → Prop}
    (hS : {x : Ω | l0 (x 0) = l0 a ∧ p (x 1) (x 2)} ∈ gens)
    (hT : {x : Ω | l0 (x 0) = l0 a ∧ q (x 1) (x 2)} ∈ gens)
    (hid : ∀ y z, sl R a y z + bi (p y z) = sl R b y z + bi (q y z))
    (hcase : (∀ y z, p y z → sl R b y z = 1) ∨ (∀ y z, q y z → sl R b y z = 0)) : Dfin R := by
  have hin : ∀ x : Ω, l0 (x 0) = l0 a →
      (cnt (cw ![coll l0 a b, id, id] ⁻¹' R) x : ℤ) = sl R b (x 1) (x 2) := by
    intro x hx
    show (cnt R (cw ![coll l0 a b, id, id] x) : ℤ) = _
    rw [cw_vec]
    unfold sl coll
    rw [if_pos hx]
    rfl
  have hout : ∀ x : Ω, l0 (x 0) ≠ l0 a →
      (cnt (cw ![coll l0 a b, id, id] ⁻¹' R) x : ℤ) = cnt R x := by
    intro x hx
    show (cnt R (cw ![coll l0 a b, id, id] x) : ℤ) = _
    rw [cw_vec]
    unfold coll
    rw [if_neg hx]
    show (cnt R ![x 0, x 1, x 2] : ℤ) = _
    rw [← eta x]
  have hcnt : ∀ x, (cnt R x : ℤ) + cnt {x : Ω | l0 (x 0) = l0 a ∧ p (x 1) (x 2)} x =
      cnt (cw ![coll l0 a b, id, id] ⁻¹' R) x + cnt {x : Ω | l0 (x 0) = l0 a ∧ q (x 1) (x 2)} x := by
    intro x
    by_cases hx : l0 (x 0) = l0 a
    · have e := hid (x 1) (x 2)
      have e1 : (cnt R x : ℤ) = sl R a (x 1) (x 2) := by
        rw [cnt_sl]; exact labdet_sl hD hx rfl rfl
      have e2 : (cnt {x : Ω | l0 (x 0) = l0 a ∧ p (x 1) (x 2)} x : ℤ) = bi (p (x 1) (x 2)) := by
        by_cases hp : p (x 1) (x 2)
        · rw [bi_pos hp]; simp [cnt, hx, hp]
        · rw [bi_neg hp]; simp [cnt, hp]
      have e3 : (cnt {x : Ω | l0 (x 0) = l0 a ∧ q (x 1) (x 2)} x : ℤ) = bi (q (x 1) (x 2)) := by
        by_cases hq : q (x 1) (x 2)
        · rw [bi_pos hq]; simp [cnt, hx, hq]
        · rw [bi_neg hq]; simp [cnt, hq]
      rw [e1, e2, e3, hin x hx]
      exact e
    · have e2 : cnt {x : Ω | l0 (x 0) = l0 a ∧ p (x 1) (x 2)} x = 0 := by simp [cnt, hx]
      have e3 : cnt {x : Ω | l0 (x 0) = l0 a ∧ q (x 1) (x 2)} x = 0 := by simp [cnt, hx]
      rw [e2, e3, hout x hx]
  rcases hcase with hc | hc
  · refine dfin_adj1 hR' hS hT hcnt ?_
    rintro x ⟨hx, hp⟩
    have h1 := hin x hx
    rw [hc _ _ hp] at h1
    rcases cnt_cases (cw ![coll l0 a b, id, id] ⁻¹' R) x with ⟨h, -⟩ | ⟨-, e⟩
    · exact h
    · rw [e] at h1; simp at h1
  · refine dfin_adj2 hR' hS hT hcnt ?_
    rw [Set.disjoint_left]
    rintro x hxR ⟨hx, hq⟩
    have h1 := hin x hx
    rw [hc _ _ hq] at h1
    rcases cnt_cases (cw ![coll l0 a b, id, id] ⁻¹' R) x with ⟨-, e⟩ | ⟨h, -⟩
    · rw [e] at h1; simp at h1
    · exact h hxR

/-- **Merge (hand "Merge").** Two label classes of coordinate 0 that are not K-related can be
merged. -/
lemma step0 {N : ℕ} (IH : ∀ R : Set Ω, Box R → DetN N R → Dfin R) (hB : Box R)
    (hD : LabDet S0 S1 S2 l0 l1 l2 R) (hN : S0.card + S1.card + S2.card ≤ N + 1) {a b : ℕ}
    (hab : l0 a ≠ l0 b) (hK : ¬ KRel R a b) : Dfin R := by
  have hR' := merged_dfin IH hB hD hN hab
  have hK' : Eq1 R a b ∨ Eq2 R a b := by
    unfold KRel at hK; tauto
  rcases hK' with h1 | h2
  · refine merge_apply hD hR' (p := fun y _ => dif R a b y 0 = -1)
      (q := fun y _ => dif R a b y 0 = 1) ?_ ?_ ?_ (Or.inl ?_)
    · exact gens01 fun x y h0 h1 hx => by
        rw [mem_setOf_eq] at hx ⊢; rw [← h0, ← h1]; exact hx
    · exact gens01 fun x y h0 h1 hx => by
        rw [mem_setOf_eq] at hx ⊢; rw [← h0, ← h1]; exact hx
    · intro y z
      beta_reduce
      have e : sl R a y z - sl R b y z = dif R a b y 0 := h1 y z 0
      have r := dif_range R a b y 0
      by_cases c1 : dif R a b y 0 = -1
      · rw [bi_pos c1, bi_neg (by omega)]; omega
      · by_cases c2 : dif R a b y 0 = 1
        · rw [bi_neg c1, bi_pos c2]; omega
        · rw [bi_neg c1, bi_neg c2]; omega
    · intro y z hp
      have e : sl R a y z - sl R b y z = dif R a b y 0 := h1 y z 0
      have := sl_cases R a y z; have := sl_cases R b y z
      omega
  · refine merge_apply hD hR' (p := fun _ z => dif R a b 0 z = -1)
      (q := fun _ z => dif R a b 0 z = 1) ?_ ?_ ?_ (Or.inl ?_)
    · exact gens20 fun x y h2 h0 hx => by
        rw [mem_setOf_eq] at hx ⊢; rw [← h0, ← h2]; exact hx
    · exact gens20 fun x y h2 h0 hx => by
        rw [mem_setOf_eq] at hx ⊢; rw [← h0, ← h2]; exact hx
    · intro y z
      beta_reduce
      have e : sl R a y z - sl R b y z = dif R a b 0 z := h2 y 0 z
      have r := dif_range R a b 0 z
      by_cases c1 : dif R a b 0 z = -1
      · rw [bi_pos c1, bi_neg (by omega)]; omega
      · by_cases c2 : dif R a b 0 z = 1
        · rw [bi_neg c1, bi_pos c2]; omega
        · rw [bi_neg c1, bi_neg c2]; omega
    · intro y z hp
      have e : sl R a y z - sl R b y z = dif R a b 0 z := h2 y 0 z
      have := sl_cases R a y z; have := sl_cases R b y z
      omega

/-- Comparability of the K forms of two values against a common base (the "Chain" of Step 1). -/
lemma krel_cmp {E : Set Ω} (hB : Box E) {m n q : ℕ} (hm : KRel E m q) (hn : KRel E n q)
    (hmn : KRel E m n) :
    (Uof (dif E m q) ⊂ Uof (dif E n q) ∧ Vof (dif E n q) ⊂ Vof (dif E m q)) ∨
      (Uof (dif E n q) ⊂ Uof (dif E m q) ∧ Vof (dif E m q) ⊂ Vof (dif E n q)) := by
  have key : ∀ y z, dif E m n y z =
      (ind (Uof (dif E m q)) y - ind (Uof (dif E n q)) y) +
        (ind (Vof (dif E m q)) z - ind (Vof (dif E n q)) z) := by
    intro y z
    have h1 := krel_form hB hm y z
    have h2 := krel_form hB hn y z
    rw [dif_def] at h1 h2 ⊢
    omega
  apply chain_cmp
  · intro y z; rw [← key]; exact dif_range _ _ _ _ _
  · have h2 := hmn.2
    unfold Eq2 at h2
    push Not at h2
    obtain ⟨y, y', z, h⟩ := h2
    rw [key, key] at h
    exact ⟨y, y', fun e => h (by omega)⟩
  · have h1 := hmn.1
    unfold Eq1 at h1
    push Not at h1
    obtain ⟨y, z, z', h⟩ := h1
    rw [key, key] at h
    exact ⟨z, z', fun e => h (by omega)⟩

/-- **All-K case, the adjacent pair** (replaces hand Fix 2). If all label classes are pairwise
K-related at coordinate 0, and K-relatedness holds between distinct classes at coordinates 1 and 2
(used in the contrapositive forms `H1`, `H2`), then for a fixed base `b` the value `a` whose
`U`-set is minimal has `U × Vᶜ` inside a single cell: the `b`-slice is constant there. -/
lemma allK_pair (hB : Box R) (hD : LabDet S0 S1 S2 l0 l1 l2 R)
    (H0 : ∀ a a', l0 a ≠ l0 a' → KRel R a a')
    (H1 : ∀ y y', (∀ z a a', sl R a y z - sl R a y' z = sl R a' y z - sl R a' y' z) →
      l1 y = l1 y')
    (H2 : ∀ z z', (∀ y a a', sl R a y z - sl R a y z' = sl R a' y z - sl R a' y z') →
      l2 z = l2 z')
    {a₀ b : ℕ} (hne : l0 a₀ ≠ l0 b) :
    ∃ a, l0 a ≠ l0 b ∧ ∀ y ∈ Uof (dif R a b), ∀ z ∉ Vof (dif R a b),
      ∀ y' ∈ Uof (dif R a b), ∀ z' ∉ Vof (dif R a b), sl R b y z = sl R b y' z' := by
  have hsame : ∀ a a', l0 a = l0 a' → dif R a b = dif R a' b := by
    intro a a' h
    funext y z
    rw [dif_def, dif_def, labdet_sl hD h rfl rfl]
  have hfin : ((fun a => Uof (dif R a b)) '' {a | l0 a ≠ l0 b}).Finite := by
    refine (S0.finite_toSet.image
      fun l => {y | ∃ a', l0 a' = l ∧ y ∈ Uof (dif R a' b)}).subset ?_
    rintro _ ⟨a, -, rfl⟩
    refine ⟨l0 a, hD.1 a, ?_⟩
    ext y
    constructor
    · rintro ⟨a', ha', hy⟩
      rwa [hsame a' a ha'] at hy
    · intro hy
      exact ⟨a, rfl, hy⟩
  obtain ⟨a, ha, hmin⟩ := Set.Finite.exists_minimalFor' (fun a => Uof (dif R a b))
    {a | l0 a ≠ l0 b} hfin ⟨a₀, hne⟩
  have ha' : l0 a ≠ l0 b := ha
  have hKa : KRel R a b := H0 a b ha'
  have form : ∀ a', l0 a' ≠ l0 b → ∀ y z, sl R a' y z =
      sl R b y z + ind (Uof (dif R a' b)) y + ind (Vof (dif R a' b)) z - 1 := by
    intro a' h y z
    have := krel_form hB (H0 a' b h) y z
    rw [dif_def] at this
    omega
  have hsub : ∀ a', l0 a' ≠ l0 b →
      Uof (dif R a b) ⊆ Uof (dif R a' b) ∧ Vof (dif R a' b) ⊆ Vof (dif R a b) := by
    intro a' h
    by_cases e : l0 a' = l0 a
    · rw [hsame a' a e]
      exact ⟨subset_rfl, subset_rfl⟩
    · rcases krel_cmp hB (H0 a' b h) hKa (H0 a' a e) with h' | h'
      · exact absurd (hmin (j := a') h h'.1.1) h'.1.2
      · exact ⟨h'.1.1, h'.2.1⟩
  -- on `U × Vᶜ` the set does not depend on coordinate 0
  have c1 : ∀ a' y z, y ∈ Uof (dif R a b) → z ∉ Vof (dif R a b) → sl R a' y z = sl R b y z := by
    intro a' y z hy hz
    by_cases e : l0 a' = l0 b
    · exact labdet_sl hD e rfl rfl
    · have f := form a' e y z
      have := ind_pos ((hsub a' e).1 hy)
      have := ind_neg (fun h => hz ((hsub a' e).2 h))
      omega
  -- on `U × V` the set does not depend on coordinate 1
  have c2 : ∀ a' y y' z, y ∈ Uof (dif R a b) → y' ∈ Uof (dif R a b) → z ∈ Vof (dif R a b) →
      sl R a' y z = sl R a' y' z := by
    intro a' y y' z hy hy' hz
    have fa := form a ha' y z
    have fa' := form a ha' y' z
    have := ind_pos hy; have := ind_pos hy'; have := ind_pos hz
    have := sl_cases R a y z; have := sl_cases R a y' z
    have := sl_cases R b y z; have := sl_cases R b y' z
    by_cases e : l0 a' = l0 b
    · have := labdet_sl hD (y := y) (y' := y) (z := z) (z' := z) e rfl rfl
      have := labdet_sl hD (y := y') (y' := y') (z := z) (z' := z) e rfl rfl
      omega
    · have f := form a' e y z
      have f' := form a' e y' z
      have := ind_pos ((hsub a' e).1 hy)
      have := ind_pos ((hsub a' e).1 hy')
      omega
  -- on `Uᶜ × Vᶜ` the set does not depend on coordinate 2
  have c3 : ∀ a' y z z', y ∉ Uof (dif R a b) → z ∉ Vof (dif R a b) → z' ∉ Vof (dif R a b) →
      sl R a' y z = sl R a' y z' := by
    intro a' y z z' hy hz hz'
    have fa := form a ha' y z
    have fa' := form a ha' y z'
    have := ind_neg hy; have := ind_neg hz; have := ind_neg hz'
    have := sl_cases R a y z; have := sl_cases R a y z'
    have := sl_cases R b y z; have := sl_cases R b y z'
    by_cases e : l0 a' = l0 b
    · have := labdet_sl hD (y := y) (y' := y) (z := z) (z' := z) e rfl rfl
      have := labdet_sl hD (y := y) (y' := y) (z := z') (z' := z') e rfl rfl
      omega
    · have f := form a' e y z
      have f' := form a' e y z'
      have := ind_neg (fun h => hz ((hsub a' e).2 h))
      have := ind_neg (fun h => hz' ((hsub a' e).2 h))
      omega
  have hl1 : ∀ y y', y ∈ Uof (dif R a b) → y' ∈ Uof (dif R a b) → l1 y = l1 y' := by
    intro y y' hy hy'
    apply H1
    intro z a' a''
    by_cases hz : z ∈ Vof (dif R a b)
    · have := c2 a' y y' z hy hy' hz
      have := c2 a'' y y' z hy hy' hz
      omega
    · have := c1 a' y z hy hz; have := c1 a' y' z hy' hz
      have := c1 a'' y z hy hz; have := c1 a'' y' z hy' hz
      omega
  have hl2 : ∀ z z', z ∉ Vof (dif R a b) → z' ∉ Vof (dif R a b) → l2 z = l2 z' := by
    intro z z' hz hz'
    apply H2
    intro y a' a''
    by_cases hy : y ∈ Uof (dif R a b)
    · have := c1 a' y z hy hz; have := c1 a' y z' hy hz'
      have := c1 a'' y z hy hz; have := c1 a'' y z' hy hz'
      omega
    · have := c3 a' y z z' hy hz hz'
      have := c3 a'' y z z' hy hz hz'
      omega
  exact ⟨a, ha', fun y hy z hz y' hy' z' hz' =>
    labdet_sl hD rfl (hl1 y y' hy hy') (hl2 z z' hz hz')⟩

/-- **All-K case (hand "Swap", replacing Fixes 2–3).** If distinct label classes are K-related at
every coordinate, the adjacent pair of `allK_pair` can be merged at the cost of one window event
removed and one added. -/
lemma stepK {N : ℕ} (IH : ∀ R : Set Ω, Box R → DetN N R → Dfin R) (hB : Box R)
    (hD : LabDet S0 S1 S2 l0 l1 l2 R) (hN : S0.card + S1.card + S2.card ≤ N + 1)
    (H0 : ∀ a a', l0 a ≠ l0 a' → KRel R a a')
    (H1 : ∀ y y', (∀ z a a', sl R a y z - sl R a y' z = sl R a' y z - sl R a' y' z) →
      l1 y = l1 y')
    (H2 : ∀ z z', (∀ y a a', sl R a y z - sl R a y z' = sl R a' y z - sl R a' y z') →
      l2 z = l2 z')
    {a₀ b : ℕ} (hne : l0 a₀ ≠ l0 b) : Dfin R := by
  obtain ⟨a, ha, hc⟩ := allK_pair hB hD H0 H1 H2 hne
  have hR' := merged_dfin IH hB hD hN ha
  have form : ∀ y z, sl R a y z =
      sl R b y z + ind (Uof (dif R a b)) y + ind (Vof (dif R a b)) z - 1 := by
    intro y z
    have := krel_form hB (H0 a b ha) y z
    rw [dif_def] at this
    omega
  refine merge_apply hD hR' (p := fun _ z => z ∉ Vof (dif R a b))
    (q := fun y _ => y ∈ Uof (dif R a b)) ?_ ?_ ?_ ?_
  · exact gens20 fun x y h2 h0 hx => by
      rw [mem_setOf_eq] at hx ⊢; rw [← h0, ← h2]; exact hx
  · exact gens01 fun x y h0 h1 hx => by
      rw [mem_setOf_eq] at hx ⊢; rw [← h0, ← h1]; exact hx
  · intro y z
    beta_reduce
    have f := form y z
    rcases ind_cases (Uof (dif R a b)) y with ⟨hy, ey⟩ | ⟨hy, ey⟩ <;>
      rcases ind_cases (Vof (dif R a b)) z with ⟨hz, ez⟩ | ⟨hz, ez⟩
    · rw [bi_neg (not_not.mpr hz), bi_pos hy]; omega
    · rw [bi_pos hz, bi_pos hy]; omega
    · rw [bi_neg (not_not.mpr hz), bi_neg hy]; omega
    · rw [bi_pos hz, bi_neg hy]; omega
  · by_cases hex : ∃ y ∈ Uof (dif R a b), ∃ z, z ∉ Vof (dif R a b) ∧ sl R b y z = 1
    · left
      obtain ⟨y₁, hy₁, z₁, hz₁, e₁⟩ := hex
      intro y z hz
      by_cases hy : y ∈ Uof (dif R a b)
      · rw [hc y hy z hz y₁ hy₁ z₁ hz₁]; exact e₁
      · have f := form y z
        have := ind_neg hy; have := ind_neg hz
        have := sl_cases R a y z; have := sl_cases R b y z
        omega
    · right
      intro y z hy
      have f := form y z
      have := sl_cases R a y z; have := sl_cases R b y z
      by_cases hz : z ∈ Vof (dif R a b)
      · have := ind_pos hy; have := ind_pos hz
        omega
      · have : sl R b y z ≠ 1 := fun e => hex ⟨y, hy, z, hz, e⟩
        omega

end Grid

lemma dfin_rot {E : Set Ω} (hE : Dfin E) : Dfin (rot ⁻¹' E) := by
  induction hE with
  | basic h => exact Dfin.basic (gens_rot h)
  | compl _ ih => rw [preimage_compl]; exact Dfin.compl ih
  | union _ _ hd ih₁ ih₂ => rw [preimage_union]; exact Dfin.union ih₁ ih₂ (hd.preimage rot)

lemma rot3 (x : Ω) : rot (rot (rot x)) = x := by
  funext i; fin_cases i <;> rfl

/-- **Step 4, inductive form.** A box set determined by at most `N` labels in total is
finitary. Induction on `N`. -/
theorem dfin_of_detN : ∀ (N : ℕ) (R : Set Ω), Box R → DetN N R → Dfin R := by
  intro N
  induction N with
  | zero =>
    rintro R - ⟨S0, S1, S2, l0, l1, l2, hD, hN⟩
    have := Finset.card_pos.mpr ⟨_, hD.1 0⟩
    omega
  | succ N IH =>
    rintro R hB ⟨S0, S1, S2, l0, l1, l2, hD, hN⟩
    have e3 : rot ⁻¹' (rot ⁻¹' (rot ⁻¹' R)) = R := by
      ext x; simp only [mem_preimage, rot3]
    by_cases h0 : ∃ a b, l0 a ≠ l0 b ∧ ¬ KRel R a b
    · obtain ⟨a, b, hab, hK⟩ := h0
      exact step0 IH hB hD hN hab hK
    by_cases h1 : ∃ a b, l1 a ≠ l1 b ∧ ¬ KRel (rot ⁻¹' R) a b
    · obtain ⟨a, b, hab, hK⟩ := h1
      have h := step0 IH (box_rot hB) (labdet_rot hD) (by omega) hab hK
      have h3 := dfin_rot (dfin_rot h)
      rwa [e3] at h3
    by_cases h2 : ∃ a b, l2 a ≠ l2 b ∧ ¬ KRel (rot ⁻¹' (rot ⁻¹' R)) a b
    · obtain ⟨a, b, hab, hK⟩ := h2
      have h := step0 IH (box_rot (box_rot hB)) (labdet_rot (labdet_rot hD)) (by omega) hab hK
      have h3 := dfin_rot h
      rwa [e3] at h3
    push Not at h0 h1 h2
    by_cases hne : ∃ a b, l0 a ≠ l0 b
    · obtain ⟨a, b, hab⟩ := hne
      refine stepK IH hB hD hN h0 ?_ ?_ hab
      · intro y y' hyp
        by_contra hl
        exact (h1 y y' hl).1 (fun p q q' => hyp p q q')
      · intro z z' hyp
        by_contra hl
        exact (h2 z z' hl).2 (fun p p' q => hyp q p p')
    · push Not at hne
      exact Dfin.basic (gens12 fun x y h1 h2 hx =>
        hD.2.2.2 x y (hne _ _) (by rw [h1]) (by rw [h2]) hx)

/-- **Step 4 (hand: "Finite grids: every box set is a carrier set"), in the pulled-back form
over ℕ³.** A box set that factors through a finite coordinatewise quotient is finitary.

Proof (`dfin_of_detN`): induction on the total number of labels. Merge two classes that are not
K-related (`step0`, at coordinate 0; coordinates 1, 2 by `rot`). If all distinct classes are
K-related at all three coordinates, fix a base class `b` and take `a` with `Uof (dif R a b)`
minimal (`allK_pair`): `U × Vᶜ` lies in one cell, so the K-related pair `a, b` can also be merged
(`stepK`), at the cost of one window event removed and one added. If coordinate 0 has a single
class the set is a window event. The total order `E_<` of the hand proof (Fix 2) is not built. -/
theorem dfin_of_box_finDet {R : Set Ω} (hB : Box R) (hF : FinDet R) : Dfin R := by
  obtain ⟨n, lab, h⟩ := hF
  refine dfin_of_detN (3 * n) R hB ⟨Finset.range n, Finset.range n, Finset.range n,
    fun x => lab 0 x, fun x => lab 1 x, fun x => lab 2 x,
    ⟨fun x => Finset.mem_range.mpr (lab 0 x).2, fun x => Finset.mem_range.mpr (lab 1 x).2,
      fun x => Finset.mem_range.mpr (lab 2 x).2, ?_⟩, by simp; omega⟩
  intro x y h0 h1 h2 hx
  refine h x y (fun i => ?_) hx
  fin_cases i
  · exact Fin.ext h0
  · exact Fin.ext h1
  · exact Fin.ext h2

/-- **By-product.** For a set determined by finitely many labels, the box identity is equivalent
to being finitary (hence to being a carrier set). -/
theorem box_iff_dfin_of_finDet {R : Set Ω} (hF : FinDet R) : Box R ↔ Dfin R :=
  ⟨fun hB => dfin_of_box_finDet hB hF, fun h => box_of_mem (dfin_mem h)⟩

theorem box_iff_mem_of_finDet {R : Set Ω} (hF : FinDet R) : Box R ↔ D₃.Has R :=
  ⟨fun hB => dfin_mem (dfin_of_box_finDet hB hF), box_of_mem⟩

/-! ## Step 3'. Collapsing a labelled cover (replaces the column analysis in the proof of
`mem_dfin`) -/

@[simp] lemma bi_false : bi False = 0 := bi_neg not_false

lemma bi_cases (p : Prop) : (p ∧ bi p = 1) ∨ (¬ p ∧ bi p = 0) := by
  by_cases h : p
  · exact Or.inl ⟨h, bi_pos h⟩
  · exact Or.inr ⟨h, bi_neg h⟩

lemma cnt_bi (P : Ω → Prop) (x : Ω) : (cnt (setOf P) x : ℤ) = bi (P x) := by
  by_cases h : P x
  · rw [bi_pos h]; simp [cnt, h]
  · rw [bi_neg h]; simp [cnt, h]

lemma mem_of_cnt {E : Set Ω} {x : Ω} (h : (cnt E x : ℤ) = 1) : x ∈ E := by
  rcases cnt_cases E x with ⟨m, -⟩ | ⟨-, e⟩
  · exact m
  · rw [e] at h; simp at h

/-- **Collapse at coordinate 0.** If every value `a` is `≃₁`- or `≃₂`-equivalent to `ρ a`, then `E`
is recovered from its pullback along `ρ` (at coordinate 0) by removing and adding window events
(two of window `{0,1}`, two of window `{2,0}`). No box hypothesis, no finiteness. -/
lemma collapse0 {E : Set Ω} (ρ : ℕ → ℕ) (κ : ℕ → Prop) (h1 : ∀ a, κ a → Eq1 E a (ρ a))
    (h2 : ∀ a, ¬ κ a → Eq2 E a (ρ a)) (hd : Dfin (cw ![ρ, id, id] ⁻¹' E)) : Dfin E := by
  classical
  obtain ⟨ρ₁, r₁, r₂⟩ : ∃ ρ₁ : ℕ → ℕ, (∀ a, κ a → ρ₁ a = ρ a) ∧ (∀ a, ¬ κ a → ρ₁ a = a) :=
    ⟨fun a => if κ a then ρ a else a, fun a h => if_pos h, fun a h => if_neg h⟩
  have hin : ∀ (σ : ℕ → ℕ) (x : Ω),
      (cnt (cw ![σ, id, id] ⁻¹' E) x : ℤ) = sl E (σ (x 0)) (x 1) (x 2) := by
    intro σ x
    show (cnt E (cw ![σ, id, id] x) : ℤ) = _
    rw [cw_vec]; rfl
  have g1 : ∀ x : Ω, κ (x 0) →
      sl E (x 0) (x 1) (x 2) - sl E (ρ (x 0)) (x 1) (x 2) = dif E (x 0) (ρ (x 0)) (x 1) 0 :=
    fun x hk => h1 _ hk (x 1) (x 2) 0
  have g2 : ∀ x : Ω, ¬ κ (x 0) →
      sl E (x 0) (x 1) (x 2) - sl E (ρ (x 0)) (x 1) (x 2) = dif E (x 0) (ρ (x 0)) 0 (x 2) :=
    fun x hk => h2 _ hk (x 1) 0 (x 2)
  -- stage 2: collapse the `≃₂` classes
  have hM : Dfin (cw ![ρ₁, id, id] ⁻¹' E) := by
    refine dfin_adj1 (S := {x | ¬ κ (x 0) ∧ dif E (x 0) (ρ (x 0)) 0 (x 2) = -1})
      (T := {x | ¬ κ (x 0) ∧ dif E (x 0) (ρ (x 0)) 0 (x 2) = 1}) hd ?_ ?_ ?_ ?_
    · exact gens20 fun x y h2 h0 hx => by
        rw [mem_setOf_eq] at hx ⊢; rw [← h0, ← h2]; exact hx
    · exact gens20 fun x y h2 h0 hx => by
        rw [mem_setOf_eq] at hx ⊢; rw [← h0, ← h2]; exact hx
    · intro x
      simp only [cnt_bi]
      rw [hin ρ₁ x, hin ρ x]
      by_cases hk : κ (x 0)
      · rw [r₁ _ hk]
        simp only [hk, not_true_eq_false, false_and, bi_false]
      · rw [r₂ _ hk]
        have e := g2 x hk
        have r := dif_range E (x 0) (ρ (x 0)) 0 (x 2)
        simp only [hk, not_false_eq_true, true_and]
        rcases bi_cases (dif E (x 0) (ρ (x 0)) 0 (x 2) = -1) with ⟨c1, e1⟩ | ⟨c1, e1⟩ <;>
          rcases bi_cases (dif E (x 0) (ρ (x 0)) 0 (x 2) = 1) with ⟨c2, e2⟩ | ⟨c2, e2⟩ <;> omega
    · rintro x ⟨hk, hv⟩
      apply mem_of_cnt
      rw [hin ρ x]
      have e := g2 x hk
      have := sl_cases E (x 0) (x 1) (x 2); have := sl_cases E (ρ (x 0)) (x 1) (x 2)
      omega
  -- stage 1: collapse the `≃₁` classes
  refine dfin_adj1 (S := {x | κ (x 0) ∧ dif E (x 0) (ρ (x 0)) (x 1) 0 = -1})
    (T := {x | κ (x 0) ∧ dif E (x 0) (ρ (x 0)) (x 1) 0 = 1}) hM ?_ ?_ ?_ ?_
  · exact gens01 fun x y h0 h1 hx => by
      rw [mem_setOf_eq] at hx ⊢; rw [← h0, ← h1]; exact hx
  · exact gens01 fun x y h0 h1 hx => by
      rw [mem_setOf_eq] at hx ⊢; rw [← h0, ← h1]; exact hx
  · intro x
    simp only [cnt_bi]
    rw [hin ρ₁ x, cnt_sl E x]
    by_cases hk : κ (x 0)
    · rw [r₁ _ hk]
      have e := g1 x hk
      have r := dif_range E (x 0) (ρ (x 0)) (x 1) 0
      simp only [hk, true_and]
      rcases bi_cases (dif E (x 0) (ρ (x 0)) (x 1) 0 = -1) with ⟨c1, e1⟩ | ⟨c1, e1⟩ <;>
        rcases bi_cases (dif E (x 0) (ρ (x 0)) (x 1) 0 = 1) with ⟨c2, e2⟩ | ⟨c2, e2⟩ <;> omega
    · rw [r₂ _ hk]
      simp only [hk, false_and, bi_false]
  · rintro x ⟨hk, hv⟩
    apply mem_of_cnt
    rw [hin ρ₁ x, r₁ _ hk]
    have e := g1 x hk
    have := sl_cases E (x 0) (x 1) (x 2); have := sl_cases E (ρ (x 0)) (x 1) (x 2)
    omega

/-- Collapse of a labelled cover at coordinate 0 onto class representatives. -/
lemma collapse_cover {E : Set Ω} (hc : Cover 0 E) :
    ∃ (ρ : ℕ → ℕ) (n : ℕ) (lab : ℕ → Fin n), (∀ a b, lab a = lab b → ρ a = ρ b) ∧
      (Dfin (cw ![ρ, id, id] ⁻¹' E) → Dfin E) := by
  obtain ⟨n, lab, kind, h⟩ := hc
  obtain ⟨rep, hrep⟩ := exists_rep lab
  refine ⟨fun a => rep (lab a), n, lab, fun a b e => by simp only [e], fun hd => ?_⟩
  refine collapse0 (fun a => rep (lab a)) (fun a => kind (lab a) = true) ?_ ?_ hd
  · intro a hk
    exact (h a (rep (lab a)) (hrep a).symm).1 hk
  · intro a hk
    exact (h a (rep (lab a)) (hrep a).symm).2 (by simpa using hk)

lemma dif_cw (g : Fin 3 → ℕ → ℕ) (E : Set Ω) (a b y z : ℕ) :
    dif (cw g ⁻¹' E) a b y z = dif E (g 0 a) (g 0 b) (g 1 y) (g 2 z) := by
  simp only [dif_def, sl, cnt_cw]

/-- A labelled cover at coordinate 0 pulls back along any coordinatewise map. -/
lemma cover0_cw (g : Fin 3 → ℕ → ℕ) {E : Set Ω} (hc : Cover 0 E) : Cover 0 (cw g ⁻¹' E) := by
  obtain ⟨n, lab, kind, h⟩ := hc
  refine ⟨n, fun a => lab (g 0 a), kind, fun a b hab => ⟨fun hk y z z' => ?_, fun hk y y' z => ?_⟩⟩
  · have := (h _ _ hab).1 hk (g 1 y) (g 2 z) (g 2 z')
    show dif (cw g ⁻¹' E) a b y z = dif (cw g ⁻¹' E) a b y z'
    rw [dif_cw, dif_cw]; exact this
  · have := (h _ _ hab).2 hk (g 1 y) (g 1 y') (g 2 z)
    show dif (cw g ⁻¹' E) a b y z = dif (cw g ⁻¹' E) a b y' z
    rw [dif_cw, dif_cw]; exact this

lemma rot_cw (g : Fin 3 → ℕ → ℕ) (E : Set Ω) :
    rot ⁻¹' (cw g ⁻¹' E) = cw ![g 1, g 2, g 0] ⁻¹' (rot ⁻¹' E) := by
  ext x
  have : cw g (rot x) = rot (cw ![g 1, g 2, g 0] x) := by
    funext i; fin_cases i <;> rfl
  simp only [mem_preimage, this]

/-- **Steps 3–5 in one.** A box set with a finite labelled cover at each coordinate is finitary.
Collapse the three covers onto class representatives (`collapse_cover`, coordinates 1 and 2 through
`rot`); the fully collapsed set is box and determined by the cover labels, so Step 4 applies. -/
theorem dfin_of_box_cover {E : Set Ω} (hB : Box E) (hc : ∀ i, Cover i E) : Dfin E := by
  have e3 : ∀ F : Set Ω, rot ⁻¹' (rot ⁻¹' (rot ⁻¹' F)) = F := fun F => by
    ext x; simp only [mem_preimage, rot3]
  obtain ⟨ρ₀, n₀, lab₀, hρ₀, back₀⟩ := collapse_cover (hc 0)
  apply back₀
  have c1 : Cover 0 (rot ⁻¹' (cw ![ρ₀, id, id] ⁻¹' E)) := by
    rw [rot_cw]; exact cover0_cw _ (hc 1)
  obtain ⟨ρ₁, n₁, lab₁, hρ₁, back₁⟩ := collapse_cover c1
  have s1 : Dfin (cw ![ρ₁, id, id] ⁻¹' (rot ⁻¹' (cw ![ρ₀, id, id] ⁻¹' E))) →
      Dfin (cw ![ρ₀, id, id] ⁻¹' E) := by
    intro h
    have := dfin_rot (dfin_rot (back₁ h))
    rwa [e3] at this
  apply s1
  have c2 : Cover 0 (rot ⁻¹' (cw ![ρ₁, id, id] ⁻¹' (rot ⁻¹' (cw ![ρ₀, id, id] ⁻¹' E)))) := by
    rw [rot_cw, rot_cw, rot_cw]; exact cover0_cw _ (cover0_cw _ (hc 2))
  obtain ⟨ρ₂, n₂, lab₂, hρ₂, back₂⟩ := collapse_cover c2
  have s2 : Dfin (cw ![ρ₂, id, id] ⁻¹'
      (rot ⁻¹' (cw ![ρ₁, id, id] ⁻¹' (rot ⁻¹' (cw ![ρ₀, id, id] ⁻¹' E))))) →
      Dfin (cw ![ρ₁, id, id] ⁻¹' (rot ⁻¹' (cw ![ρ₀, id, id] ⁻¹' E))) := by
    intro h
    have := dfin_rot (dfin_rot (back₂ h))
    rwa [e3] at this
  apply s2
  have key : ∀ x : Ω, x ∈ cw ![ρ₂, id, id] ⁻¹'
      (rot ⁻¹' (cw ![ρ₁, id, id] ⁻¹' (rot ⁻¹' (cw ![ρ₀, id, id] ⁻¹' E)))) ↔
      ![ρ₀ (x 1), ρ₁ (x 2), ρ₂ (x 0)] ∈ E := by
    intro x
    have e : cw ![ρ₀, id, id] (rot (cw ![ρ₁, id, id] (rot (cw ![ρ₂, id, id] x)))) =
        ![ρ₀ (x 1), ρ₁ (x 2), ρ₂ (x 0)] := by
      funext i; fin_cases i <;> rfl
    show cw ![ρ₀, id, id] (rot (cw ![ρ₁, id, id] (rot (cw ![ρ₂, id, id] x)))) ∈ E ↔ _
    rw [e]
  refine dfin_of_detN (n₂ + n₀ + n₁) _
    (box_cw _ (box_rot (box_cw _ (box_rot (box_cw _ hB)))))
    ⟨Finset.range n₂, Finset.range n₀, Finset.range n₁,
      fun x => lab₂ x, fun x => lab₀ x, fun x => lab₁ x,
      ⟨fun x => Finset.mem_range.mpr (lab₂ x).2, fun x => Finset.mem_range.mpr (lab₀ x).2,
        fun x => Finset.mem_range.mpr (lab₁ x).2, ?_⟩, by simp⟩
  intro x y h0 h1 h2 hx
  rw [key] at hx ⊢
  rw [← hρ₀ _ _ (Fin.ext h1), ← hρ₁ _ _ (Fin.ext h2), ← hρ₂ _ _ (Fin.ext h0)]
  exact hx

/-! ## Step 5. Assembly -/

/-- **`D₃ ⊆ D_fin`.** From Steps 1–2 (`finite_cover`), the collapse of the covers
(`dfin_of_box_cover`) and Step 4 (`dfin_of_detN`). Does not use `residue`. -/
theorem mem_dfin {E : Set Ω} (h : D₃.Has E) : Dfin E :=
  dfin_of_box_cover (box_of_mem h) (fun i => finite_cover h i)

/-- The three classes coincide: carrier sets = finitary sets = box sets with a finite labelled
cover at each coordinate. -/
theorem mem_iff_dfin {E : Set Ω} : D₃.Has E ↔ Dfin E := ⟨mem_dfin, dfin_mem⟩

theorem mem_iff_box_cover {E : Set Ω} : D₃.Has E ↔ Box E ∧ ∀ i, Cover i E :=
  ⟨fun h => ⟨box_of_mem h, fun i => finite_cover h i⟩,
    fun h => dfin_mem (dfin_of_box_cover h.1 h.2)⟩

/-- **Normal form.** Every carrier set is a disjoint union of three window events and a box
residue determined by finitely many labels per coordinate. -/
theorem normal_form {E : Set Ω} (h : D₃.Has E) :
    ∃ W₀ W₁ W₂ R : Set Ω, W₀ ∈ gens ∧ W₁ ∈ gens ∧ W₂ ∈ gens ∧
      Disjoint W₀ W₁ ∧ Disjoint W₀ W₂ ∧ Disjoint W₁ W₂ ∧ Disjoint (W₀ ∪ W₁ ∪ W₂) R ∧
      E = W₀ ∪ W₁ ∪ W₂ ∪ R ∧ FinDet R ∧ Box R := by
  have hB := box_of_mem h
  obtain ⟨W₀, W₁, W₂, R, h0, h1, h2, d01, d02, d12, dR, hEq, hF⟩ :=
    residue hB (fun i => finite_cover h i)
  have hW : Dfin (W₀ ∪ W₁ ∪ W₂) :=
    Dfin.union (Dfin.union (Dfin.basic h0) (Dfin.basic h1) d01) (Dfin.basic h2)
      (Set.disjoint_union_left.mpr ⟨d02, d12⟩)
  exact ⟨W₀, W₁, W₂, R, h0, h1, h2, d01, d02, d12, dR, hEq, hF,
    box_cancel (hEq ▸ hB) (box_of_mem (dfin_mem hW)) dR⟩

theorem memDfinTarget : MemDfinTarget := fun _ h => mem_dfin h

/-- Agreement on window events propagates along the finitary closure (sorry-free). -/
theorem agree_of_dfin {s t : Set Ω → ℤ}
    (hs_c : ∀ E, D₃.Has E → s Eᶜ = 1 - s E)
    (hs_u : ∀ A B, D₃.Has A → D₃.Has B → Disjoint A B → s (A ∪ B) = s A + s B)
    (ht_c : ∀ E, D₃.Has E → t Eᶜ = 1 - t E)
    (ht_u : ∀ A B, D₃.Has A → D₃.Has B → Disjoint A B → t (A ∪ B) = t A + t B)
    (hg : ∀ E ∈ gens, s E = t E) {E : Set Ω} (h : Dfin E) : s E = t E := by
  induction h with
  | basic h => exact hg _ h
  | compl hF ih => rw [hs_c _ (dfin_mem hF), ht_c _ (dfin_mem hF), ih]
  | union h₁ h₂ hd ih₁ ih₂ =>
    rw [hs_u _ _ (dfin_mem h₁) (dfin_mem h₂) hd, ht_u _ _ (dfin_mem h₁) (dfin_mem h₂) hd, ih₁, ih₂]

/-- **Corollary.** Complement-normalised, finitely additive functions on `D₃` that agree on the
window events agree on `D₃`. From `mem_dfin`. -/
theorem state_ext : StateExtTarget :=
  fun _ _ hs_c hs_u ht_c ht_u hg _ hE => agree_of_dfin hs_c hs_u ht_c ht_u hg (mem_dfin hE)

end TriangleCyclic

/-! ## Axiom receipts
None of these may show `sorryAx`. -/
#print axioms TriangleCyclic.dfin_mem
#print axioms TriangleCyclic.mem_cw
#print axioms TriangleCyclic.mem_turn
#print axioms TriangleCyclic.dif_split
#print axioms TriangleCyclic.krel_form
#print axioms TriangleCyclic.clique_inP
#print axioms TriangleCyclic.no_infinite_clique₀
#print axioms TriangleCyclic.no_infinite_clique
#print axioms TriangleCyclic.finite_cover₀
#print axioms TriangleCyclic.finite_cover
#print axioms TriangleCyclic.dfin_cw
#print axioms TriangleCyclic.dfin_diff
#print axioms TriangleCyclic.box_cancel
#print axioms TriangleCyclic.agree_of_dfin
#print axioms TriangleCyclic.residue
#print axioms TriangleCyclic.dfin_of_box_finDet
#print axioms TriangleCyclic.box_iff_dfin_of_finDet
#print axioms TriangleCyclic.box_iff_mem_of_finDet
#print axioms TriangleCyclic.dfin_of_box_cover
#print axioms TriangleCyclic.mem_dfin
#print axioms TriangleCyclic.mem_iff_box_cover
#print axioms TriangleCyclic.normal_form
#print axioms TriangleCyclic.state_ext
