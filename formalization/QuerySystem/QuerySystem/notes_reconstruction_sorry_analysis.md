# ReconstructionTheorem.lean — Sorry Analysis (2026-04-27)

Two sorrys remain. Both are now analysable with specific Mathlib APIs identified.

---

## Sorry 1: `lpMeas_eq_top_of_ae_eq` (line 146)

### Statement
```lean
theorem lpMeas_eq_top_of_ae_eq [MeasurableSpace X] {m : MeasurableSpace X}
    (hm : m ≤ ‹MeasurableSpace X›) (μ : Measure X) [IsFiniteMeasure μ]
    (h_ae : ∀ s : Set X, MeasurableSet s →
        ∃ t : Set X, MeasurableSet[m] t ∧ μ (s ∆ t) = 0) :
    lpMeas ℝ ℝ m 2 μ = ⊤
```

### Key Mathlib APIs found
- `mem_lpMeas_iff_aestronglyMeasurable` (AEMeasurable.lean:101): `f ∈ lpMeas ↔ AEStronglyMeasurable[m] f μ`
- `mem_lpMeas_self` (AEMeasurable.lean:109): `f ∈ lpMeas F 𝕜 m0 p μ` (every Lp element is m0-measurable)
- `measure_symmDiff_eq_zero_iff` (OuterMeasure/AE.lean:176): `μ (s △ t) = 0 ↔ s =ᵐ[μ] t`
- `lpMeasToLpTrimLie` (AEMeasurable.lean:287): `LinearIsometryEquiv` between `lpMeas F 𝕜 m p μ` and `Lp F p (μ.trim hm)` — implies lpMeas is closed
- `isClosed_aestronglyMeasurable` (AEMeasurable.lean:314): `IsClosed {f : Lp F p μ | AEStronglyMeasurable[m] f μ}` (requires `Fact (1 ≤ p)` and `CompleteSpace F`)
- `AEStronglyMeasurable.mono` (AEStronglyMeasurable.lean:189): `m ≤ m' → AEStronglyMeasurable[m] → AEStronglyMeasurable[m']` (upward only)
- `aestronglyMeasurable_of_aestronglyMeasurable_trim` (AEStronglyMeasurable.lean:560): `AEStronglyMeasurable[m] f (μ.trim hm) → AEStronglyMeasurable[m] f μ`
- `Lp.induction_stronglyMeasurable` (AEMeasurable.lean:411): induction on lpMeas — for functions ALREADY in lpMeas

### Proof path

The hypothesis `h_ae` says: every m0-set has an m-version up to null sets, i.e., m0 ≤ m mod μ.

**Step 1**: Goal is `Submodule.eq_top_iff'.mpr`: show every `f : Lp ℝ 2 μ` is in `lpMeas ℝ ℝ m 2 μ`, i.e., has `AEStronglyMeasurable[m] f μ`.

**Step 2**: Use `lpMeasToLpTrimLie` surjectivity: the map from `lpMeas F 𝕜 m p μ` to `Lp F p (μ.trim hm)` is a `LinearIsometryEquiv`. The inverse `lpTrimToLpMeas` sends any `g : Lp ℝ 2 (μ.trim hm)` to an element of `lpMeas ℝ ℝ m 2 μ`. So `lpMeas` is in bijection with `Lp ℝ 2 (μ.trim hm)`.

**Step 3**: Under `h_ae`, `μ.trim hm` and `μ` have the same measurable sets up to null sets. The trim measure `μ.trim hm` satisfies: for every `m0`-measurable `s`, `μ.trim hm s = μ s` (since there exists an `m`-measurable `t` with `μ(s △ t) = 0`, so `μ s = μ t = μ.trim hm t`, and... wait, `μ.trim hm` only sees `m`-measurable sets directly).

Actually the cleaner path: show `Lp ℝ 2 μ = Lp ℝ 2 (μ.trim hm)` as sets is NOT right. The measures are on different σ-algebras.

**Better path via density**:

The correct strategy is:
1. `lpMeas` is a **closed** subspace of `Lp ℝ 2 μ` (from `isClosed_aestronglyMeasurable`, which needs `Fact (1 ≤ 2)` and `CompleteSpace ℝ`).
2. `lpMeas` contains a **dense** subset of `Lp ℝ 2 μ`.
3. Therefore `lpMeas = ⊤`.

