/-
# The triangle carrier is finitary (`D₃ = D_fin`): machine-check in progress

Hand proof: `notes/open_questions/views_across_records/TRIANGLE_D3_DFIN_REVERSAL_CHECK.md`
(original: `TRIANGLE_5DE_CHECK.md` C6). Section numbers below are the hand proof's steps.

STATUS (see the end of the file for the list):
* (0) targets: `dfin_mem` proved; `mem_dfin` and `state_ext` are proved MODULO the two
  `sorry` lemmas `residue` (Step 3) and `dfin_of_box_finDet` (Step 4).
* Step 1 (no infinite K-clique): sorry-free (`clique_inP`, `no_infinite_clique`).
* Step 2 (finite labelled cover): sorry-free (`finite_cover`).
* Step 3, Step 4: stated, `sorry`, with proof sketches.
* Step 5 (assembly): sorry-free given Steps 3 and 4.

Alphabet: ℕ on each coordinate (`Ω = Fin 3 → ℕ`), as in `TriangleCyclic.lean`.
-/
import QuerySystem.TriangleCyclic
import Mathlib.Order.OrderIsoNat
import Mathlib.Order.Zorn
import Mathlib.Data.Set.Pairwise.Lattice

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

/-- TARGET 1 (the theorem `D₃ = D_fin`). Proved at the end as `mem_dfin`, modulo Steps 3, 4. -/
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

/-! ## Step 3. Columns and the residue (STATED, NOT PROVED) -/

