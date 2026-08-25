# Scope: the unformalized layer between `AndersenJessen` and `EscapingTower`

**Written 2026-08-24.** Scoping only — no math claimed, no code written.
Status of the gap: real, and recorded by `rmk:tower-remaining` /
`rmk:aj-remaining` in the blueprint.

## What the gap is

`ExtensionObstruction.lean` (ch1) defines `QuerySystem.EscapingTower` and proves
`not_exists_extension_of_escapingTower`. `AndersenJessen.lean` (ch2) builds the
thick tower. **Nothing connects them.**

Evidence (all three agree, checked 2026-08-24):
- `AndersenJessen.lean` and `Diagonal.lean` import *only Mathlib* — no project import.
- No module outside ch0/ch1 imports `QuerySystem.QuerySystem`.
- The dep graph has exactly one ch1→ch2 edge, `def:escaping-tower → rmk:aj-remaining`,
  which terminates in a remark (zero out-edges).
- The only mention of `EscapingTower` in `AndersenJessen.lean` is in a **docstring**
  ("Feeding it through `QuerySystem.EscapingTower` refutes…"). Prose, not code.

So the graph is *not* under-annotated. The dependency does not exist.

Consequence, stated by `rmk:tower-remaining`: the claim that the original
`UpperDirected` form was false "rests on a hand check against the source, not on
the kernel."

## What is already in the kernel (endpoints, both done)

| Piece | Where | Status |
|---|---|---|
| `X_thick` — every `Xₖ` has full outer measure | `AndersenJessen.lean:523` | proved |
| `X_antitone`, `X_iInter` (`⋂ₖ Xₖ = ∅`) | `AndersenJessen.lean:493,498` | proved |
| Vitali transversal `V`, `V_covers`, `V_unique` | `AndersenJessen.lean:223–267` | proved |
| `pi_inter_diag_eq_empty` | `Diagonal.lean:58` | proved |
| `no_mass_one_of_iInter_empty` | `Diagonal.lean:106` | proved |
| `EscapingTower` + the obstruction theorem | `ExtensionObstruction.lean:56,~78` | proved |

Axiom receipts: all rest on `[propext, Classical.choice, Quot.sound]` only.

## The blocking obstruction (verified against Mathlib, not assumed)

The natural route is the trace measure λ_X(E ∩ X) = λ(E) on a thick set
(Border, *Kolmogorov Extension Problem*, Prop. 14), then `Measure.comap Subtype.val`.

**This does not work off the shelf.** `Measure.comap` is:

```
if hf : Function.Injective f ∧ ∀ s, MeasurableSet s → NullMeasurableSet (f '' s) μ
then ((OuterMeasure.comap f) μ.toOuterMeasure).toMeasure _ else 0
```

For `X` thick with thick complement, subsets of `X` are not generally
null-measurable, the guard fails, and **`comap` silently returns `0`**.
`Measure.Subtype.measureSpace` is `comap Subtype.val volume`, so it degenerates too.
`Subtype.volume_univ` needs `NullMeasurableSet u` — a thick set with thick
complement is not null-measurable (if it were, thickness would force it conull).

Mathlib has **no** thick-set trace measure and **no** Vitali-style transversal
measure. The `ExtensionObstruction.lean` header already says exactly this:
"Mathlib has no thick sets and no Vitali-style transversal, so this remains a
real construction project."

## What closing it actually requires

Four units, in dependency order. Unit 1 is the hard one.

1. **Trace measure on a thick set.** Build λ_X on the subtype `↥(X α k)` directly
   as a `Measure`, bypassing `comap`. Route: define the σ-algebra on `↥X` as
   `{E ∩ X : E measurable}` (well defined: thickness + `X_thick` give
   `E ∩ X = E' ∩ X → λ(E) = λ(E')`, since the symmetric difference is a
   measurable set disjoint from `X`, hence null). Then σ-additivity of λ_X
   from σ-additivity of λ. `X_thick` is *exactly* the well-definedness hypothesis.
   **Not in Mathlib; must be written.** Largest single unit.

2. **Projective system over `X₀ × ⋯ × Xₙ` with diagonal maps.** Package as a
   `QuerySystem`: `ι := ℕ`, `q n := ⟨X₀ × ⋯ × Xₙ, borel⟩`, `le := (· ≤ ·)`,
   `π` = coordinate projection. Must discharge `π_refl` and `π_trans`
   (definitional-ish, but the dependent-product encoding is fiddly).

3. **Contents from the trace measures + compatibility.** Instantiate
   `NormalizedCompatibleContents`. **Cheaper than it looks:** that structure needs
   an `AddContent` (finitely additive) plus `compat` and `norm` — *not* a measure.
   The trace measures give this directly once unit 1 exists.

4. **Instantiate `EscapingTower` and discharge the five fields.**
   `idx := id`, `base n := diagonal in X₀ × ⋯ × Xₙ`.
   - `full` ← λ_X(Xₙ) = 1 (unit 1)
   - `empty` ← `pi_inter_diag_eq_empty` + `X_iInter` (both already proved)
   - `anti` ← `X_antitone` + `Diag_antitone` (already proved)
   - `meas` ← `measurableSet_Diag` (already proved)
   Then feed to `not_exists_extension_of_escapingTower`. Mostly assembly.

## Estimate and recommendation

Unit 1 dominates — it is a genuine Mathlib-gap construction, not an assembly job.
Units 2–4 are moderate-to-routine given unit 1, and unit 4 is largely already paid for.

**Do unit 1 first and standalone**, as its own file (`ThickTrace.lean`), stated
against an abstract thick set rather than `X α k` — it is reusable, and it is the
only part that can fail. If unit 1 lands, 2–4 are bookkeeping. If it does not,
nothing downstream was wasted.

Payoff: the first real ch1→ch2 mathematical edge, and the Andersen–Jessen
refutation moves from hand-checked to kernel-checked — which is precisely what
`rmk:tower-remaining` says is outstanding.

## Not in scope here

The other open item, `slab0_not_mem` (`UlamWitnessLatticeGap.lean:114`), is an
axiom stub for §3 Normal Form in the σ-essential chapter. Independent of this.