For step 2: We show m0-simple functions are in `lpMeas`. Each m0-simple function is a finite linear combination of indicators `𝟙_s` for m0-measurable sets `s`. By `h_ae`, each such `𝟙_s =ᵐ[μ] 𝟙_t` for some m-measurable `t`. So `𝟙_s` is `AEStronglyMeasurable[m]`, hence in `lpMeas`. Since m0-simple functions are dense in `Lp ℝ 2 μ` (by `Lp.simpleFunc.dense`) and all lie in the closed subspace `lpMeas`, we get `lpMeas = ⊤`.

**Key gap**: showing `𝟙_s ∈ lpMeas` from `h_ae`. Specifically:
- `h_ae s hs` gives `t, ht : MeasurableSet[m] t, hst : μ (s △ t) = 0`
- `measure_symmDiff_eq_zero_iff.mp hst : s =ᵐ[μ] t`  (this requires checking the `.mp` direction)
- Then `𝟙_s =ᵐ[μ] 𝟙_t` (measurability of indicator, congr a.e.)
- `𝟙_t` is `StronglyMeasurable[m]` (from `ht`)
- So `𝟙_s` is `AEStronglyMeasurable[m]` (by `congr`)

**For the full simple function**: each `indicatorConstLp p (hm s hs') hμs c` is already in `lpMeas` when `s` is m-measurable (by `mem_lpMeas_indicatorConstLp`). But we need this for m0-measurable sets. We use h_ae to replace s with t.

**Remaining Lean challenge**: The `Lp.simpleFunc.indicatorConst` in `Lp` vs. plain `𝟙_s ∈ Lp`. Need to connect `Lp.simpleFunc.dense` (which gives density in `Lp ℝ 2 μ`) with elements that are in `lpMeas`. The induction lemma `Lp.induction_stronglyMeasurable_aux` requires `AEStronglyMeasurable[m]` as a hypothesis — so it won't help here.

**Clean Lean proof sketch**:
```lean
theorem lpMeas_eq_top_of_ae_eq ... := by
  apply Submodule.eq_top_iff'.mpr
  intro f
  -- f : Lp ℝ 2 μ, goal: f ∈ lpMeas ℝ ℝ m 2 μ
  rw [mem_lpMeas_iff_aestronglyMeasurable]
  -- goal: AEStronglyMeasurable[m] f μ
  -- Strategy: lpMeas is closed, m0-simple functions in lpMeas are dense → lpMeas = ⊤
  -- Use: every f is in the closure of m0-simple functions (by Lp.simpleFunc.dense applied to μ),
  -- and each m0-simple function is AEStronglyMeasurable[m] (via h_ae).
  -- Then closed set containing dense set = everything.
  sorry
```

The proof requires the closedness of `{f | AEStronglyMeasurable[m] f μ}` in `Lp ℝ 2 μ` (available) plus density of a subset (harder to formalize directly without more infrastructure).

**Alternative via `lpTrimToLpMeas` surjectivity**: if we can show that `Lp ℝ 2 μ` and `Lp ℝ 2 (μ.trim hm)` are isometric (under `h_ae`), then `lpMeas` is all of `Lp ℝ 2 μ`. But this requires showing `μ.trim hm = μ` as measures on (m0), which is NOT true in general — `μ.trim hm` lives on m, not m0. This path is blocked.

### Current status: **partial** — mathematical path is clear, Lean formalization requires careful assembly

---

## Sorry 2: `reconstruction_iff_lpMeas` ← direction (line 171)

### Statement
```lean
  · intro _h_dense s _hs
    sorry
    -- goal: ∃ t, MeasurableSet[m] t ∧ μ (s △ t) = 0
```

Given: `h_dense : Dense (lpMeas ℝ ℝ m 2 μ : Set (Lp ℝ 2 μ))`, `s : Set X`, `hs : MeasurableSet s`.

