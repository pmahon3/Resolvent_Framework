# Branch Plan: `stone-duality-extension`

## Purpose

This branch develops Paper 0′ — the **Stone duality route** to the observational extension
theorem. It is a companion to the algebraic route already proved in `QuerySystem.lean`.

The thesis argument is:

> The algebraic route (Carathéodory, Paper 0) requires σ-subadditivity of the premeasure
> as an explicit input, which is supplied by `SequentiallyUpperDirected`. The Stone route
> derives σ-additivity from compactness of the Stone space — finite additivity on `CylGen`
> is enough, and the topology does the rest. This is the deeper structural reason why
> compatible marginals extend: the cylinder algebra *lives compactly*.

---

## Starting Point

Branch cut from `main` at commit `a30f219`:

- `QuerySystem.lean` — **0 sorrys** ✅
- `PredictiveState.lean` — **0 sorrys** ✅
- `PredictiveOperators.lean` — **0 sorrys** ✅
- `DelayEmbedding.lean` — **1 intentional sorry** (full delay system not SUD; proved impossible)
- `DiscriminabilityFoundations.lean` — **3 sorrys** (2 ultraproduct-blocked, 1 intentional Tychonoff)
- `TopologicalQuerySystem.lean` — **1 sorry** (Kolmogorov extension not in Mathlib)
- `ProkhorovExtension.lean` — **1 sorry** (PerfectMeasure / Musiał not in Mathlib)

---

## What This Branch Adds

A single new file: **`StoneDualityExtension.lean`**

This file proves (or scaffolds with intentional sorrys) the Stone duality route to the
observational extension theorem.

---

## Mathematical Plan

### Step 0: Prerequisites (already in Mathlib)

- `Ultrafilter α` is compact T2 — `ultrafilter_compact`, `Ultrafilter.t2Space`
- `E ↦ { u | E ∈ u }` maps sets to clopens — `ultrafilter_isOpen_basic`, `ultrafilter_isClosed_basic`
- `Ultrafilter.map f` is continuous — needs API check (likely `continuous_ultrafilter_extend`)
- `Ultrafilter.map_pure` — already confirmed present

### Task 0′-A: Stone space basics

Define `stoneSpace S := Ultrafilter S.Omega` and prove:

- `stoneSpace_compactSpace` — from `ultrafilter_compact`
- `stoneSpace_t2Space` — from `Ultrafilter.t2Space`
- `stoneEmbedding : S.Omega → stoneSpace S := pure`
- `cylGen_clopen` — each `E ∈ CylGen` gives a clopen `{ u | E ∈ u }`
- `stoneEval i : stoneSpace S → Ultrafilter (S.q i).Outcome` — `Ultrafilter.map (eval i)`
- `stoneEval_compat` — commutes with refinement maps

**Risk:** Low. All Mathlib pieces exist; main work is API name lookup.

### Task 0′-B: Charge on CylGen → Borel measure on Stone space

Given `cylGen_addContent ν` (the finitely additive charge on `CylGen`, already proved),
construct a Borel measure `P̂` on `stoneSpace S` such that:

```
P̂ { u | E ∈ u } = (cylGen_addContent ν) E   for all E ∈ CylGen
```

**Mathlib route:**
- `MeasureTheory.Content` works on compact sets of a locally compact space
- `stoneSpace S` is compact T2, so every closed set is compact
- The clopen algebra is a basis; the charge on clopens extends to a Borel measure
- Key lemma: on a totally disconnected compact T2 space, a finitely additive charge
  on the clopen algebra extends uniquely to a regular Borel measure

**Mathlib API to locate:**
- `MeasureTheory.Content.measure` — takes a `Content` (on compacts) to a `Measure`
- Whether `AddContent ℝ≥0∞ S.CylGen` can be lifted to a `Content` on clopens of `stoneSpace S`
- Alternatively: Riesz representation for `C(X, ℝ)` with `X` compact T2

**Risk:** Medium. The Content API in Mathlib works on compact sets; adapting it to the
clopen algebra of a Stone space requires checking whether the interface fits directly
or needs a small wrapper.

### Task 0′-C: Inverse system of Stone outcome spaces

For each `i : S.ι`, define the Stone outcome space `Ultrafilter (S.q i).Outcome`.
The refinement maps `(S.π hij).π : (S.q j).Outcome → (S.q i).Outcome` (for `i ≤ j`)
induce bonding maps `stoneOutcomeMap hij : Ultrafilter (S.q j).Outcome → Ultrafilter (S.q i).Outcome`.

