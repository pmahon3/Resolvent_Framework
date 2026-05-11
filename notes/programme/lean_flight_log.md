# Lean Formalization Flight Log

Running log of non-trivial Lean errors, attempted fixes, and outcomes.
Updated as work progresses. Most recent entry at top.

---

## 2026-05-09 — Formalization Alignment Plan (post Paper I revision)

### Context

Paper I revised from 13pp to 8pp. Main structural change: four-way main
equivalence theorem (Thm 6.1) added in synthesis, gathering:
- (i) Kolmogorov: each $\ell_i$ σ-additive
- (ii) CE: collectively exhaustive
- (iii) Yosida-Hewitt: $\ell_p = 0$
- (iv) Stone support: $\hat\mu(\mathrm{pure}(\Omega)) = 1$

No new mathematical content — all four equivalences were already proved
in the body. The theorem assembles them.

### Current sorry inventory (updated 2026-05-10)

| File | Sorrys | Type |
|------|--------|------|
| `StoneDualityExtension.lean` | 1 | `stone_observational_extension` (Yosida-Hewitt) |
| All other active files | 0 ✅ | |

**Total: 1 sorry** in active codebase. Mathlib infrastructure gap (Yosida-Hewitt decomposition).

Archived (not in papers): `TopologicalQuerySystem.lean`, `ProkhorovExtension.lean` → `archive/`
Removed (not in papers): `IsFinitarilyExpressible`, `ce_irreducibility`, `evalSurjective_of_upperDirected...`

Key proved results:
- `sp1_iff` (CE characterisation, Paper I Thm 4.2): 0 sorry
- `observational_extension` (Carathéodory route, Paper I Thm 3.3): 0 sorry
- `stone_measure_exists` (Stone route measure, Paper I §5): 0 sorry
- `ce_independence` (CE not implied by structural conditions, Paper I §4): 0 sorry

### Prioritized plan

**Tier 1 — Highest leverage (blocks submission quality)**

P1. **Main equivalence theorem (Thm 6.1)**
    File: new theorem, likely in `StoneDualityExtension.lean` or new file
    Depends on: sp1_iff (✅), Yosida-Hewitt (❌ Mathlib gap),
    Prop B2 support condition (⚠️ 2 sorry)
    Action: Formalize the assembling theorem. Accept Mathlib-gap sorrys
    for legs (iii) and (iv); legs (i)↔(ii) already proved.
    Effort: Low (assembles existing results)

P2. **Stone support condition (Prop 5.5)**
    File: `StoneDualityExtension.lean`
    Gap: 2 sorrys at clopen→Borel and Choksi
    Action: Assess whether these can be worked around inline or need
    Mathlib contributions. If workaround possible, close. If not,
    document as Mathlib frontier sorrys.
    Effort: Medium (Mathlib assessment needed)

**Tier 2 — Valuable but not blocking**

P3. **IsFinitarilyExpressible + ce_irreducibility**
    File: `DiscriminabilityFoundations.lean`
    Gap: needs ultraproduct construction for QuerySystem
    Action: Either build minimal ultraproduct infrastructure or accept
    sorry with documentation. The companion note (UltrafilterCharge.lean,
    0 sorry) already proves the result at the Boolean algebra level.
    Effort: High (ultraproduct infra) or Low (accept sorry)

P4. **Abstract EvalSurjective from inverse limit**
    File: `DiscriminabilityFoundations.lean`
    Gap: needs Tychonoff for abstract inverse limit
    Action: Accept sorry. Concrete delay systems bypass this entirely.
    Not load-bearing for any paper result.
    Effort: N/A (accept)

**Tier 3 — Supporting**

P5. `DelayEmbedding.lean` — 4 sorrys around SUD. Not blocking.
P6. `ProkhorovExtension.lean` — Mathlib gap. Not blocking.
P7. `TopologicalQuerySystem.lean` — skeleton. Not blocking.

### Honest frontier

The formalization already covers Paper I's central results:
- Carathéodory extension (0 sorry) ✅
- CE characterisation (0 sorry) ✅
- Ultrafilter charge non-σ-additivity (0 sorry) ✅
- CE independence from structural conditions (0 sorry) ✅

The remaining sorrys are at Mathlib infrastructure boundaries:
- Stone-space measure theory (clopen→Borel, Choksi)
- Ultraproduct construction for first-order structures
- Yosida-Hewitt decomposition

