# Lean Formalization Flight Log

Running log of non-trivial Lean errors, attempted fixes, and outcomes.
Updated as work progresses. Most recent entry at top.

---

## 2026-04-27 — ReconstructionTheorem.lean (closing lpMeas_eq_top_of_ae_eq)

### Goal

Close `lpMeas_eq_top_of_ae_eq` (Sorry 1 of 2) in `ReconstructionTheorem.lean`.

**Mathematical plan:**
1. `isClosed_aestronglyMeasurable` — `lpMeas ℝ ℝ m 2 μ` is closed.
2. `induction s using MeasureTheory.SimpleFunc.induction` — every Lp simple function
   has an `m`-version a.e., using `h_ae` for the `const` case.
3. `Lp.simpleFunc.dense` — Lp simple functions are dense in `Lp ℝ 2 μ`.
4. `Dense.mono hsubset` — `lpMeas` is dense (contains a dense subset).
5. Closed + dense = ⊤ via `IsClosed.closure_eq` + `Dense.closure_eq`.

### Problem: `simp only [SetLike.mem_coe] at hf; obtain ⟨φ, rfl⟩ := hf`

**File:** `ReconstructionTheorem.lean`, `hsubset` inside `lpMeas_eq_top_of_ae_eq`

**Symptom:**
```
error: QuerySystem/ReconstructionTheorem.lean:191:13:
  Invalid `⟨...⟩` notation: The expected type of this term could not be determined
```

**Root cause:** `simp only [SetLike.mem_coe]` transforms `hf : f ∈ (Lp.simpleFunc ℝ 2 μ : Set (Lp ℝ 2 μ))` but leaves the type in a form `obtain ⟨φ, rfl⟩` cannot pattern-match (expected type is not exposed as an existential).

**Fix:** `Lp.simpleFunc ℝ 2 μ` is an `AddSubgroup`, so membership `hf : f ∈ Lp.simpleFunc ℝ 2 μ` is an `AddSubgroup` membership proposition — not an existential. The subtype term is `⟨f, hf⟩ : Lp.simpleFunc ℝ 2 μ`. Replace the `simp + obtain` block with:
```lean
exact hmem ⟨f, hf⟩
```
The coercion `↑⟨f, hf⟩ = f` is definitional, so `hmem ⟨f, hf⟩` has type `(⟨f, hf⟩ : Lp.simpleFunc ℝ 2 μ : Lp ℝ 2 μ) ∈ lpMeas ...`, which reduces to `f ∈ lpMeas ...`.

**Lesson:** For `AddSubgroup`-backed sets, membership is a proposition, not an existential. Package `⟨f, hf⟩` into the subtype directly. Do not use `simp [SetLike.mem_coe]` + `obtain ⟨φ, rfl⟩`.

**Status:** RESOLVED ✅ (2026-04-27). `lpMeas_eq_top_of_ae_eq` closed. Build clean.

### Problem: `reconstruction_iff_lpMeas` ← direction (Sorry 2)

**File:** `ReconstructionTheorem.lean`, `reconstruction_iff_lpMeas`

**Goal:** `Dense (lpMeas ℝ ℝ m 2 μ) → ∀ s, MeasurableSet s → ∃ t, MeasurableSet[m] t ∧ μ(s △ t) = 0`

**Key insight:** The sorry inventory's description ("tendsto_ae_of_tendsto_Lp not in Mathlib") was a red herring. The proof does NOT need convergence-in-measure. It follows by:
1. `lpMeas` is closed (`isClosed_aestronglyMeasurable`) + dense (hypothesis) → `lpMeas = ⊤` (same argument as → direction)
2. Build `𝟙_s ∈ Lp ℝ 2 μ` via `memLp_indicator_const 2 hs 1 (Or.inr (measure_ne_top μ s))` + `MemLp.toLp`
3. `f_lp ∈ ⊤ = lpMeas` → `AEStronglyMeasurable[m] f_lp μ` via `mem_lpMeas_iff_aestronglyMeasurable`
4. Get rep `g := haesm.mk f_lp` with `Measurable[m] g` and `𝟙_s =ᵐ[μ] g` (via `coeFn_toLp` + `ae_eq_mk`)
5. Set `t := g⁻¹' Ioi 0`: `MeasurableSet[m] t` from `hgm measurableSet_Ioi`; `s =ᵐ[μ] t` via `filter_upwards` + `Set.indicator_of_mem`/`Set.indicator_of_notMem` + `linarith`

