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
1. **`delayMap_intertwines_shift`** — `Int.toNat` arithmetic + `Function.iterate`.
   Key question: can we prove `T^[n.toNat] (T x) = T^[(n+1).toNat] x` for all `n : ℤ`?
   For `n < 0`: `n.toNat = 0` and `(n+1).toNat` is 0 (if n+1 < 0) or 1 (if n+1 = 0),
   so the claim either says `T x = T x` (trivial) or `T x = T^[0] x = x` (false unless T = id).
   **Resolution**: the ℤ-indexed delay map with `n.toNat` is wrong for n < 0.
   Fix: index by ℕ or add `hn : 0 ≤ n`. Log attempts in flight log.

### Round 2 — MeasurableSpace.comap API
2. **`observableAlgebra_eq_comap`** — both directions via `generateFrom_le` +
   `comap_le_iff_le_map`. No instance issues since `mX` is the ambient typeclass.

### Round 3 — Submodule containment
3. **`cyclic_implies_dense`** — show `cyclicSpan ≤ lpMeas 𝒪_h`, then use
   `Submodule.topologicalClosure_mono`.

### Round 4 — lpMeas instance refactor (hardest)
4. **`lpMeasSubgroup_dense_in_Lp`** — requires section-variable rewrite of §2.
   Use `variable {m m0 : MeasurableSpace X}` + `(μ : @Measure X m0)` throughout.
5. **`lpMeas_eq_top_of_ae_eq`** — depends on 4.
6. **`reconstruction_iff_lpMeas` (←)** — depends on 4 and 5.

---

## Sorry inventory (current state: 2026-04-05)

| Sorry | Round | Status |
|-------|-------|--------|
| `delayMap_intertwines_shift` | 1 | 🔄 in progress |
| `observableAlgebra_eq_comap` | 2 | ⬜ queued |
| `cyclic_implies_dense` | 3 | ⬜ queued |
| `lpMeasSubgroup_dense_in_Lp` | 4 | ⬜ queued |
| `lpMeas_eq_top_of_ae_eq` | 4 | ⬜ queued |
| `reconstruction_iff_lpMeas` (←) | 4 | ⬜ queued |
