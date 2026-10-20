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

## Check 1, the physics (2026-10-20; search level unless noted)

- **Clock holonomy is owned physics.**
  - Einstein synchronisation is transitive round closed loops iff the observers' congruence has no
    vorticity, i.e. is time-orthogonal (attributed to Landau–Lifshitz; book not checked).
  - Minguzzi (arXiv:gr-qc/0501055) treats the failure as the **holonomy of the simultaneity
    connection**, whose curvature is the vorticity. It can be non-zero in flat spacetime for a
    rotating congruence.
  - So `definitions_draft.md` §12's "clock holonomy" is OWNED in the relativistic setting. Cite
    it; don't claim it.
- **The Sagnac gap.** Slowly transporting a clock round a rotating disk, or Einstein-synchronising
  along the rim, leaves a gap equal to the Sagnac time difference (Rizzi–Ruggiero–Serafini;
  arXiv:gr-qc/0306128, gr-qc/0604118).
  - **Factor unverified:** 2ωA/c² one-way vs 4ωA/c² round-trip difference. Check the primary
    source before quoting a number.
- **A natural instance with real numbers: the rotating Earth.**
  - Einstein-synchronising clocks station by station round the equator does not close. The gap is
    about 207 ns (memory: Ashby, *Living Rev. Relativ.* 2003, the GPS review; verify).
  - GPS resolves it by **adopting a centre**: coordinate time of the Earth-centred, non-rotating
    frame, with explicit Sagnac corrections.
  - That is "order *with* a centre" chosen as an engineering fix, and the clearest lived contrast
    to the theory's question.

**Updated reading of the case.**
- **(a) Definite readings:** owned (Minguzzi; GPS practice). There is no global Einstein time.
- **(b) Answers-first, absolute settings unknown:** still the impossible-point question. The
  overlaps agree (each pair synchronises fine), and the loop carries a real, measured holonomy.
- **The new datum for the theory:** a natural system where asynchrony is *forced by law* (§12's
  necessary condition holds), with a **clock cocycle** (offsets) whose holonomy is measurable.
  Unlike cases 1–3, nothing supplies a shared clock unless someone imposes a centre.

**Next check (2):** whether the answers-first reading (b) is the right state: unknown settings,
evenly spread over ℝ. Compare with clock gauge in relativity. Then (3), the reduction to the
difference plane over ℝ.

## Check 1, verified against primary sources (2026-10-20; PDFs on the shelf)

