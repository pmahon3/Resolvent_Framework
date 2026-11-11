/-
# Every compatible window family on the triangle extends to a state on `D₃`, uniquely

Hand claim: `notes/open_questions/views_across_records/TRIANGLE_CONSEQUENCES_CHECK.md`, C6 and C7.

STATUS: no `sorry` in this file; axiom receipts at the end (`propext`, `Classical.choice`,
`Quot.sound` only). Verdict: the claim is TRUE as stated, for every compatible family (tensor
type or not). No extra hypothesis.

What is proved.
* `WFam`, `Compatible`: a window family is three ultrafilters on `ℕ × ℕ`, one per pair window,
  read in the orientations `(x₀, x₁)`, `(x₁, x₂)`, `(x₂, x₀)` (the orientation of `stair01`,
  `stair12`, `stair20` in `TriangleCyclic.lean`). Compatible = the three one-coordinate marginals
  (pushforwards along `Prod.fst` / `Prod.snd`) match.
* `IsStateOf F s`: `s : Set Ω → ℤ` is {0,1}-valued on `D₃`, `s univ = 1`, `s Eᶜ = 1 - s E` and
  `s (A ∪ B) = s A + s B` for disjoint carrier sets, and on each window `s` is the window's
  ultrafilter: `s {x | (x i, x j) ∈ S} = 1 ↔ S ∈ u_ij` for every `S : Set (ℕ × ℕ)`.
  Faithfulness: the window events of window `{i,j}` are exactly the cylinders `{x | (x i, x j) ∈ S}`
  (`cyl_gens`, `gens_cyl`), so the three clauses fix `s` on all of `gens`.
* `compatible_family_extends`: for a compatible `F` the functional `lam F` is a state of `F`, and
  every state of `F` equals it on `D₃` (uniqueness = `state_ext`).
* `state_unique`: two states of the same family agree on `D₃` (no compatibility hypothesis needed).
* `ideal_iff_glued` (C7): a state of `F` is induced by an ultrafilter on `Ω` iff `F` is the
  pushforward of an ultrafilter on `Ω`.

Proof of existence. `lam F E` is the seven-term formula with base point `(0,0,0)`:
  u₀₁(E(·,·,0)) + u₁₂(E(0,·,·)) + u₂₀(E(·,0,·)) − p₀(E(·,0,0)) − p₁(E(0,·,0)) − p₂(E(0,0,·)) + E(0,0,0).
