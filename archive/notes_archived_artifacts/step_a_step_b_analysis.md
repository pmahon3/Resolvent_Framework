# Step A and Step B: Analysis

## The Central Theorem

> A compatible family of finitely additive charges on a directed system of Boolean
> algebras extends to a σ-additive measure on the generated σ-algebra, via Stone duality.

The proof has two non-trivial assembly steps. This document records the analysis of
each, the philosophical observations that accompany them, and the road to
implementation.

---

## Step A: Is St(⋃ Bᵢ) = lim← St(Bᵢ)?

### The Question

Stone duality is contravariant: a directed system of Boolean algebras (with injective
connecting maps) dualises to a cofiltered inverse system of compact Hausdorff spaces.
The question is whether the Stone space of the direct limit **is** the inverse limit of
the individual Stone spaces. The answer is yes when the connecting maps φᵢⱼ : Bᵢ → Bⱼ
are injective — so the key question is whether they are.

### Setting

A query system has:
- A poset ι of query levels, upper-directed
- For each level i, a measurable space Outcome(i)
- For i ≤ j, a measurable surjection π_ij : Outcome(j) → Outcome(i) — "forgetting detail"
- A sample space Ω with evaluation maps eval_i : Ω → Outcome(i)
- Coherence: π_ij ∘ eval_j = eval_i

Cylinder sets and connecting maps:

```
Cyl(i, A) = { ω ∈ Ω : eval_i(ω) ∈ A }

cyl_refine:  Cyl(i, A) = Cyl(j, π_ij⁻¹(A))

φ_ij : Bᵢ → Bⱼ  defined by  φ_ij(Cyl(i, A)) = Cyl(j, π_ij⁻¹(A))
```

### Answer

**φ_ij is injective, proved via EvalSurjective.**

1. **EvalSurjective → π_ij surjective.** If eval_i is surjective and π_ij ∘ eval_j = eval_i,
   every element of Outcome(i) is in the image of π_ij.

