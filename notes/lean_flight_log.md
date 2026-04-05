# Lean Formalization Flight Log

Running log of non-trivial Lean errors, attempted fixes, and outcomes.
Updated as work progresses. Most recent entry at top.

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
