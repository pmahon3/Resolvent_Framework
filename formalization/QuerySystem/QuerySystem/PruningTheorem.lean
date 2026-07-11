/-
# Theorem P (pruning, phase-parametrized): LISC_k = TR_k at generator rotations

Formalizes the core of `papers/reconstruction/notes/pruning_theorem_and_B.md`
§2 (proof-read SOUND, receipt `PROOF_READ_2026-07-10_pruning.md`);
ratification kit item 5, gaps 5.1 (Step 3, assembly at general `k`) and 5.2
(Step 4, generator conjugation at general `k`).

## Encodings (faithful, and where Step 1 went)
* A winding-`k` simple cycle in the layered ring `R_L(ρ)` is encoded by its
  state sequence `W : ℕ → α` on positions `t < k*L`: ρ-steps between
  consecutive positions, a closing ρ-step, and the SIMPLICITY clause "same
  layer (`t % L`) + same state ⟹ same position" — which is literally
  layer-injectivity, automatic-given-simplicity (Lemma 0 + the note's
  "k distinct states per layer"). The note's Step 1 (phase normalization —
  cyclically reindex so position 0 sits at layer 0) is absorbed by the
  encoding: layers of `R_L` do not constrain ρ-arcs, so a cycle starting at
  layer `c` and its reindexing are the same `W`. `IsLISC ρ k L`.
* A tuple-walk witness is `τ : ℕ → ZMod k → α` with injective tuples for
  `i ≤ L`, coordinatewise ρ-arcs for `i < L`, and endpoint
  `τ L = σ_r (τ 0)` where `σ_r u j = u (j + r)`. `IsTR ρ L r`.
  The alphabet is NOT assumed finite — Theorem P doesn't need it (only
  Theorem B's effectivity does).

## PROVED (axiom-free)
* `isTR_one_of_isLISC` — Step 2 (extraction): read the `k` strands at each
  layer; injectivity of every `τ_i` is forced by simplicity, off-diagonality
  is not assumed.
* `isLISC_of_isTR_one` — Step 3 (assembly; KIT GAP 5.1): place position
  `t = jL + i` at state `τ_i[j]`; simplicity from layer-injectivity +
  injectivity of `τ_i`; strand boundaries including the closing step from
  the rotation endpoint. NO strong-connectivity hypothesis anywhere — `ρ`
  is an arbitrary relation on an arbitrary type.
* `isTR_rot_iff_isTR_one` — Step 4 (generator conjugation; KIT GAP 5.2):
  for `r` a UNIT of `ZMod k` (= `gcd(r,k) = 1`), the slot relabelling
  `u ∘ (· * r⁻¹)` conjugates `σ_1` to `σ_r`; the modular index bookkeeping
  `(j + r)·r̄ = j·r̄ + 1` is ring algebra in `ZMod k` — the exact three
  lines the kit asks to have checked, with no off-by-one possible.
* `pruning` — **Theorem P**: for `0 < k`, `0 < L`, `r` a unit:
  `IsLISC ρ k L ↔ IsTR ρ L r`. Exact for every `L`, every `ρ`. (The `k = 1`
  remark is the instance `k = 1`: `ZMod 1` is trivial and the rotation is
  the identity — nothing separate to state.)

## NOT formalized (recorded, honest)
* Lemma NG (non-generators overcount: `gcd(r,k) = d > 1` assembles `d`
  disjoint winding-`k/d` cycles): the orbit decomposition is extra
  bookkeeping on top of Step 3; the load-bearing kit gaps are 5.1/5.2,
  and NG's refutation half is machine-checked in the oracle
  (`pruning_k2_theorem.md` rot-check, C4dir witness). Future work if the
  lane needs it in Lean.
* Theorem B (kit gap 5.3: eventual periodicity of `Safe(ρ)`, the `k`-cap
  pigeonhole, union bookkeeping) — rides on Theorem P + a first-repeat
  argument; the instrument (`safe_rho_instrument.py`, 15 targets, 0 fail)
  covers the computational content. Not encoded here.

## Receipts
`#print axioms` at file end; everything `[propext, Classical.choice,
Quot.sound]`.
-/
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Push

open Function

namespace Reconstruction.Pruning

variable {α : Type*} (ρ : α → α → Prop)

/-- A winding-`k` **layer-injective simple cycle** in the layered ring
`R_L(ρ)`, by its state sequence on positions `< k*L` (see header for the
encoding). -/
def IsLISC (k L : ℕ) : Prop :=
  ∃ W : ℕ → α,
    (∀ t, t + 1 < k * L → ρ (W t) (W (t + 1))) ∧
    ρ (W (k * L - 1)) (W 0) ∧
    ∀ t₁ t₂, t₁ < k * L → t₂ < k * L → t₁ % L = t₂ % L → W t₁ = W t₂ →
      t₁ = t₂