2. **π_ij surjective → φ_ij injective.** If π_ij⁻¹(A) = π_ij⁻¹(A') then A = A', so
   φ_ij(Cyl(i, A)) = φ_ij(Cyl(i, A')) implies Cyl(i, A) = Cyl(i, A').

3. **φ_ij injective → Step A holds.** A direct limit of Boolean algebras along injective
   homomorphisms dualises to an inverse limit of compact Hausdorff spaces along surjective
   continuous maps. This is the standard Stone duality categorical fact.

Step 1 is already proved in `QuerySystem.lean`. Step 2 is a short argument. Step 3 is
standard.

### Philosophical Observation

Injectivity of φ_ij is not an extra assumption — it is constitutive of what coherence
means. If the projection maps were not injective on measurable sets, there would be two
distinct events at level i that are indistinguishable at every finer level j. The
refinement maps would not be refining anything.

In the Merleau-Ponty framing: the horizon of finer observations must genuinely *reveal*
more of the world. A system where finer queries collapsed back to coarser ones would have
a kind of observational degeneracy — going through the motions of refinement without
learning anything new. Coherence requires injectivity. The two are not separable.

**Status: complete.** The argument is clean and all components are in hand.

---

## Step B: Does the Borel σ-algebra of lim← St(Bᵢ) match σ(CylGen)?

### The Question

Even with a σ-additive measure on lim← St(Bᵢ), pulling it back to a measure on
σ(CylGen) requires identifying:

```
σ(CylGen)  ≅  Borel(lim← St(Bᵢ))   pulled back to Ω
```

This splits into two sub-problems:

- **B1 (structural):** Does σ(CylGen) equal the pullback of Borel(lim← St(Bᵢ)) along
  `pure : Ω → lim← St(Bᵢ)`? This is about what sets are nameable.
- **B2 (measure-theoretic):** Does the measure on lim← St(Bᵢ) pull back to a
  well-defined σ-additive measure on σ(CylGen)? This is about where the mass lives.

### The Proof Strategy

**B1 — Structural identification, via Discriminability.**

The queries define a *separation structure* on Ω: discriminability (Paper −1) says the
queries separate points. This is the Hausdorff condition in disguise.

1. If the queries separate points of Ω, then `pure : Ω → St(CylGen)` is injective: two
   distinct points ω ≠ ω' have a cylinder set containing one but not the other, so their
   principal ultrafilters differ.

2. The image of `pure` is always dense in the Stone space — principal ultrafilters are
   dense in any Stone space.

3. Every clopen of St(CylGen) pulls back along `pure` to a cylinder set in σ(CylGen),
   and clopens generate Borel(St(CylGen)). The reverse inclusion holds because every
   cylinder set is the preimage of a clopen. So:

   ```
   pure⁻¹(Borel(St(CylGen))) = σ(CylGen)
   ```

   **Gap:** Step 3 needs to be made precise. Density gives approximation; it doesn't
   immediately give σ-algebra equality. The clopen basis argument is the right route
   but needs to be written out carefully.

**B2 — Measure-theoretic identification, via CE.**

The Stone space St(CylGen) contains both principal ultrafilters (points of Ω) and
non-principal ones — the "phantom" points at infinity. A measure on St(CylGen) is
always σ-additive (compact space), but it might assign mass to phantom points. If it
does, that mass has nowhere to go when we pull back to Ω.

CE (collective exhaustion) is precisely the condition that mass doesn't escape to
non-principal ultrafilters. The translation is:

```
CE (Paper 0 definition)
    ↔  σ-additive extensibility          [proved: sp1_iff, zero sorrys]
    ↔  mass does not escape to non-principal ultrafilters in St(CylGen)
    ↔  Stone measure supported on pure(Ω)
```

The first equivalence is already proved. The conceptual content of the remaining two
is established by the irreducibility argument: an ultrafilter observer *is* a
non-principal ultrafilter — a phantom point in St(CylGen). CE rules out that observer.
In Stone language, that is exactly the support condition.

**Gap:** The middle two equivalences need to be written out precisely via the
Yosida-Hewitt decomposition, which identifies the purely finitely additive component
of a charge with mass on non-principal ultrafilters.

### Division of Labour

```
Discriminability (Paper −1)  →  B1: structural identification
                                  queries separate points → embedding injective
                                  → Borel(St) pulls back to σ(CylGen)

CE (Paper 0)                 →  B2: measure-theoretic identification
                                  mass doesn't escape to phantom ultrafilters
                                  → Stone measure descends to σ(CylGen)
```

Paper −1 is not philosophical preamble — discriminability is load-bearing in the Stone
route. CE is not bypassed by Stone duality; it is *rephrased*. The Stone route converts
CE from a condition on a directed system of charges into a support condition on a Borel
measure on a compact space. Same content, different language.

### The Full Proof Chain

```
Compatible charges on directed system {Bᵢ}
    → Stone duality → cofiltered inverse system {St(Bᵢ)}
    → [Step A] φᵢⱼ injective (EvalSurjective) → St(⋃ Bᵢ) = lim← St(Bᵢ)
    → compact inverse limit → σ-additive measure on Borel(lim← St(Bᵢ))
    → [Step B1] discriminability → pure⁻¹(Borel(St)) = σ(CylGen)
    → [Step B2] CE → Stone measure supported on pure(Ω)
    → σ-additive measure on σ(CylGen)
```

### Holding Question

*Raised in conversation, 2026-04-01.*

Assuming all observable distinctions are visible in the Stone space might be *equivalent*
to countable additivity — not just related to it. If true, this would mean the Stone route
succeeds if and only if the charge is already σ-additive, making the approach circular.
The candidate strategy suggests this is not the case: the circularity is broken by CE,
which is an independent condition. But the conjecture should be tested explicitly when
writing the LaTeX proof.

---

## Road to Implementation

The workflow is: **LaTeX proof first, Lean formalization second**, iterating between
them to equilibrium. The LaTeX proof is also the paper (Paper A).

### What needs to be written (LaTeX)

| Item | Status |
|------|--------|
| Step A: full proof | Argument complete — needs writeup |
| B1: clopen basis argument made precise | Gap — needs careful proof |
| B2: Yosida-Hewitt → Stone support translation | Gap — needs writeup |
| Full chain assembled end-to-end | Pending B1 and B2 |
| Holding question addressed or deferred | Pending |

### What the Lean formalization will need

Once the LaTeX proof is stable, the Lean scaffold in `StoneDualityExtension.lean`
needs to match it. Known gaps in Mathlib:

| Component | Mathlib status |
|-----------|---------------|
| `CompactSpace (Ultrafilter α)`, `T2Space (Ultrafilter α)` | Present |
| `pure` dense in `Ultrafilter α` | Present (or short argument) |
| Charge on clopen algebra → Borel measure on Stone space | Gap — `MeasureTheory.Content` API needs checking |
| Inverse limit of measures on compact spaces | Choksi (1958); not in Mathlib |
| Yosida-Hewitt decomposition | Not in Mathlib |

The intentional sorrys in `StoneDualityExtension.lean` mark precisely the Mathlib
gaps. They are acceptable — they document where the formalization exceeds current
Mathlib, which is itself a contribution.

### Immediate next action

Write the LaTeX proof of B1 (the clopen basis argument). This is the last open
mathematical question before the full chain is in hand.
