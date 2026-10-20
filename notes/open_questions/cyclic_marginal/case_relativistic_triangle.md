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

## Check 4: prior art for the core Z₁, shelf first (2026-10-20; primary sources on the shelf)

**The invariant part of Z₁ is the Czech school's three-direction problem.**
- On questions that depend only on differences u = x₁ − x₀ and v = x₂ − x₁ (with w = −u − v), the
  carrier is the class generated by the level sets of u, v and u + v on ℤ².
- The forced functional there is a state concentrated at the **impossible triple**
  u = 0, v = 0, u + v = −1.
- That is the object of Navara–Pták 1983 and Navara 1984 (Gudder's integral-additivity problem): a
  state on the σ-class generated by f, g, f + g with m(f = a) = m(g = b) = m(f + g = c) = 1 and
  c ≠ a + b, i.e. ∫f + ∫g ≠ ∫(f + g).

**What they prove (read from the PDFs).**
- **Navara–Pták 1983, Thm 1.** Such a two-valued m exists only if some set K(a,b) falls outside the
  class. If all K(a,b) are in the class, m is concentrated (a point).
- **NP 1983, Example.** On (ℚ ∩ (0,1))² with f = x, g = y: m(A) = 1 iff A contains one of three lines
  B, C, D, with D a level set of f + g. B, C, D meet pairwise and have **no common point**. This is a
  two-valued, σ-additive state at an impossible triple. The phenomenon exists **for dense ranges**.
- **NP 1983, Thm 2.** If f takes finitely many values: concentrated, so no impossible point.
- **Navara 1984, Theorem.** Also concentrated if R_f is nowhere dense, R_g ≠ ℝ and one function is
  bounded on one side. He remarks that none of the conditions can be dropped, citing NP 1983.

**Where Z₁ sits.**
- Its ranges are ℤ: nowhere dense ✓, ≠ ℝ ✓. But both directions are **unbounded on both sides**,
  so Navara 1984's third condition fails.
- So Z₁'s invariant part is exactly **the two-sided-unbounded integer case of the Navara–Pták
  problem**. None of the shelf papers settles it. NP 1983's example uses dense ranges, and I did not
  find an integer two-sided example there. Navara's "none can be omitted" remark may be loose for
  condition (iii); this needs checking.

**Consequences.**
- If a two-valued (even finitely additive) state at the impossible triple exists on the integer
  three-direction class, then Λ ≥ 0 on every difference question. Z₁ is then **hidden** on that
  part, though non-invariant questions still need checking.
- If every such state is concentrated (some K(a,b)-type set is buildable), then Z₁'s twist is
  **visible**, and by the transport lemma so is every relativistic clock loop.
- Either way the relativistic clock problem lands in **owned framework, possibly open instance**:
  Gudder 1969 → Navara–Pták 1983 → Navara 1984. Cite them. Do not claim the framework.

**Next.**
1. Decide whether K(a,b)-type sets are buildable in the integer two-sided class: Navara's induction
   on values needs a starting value, which two-sided unboundedness removes.
2. Prior-art pass on later literature on "Gudder's problem / additivity of the integral on
   σ-classes" (Dravecký–Šipoš 1980, Ovchinnikov, Pták–Pulmannová book) for the two-sided integer
   case.

## Check 4b: prior art settled the difference part, and (a) a first hand attempt (2026-10-20)

**(b) result (scout + primary source).** Dravecký–Šipoš 1980, Example 6 (`dravecky_sipos_1980_additivity_gudder_integral.pdf`,
p. 301, read by me from the page image):
- If all non-empty preimages of f, g, f + g pairwise meet, then A_f ∪ A_g ∪ A_{f+g} is already a
  σ-class.
- A Dirac pair (α for f and g, β for f + g) is then a two-valued σ-additive state at an impossible
  triple.
- On ℤ² with f = x₁, g = x₂ the hypothesis holds: (x, y − x) meets both. So **the difference part
  of Z₁ is hidden, and this is OWNED** (D–Š 1980; it is also the example for Navara's condition
  (iii)).
- **Process failure.** This was already in our taxonomy (`own.dravecky_sipos_flight_subcarrier`,
  audit 2026-10-17). I missed it in the shelf-first check. The taxonomy entry states the real
  content: *extension to the full triangle carrier*, which D–Š's union class lacks.
- Shelved as well: Navara 1989 survey (`navara_1989_integration_generalized_measure_spaces.pdf`).

**The residual question, now sharp (Z₁-full).** Does the invariant-mean pre-state
Λ(g) = λ(f₀₁(s,s) + f₁₂(s,s) + f₂₀(s,s+1)) stay ≥ 0 on the **full** triangle carrier D₃ over ℤ³?
D₃ includes pair events in absolute positions, whose intersections across views D–Š's class
cannot form. This is the probabilistic twin of the Lean two-valued triangle theorem.

**(a) Hand attempt: Navara's witness is our E\*.** ⟦hand; case check done⟧
- Navara's set K(a,b) = (u<a ∧ v<b) ∪ (u<a ∧ u+v ≥ a+b) ∪ (v<b ∧ u+v ≥ a+b) has the linear identity
  **1_K = 1{u<a} + 1{v<b} − 1{u+v < a+b}**. This is Navara 1984's measure equation as a function
  identity; I checked it in four cases. So K always lies in the span.
- At Z₁'s impossible point (u, v, u+v) = (0, 0, −1), the set K(0,0) gets **Λ = 0 + 0 − 1 = −1**.
  So if K(0,0) were buildable, Z₁ would be visible, by Navara's own argument.
- In clock coordinates, 1_{K(0,0)} = [x₁<x₀] + [x₂<x₁] − [x₂<x₀]. Off ties this is the
  **anticyclic set**, the complement of E\* (machine-checked on all distinct triples in [−3, 3]).
  Lean catches both: `InF` contains every set agreeing with the cyclic *or* anticyclic set on the
  distinct points of some infinite P³, and `not_inF_of_mem` shows no such set is buildable over ℕ. Over ℤ the lift argument should carry over unchanged
  (raise the lowest above the highest); hand, not checked line by line.
- **So Navara's route to visibility is blocked exactly where the Lean triangle theorem says.** The
  one witness the 1980s theory supplies is the unaskable (anti)cyclic question.

**Status.**
- Z₁-full remains open.
- Evidence leans *hidden*: the canonical witness is unaskable, and the difference part is hidden
  (D–Š).
- A proof would need either a probabilistic extension theorem for D₃ (the twin of the Lean
  construction) or a different buildable witness.
- **Note:** Λ cannot be a mixture of two-valued D₃-states. Each two-valued component would need
  overlap-consistent marginals, and shifts move ultrafilters. So any extension is genuinely
  probabilistic.

**What it says.** The 1980s additivity problem and the triangle's unaskable cyclic question are the
same obstruction. Where expectations of sums fail to add (Gudder's problem), the failure is
witnessed by the (anti)cyclic set, and the triangle cannot ask that set.

## Check 4c: shelf reading pass (2026-10-20)

- **Maharam 1972, Example 2.1 (p.129, verified).** Three lines spanned by (1,0), (0,1), (1,1) carry
  consistent linear maps (0, 0 and "x ↦ x") with no common extension. This is the impossible triple
  in linear form, which is Gudder's problem at the level of linear maps.
- **Maharam, Thm 6.1(iv) (verified).** A positive extension exists iff Σxᵢ ≥ 0 implies Σφ(xᵢ) ≥ 0.
  This is the dual test for Z₁: Λ ≥ 0 on the carrier is the *carrier-level* version. Extension to
  all of ℤ³ is impossible anyway, since Kelley's intersection number for three sets with empty
  triple intersection is 2/3.
- **Navara 1989, Remark 3:** a σ-additive state at an impossible triple on P × Q (P = 2^ℤ, Q
  dense) shows hypothesis (3) of his Thm 2 is needed. On ℤ², hypotheses (2) and (3) hold and (1)
  (one-sided bound) fails. That is D–Š Ex. 6 territory, already noted.
- No shelf item settles Z₁-full (positivity on the full triangle carrier over ℤ³).
- **Keleti–Preiss Lemma 12** (non-crossing boundary families off a σ-ideal) is the nearest template
  for a *non-membership* proof. It is built on countable unions and a topological ideal, so it is a
  lens for discrete ℤ³.

## Check 4d: Lean, Navara's witness over ℤ (2026-10-20)

`formalization/staging/TriangleCyclic.lean`, section `OverZ` (0 sorry; standard axioms; 37 s).
- `mem_pre`: the triangle carrier over ℤ pulls back into the carrier over ℕ along the
  coordinatewise inclusion. This is the transport lemma, machine-checked for this map.
- `not_mem_of_restrict_inF`: any set over ℤ whose restriction to ℕ³ lies in `InF` is
  unbuildable.
- `navaraK_not_mem`: **Navara's K(0,0) is not in the carrier over ℤ.**
- The clocks' impossible point therefore cannot be exposed by the one witness the 1980s theory
  supplies. Z₁-full (positivity of Λ on the whole carrier) stays open.

## Attempt (i), step 1: the unit must escape to infinity (2026-10-20) ⟦hand; checked twice⟧

**Placements.**
- A placement is a configuration c ∈ ℤ³ averaged along the diagonal:
  μ_c(h) = λ_s h(s + c₀, s + c₁, s + c₂).
- Its view laws depend only on the differences u = c₁ − c₀, v = c₂ − c₁, w = c₀ − c₂, with
  u + v + w = 0.
- The clock state Λ needs view laws u ≡ 0, v ≡ 0, w ≡ 1.

**Lemma (no finite signed decomposition).** Λ is not a finite signed combination Σ a_c μ_c of
placements, even agreeing only on the three views.
- *First-moment proof.* Every placement has u + v + w = 0, so any combination has
  Σ a_c (u_c + v_c + w_c) = 0. The required marginals give 0 + 0 + 1 = 1.
- *Generating-function proof.* Write p(x,y) = Σ a_c x^{u_c} y^{v_c}. The views force p(x,1) = 1,
  p(1,y) = 1 and p(t,t) = 1/t. The first two give p = 1 + (x−1)(y−1)r for a Laurent polynomial r.
  Then r(t,t) = −1/(t(t−1)), which has a pole at t = 1. Contradiction.

**Reading.**
- Any representation of the clock state by actual configurations needs mass at unbounded offsets:
  the holonomy's unit has to *escape to infinity*.
- That is the converse picture to the box-limit lemma ("the unit of down never escapes" for limits
  of finite mixtures). It is why Λ is not a limit of finite pictures, and why finite truncation
  cannot decide Z₁.

**Next (step 2).**
- Truncate: r_N(x,y) = −Σ_{k=0}^{N} x^{k−1}·(…) chosen so the diagonal matches up to a remainder
  carried by far placements (offsets ≥ N).
- Then use the Lean far-point structure: the lift lemma and const_cyc / const_acy make membership
  of a carrier set at far points depend only on cyclic vs anticyclic type, under the lemma's
  hypotheses.
- If the far remainder is controlled by those two constants, positivity of Λ reduces to a finite
  check plus a sign condition on the two constants.
- Caveat: const_cyc needs the set to avoid far anticyclic points. General carrier sets need the
  box identity directly.

## RESULT, step 2: Z₁ is VISIBLE (2026-10-20). REVERSAL of "leans hidden" ⟦hand reduction + exact computation⟧

**The finite quotient sees the twist.**
- Reduce clock readings mod n. The map s ↦ s mod n pushes the invariant mean on ℤ to the uniform
  law on ℤ_n, and the relations to x₁ ≡ x₀, x₂ ≡ x₁, x₀ ≡ x₂ + 1 (mod n).
- By the transport lemma (machine-checked for the inclusion as `mem_pre`; the same proof works for
  any per-coordinate map), a buildable set over ℤ_n pulls back to a buildable set over ℤ with the
  same forced value.

**Witness (n = 2), checked by hand.** W = {x₀ ≡ x₂ ≢ x₁ (mod 2)}, i.e. "clocks 1 and 3 have the
same parity, clock 2 the other".
- With two values, 1_W = ½[x₀=x₂] − ½[x₀=x₁] − ½[x₁=x₂] + ½.
- The forced values of the pair terms are 0, 1, 1, so **Λ(W) = −½**.
- W is buildable over ℤ₂³ (explicit Dynkin closure, `verification/z1_modn_witness.py 2 0,0,1`).
- n = 3 gives a 9-point witness with Λ = −2/3, verified in exact arithmetic: the functional kills
  all 8 dependencies, the witness is in D at depth 5, and the pullback is consistent on [−4,4]³
  (`verification/z1_mod3_verify.py`).

**Consequences.**
- **Z₁ is visible.** By the reductions (renaming, scaling, floor, mod 2), **every relativistic clock
  loop with non-zero holonomy, read with an even spread, has an askable question exposing it**:
  read each clock in units of the holonomy and compare *parities* pairwise.
- The original gate (+1, +1, +1 over ℕ, holonomy 3) is visible via mod 2: the set {x₀ ≡ x₁ ≡ x₂}
  gets Λ = −½. `gate.triangle_density_plus1` FIRES branch (b).
- So case 4 does **not** produce pointless coherence. The relativistic twist is real (no world) but
  *visible*: class Tv, not Th.

**What the proof says (theory, candidate; prior art owed: residual finiteness / profinite detection
of holonomy).**
- Renaming (gauge) twists are detected by **finite quotients**. Nonzero holonomy in ℤ survives mod
  n for some n, and finite triangles see every twist.
- Hiding needs a twist that **no finite quotient preserves**: order ("beyond") types, as in the Lean
  staircase. No finite quotient respects "x₁ far beyond x₀".
- This sharpens the regime split: **gauge twists are finitely visible; order twists can hide at
  infinity.**

**Equilibrium with experience.** Clocks whose synchronisation fails round a loop produce a
*detectable* inconsistency (parity questions any pair can ask). Pointless coherence in nature
would need an *order*-type idealisation (something running off to infinity), not a gauge one.