### Key Mathlib APIs found
- `tendstoInMeasure_of_tendsto_Lp` (LpOrder.lean): Lp convergence → convergence in measure
- `TendstoInMeasure.exists_seq_tendsto_ae` (ConvergenceInMeasure.lean:33): convergence in measure → a.e. convergent subsequence
- `measure_symmDiff_eq_zero_iff` (OuterMeasure/AE.lean:176): `μ (s △ t) = 0 ↔ s =ᵐ[μ] t`

### Proof path

1. Let `f = indicatorConstLp 2 hs hμs (1 : ℝ)` (the indicator of `s` in `Lp ℝ 2 μ`). Here `hμs : μ s ≠ ∞` is needed; use `measure_lt_top μ s` since `μ` is finite.
2. By density, there exists a sequence `(fₙ)` in `lpMeas` with `‖fₙ - f‖ → 0` in `Lp`.
3. `tendstoInMeasure_of_tendsto_Lp` gives `fₙ → f` in measure.
4. `TendstoInMeasure.exists_seq_tendsto_ae` gives a subsequence `fₙₖ →ᵃᵉ f`.
5. Each `fₙₖ` is `AEStronglyMeasurable[m]`, so has an m-measurable version `gₙₖ`.
6. The a.e. limit `f` is a.e. equal to an m-measurable function (the pointwise limit of m-measurable functions is m-measurable).
7. But `f = 𝟙_s` a.e., and if `f =ᵐ[μ] g` for m-measurable `g`, then the level set `{g ≥ 1/2}` is m-measurable, and `μ (s △ {g ≥ 1/2}) = 0`.

### Remaining Lean challenges
- Step 6 requires: measurability of a.e.-pointwise limit. In Lean: `AEStronglyMeasurable.ae_seq_tendsto` and `MeasurableSpace.measurable_of_tendsto_measurable` or `Measurable.measurable_of_tendsto_nhds`. Need to check what's available for **pointwise** a.e. limits of m-strongly-measurable functions.
- Key lemma needed: if `(gₙ)` are `StronglyMeasurable[m]` and `gₙ →ᵃᵉ h`, then `AEStronglyMeasurable[m] h μ`. This is `MeasureTheory.aestronglyMeasurable_of_tendsto_ae` or similar.
- Step 7: extracting the m-measurable set from the a.e.-m-measurable indicator function.

### Search still needed
- `aestronglyMeasurable_of_tendsto_ae` or `tendsto_ae_aestronglyMeasurable` in Mathlib
- `AEStronglyMeasurable.indicator` inverse: from `f =ᵐ[μ] 𝟙_s` and `AEStronglyMeasurable[m] f`, extract `t` with `MeasurableSet[m] t` and `s =ᵐ[μ] t`

---

## Summary table (updated)

| Sorry | Strategy | Key gap | Status |
|-------|----------|---------|--------|
| `lpMeas_eq_top_of_ae_eq` | Closed subspace + dense subset = ⊤ | Assembling: closedness (have it) + indicator a.e. equivalence + Lp.simpleFunc.dense | Path clear, needs Lean assembly |
| `reconstruction_iff_lpMeas` ←  | Density → Lp approx → in-measure → a.e. convergence → m-measurable limit | Need `aestronglyMeasurable_of_tendsto_ae`; need indicator inverse lemma | One more Mathlib search needed |

---

## Files consulted (2026-04-27)

- `Mathlib/MeasureTheory/Function/ConditionalExpectation/AEMeasurable.lean` — `lpMeas`, `lpMeasToLpTrimLie`, `isClosed_aestronglyMeasurable`, `Lp.induction_stronglyMeasurable`
- `Mathlib/MeasureTheory/Function/StronglyMeasurable/AEStronglyMeasurable.lean` — `AEStronglyMeasurable.mono`, `aestronglyMeasurable_of_aestronglyMeasurable_trim`
- `Mathlib/MeasureTheory/Measure/Trim.lean` — `trim_measurableSet_eq`, `ae_eq_of_ae_eq_trim`
- `Mathlib/MeasureTheory/OuterMeasure/AE.lean` — `measure_symmDiff_eq_zero_iff`
- `Mathlib/MeasureTheory/Function/ConvergenceInMeasure.lean` — `TendstoInMeasure.exists_seq_tendsto_ae`
- `Mathlib/MeasureTheory/Function/LpOrder.lean` — `tendstoInMeasure_of_tendsto_Lp`