- **Minguzzi** (arXiv:gr-qc/0501055, "Spacelike slices from globally well-behaved simultaneity
  connections"; `minguzzi_2005_simultaneity_holonomy.pdf`).
  - The Einstein convention "is nothing but a connection", and its holonomy is non-zero "even in
    flat spacetime" for rotating frames.
  - Its curvature is the vorticity. He names the Sagnac effect and the Earth explicitly.
  - **Clock holonomy is OWNED.** Read from the primary source.
- **Rizzi–Ruggiero** (arXiv:gr-qc/0306128; `rizzi_ruggiero_2003_sagnac_kinematical.pdf`, eq. 18).
  The Sagnac round-trip difference is Δτ = 4πR²Ω/c² · γ = 4ΩA/c² · γ. Read from the primary source.
- **Earth's equator, arithmetic:**
  - 2ΩA/c² = 207.4 ns, which matches the remembered GPS synchronisation gap (Ashby).
  - 4ΩA/c² = 414.8 ns is the counter-propagating difference.
  - So the one-circuit synchronisation gap is 2ΩA/c², half the Sagnac difference. That is
    consistent, but the "half" is not quoted from a source. The Ashby PDF could not be fetched
    (publisher returned HTML), so it still needs verifying.

## Check 2: the answers-first state (2026-10-20) ⟦hand⟧

**Setting.**
- Clocks i = 1, 2, 3 have unknown settings tᵢ ∈ ℝ.
- Pair (i,j) synchronises and answers only the relation t_j = t_i + d_ij.
- The holonomy is h = d₁₂ + d₂₃ + d₃₁, about 207 ns for the equator in the limit of many stations.

**Two-valued answers: overlaps cannot agree (pre-class A).**
- Each view would be the image of an ultrafilter u under s ↦ (s, s + d).
- Then the second clock's marginal is u shifted by d. A non-principal ultrafilter is moved by
  every non-zero shift (Katětov), so neighbouring views cannot agree on their shared clock.
- This is note §5 ("renaming never twists for yes-or-no answers") again.

**Probabilistic answers, gauge-invariant: overlaps agree, no world, hidden-or-visible open.**
- **Choose the state.** Absolute clock setting is a *gauge* in relativity: the origin of time has no
  physical meaning. So the answers-first state should not prefer an origin. Take a
  translation-invariant mean λ on ℝ, and let view (i,j) be the image of λ under s ↦ (s, s + d_ij).
- **Overlaps agree.** Every clock's marginal is λ, by invariance.
- **No world.** A charge on ℝ³ with these views gives full mass to each line t_j − t_i = d_ij. By
  finite additivity it gives full mass to their intersection, which is empty when h ≠ 0.
- **Open: is it a state on the questions the clocks can ask (visible vs hidden)?** That is exactly
  the impossible-point question (`gate.triangle_density_plus1`), over ℝ with step sizes d_ij
  instead of ℤ with +1.

**What the case contributes (equilibrium).**
- Gauge invariance **forces the probabilistic regime.** No two-valued state is translation
  invariant. So "renaming never twists" (two-valued) and "relativistic clocks can twist"
  (probabilistic) are the same fact seen from two regimes.
- The case lands in cell **(ii′) of the three-part theorem**: infinitely many values (ℝ), finite
  adding (an invariant mean is only finitely additive, since no σ-additive invariant probability
  on ℝ exists), probabilistic. **That is exactly the open cell.**
- So the natural phenomenon picks out the open mathematical question by itself. This is the first
  case to do so.

**Check 3 (next).** Reduce over ℝ:
- If the d_ij are rational multiples of one step, restrict to a coset lattice and reduce to the ℤ
  question.
- For incommensurable offsets, check whether ℝ adds anything.
- Then attack the impossible point itself (ergodic Ramsey territory; prior art first).

## Check 3: reduction over ℝ (2026-10-20) ⟦hand, unverified⟧

**Transport lemma.**
- Take a per-variable map f : X → Y applied to each clock.
- Suppose it pushes the invariant mean to an invariant mean and carries each view's relation to the
  target's relation.
- Then preimages of pair events are pair events, so f⁻¹ maps the target carrier D_Y into D_X.
- The forced functional pulls back: Λ_X(1_{f⁻¹E}) = Λ_Y(1_E).
- **So a visible twist (some buildable E with Λ < 0) in the target gives one in the source.**

**Chain of reductions.**
1. **Offsets → holonomy only.** Rename clocks: t₂′ = t₂ − d₁₂, t₃′ = t₃ − d₁₂ − d₂₃. These are
   per-variable bijections of ℝ, and they preserve D and the invariant mean. The relations become
   t₂′ = t₁, t₃′ = t₂′, t₁ = t₃′ + h. Scaling by 1/h then gives h = 1. **Commensurability of the
   offsets is irrelevant. Only whether the holonomy is non-zero matters.**
2. **ℝ → ℤ by integer part.** All three relations preserve the fractional part. The floor map pushes
   the invariant mean on ℝ to one on ℤ and the relations to x₁ = x₀, x₂ = x₁, x₀ = x₂ + 1.
3. **Steps of +1 (the original gate) → the same target.** Rename to steps (0, 0, 3) over ℤ, then
   map n ↦ ⌊n/3⌋, which pushes to (0, 0, 1).

**The core problem Z₁.** The triangle over ℤ, invariant mean λ, with views x₁ = x₀, x₂ = x₁ and the
closing view x₀ = x₂ + 1: two identities and one step.
- **If Z₁ is visible**, a buildable question with Λ < 0, then **every** relativistic clock loop with
  non-zero holonomy is visible, and so is the original +1 gate (by the transport lemma).
- **If any clock loop is hidden**, so is Z₁.
- The converse transfers (Z₁ hidden ⇒ clocks hidden) are not proved.

**What it says.** Physically, all that matters is that the holonomy is non-zero. Its size,
direction and how it is split between the pairs drop out. Mathematically, the impossible point
reduces to one universal problem: **can the questions askable from two "same" views and one "one
step later" view, read with a translation-invariant average, expose the step?**

**Next: the impossible point Z₁ itself.**
- Earlier hand reduction (`gate.triangle_density_plus1`): on translation-invariant questions,
  Λ is evaluation at the impossible point u = v = 0, w = 1 of a decomposition
  1_E = g₀(u) + g₁(v) + g₂(w) with u + v + w = 0.
- Prior art first: invariant means and three-direction decompositions on ℤ² (ergodic Ramsey;
  Bergelson–Ferré Moragues; Navara's two-sided unbounded regime).
