# Case study 4 (DESIGN): the relativistic three-body triangle (2026-10-19)

reviewed: false. This is a CASE DESIGN, not a result (memory: feedback_reflective_equilibrium). It
is the first test of the working hypothesis below.
- **memory:** physics recalled, not yet checked.
- **hand:** my reading.

## The working hypothesis it tests (conversation, 2026-10-19, NOT recorded as theory)

**Information is local.** Each view carries information about its own variables only. A **world**
is a global composition of that local information. Composition can be:
- *unobstructed*: a world exists;
- *obstructed*: a twist, so no world;
- *underdetermined*: many worlds (case 1's loop of long-run worlds).

"Normal" theory is the case where composition is automatically unobstructed: Boolean boards, trees,
shared clocks. The "pathologies" of order without a centre are the general case.

## The physical anchor

- **Lagrange's solution.** The equilateral solution of the three-body problem has three bodies at
  the corners of a rigidly rotating triangle. **memory**
- **Synchronisation holonomy.** In a rotating system, Einstein (light-signal) synchronisation of
  clocks is not transitive around a closed loop. The offsets accumulated round the loop add to a
  non-zero amount, ∝ (rotation rate × enclosed area)/c². This is the Sagnac effect (Sagnac 1913;
  Anandan 1981; textbook treatments of rotating frames). **memory, to be checked**
- **Do post-Newtonian versions of the equilateral solution exist?** To be checked. **memory**

## The case, in the method's four questions

1. **Queries.** Each pair of bodies runs a synchronisation query: "how far ahead is your clock of
   mine?". The window graph is the triangle.
2. **Answers.** Pairwise offsets d₁₂, d₂₃, d₃₁. These are translation-type (renaming-with-shift)
   windows: t_j = t_i + d_ij.
3. **Joint askability.** No observer stands outside; each pair synchronises by itself.
4. **What a world is here.** A global time: clock settings t₁, t₂, t₃ fitting all three relations.
   It exists iff d₁₂ + d₂₃ + d₃₁ = 0, i.e. iff the composition round the loop is trivial.

## Two readings, which must be kept apart ⟦hand⟧

**(a) Definite clock readings.** If each clock has a definite reading, the family is not even locally
consistent once Σd ≠ 0. It is simply "no global time": a nonzero cohomology class, Penrose-style.
This is owned physics and owned mathematics.

**(b) Answers-first, with no presupposed clock settings.** Each clock's absolute reading is unknown,
"anywhere, evenly" (a translation-invariant density on ℝ), and only the relations are answered.
- The marginals are then consistent: every clock is evenly spread.
- The loop is the **probabilistic renaming twist on the triangle over ℝ with an invariant mean**.
- Whether the triangle's askable questions absorb it is exactly the open **impossible-point
  question** (`gate.triangle_density_plus1`). The step "+1" becomes the Sagnac offset, and the
  impossible point becomes Σd ≠ 0.
- If this holds up, the impossible-point question has a physical meaning: can relational answers
  about clocks that do not close round a loop still be coherent on every question the clocks can
  jointly ask?

## What to check, in order

1. **The physics.** The Sagnac synchronisation holonomy: its exact expression and its standard
   sources. Post-Newtonian Lagrange triangles.
2. **The modelling choice in (b).** Is "evenly spread unknown clock setting" the right answers-first
   state? Compare with how relativity treats clock gauge.
3. **The mathematics.** Reduce (b) to the impossible-point question precisely. The translation group
   is ℝ, not ℤ: is the reduction to the difference plane unchanged?
4. **Then, and only then,** decide what this says about the working hypothesis.

## Status

Design only. Nothing here is a result.
