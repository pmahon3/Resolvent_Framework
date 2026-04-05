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

## Sorry-closing plan (2026-04-05)

Attack order by difficulty (easiest first):

### Round 1 — Pure logic/arithmetic (no instance issues)
1. **`delayMap_intertwines_shift`** ✅ **CLOSED** — Fixed by indexing `delayMap` by `ℕ` instead of `ℤ`.
   The ℤ-indexed version with `n.toNat` is mathematically wrong for `n < 0`.
   Fix: changed `delayMap : X → (ℕ → ℝ)` and `unilateralShift : (ℕ → ℝ) → (ℕ → ℝ)`.
   Proof: `simp only [delayMap, unilateralShift, Function.iterate_succ_apply]` — closes in one line.
   `Function.iterate_succ_apply : f^[n+1] a = f^[n] (f a)` is exactly what's needed.

### Round 2 — MeasurableSpace.comap API ✅ CLOSED
2. **`observableAlgebra_eq_comap`** ✅ — proved equality of two `MeasurableSpace X` instances.

   **Goal:**
   ```lean
   observableAlgebra (fun n : ℤ => h ∘ T^[n.toNat]) =
   MeasurableSpace.comap (delayMap h T) (MeasurableSpace.pi (m := fun (_ : ℕ) => inferInstance))
   ```

   **Strategy:** `le_antisymm` + two `≤` proofs.

   **(≤) direction** — `observableAlgebra ≤ comap`:
   Use `observableAlgebra_le`. Need: for each `n : ℤ`, `h ∘ T^[n.toNat]` is measurable
   w.r.t. `comap (delayMap h T) (pi ...)`.
   Key: `h ∘ T^[n.toNat] = (fun f : ℕ → ℝ => f n.toNat) ∘ delayMap h T`.
   The coordinate projection `(fun f => f k) : (ℕ → ℝ) → ℝ` is measurable w.r.t. `pi`,
   so its composition with `delayMap h T` is `comap`-measurable.
   Lean path: `Measurable.comp (measurable_pi_apply n.toNat) (delayMap_measurable ...)` — but
   need to show this gives measurability w.r.t. `comap`. Use `MeasurableSpace.measurable_comap`.

   **(≥) direction** — `comap ≤ observableAlgebra`:
   The comap is the smallest σ-algebra making `delayMap h T` measurable.
   So it suffices to show `delayMap h T` is measurable w.r.t. `observableAlgebra`.
   `delayMap h T x n = h (T^[n] x)` — each coordinate `n : ℕ` is `observableAlgebra`-measurable
   by `observableAlgebra_measurable` (since `n : ℕ` embeds into `ℤ` as `(n : ℤ)` with `.toNat = n`).
   Lean path: `MeasurableSpace.comap_le_iff_le_map.mpr` or direct use of
   `MeasurableSpace.le_comap_iff` (if it exists).

   **Key Mathlib lemmas to check:**
   - `MeasurableSpace.comap_le_iff_le_map` (direction: `comap f m ≤ m' ↔ m ≤ map f m'`)
   - `MeasurableSpace.measurable_iff_comap_le` (measurability iff comap ≤ ambient)
   - `MeasurableSpace.pi` — product measurable space on `ℕ → ℝ`
   - `measurable_pi_apply` — coordinate projections are measurable

   **Potential issue:** The `observableAlgebra` uses `n : ℤ` generators but `delayMap` is ℕ-indexed.
   For the `≥` direction, we need `(n : ℕ)` generators to match. Since `(n : ℤ).toNat = n` for
   `n : ℕ` (after coercion), the generators for `k : ℕ` are `h ∘ T^[k]` — exactly the
   coordinates of `delayMap`. The ℤ generators with `n < 0` all reduce to `h ∘ T^[0]` which
   is also a ℕ generator, so they don't add anything new.

   **Approach if `comap_le_iff_le_map` is hard to use:**
   Prove equality as two `generateFrom_le` applications on both sides after unfolding comap.

### Round 3 — Submodule containment ✅ CLOSED
3. **`cyclic_implies_dense`** ✅ — Key steps:
   1. `aestronglyMeasurable_congr (hmem n).coeFn_toLp` to reduce from Lp coercion to `h ∘ T^[n]`
   2. `observableAlgebra_measurable ... .aestronglyMeasurable` for each generator
   3. `Submodule.span_le.mpr` + `Submodule.topologicalClosure_mono`
   4. `Submodule.dense_iff_topologicalClosure_eq_top` + `top_le_iff.mp`

### Round 4 — lpMeas/trim API (hardest; genuine Mathlib gaps)

4. **`lpMeas_eq_top_of_ae_eq`** — If every `m0`-set has an `m`-a.e.-equal version,
   then every `f : Lp ℝ 2 μ` is a.e. `m`-strongly-measurable.
   The argument requires: `AEStronglyMeasurable[m0] f μ` + (m = m0 mod μ) → `AEStronglyMeasurable[m] f μ`.
   No direct Mathlib lemma found. Nearest: `AEStronglyMeasurable.mono` goes the wrong direction (m → m').
   **Mathlib gap**: needs `aestronglyMeasurable_of_ae_measurableSpace_eq` or similar.

5. **`reconstruction_iff_lpMeas` (←)** — Dense `lpMeas m` → every `m0`-set has an `m`-version a.e.
   Argument: approximate `𝟙_s` in L² by `lpMeas m` elements; each approximant is a.e. `m`-measurable;
   take a subsequence converging a.e.; the a.e. limit is 0 or 1 a.e. and `m`-measurable.
   **Mathlib gap**: needs `tendsto_ae_of_tendsto_Lp` + measurability of the a.e. limit.

6. **`lpMeasSubgroup_dense_in_Lp`** — NOT USED by the current file; deferred.
   Note: this lemma as stated (for general m ≤ m0) is FALSE. Density holds only when m = m0.
   Correctly stated: `lpMeasSubgroup ≅ Lp(μ.trim hm)` is dense in `Lp(μ)` iff `μ.trim hm = μ`.

---

## Sorry inventory (current state: 2026-04-05)

| Sorry | Round | Status |
|-------|-------|--------|
| `delayMap_intertwines_shift` | 1 | ✅ closed |
| `observableAlgebra_eq_comap` | 2 | ✅ closed |
| `cyclic_implies_dense` | 3 | ✅ closed |
| `lpMeasSubgroup_dense_in_Lp` | 4 | ⚠️ deferred — FALSE for general `m ≤ m0`; not used by file |
| `lpMeas_eq_top_of_ae_eq` | 4 | ⬜ Mathlib gap — no downward `AEStronglyMeasurable` monotonicity |
| `reconstruction_iff_lpMeas` (←) | 4 | ⬜ Mathlib gap — a.e.-convergent subsequence from Lp convergence |

---

## DelayEmbedding bridge (2026-04-05)

`DelayEmbedding.lean` now imports `ReconstructionTheorem.lean` and provides
`section ReconstructionBridge` with:

| Declaration | Status |
|-------------|--------|
| `delayObservableAlgebra` | ✅ compiles |
| `delayObservableAlgebra_eq_comap` | ✅ = `observableAlgebra_eq_comap` |
| `delayMap_shift_intertwining` | ✅ = `delayMap_intertwines_shift` |
| `delay_cyclic_implies_reconstruction` | ✅ = `cyclic_implies_dense` |
| `delay_reconstruction_iff` | ⚠️ sorry — two-MeasurableSpace elaboration; Lean resolves `[MeasurableSpace X]` as `delayObservableAlgebra h T` preventing call to `reconstruction_iff_lpMeas` |