**Pitfalls:**
- `filter_upwards ... with x hx` gives pointwise Prop *equality* (not iff) goal — must use `propext` before `constructor`
- `simp [Set.mem_preimage, Set.mem_Ioi]` often makes no progress when the goal is already in the right form; use `Set.mem_preimage.mpr`, `Set.mem_Ioi.mp` directly
- `Set.indicator_of_not_mem` — WRONG name. Correct: `Set.indicator_of_notMem`

**Status:** RESOLVED ✅ (2026-04-27). Both sorrys in `ReconstructionTheorem.lean` closed. File now has 0 sorrys.

---

## 2026-04-05 — ReconstructionTheorem.lean (cleanup) + Paper III revision

### Action: deleted `lpMeasSubgroup_dense_in_Lp`

**Reason:** The lemma was (a) unused by any proof in the file and (b) mathematically
false as stated: `lpMeasSubgroup ℝ m 2 μ` is NOT dense in `Lp ℝ 2 μ` for general
`m ≤ m0` — density holds only when `m = m0` mod `μ`, which is the content of the
reconstruction theorem itself. Keeping it as a sorry was misleading.

**Lesson:** Before parking a sorry, check whether the statement is actually true.
Density-via-isometry arguments (`lpMeasSubgroupToLpTrimIso`) transfer density from
`Lp(μ.trim hm)` to the subgroup, but `Lp(μ.trim hm)` is only isometrically embedded
in `Lp μ` when `μ.trim hm = μ`, i.e., when `m = m0`.

### Problem: `delay_reconstruction_iff` — two-instance elaboration in DelayEmbedding.lean

**File:** `DelayEmbedding.lean`, `section ReconstructionBridge`

**Symptom:** Any attempt to apply `reconstruction_iff_lpMeas` from `DelayEmbedding.lean`
with `m := delayObservableAlgebra h T` fails. Lean resolves `[MeasurableSpace X]` as
`delayObservableAlgebra h T` rather than the ambient `mX`, so the hypothesis
`hm : delayObservableAlgebra h T ≤ ‹MeasurableSpace X›` can't be discharged.

**Root cause:** `delayObservableAlgebra h T : MeasurableSpace X` is a term of the
right type to be synthesized as the `[MeasurableSpace X]` instance. Lean's instance
synthesis is greedy: any `MeasurableSpace X` in scope can be picked. Since
`reconstruction_iff_lpMeas` takes `[MeasurableSpace X]` as the ambient σ-algebra,
the call site in `DelayEmbedding.lean` can't force it to use the imported ambient
rather than the locally-defined sub-σ-algebra.

**Attempts:**
- `@reconstruction_iff_lpMeas X mX (delayObservableAlgebra h T) hm μ _` — failed,
  `mX` and the synthesized instance still clash in downstream terms
- `haveI : MeasurableSpace X := mX` — no effect on synthesis
- Moving the theorem into a `section` with explicit `variable [mX : MeasurableSpace X]`
  — the import boundary means the variable is re-synthesized at the call site

**Resolution:** Left as documented sorry with explanation. The mathematical content
is correct; the issue is purely elaboration. Will resolve if/when `reconstruction_iff_lpMeas`
is refactored to use explicit (not typeclass) `MeasurableSpace` arguments.

**Lesson:** When a file imports another and both involve two `MeasurableSpace X`
instances (ambient + sub-σ-algebra), typeclass-based theorems from the imported file
cannot be reliably called with the sub-σ-algebra as the ambient instance. Use
explicit `@` application with named instances, or restructure to pass both σ-algebras
explicitly (no `[MeasurableSpace X]` typeclass in the signature).

---

