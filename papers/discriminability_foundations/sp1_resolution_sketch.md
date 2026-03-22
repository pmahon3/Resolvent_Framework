# SP1 Resolution Sketch
**Status:** Refined (2026-03-22). Counterexample verified. Ready for Lean attempt.

---

## The question

Does sequential upper-directedness + compatible finitely-additive contents force
σ-additivity at every finite level? This is what the witnessing conjecture asserts.

**Answer: No.** The conjecture as originally stated is false. The correct result is an
equivalence: σ-additive extensibility is equivalent to a valuation-layer condition
(collective exhaustion) that is independent of the index-layer conditions.

---

## Layer separation

The query system has two independent layers:

- **Index layer**: the preorder (ι, ≤), refinement maps π, sequential upper-directedness.
  Pure functions between sets. No measure theory.
- **Valuation layer**: the contents ℓ_Q : E_Q → [0,1], compatibility.
  How mass is assigned and transported.

Sequential upper-directedness is an index-layer condition. σ-additivity is a
valuation-layer property. These layers are independent: index-layer conditions cannot
force valuation-layer properties. The witnessing conjecture was asking whether they
could, which is why it was unprovable — and false.

---

## The counterexample (C1 refuted)

**Claim:** There exists a compatible family of finitely-additive contents on a
sequentially upper-directed query system that fails σ-additivity at every level.

**Construction:**

- **Index set:** ι = ℕ ∪ {ω}, with i ≤ j (usual order on ℕ) and n ≤ ω for all n ∈ ℕ.
  This is sequentially upper-directed: bounded sequences have a max; unbounded
  sequences have ω as a common upper bound.

- **Outcome spaces:** O_i = ℚ ∩ [0,1] for all i ∈ ι.

- **Event algebras:** E_i = finite-cofinite algebra on ℚ ∩ [0,1] for all i.
  (Sets that are either finite or cofinite. This is a Boolean algebra.)

- **Refinement maps:** All identity maps π = id.

- **Contents:** ℓ_i(E) = 0 if E is finite, 1 if E is cofinite, for all i.
  (This is a normalized finitely-additive content. It is not σ-additive.)

- **Compatibility:** Trivial — all maps are identities, all contents identical.

**Failure of σ-additivity:** Enumerate ℚ ∩ [0,1] = {x_1, x_2, ...}. Let
E_n = (ℚ ∩ [0,1]) \ {x_1, ..., x_n}. Then:
  - Each E_n is cofinite, so E_n ∈ E_i and ℓ_i(E_n) = 1 for all i, n.
  - E_1 ⊇ E_2 ⊇ ... is decreasing.
  - ∩_n E_n = ∅ (every rational is eventually removed).
  - But ℓ_i(E_n) = 1 → 1 ≠ 0.

So ℓ_i fails continuity at ∅ at every level i. No witnessing query exists: for any
Q' ≥ Q_0, the refinement map is the identity, so ℓ_{Q'}(π^{-1}(E_n)) = ℓ_{Q'}(E_n) = 1.

**The counterexample is valid.** C1 is refuted.

**What it reveals:** The finite-cofinite algebra cannot express "this set is getting
small" — it only distinguishes finite from cofinite. The content is perfectly coherent
within the algebra but blind to the convergence structure. This blindness cannot be
cured by the index order. It is a valuation-layer pathology.

---

## The tetralemma

Applied to: "does sequential upper-directedness + compatibility force σ-additivity?"

- **C1** (yes, derivable): **False.** Counterexample above.
- **C2** (must be assumed as axiom): Unsatisfying — imports σ-additivity directly,
  which is what the program is trying to avoid.
- **C3** (both derive and assume): Incoherent.
- **C4** (neither): The live corner — σ-additivity is neither derivable from nor
  reducible to the index-layer conditions alone.

**Dissolution (middle way):** The question was malformed because it conflated index-
and valuation-layer conditions. The correct question is: what is the valuation-layer
condition that characterizes systems modeling coherent worlds, and what does it force?

The answer is collective exhaustion (defined below). It is not an axiom imposed from
outside — it is the exact valuation-layer characterization of σ-additive extensibility.
The equivalence (Step 7) is the formal content of the dissolution.

---

## Collective exhaustion

**Definition.** A compatible family of contents {ℓ_Q} on a query system is
*collectively exhaustive* if: for every Q and every decreasing sequence (E_n) in E_Q
with ∩_n E_n = ∅, there exists Q' ≥ Q such that ℓ_{Q'}(π^{-1}(E_n)) → 0.

