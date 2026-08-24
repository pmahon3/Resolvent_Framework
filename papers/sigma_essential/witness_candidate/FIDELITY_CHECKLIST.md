# Definitional-fidelity checklist (the ~15-minute read)

The Lean development proves `psiAmended_ZFC` with zero sorries from standard
axioms, so **the proofs need no re-checking**. The one remaining trust surface
is that the formal *definitions* transcribe the paper's (v2 `def:coherence`,
`def:sigma-essential`, Defs 1.1–1.2). This sheet lists every definition on the
trust path, where it lives, what to compare it against, and the known caveats
(each checked, none load-bearing — but they are yours to accept, not mine).

Read top to bottom; every item is a few lines of Lean.

## 1. The carrier notion (σ-class)

**Lean:** Mathlib's `MeasurableSpace.DynkinSystem` — fields `has_empty`,
`has_compl`, `has_iUnion_nat` (countable *pairwise-disjoint* unions).
**Paper:** Def 1.1 (σ-class: ∅, Ω, complement, countable disjoint unions).
**Check:** `has_iUnion_nat` takes `Pairwise (Disjoint on f)` — disjoint unions
only, NOT arbitrary unions (which would make it a σ-algebra and trivialize
non-distributivity). `Ω ∈ L` is `has_compl has_empty`.
**Caveat (none).**

## 2. σ-additive two-valued states

**Lean:** `TwoValuedState` (`SigmaEssentialLocalization.lean:36`): `val_univ`,
`not_val_empty`, `val_compl` (`Val Aᶜ ↔ ¬Val A` on carrier sets), `val_iUnion`
(`Val (⋃ f i) ↔ ∃ i, Val (f i)` for countable disjoint carrier families).
**Paper:** Def 1.2, σ-additive case: `s(⊔Aₙ) = Σ s(Aₙ)`.
**Check:** the `∃i`-form vs the paper's `=Σ` form. "At most one summand true"
is NOT assumed — it is *derived* (`val_at_most_one`, via monotonicity from
`val_union` + `has_diff`). So `∃`-form + complement-additivity ⟺ the paper's
sum form. (This fidelity argument was already certified in the old spine's
docstring block and re-checked this session.)
**Caveat (none).**

## 3. Finitely additive states — clause (0)'s quantifier

**Lean:** `FinAddState` (`SigmaEssentialAmended.lean`): same as above but
`val_union` (disjoint PAIRS) instead of `val_iUnion`.
**Paper:** "(finitely additive) two-valued state" in Def `def:coherence`.
**Check:** pair additivity suffices for finite additivity because a σ-class is
closed under finite disjoint unions (pad with ∅), so finite-family additivity
follows by induction. Nothing σ-additive is smuggled in.
**Caveat (none).**

## 4. The local pattern — THE key encoding choice

**Lean:** `LocalState d B` (`SigmaEssentialAmended.lean`): values + decidability
+ `val_compl` **inside `B` only**.
**Paper:** "two-valued state s₀ on B" (Def 1.2 restricted to B).
**Check + caveat (the one that matters):** `LocalState` demands only
complement-additivity in `B`, which is *weaker* than Def 1.2-on-`B` when `B`
contains other disjoint-union configurations. Two reasons this is harmless,
both checkable:
  (a) On the witness's block (`coreBlock` = the six core/complement sets), the
  only disjoint families with union in `B` ARE the complement pairs — all
  twelve cross-intersections are full fibers (paper Cor 6.4's parenthetical;
  verified by two passes). So on THIS `B`, `LocalState` = Def 1.2-on-`B` exactly.
  (b) In general, clause (0) upgrades for free: if a `FinAddState` extends the
  pattern, the pattern is its restriction, hence satisfies every Def-1.2
  constraint on `B`. A coherent `LocalState` is automatically a genuine state.
  So the amended definition's extension is faithful wherever coherence holds —
  and `IsSigmaEssentialL` requires coherence.

## 5. The amended σ-essential definition

