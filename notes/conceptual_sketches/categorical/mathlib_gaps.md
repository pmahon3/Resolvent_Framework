---
# Mathlib 4 — Availability for the Categorical Program
*Working note — 2026-03-19*

---

## What exists

| Structure | Mathlib file | Key declarations |
|---|---|---|
| Giry monad | `MeasureTheory/Measure/GiryMonad.lean` | `Measure.bind`, `Measure.dirac`, `join`, monad laws |
| Giry functor on MeasCat | `MeasureTheory/Category/MeasCat.lean` | `MeasCat.Giry` |
| Kleisli category (general) | `CategoryTheory/Monad/Kleisli.lean` | `Kleisli T`, `toKleisli`, `fromKleisli`, `adj` |
| Monad algebras (general) | `CategoryTheory/Monad/Algebra.lean` | `Algebra T`, free/forgetful adjunction |
| Markov kernels | `Probability/Kernel/Defs.lean`, `Basic.lean` | `Kernel`, `IsMarkovKernel`, composition `∘ₖ`, disintegration |
| Finite product measures | `MeasureTheory/Constructions/Pi.lean` | `Measure.pi`, `Measure.tprod` |

The general `Kleisli T` construction applies to any monad in any category, so
`Kleisli` instantiated at the Giry monad is in principle available — it just
isn't named or developed as a standalone object. The morphisms in
`Kleisli GiryMonad` are exactly Markov kernels (`Kernel α β`), which *are*
extensively developed.

---

## What is absent

### Projective limits in Meas
The categorical limit `lim F` for diagrams `F : Iᵒᵖ → Meas` is not in
Mathlib. Finite products are present; the general projective limit
construction is not.

**Mathematical status**: Classical and uncontroversial. The projective limit
of a countable inverse system of measurable spaces exists as a measurable
space (take the product, restrict to compatible sequences, equip with the
trace σ-algebra). No open mathematical questions.

**Why absent**: Formalizing general categorical limits in **Meas** requires
connecting the categorical limit machinery (`CategoryTheory.Limits`) to
`MeasureTheory`. This is a formalization gap, not a mathematical one.

### Kolmogorov extension theorem
The theorem that a consistent family of finite-dimensional distributions
extends to a measure on the projective limit is not in Mathlib.

**Mathematical status**: Proved by Kolmogorov (1933). Requires Polish/standard
Borel hypotheses in the general case (inner regularity / tightness). Multiple
proofs in the literature (Kolmogorov, Bochner, Prokhorov, categorical via
Radon measures). Not an open problem.

**Why absent**: The proof requires the Prokhorov tightness theorem and
inner regularity machinery, which are only partially in Mathlib. This is a
known gap — it appears on informal Mathlib roadmap discussions — but the
formalization effort is non-trivial. The key difficulty is showing that the
content measure on the projective limit is σ-additive, which requires
compactness/tightness arguments.

**Relevance to our program**: Our `observational_extension` theorem in
`QuerySystem.lean` is doing the work that Kolmogorov would do in the
classical setting — constructing a measure on the projective limit from
compatible marginals. We build it from scratch rather than citing Kolmogorov
because it isn't available in Mathlib. This also means our formalization is
genuinely new Lean infrastructure, not a wrapper around existing Mathlib results.

### Giry monad algebras (specifically)
The general monad algebra framework (`Algebra T`) exists, but there is no
named development of Giry monad algebras — i.e., measurable spaces equipped
with an `𝒫X → X` structure satisfying the algebra axioms — as a standalone
object in Mathlib. The framework is there; the instantiation is not.

---

## Implications for `categorical_program.tex`

When writing the program's categorical picture:

1. **Can cite Mathlib directly**: Giry monad, Markov kernels, general Kleisli
   construction, monad algebras.

2. **Natural instantiation, not yet named**: The Kleisli category of the Giry
   monad — morphisms are `Kernel α β`, composition is Chapman-Kolmogorov —
   is a natural instantiation of `Kleisli GiryMonad` but hasn't been
   developed as a named object. We can describe it as such.

3. **Must build from scratch**: Projective limits in Meas, Kolmogorov
   extension, and the specific adjunction claimed in the program (forgetful
   functor from probability spaces to compatible marginal systems has a left
   adjoint) are all outside current Mathlib. These are the mathematically
   novel parts of the formalization program.

4. **Our `QuerySystem.lean` fills the Kolmogorov gap**: The
   `observational_extension` theorem is essentially the Kolmogorov extension
   theorem restricted to the query system setting. It is new Lean
   infrastructure.