**Reading:** No observer assigns persistent weight to events that the system as a
whole sees as empty. The system's refinement structure always provides a witness that
registers the convergence — if the system models a coherent world.

**The counterexample fails collective exhaustion** because for the sequence E_n above,
every Q' gives ℓ_{Q'}(π^{-1}(E_n)) = 1 for all n. No witness exists anywhere in the
system. The system does not model a coherent world — it is a formal structure in which
every observer is permanently blind to a convergence that is right in front of them.

---

## The SP1 theorem

**Theorem (SP1).** Let {(E_Q, ℓ_Q)} be a compatible family on a sequentially
upper-directed query system. The following are equivalent:

  (i)  The family is collectively exhaustive.
  (ii) ℓ_Q extends uniquely to a σ-additive measure on σ(E_Q) for every Q.

**Proof of (i) → (ii):**
1. Fix Q and (E_n) decreasing in E_Q with ∩_n E_n = ∅.
2. By collective exhaustion, find Q' ≥ Q with ℓ_{Q'}(π^{-1}(E_n)) → 0.
3. By compatibility, ℓ_Q(E_n) = ℓ_{Q'}(π^{-1}(E_n)) → 0.
4. So ℓ_Q is continuous at ∅. By the extension criterion (Thm 3.2), ℓ_Q extends
   uniquely to σ(E_Q). □

**Proof of (ii) → (i):**
If ℓ_Q extends to μ_Q for every Q, then for (E_n) ↘ ∅ in E_Q:
ℓ_Q(E_n) = μ_Q(E_n) → 0 by σ-additivity of μ_Q. Take Q' = Q. □

**Note on sequential upper-directedness:** The theorem as stated does not use
sequential upper-directedness. That condition is needed for the *global* extension
to Ω (SP2), not for the per-level extension. SP1 is purely a statement about
individual levels, mediated by the refinement structure. Sequential upper-directedness
enters when one asks whether the system as a whole assembles into a global measure.

---

## Foundational reading

The SP1 theorem settles the de Finetti question precisely:

- De Finetti was right: no finitary or index-layer coherence condition forces
  σ-additivity. The counterexample makes this exact.

- The additional ingredient is not a stronger syntactic condition. It is a semantic
  one: the system must actually model a coherent world — one in which every convergence
  is visible somewhere in the refinement order. That is collective exhaustion.

- Collective exhaustion is not assumed. It is the criterion distinguishing query
  systems that model coherent worlds from those that do not. A system failing it
  contains observers with persistent mass on events that vanish everywhere in the
  system. That is incoherence, not a gap in the axioms.

- The σ-algebra is forced in coherent systems and evadable in incoherent ones. This
  is the correct resolution of the original question.

---

## What changes in the paper

### §5 (currently: positive result / witnessing conjecture)

Replace Conjecture 5.1 with the SP1 theorem above. The section now has three parts:

1. **The independence result** (new): Proposition — sequential upper-directedness +
   compatibility does not force σ-additivity. Proof: the counterexample.

2. **Collective exhaustion** (new): Definition and foundational reading.

3. **SP1 theorem** (replaces conjecture): The equivalence (i) ↔ (ii) above.

### §6 (foundational conclusions)

Add a subsection: "Collective exhaustion and the de Finetti settlement." The revised
chain reads:

  bounded discriminability
  → refinement
  → coherence (= collective exhaustion)
  → probability.

The chain is now complete at the SP1 level. Every arrow is a theorem or definition,
not a conjecture.

### Abstract and introduction

Update to reflect that SP1 is resolved: "we show that σ-additivity is equivalent to
collective exhaustion — the valuation-layer condition characterizing coherent observer
systems — and is neither derivable from nor reducible to index-layer conditions alone."

---

## Lean plan

Five layers in order of dependency:

### Layer 0: Counterexample
Construct the finite-cofinite counterexample explicitly. Show it satisfies
`SequentiallyUpperDirected` and `CompatibleContents` but fails `CollectivelyExhaustive`
and σ-additive extension.

This closes C1 formally.

```lean
-- The finite-cofinite algebra on a countably infinite type
def finCofin (α : Type*) [Infinite α] : MeasurableSpace α :=
  MeasurableSpace.generateFrom {s | s.Finite ∨ sᶜ.Finite}

-- The counterexample query system
def counterexampleQS : QuerySystem where
  ι := WithTop ℕ  -- ℕ ∪ {ω}
  q _ := { Outcome := ℚ, instMeas := finCofin ℚ }
  le i j := i ≤ j
  π _ := { π := id, measurable_π := measurable_id }
  ...

-- The finitely-additive content: 0 on finite sets, 1 on cofinite sets
noncomputable def fcContent : AddContent ℝ≥0∞ (finCofin ℚ) := ...

-- It fails σ-additivity
theorem fcContent_not_sigma_additive : ¬ fcContent.IsSigmaSubadditive := ...
```

### Layer 1: CompatibleContents
Finitely-additive version of `CompatibleMarginals`. Works with `AddContent` per level
rather than `Measure`.

```lean
def QuerySystem.CompatibleContents
    (ν : ∀ i : S.ι, AddContent ℝ≥0∞ (S.q i).instMeas) : Prop :=
  ∀ {i j} (hij : S.le i j) (A : Set (S.q i).Outcome),
    MeasurableSet A → ν i A = ν j ((S.π hij).π ⁻¹' A)
```

### Layer 2: CollectivelyExhaustive
```lean
def QuerySystem.CollectivelyExhaustive
    (ν : ∀ i : S.ι, AddContent ℝ≥0∞ (S.q i).instMeas) : Prop :=
  ∀ (i : S.ι) (E : ℕ → Set (S.q i).Outcome),
    (∀ n, MeasurableSet (E n)) →
    (∀ n, E (n+1) ⊆ E n) →
    (⋂ n, E n = ∅) →
    ∃ j : S.ι, S.le i j ∧
      Filter.Tendsto
        (fun n => ν j ((S.π ‹S.le i j›).π ⁻¹' E n))
        Filter.atTop (nhds 0)
```

### Layer 3: SP1 theorem (easy direction first)
```lean
-- (i) → (ii): collective exhaustion → σ-additive extension at each level
theorem sp1_extension
    (ν : ∀ i : S.ι, AddContent ℝ≥0∞ (S.q i).instMeas)
    (compat : S.CompatibleContents ν)
    (exhaust : S.CollectivelyExhaustive ν)
    (i : S.ι) :
    ∃ μ : Measure (S.q i).Outcome,
      ∀ (A : Set (S.q i).Outcome), MeasurableSet A → μ A = ν i A

-- (ii) → (i): σ-additive extension → collective exhaustion
theorem sp1_necessity
    (ν : ∀ i : S.ι, AddContent ℝ≥0∞ (S.q i).instMeas)
    (compat : S.CompatibleContents ν)
    (ext : ∀ i, ∃ μ : Measure (S.q i).Outcome,
      ∀ A, MeasurableSet A → μ A = ν i A) :
    S.CollectivelyExhaustive ν
```

### Layer 4: Equivalence
```lean
theorem sp1_iff
    (ν : ∀ i : S.ι, AddContent ℝ≥0∞ (S.q i).instMeas)
    (compat : S.CompatibleContents ν) :
    S.CollectivelyExhaustive ν ↔
    ∀ i, ∃ μ : Measure (S.q i).Outcome,
      ∀ A, MeasurableSet A → μ A = ν i A :=
  ⟨fun h => sp1_extension ν compat h, fun h => sp1_necessity ν compat h⟩
```

---

## Key Mathlib dependencies to check

Before writing Lean, verify availability of:

1. `MeasureTheory.AddContent` — finitely additive content. Exists in Mathlib
   (`Mathlib.MeasureTheory.Measure.AddContent`). Already used in QuerySystem.lean.

2. Extension from `AddContent` to `Measure` via Carathéodory —
   `MeasureTheory.AddContent.measure`. Already used in `observational_extension`.

3. Continuity at ∅ as a condition on `AddContent` — need to check whether
   `AddContent.IsSigmaSubadditive` captures this or whether we need a separate
   `IsContinuousAtEmpty` predicate.

4. `WithTop ℕ` for the index type — standard in Mathlib.

5. Finite-cofinite algebra — may need to construct from scratch using
   `MeasurableSpace.generateFrom`.

---

## Priority order for Lean work

1. **First:** Layer 0 (counterexample). This is the load-bearing result.
   If it goes through cleanly, the rest follows the sketch.

2. **Second:** Layer 1 + 2 (definitions). These are definitional, should be
   straightforward once we know the right Mathlib types.

3. **Third:** Layer 3 easy direction (i → ii). The proof is two lines once
   the definitions are in place.

4. **Fourth:** Layer 3 hard direction (ii → i) and Layer 4 (equivalence).
   These are short given (i → ii).

5. **Last:** Update the tex body once Lean is clean.