It is additive on all disjoint pairs and `lam F univ = 1` (`lam_union`, `lam_univ`); on a window
event it is the window's ultrafilter (`lam_w01/12/20`, this is where matching marginals enter).
{0,1}-valued on `D₃` (`lam_two`): by `normal_form` (TriangleFinitary), `E = W₀ ⊔ W₁ ⊔ W₂ ⊔ R` with
`Wᵢ` window events and `R` a box set determined by finitely many labels.
* `lam_gens`: a window event has value 0 or 1, and value 1 makes it `Thick` (it contains a
  cylinder over a set of its window's ultrafilter).
* `lam_findet`: `lam F R = [r ∈ R]` for a point `r` of the cell `C₀ × C₁ × C₂` of label classes
  chosen by the three marginals (one box identity of `R`), and value 1 makes `R` contain that
  cell (`Cell`).
* `thick_inter`, `thick_cell`: two thick sets meet (same window: one ultrafilter; two windows:
  the common coordinate's marginal), and a thick set meets a cell. So at most one of the four
  disjoint pieces has value 1.

Departures from the hand sketch.
* Base point fixed at `(0,0,0)`; independence of the base point (well-definedness of Λ) is never
  needed, because uniqueness already gives it on `D₃`.
* The sketch treats two `W`'s as coming from different windows. `normal_form` only says
  `Wᵢ ∈ gens`, so `thick_inter` covers all nine window pairs.
* "Image point in the label grid" is replaced by an actual point `r` of the cell.

Not in this file: the converse (every state on `D₃` has a compatible window family).
-/
import QuerySystem.TriangleFinitary

open Set MeasurableSpace Function

namespace TriangleCyclic

/-! ## Window families -/

/-- A window family on the triangle: an ultrafilter on `ℕ × ℕ` for each pair window, read as
`(x₀, x₁)`, `(x₁, x₂)`, `(x₂, x₀)`. -/
structure WFam where
  u01 : Ultrafilter (ℕ × ℕ)
  u12 : Ultrafilter (ℕ × ℕ)
  u20 : Ultrafilter (ℕ × ℕ)

/-- Matching one-coordinate marginals: coordinate 0 (from `u20` and `u01`), coordinate 1 (from
`u01` and `u12`), coordinate 2 (from `u12` and `u20`). -/
def Compatible (F : WFam) : Prop :=
  F.u20.map Prod.snd = F.u01.map Prod.fst ∧ F.u01.map Prod.snd = F.u12.map Prod.fst ∧
    F.u12.map Prod.snd = F.u20.map Prod.fst

/-- Cylinders: the window events of the three windows. -/
def cyl01 (S : Set (ℕ × ℕ)) : Set Ω := {x | (x 0, x 1) ∈ S}
def cyl12 (S : Set (ℕ × ℕ)) : Set Ω := {x | (x 1, x 2) ∈ S}
def cyl20 (S : Set (ℕ × ℕ)) : Set Ω := {x | (x 2, x 0) ∈ S}

/-- `s` is a two-valued finitely additive state on `D₃` whose window family is `F`. -/
structure IsStateOf (F : WFam) (s : Set Ω → ℤ) : Prop where
  two : ∀ E, D₃.Has E → s E = 0 ∨ s E = 1
  univ : s univ = 1
  compl : ∀ E, D₃.Has E → s Eᶜ = 1 - s E
  add : ∀ A B, D₃.Has A → D₃.Has B → Disjoint A B → s (A ∪ B) = s A + s B
  w01 : ∀ S : Set (ℕ × ℕ), (s (cyl01 S) = 1 ↔ S ∈ F.u01)
  w12 : ∀ S : Set (ℕ × ℕ), (s (cyl12 S) = 1 ↔ S ∈ F.u12)
  w20 : ∀ S : Set (ℕ × ℕ), (s (cyl20 S) = 1 ↔ S ∈ F.u20)

lemma cyl01_gens (S : Set (ℕ × ℕ)) : cyl01 S ∈ gens :=
  gens01 fun x y h0 h1 hx => by
    show (y 0, y 1) ∈ S
    rw [← h0, ← h1]; exact hx

lemma cyl12_gens (S : Set (ℕ × ℕ)) : cyl12 S ∈ gens :=
  gens12 fun x y h1 h2 hx => by
    show (y 1, y 2) ∈ S
    rw [← h1, ← h2]; exact hx

lemma cyl20_gens (S : Set (ℕ × ℕ)) : cyl20 S ∈ gens :=
  gens20 fun x y h2 h0 hx => by
    show (y 2, y 0) ∈ S
    rw [← h2, ← h0]; exact hx

/-- Every window event is a cylinder of one of the three windows. -/
lemma gens_cyl {E : Set Ω} (hE : E ∈ gens) :
    (∃ S, E = cyl01 S) ∨ (∃ S, E = cyl12 S) ∨ (∃ S, E = cyl20 S) := by
  obtain ⟨w, hw, hE⟩ := hE
  rcases hw with rfl | rfl | rfl
  · refine Or.inl ⟨{q | ![q.1, q.2, 0] ∈ E}, ?_⟩
    ext x
    exact window_event_local hE (by
      intro k hk; simp only [Set.mem_insert_iff, Set.mem_singleton_iff] at hk
      rcases hk with rfl | rfl <;> rfl)
  · refine Or.inr (Or.inl ⟨{q | ![0, q.1, q.2] ∈ E}, ?_⟩)
    ext x
    exact window_event_local hE (by
      intro k hk; simp only [Set.mem_insert_iff, Set.mem_singleton_iff] at hk
      rcases hk with rfl | rfl <;> rfl)
  · refine Or.inr (Or.inr ⟨{q | ![q.2, 0, q.1] ∈ E}, ?_⟩)
    ext x
    exact window_event_local hE (by
      intro k hk; simp only [Set.mem_insert_iff, Set.mem_singleton_iff] at hk
      rcases hk with rfl | rfl <;> rfl)

lemma gens_mem {E : Set Ω} (hE : E ∈ gens) : D₃.Has E := DynkinSystem.GenerateHas.basic _ hE

/-! ## Ultrafilter values -/

lemma bi_congr {p q : Prop} (h : p ↔ q) : bi p = bi q := by rw [propext h]

lemma bi_one {p : Prop} : bi p = 1 ↔ p := by
  rcases bi_cases p with ⟨h, e⟩ | ⟨h, e⟩
  · exact ⟨fun _ => h, fun _ => e⟩
  · exact ⟨fun h1 => by rw [e] at h1; exact absurd h1 (by norm_num), fun hp => absurd hp h⟩

lemma bi_cnt (E : Set Ω) (x : Ω) : bi (x ∈ E) = (cnt E x : ℤ) := by
  rcases cnt_cases E x with ⟨h, e⟩ | ⟨h, e⟩
  · rw [bi_pos h, e]; rfl
  · rw [bi_neg h, e]; rfl

/-- The {0,1} value of an ultrafilter on a set. -/
noncomputable def uv {α : Type} (u : Ultrafilter α) (S : Set α) : ℤ := bi (S ∈ u)

section UV
variable {α : Type} (u : Ultrafilter α)

lemma uv_cases (S : Set α) : uv u S = 0 ∨ uv u S = 1 := by
  rcases bi_cases (S ∈ u) with ⟨-, e⟩ | ⟨-, e⟩
  · exact Or.inr e
  · exact Or.inl e

lemma uv_one {S : Set α} : uv u S = 1 ↔ S ∈ u := bi_one

lemma uv_univ : uv u univ = 1 := (uv_one u).mpr Filter.univ_mem

lemma uv_union {S T : Set α} (hd : Disjoint S T) : uv u (S ∪ T) = uv u S + uv u T := by
  unfold uv
  have hnot : S ∈ u → T ∈ u → False := fun hS hT => by
    obtain ⟨x, hx⟩ := Ultrafilter.nonempty_of_mem (Filter.inter_mem hS hT)
    exact Set.disjoint_left.mp hd hx.1 hx.2
  by_cases hS : S ∈ u
  · have hT : T ∉ u := fun hT => hnot hS hT
    rw [bi_pos (Ultrafilter.union_mem_iff.mpr (Or.inl hS)), bi_pos hS, bi_neg hT]; rfl
  · by_cases hT : T ∈ u
    · rw [bi_pos (Ultrafilter.union_mem_iff.mpr (Or.inr hT)), bi_neg hS, bi_pos hT]; rfl
    · have : S ∪ T ∉ u := fun h => (Ultrafilter.union_mem_iff.mp h).elim hS hT
      rw [bi_neg this, bi_neg hS, bi_neg hT]; rfl

lemma uv_pre_union (f : α → Ω) {A B : Set Ω} (hd : Disjoint A B) :
    uv u (f ⁻¹' (A ∪ B)) = uv u (f ⁻¹' A) + uv u (f ⁻¹' B) := by
  rw [preimage_union]; exact uv_union u (hd.preimage f)

/-- Two sets that agree on a set of the ultrafilter have the same value. -/
lemma uv_congr_on {S A B : Set α} (hS : S ∈ u) (h : ∀ q ∈ S, (q ∈ A ↔ q ∈ B)) :
    uv u A = uv u B := by
  refine bi_congr ⟨fun hA => ?_, fun hB => ?_⟩
  · exact Filter.mem_of_superset (Filter.inter_mem hS hA) fun q hq => (h q hq.1).mp hq.2
  · exact Filter.mem_of_superset (Filter.inter_mem hS hB) fun q hq => (h q hq.1).mpr hq.2

/-- A set that is constantly `P` on a set of the ultrafilter has value `[P]`. -/
lemma uv_const_on {S A : Set α} {P : Prop} (hS : S ∈ u) (h : ∀ q ∈ S, (q ∈ A ↔ P)) :
    uv u A = bi P := by
  by_cases hP : P
  · rw [bi_pos hP]
    exact (uv_one u).mpr (Filter.mem_of_superset hS fun q hq => (h q hq).mpr hP)
  · rw [bi_neg hP]
    have : A ∉ u := fun hA => by
      obtain ⟨q, hq⟩ := Ultrafilter.nonempty_of_mem (Filter.inter_mem hS hA)
      exact hP ((h q hq.1).mp hq.2)
    exact bi_neg this

end UV

/-! ## The functional `lam` (seven-term formula, base point `(0,0,0)`) -/

def i01 (q : ℕ × ℕ) : Ω := ![q.1, q.2, 0]
def i12 (q : ℕ × ℕ) : Ω := ![0, q.1, q.2]
def i20 (q : ℕ × ℕ) : Ω := ![q.2, 0, q.1]
def j0 (q : ℕ × ℕ) : Ω := ![q.1, 0, 0]
def j1 (q : ℕ × ℕ) : Ω := ![0, q.1, 0]
def j2 (q : ℕ × ℕ) : Ω := ![0, 0, q.1]

/-- The base point. -/
def o3 : Ω := ![0, 0, 0]

/-- **The candidate state of a window family.** The three pair terms use the window ultrafilters;
the three single-coordinate terms use the marginals of coordinates 0, 1, 2, taken from `u01`,
`u12`, `u20` (first coordinate of each). -/
noncomputable def lam (F : WFam) (E : Set Ω) : ℤ :=
  uv F.u01 (i01 ⁻¹' E) + uv F.u12 (i12 ⁻¹' E) + uv F.u20 (i20 ⁻¹' E)
    - uv F.u01 (j0 ⁻¹' E) - uv F.u12 (j1 ⁻¹' E) - uv F.u20 (j2 ⁻¹' E) + bi (o3 ∈ E)

variable {F : WFam}

/-- Additive on every disjoint pair of sets (carrier or not). -/
theorem lam_union {A B : Set Ω} (hd : Disjoint A B) : lam F (A ∪ B) = lam F A + lam F B := by
  have h7 : bi (o3 ∈ A ∪ B) = bi (o3 ∈ A) + bi (o3 ∈ B) := by
    have := cnt_union hd o3
    rw [bi_cnt, bi_cnt, bi_cnt, this]; push_cast; rfl
  unfold lam
  rw [uv_pre_union _ _ hd, uv_pre_union _ _ hd, uv_pre_union _ _ hd, uv_pre_union _ _ hd,
    uv_pre_union _ _ hd, uv_pre_union _ _ hd, h7]
  ring

theorem lam_univ : lam F univ = 1 := by
  unfold lam
  simp only [preimage_univ, uv_univ, bi_pos (mem_univ o3)]
  norm_num

theorem lam_compl (E : Set Ω) : lam F Eᶜ = 1 - lam F E := by
  have h := lam_union (F := F) (disjoint_compl_right (a := E))
  rw [union_compl_self, lam_univ] at h
  omega

/-! ### Marginals -/

lemma c0 (h : Compatible F) (T : Set ℕ) : Prod.snd ⁻¹' T ∈ F.u20 ↔ Prod.fst ⁻¹' T ∈ F.u01 := by
  rw [← Ultrafilter.mem_map, ← Ultrafilter.mem_map, h.1]

lemma c1 (h : Compatible F) (T : Set ℕ) : Prod.snd ⁻¹' T ∈ F.u01 ↔ Prod.fst ⁻¹' T ∈ F.u12 := by
  rw [← Ultrafilter.mem_map, ← Ultrafilter.mem_map, h.2.1]

lemma c2 (h : Compatible F) (T : Set ℕ) : Prod.snd ⁻¹' T ∈ F.u12 ↔ Prod.fst ⁻¹' T ∈ F.u20 := by
  rw [← Ultrafilter.mem_map, ← Ultrafilter.mem_map, h.2.2]

/-! ### Value on window events -/

theorem lam_w01 (h : Compatible F) (S : Set (ℕ × ℕ)) : lam F (cyl01 S) = uv F.u01 S := by
  have e0 : i01 ⁻¹' cyl01 S = S := rfl
  have e1 : i12 ⁻¹' cyl01 S = j1 ⁻¹' cyl01 S := rfl
  have e2 : uv F.u20 (i20 ⁻¹' cyl01 S) = uv F.u01 (j0 ⁻¹' cyl01 S) :=
    bi_congr (c0 h {a | (a, 0) ∈ S})
  have e3 : uv F.u20 (j2 ⁻¹' cyl01 S) = bi (o3 ∈ cyl01 S) :=
    uv_const_on _ Filter.univ_mem fun q _ => Iff.rfl
  unfold lam
  rw [e0, e1, e2, e3]; ring

theorem lam_w12 (h : Compatible F) (S : Set (ℕ × ℕ)) : lam F (cyl12 S) = uv F.u12 S := by
  have e0 : i12 ⁻¹' cyl12 S = S := rfl
  have e1 : i20 ⁻¹' cyl12 S = j2 ⁻¹' cyl12 S := rfl
  have e2 : uv F.u01 (i01 ⁻¹' cyl12 S) = uv F.u12 (j1 ⁻¹' cyl12 S) :=
    bi_congr (c1 h {b | (b, 0) ∈ S})
  have e3 : uv F.u01 (j0 ⁻¹' cyl12 S) = bi (o3 ∈ cyl12 S) :=
    uv_const_on _ Filter.univ_mem fun q _ => Iff.rfl
  unfold lam
  rw [e0, e1, e2, e3]; ring

theorem lam_w20 (h : Compatible F) (S : Set (ℕ × ℕ)) : lam F (cyl20 S) = uv F.u20 S := by
  have e0 : i20 ⁻¹' cyl20 S = S := rfl
  have e1 : i01 ⁻¹' cyl20 S = j0 ⁻¹' cyl20 S := rfl
  have e2 : uv F.u12 (i12 ⁻¹' cyl20 S) = uv F.u20 (j2 ⁻¹' cyl20 S) :=
    bi_congr (c2 h {c | (c, 0) ∈ S})
  have e3 : uv F.u12 (j1 ⁻¹' cyl20 S) = bi (o3 ∈ cyl20 S) :=
    uv_const_on _ Filter.univ_mem fun q _ => Iff.rfl
  unfold lam
  rw [e0, e1, e2, e3]; ring

/-! ### Thick sets and cells -/

/-- `A` contains a cylinder over a set of its window's ultrafilter. -/
def Thick (F : WFam) (A : Set Ω) : Prop :=
  (∃ S ∈ F.u01, cyl01 S ⊆ A) ∨ (∃ S ∈ F.u12, cyl12 S ⊆ A) ∨ (∃ S ∈ F.u20, cyl20 S ⊆ A)

/-- `R` contains a product `C₀ × C₁ × C₂` of sets of the three marginals. -/
def Cell (F : WFam) (R : Set Ω) : Prop :=
  ∃ C0 C1 C2 : Set ℕ, Prod.fst ⁻¹' C0 ∈ F.u01 ∧ Prod.fst ⁻¹' C1 ∈ F.u12 ∧
    Prod.fst ⁻¹' C2 ∈ F.u20 ∧ ∀ x : Ω, x 0 ∈ C0 → x 1 ∈ C1 → x 2 ∈ C2 → x ∈ R

/-- A window event has value 0 or 1; value 1 makes it thick. -/
lemma lam_gens (h : Compatible F) {E : Set Ω} (hE : E ∈ gens) :
    (lam F E = 0 ∨ lam F E = 1) ∧ (lam F E = 1 → Thick F E) := by
  rcases gens_cyl hE with ⟨S, rfl⟩ | ⟨S, rfl⟩ | ⟨S, rfl⟩
  · rw [lam_w01 h]
    exact ⟨uv_cases _ _, fun h1 => Or.inl ⟨S, (uv_one _).mp h1, Subset.rfl⟩⟩
  · rw [lam_w12 h]
    exact ⟨uv_cases _ _, fun h1 => Or.inr (Or.inl ⟨S, (uv_one _).mp h1, Subset.rfl⟩)⟩
  · rw [lam_w20 h]
    exact ⟨uv_cases _ _, fun h1 => Or.inr (Or.inr ⟨S, (uv_one _).mp h1, Subset.rfl⟩)⟩

/-- Sets of two adjacent windows meet over the common coordinate (coordinate 1). -/
lemma meet1 (h : Compatible F) {S T : Set (ℕ × ℕ)} (hS : S ∈ F.u01) (hT : T ∈ F.u12) :
    ∃ a b c, (a, b) ∈ S ∧ (b, c) ∈ T := by
  have h1 : Prod.snd ⁻¹' (Prod.snd '' S) ∈ F.u01 :=
    Filter.mem_of_superset hS (subset_preimage_image _ _)
  obtain ⟨⟨b, c⟩, hb, hT'⟩ := Ultrafilter.nonempty_of_mem (Filter.inter_mem ((c1 h _).mp h1) hT)
  obtain ⟨⟨a, b'⟩, hq, e⟩ := hb
  have e' : b' = b := e
  subst e'
  exact ⟨a, b', c, hq, hT'⟩

/-- Coordinate 2. -/
lemma meet2 (h : Compatible F) {S T : Set (ℕ × ℕ)} (hS : S ∈ F.u12) (hT : T ∈ F.u20) :
    ∃ a b c, (b, c) ∈ S ∧ (c, a) ∈ T := by
  have h1 : Prod.snd ⁻¹' (Prod.snd '' S) ∈ F.u12 :=
    Filter.mem_of_superset hS (subset_preimage_image _ _)
  obtain ⟨⟨c, a⟩, hc, hT'⟩ := Ultrafilter.nonempty_of_mem (Filter.inter_mem ((c2 h _).mp h1) hT)
  obtain ⟨⟨b, c'⟩, hq, e⟩ := hc
  have e' : c' = c := e
  subst e'
  exact ⟨a, b, c', hq, hT'⟩

/-- Coordinate 0. -/
lemma meet0 (h : Compatible F) {S T : Set (ℕ × ℕ)} (hS : S ∈ F.u20) (hT : T ∈ F.u01) :
    ∃ a b c, (c, a) ∈ S ∧ (a, b) ∈ T := by
  have h1 : Prod.snd ⁻¹' (Prod.snd '' S) ∈ F.u20 :=
    Filter.mem_of_superset hS (subset_preimage_image _ _)
  obtain ⟨⟨a, b⟩, ha, hT'⟩ := Ultrafilter.nonempty_of_mem (Filter.inter_mem ((c0 h _).mp h1) hT)
  obtain ⟨⟨c, a'⟩, hq, e⟩ := ha
  have e' : a' = a := e
  subst e'
  exact ⟨a', b, c, hq, hT'⟩

/-- **Two thick sets meet.** -/
lemma thick_inter (h : Compatible F) {A B : Set Ω} (hA : Thick F A) (hB : Thick F B) :
    ∃ x, x ∈ A ∧ x ∈ B := by
  rcases hA with ⟨S, hS, hSA⟩ | ⟨S, hS, hSA⟩ | ⟨S, hS, hSA⟩ <;>
    rcases hB with ⟨T, hT, hTB⟩ | ⟨T, hT, hTB⟩ | ⟨T, hT, hTB⟩
  · obtain ⟨⟨a, b⟩, h1, h2⟩ := Ultrafilter.nonempty_of_mem (Filter.inter_mem hS hT)
    exact ⟨![a, b, 0], hSA (show (a, b) ∈ S from h1), hTB (show (a, b) ∈ T from h2)⟩
  · obtain ⟨a, b, c, h1, h2⟩ := meet1 h hS hT
    exact ⟨![a, b, c], hSA (show (a, b) ∈ S from h1), hTB (show (b, c) ∈ T from h2)⟩
  · obtain ⟨a, b, c, h1, h2⟩ := meet0 h hT hS
    exact ⟨![a, b, c], hSA (show (a, b) ∈ S from h2), hTB (show (c, a) ∈ T from h1)⟩
  · obtain ⟨a, b, c, h1, h2⟩ := meet1 h hT hS
    exact ⟨![a, b, c], hSA (show (b, c) ∈ S from h2), hTB (show (a, b) ∈ T from h1)⟩
  · obtain ⟨⟨b, c⟩, h1, h2⟩ := Ultrafilter.nonempty_of_mem (Filter.inter_mem hS hT)
    exact ⟨![0, b, c], hSA (show (b, c) ∈ S from h1), hTB (show (b, c) ∈ T from h2)⟩
  · obtain ⟨a, b, c, h1, h2⟩ := meet2 h hS hT
    exact ⟨![a, b, c], hSA (show (b, c) ∈ S from h1), hTB (show (c, a) ∈ T from h2)⟩
  · obtain ⟨a, b, c, h1, h2⟩ := meet0 h hS hT
    exact ⟨![a, b, c], hSA (show (c, a) ∈ S from h1), hTB (show (a, b) ∈ T from h2)⟩
  · obtain ⟨a, b, c, h1, h2⟩ := meet2 h hT hS
    exact ⟨![a, b, c], hSA (show (c, a) ∈ S from h2), hTB (show (b, c) ∈ T from h1)⟩
  · obtain ⟨⟨c, a⟩, h1, h2⟩ := Ultrafilter.nonempty_of_mem (Filter.inter_mem hS hT)
    exact ⟨![a, 0, c], hSA (show (c, a) ∈ S from h1), hTB (show (c, a) ∈ T from h2)⟩

/-- **A thick set meets a cell.** -/
lemma thick_cell (h : Compatible F) {A R : Set Ω} (hA : Thick F A) (hR : Cell F R) :
    ∃ x, x ∈ A ∧ x ∈ R := by
  obtain ⟨C0, C1, C2, h0, h1, h2, hC⟩ := hR
  rcases hA with ⟨S, hS, hSA⟩ | ⟨S, hS, hSA⟩ | ⟨S, hS, hSA⟩
  · obtain ⟨⟨a, b⟩, ⟨m1, m2⟩, m3⟩ := Ultrafilter.nonempty_of_mem
      (Filter.inter_mem (Filter.inter_mem hS h0) ((c1 h C1).mpr h1))
    obtain ⟨⟨c, d⟩, m4⟩ := Ultrafilter.nonempty_of_mem h2
    exact ⟨![a, b, c], hSA (show (a, b) ∈ S from m1), hC _ m2 m3 m4⟩
  · obtain ⟨⟨b, c⟩, ⟨m1, m2⟩, m3⟩ := Ultrafilter.nonempty_of_mem
      (Filter.inter_mem (Filter.inter_mem hS h1) ((c2 h C2).mpr h2))
    obtain ⟨⟨a, d⟩, m4⟩ := Ultrafilter.nonempty_of_mem h0
    exact ⟨![a, b, c], hSA (show (b, c) ∈ S from m1), hC _ m4 m2 m3⟩
  · obtain ⟨⟨c, a⟩, ⟨m1, m2⟩, m3⟩ := Ultrafilter.nonempty_of_mem
      (Filter.inter_mem (Filter.inter_mem hS h2) ((c0 h C0).mpr h0))
    obtain ⟨⟨b, d⟩, m4⟩ := Ultrafilter.nonempty_of_mem h1
    exact ⟨![a, b, c], hSA (show (c, a) ∈ S from m1), hC _ m3 m4 m2⟩

/-- Each marginal picks one label class. -/
lemma label_class {n : ℕ} (u : Ultrafilter (ℕ × ℕ)) (lab : ℕ → Fin n) :
    ∃ r : ℕ, Prod.fst ⁻¹' {a | lab a = lab r} ∈ u := by
  obtain ⟨c, hc⟩ := Ultrafilter.eq_pure_of_finite ((u.map Prod.fst).map lab)
  have h1 : ({c} : Set (Fin n)) ∈ (u.map Prod.fst).map lab := by
    rw [hc]; exact Ultrafilter.mem_pure.mpr rfl
  have h2 : Prod.fst ⁻¹' (lab ⁻¹' {c}) ∈ u := Ultrafilter.mem_map.mp (Ultrafilter.mem_map.mp h1)
  obtain ⟨⟨r, d⟩, hr⟩ := Ultrafilter.nonempty_of_mem h2
  have hr' : lab r = c := hr
  refine ⟨r, Filter.mem_of_superset h2 fun q hq => ?_⟩
  have hq' : lab q.1 = c := hq
  show lab q.1 = lab r
  rw [hq', hr']

/-- **Residue.** A box set determined by finitely many labels has value `[r ∈ R]` at a point `r`
of the cell chosen by the marginals; value 1 puts the whole cell inside `R`. -/
lemma lam_findet (h : Compatible F) {R : Set Ω} (hB : Box R) (hF : FinDet R) :
    (lam F R = 0 ∨ lam F R = 1) ∧ (lam F R = 1 → Cell F R) := by
  obtain ⟨n, lab, hlab⟩ := hF
  obtain ⟨r0, hr0⟩ := label_class F.u01 (lab 0)
  obtain ⟨r1, hr1⟩ := label_class F.u12 (lab 1)
  obtain ⟨r2, hr2⟩ := label_class F.u20 (lab 2)
  have key : ∀ a b c a' b' c' : ℕ, lab 0 a = lab 0 a' → lab 1 b = lab 1 b' → lab 2 c = lab 2 c' →
      (![a, b, c] ∈ R ↔ ![a', b', c'] ∈ R) := by
    intro a b c a' b' c' e0 e1 e2
    constructor
    · refine hlab _ _ fun i => ?_
      fin_cases i
      · exact e0
      · exact e1
      · exact e2
    · refine hlab _ _ fun i => ?_
      fin_cases i
      · exact e0.symm
      · exact e1.symm
      · exact e2.symm
  have t1 : uv F.u01 (i01 ⁻¹' R) = bi (![r0, r1, 0] ∈ R) :=
    uv_const_on _ (Filter.inter_mem hr0 ((c1 h _).mpr hr1)) fun q hq =>
      key q.1 q.2 0 r0 r1 0 hq.1 hq.2 rfl
  have t2 : uv F.u12 (i12 ⁻¹' R) = bi (![0, r1, r2] ∈ R) :=
    uv_const_on _ (Filter.inter_mem hr1 ((c2 h _).mpr hr2)) fun q hq =>
      key 0 q.1 q.2 0 r1 r2 rfl hq.1 hq.2
  have t3 : uv F.u20 (i20 ⁻¹' R) = bi (![r0, 0, r2] ∈ R) :=
    uv_const_on _ (Filter.inter_mem hr2 ((c0 h _).mpr hr0)) fun q hq =>
      key q.2 0 q.1 r0 0 r2 hq.2 rfl hq.1
  have t4 : uv F.u01 (j0 ⁻¹' R) = bi (![r0, 0, 0] ∈ R) :=
    uv_const_on _ hr0 fun q hq => key q.1 0 0 r0 0 0 hq rfl rfl
  have t5 : uv F.u12 (j1 ⁻¹' R) = bi (![0, r1, 0] ∈ R) :=
    uv_const_on _ hr1 fun q hq => key 0 q.1 0 0 r1 0 rfl hq rfl
  have t6 : uv F.u20 (j2 ⁻¹' R) = bi (![0, 0, r2] ∈ R) :=
    uv_const_on _ hr2 fun q hq => key 0 0 q.1 0 0 r2 rfl rfl hq
  have hbox := hB r0 0 r1 0 r2 0
  have hval : lam F R = bi (![r0, r1, r2] ∈ R) := by
    unfold lam
    rw [t1, t2, t3, t4, t5, t6]
    show _ + bi (![0, 0, 0] ∈ R) = _
    simp only [bi_cnt]
    omega
  rw [hval]
  refine ⟨?_, fun h1 => ?_⟩
  · rcases bi_cases (![r0, r1, r2] ∈ R) with ⟨-, e⟩ | ⟨-, e⟩
    · exact Or.inr e
    · exact Or.inl e
  · have hr : ![r0, r1, r2] ∈ R := bi_one.mp h1
    refine ⟨_, _, _, hr0, hr1, hr2, fun x m0 m1 m2 => ?_⟩
    refine hlab _ x (fun i => ?_) hr
    fin_cases i
    · exact (show lab 0 (x 0) = lab 0 r0 from m0).symm
    · exact (show lab 1 (x 1) = lab 1 r1 from m1).symm
    · exact (show lab 2 (x 2) = lab 2 r2 from m2).symm

/-- **`lam F` is {0,1}-valued on the triangle carrier**, for every compatible family. -/
theorem lam_two (h : Compatible F) {E : Set Ω} (hE : D₃.Has E) : lam F E = 0 ∨ lam F E = 1 := by
  obtain ⟨W₀, W₁, W₂, R, g0, g1, g2, d01, d02, d12, dR, hEq, hF, hB⟩ := normal_form hE
  have dW : Disjoint (W₀ ∪ W₁) W₂ := Set.disjoint_union_left.mpr ⟨d02, d12⟩
  have hsum : lam F E = lam F W₀ + lam F W₁ + lam F W₂ + lam F R := by
    rw [hEq, lam_union dR, lam_union dW, lam_union d01]
  rw [hsum]
  obtain ⟨a0, b0⟩ := lam_gens h g0
  obtain ⟨a1, b1⟩ := lam_gens h g1
  obtain ⟨a2, b2⟩ := lam_gens h g2
  obtain ⟨aR, bR⟩ := lam_findet h hB hF
  have n01 : ¬ (lam F W₀ = 1 ∧ lam F W₁ = 1) := fun ⟨x, y⟩ => by
    obtain ⟨p, hp, hq⟩ := thick_inter h (b0 x) (b1 y)
    exact Set.disjoint_left.mp d01 hp hq
  have n02 : ¬ (lam F W₀ = 1 ∧ lam F W₂ = 1) := fun ⟨x, y⟩ => by
    obtain ⟨p, hp, hq⟩ := thick_inter h (b0 x) (b2 y)
    exact Set.disjoint_left.mp d02 hp hq
  have n12 : ¬ (lam F W₁ = 1 ∧ lam F W₂ = 1) := fun ⟨x, y⟩ => by
    obtain ⟨p, hp, hq⟩ := thick_inter h (b1 x) (b2 y)
    exact Set.disjoint_left.mp d12 hp hq
  have n0R : ¬ (lam F W₀ = 1 ∧ lam F R = 1) := fun ⟨x, y⟩ => by
    obtain ⟨p, hp, hq⟩ := thick_cell h (b0 x) (bR y)
    exact Set.disjoint_left.mp dR (Or.inl (Or.inl hp)) hq
  have n1R : ¬ (lam F W₁ = 1 ∧ lam F R = 1) := fun ⟨x, y⟩ => by
    obtain ⟨p, hp, hq⟩ := thick_cell h (b1 x) (bR y)
    exact Set.disjoint_left.mp dR (Or.inl (Or.inr hp)) hq
  have n2R : ¬ (lam F W₂ = 1 ∧ lam F R = 1) := fun ⟨x, y⟩ => by
    obtain ⟨p, hp, hq⟩ := thick_cell h (b2 x) (bR y)
    exact Set.disjoint_left.mp dR (Or.inr hp) hq
  clear hsum b0 b1 b2 bR
  generalize lam F W₀ = x0 at *
  generalize lam F W₁ = x1 at *
  generalize lam F W₂ = x2 at *
  generalize lam F R = xR at *
  omega

/-! ## The theorem -/

/-- `lam F` is a state with window family `F`. -/
theorem lam_isState (h : Compatible F) : IsStateOf F (lam F) where
  two := fun _ hE => lam_two h hE
  univ := lam_univ
  compl := fun E _ => lam_compl E
  add := fun _ _ _ _ hd => lam_union hd
  w01 := fun S => by rw [lam_w01 h]; exact uv_one _
  w12 := fun S => by rw [lam_w12 h]; exact uv_one _
  w20 := fun S => by rw [lam_w20 h]; exact uv_one _

lemma eq_of_two {a b : ℤ} (ha : a = 0 ∨ a = 1) (hb : b = 0 ∨ b = 1) (h : a = 1 ↔ b = 1) :
    a = b := by
  rcases ha with rfl | rfl <;> rcases hb with rfl | rfl
  · rfl
  · exact absurd (h.mpr rfl) (by norm_num)
  · exact absurd (h.mp rfl) (by norm_num)
  · rfl

/-- **Uniqueness** (from `state_ext`): two states with the same window family agree on `D₃`. -/
theorem state_unique {s t : Set Ω → ℤ} (hs : IsStateOf F s) (ht : IsStateOf F t) :
    ∀ E, D₃.Has E → s E = t E := by
  refine state_ext s t hs.compl hs.add ht.compl ht.add fun E hE => ?_
  refine eq_of_two (hs.two E (gens_mem hE)) (ht.two E (gens_mem hE)) ?_
  rcases gens_cyl hE with ⟨S, rfl⟩ | ⟨S, rfl⟩ | ⟨S, rfl⟩
  · exact (hs.w01 S).trans (ht.w01 S).symm
  · exact (hs.w12 S).trans (ht.w12 S).symm
  · exact (hs.w20 S).trans (ht.w20 S).symm

/-- **Every compatible window family on the triangle extends to a state on `D₃`, uniquely.** -/
theorem compatible_family_extends (F : WFam) (h : Compatible F) :
    ∃ s : Set Ω → ℤ, IsStateOf F s ∧ ∀ t : Set Ω → ℤ, IsStateOf F t → ∀ E, D₃.Has E → t E = s E :=
  ⟨lam F, lam_isState h, fun _ ht => state_unique ht (lam_isState h)⟩

/-! ## C7: ideal point ⟺ globally glued -/

/-- The window family of an ultrafilter on `Ω` (pushforward to the three windows). -/
def pushF (U : Ultrafilter Ω) : WFam where
  u01 := U.map fun x => (x 0, x 1)
  u12 := U.map fun x => (x 1, x 2)
  u20 := U.map fun x => (x 2, x 0)

lemma pushF_compatible (U : Ultrafilter Ω) : Compatible (pushF U) := by
  refine ⟨?_, ?_, ?_⟩ <;> simp only [pushF, Ultrafilter.map_map] <;> rfl

/-- An ultrafilter on `Ω` is a state with its own window family. -/
lemma pushF_isState (U : Ultrafilter Ω) : IsStateOf (pushF U) (fun E => uv U E) where
  two := fun E _ => uv_cases U E
  univ := uv_univ U
  compl := fun E _ => by
    have h := uv_union U (disjoint_compl_right (a := E))
    rw [union_compl_self, uv_univ] at h
    show uv U Eᶜ = 1 - uv U E
    omega
  add := fun _ _ _ _ hd => uv_union U hd
  w01 := fun S => (uv_one U).trans Ultrafilter.mem_map.symm
  w12 := fun S => (uv_one U).trans Ultrafilter.mem_map.symm
  w20 := fun S => (uv_one U).trans Ultrafilter.mem_map.symm

/-- **Ideal point ⟺ globally glued.** A state with window family `F` is induced by an ultrafilter
on `Ω` iff `F` is the pushforward of an ultrafilter on `Ω`. (No compatibility hypothesis: both
sides imply it.) -/
theorem ideal_iff_glued {s : Set Ω → ℤ} (hs : IsStateOf F s) :
    (∃ U : Ultrafilter Ω, ∀ E, D₃.Has E → (s E = 1 ↔ E ∈ U)) ↔ ∃ U : Ultrafilter Ω, F = pushF U := by
  constructor
  · rintro ⟨U, hU⟩
    refine ⟨U, ?_⟩
    obtain ⟨u01, u12, u20⟩ := F
    have e01 : u01 = U.map fun x => (x 0, x 1) := Ultrafilter.ext fun S =>
      ((hs.w01 S).symm.trans (hU _ (gens_mem (cyl01_gens S)))).trans Ultrafilter.mem_map.symm
    have e12 : u12 = U.map fun x => (x 1, x 2) := Ultrafilter.ext fun S =>
      ((hs.w12 S).symm.trans (hU _ (gens_mem (cyl12_gens S)))).trans Ultrafilter.mem_map.symm
    have e20 : u20 = U.map fun x => (x 2, x 0) := Ultrafilter.ext fun S =>
      ((hs.w20 S).symm.trans (hU _ (gens_mem (cyl20_gens S)))).trans Ultrafilter.mem_map.symm
    rw [e01, e12, e20]; rfl
  · rintro ⟨U, rfl⟩
    refine ⟨U, fun E hE => ?_⟩
    rw [state_unique hs (pushF_isState U) E hE]
    exact uv_one U

/-- The staircase family and every other compatible family: pointless states on the triangle are
exactly the states of compatible families that are not globally glued. -/
theorem pointless_iff_not_glued (h : Compatible F) :
    (¬ ∃ U : Ultrafilter Ω, ∀ E, D₃.Has E → (lam F E = 1 ↔ E ∈ U)) ↔
      ¬ ∃ U : Ultrafilter Ω, F = pushF U :=
  not_congr (ideal_iff_glued (lam_isState h))

end TriangleCyclic

/-! ## Axiom receipts
None of these may show `sorryAx`. -/
#print axioms TriangleCyclic.lam_two
#print axioms TriangleCyclic.lam_isState
#print axioms TriangleCyclic.state_unique
#print axioms TriangleCyclic.compatible_family_extends
#print axioms TriangleCyclic.ideal_iff_glued
#print axioms TriangleCyclic.pointless_iff_not_glued