This forms a cofiltered inverse system of compact T2 spaces.

**What to prove:**
- `stoneOutcomeMap_continuous` — continuous bonding maps
- `stoneOutcomeMap_trans` — composition law
- `stoneEval_factor` — `stoneEval i = stoneOutcomeMap hij ∘ stoneEval j`

**Risk:** Low-Medium. The category-theoretic setup is straightforward; the main question
is whether Mathlib's `TopCat.nonempty_limitCone_of_compact_t2_cofiltered_system` applies
directly.

### Task 0′-D: Measure on the inverse limit

The compatible family of measures `ν i` on each `(S.q i).Outcome` pushes forward to
measures on `Ultrafilter (S.q i).Outcome` via the Stone embedding. The inverse limit
of these Stone outcome spaces carries a compatible family of measures; extend to a single
measure on the limit.

**Connection to existing work:** `compactInverseLimit_nonempty` in `ProkhorovExtension.lean`
already proves the limit is nonempty using an FIP argument. The measure extension part
is the new ingredient.

**Risk:** Medium. This is the deepest step; depends on 0′-B being settled.

### Task 0′-E: Agreement with Carathéodory extension

When both routes apply (i.e., under `SequentiallyUpperDirected + LowerDirected`), the
Stone route and the Carathéodory route (`observational_extension`) produce the same
measure `P` on `S.Omega`.

**Proof:** Both measures agree on `CylGen`; `observational_determination` (already proved)
gives uniqueness.

**Risk:** Low. `observational_determination` is already in `QuerySystem.lean`.

---

## File Structure

```
StoneDualityExtension.lean
├── stoneSpace S            (= Ultrafilter S.Omega)
├── stoneSpace_compactSpace
├── stoneSpace_t2Space
├── stoneEmbedding
├── cylGen_clopen
├── stoneEval i
├── stoneEval_compat
├── stoneOutcomeMap         (bonding maps)
├── stoneOutcomeMap_trans
├── stoneEval_factor
├── stone_measure_exists    (Task 0′-B, key sorry)
├── stone_observational_extension  (Tasks 0′-C/D, key sorry)
└── stone_agrees_with_caratheodory (Task 0′-E, proved from observational_determination)
```

---

## Current Status (2026-04-02)

The mathematical analysis and LaTeX phases are **complete**. The Stone route has been
integrated into the unified Paper I draft at `papers/paper_i/paper_i.tex`.

| Document | Status |
|----------|--------|
| `archive/notes_archived_artifacts/step_a_step_b_analysis.md` | Complete |
| `archive/notes_archived_artifacts/tex_proof_plan.md` | Complete — used to produce the LaTeX drafts |
| `papers/stone_duality_extension/` | Superseded by integration into Paper I |
| `papers/paper_i/paper_i.tex` | **Authoritative LaTeX** — 13 pages, compiles cleanly |

The Stone route proof (Steps A, B1, B2, assembly) lives in §5 of `papers/paper_i/`.
`papers/stone_duality_extension/` is retained as a record of the standalone draft.

### Next priority for this branch

**Lean formalization**: create `StoneDualityExtension.lean` using the proof in
`papers/paper_i/` §5 as the authoritative spec. Work through Tasks 0′-A through 0′-E
in the order below. Do the API audit (§ "Before Writing Any Code") first.

### Live mathematical analysis

---

## Before Writing Any Code

1. **API audit**: confirm the correct Lean 4 / Mathlib names for:
   - `Continuous (Ultrafilter.map f)` — what is it called?
   - `Content.measure` — does it work for clopen algebras directly?
   - `pure` continuity as `S.Omega → Ultrafilter S.Omega`
2. **Dot notation**: `stoneSpace` is an `abbrev`, not a structure field — use `stoneSpace S`
   not `S.stoneSpace` everywhere, or define it as a `def` with explicit `S` parameter.
3. **Build first**: confirm `lake build QuerySystem.QuerySystem` is clean on this branch
   before adding new code.

---

## Success Criteria

The branch is complete when `StoneDualityExtension.lean` builds with:

- `stone_agrees_with_caratheodory` — **proved** (no sorry)
- `stoneSpace_compactSpace`, `stoneSpace_t2Space`, all 0′-A results — **proved**
- `stone_measure_exists` — **intentional sorry** with documented Mathlib gap
- `stone_observational_extension` — **intentional sorry** with documented Mathlib gap

The intentional sorrys are acceptable because they document precisely where the
formalization exceeds current Mathlib — a meaningful mathematical contribution in itself.