/-- A length-`L` walk in the injective-tuple digraph `T_k(ρ)` from `u` to
`σ_r u` (rotation endpoint). Slots are `ZMod k`. -/
def IsTR {k : ℕ} (L : ℕ) (r : ZMod k) : Prop :=
  ∃ τ : ℕ → ZMod k → α,
    (∀ i ≤ L, Injective (τ i)) ∧
    (∀ i < L, ∀ j, ρ (τ i j) (τ (i + 1) j)) ∧
    ∀ j, τ L j = τ 0 (j + r)

variable {ρ} {k L : ℕ}

/-! ## Step 2: extraction (LISC ⟹ TR at the generator `1`) -/

theorem isTR_one_of_isLISC [NeZero k] (hL : 0 < L)
    (h : IsLISC ρ k L) : IsTR ρ L (1 : ZMod k) := by
  obtain ⟨W, hstep, hclose, hsimple⟩ := h
  have hk : 0 < k := Nat.pos_of_ne_zero (NeZero.ne k)
  have hsub : (k - 1) * L = k * L - L := Nat.sub_one_mul k L
  have hLle : L ≤ k * L := Nat.le_mul_of_pos_left L hk
  have hpos_lt : ∀ (j : ZMod k) (i : ℕ), i < L → j.val * L + i < k * L := by
    intro j i hi
    have h1 : j.val ≤ k - 1 := by have := ZMod.val_lt (n := k) j; omega
    have h2 : j.val * L ≤ (k - 1) * L := Nat.mul_le_mul_right L h1
    omega
  classical
  refine ⟨fun i j => if i = L then W ((j + 1).val * L) else W (j.val * L + i),
    ?_, ?_, ?_⟩
  · -- injectivity of every tuple, from simplicity
    intro i hi j₁ j₂ hval
    by_cases hiL : i = L
    · simp only [if_pos hiL] at hval
      have hlt : ∀ j : ZMod k, (j + 1).val * L < k * L := by
        intro j
        have h1 : (j + 1).val ≤ k - 1 := by
          have := ZMod.val_lt (n := k) (j + 1); omega
        have h2 : (j + 1).val * L ≤ (k - 1) * L := Nat.mul_le_mul_right L h1
        omega
      have heq := hsimple _ _ (hlt j₁) (hlt j₂)
        (by rw [Nat.mul_mod_left, Nat.mul_mod_left]) hval
      have hv : (j₁ + 1).val = (j₂ + 1).val :=
        Nat.eq_of_mul_eq_mul_right hL heq
      exact add_right_cancel (ZMod.val_injective k hv)
    · have hiL' : i < L := lt_of_le_of_ne hi hiL
      simp only [if_neg hiL] at hval
      have heq := hsimple _ _ (hpos_lt j₁ i hiL') (hpos_lt j₂ i hiL')
        (by rw [Nat.mul_add_mod', Nat.mul_add_mod']) hval
      have hv : j₁.val = j₂.val :=
        Nat.eq_of_mul_eq_mul_right hL (by omega)
      exact ZMod.val_injective k hv
  · -- coordinatewise arcs
    intro i hi j
    have hne : i ≠ L := by omega
    by_cases hi1 : i + 1 = L
    · simp only [if_neg hne, if_pos hi1]
      by_cases hjtop : j.val = k - 1
      · -- closing strand: position k*L − 1 steps to position 0
        have hj1val : (j + 1).val = 0 := by
          have hklt : k - 1 < k := by omega
          have hj : j = ((k - 1 : ℕ) : ZMod k) :=
            ZMod.val_injective k
              (by rw [ZMod.val_natCast_of_lt hklt]; exact hjtop)
          rw [hj]
          have h1 : ((k - 1 : ℕ) : ZMod k) + ((1 : ℕ) : ZMod k) =
              ((k - 1 + 1 : ℕ) : ZMod k) := (Nat.cast_add _ _).symm
          rw [Nat.cast_one] at h1
          rw [h1, show k - 1 + 1 = k by omega, ZMod.natCast_self,
            ZMod.val_zero]
        have hposition : j.val * L + i = k * L - 1 := by
          rw [hjtop]
          omega
        rw [hposition, hj1val, Nat.zero_mul]
        exact hclose
      · -- interior strand boundary: still a consecutive pair of W
        have hjlt : j.val < k - 1 := by
          have := ZMod.val_lt (n := k) j
          omega
        have hk2 : 1 < k := by omega
        haveI : Fact (1 < k) := ⟨hk2⟩
        have hj1 : (j + 1).val = j.val + 1 := by
          rw [ZMod.val_add_of_lt (by rw [ZMod.val_one]; omega), ZMod.val_one]
        have hlt : j.val * L + i + 1 < k * L := by
          have h1 : j.val + 1 ≤ k - 1 := by omega
          have h2 : (j.val + 1) * L ≤ (k - 1) * L := Nat.mul_le_mul_right L h1
          have h3 : (j.val + 1) * L = j.val * L + L := by ring
          omega
        have heq : (j + 1).val * L = j.val * L + i + 1 := by
          rw [hj1]
          have h3 : (j.val + 1) * L = j.val * L + L := by ring
          omega
        rw [heq]
        exact hstep _ hlt
    · simp only [if_neg hne, if_neg (hi1 : ¬ i + 1 = L)]
      exact hstep _ (by have := hpos_lt j (i + 1) (by omega); omega)
  · -- rotation endpoint
    intro j
    have hne : (0 : ℕ) ≠ L := by omega
    simp [hne]

