# Lean Flight Plan: StoneDualityExtension.lean

## Goal — COMPLETE (2026-04-04)

`StoneDualityExtension.lean` builds cleanly on `main`.
- `stone_agrees_with_caratheodory` — **proved** ✅ (no sorry)
- All Task 0′-A and 0′-C results — **proved** ✅
- `stone_measure_exists` — **intentional sorry** (documented Mathlib gap: no `Content.toMeasure` for Stone spaces)
- `stone_observational_extension` — **intentional sorry** (documented Mathlib gap: Choksi's theorem not in Mathlib)

Merged to `main` 2026-04-05. Branch `stone-duality-extension` deleted.

---

## Environment

- Lean / Mathlib: `.lake/packages/mathlib/`
- Build tool: `~/.elan/bin/lake`
- Project target: `QuerySystem.StoneDualityExtension`

---

## ~~Blocker: `QuerySystem.lean` pre-existing errors~~ RESOLVED (2026-04-04)

`QuerySystem.lean` builds cleanly. The errors documented below were fixed
during the `stone-duality-extension` session and are preserved here for
historical reference only.

### The two failing lemmas

**1. `cylGenMass_eq_marginal` (lines 1021–~1093)**

Statement: `S.cylGenMass udir surj ν compat (S.Cyl i A) ⟨i, A, hA, rfl⟩ = ν i A`

Root cause: `cylGenMass` is defined via `Classical.choose` (opaque). After `simp only [cylGenMass]` the goal becomes `S.preμ udir ν {hE.choose} (fun j => if h : j = hE.choose then h ▸ hE.choose_spec.choose else ∅) = ν i A`. The `hE.choose` is opaque — Lean cannot reduce it or unify it with anything we name as a `let` binding.

**2. `cylGen_addContent.empty'` (inside `cylGen_addContent`)**

Statement: `toFun ∅ = 0`

Root cause: After `simp only [hempty_mem, dite_true]`, goal is `cylGenMass ... ∅ hempty_mem = 0`. The `rw [hempty_eq_cyl]` (rewriting `∅` to `S.Cyl i ∅`) fails because `hempty_mem : ∅ ∈ CylGen` appears in the type of the membership argument and the motive becomes ill-typed.

**3. `cylGen_addContent.sUnion'`**

Two sub-errors (downstream from the above; may clear once 1 and 2 are fixed):
- `| empty => simp` leaves unsolved goals
- `Application type mismatch` on `I'` (induction hypothesis type mismatch)

---

## Attempt log for `cylGenMass_eq_marginal`

### What we know for certain (2026-04-03)

- `Classical.choose` / `Exists.choose` is **opaque** in Lean 4. `Exists.choose` is `@[reducible]` but reduces to `Classical.choose` which is a plain `noncomputable def` (not `@[reducible]`, not `@[simp]`). Confirmed in `Init/Classical.lean`.
- `cylGenMass` is a plain `noncomputable def` (no `@[irreducible]`), so `simp only [cylGenMass]` CAN unfold it. After unfolding, the goal body contains `hE.choose` and `hE.choose_spec.choose` as opaque terms.
- `show`/`change` CANNOT be used to rewrite `cylGenMass ... hE` as `preμ ... C₀.s C₀.A` — definitional equality check fails because struct field projections of local `let C₀` don't reduce through `Classical.choose`.
- `dsimp only [C₀, ...]` makes no progress on local `let` bindings in this context.
- `exact hcyls` fails when `hcyls : preμ ... C₀.s C₀.A = ν i A` and goal is `preμ ... {hE.choose} (...) = ν i A` — same definitional equality failure.
- `rfl` cannot prove `cylGenMass ... hE = preμ ... C₀.s C₀.A`.
- `subst hj` where `hj : j = i` (outer parameter) inside a lambda **sometimes** gives "Unknown identifier `i`" at `S.le_refl i`. Fixed by using `have hji := Finset.mem_singleton.mp hj; rw [hji]` instead.

### Attempts tried (all failed)

| Attempt | Tactic | Result |
|---------|--------|--------|
| A | `simp only [cylGenMass, Cchosen, Achosen, i', A']` | Leaves unsolved goals; simp can't close |
| B | `rfl` to prove `cylGenMass = preμ Cchosen.s Cchosen.A` | Type mismatch; Classical.choose is opaque |
| C | `show S.preμ udir ν Cchosen.s Cchosen.A = ν i A` | "'show' tactic failed, pattern not definitionally equal to target" |
| D | `simp only [cylGenMass]` then `rw [preμ_respects_finCyl_eq ... Cchosen Cexpl]` | `rw` can't find `Cchosen.s` in goal (goal has `{hE.choose}`, not the struct projection) |
| E | `simp only [cylGenMass]` then `exact hcyls` | Type mismatch: `hcyls` has `C₀.s` / `C₀.A`, goal has `{hE.choose}` / raw lambda |
| F | `suffices h : preμ C₀.s C₀.A = ... from by simp only [cylGenMass]; exact h` | Same type mismatch in the `from by` step |
| G | `dsimp only [C₀, A₀ext, i₀, A₀, h₀]` after `simp only [cylGenMass]` | "dsimp made no progress" — can't unfold local lets this way |

### What has NOT been tried yet

- `conv` to fold the goal into `preμ C₀.s C₀.A` before calling `exact`
- `apply preμ_respects_finCyl_eq` (instead of `rw`) — `apply` uses unification, not pattern matching, so it might accept `{hE.choose}` matching against `C₀.s` via let-unfolding
- Defining `C₀` NOT as a `let`/`MeasFinCyl` struct but inline as anonymous angle brackets in the `apply` call
- `unfold cylGenMass` (uses `delta`, different from `simp only [cylGenMass]`) — may expose the body differently
- `native_decide` or `decide` (not applicable here)
- Marking `cylGenMass` as `@[simp]` to see if that changes unfolding behavior
- Restructuring `cylGenMass_eq_marginal` to use `cylGenMass_wellDef` as the first step (swapping the membership proof to a canonical one, then applying `cylGenMass_eq_marginal` recursively — but this is circular)
- Proving a helper lemma `cylGenMass_eq_preμ_chosen` **outside** the current proof context so that `Classical.choose` is fully opaque but the lemma provides the bridge

### Most promising next approach

Use `apply` instead of `rw` for `preμ_respects_finCyl_eq`. After `simp only [cylGenMass]`, the goal is:

```
S.preμ udir ν {hE.choose} (fun j => if h : j = hE.choose then h ▸ hE.choose_spec.choose else ∅) = ν i A
```

Try:
```lean
apply (S.preμ_respects_finCyl_eq udir ν compat surj C₀ Cexpl ?_).symm.trans ?_
```
where `C₀` is constructed to match the goal's first preμ argument **without** struct field projections.

Alternatively: prove the bridge lemma separately:
```lean
private lemma cylGenMass_eq_preμ_chosen [Nonempty S.ι] (udir) (surj) (ν) (compat)
    (E : Set S.Omega) (hE : E ∈ S.CylGen) :
    S.cylGenMass udir surj ν compat E hE =
    S.preμ udir ν {hE.choose} (fun j => if h : j = hE.choose then h ▸ hE.choose_spec.choose else ∅) := by
  simp only [cylGenMass]
  -- NOW the goal is preμ ... {hE.choose} ... = preμ ... {hE.choose} ...  which should be rfl
```
This would be `rfl` after `simp only [cylGenMass]` because both sides have the same expression. No struct projections involved.

---

## Attempt log for `cylGen_addContent.empty'`

### Root cause (confirmed)

After `simp only [hempty_mem, dite_true]`, goal is `S.cylGenMass udir surj ν compat ∅ hempty_mem = 0`. The `rw [hempty_eq_cyl]` (where `hempty_eq_cyl : ∅ = S.Cyl i ∅`) fails because the motive `fun _a => S.cylGenMass ... _a ⋯ = 0` is ill-typed: `hempty_mem : ∅ ∈ CylGen` has `∅` in its type, and replacing `∅` with `S.Cyl i ∅` makes `hempty_mem` ill-typed in the motive.

This is a **dependent rewrite** problem: the membership proof `hempty_mem` depends on the set `∅`.

### Attempts tried

| Attempt | Tactic | Result |
|---------|--------|--------|
| A | `rw [hempty_eq_cyl]` then `cylGenMass_wellDef` then `cylGenMass_eq_marginal` | Fails: motive not type correct (dependent type issue) |
| B | `calc` chain via `congr 1; exact hempty_eq_cyl` | Unclear; probably similar issue |
| C | `rw [hempty_eq_cyl, cylGenMass_wellDef ..., cylGenMass_eq_marginal ...]` | Same motive failure |

### What has NOT been tried

- `conv lhs => rw [show ∅ = S.Cyl i ∅ from ...]` — `conv` can sometimes handle dependent rewrites
- `simp only [show ∅ = S.Cyl i ∅ from ..., cylGenMass_wellDef, cylGenMass_eq_marginal]`
- `cases hempty_mem` or `obtain ⟨j, B, hB, hBcyl⟩ := hempty_mem` to destructure and rebuild
- `cylGenMass_eq_marginal` applied **directly** via the alternative route through the bridge lemma `cylGenMass_eq_preμ_chosen` (once that is proved), then using `preμ_respects_finCyl_eq` to compare the empty cylinder to any explicit presentation

---

## API Audit Results (2026-04-03)

| Item | Mathlib name | File | Notes |
|------|-------------|------|-------|
| `Ultrafilter α` compact | `ultrafilter_compact` | `StoneCech.lean` | ✅ confirmed |
| `Ultrafilter α` T2 | `Ultrafilter.t2Space` | `StoneCech.lean` | ✅ confirmed |
| `Ultrafilter α` totally disconnected | `inferInstance` | `StoneCech.lean` | ✅ confirmed |
| Basic clopen open | `ultrafilter_isOpen_basic` | `StoneCech.lean` | ✅ confirmed |
| Basic clopen closed | `ultrafilter_isClosed_basic` | `StoneCech.lean` | ✅ confirmed |
| `pure` dense range | `denseRange_pure` | `StoneCech.lean` | ✅ confirmed |
| `pure` dense inducing | `isDenseInducing_pure` | `StoneCech.lean` | ✅ confirmed |
| Continuous extension | `continuous_ultrafilter_extend` | `StoneCech.lean` | ✅ confirmed; requires compact T2 target |
| `Ultrafilter.map f` continuity | No direct lemma; use `continuous_ultrafilter_extend` with `pure ∘ f` | — | `Ultrafilter.map f = Ultrafilter.extend (pure ∘ f)` — needs proof |
| `Content.measure` | `MeasureTheory.Content.measure` | `Measure/Content.lean` | ⚠️ works on locally compact spaces |
| Charge on clopens → Borel measure | **Not in Mathlib** | — | Halmos §53–54; intentional sorry |
| Choksi's theorem | **Not in Mathlib** | — | Choksi 1958; intentional sorry |
| `observational_determination` | `QuerySystem.observational_determination` | `QuerySystem.lean:333` | Takes `UpperDirected`, not `LowerDirected` |
| `CollectivelyExhaustive` | `QuerySystem.CollectivelyExhaustive` | `DiscriminabilityFoundations.lean:481` | Takes `AddContent` families, not `Measure` families |
| `NormalizedCompatibleContents` | `QuerySystem.NormalizedCompatibleContents` | `DiscriminabilityFoundations.lean:506` | Bundles ν + compat + norm |
| `π_trans` direction | `(π (le_trans hij hjk)).π = (π hjk).π ∘ (π hij).π` | `QuerySystem.lean:150` | NOT `(π hij).π ∘ (π hjk).π` |
| `eval_comp_refine` | `S.eval_comp_refine hij : S.eval i = (S.π hij).π ∘ S.eval j` | `QuerySystem.lean:290` | Coherence condition |
| `S.le` vs `≤` | `S.le` is the system's own relation, not the `Preorder` `≤` | — | Use `S.le i j` not `i ≤ j` |
| `subst` + outer parameter | `subst hj` where `hj : j = i` (outer param) causes "Unknown identifier" on `i` | — | Use `have hji := ...; rw [hji]` instead |

---

## File Status

### `StoneDualityExtension.lean` — written 2026-04-03, not yet successfully compiled

Blocked on `QuerySystem.lean` errors above.

#### Structure
- Task 0′-A: `stoneSpace`, `stoneEmbedding`, `cylGen_clopen`, `stoneEval`, `stoneEval_compat` — written
- Task 0′-C: `stoneOutcomeMap`, `stoneOutcomeMap_continuous`, `stoneOutcomeMap_trans`, `stoneEval_factor` — written
- Task 0′-B/D: `stone_measure_exists` (intentional sorry)
- Task 0′-B/D cont: `stone_observational_extension` (intentional sorry)
- Task 0′-E: `stone_agrees_with_caratheodory` — proved

#### Known issues in StoneDualityExtension.lean (separate from QuerySystem.lean blocker)
1. `stoneEval_continuous` sorry: `Ultrafilter.map f = Ultrafilter.extend (pure ∘ f)` — no Mathlib lemma; not yet tried `apply` approach
2. `stoneOutcomeMap_continuous` sorry: same issue
3. `cylGen_basis` minor sorry: not load-bearing

---

## Build Attempts

| Date | Command | Result | Notes |
|------|---------|--------|-------|
| 2026-04-03 | `lake build QuerySystem` | ❌ disk full | Only 3GB free; Mathlib rebuild exhausts disk |
| 2026-04-03 | `lake build QuerySystem.QuerySystem` | ❌ 4 errors | Pre-existing failures in `cylGenMass_eq_marginal` and `cylGen_addContent` |
| 2026-04-03 | Many incremental edits | ❌ 4 errors (different forms) | See attempt log above |
| 2026-04-04 | `lake build QuerySystem.QuerySystem` | ❌ 3 errors → 0 → new errors | Session fixed `cylGenMass_eq_marginal` and `empty'`; new errors in `sUnion'` insert case |
| 2026-04-04 | `lake build QuerySystem.QuerySystem` | ✅ **0 errors** | `sUnion'` insert case fully closed |
| 2026-04-04 | `lake build QuerySystem.StoneDualityExtension` | ✅ **0 errors** | All API fixes applied; 2 intentional sorrys remain |

---

## Session 2026-04-04: What was fixed and how

### `cylGenMass_eq_marginal` — FIXED

Route taken: added `private lemma preμ_eq_of_finCyl_eq` which proves
`S.preμ udir ν C₁.s C₁.A = S.preμ udir ν C₂.s C₂.A` when `C₁.set = C₂.set`,
via `preμ_respects_finCyl_eq`. Then `cylGenMass_eq_marginal` uses:
```lean
simp only [cylGenMass]
apply (S.preμ_eq_of_finCyl_eq udir surj ν compat Cchosen Cexpl hCeq).trans hcyls
```
Key insight: `apply` uses unification (not pattern matching), so it can match
`{hE.choose}` against `Cchosen.s` without needing definitional reduction of `Classical.choose`.

### `cylGen_addContent.empty'` — FIXED

The dependent rewrite problem (`rw [hempty_eq_cyl]` making `hempty_mem` ill-typed) was
bypassed by using `simp only [hempty_eq_cyl]` instead of `rw`. `simp` handles dependent
rewrites correctly. After `simp only [hempty_mem, dite_true, hempty_eq_cyl]`, the goal
reduces cleanly.

### `cylGen_addContent.sUnion'` — PARTIALLY FIXED

The `empty` base case and induction setup now work. The `insert` inductive case has most
of the machinery in place. Current state (errors at lines 1325–1343):

**What works:**
- `simp only [dif_pos hmem_full, dif_pos ht_mem]` to reduce dif expressions (avoids
  Decidable instance mismatch from `rw`)
- `simp only [hfull_union_eq_orig]` to bridge `cylGenMass ... (S.Cyl it At ∪ ⋃₀ ↑I') hmem_full`
  to `cylGenMass ... (S.Cyl iU AU) ⟨iU, AU, hAU, rfl⟩` (handles the dependent argument
  correctly — `rw` fails here with "motive not type correct")
- `simp only [hI'_eq, dif_pos hI'_cylmem]` to reduce the I' dif (Decidable mismatch fix)

**Key lemmas added:**
- `hmem_full : (S.Cyl it At ∪ ⋃₀ ↑I') ∈ S.CylGen` — computed BEFORE `obtain ⟨iu, Au, ...⟩ := hI'_mem` destructures the union witness
- `hfull_union_eq_orig : S.Cyl it At ∪ ⋃₀ ↑I' = S.Cyl iU AU` — saved BEFORE `rw [hI'_eq]` rewrites the hypothesis

**Current errors (lines 1325–1343):**
`hpCt/hpCu/hpCU` proofs use `preμ_eq ... (fun j hj => Finset.mem_singleton.mp hj ▸ S.le_refl j)` but Lean can't infer the implicit `k` argument. Errors:
- `S.le_refl j ▸ ...` produces `S.le it it` but expected `S.le j ?m`
- `simpa using hAt` fails because `Ct.A j` doesn't reduce with `j` still free

**Fix needed:** Add explicit `(k := it)` / `(k := iu)` / `(k := iU)` to each `preμ_eq` call, and replace `simpa using hAt` with `simp only [dif_pos rfl]; exact hAt` (or similar).

Also: `linarith` at line 1343 may need adjustment once `hpCt/hpCu/hpCU` are fixed.

---

## Confirmed tactics/insights (2026-04-04)

| Situation | Use this | Not this | Why |
|-----------|----------|----------|-----|
| Reduce `dif`/`if` with potential Decidable mismatch | `simp only [dif_pos h]` | `rw [dif_pos h]` | `simp` is robust to instance differences |
| Rewrite set in `cylGenMass E hE` where `hE` depends on `E` | `simp only [heq]` | `rw [heq]` or `conv_lhs => rw [heq]` | Dependent rewrite; `simp` handles the transport |
| Bridge `cylGenMass` through two proofs of same set | `cylGenMass_wellDef` | — | Standard |
| Unify `Classical.choose`-based goals | `apply` | `rw`, `exact`, `show` | `apply` uses unification, bypasses opaqueness |

---

## Final status (2026-04-04)

### `QuerySystem.QuerySystem` — ✅ BUILDS CLEANLY (0 errors)

All three original blockers resolved:
1. `cylGenMass_eq_marginal` — via `preμ_eq_of_finCyl_eq` bridge + `apply`
2. `cylGen_addContent.empty'` — via `simp only [hempty_eq_cyl]`
3. `cylGen_addContent.sUnion'` — full insert case closed; key fixes:
   - `revert hI_ss hI_dis hI_mem` before `induction` (eliminates spurious `case insert.h1.h`)
   - `simp only [dif_pos h]` instead of `rw [dif_pos h]` for Decidable mismatches
   - `simp only [heq]` instead of `rw [heq]` for dependent rewrites on `cylGenMass`
   - `calc` chain (not `linarith`) for closing ENNReal equalities

### `StoneDualityExtension.lean` — ✅ BUILDS CLEANLY (0 errors, 2 intentional sorrys)

Fixes applied:
- `QuerySystem ι` → `QuerySystem` (structure has no type parameter)
- `abbrev stoneSpace` drop `: Type*` annotation (universe constraint)
- `rw [h]` → `funext + congr 1` approach for eta-contracted continuity goals
- `Ultrafilter.map_map` needs `funext u` before `simp only [Function.comp, ...]`
- `S.π_trans hij hjk` direction corrected to `.symm`
- `P̂` (combining diacritic) replaced with `Phat`
- `MeasurableSpace (stoneSpace S)` provided via `borel (stoneSpace S)` in `stone_measure_exists`

### Intentional sorrys (Mathlib gaps, documented)

| Theorem | Gap |
|---------|-----|
| `stone_measure_exists` | Clopen charge → regular Borel measure (Halmos §53–54); Choksi's theorem |
| `stone_observational_extension` | Yosida–Hewitt decomposition for charges on Boolean algebras |

### No further steps needed on this branch