## 2026-04-05 — ReconstructionTheorem.lean (sorry-closing session)

### Problem: `observableAlgebra_eq_comap` — MeasurableSpace.pi vs comap

**Goal:**
```lean
observableAlgebra (fun n : ℤ => h ∘ T^[n.toNat]) =
MeasurableSpace.comap (delayMap h T) (MeasurableSpace.pi (m := fun (_ : ℕ) => inferInstance))
```

**≤ direction** — each generator factors through `delayMap h T`:
```lean
have hfactor : h ∘ T^[n.toNat] = (fun f : ℕ → ℝ => f n.toNat) ∘ delayMap h T := rfl
rw [hfactor]
exact (measurable_pi_apply n.toNat).comp (measurable_iff_comap_le.mpr le_rfl)
```
Key: `measurable_iff_comap_le.mpr le_rfl` says `id` is comap-measurable; `measurable_pi_apply` composed with it gives the result.

**≥ direction** — unfold `pi` as `iSup`, then show each summand:
```lean
simp only [MeasurableSpace.pi, MeasurableSpace.comap_iSup, MeasurableSpace.comap_comp]
apply iSup_le; intro n
apply measurable_iff_comap_le.mp
-- prove (fun b => b n) ∘ delayMap h T = generator at (n : ℤ) by funext + simp
```
Key: `MeasurableSpace.pi = ⨆ a, comap (eval a) inferInstance` (from `Constructions.lean:566`).
After `simp [comap_iSup, comap_comp]` the goal becomes `comap (eval n ∘ delayMap h T) ℝ ≤ observableAlgebra`.
Use `measurable_iff_comap_le.mp` + `observableAlgebra_measurable`.

**Lesson:** When working with `MeasurableSpace.pi`, unfold with `simp [MeasurableSpace.pi, comap_iSup, comap_comp]` to expose the `iSup` structure. Do NOT try `measurable_pi_iff` with an explicit source measurable space — instance inference breaks.

---

## 2026-04-04 — ReconstructionTheorem.lean

### Problem: Two-MeasurableSpace-instance issue

**File:** `ReconstructionTheorem.lean`, all theorems involving `Measure.trim`

**Symptom:**
```
error: synthesized type class instance is not definitionally equal to expression
       inferred by typing rules
```
When writing `μ.trim hm` with `{m m0 : MeasurableSpace X}` and `μ : Measure X`,
Lean synthesizes a *different* `MeasurableSpace X` instance for `Measure X` than
the explicit `m0`.

**Root cause:**
`Measure X` uses the ambient `[MeasurableSpace X]` typeclass, not an explicit one.
`Measure.trim` has signature `{m m0 : MeasurableSpace α} (μ : @Measure α m0)`.
When you write `μ : Measure X` (using the typeclass), `μ.trim hm` can't unify
the ambient instance with `m0`.

