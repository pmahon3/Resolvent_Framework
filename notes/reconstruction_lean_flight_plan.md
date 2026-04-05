# ReconstructionTheorem.lean — Flight Plan

## Goal

Formalize Paper III in `QuerySystem/ReconstructionTheorem.lean`.

The file structure mirrors the paper:
1. Observable algebra (`observableAlgebra`)
2. Density bridge (`density_bridge`, `lpMeas_eq_top_of_ae_eq`)
3. Reconstruction theorem, (i)↔(ii) (`reconstruction_iff_lpMeas`)
4. Delay map and pullback (`delayMap`, `delayMap_pullback_le`)
5. Shift intertwining (`delayMap_intertwines_shift`)
6. Cyclic vector → reconstruction (`cyclic_implies_dense`)

---

## Status (2026-04-04)

### Done ✅

- `observableAlgebra`: definition compiles
- `observableAlgebra_measurable`: compiles
- `observableAlgebra_le`: compiles
- `delayMap`: definition compiles
- `delayMap_measurable`: compiles
- `bilateralShift`: definition compiles
- `density_bridge`: compiles (`Lp.simpleFunc.dense`)

### In progress / blocked

The file currently has **compile errors** from API mismatch between
the paper-level abstractions and Mathlib's concrete `lpMeas` API.
See §Mathlib API notes below.

---

## Mathlib API notes

### `lpMeas` signature

```lean
def lpMeas (F 𝕜 : Type*) [NormedField 𝕜] [NormedAddCommGroup F] [NormedSpace 𝕜 F]
    (m : MeasurableSpace α) [MeasurableSpace α] (p : ℝ≥0∞) (μ : Measure α) :
    Submodule 𝕜 (Lp F p μ)
```

Invocation: `lpMeas ℝ ℝ m p μ` (all arguments positional).

### `lpMeasSubgroup` / density

- `lpMeasSubgroupToLpTrimIso` (`isometry_lpMeasSubgroupToLpTrim`): isometric iso
  between `lpMeasSubgroup F m p μ` and `Lp F p (μ.trim hm)`
- `Lp.simpleFunc.dense` (p ≠ ∞): simple functions dense in `Lp F p ν`
- **No direct `lpMeas_dense` lemma in Mathlib.**
  Density proof path: isometry + `dense_range` of the iso + `Lp.simpleFunc.dense`

### `symmDiff`

- Need `open scoped symmDiff` for `∆` notation
- `μ (s ∆ t)` has type `ℝ≥0∞`
- `measure_symmDiff_eq_zero_iff`: `μ (s ∆ t) = 0 ↔ s =ᵐ[μ] t`

### `MeasurableSpace.generateFrom` and `rintro`

The `generateFrom_le` callback gives a `Set X` in the generating set.
**Cannot** `rintro ⟨n, E, hE, rfl⟩` directly — must `simp only [Set.mem_iUnion]`
first, then `obtain ⟨n, E, hE, rfl⟩ := hs`.

Pattern:
```lean
apply MeasurableSpace.generateFrom_le
intro s hs
simp only [Set.mem_iUnion, Set.mem_setOf_eq] at hs
obtain ⟨n, E, hE, rfl⟩ := hs
```

### `MeasurableSpace.comap` and product σ-algebra

`MeasurableSpace.pi (m := fun (_ : ℤ) => inferInstance)` — the product σ-algebra
on `ℤ → ℝ`. The `comap_le_iff_le_map` rewrite goes the wrong direction for our use.
Better approach: show `observableAlgebra_le` directly by noting each coordinate map
`(fun f : ℤ → ℝ => f n) ∘ Φ_h = h ∘ T^[n.toNat]` is `𝒪_h`-measurable.

### `delayMap_intertwines_shift` sorry

Goal after `congr 1`: `T^[n.toNat] (T x) = T^[(n + 1).toNat] x`

For `n : ℤ` (with `n ≥ 0` implicit in `n.toNat` semantics):
- `(n + 1).toNat = n.toNat + 1` — need `Int.toNat_add_one` (requires `0 ≤ n`)
- `T^[k + 1] y = T (T^[k] y)` — `Function.iterate_succ_apply`

The full ℤ-indexed version requires `T` to be invertible (for negative lags).
Since we only use `n.toNat` (which maps negative n to 0), the claim holds vacuously
for n < 0 but the intertwining only works cleanly for n ≥ 0.
**Resolution**: use n ∈ ℕ in the delay map, or add `hn : 0 ≤ n` hypothesis.

---

## Task breakdown

| Task | API blocker | Mathlib path |
|------|------------|--------------|
| `density_bridge` ✅ | none | `Lp.simpleFunc.dense` |
| `lpMeas_dense_in_itself` | no direct lemma | `lpMeasSubgroupToLpTrimIso` + `DenseRange` of isometric embedding |
| `lpMeas_eq_top_of_ae_eq` | sorry | approximation + a.e. measurability |
| `reconstruction_iff_lpMeas` (→) | sorry in `lpMeas_eq_top` | depends above |
| `reconstruction_iff_lpMeas` (←) | sorry | `Dense.exists_seq_tendsto` + a.e. subsequence |
| `delayMap_pullback_le` ✅ | `comap_le_iff_le_map` direction | via `generateFrom_le` |
| `observableAlgebra_le_pullback` | API mismatch | `Measurable.comp` |
| `delayMap_intertwines_shift` | sorry | `Int.toNat_add_one` + invertibility |
| `cyclic_implies_dense` | sorry | span ≤ lpMeas + monotone closure |

---

## Next actions

1. Fix remaining compile errors in the file (lpMeas API, comap direction)
2. Attempt to close `lpMeas_dense_in_itself` via `lpMeasSubgroupToLpTrimIso`
3. Attempt `delayMap_intertwines_shift` by restricting to n : ℕ
4. Leave `lpMeas_eq_top_of_ae_eq` and `reconstruction_iff_lpMeas` (←) as intentional sorrys
   with documented proof sketches

---

## Sorry inventory target

| Sorry | Type | Notes |
|-------|------|-------|
| `lpMeas_eq_top_of_ae_eq` | Mathlib API gap | approximation argument; provable but needs `ae_measurable_of_measurable_mod_null` |
| `reconstruction_iff_lpMeas` (←) | Mathlib API gap | a.e.-convergent subsequence extraction |
| `delayMap_intertwines_shift` | Scope note | clean for n : ℕ; ℤ version needs invertibility |
| `cyclic_implies_dense` | Scope/API | span ≤ Submodule containment |
| `cyclicSpan` MemLp bound | Scope note | measure-preservation; provable with T_*μ = μ |