/-! ## Step 3: assembly (TR at the generator `1` ⟹ LISC) — kit gap 5.1 -/

theorem isLISC_of_isTR_one [NeZero k] (hL : 0 < L)
    (h : IsTR ρ L (1 : ZMod k)) : IsLISC ρ k L := by
  obtain ⟨τ, hinj, harc, hend⟩ := h
  have hk : 0 < k := Nat.pos_of_ne_zero (NeZero.ne k)
  have hsub : (k - 1) * L = k * L - L := Nat.sub_one_mul k L
  have hLle : L ≤ k * L := Nat.le_mul_of_pos_left L hk
  refine ⟨fun t => τ (t % L) ((t / L : ℕ) : ZMod k), ?_, ?_, ?_⟩
  · -- ρ-steps between consecutive positions
    intro t ht
    by_cases hbound : t % L = L - 1
    · -- strand boundary
      have hmul : L * (t / L + 1) = L * (t / L) + L := by ring
      have hq : t + 1 = L * (t / L + 1) := by
        have := Nat.div_add_mod t L
        omega
      have h1 : (t + 1) % L = 0 := by
        rw [hq]
        exact Nat.mul_mod_right L _
      have h2 : (t + 1) / L = t / L + 1 := by
        rw [hq]
        exact Nat.mul_div_cancel_left _ hL
      have harc' := harc (t % L) (Nat.mod_lt t hL) ((t / L : ℕ) : ZMod k)
      rw [show t % L + 1 = L by omega, hend] at harc'
      have hcast : ((t / L : ℕ) : ZMod k) + 1 = ((t / L + 1 : ℕ) : ZMod k) := by
        push_cast
        ring
      rw [hcast] at harc'
      simpa only [h1, h2] using harc'
    · -- interior step
      have hqm := Nat.div_add_mod t L
      have hmlt : t % L < L := Nat.mod_lt t hL
      have hrw : t + 1 = L * (t / L) + (t % L + 1) := by omega
      have hlt : t % L + 1 < L := by omega
      have h1 : (t + 1) % L = t % L + 1 := by
        rw [hrw, Nat.mul_add_mod, Nat.mod_eq_of_lt hlt]
      have h2 : (t + 1) / L = t / L := by
        rw [hrw, Nat.mul_add_div hL, Nat.div_eq_of_lt hlt]
        omega
      simp only [h1, h2]
      exact harc (t % L) (by omega) _
  · -- the closing step
    have hlast : k * L - 1 = L * (k - 1) + (L - 1) := by
      rw [Nat.mul_comm L (k - 1)]
      omega
    have hL1 : L - 1 < L := by omega
    have hlast_mod : (k * L - 1) % L = L - 1 := by
      rw [hlast, Nat.mul_add_mod, Nat.mod_eq_of_lt hL1]
    have hlast_div : (k * L - 1) / L = k - 1 := by
      rw [hlast, Nat.mul_add_div hL, Nat.div_eq_of_lt hL1]
      omega
    have harc' := harc (L - 1) (by omega) (((k - 1 : ℕ)) : ZMod k)
    rw [show L - 1 + 1 = L by omega, hend] at harc'
    have hcast : ((k - 1 : ℕ) : ZMod k) + 1 = 0 := by
      have h1 : ((k - 1 : ℕ) : ZMod k) + ((1 : ℕ) : ZMod k) =
          ((k - 1 + 1 : ℕ) : ZMod k) := (Nat.cast_add _ _).symm
      rw [Nat.cast_one] at h1
      rw [h1, show k - 1 + 1 = k by omega, ZMod.natCast_self]
    rw [hcast] at harc'
    simpa only [hlast_mod, hlast_div, Nat.zero_mod, Nat.zero_div,
      Nat.cast_zero] using harc'
  · -- simplicity: layer + state determine the position
    intro t₁ t₂ h₁ h₂ hlayer hstate
    have hd₁ : t₁ / L < k := (Nat.div_lt_iff_lt_mul hL).mpr (by omega)
    have hd₂ : t₂ / L < k := (Nat.div_lt_iff_lt_mul hL).mpr (by omega)
    simp only [] at hstate
    rw [hlayer] at hstate
    have hj := hinj (t₂ % L) (le_of_lt (Nat.mod_lt t₂ hL)) hstate
    have hv : t₁ / L = t₂ / L := by
      have hval := congrArg ZMod.val hj
      rwa [ZMod.val_natCast_of_lt hd₁, ZMod.val_natCast_of_lt hd₂] at hval
    have e₁ := Nat.div_add_mod t₁ L
    have e₂ := Nat.div_add_mod t₂ L
    rw [hv] at e₁
    omega