**Attempts:**
1. `variable [mX : MeasurableSpace X]` + `hm : m ≤ mX` — failed (same issue)
2. `@Measure X m0` + `[@IsFiniteMeasure X m0 μ]` — failed (NormedSpace instances
   can't be synthesized without the ambient typeclass)
3. `{m0 : MeasurableSpace X}` + `μ : Measure X` — failed (m0 not connected to μ)

**Resolution:**
Use `[MeasurableSpace X]` as the ambient instance and `{m : MeasurableSpace X}` as
the sub-σ-algebra, then `hm : m ≤ ‹MeasurableSpace X›`. The trim-based theorems
(`density_bridge`, `lpMeasSubgroup_dense_in_Lp`) are marked sorry with proof sketches.
The one theorem that does compile cleanly using this pattern: `density_bridge`.

**Lesson:**
When working with `Measure.trim`, always use the standard Mathlib section-variable
pattern: declare `variable {m m0 : MeasurableSpace α}` at the section level so both
are explicit section variables, then use `(μ : @Measure α m0)`. This is how Mathlib's
own `ConditionalExpectation` files are structured.

---

### Problem: `lpMeas` identifier not found

**File:** `ReconstructionTheorem.lean`

**Symptom:** `error: Unknown identifier 'lpMeas'`

**Root cause:**
Missing import. `lpMeas` is defined in:
`Mathlib.MeasureTheory.Function.ConditionalExpectation.AEMeasurable`
Not re-exported by `L2Space.lean` or `SimpleFuncDenseLp.lean`.

**Fix:** Added import:
```lean
import Mathlib.MeasureTheory.Function.ConditionalExpectation.AEMeasurable
import Mathlib.MeasureTheory.Function.ConditionalExpectation.Basic
```

---

### Problem: `rintro ⟨n, E, hE, rfl⟩` failed on generateFrom_le callback

**File:** `ReconstructionTheorem.lean`, `observableAlgebra_le`

**Symptom:**
```
error: Tactic `rcases` failed: `right✝ : n s` is not an inductive datatype
```

**Root cause:**
`MeasurableSpace.generateFrom_le` gives a callback `hs : s ∈ generating_set`.
The set `generating_set = ⋃ n : ℤ, ⋃ (E : Set ℝ) (_ : MeasurableSet E), {f n ⁻¹' E}`
is a `Set (Set X)`, and `hs` is a membership proof. Lean doesn't auto-destructor
a `Set.mem_iUnion` proof — you must unfold it first with `simp` then `obtain`.

**Fix:**
```lean
apply MeasurableSpace.generateFrom_le
intro s hs
simp only [Set.mem_iUnion] at hs
obtain ⟨n, E, hE, rfl⟩ := hs
exact hf n hE
```

**Lesson:**
Never use `rintro` directly on `generateFrom_le` callbacks for compound union sets.
Always `intro s hs; simp only [Set.mem_iUnion] at hs; obtain`.

---

### Problem: `△` notation not available

**File:** `ReconstructionTheorem.lean`

**Symptom:** `error: expected token` at `△`

**Root cause:**
`∆` notation is in `scoped[symmDiff]` scope, defined in `Mathlib.Order.SymmDiff`.
Not automatically opened.

**Fix:**
```lean
import Mathlib.Order.SymmDiff
open scoped symmDiff
```

---

### Problem: `MeasureTheory.Measure.measure` does not exist

**Symptom:** `error: Invalid field 'measure': The environment does not contain 'MeasureTheory.Measure.measure'`

**Root cause:**
Measure application `μ s` is written directly as `μ s` (function application),
not `μ.measure s` or `@Measure.measure α _ μ s`.

**Fix:** Write `μ (s ∆ t) = 0` not `μ.measure (s ∆ t) = 0`.

---

### Problem: `Lp.simpleFunc ℝ 2 ν` coercion to `Set`

**Symptom:**
```
error: Type mismatch
  Lp.simpleFunc ℝ 2 (μ.trim ?m.26)
has type
  AddSubgroup ↥(Lp ℝ 2 (μ.trim ?m.26))
but is expected to have type
  Set ↥(Lp ℝ 2 (μ.trim hm))
```

**Root cause:**
Two different `MeasurableSpace X` metavariables (`?m.25` and `?m.16`) — the trim
can't unify which `MeasurableSpace` to use. This is the same root cause as the
two-instance problem above; the `Set` coercion would work once the instance is fixed.

**Fix:** Resolved by using `[MeasurableSpace X]` as ambient typeclass throughout.

---

## 2026-04-04 — StoneDualityExtension.lean (from previous session)

### Intentional sorrys (documented, not errors)

- Task 0′-B: `clopen_charge_to_borel_measure` — no `Content.toMeasure` for Stone spaces in Mathlib
- Task 0′-D: measure on inverse limit via Choksi's theorem — not in Mathlib

Both are mathematical Mathlib gaps (not Lean API issues). The stone-level mathematics is correct; the gap is in Mathlib's Stone space measure theory.

---

## Template for new entries

```
### Problem: [brief description]

**File:** [filename], [location]
**Symptom:** [exact error message]
**Root cause:** [why it happened]
**Attempts:** [what didn't work]
**Fix:** [what worked]
**Lesson:** [generalizable rule for future]
```