/-- A set that factors through a finite coordinatewise quotient: membership depends only on
finitely many labels per coordinate. (Over ℕ³ this replaces "`R = g⁻¹(F̂)` with `F̂` on a finite
grid": the grid is the set of label triples.) -/
def FinDet (R : Set Ω) : Prop :=
  ∃ (n : ℕ) (lab : Fin 3 → ℕ → Fin n),
    ∀ x y : Ω, (∀ i, lab i (x i) = lab i (y i)) → x ∈ R → y ∈ R

/-- **Step 3 (hand: "Columns and residue", with Fix 1).** NOT PROVED.

Statement: a box set with a finite labelled cover at each coordinate is a disjoint union of three
window events and a residue that factors through a finite coordinatewise quotient.

Proof sketch. Write `P, Q, R` for parts of coordinates 0, 1, 2. Labels (see `Cover`, `turn`):
`P→1` means `F(a,y,z) − F(b,y,z)` is a function of `y` for `a b ∈ P` (kind true at i=0), `P→2` a
function of `z`; `Q→2` / `Q→0` (kind true / false at i=1); `R→0` / `R→1` (kind true / false at i=2).
1. *Mutual column* `P→1, Q→0`, all `z`: fixing `a₀ ∈ P, y₀ ∈ Q`,
   `F(a,y,z) = F(a₀,y₀,z) + k_y(a₀) + h_a(y) = φ(z) + ψ(a,y)` on `P×Q×ℕ`. As `F ∈ {0,1}`: either `φ`
   is constant and the column is `A×ℕ` with `A ⊆ P×Q` (call the column *flat*), or `ψ ≡ 0` and the
   column is `P×Q×R'`. Same for mutual pairs `(Q→2, R→1)` and `(R→0, P→2)` by `turn`.
2. `W₀ :=` union of the flat `(P→1,Q→0)` columns: local to window `{0,1}`, so in `gens` by
   `gens_of_local`; `W₀ ⊆ E`. `W₁, W₂` likewise for windows `{1,2}`, `{2,0}`. Pairwise disjoint: `W₀`
   lives over parts `Q→0`, `W₁` over parts `Q→2`; `W₀` over `P→1`, `W₂` over `P→2`; `W₁` over `R→1`,
   `W₂` over `R→0`.
3. *Cyclic column* `P→1, Q→2`: `F(a,y,z) − F(a₀,y,z) = h_a(y)` and `F(a,y,z) − F(a,y₀,z) = m_y(z)`
   independent of `a`, hence `h_a(y) = h_a(y₀) =: c_a` on `P×Q×ℕ`; so on that column `F` is
   independent of `x₀` or (when `F(a₀,·,·)` is constant on `Q×ℕ`) a function of `x₀` alone.
4. Cells `P×Q×R`: the three labels form a fixed-point-free map on `{0,1,2}`, so the cell has exactly
   one mutual pair or is cyclic. Mutual cell: removed whole by its own `W`, or equal to a product
   `P×Q×R''` and untouched by the other two `W`s (label mismatch). Cyclic cell: by 3 applied to its
   three pairs, `F` ∩ cell is, for each `i`, independent of `xᵢ` or a function of `xᵢ` alone; hence a
   function of one coordinate: `P'×Q×R`, `P×Q'×R` or `P×Q×R'`; no `W` meets it.
5. `R := E ∖ (W₀ ∪ W₁ ∪ W₂)` is in each of the finitely many cells a product with one arbitrary
   factor. Refine each coordinate's partition by the finitely many factor subsets occurring (Fix 1):
   labels `lab i a := (cover label of a, membership bits of a in those subsets)`, finite. `R` is
   saturated for these labels: `FinDet R`.

Lean route: unpack the three `Cover`s through `turn`/`rot` (`mem_turn_one`, `mem_turn_two`); prove
the mutual and cyclic column lemmas once at coordinate pair (0,1) for an arbitrary set and transport
by `rot`; define `W₀` as `{x | kind₀ (lab₀ (x 0)) = true ∧ kind₁ (lab₁ (x 1)) = false ∧ column flat
∧ x ∈ E}`. The sketch never uses `hB` (kept as a hypothesis: it is available at the call site).
Expected difficulty: long but elementary, estimated 600–1000 lines; the bookkeeping of the refined
labels in 5 (a finite product of `Fin`/`Bool` types, then `Finite.exists_equiv_fin`) and the three
rotated copies are the bulk. No new mathematical input. -/
theorem residue {E : Set Ω} (hB : Box E) (hc : ∀ i, Cover i E) :
    ∃ W₀ W₁ W₂ R : Set Ω, W₀ ∈ gens ∧ W₁ ∈ gens ∧ W₂ ∈ gens ∧
      Disjoint W₀ W₁ ∧ Disjoint W₀ W₂ ∧ Disjoint W₁ W₂ ∧ Disjoint (W₀ ∪ W₁ ∪ W₂) R ∧
      E = W₀ ∪ W₁ ∪ W₂ ∪ R ∧ FinDet R := by
  sorry

/-! ## Step 4. Finite grids (STATED, NOT PROVED) -/

/-- **Step 4 (hand: "Finite grids: every box set is a carrier set", with Fixes 2–3), in the
pulled-back form over ℕ³.** NOT PROVED.

Statement: a box set that factors through a finite coordinatewise quotient is finitary. (The hand
statement "on a finite grid, box ⇒ finitary" plus "`g⁻¹` preserves the finitary closure" of Step 5;
equivalent because a set with `FinDet` is the pullback of its image on the finite grid of labels
and the quotient map has a section.)

Proof sketch. Strong induction on `N =` total number of label classes that occur
(`∑ i, |range (lab i)|`), for all `R, lab` simultaneously.
* Base: some coordinate has one class. Then `R` is local to the opposite window: `gens_of_local`.
* Merge (hand "Merge"): suppose at some coordinate (WLOG 0, by `turn`) two values `a, b` in
  different classes satisfy `Eq1 R a b` (resp. `Eq2`), `dif R a b y z = h y`. Let `c : ℕ → ℕ` send
  the class `A` of `a` to `b` and fix everything else, `R' := cw ![c, id, id] ⁻¹' R`. `R'` is box
  (`box_cw`) and `FinDet` with one class fewer (labels `lab 0 ∘ c`), so `Dfin R'` by induction.
  `S₋ := {x | x 0 ∈ A ∧ h (x 1) = −1}`, `S₊ := {x | x 0 ∈ A ∧ h (x 1) = 1}` are local to window
  `{0,1}`; `S₋ ⊆ R'`, `S₊ ∩ R' = ∅` (on those lines the `b`-slice is full, resp. empty), and
  `R = (R' ∖ S₋) ∪ S₊`: use `dfin_diff` and `Dfin.union`.
* All-K (Fix 2): otherwise any two classes at any coordinate are K-related. Take class
  representatives `a₀ = q, a₁, …, a_n` at coordinate 0. By `krel_form` and `chain_cmp` (as in
  `clique_inP`) the sets `U_i, V_i` form a strict chain; relabel so `U₁ ⊂ … ⊂ U_n`. With
  `λ y := min {i | y ∈ U_i}`, `μ z := 1 + max {i | z ∈ V_i}`,
  `R(a_i,y,z) = G(y,z) + [λ y ≤ i] + [i < μ z] − 1` and `G(y,z) = [μ z < λ y]` when `λ y ≠ μ z`.
  If `λ y = λ y'` the two slices at coordinate 1 differ by a function of `z` alone, so `y, y'` are
  in one class: `λ` and `μ` are injective on classes, and all three coordinates have `n+1` classes.
* Swap (Fix 3): let `y₁, z₁` be the classes with `λ = μ = 1`. The line `{x 0 ∈ class a₀, x 1 ∈ class
  y₁}` (window `{0,1}`) is entirely inside or entirely outside `R`, likewise `{x 0 ∈ class a₀, x 2 ∈
  class z₁}` (window `{2,0}`); removing/adding them (in the order dictated by `G(y₁,z₁)`) gives a box
  `FinDet` set with the same classes in which `a₀` and `a₁` have equal slices, i.e. `Eq1`: the Merge
  case applies to it, and `R` is recovered by `dfin_diff` / `Dfin.union` with those two window events.

Lean route: do NOT build the order `E_<` of the hand proof; the swap needs only the displayed formula
for `i ∈ {0,1}` and `λ, μ ∈ {1, >1}`, i.e. the K form of the single pair `(a₁, a₀)` together with
minimality of `U₁` and maximality of `V₁` in the chain (finite chain ⇒ a minimal element, via
`Set.Finite.exists_minimal` on the finite set of class representatives). Expected difficulty: the
hardest part of the whole proof; Merge about 200 lines, All-K + Swap an estimated 600–1200 lines,
plus the induction scaffolding (class counting, WLOG over `turn`). Evidence only so far: exhaustive
finite computations recorded in the hand note (2×3×3, 3×3×3, 3×3×4). -/
theorem dfin_of_box_finDet {R : Set Ω} (hB : Box R) (hF : FinDet R) : Dfin R := by
  sorry

/-! ## Step 5. Assembly -/

/-- **`D₃ ⊆ D_fin`.** Proved from Steps 1–2 (sorry-free) and Steps 3–4 (`residue`,
`dfin_of_box_finDet`: `sorry`). -/
theorem mem_dfin {E : Set Ω} (h : D₃.Has E) : Dfin E := by
  have hB := box_of_mem h
  obtain ⟨W₀, W₁, W₂, R, h0, h1, h2, d01, d02, d12, dR, hEq, hF⟩ :=
    residue hB (fun i => finite_cover h i)
  have hW : Dfin (W₀ ∪ W₁ ∪ W₂) :=
    Dfin.union (Dfin.union (Dfin.basic h0) (Dfin.basic h1) d01) (Dfin.basic h2)
      (Set.disjoint_union_left.mpr ⟨d02, d12⟩)
  have hBR : Box R := box_cancel (hEq ▸ hB) (box_of_mem (dfin_mem hW)) dR
  rw [hEq]
  exact Dfin.union hW (dfin_of_box_finDet hBR hF) dR

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
window events agree on `D₃`. Depends on `mem_dfin`, hence on the two `sorry` lemmas. -/
theorem state_ext : StateExtTarget :=
  fun _ _ hs_c hs_u ht_c ht_u hg _ hE => agree_of_dfin hs_c hs_u ht_c ht_u hg (mem_dfin hE)

end TriangleCyclic

/-! ## Axiom receipts
Milestone A (Step 1) and Milestone B (Step 2) must show no `sorryAx`; `mem_dfin` and `state_ext`
show `sorryAx` until `residue` and `dfin_of_box_finDet` are proved. -/
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
#print axioms TriangleCyclic.mem_dfin
#print axioms TriangleCyclic.state_ext