These are genuine Mathlib gaps, not proof-logic gaps. The mathematical
content behind every sorry is clear and documented.

### Decision needed

Accept Mathlib-frontier sorrys and submit with current coverage, or
invest in closing them first? The companion note (UltrafilterCharge.lean)
is already 0 sorry. The Carathéodory route is 0 sorry. The Stone route
has 2 documented Mathlib sorrys. This is a strong formalization for a
submission.

---

## 2026-05-10 — StoneDualityExtension.lean (stone_measure_exists assessment)

### Goal

Close `stone_measure_exists` sorry: construct a Borel probability measure
on `stoneSpace S` from the compatible charges.

### Assessment

The statement `∃ Phat, IsProbabilityMeasure Phat` is weaker than intended —
it doesn't require `Phat` to extend the charges. Should be strengthened.

### Mathlib infrastructure available (2025)

- `AddContent` (structure): finitely additive set function on a family `C`
- `AddContent.measure`: extends an `AddContent` on a semiring to a `Measure`
  via Carathéodory, requires `IsSetSemiring C`, `mα ≤ generateFrom C`,
  and `IsSigmaSubadditive`
- `IsProjectiveMeasureFamily`, `IsProjectiveLimit.unique`: projective limit
  framework (existence NOT proved — Kolmogorov extension not in Mathlib)
- `ProjectiveFamilyContent`: builds `AddContent` from projective families

### Proof plan for single-algebra step

1. Define `stoneContent : Set (stoneSpace S) → ℝ≥0∞` on clopens `{u | E ∈ u}`
   via `P.ν` (the compatible charge on cylinder sets)
2. Prove `stoneContent` is an `AddContent` on clopens (finite additivity)
3. Prove clopens of `stoneSpace S` form an `IsSetSemiring`
4. Prove `IsSigmaSubadditive stoneContent` via compactness:
   if clopens `U_n` cover a clopen `K`, finitely many suffice by compactness,
   then finite additivity gives the σ-subadditivity bound
5. Apply `AddContent.measure` with `borel (stoneSpace S) ≤ generateFrom clopens`
6. Prove `IsProbabilityMeasure` via normalization

Each step is ~10-20 lines. Total: ~100 lines of new Lean code.

### Choksi step (projective limit)

NOT needed for single-algebra construction. The Stone space `St(C)` of
the direct limit carries the measure directly — no need to build on
each `St(B_i)` and take an inverse limit. The projective limit
identification `St(⋃ B_i) ≅ lim St(B_i)` (Proposition 5.1) shows
they're the same space.

### Detailed Lean construction plan

**Path A: AddContent.measure (preferred)**

```
ultrafilterBasis α = range (fun s => {u | s ∈ u})
```