**Lean:** `IsSigmaEssentialL s₀ := FinitelyCoherent s₀ ∧ ¬∃ s : TwoValuedState d, ExtendsS s s₀`
with `FinitelyCoherent s₀ := ∃ μ : FinAddState d, ExtendsF μ s₀`, and
`Extends… := ∀ A ∈ B.sets, (Val A ↔ s₀.Val A)`.
**Paper:** v2 `def:sigma-essential` (finitely coherent + no σ-additive
extension); extension = agreement on `B`.
**Check:** conjunction shape and quantifiers match; `ExtendsS` quantifies over
ALL σ-additive states (Dirac and non-Dirac — no Dirac-only weakening).
**Caveat:** `PsiAmended` is the *localized* existence sentence (∃ carrier,
block, pattern: witness). It does NOT bundle the admissibility predicates
(non-Boolean, essential irreducibility, non-segregation) into the formal
statement — those are paper-level (Cor 4.3/4.5, Prop `prop:adm`), with two
exceptions now ALSO machine-checked: non-Booleanness
(`carrier_not_interClosed` in `UlamWitnessMain.lean` — the witness itself
forces it via the amended Boolean baseline), and the Boolean baseline itself
(`boolean_no_witness_amended`). Essential irreducibility and non-segregation
remain paper-level claims about THIS carrier; they do not affect the truth of
`psiAmended_ZFC`, only the "admissible-cell" framing.

## 6. The carrier, block, and pattern are the paper's

**Lean:** `UlamWitnessCore.lean`: `coreA/B/C = Prod.snd ⁻¹' {0,1}/{0,2}/{1,2}`
(fibers 0–3 = paper's 1–4), `cell = Prod.fst ⁻¹' C_{α,n}`,
`generators` = singletons ∪ cells ∪ cores, `carrier = DynkinSystem.generate`;
`coreBlock` = the six-element ⊥-closure; `UlamMatrix` fields = Lem 2.1's (1)(2)(3)
(row-disjoint, row-covers-above-index, EXACT column-disjointness).
**Check:** the fiber sets and that `row_cover` + complement give the paper's
"complement of a row is {β ≤ α} × F" (used for co-countability).
**Caveat (encoding of s₀):** `corePattern` is the majority vote of the three
marked points `(m₀,0),(m₀,1),(m₀,2)` — NOT a lookup table on the six sets. On
the block it takes the paper's values (true on each core — `corePattern_val_core*`;
false on complements — forced by self-duality), and majority-of-3 being
self-dual gives `val_compl` for every set. Same pattern, slicker carrier.
Check the three `corePattern_val_core*` lemmas and you have Def-level identity.

## 7. Dirac-on-carrier

**Lean:** `IsDiracOn d s := ∃ ω, ∀ A, d.Has A → (s.Val A ↔ ω ∈ A)` (rigidity's
conclusion), rather than the spine's structure-equality `IsDirac`.
**Check:** this is the right notion — `Val` is unconstrained off the carrier,
so "equals δ_ω as a structure" is stronger than anything the paper asserts.
All downstream uses (kernel argument) only evaluate on carrier sets.
**Caveat (none).**

## 8. The instantiation

**Lean:** `UlamWitnessOmega1.lean`: `M₁ := (ω₁ : Ordinal).ToType`;
`M₁_uncountable` (via `#M₁ = ℵ₁`), `M₁_seg` (initial segments countable, via
`typein < ω₁ = (ℵ₁).ord`).
**Check:** these are the only two facts consumed; both from Mathlib's ordinal
API, no choice beyond the global `Classical.choice` in the receipt.

---

**If all eight read faithfully:** `psiAmended_ZFC` IS the paper's Theorem 7.1
(amended Ψ, ZFC), and the verification is complete at ground-truth level.
Receipts: `UlamWitnessReceipts.lean` (`#print axioms` — every theorem shows
exactly `[propext, Classical.choice, Quot.sound]`).
