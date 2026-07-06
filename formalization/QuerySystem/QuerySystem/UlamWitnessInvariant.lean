/-
# The Product Ulam Carrier — §3: the trace invariant and normal form

Formalizes §3 of the witness construction (`papers/sigma_essential/witness_candidate/`):
the mod-countable trace invariant `P̃`, representation rigidity (Lem 3.2), the
disjointness table (Lem 3.3), the family trichotomy (Lem 3.4), and the normal
form (Thm 3.5: every carrier set has a normalized representation).

Fiber renaming: the paper's fibers `1,2,3,4` are the Lean `0,1,2,3`; the cores
`A,B,C` carry codes `κA = 1100`, `κB = 1010`, `κC = 0110` in coordinates
`(0,1,2,3)`.
-/
import QuerySystem.UlamWitnessCore
import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic.FinCases

open Set Function MeasurableSpace

set_option linter.unusedSectionVars false

namespace SigmaEssential.Ulam

section Invariant

variable {M : Type*} [LinearOrder M]

/-! ## §3.0 Countable-equivalence `≈` -/

/-- `X ≈ Y`: the symmetric difference is countable. -/
def CEq (X Y : Set M) : Prop := (symmDiff X Y).Countable

theorem cEq_refl (X : Set M) : CEq X X := by
  simp only [CEq, symmDiff_self, bot_eq_empty]; exact countable_empty

theorem cEq_symm {X Y : Set M} (h : CEq X Y) : CEq Y X := by
  rwa [CEq, symmDiff_comm]

theorem cEq_trans {X Y Z : Set M} (hXY : CEq X Y) (hYZ : CEq Y Z) : CEq X Z := by
  have hsub : symmDiff X Z ⊆ symmDiff X Y ∪ symmDiff Y Z := by
    intro a ha
    rcases Set.mem_symmDiff.mp ha with ⟨haX, haZ⟩ | ⟨haZ, haX⟩
    · by_cases haY : a ∈ Y
      · exact Or.inr (Set.mem_symmDiff.mpr (Or.inl ⟨haY, haZ⟩))
      · exact Or.inl (Set.mem_symmDiff.mpr (Or.inl ⟨haX, haY⟩))
    · by_cases haY : a ∈ Y
      · exact Or.inl (Set.mem_symmDiff.mpr (Or.inr ⟨haY, haX⟩))
      · exact Or.inr (Set.mem_symmDiff.mpr (Or.inr ⟨haZ, haY⟩))
  exact (hXY.union hYZ).mono hsub

theorem cEq_compl {X Y : Set M} (h : CEq X Y) : CEq Xᶜ Yᶜ := by
  rw [CEq, compl_symmDiff_compl]; exact h

theorem cEq_empty_iff {X : Set M} : CEq X ∅ ↔ X.Countable := by
  simp only [CEq, bot_eq_empty ▸ symmDiff_bot]

/-- `≈` is compatible with unions. -/
theorem cEq_union {X Y X' Y' : Set M} (h1 : CEq X X') (h2 : CEq Y Y') :
    CEq (X ∪ Y) (X' ∪ Y') := by
  have hsub : symmDiff (X ∪ Y) (X' ∪ Y') ⊆ symmDiff X X' ∪ symmDiff Y Y' := by
    intro x hx
    rcases Set.mem_symmDiff.mp hx with ⟨hxU, hxV⟩ | ⟨hxV, hxU⟩
    · rcases hxU with hxX | hxY
      · exact Or.inl (Set.mem_symmDiff.mpr (Or.inl ⟨hxX, fun h => hxV (Or.inl h)⟩))
      · exact Or.inr (Set.mem_symmDiff.mpr (Or.inl ⟨hxY, fun h => hxV (Or.inr h)⟩))
    · rcases hxV with hxX | hxY
      · exact Or.inl (Set.mem_symmDiff.mpr (Or.inr ⟨hxX, fun h => hxU (Or.inl h)⟩))
      · exact Or.inr (Set.mem_symmDiff.mpr (Or.inr ⟨hxY, fun h => hxU (Or.inr h)⟩))
  exact (Set.Countable.union h1 h2).mono hsub

/-- Countable sets are `≈ ∅`. -/
theorem cEq_empty_of_countable {X : Set M} (h : X.Countable) : CEq X ∅ :=
  cEq_empty_iff.mpr h

/-- If two sets are `≈` and one is countable, so is the other. -/
theorem countable_of_cEq {X Y : Set M} (h : CEq X Y) (hX : X.Countable) :
    Y.Countable := by
  have hsub : Y ⊆ X ∪ symmDiff X Y := by
    intro a ha
    by_cases haX : a ∈ X
    · exact Or.inl haX
    · exact Or.inr (Set.mem_symmDiff.mpr (Or.inr ⟨ha, haX⟩))
  exact (hX.union h).mono hsub

/-- On an uncountable `M`, no set is `≈` to its own complement. -/
theorem not_cEq_self_compl (huncount : ¬ (Set.univ : Set M).Countable) (ξ : Set M) :
    ¬ CEq ξ ξᶜ := by
  intro h
  apply huncount
  have hsd : symmDiff ξ ξᶜ = Set.univ := by
    ext a; by_cases ha : a ∈ ξ <;> simp [Set.mem_symmDiff, ha]
  rw [CEq, hsd] at h
  exact h

/-! ## §3.1 The invariant -/