Step 1: Prove `ultrafilterBasis` is a `IsSetSemiring`:
- Empty: `{u | ∅ ∈ u} = ∅` (ultrafilters don't contain ∅)
- Intersection: `{u | s ∈ u} ∩ {u | t ∈ u} = {u | s ∩ t ∈ u}` (ultrafilter inter)
- Difference: `{u | s ∈ u} \ {u | t ∈ u} = {u | s \ t ∈ u}` (ultrafilter compl)
- ~20 lines

Step 2: Build `AddContent ℝ≥0∞ (ultrafilterBasis S.Omega)`:
- `toFun {u | E ∈ u} := P_charge(E)` where P_charge comes from compatible family
- Well-definedness: `{u | E ∈ u} = {u | E' ∈ u} → E = E'` (ultrafilter separation)
- `empty'`: charge of ∅ = 0
- `sUnion'`: finite additivity from P.ν compatibility
- ~30 lines

Step 3: Prove `borel (stoneSpace S) ≤ generateFrom (ultrafilterBasis S.Omega)`:
- The topology IS generated by ultrafilterBasis (by definition)
- `borel = generateFrom opens ≤ generateFrom basis`
- ~5 lines (may be `rfl` or near)

Step 4: Prove `IsSigmaSubadditive`:
- If `{u | K ∈ u} ⊆ ⋃ {u | E_n ∈ u}`, compactness gives finite subcover
- Finite additivity handles the finite case
- ~20 lines (compactness argument)

Step 5: Apply `AddContent.measure` → get `Measure (stoneSpace S)`
Step 6: Prove `IsProbabilityMeasure` from normalization

Total: ~80-100 lines

**Path B: Content (alternative)**

Build `Content (stoneSpace S)` from the charge on compacts. On compact
TD space, every compact = finite union of clopens. Monotonicity and
sub-additivity follow. `Content.measure` gives the extension. Similar
line count but different API threading.

### Progress (2026-05-10)

Steps 1-2 completed:
- `isSetRing_ultrafilterBasis` ✅ (empty/union/diff via ultrafilter API)
- `isSetSemiring_stoneClopens` ✅ (transfer from CylGen + Ultrafilter.exists_mem_of_sUnion_mem)
- `stone_clopen_injective` ✅
- `Ultrafilter.exists_mem_of_sUnion_mem` ✅ (Finset.induction_on + union_mem_iff)

Steps 3-6 progress:
- `cylGen_charge_wellDef` ✅ (presentation independence: CompatibleContents +
  EvalSurjective + cyl_refine at common refinement)
- `cylGenCharge` ✅ (extracts P.ν value for cylinder event)
- `stoneAddContent` partial: `empty'` ✅, `sUnion'` ❌ (1 sorry — Finset plumbing)
- `stoneAddContent_isSigmaSubadditive` ✅ (compactness argument:
  IsCompact.elim_finite_subcover + addContent_sUnion_le_sum +
  Finset.sum_image_le_of_nonneg + ENNReal.sum_le_tsum)
- `stone_measure_exists` structural: AddContent.measure application ✅,
  IsProbabilityMeasure ✅ (measure_eq + cylGen_charge_wellDef + P.norm)
- Statement changed: MeasurableSpace := generateFrom (stoneClopens S) instead of borel,
  since stoneClopens ⊊ all clopens and may not generate full Borel σ-algebra.

### Remaining sorry in stone_measure_exists

One sorry: `sUnion'` in `stoneAddContent`. This is pure Finset plumbing:
- For each V ∈ I, extract E_V via Classical.choice from stoneClopens membership
- Show K = ⋃₀ {E_V} via stone_clopen_injective
- Find common refinement level for all E_V (Finset + UpperDirected)
- Use P.ν's own AddContent.sUnion' at that level (via CompatibleContents transfer)
- Thread through cylGen_charge_wellDef for each term

No mathematical gap. Closing requires ~50 lines of Finset.induction + Classical.choice threading.

### Status: COMPLETE — `stone_measure_exists` proved with 0 sorry.

Only remaining sorry in file: `stone_observational_extension` (intentional, Yosida-Hewitt).

The `sUnion'` proof uses Finset.induction_on with:
- Base: cylGen_charge_wellDef + addContent_empty
- Step (a): ⋃₀ ↑I' ∈ stoneClopens via Ultrafilter.diff_mem_iff + cyl_refine + measurable diff
- Step (c): Binary additivity via cylGen_charge_wellDef at common level + addContent_union

Key Lean technique: avoid `set` with Classical.choice projections. Use explicit
`have` statements and `rw` with named equalities. The `(fun E => {u|E∈u})` wrapper
from `Set.mem_image` requires `rw [spec.2]` on typed intermediate hypotheses rather
than `▸` on the goal.

---

## 2026-05-09 — DelayEmbedding.lean (reconstruction refactor attempt)

### Goal

Close `delay_reconstruction_iff` sorry by calling `reconstruction_iff_lpMeas`
across the file boundary.

### Root cause (confirmed)

`reconstruction_iff_lpMeas` has signature `[MeasurableSpace X] {m : MeasurableSpace X}`.
At the call site in `DelayEmbedding.lean`, `delayObservableAlgebra h T : MeasurableSpace X`
is in scope. When Lean elaborates `reconstruction_iff_lpMeas hm`, it unifies
`[MeasurableSpace X]` with `delayObservableAlgebra h T` instead of the section-level
ambient instance, making `hm : m ≤ ambient` fail to unify with `m ≤ m`.

### Approaches tried

1. **Named argument**: `reconstruction_iff_lpMeas (m := delayObservableAlgebra h T) hm μ`
   — fails: same unification

2. **`@` with explicit instances**: `@reconstruction_iff_lpMeas X mX (delayObservableAlgebra h T) hm μ inferInstance`
   — fails: Lean ignores the explicitly-passed `mX` and still synthesizes `delayObservableAlgebra`

3. **`change` to force goal type**: changed goal to use `@MeasurableSet X mX s`, then
   called `reconstruction_iff_lpMeas` — fails: same unification on `hm`

4. **Refactor ReconstructionTheorem.lean** to use `{m0 : MeasurableSpace X}` instead of
   `[MeasurableSpace X]`: cascades "synthesized type class instance is not definitionally
   equal" errors through all Mathlib API calls (`isClosed_aestronglyMeasurable`,
   `memLp_indicator_const`, `mem_lpMeas_iff_aestronglyMeasurable`, etc.)