/-! ## Step 4: generator conjugation — kit gap 5.2 -/

/-- For `r` a unit of `ZMod k` (`gcd(r,k) = 1`), rotation-`r` witnesses and
rotation-`1` witnesses relabel into each other: the slot bijection
`j ↦ j·r̄` conjugates the rotations, by `(j + r)·r̄ = j·r̄ + 1` — ring
algebra, no index chasing. -/
theorem isTR_rot_iff_isTR_one {r : ZMod k} (hr : IsUnit r) :
    IsTR ρ L r ↔ IsTR ρ L (1 : ZMod k) := by
  obtain ⟨u, rfl⟩ := hr
  constructor
  · rintro ⟨τ, hinj, harc, hend⟩
    refine ⟨fun i j => τ i (j * u), fun i hi j₁ j₂ h => ?_,
      fun i hi j => harc i hi _, fun j => ?_⟩
    · have h2 := hinj i hi h
      have h' := congrArg (fun x => x * ((u⁻¹ : (ZMod k)ˣ) : ZMod k)) h2
      simpa only [Units.mul_inv_cancel_right] using h'
    · change τ L (j * (u : ZMod k)) = τ 0 ((j + 1) * (u : ZMod k))
      rw [hend (j * (u : ZMod k))]
      congr 1
      ring
  · rintro ⟨τ, hinj, harc, hend⟩
    refine ⟨fun i j => τ i (j * ((u⁻¹ : (ZMod k)ˣ) : ZMod k)),
      fun i hi j₁ j₂ h => ?_, fun i hi j => harc i hi _, fun j => ?_⟩
    · have h2 := hinj i hi h
      have h' := congrArg (fun x => x * ((u : (ZMod k)ˣ) : ZMod k)) h2
      simpa only [Units.inv_mul_cancel_right] using h'
    · change τ L (j * ((u⁻¹ : (ZMod k)ˣ) : ZMod k)) =
        τ 0 ((j + (u : ZMod k)) * ((u⁻¹ : (ZMod k)ˣ) : ZMod k))
      rw [hend (j * ((u⁻¹ : (ZMod k)ˣ) : ZMod k))]
      congr 1
      rw [add_mul, u.mul_inv]

/-! ## Theorem P -/

/-- **Theorem P (pruning, phase-parametrized).** For every relation `ρ` on
any alphabet, every `L ≥ 1`, `k ≥ 1`, and every rotation `r` that generates
`ZMod k` (`gcd(r,k) = 1`): winding-`k` simple cycles in the layered ring
exist iff length-`L` rotation-`r` tuple walks do. Exact for every `L`; no
strong connectivity. -/
theorem pruning [NeZero k] (hL : 0 < L) {r : ZMod k} (hr : IsUnit r) :
    IsLISC ρ k L ↔ IsTR ρ L r := by
  rw [isTR_rot_iff_isTR_one hr]
  exact ⟨isTR_one_of_isLISC hL, isLISC_of_isTR_one hL⟩

/-! ## Receipts -/

#print axioms isTR_one_of_isLISC
#print axioms isLISC_of_isTR_one
#print axioms isTR_rot_iff_isTR_one
#print axioms pruning

end Reconstruction.Pruning