/-- `sel ξ b` = `ξ` if `b = false`, `ξᶜ` if `b = true` (the paper's `ξ^(b)`). -/
def sel (ξ : Set M) (b : Bool) : Set M := if b then ξᶜ else ξ

@[simp] theorem sel_false (ξ : Set M) : sel ξ false = ξ := rfl
@[simp] theorem sel_true (ξ : Set M) : sel ξ true = ξᶜ := rfl

theorem sel_not (ξ : Set M) (b : Bool) : sel ξ (! b) = (sel ξ b)ᶜ := by
  cases b <;> simp [sel]

theorem sel_compl (ξ : Set M) (b : Bool) : sel ξᶜ b = (sel ξ b)ᶜ := by
  cases b <;> simp [sel]

/-- Fiber trace `E_f`. -/
def trace (E : Set (M × Fin 4)) (f : Fin 4) : Set M := {x | (x, f) ∈ E}

@[simp] theorem mem_trace {E : Set (M × Fin 4)} {f : Fin 4} {x : M} :
    x ∈ trace E f ↔ (x, f) ∈ E := Iff.rfl

theorem trace_compl (E : Set (M × Fin 4)) (f : Fin 4) :
    trace Eᶜ f = (trace E f)ᶜ := by
  ext x; simp [trace]

theorem trace_union (E G : Set (M × Fin 4)) (f : Fin 4) :
    trace (E ∪ G) f = trace E f ∪ trace G f := by
  ext x; simp [trace]

theorem trace_iUnion (F : ℕ → Set (M × Fin 4)) (f : Fin 4) :
    trace (⋃ n, F n) f = ⋃ n, trace (F n) f := by
  ext x; simp [trace]

theorem trace_disjoint {E G : Set (M × Fin 4)} (hdisj : Disjoint E G) (f : Fin 4) :
    Disjoint (trace E f) (trace G f) := by
  rw [Set.disjoint_left] at hdisj ⊢
  intro x hxE hxG
  exact hdisj hxE hxG

/-- The even-weight code `E₄`: the four Bool coordinates xor to `false`. -/
@[reducible] def EvenCode (κ : Fin 4 → Bool) : Prop :=
  xor (κ 0) (xor (κ 1) (xor (κ 2) (κ 3))) = false

/-- The zero code word. -/
@[reducible] def zeroCode : Fin 4 → Bool := fun _ => false

/-- Core code `1100`. -/
@[reducible] def κA : Fin 4 → Bool := ![true, true, false, false]
/-- Core code `1010`. -/
@[reducible] def κB : Fin 4 → Bool := ![true, false, true, false]
/-- Core code `0110`. -/
@[reducible] def κC : Fin 4 → Bool := ![false, true, true, false]

theorem evenCode_zeroCode : EvenCode zeroCode := by decide
theorem evenCode_κA : EvenCode κA := by decide
theorem evenCode_κB : EvenCode κB := by decide
theorem evenCode_κC : EvenCode κC := by decide

/-- The normalized even codes are exactly `{zeroCode, κA, κB, κC}`. -/
theorem normalized_code_cases {κ : Fin 4 → Bool} (h : EvenCode κ) (h3 : κ 3 = false) :
    κ = zeroCode ∨ κ = κA ∨ κ = κB ∨ κ = κC := by
  have key : ∀ b0 b1 b2 b3 : Bool,
      xor b0 (xor b1 (xor b2 b3)) = false → b3 = false →
      (![b0, b1, b2, b3] : Fin 4 → Bool) = zeroCode ∨
      (![b0, b1, b2, b3] : Fin 4 → Bool) = κA ∨
      (![b0, b1, b2, b3] : Fin 4 → Bool) = κB ∨
      (![b0, b1, b2, b3] : Fin 4 → Bool) = κC := by
    decide
  have hκ : κ = ![κ 0, κ 1, κ 2, κ 3] := by
    funext i; fin_cases i <;> simp
  have hev : xor (κ 0) (xor (κ 1) (xor (κ 2) (κ 3))) = false := h
  have := key (κ 0) (κ 1) (κ 2) (κ 3) hev h3
  rwa [← hκ] at this

/-- `(ξ, κ)` represents `E`: every trace is `≈ sel ξ (κ f)`. -/
def Represents (E : Set (M × Fin 4)) (ξ : Set M) (κ : Fin 4 → Bool) : Prop :=
  ∀ f, CEq (trace E f) (sel ξ (κ f))

/-- Normalized representation: even code, fourth coordinate false. -/
def NRep (E : Set (M × Fin 4)) (ξ : Set M) (κ : Fin 4 → Bool) : Prop :=
  EvenCode κ ∧ κ 3 = false ∧ Represents E ξ κ

/-! ## §3.2 Representation rigidity (Lem 3.2) -/

/-- **Lemma 3.2 (normalized form).** Two normalized representations of the same
`E` have equal codes and `≈`-equal `ξ`. Normalization makes coordinate `3` the
common anchor: `κ 3 = lam 3 = false`, so `ξ ≈ trace E 3 ≈ η` immediately. -/
theorem nrep_unique (huncount : ¬ (Set.univ : Set M).Countable)
    {E : Set (M × Fin 4)} {ξ η : Set M} {κ lam : Fin 4 → Bool}
    (h1 : NRep E ξ κ) (h2 : NRep E η lam) : κ = lam ∧ CEq ξ η := by
  obtain ⟨_, hκ3, hrepκ⟩ := h1
  obtain ⟨_, hlam3, hreplam⟩ := h2
  -- coordinate 3: both codes false, so ξ ≈ trace E 3 ≈ η
  have hξ3 : CEq (trace E 3) ξ := by
    have := hrepκ 3; rwa [hκ3, sel_false] at this
  have hη3 : CEq (trace E 3) η := by
    have := hreplam 3; rwa [hlam3, sel_false] at this
  have hξη : CEq ξ η := cEq_trans (cEq_symm hξ3) hη3
  refine ⟨?_, hξη⟩
  funext f
  -- if κ f ≠ lam f, then sel ξ (κ f) ≈ sel η (lam f) with lam f = ¬ κ f, and ξ ≈ η
  by_contra hne
  have hbne : lam f = ! κ f := by
    cases hκf : κ f <;> cases hlf : lam f <;> simp_all
  have hκf : CEq (trace E f) (sel ξ (κ f)) := hrepκ f
  have hlf : CEq (trace E f) (sel η (lam f)) := hreplam f
  have hsel : CEq (sel ξ (κ f)) (sel η (lam f)) := cEq_trans (cEq_symm hκf) hlf
  rw [hbne, sel_not] at hsel
  -- sel ξ (κ f) ≈ (sel η (κ f))ᶜ; with ξ ≈ η get sel ξ (κ f) ≈ (sel ξ (κ f))ᶜ
  have hξηsel : CEq (sel η (κ f)) (sel ξ (κ f)) := by
    cases hb : κ f
    · simpa [sel] using cEq_symm hξη
    · simpa [sel] using cEq_compl (cEq_symm hξη)
  have : CEq (sel ξ (κ f)) (sel ξ (κ f))ᶜ :=
    cEq_trans hsel (cEq_compl hξηsel)
  cases hb : κ f
  · simp only [hb, sel_false] at this
    exact not_cEq_self_compl huncount ξ this
  · simp only [hb, sel_true] at this
    -- this : CEq ξᶜ (ξᶜ)ᶜ ; rewrite compl_compl to get CEq ξᶜ ξ, then symm
    rw [compl_compl] at this
    exact not_cEq_self_compl huncount ξ (cEq_symm this)

/-! ## §3.2 (cont.) Countability characterization -/

/-- `E.Countable ↔ every trace countable`. -/
theorem countable_iff_traces_countable {E : Set (M × Fin 4)} :
    E.Countable ↔ ∀ f, (trace E f).Countable := by
  constructor
  · intro hE f
    have hsub : trace E f ⊆ Prod.fst '' E := by
      rintro x hx
      exact ⟨(x, f), hx, rfl⟩
    exact (hE.image Prod.fst).mono hsub
  · intro hf
    have hsub : E ⊆ ⋃ f : Fin 4, (fun x => (x, f)) '' trace E f := by
      rintro ⟨x, f⟩ hp
      exact Set.mem_iUnion.2 ⟨f, ⟨x, hp, rfl⟩⟩
    exact (countable_iUnion (fun f => (hf f).image _)).mono hsub

/-- Lemma 3.2(2), forward: a countable set has zero normalized code and `ξ ≈ ∅`. -/
theorem nrep_countable_of (huncount : ¬ (Set.univ : Set M).Countable)
    {E : Set (M × Fin 4)} {ξ : Set M} {κ : Fin 4 → Bool}
    (h : NRep E ξ κ) (hE : E.Countable) : κ = zeroCode ∧ CEq ξ ∅ := by
  obtain ⟨_, hκ3, hrep⟩ := h
  have htr := countable_iff_traces_countable.mp hE
  -- coordinate 3: ξ ≈ trace E 3 countable, so ξ countable
  have hξc : ξ.Countable := by
    have h3 := hrep 3; rw [hκ3, sel_false] at h3
    exact countable_of_cEq h3 (htr 3)
  have hξe : CEq ξ ∅ := cEq_empty_of_countable hξc
  refine ⟨?_, hξe⟩
  funext f
  by_contra hne
  -- κ f = true (since ≠ false = zeroCode f)
  have hκf : κ f = true := by
    cases hb : κ f
    · exact absurd hb (by simpa [zeroCode] using hne)
    · rfl
  -- then trace E f ≈ ξᶜ, but trace E f countable and ξᶜ uncountable
  have h3 := hrep f; rw [hκf, sel_true] at h3
  have hξcompl : (ξᶜ).Countable := countable_of_cEq h3 (htr f)
  apply huncount
  have : (Set.univ : Set M) = ξ ∪ ξᶜ := by rw [union_compl_self]
  rw [this]; exact hξc.union hξcompl

/-- Lemma 3.2(2), backward. -/
theorem countable_of_nrep {E : Set (M × Fin 4)} {ξ : Set M}
    (h : NRep E ξ zeroCode) (hξ : CEq ξ ∅) : E.Countable := by
  obtain ⟨_, _, hrep⟩ := h
  rw [countable_iff_traces_countable]
  intro f
  have h3 := hrep f
  simp only [zeroCode, sel_false] at h3
  have : CEq (trace E f) ∅ := cEq_trans h3 hξ
  exact cEq_empty_iff.mp this

/-! ## §3 complement and generators -/

/-- Complement of a representation. -/
theorem represents_compl {E : Set (M × Fin 4)} {ξ : Set M} {κ : Fin 4 → Bool}
    (h : Represents E ξ κ) : Represents Eᶜ ξ (fun f => ! (κ f)) := by
  intro f
  rw [trace_compl, sel_not]
  exact cEq_compl (h f)

/-- `EvenCode` is preserved by pointwise negation (four coordinates). -/
theorem evenCode_not {κ : Fin 4 → Bool} (h : EvenCode κ) :
    EvenCode (fun f => ! (κ f)) := by
  simp only [EvenCode] at h ⊢
  revert h
  cases κ 0 <;> cases κ 1 <;> cases κ 2 <;> cases κ 3 <;> decide

/-- Complement of a normalized representation is a representation with negated
code; normalize it (it may fail `κ 3 = false`, handled by `nrep_normalize`). -/
theorem represents_compl_nrep {E : Set (M × Fin 4)} {ξ : Set M} {κ : Fin 4 → Bool}
    (h : NRep E ξ κ) : EvenCode (fun f => ! (κ f)) ∧
      Represents Eᶜ ξ (fun f => ! (κ f)) :=
  ⟨evenCode_not h.1, represents_compl h.2.2⟩

/-- Normalize a representation: if `κ 3 = true`, swap to `(ξᶜ, ¬κ)`. -/
theorem nrep_normalize {E : Set (M × Fin 4)} {ξ : Set M} {κ : Fin 4 → Bool}
    (hev : EvenCode κ) (hrep : Represents E ξ κ) : ∃ η lam, NRep E η lam := by
  by_cases h3 : κ 3 = false
  · exact ⟨ξ, κ, hev, h3, hrep⟩
  · have hκ3 : κ 3 = true := by
      cases hb : κ 3
      · exact absurd hb h3
      · rfl
    refine ⟨ξᶜ, fun f => ! (κ f), evenCode_not hev, ?_, ?_⟩
    · show (! κ 3) = false
      rw [hκ3]; rfl
    · intro f
      show CEq (trace E f) (sel ξᶜ (! κ f))
      have hsel : sel ξᶜ (! κ f) = sel ξ (κ f) := by
        rw [sel_compl, sel_not, compl_compl]
      rw [hsel]
      exact hrep f

/-! ### Generators are represented -/

theorem represents_singleton (p : M × Fin 4) : Represents {p} ∅ zeroCode := by
  intro f
  simp only [zeroCode, sel_false]
  apply cEq_empty_of_countable
  have hsub : trace ({p} : Set (M × Fin 4)) f ⊆ {p.1} := by
    intro x hx
    simp only [mem_trace, mem_singleton_iff] at hx
    simp only [mem_singleton_iff]
    exact (Prod.ext_iff.mp hx).1
  exact (countable_singleton p.1).mono hsub

theorem represents_empty : Represents (∅ : Set (M × Fin 4)) ∅ zeroCode := by
  intro f
  simp only [zeroCode, sel_false, trace]
  simp only [Set.mem_empty_iff_false, Set.setOf_false]
  exact cEq_refl _

theorem nrep_empty : NRep (∅ : Set (M × Fin 4)) ∅ zeroCode :=
  ⟨evenCode_zeroCode, rfl, represents_empty⟩

theorem represents_univ :
    Represents (Set.univ : Set (M × Fin 4)) Set.univ zeroCode := by
  intro f
  simp only [zeroCode, sel_false, trace]
  simp only [Set.mem_univ, Set.setOf_true]
  exact cEq_refl _

theorem nrep_univ : NRep (Set.univ : Set (M × Fin 4)) Set.univ zeroCode :=
  ⟨evenCode_zeroCode, rfl, represents_univ⟩

theorem represents_cell (U : UlamMatrix M) (α : M) (n : ℕ) :
    Represents (cell U α n) (U.C α n) zeroCode := by
  intro f
  simp only [zeroCode, sel_false]
  have : trace (cell U α n) f = U.C α n := by
    ext x; simp [trace, cell]
  rw [this]; exact cEq_refl _

/-- Trace of a core `Prod.snd ⁻¹' S`, per concrete fiber. -/
private theorem trace_coreset_eq (S : Set (Fin 4)) [DecidablePred (· ∈ S)]
    (f : Fin 4) : trace (Prod.snd ⁻¹' S) f = (if f ∈ S then (Set.univ : Set M) else ∅) := by
  by_cases hf : f ∈ S
  · rw [if_pos hf]
    ext x
    simp only [trace, mem_preimage, mem_setOf_eq, mem_univ, iff_true]
    exact hf
  · rw [if_neg hf]
    ext x
    simp only [trace, mem_preimage, mem_setOf_eq, mem_empty_iff_false, iff_false]
    exact hf

/-- `univ` and `∅` are the two reflexive targets. -/
private theorem cEq_univ_compl_empty : CEq (Set.univ : Set M) (∅ : Set M)ᶜ := by
  rw [compl_empty]; exact cEq_refl _

theorem nrep_coreA : NRep (coreA M) ∅ κA := by
  refine ⟨evenCode_κA, by decide, ?_⟩
  intro f
  rw [coreA, trace_coreset_eq]
  fin_cases f <;>
    first
      | (rw [if_pos (by decide)]; simp only [κA, sel]; exact cEq_univ_compl_empty)
      | (rw [if_neg (by decide)]; simp only [κA, sel]; exact cEq_refl _)

theorem nrep_coreB : NRep (coreB M) ∅ κB := by
  refine ⟨evenCode_κB, by decide, ?_⟩
  intro f
  rw [coreB, trace_coreset_eq]
  fin_cases f <;>
    first
      | (rw [if_pos (by decide)]; simp only [κB, sel]; exact cEq_univ_compl_empty)
      | (rw [if_neg (by decide)]; simp only [κB, sel]; exact cEq_refl _)

theorem nrep_coreC : NRep (coreC M) ∅ κC := by
  refine ⟨evenCode_κC, by decide, ?_⟩
  intro f
  rw [coreC, trace_coreset_eq]
  fin_cases f <;>
    first
      | (rw [if_pos (by decide)]; simp only [κC, sel]; exact cEq_univ_compl_empty)
      | (rw [if_neg (by decide)]; simp only [κC, sel]; exact cEq_refl _)

/-- `nrep_compl`: complement of a normalized rep, re-normalized. Since a
normalized `κ` has `κ 3 = false`, `¬κ` has `(¬κ) 3 = true`, so we swap to
`(ξᶜ, κ)` — the normalized rep of `Eᶜ` is `(ξᶜ, κ)`. -/
theorem nrep_compl {E : Set (M × Fin 4)} {ξ : Set M} {κ : Fin 4 → Bool}
    (h : NRep E ξ κ) : NRep Eᶜ ξᶜ κ := by
  obtain ⟨hev, h3, hrep⟩ := h
  refine ⟨hev, h3, ?_⟩
  intro f
  rw [trace_compl, sel_compl]
  exact cEq_compl (hrep f)

/-! ## §3.3 The disjointness table (Lem 3.3) -/

/-- Coordinate translation: from `Disjoint E G` and the two representations, the
`sel`-intersection at each `f` is countable. -/
theorem sel_inter_countable {E G : Set (M × Fin 4)} {ξ η : Set M}
    {κ lam : Fin 4 → Bool} (hE : Represents E ξ κ) (hG : Represents G η lam)
    (hdisj : Disjoint E G) (f : Fin 4) :
    (sel ξ (κ f) ∩ sel η (lam f)).Countable := by
  -- sel ξ (κ f) ∩ sel η (lam f) ⊆ (sel ξ (κ f) \ trace E f) ∪ (sel η (lam f) \ trace G f)
  --   ∪ (trace E f ∩ trace G f)
  have hd : Disjoint (trace E f) (trace G f) := trace_disjoint hdisj f
  have hEc : (symmDiff (trace E f) (sel ξ (κ f))).Countable := hE f
  have hGc : (symmDiff (trace G f) (sel η (lam f))).Countable := hG f
  have hsub : sel ξ (κ f) ∩ sel η (lam f) ⊆
      symmDiff (trace E f) (sel ξ (κ f)) ∪ symmDiff (trace G f) (sel η (lam f)) := by
    intro x ⟨hxξ, hxη⟩
    by_cases hxE : x ∈ trace E f
    · by_cases hxG : x ∈ trace G f
      · exact absurd (Set.disjoint_left.mp hd hxE hxG) (by simp)
      · exact Or.inr (Set.mem_symmDiff.mpr (Or.inr ⟨hxη, hxG⟩))
    · exact Or.inl (Set.mem_symmDiff.mpr (Or.inr ⟨hxξ, hxE⟩))
  exact (hEc.union hGc).mono hsub

/-- Case (I): both diagonal. -/
theorem table_I (huncount : ¬ (Set.univ : Set M).Countable)
    {E G : Set (M × Fin 4)} {ξ η : Set M}
    (hE : NRep E ξ zeroCode) (hG : NRep G η zeroCode) (hdisj : Disjoint E G) :
    (ξ ∩ η).Countable ∧ NRep (E ∪ G) (ξ ∪ η) zeroCode := by
  obtain ⟨_, _, hrepE⟩ := hE
  obtain ⟨_, _, hrepG⟩ := hG
  have hint : (ξ ∩ η).Countable := by
    have := sel_inter_countable hrepE hrepG hdisj 0
    simpa [zeroCode, sel] using this
  refine ⟨hint, evenCode_zeroCode, rfl, ?_⟩
  intro f
  show CEq (trace (E ∪ G) f) (sel (ξ ∪ η) (zeroCode f))
  rw [trace_union]
  simp only [zeroCode, sel_false]
  have hEf : CEq (trace E f) ξ := by have := hrepE f; simpa [zeroCode, sel] using this
  have hGf : CEq (trace G f) η := by have := hrepG f; simpa [zeroCode, sel] using this
  exact cEq_union hEf hGf

/-! ### Code-coordinate witnesses (finite facts about the four codes) -/

/-- Every nonzero normalized code has a coordinate `= false` and one `= true`. -/
theorem nonzero_code_has_false_true {κ : Fin 4 → Bool}
    (hev : EvenCode κ) (h3 : κ 3 = false) (hne : κ ≠ zeroCode) :
    (∃ f, κ f = false) ∧ (∃ f, κ f = true) := by
  rcases normalized_code_cases hev h3 with rfl | rfl | rfl | rfl
  · exact absurd rfl hne
  · exact ⟨⟨2, by decide⟩, ⟨0, by decide⟩⟩
  · exact ⟨⟨1, by decide⟩, ⟨0, by decide⟩⟩
  · exact ⟨⟨0, by decide⟩, ⟨1, by decide⟩⟩

/-- For two distinct nonzero normalized codes, there is a coordinate with pattern
`(true, false)`, one with `(false, true)`, one with `(false, false)`, and one with
`(true, true)`. -/
theorem distinct_codes_patterns {κ lam : Fin 4 → Bool}
    (hevκ : EvenCode κ) (h3κ : κ 3 = false) (hneκ : κ ≠ zeroCode)
    (hevlam : EvenCode lam) (h3lam : lam 3 = false) (hnelam : lam ≠ zeroCode)
    (hne : κ ≠ lam) :
    (∃ f, κ f = true ∧ lam f = false) ∧ (∃ f, κ f = false ∧ lam f = true) ∧
    (∃ f, κ f = false ∧ lam f = false) ∧ (∃ f, κ f = true ∧ lam f = true) := by
  rcases normalized_code_cases hevκ h3κ with rfl | rfl | rfl | rfl <;>
    rcases normalized_code_cases hevlam h3lam with rfl | rfl | rfl | rfl <;>
    first
      | exact absurd rfl hneκ
      | exact absurd rfl hnelam
      | exact absurd rfl hne
      | exact ⟨⟨0, by decide⟩, ⟨1, by decide⟩, ⟨3, by decide⟩, ⟨2, by decide⟩⟩
      | exact ⟨⟨1, by decide⟩, ⟨0, by decide⟩, ⟨3, by decide⟩, ⟨2, by decide⟩⟩
      | exact ⟨⟨0, by decide⟩, ⟨2, by decide⟩, ⟨3, by decide⟩, ⟨1, by decide⟩⟩
      | exact ⟨⟨2, by decide⟩, ⟨0, by decide⟩, ⟨3, by decide⟩, ⟨1, by decide⟩⟩
      | exact ⟨⟨1, by decide⟩, ⟨2, by decide⟩, ⟨3, by decide⟩, ⟨0, by decide⟩⟩
      | exact ⟨⟨2, by decide⟩, ⟨1, by decide⟩, ⟨3, by decide⟩, ⟨0, by decide⟩⟩

/-- Coordinate-`f` translation of the disjointness data, packaged as the four
possible `sel`-intersection facts. -/
theorem sel_pair_countable {E G : Set (M × Fin 4)} {ξ η : Set M}
    {κ lam : Fin 4 → Bool} (hE : Represents E ξ κ) (hG : Represents G η lam)
    (hdisj : Disjoint E G) (f : Fin 4) :
    (sel ξ (κ f) ∩ sel η (lam f)).Countable :=
  sel_inter_countable hE hG hdisj f

/-- Case (II): same nonzero code. `ξ ∩ η ≈ ∅` (a false coord) and `ξ ∪ η ≈ univ`
(a true coord), so `η ≈ ξᶜ` and the union has zero code with `ξ ∪ η ≈ univ`. -/
theorem table_II (huncount : ¬ (Set.univ : Set M).Countable)
    {E G : Set (M × Fin 4)} {ξ η : Set M} {κ : Fin 4 → Bool}
    (hκ : κ ≠ zeroCode) (hE : NRep E ξ κ) (hG : NRep G η κ) (hdisj : Disjoint E G) :
    CEq η ξᶜ ∧ NRep (E ∪ G) Set.univ zeroCode := by
  obtain ⟨hev, h3, hrepE⟩ := hE
  obtain ⟨_, _, hrepG⟩ := hG
  obtain ⟨⟨f0, hf0⟩, ⟨f1, hf1⟩⟩ := nonzero_code_has_false_true hev h3 hκ
  -- false coord: sel ξ false ∩ sel η false = ξ ∩ η countable
  have hint : (ξ ∩ η).Countable := by
    have := sel_pair_countable hrepE hrepG hdisj f0
    rw [hf0] at this; simpa [sel] using this
  -- true coord: sel ξ true ∩ sel η true = ξᶜ ∩ ηᶜ = (ξ ∪ η)ᶜ countable
  have hunion : ((ξ ∪ η)ᶜ).Countable := by
    have := sel_pair_countable hrepE hrepG hdisj f1
    rw [hf1] at this
    rw [Set.compl_union]
    simpa [sel] using this
  -- η ≈ ξᶜ: symmDiff η ξᶜ ⊆ (ξ ∩ η) ∪ (ξ ∪ η)ᶜ
  have hηξc : CEq η ξᶜ := by
    have hsub : symmDiff η ξᶜ ⊆ (ξ ∩ η) ∪ (ξ ∪ η)ᶜ := by
      intro x hx
      rcases Set.mem_symmDiff.mp hx with ⟨hxη, hxξc⟩ | ⟨hxξc, hxη⟩
      · have hxξ : x ∈ ξ := by simpa [mem_compl_iff] using hxξc
        exact Or.inl ⟨hxξ, hxη⟩
      · have hxξ : x ∉ ξ := by simpa [mem_compl_iff] using hxξc
        exact Or.inr (by
          rw [mem_compl_iff, mem_union]
          rintro (h | h)
          · exact hxξ h
          · exact hxη h)
    exact (hint.union hunion).mono hsub
  refine ⟨hηξc, evenCode_zeroCode, rfl, ?_⟩
  -- E ∪ G ≈ univ: at each fiber, trace (E ∪ G) f ≈ univ
  intro f
  show CEq (trace (E ∪ G) f) (sel Set.univ (zeroCode f))
  rw [trace_union]
  simp only [zeroCode, sel_false]
  -- trace E f ≈ sel ξ (κ f), trace G f ≈ sel η (κ f) = sel ξᶜ (κ f)ᶜ-side; union ≈ univ
  have hEf : CEq (trace E f) (sel ξ (κ f)) := hrepE f
  have hGf : CEq (trace G f) (sel η (κ f)) := hrepG f
  have hgη : CEq (sel η (κ f)) (sel ξ (κ f))ᶜ := by
    have : CEq (sel η (κ f)) (sel ξᶜ (κ f)) := by
      cases hb : κ f
      · simpa [sel] using hηξc
      · simpa [sel] using cEq_compl hηξc
    rw [sel_compl] at this; exact this
  have hunionf : CEq (trace E f ∪ trace G f) (sel ξ (κ f) ∪ (sel ξ (κ f))ᶜ) :=
    cEq_union hEf (cEq_trans hGf hgη)
  rw [union_compl_self] at hunionf
  exact hunionf

/-- Case (III): one diagonal, one nonzero. The diagonal member is countable and
the union has the nonzero member's representation. -/
theorem table_III (huncount : ¬ (Set.univ : Set M).Countable)
    {E G : Set (M × Fin 4)} {ξ η : Set M} {lam : Fin 4 → Bool}
    (hlam : lam ≠ zeroCode) (hE : NRep E ξ zeroCode) (hG : NRep G η lam)
    (hdisj : Disjoint E G) :
    E.Countable ∧ NRep (E ∪ G) η lam := by
  obtain ⟨_, _, hrepE⟩ := hE
  obtain ⟨hevlam, h3lam, hrepG⟩ := hG
  obtain ⟨⟨f0, hf0⟩, _⟩ := nonzero_code_has_false_true hevlam h3lam hlam
  -- at a false coord of lam: sel ξ false ∩ sel η false = ξ ∩ η countable
  -- at a true coord: ξ ⊆ ηᶜ... we instead use: ξ countable directly.
  -- ξ ≈ trace E f0; and sel ξ 0 ∩ sel η (lam f0) with lam f0 = false is ξ ∩ η.
  -- Better: use ALL false coords give ξ ∩ η ctble; a true coord gives ξ ⊆ ... .
  -- Cleanest: ξ is countable because ξ ∩ η ≈ ∅ AND ξ ∩ ηᶜ ≈ ∅.
  obtain ⟨f1, hf1⟩ := (nonzero_code_has_false_true hevlam h3lam hlam).2
  have hint0 : (ξ ∩ η).Countable := by
    have := sel_pair_countable hrepE hrepG hdisj f0
    rw [hf0] at this; simpa [sel] using this
  have hint1 : (ξ ∩ ηᶜ).Countable := by
    have := sel_pair_countable hrepE hrepG hdisj f1
    rw [hf1] at this; simpa [sel] using this
  have hξc : ξ.Countable := by
    have hsub : ξ ⊆ (ξ ∩ η) ∪ (ξ ∩ ηᶜ) := by
      intro x hx
      by_cases hxη : x ∈ η
      · exact Or.inl ⟨hx, hxη⟩
      · exact Or.inr ⟨hx, hxη⟩
    exact (hint0.union hint1).mono hsub
  have hEc : E.Countable := countable_of_nrep ⟨evenCode_zeroCode, rfl, hrepE⟩
    (cEq_empty_of_countable hξc)
  refine ⟨hEc, hevlam, h3lam, ?_⟩
  -- union rep: trace (E ∪ G) f ≈ trace G f (E countable ⟹ trace E f countable)
  intro f
  show CEq (trace (E ∪ G) f) (sel η (lam f))
  rw [trace_union]
  have hEtr : (trace E f).Countable :=
    countable_iff_traces_countable.mp hEc f
  -- trace E f ∪ trace G f ≈ trace G f ≈ sel η (lam f)
  have h1 : CEq (trace E f ∪ trace G f) (trace G f) := by
    have hsub : symmDiff (trace E f ∪ trace G f) (trace G f) ⊆ trace E f := by
      intro x hx
      rcases Set.mem_symmDiff.mp hx with ⟨hxU, hxG⟩ | ⟨hxG, hxU⟩
      · rcases hxU with hxE | hxG'
        · exact hxE
        · exact absurd hxG' hxG
      · exact absurd (Or.inr hxG) hxU
    exact hEtr.mono hsub
  exact cEq_trans h1 (hrepG f)

/-- Case (IV): two distinct nonzero codes — impossible. -/
theorem table_IV (huncount : ¬ (Set.univ : Set M).Countable)
    {E G : Set (M × Fin 4)} {ξ η : Set M} {κ lam : Fin 4 → Bool}
    (hκ : κ ≠ zeroCode) (hlam : lam ≠ zeroCode) (hne : κ ≠ lam)
    (hE : NRep E ξ κ) (hG : NRep G η lam) (hdisj : Disjoint E G) : False := by
  obtain ⟨hevκ, h3κ, hrepE⟩ := hE
  obtain ⟨hevlam, h3lam, hrepG⟩ := hG
  obtain ⟨⟨ftf, hκtf, hltf⟩, ⟨fft, hκft, hlft⟩, ⟨fff, hκff, hlff⟩, ⟨ftt, hκtt, hltt⟩⟩ :=
    distinct_codes_patterns hevκ h3κ hκ hevlam h3lam hlam hne
  -- (t,f): sel ξ true ∩ sel η false = ξᶜ ∩ η countable → η ⊆ ξ mod ctble (η \ ξ ctble)
  have h_tf : (ξᶜ ∩ η).Countable := by
    have := sel_pair_countable hrepE hrepG hdisj ftf
    rw [hκtf, hltf] at this; simpa [sel] using this
  -- (f,t): sel ξ false ∩ sel η true = ξ ∩ ηᶜ countable → ξ \ η ctble
  have h_ft : (ξ ∩ ηᶜ).Countable := by
    have := sel_pair_countable hrepE hrepG hdisj fft
    rw [hκft, hlft] at this; simpa [sel] using this
  -- (f,f): ξ ∩ η countable
  have h_ff : (ξ ∩ η).Countable := by
    have := sel_pair_countable hrepE hrepG hdisj fff
    rw [hκff, hlff] at this; simpa [sel] using this
  -- (t,t): ξᶜ ∩ ηᶜ = (ξ ∪ η)ᶜ countable
  have h_tt : ((ξ ∪ η)ᶜ).Countable := by
    have := sel_pair_countable hrepE hrepG hdisj ftt
    rw [hκtt, hltt] at this
    rw [Set.compl_union]; simpa [sel] using this
  -- ξ ≈ η: symmDiff ξ η = (ξ ∩ ηᶜ) ∪ (ξᶜ ∩ η)
  have hξη : CEq ξ η := by
    have hsub : symmDiff ξ η ⊆ (ξ ∩ ηᶜ) ∪ (ξᶜ ∩ η) := by
      intro x hx
      rcases Set.mem_symmDiff.mp hx with ⟨hxξ, hxη⟩ | ⟨hxη, hxξ⟩
      · exact Or.inl ⟨hxξ, hxη⟩
      · exact Or.inr ⟨hxξ, hxη⟩
    exact (h_ft.union h_tf).mono hsub
  -- ξ countable: ξ ⊆ (ξ ∩ η) ∪ (ξ ∩ ηᶜ)
  have hξc : ξ.Countable := by
    have hsub : ξ ⊆ (ξ ∩ η) ∪ (ξ ∩ ηᶜ) := by
      intro x hx
      by_cases hxη : x ∈ η
      · exact Or.inl ⟨hx, hxη⟩
      · exact Or.inr ⟨hx, hxη⟩
    exact (h_ff.union h_ft).mono hsub
  -- η countable (ξ ≈ η)
  have hηc : η.Countable := countable_of_cEq hξη hξc
  -- ξ ∪ η countable, but (ξ ∪ η)ᶜ countable ⟹ univ countable
  apply huncount
  have : (Set.univ : Set M) = (ξ ∪ η) ∪ (ξ ∪ η)ᶜ := by rw [union_compl_self]
  rw [this]
  exact (hξc.union hηc).union h_tt

/-! ## §3.4–3.5 Normal form (Thm 3.5): the closure under countable unions -/

/-- Trace-countability transfers `NRep` across a countable perturbation. -/
theorem nrep_union_countable {E N : Set (M × Fin 4)} {ξ : Set M} {κ : Fin 4 → Bool}
    (h : NRep E ξ κ) (hN : N.Countable) : NRep (E ∪ N) ξ κ := by
  obtain ⟨hev, h3, hrep⟩ := h
  refine ⟨hev, h3, ?_⟩
  intro f
  rw [trace_union]
  have hNtr : (trace N f).Countable := countable_iff_traces_countable.mp hN f
  -- trace E f ∪ trace N f ≈ trace E f ≈ sel ξ (κ f)
  have h1 : CEq (trace E f ∪ trace N f) (trace E f) := by
    have hsub : symmDiff (trace E f ∪ trace N f) (trace E f) ⊆ trace N f := by
      intro x hx
      rcases Set.mem_symmDiff.mp hx with ⟨hxU, hxE⟩ | ⟨hxE, hxU⟩
      · rcases hxU with h | h
        · exact absurd h hxE
        · exact h
      · exact absurd (Or.inl hxE) hxU
    exact hNtr.mono hsub
  exact cEq_trans h1 (hrep f)

/-- **Normalized closure under a disjoint pair.** If `E, G` each have a normalized
representation and are disjoint, so does `E ∪ G` (all four table cases). -/
theorem nrep_union_pair (huncount : ¬ (Set.univ : Set M).Countable)
    {E G : Set (M × Fin 4)} {ξ η : Set M} {κ lam : Fin 4 → Bool}
    (hE : NRep E ξ κ) (hG : NRep G η lam) (hdisj : Disjoint E G) :
    ∃ ζ ν, NRep (E ∪ G) ζ ν := by
  by_cases hκ0 : κ = zeroCode <;> by_cases hlam0 : lam = zeroCode
  · subst hκ0; subst hlam0
    exact ⟨ξ ∪ η, zeroCode, (table_I huncount hE hG hdisj).2⟩
  · subst hκ0
    exact ⟨η, lam, (table_III huncount hlam0 hE hG hdisj).2⟩
  · subst hlam0
    have := (table_III huncount hκ0 hG hE hdisj.symm).2
    rw [union_comm] at this
    exact ⟨ξ, κ, this⟩
  · -- both nonzero: table_IV forbids distinct, so κ = lam, then table_II
    have hκlam : κ = lam := by
      by_contra hne
      exact table_IV huncount hκ0 hlam0 hne hE hG hdisj
    subst hκlam
    exact ⟨Set.univ, zeroCode, (table_II huncount hκ0 hE hG hdisj).2⟩

/-- **Thm 3.5 (normal form).** Every carrier set has a normalized representation.
Induction over `GenerateHas`: generators are represented (§ above), complement via
`nrep_compl`, and countable disjoint unions via a `Nat`-recursion that folds the
family pairwise using `nrep_union_pair`, the partial unions staying disjoint from
the next member. -/
theorem nrep_exists (huncount : ¬ (Set.univ : Set M).Countable) {U : UlamMatrix M}
    {E : Set (M × Fin 4)} (hE : (carrier U).Has E) : ∃ ξ κ, NRep E ξ κ := by
  induction hE with
  | basic t ht =>
    rcases ht with (⟨p, rfl⟩ | ⟨α, n, rfl⟩) | h
    · exact ⟨∅, zeroCode, evenCode_zeroCode, rfl, represents_singleton p⟩
    · exact ⟨U.C α n, zeroCode, evenCode_zeroCode, rfl, represents_cell U α n⟩
    · rcases h with rfl | rfl | rfl
      · exact ⟨∅, κA, nrep_coreA⟩
      · exact ⟨∅, κB, nrep_coreB⟩
      · exact ⟨∅, κC, nrep_coreC⟩
  | empty => exact ⟨∅, zeroCode, nrep_empty⟩
  | compl _ ih =>
    obtain ⟨ξ, κ, h⟩ := ih
    exact ⟨ξᶜ, κ, nrep_compl h⟩
  | @iUnion F hdisj _ ih =>
    -- ih : ∀ i, ∃ ξ κ, NRep (F i) ξ κ ; choose reps
    choose ξ κ hrep using ih
    -- partial unions Uₙ = ⋃ i < n, F i are disjoint from F n and each has a rep.
    -- Build a normalized rep of ⋃ i, F i by a limiting trace argument:
    -- since GenerateHas is closed, ⋃ i F i ∈ carrier; we produce ITS rep directly.
    -- Strategy: prove the whole union has a normalized rep by cases on whether any
    -- κ i is nonzero.
    classical
    by_cases hnonzero : ∃ i, κ i ≠ zeroCode
    · -- some member is nonzero; its rep or the complementary pair reps the union
      obtain ⟨i₀, hi₀⟩ := hnonzero
      -- Every OTHER member j is disjoint from F i₀; table_III/table_II/table_IV apply.
      -- Case: is there a second nonzero member?
      by_cases hsecond : ∃ j, j ≠ i₀ ∧ κ j ≠ zeroCode
      · obtain ⟨j₀, hj₀ne, hj₀⟩ := hsecond
        -- table_IV forces κ i₀ = κ j₀, table_II gives the pair ≈ univ
        have hdij : Disjoint (F i₀) (F j₀) := hdisj hj₀ne.symm
        have hκeq : κ i₀ = κ j₀ := by
          by_contra hne
          exact table_IV huncount hi₀ hj₀ hne (hrep i₀) (hrep j₀) hdij
        -- the union is ≈ univ; show ⋃ i, F i has rep (univ, zeroCode)
        refine ⟨Set.univ, zeroCode, evenCode_zeroCode, rfl, ?_⟩
        intro f
        show CEq (trace (⋃ i, F i) f) (sel Set.univ (zeroCode f))
        simp only [zeroCode, sel_false]
        -- F i₀ ∪ F j₀ ⊆ ⋃ i, F i, and F i₀ ∪ F j₀ ≈ univ; univ ⊇ trace ⊇ (that)
        have hpair : CEq (trace (F i₀ ∪ F j₀) f) (sel Set.univ (zeroCode f)) := by
          have := (table_II huncount hi₀ (hrep i₀) (hκeq ▸ hrep j₀) hdij).2
          exact this.2.2 f
        simp only [zeroCode, sel_false] at hpair
        -- trace (F i₀ ∪ F j₀) f ≈ univ and ⊆ trace (⋃) f ⊆ univ ⟹ trace (⋃) f ≈ univ
        have hsub1 : trace (F i₀ ∪ F j₀) f ⊆ trace (⋃ i, F i) f := by
          intro x hx
          simp only [mem_trace] at hx ⊢
          rw [mem_union] at hx
          rw [mem_iUnion]
          rcases hx with h | h
          · exact ⟨i₀, h⟩
          · exact ⟨j₀, h⟩
        -- univ ≈ trace(pair) ⊆ trace(⋃) ⊆ univ ⟹ trace(⋃) ≈ univ
        have hpc : (trace (F i₀ ∪ F j₀) f)ᶜ.Countable := by
          have : CEq Set.univ (trace (F i₀ ∪ F j₀) f) := cEq_symm hpair
          rw [CEq] at this
          have heq : symmDiff (Set.univ : Set M) (trace (F i₀ ∪ F j₀) f)
              = (trace (F i₀ ∪ F j₀) f)ᶜ := by
            ext x; by_cases hxx : x ∈ trace (F i₀ ∪ F j₀) f <;>
              simp [Set.mem_symmDiff, hxx]
          rwa [heq] at this
        -- trace(⋃)ᶜ ⊆ trace(pair)ᶜ countable
        have huc : (trace (⋃ i, F i) f)ᶜ.Countable :=
          hpc.mono (compl_subset_compl.mpr hsub1)
        -- so trace(⋃) ≈ univ
        rw [CEq]
        have heq : symmDiff (trace (⋃ i, F i) f) (Set.univ : Set M)
            = (trace (⋃ i, F i) f)ᶜ := by
          ext x; by_cases hxx : x ∈ trace (⋃ i, F i) f <;>
            simp [Set.mem_symmDiff, hxx]
        rwa [heq]
      · -- i₀ is the ONLY nonzero member; every other F j is countable, union ≈ F i₀
        have hsecond' : ∀ j, j ≠ i₀ → κ j = zeroCode := by
          intro j hj
          by_contra hc
          exact hsecond ⟨j, hj, hc⟩
        refine ⟨ξ i₀, κ i₀, (hrep i₀).1, (hrep i₀).2.1, ?_⟩
        intro f
        -- trace (⋃ i, F i) f = ⋃ i, trace (F i) f; split off i₀
        rw [trace_iUnion]
        -- ⋃ i, trace (F i) f ≈ trace (F i₀) f ≈ sel (ξ i₀) (κ i₀ f)
        have hrest : (⋃ (i : ℕ) (_ : i ≠ i₀), trace (F i) f).Countable := by
          apply countable_iUnion
          intro i
          apply countable_iUnion
          intro hine
          -- F i has zero code (i ≠ i₀), disjoint from F i₀ nonzero ⟹ F i countable
          have hκi : κ i = zeroCode := hsecond' i hine
          have hdii : Disjoint (F i) (F i₀) := hdisj hine
          have hFic : (F i).Countable :=
            (table_III huncount hi₀ (hκi ▸ hrep i) (hrep i₀) hdii).1
          exact countable_iff_traces_countable.mp hFic f
        have hsplit : (⋃ i, trace (F i) f) =
            trace (F i₀) f ∪ (⋃ (i : ℕ) (_ : i ≠ i₀), trace (F i) f) := by
          ext x
          simp only [mem_iUnion, mem_union]
          constructor
          · rintro ⟨i, hi⟩
            by_cases h : i = i₀
            · exact Or.inl (h ▸ hi)
            · exact Or.inr ⟨i, h, hi⟩
          · rintro (h | ⟨i, _, hi⟩)
            · exact ⟨i₀, h⟩
            · exact ⟨i, hi⟩
        rw [hsplit]
        have h1 : CEq (trace (F i₀) f ∪ (⋃ (i : ℕ) (_ : i ≠ i₀), trace (F i) f))
            (trace (F i₀) f) := by
          have hsub : symmDiff (trace (F i₀) f ∪
              (⋃ (i : ℕ) (_ : i ≠ i₀), trace (F i) f)) (trace (F i₀) f) ⊆
              (⋃ (i : ℕ) (_ : i ≠ i₀), trace (F i) f) := by
            intro x hx
            rcases Set.mem_symmDiff.mp hx with ⟨hxU, hxE⟩ | ⟨hxE, hxU⟩
            · rcases hxU with h | h
              · exact absurd h hxE
              · exact h
            · exact absurd (Or.inl hxE) hxU
          exact hrest.mono hsub
        exact cEq_trans h1 ((hrep i₀).2.2 f)
    · -- all members diagonal (zero code): union has zero code
      have hallzero : ∀ i, κ i = zeroCode := by
        intro i
        by_contra hc
        exact hnonzero ⟨i, hc⟩
      refine ⟨⋃ i, ξ i, zeroCode, evenCode_zeroCode, rfl, ?_⟩
      intro f
      show CEq (trace (⋃ i, F i) f) (sel (⋃ i, ξ i) (zeroCode f))
      simp only [zeroCode, sel_false]
      rw [trace_iUnion]
      -- each trace (F i) f ≈ ξ i (zero code); ⋃ traces ≈ ⋃ ξ i
      have hsub : symmDiff (⋃ i, trace (F i) f) (⋃ i, ξ i) ⊆
          ⋃ i, symmDiff (trace (F i) f) (ξ i) := by
        intro x hx
        rcases Set.mem_symmDiff.mp hx with ⟨hxU, hxV⟩ | ⟨hxV, hxU⟩
        · obtain ⟨i, hi⟩ := Set.mem_iUnion.mp hxU
          refine Set.mem_iUnion.2 ⟨i, Set.mem_symmDiff.mpr (Or.inl ⟨hi, ?_⟩)⟩
          intro h; exact hxV (Set.mem_iUnion.2 ⟨i, h⟩)
        · obtain ⟨i, hi⟩ := Set.mem_iUnion.mp hxV
          refine Set.mem_iUnion.2 ⟨i, Set.mem_symmDiff.mpr (Or.inr ⟨hi, ?_⟩)⟩
          intro h; exact hxU (Set.mem_iUnion.2 ⟨i, h⟩)
      have hcount : (⋃ i, symmDiff (trace (F i) f) (ξ i)).Countable := by
        apply countable_iUnion
        intro i
        have hi : CEq (trace (F i) f) (sel (ξ i) (κ i f)) := (hrep i).2.2 f
        have hzi : κ i f = false := by rw [hallzero i]
        rw [hzi] at hi
        simpa [sel] using hi
      exact hcount.mono hsub

end Invariant

end SigmaEssential.Ulam