5. **Branch `refactor/reconstruction-measurable-space`**: created and deleted; not viable
   without a major rewrite of both files

### Correct fix (not yet attempted)

Match Mathlib's ConditionalExpectation pattern exactly: the section in
`DelayEmbedding.lean` should use `variable {X : Type u}` with NO `[MeasurableSpace X]`,
then `variable {m0 : MeasurableSpace X}` and `{μ : @Measure X m0}` explicitly. This
would cascade through every theorem in the `ReconstructionBridge` section
(`delayObservableAlgebra_eq_comap`, `delayMap_shift_intertwining`, etc.).

### Resolution (2026-05-10)

The correct fix was simpler than expected. Wrap §§2-3 of
`ReconstructionTheorem.lean` in a `section DensityBridge` with:

```lean
variable {m m0 : MeasurableSpace X} {μ : Measure X}
```

No `[MeasurableSpace X]` typeclass in the section. `Measure X` resolves
to `m0` (last declared). Inside `density_bridge`, use
`letI : MeasurableSpace X := m` to resolve `Lp.simpleFunc.dense` against
the sub-σ-algebra.

Call site in `DelayEmbedding.lean`:
```lean
exact reconstruction_iff_lpMeas (m0 := ‹MeasurableSpace X›) (μ := μ) hm
```

19 lines changed, 0 sorrys remaining in DelayEmbedding.lean.

### Status: RESOLVED ✅ (2026-05-10)

---

## 2026-05-09 — StoneDualityExtension.lean (ultrafilter_map_eq_extend)

### Goal

Close two "technical" sorrys in `stoneEval_continuous` and
`stoneOutcomeMap_continuous`. Both need the same fact:
`Ultrafilter.map f = Ultrafilter.extend (pure ∘ f)`.

### Mathematical proof

Both sides are continuous maps `Ultrafilter α → Ultrafilter β` that
agree on `pure(α)`: `map f (pure a) = pure (f a) = (pure ∘ f) a`.
By density of `pure` (`denseRange_pure`) and T2 separation of
`Ultrafilter β`, they agree everywhere.

### Lean status

Extracted as `ultrafilter_map_eq_extend`. The helper lemma compiles
as a sorry; the two call sites are cleaned up to:
```lean
rw [ultrafilter_map_eq_extend]
exact continuous_ultrafilter_extend _
```

### Proof attempts

1. `rw [ultrafilter_extend_eq_iff]` + manual Filter.map manipulation:
   blocked by coercion issues between `Ultrafilter.map` and `Filter.map`.
   `↑(Ultrafilter.map pure v)` parsed as `Ultrafilter (Ultrafilter β)`,
   not `Filter (Ultrafilter β)`.

2. `simp only [Ultrafilter.coe_map, Filter.map_map]` + `change`:
   `simp` didn't fire on `Filter.map_map` (unused argument warning).

3. Term-mode via `isDenseInducing_pure.extend_eq_of_tendsto`:
   needs `Tendsto (pure ∘ f) (comap pure (𝓝 u)) (𝓝 (map f u))`.
   This should follow from `ultrafilter_comap_pure_nhds` but the
   composition with `f` needs care.

### Next step

Try: `isDenseInducing_pure.extend_eq_of_tendsto` with
`Tendsto` constructed via `ultrafilter_comap_pure_nhds` and
`Ultrafilter.map_pure`. Or: prove `Continuous (Ultrafilter.map f)`
directly without the `extend` detour, using `Ultrafilter.map_pure`
and `isTopologicalBasis_ultrafilterBasis`.

### Status: WIP (1 temporary sorry, down from 2 sorrys)

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
