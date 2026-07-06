# Definitional-fidelity review — side-by-side (2026-07-06)

The Lean development proves `psiAmended_ZFC` from `[propext, Classical.choice,
Quot.sound]` with zero sorries, so the proofs need no re-checking. What follows
is the complete trust surface: every definition on the path from the paper's
Theorem 7.1 to the Lean statement, quoted verbatim on both sides, with the
transcription verdict. Two former prose-caveats are now themselves theorems
(`UlamWitnessFidelity.lean`, receipts clean), so every item below is either a
direct transcription or machine-closed. **Sign-off = agreeing that the eight
quoted pairs say the same thing.**

---

## 1. The carrier notion (σ-class = concrete σ-complete OMP)

**Paper** (v2 §1, = [M]):
> a family L ⊆ P(Ω) with: ∅, Ω ∈ L; A ∈ L ⟹ A⊥ := Ω∖A ∈ L; {Aₙ} ⊆ L
> pairwise disjoint ⟹ ⋃ₙ Aₙ ∈ L, ordered by inclusion.

**Lean** (Mathlib `MeasurableSpace.DynkinSystem`):
```lean
structure DynkinSystem (α : Type*) where
  Has : Set α → Prop
  has_empty : Has ∅
  has_compl : ∀ {a}, Has a → Has aᶜ
  has_iUnion_nat : ∀ {f : ℕ → Set α},
    Pairwise (Disjoint on f) → (∀ i, Has (f i)) → Has (⋃ i, f i)
```

**Check:** `has_iUnion_nat` requires `Pairwise (Disjoint on f)` — disjoint
unions only (a σ-class, NOT a σ-algebra). `Ω ∈ L` = `has_compl has_empty`.
Countable = ℕ-indexed with ∅-padding for finite families. ✓ direct.

## 2. σ-additive two-valued states

**Paper** (v2 §1): s : L → {0,1}, s(Ω)=1, additive over orthogonal joins in
its domain — s(⋃ₙAₙ) = Σₙ s(Aₙ) for countable pairwise-disjoint families with
union in L (in particular s(A) + s(A⊥) = 1).

**Lean** (`SigmaEssentialLocalization.lean`):
```lean
structure TwoValuedState (d : DynkinSystem Ω) where
  Val : Set Ω → Prop
  decVal : DecidablePred Val
  val_univ : Val univ
  not_val_empty : ¬ Val ∅
  val_compl : ∀ {A}, d.Has A → (Val Aᶜ ↔ ¬ Val A)
  val_iUnion : ∀ {f : ℕ → Set Ω}, Pairwise (Disjoint on f) → (∀ i, d.Has (f i)) →
    (Val (⋃ i, f i) ↔ ∃ i, Val (f i))
```

**Check:** the paper's `= Σ` for a {0,1}-valued function over a disjoint family
means "union true ⟺ exactly one member true." The structure asserts the
`∃`-half; the "at most one" half is DERIVED, not assumed
(`val_at_most_one`, via monotonicity from `val_union` + Dynkin `has_diff`) —
so the conjunction (∃ ∧ at-most-one) ⟺ `= Σ`. ✓ faithful (the derivation
direction only makes the structure *weaker-or-equal*, and the derived lemma
restores equality).

## 3. Finitely additive states — clause (0)'s quantifier

**Paper** (v2 `def:coherence`): "a (finitely additive) two-valued state on all
of L" — Def 1.2 with additivity over *finite* disjoint families.

**Lean** (`SigmaEssentialAmended.lean`):
```lean
structure FinAddState (d : DynkinSystem Ω) where
  Val : Set Ω → Prop
  decVal : DecidablePred Val
  val_univ : Val univ
  not_val_empty : ¬ Val ∅
  val_compl : ∀ {A}, d.Has A → (Val Aᶜ ↔ ¬ Val A)
  val_union : ∀ {A A'}, d.Has A → d.Has A' → Disjoint A A' →
    (Val (A ∪ A') ↔ (Val A ∨ Val A'))
```

