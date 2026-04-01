# Break Reading & Questions

## 1. Stone Duality — The Core Bijection

### What to read
- Stone (1936) — *The theory of representations for Boolean algebras*
- Johnstone — *Stone Spaces* (Part I, Chapters 1–2) for a modern treatment
- Or: any good functional analysis text covering the Gelfand–Stone theorem

### The one thing to absorb
The bijection:

```
Boolean algebra B  ←→  compact totally disconnected Hausdorff space St(B)
charge on B        ←→  regular Borel measure on St(B)
```

Finite additivity on B becomes σ-additivity on St(B) because compact spaces
carry regular measures automatically. This is the conceptual engine of Paper 0′.

### Questions to sit with
- Why is the Stone space of P(ℕ) the Čech–Stone compactification βℕ?
- A non-principal ultrafilter on ℕ is a point of βℕ \ ℕ. What charge on P(ℕ)
  does it correspond to? Is it σ-additive?
- The finite-cofinite algebra on ℕ has a Stone space homeomorphic to the
  one-point compactification ℕ∪{∞}. What does the charge "density at ∞"
  look like on the algebra side?
- In the program: CylGen is a Boolean algebra (set semiring, closed under
  complements in the right sense). What is its Stone space? What are its points?

---

## 2. Riesz Representation and the Content Construction

### What to read
- Halmos — *Measure Theory* §53–54 (contents and the Riesz theorem)
- Rudin — *Real and Complex Analysis* Chapter 2 (Riesz for locally compact spaces)
- For Mathlib specifically: skim
  `Mathlib/MeasureTheory/Measure/Content.lean` — just the definitions and
  the statement of `Content.measure`, not the proofs

### The one thing to absorb
The pipeline:

```
Content λ on compact sets
  → inner content λ* on open sets  (λ* U = sup { λ K : K ⊆ U, K compact })
  → outer measure μ*               (μ* E = inf { λ* U : E ⊆ U, U open })
  → Borel measure μ                (restrict to Borel sets)
```

On a compact Hausdorff space, a finitely additive non-negative function on
compact sets that is additive on disjoint compacts extends to a regular Borel
measure. This is what we need for Task 0′-B.

### Questions to sit with
- `MeasureTheory.Content` in Mathlib works on compact sets of a locally compact
  space. Our Stone space is compact (hence locally compact). Does the clopen
  algebra of a Stone space fit the `Content` interface directly, or does it
  need a wrapper?
- A clopen set in a compact space is both compact and open. So clopens are
  compact sets. Can we define a `Content` whose domain is exactly the clopens,
  and does `Content.measure` then give the right Borel extension?
- `cylGen_addContent` is an `AddContent ℝ≥0∞ S.CylGen` in Lean. Is there a
  direct path from `AddContent` to `Content`, or do we need to build a new
  structure?
- What is the relationship between `MeasureTheory.Content` and the Riesz
  representation theorem `MeasureTheory.RieszMarkovKakutani` in Mathlib?
  Which is more directly applicable here?

---

## 3. Cyclic Vectors and Koopman Operators

### What to read
- Walters — *An Introduction to Ergodic Theory* Chapter 2
- Eisner, Farkas, Haase, Nagel — *Operator Theoretic Aspects of Ergodic Theory*
  Chapter 7 (Koopman operators and spectral theory)
- For the connection to delay embeddings: Takens (1981) original paper, or
  Sauer–Yorke–Casdagli (1991) for the probabilistic version

### The one thing to absorb
h ∈ L∞(X, μ) is a **cyclic vector** for the Koopman operator Uᴛ if:

```
span { h ∘ Tⁿ : n ∈ ℤ }  is dense in  L²(X, μ)
```

This is equivalent to: the time-delay observables of h generate the full
observable σ-algebra B(X) mod μ. It is the measure-theoretic analogue of
Takens' injectivity condition, and it is generic.

### Questions to sit with
- A measure-preserving system is **ergodic** iff every invariant function is
  constant. How does ergodicity relate to cyclicity? (Ergodicity is weaker —
  it says no nontrivial invariant subspaces; cyclicity says one vector generates
  everything.)
- For a system with purely discrete spectrum (e.g., an irrational rotation),
  what does a cyclic vector look like? Does exp(2πiθ) work?
- For a Bernoulli shift, is the projection onto the 0th coordinate cyclic?
- In the program: `DelayEmbedding.lean` proves that the full delay system is
  not SequentiallyUpperDirected. But the cyclic vector question is about
  measure-theoretic generation, not the index structure. Are these two
  obstructions related or independent?
- Classical Takens needs 2d+1 delays for a d-dimensional manifold. The
  measure-theoretic version uses all finite delays. Is there a finite version
  — a theorem saying N delays suffice under some spectral condition?

---

## 4. The Big Picture Question

All three topics connect at one point:

> The Stone space of B∞ = ⋃ₛ Bₛ (the direct limit of the time-delay Boolean
> algebras) is the inverse limit of the St(Bₛ). When h is cyclic, this inverse
> limit is measure-theoretically isomorphic to X itself.

So the reconstruction theorem says: **the Stone space of the observable algebra
is the state space**.

Question to sit with:
- The program already proves (in `QuerySystem.lean`) that compatible marginals
  + SUD give a unique measure P on Ω. The Stone space of CylGen is
  Ultrafilter(Ω). Is there a sense in which Ω embeds densely into its own
  Stone space, and P extends to a measure on that compactification?
- CE (collective exhaustion) was shown to be irreducible — no first-order
  condition implies it. But the Stone duality route bypasses CE entirely by
  working on the compact Stone space. Does this mean CE is an artefact of
  the algebraic route, or does it reappear somewhere in the Stone picture?

---

## Summary: What to Have Clear Before Returning

1. **Stone duality**: feel the bijection between charges and measures on St(B).
   Especially: why ultrafilters are points of the Stone space.

2. **Content pipeline**: understand how `MeasureTheory.Content` works in Mathlib
   well enough to know whether the clopen-algebra charge fits it directly.

3. **Cyclic vectors**: be comfortable with the equivalence between cyclic vectors
   and generating σ-algebras. Know one example (e.g., irrational rotation).

4. **The bridge**: see why Paper 0′ connects Pillar 1 (extension) to Pillar 2
   (reconstruction) — the Stone space of the observable algebra IS the state
   space when reconstruction holds.