**Check:** pair additivity; finite-family additivity is derived
(`FinAddState.val_sUnion_finset` in `UlamWitnessFidelity.lean` — Finset
induction, since a σ-class contains finite disjoint unions), at-most-one
derived (`FinAddState.val_at_most_one`). Nothing σ-additive is assumed of μ —
so clause (0) quantifies over exactly the paper's finitely additive states. ✓

## 4. The local pattern

**Paper** (v2): "a two-valued state s₀ on a finite ⊥-closed sub-orthoposet
B ⊆ L" — Def 1.2 with additivity over orthogonal joins *that exist in B*.

**Lean** (`SigmaEssentialAmended.lean`):
```lean
structure LocalState (d : DynkinSystem Ω) (B : Block d) where
  Val : Set Ω → Prop
  decVal : DecidablePred Val
  val_compl : ∀ {A}, A ∈ B.sets → (Val Aᶜ ↔ ¬ Val A)
```
(`Block` = finite `Finset (Set Ω)`, members in `d`, complement-closed.)

**Check — the one substantive encoding choice, now closed BOTH ways in Lean:**
`LocalState` demands only complement-additivity inside `B` (weaker than
Def 1.2-on-B in general). Closure:
- `coherent_pattern_fully_additive` (**theorem**): a finitely coherent
  `LocalState` satisfies EVERY Def-1.2 constraint on B (finite disjoint family
  of B-members with union in B: union true ⟺ some member true, plus
  at-most-one). Since `IsSigmaEssentialL` requires coherence, the pattern is a
  genuine paper-state wherever the definition applies. A weaker structure +
  a clause that provably upgrades it = faithful.
- `coreBlock_disjoint_eq_compl` (**theorem**): on the witness's block the only
  disjoint pairs are the complement pairs (the twelve cross-intersections are
  nonempty), so for THIS `B`, `LocalState` = Def 1.2-on-B exactly, coherence
  or not. (= Cor 6.4's parenthetical, machine-checked.)
✓ closed.

## 5. The amended σ-essential definition and Ψ

**Paper** (v2 `def:sigma-essential`):
> A σ-essential contextual state on L is a two-valued state s₀ on a finite
> ⊥-closed sub-orthoposet B ⊆ L that is finitely coherent on L but extends to
> **no** global σ-additive two-valued state on L.
> (`def:coherence`: s₀ finitely coherent ⟺ s₀ extends to a finitely additive
> two-valued state on all of L.)

**Lean** (`SigmaEssentialAmended.lean`):
```lean
def ExtendsF (μ : FinAddState d) (s₀ : LocalState d B) : Prop :=
  ∀ A ∈ B.sets, (μ.Val A ↔ s₀.Val A)
def ExtendsS (s : TwoValuedState d) (s₀ : LocalState d B) : Prop :=
  ∀ A ∈ B.sets, (s.Val A ↔ s₀.Val A)
def FinitelyCoherent (s₀ : LocalState d B) : Prop :=
  ∃ μ : FinAddState d, ExtendsF μ s₀
def IsSigmaEssentialL (s₀ : LocalState d B) : Prop :=
  FinitelyCoherent s₀ ∧ ¬ ∃ s : TwoValuedState d, ExtendsS s s₀
def PsiAmended : Prop :=
  ∃ (Ω : Type) (d : DynkinSystem Ω) (B : Block d) (s₀ : LocalState d B),
    IsSigmaEssentialL s₀
```

**Check:** extension = agreement on B (the paper's s↾B = s₀); the negative
clause quantifies over ALL σ-additive states — Dirac and non-Dirac, no
weakening. `PsiAmended` is the localized existence sentence; the admissibility
predicates are NOT bundled in (they are consequences/paper-level: non-Boolean
is now also machine-checked — `carrier_not_interClosed` — via the amended
Boolean baseline; essential irreducibility and non-segregation remain
paper-level facts about this carrier and do not affect `psiAmended_ZFC`'s
truth). ✓ with that scope note.

## 6. The carrier, block, and pattern are the paper's

**Paper** (v2 §sec:witness): Ω = ω₁ × {1,2,3,4}; cores A₁ = M×{1,2},
A₂ = M×{1,3}, A₃ = M×{2,3}; cells C_{α,n} × F from an Ulam matrix with (1) row
disjointness, (2) row covering above the index, (3) exact column disjointness;
L = least σ-class containing singletons, cells, cores; B = ⊥-closure of the
cores; s₀ ≡ 1 on the three cores.

**Lean** (`UlamWitnessCore.lean`, fibers 0–3 = paper's 1–4):
```lean
def coreA (M) : Set (M × Fin 4) := Prod.snd ⁻¹' {0, 1}
def coreB (M) : Set (M × Fin 4) := Prod.snd ⁻¹' {0, 2}
def coreC (M) : Set (M × Fin 4) := Prod.snd ⁻¹' {1, 2}
structure UlamMatrix (M) [LinearOrder M] where
  C : M → ℕ → Set M
  row_disjoint : ∀ α, Pairwise (Disjoint on C α)
  row_cover    : ∀ {α β}, α < β → ∃ n, β ∈ C α n
  col_disjoint : ∀ n {α α'}, α ≠ α' → Disjoint (C α n) (C α' n)
def cell (α n) : Set (M × Fin 4) := Prod.fst ⁻¹' U.C α n
def generators : Set (Set (M × Fin 4)) :=
  {S | ∃ p, S = {p}} ∪ {S | ∃ α n, S = cell U α n} ∪ {coreA M, coreB M, coreC M}
def carrier : DynkinSystem (M × Fin 4) := DynkinSystem.generate (generators U)
noncomputable def coreBlock : Block (carrier U) :=
  { sets := {coreA M, coreB M, coreC M, (coreA M)ᶜ, (coreB M)ᶜ, (coreC M)ᶜ}, ... }
noncomputable def corePattern (m₀ : M) : LocalState (carrier U) (coreBlock U) where
  Val S := ((m₀,0) ∈ S ∧ (m₀,1) ∈ S) ∨ ((m₀,0) ∈ S ∧ (m₀,2) ∈ S) ∨
           ((m₀,1) ∈ S ∧ (m₀,2) ∈ S)
```

**Check:** cores/cells/generators/carrier are direct transcriptions
(Lem 2.1's property (2) "complement of the row = {β ≤ α}" is recovered from
`row_cover`'s contrapositive, which is the only direction Thm 5.1 consumes).
The pattern is encoded as the majority vote of three marked points rather than
a table: on the block it takes exactly the paper's values — TRUE on each core
(`corePattern_val_core*`), FALSE on each complement (forced, since
majority-of-3 is self-dual) — and `val_compl` holds for every set for the same
reason. Same pattern, coordinate-free carrier. ✓

## 7. Rigidity's conclusion: Dirac *on the carrier*

**Lean:** `IsDiracOn d s := ∃ ω, ∀ A, d.Has A → (s.Val A ↔ ω ∈ A)`.

**Check:** the spine's structure-equality `IsDirac` (`s = dirac ω`) would
constrain `Val` on non-carrier sets, which the paper never does; `IsDiracOn`
says exactly "agrees with δ_ω on L." All uses (the kernel argument in
Thm 7.1(2)) evaluate only on carrier sets. ✓ the correct notion.

## 8. The instantiation at ω₁

**Lean** (`UlamWitnessOmega1.lean`): `M₁ := (ω₁ : Ordinal).ToType` with
`M₁_uncountable : ¬(univ : Set M₁).Countable` (via `#M₁ = ℵ₁`) and
`M₁_seg : ∀ β, (Iio β).Countable` (via `typein < ω₁ = (ℵ₁).ord`).

**Check:** these two facts are the only inputs the abstract development
consumes; both discharged from Mathlib's ordinal API; no extra axioms appear
in the receipts. ✓

---

## Verdict template

If items 1–8 read as faithful transcriptions, then
`psiAmended_ZFC : PsiAmended` **is** Theorem 7.1 (the amended Ψ, in ZFC), and
the verification chain is closed at ground-truth level:
paper ⟷ (this review) ⟷ Lean definitions ⟶ (0-sorry proofs, standard axioms)
⟶ theorem. Receipts: `UlamWitnessReceipts.lean`.
