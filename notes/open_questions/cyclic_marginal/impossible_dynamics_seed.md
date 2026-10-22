# Dynamics on impossible figures (seed, 2026-10-17)

reviewed: false. **PARKED 2026-10-17 (user approved)**; see the last section. This is the user's idea (2026-10-16), seeded as `conj.impossible_dynamics` in
`glued_carriers_taxonomy.json`. It was taken up after the triangle settled.

## The puzzle: Escher's staircase as a frieze

Escher's *Ascending and Descending* repeats. Unroll it and you get an endless
frieze of landings …, x₋₁, x₀, x₁, x₂, …:
- every flight goes up: x_n < x_{n+1};
- the picture repeats every 4 landings.

Walking the stairs is the dynamics: one step is the shift x_n ↦ x_{n+1}.

**What it means for walking to change nothing:**
- **A real building.** Repeating every 4 landings would force x₀ < x₁ < x₂ < x₃ < x₄ = x₀, so there
  is none. That is the ring of length 4.
- **On the unrolled frieze.** There are real buildings, for example x_n = n. But walking changes them,
  since x_n = n becomes x_n = n+1.
- **The question.** Is there a consistent answer pattern about the frieze that walking leaves
  unchanged, but that no building, not even an ideal one, fits in a way walking leaves unchanged?

## Dictionary

| figure | dynamics |
|---|---|
| a loop in the window graph | a group acting freely on the window graph (the quotient has the loop) |
| a window (one flight) | one time step {x, Tx} |
| the twist (all flights up) | a cocycle with nonzero "winding": steps that never sum back to 0 |
| real building | a height function h with h(Tx) = h(x) + step (a coboundary) |
| pointless state | an *invariant* state with no *invariant* ideal point |

## Hand observations ⟦HAND — unverified⟧

**H1. An invariant state on the frieze exists (L ≥ 4).**
- Let ι: ℕ^L → ℕ^ℤ copy a ring configuration periodically.
- The preimage of a frieze window event is a ring window event. Preimages also respect complements
  and countable disjoint unions. So ι⁻¹(D_line) ⊆ D_ring.
- Hence s = μ ∘ ι⁻¹ is a state on the frieze carrier, with μ the ring staircase state
  (Lean, `WindowGluing`). Every window of s is p⊗p, with every flight going up.
- s is shift-invariant provided μ is invariant under rotating the ring. By locality
  (`thm:star`), a state on a triangle-free graph is determined by its window values, and the window
  family is rotation-symmetric, so μ is.
- **Check needed:** that `thm:star` applies to the ring (L ≥ 4, triangle-free: yes, hand).

**H2. No invariant ultrafilter fits it.**
- Suppose U is a shift-invariant ultrafilter on ℕ^ℤ containing {x₀ < x₁}.
- Then U contains the non-constant sequences, an invariant set on which the shift has no fixed
  point.
- Katětov's three-set lemma (cited, not proved here): a map with no fixed point splits its domain
  into A₁, A₂, A₃ with f(Aᵢ) ∩ Aᵢ = ∅.
- So some Aᵢ ∈ U. By invariance σ(Aᵢ) ∈ U as well, which gives ∅ ∈ U, a contradiction.
- **Consequence (H1 + H2):** the frieze carries an invariant state that no invariant ideal point
  fits. The twist has moved out of the window graph, which is a line (a forest), and into the
  group action.

**H3. σ-additively, even a stationary version is impossible.**
- If X₀ < X₁ almost surely with the same law, then for every K,
  E[min(X₁,K)] − E[min(X₀,K)] = 0, while min(X₁,K) ≥ min(X₀,K) with strict inequality when
  X₀ < K.
- So P(X₀ < K) = 0 for every K, which is impossible.
- This is the dynamical form of `prop:sigma`.

**H4. The circle version.**
- Rotate a circle by an irrational angle α, and let each step go up by 1.
- A *measurable* height h with h(x+α) = h(x) + 1 is impossible. For every t, e^{2πi t h} would be an
  eigenfunction of the rotation with eigenvalue e^{2πit}, but the rotation's eigenvalues are only
  the countable set {e^{2πikα}}.
- Heights that are not measurable exist (choose one per orbit).
- So here the role of "ideal" is played by regularity (measurability or invariance), not by
  compactness.

## Seam guess

These theories each own a piece of the region:
- **Penrose:** an impossible figure is a nonzero class in Čech H¹ (Penrose 1991/1992). That part is
  owned.
- **Cocycles and coboundaries in ergodic theory:** Gottschalk–Hedlund 1955; Anosov 1973;
  K. Schmidt 1977. Owned.
- **Amenability and invariant means:** Tarski, and finitely additive *probability* invariant states.
  Owned.
- **No invariant ultrafilters for free actions:** Katětov 1967, essentially folklore. Owned.

The candidate seam is **two-valued invariant states on glued (non-Boolean) carriers**: the
equivariant version of pointless coherence. It lies between the covering-space or cohomology view
and invariant means. Means are probability-valued, and our states are two-valued.

## Theory sketch: candidate conjectures

**CE1 (covering).** Let a group G act freely on a window graph Γ. Then G-invariant states on Γ
correspond to states on the quotient Γ/G. In particular, equivariant pointlessness on a free
cover happens exactly when the quotient has a pointless state.
- If true, the dynamics adds nothing beyond loops. It would be a statement about quotients, and an
  owner should be looked for.

**CE2 (aperiodic).** Probe P1 decides between CE1 and CE2. Some shift-invariant states on the
ℤ-line staircase carrier do **not** come from any periodic (ring) state. If so, the dynamics is
genuinely new: twist without a finite loop, for example along a Sturmian or irrational-rotation
pattern.

## Pre-registered probes (2026-10-17, before any work)

**P1. Does every invariant state on the frieze come from a ring?**
- The setting is the ℤ-line, windows {n, n+1}, window states p⊗p going up.
- Does every shift-invariant state on the carrier factor through some ring of length L via ι?
  - (a) Yes → CE1 gains support, and the dynamics reduces to loops in quotients.
  - (b) No → CE2. Then classify the aperiodic invariant states.

**P2. Circle.**
- The setting: slots are the points of the circle, windows are {x, x+α}, and steps go up.
- Does a rotation-invariant state exist on the carrier? If one exists, is it pointless in the
  equivariant sense?
  - (a) Yes → a genuinely ergodic impossible figure.
  - (b) No → the obstruction is σ-like even for finite additivity, and the reason is the next
    object of study.
- **Scope:** the possibility space is uncountable (ℕ^X), while our theorems assume finitely many
  slots. First check which results survive infinitely many slots: locality, and the forests
  theorem by compactness.

**Pre-check on P1 ⟦HAND — not a fired gate⟧.**
- Locality (`thm:star`) says every buildable question lives on one star.
- Questions at two distant stars of the line constrain disjoint coordinates. So they intersect
  whenever both are nonempty, and countable disjoint unions cannot spread across stars.
- If that proof survives infinitely many slots, window values determine every state on the line.
  The invariant state is then unique (the ring pullback, for every L), and P1 fires (a)
  trivially.
- All content then sits in H2 (no invariant ideal point) and in P2. Verify locality on infinite
  triangle-free graphs before firing.

**First step.** Run a hostile owned-region scout on the four seam pieces above and on "invariant
two-valued states / equivariant contextuality / periodic contextuality". Do this before any hand
work on P1 or P2.

## Owned-region scout (2026-10-17, sonnet, about 9 searches, snippets only): PARTLY OWNED, core NOT FOUND

**Owned:**
- **Penrose 1991.** Structural Topology 17, 11–16; reprinted in Leonardo 1992. Region: impossible
  figures as Čech H¹ with coefficients in R₊ (Z₂ for the heptagonal staircase). Read only through
  snippets and the AMS Feature Column 2014.
- **Katětov 1967.** CMUC 8, 431–433. Region: the three-set partition for maps without fixed points.
  The corollary "no invariant ultrafilter" is folklore with no reference found; the n-Category
  Café post (2022) found none either. This covers H2.
  `cyclic_marginal_scoping.md` §5 already used "the Katětov argument for graph-type
  ultrafilters".
- **Gottschalk–Hedlund 1955.** Region: continuous coboundaries over minimal systems, which are
  exactly the cocycles with bounded sums.
- **Anosov 1973.** Region: the measurable homological equation over an irrational rotation. This
  is close to H4. Only the title was seen.
- **K. Schmidt 1977.** Region: essential values. The attribution is UNCONFIRMED.
- **Okay–Roberts–Bartlett–Raussendorf 2017 and Raussendorf 2016.** Region: group-cohomology
  witnesses of contextuality.
- **Abramsky–Mansfield–Barbosa 2011 and ABKLM 2015.** Region: sheaf H¹ obstructions in finite
  scenarios. Carù (arXiv:1701.00656) finds H¹ incomplete; author and title only weakly confirmed.
- **Invariant means and Tarski.** Region: amenability. A {0,1}-valued invariant mean is an
  invariant ultrafilter (Steprāns, Bonn 2011 notes). That is known territory on the Boolean P(ℕ),
  not on a glued carrier.

**Close to the seam:**
- Yang–Zeng–Navascués–Wang et al. (arXiv:2112.11646): translation-invariant contextuality on
  infinite chains. Finite outcomes, quantum or non-signalling; no notion of ideal point.
- Navara–Tkadlec 1991: automorphisms of concrete logics.
- arXiv:1705.03045: invariant probability measures on orthomodular lattices.

**Not found:**
- Invariant two-valued finitely additive states on a glued non-Boolean carrier that no invariant
  ultrafilter reproduces (H1 + H2).
- Any citation for H3 (a standard argument).

**Coverage gaps, to close before claiming:**
- Hindman–Strauss on invariant and idempotent ultrafilters in βG.
- Bhaskara Rao on invariant charges.
- Dubins–Savage on finitely additive stationary processes.
- Carù's follow-ups.
- Full texts of Penrose and Anosov.

**Reading for the theory.** The owned pieces split the problem in two: the cohomology and coboundary
side, and the means side, where means are probability-valued. The candidate seam is the two-valued,
non-Boolean, invariant combination.

## Session 2026-10-17: probes run ⟦HAND — unverified⟧

**L∞ (locality survives infinitely many slots).** The proof of `thm:star` never uses finiteness:
- *Rigidity:* window questions on windows that share no coordinate meet.
- *Pairwise-meeting edges:* in a triangle-free graph they share a vertex, for any number of edges.
- *Slicing* and *regrouping* (a window σ-algebra is all subsets of X²).

So on any triangle-free window graph, D = disjoint unions of window questions on a star. When
degrees are finite (the line, the circle-rotation graph), every state is the finite sum of its
window values. Window values therefore determine the state, and invariance of the window family
gives invariance of the state.

**gate.dynamics_frieze_periodic fired (a).**
- With the staircase windows (p⊗p, flights up) the state on the ℤ-line is unique. It equals the
  ring pullback for every L for which the ring state exists.
- General invariant states on the line correspond to constant consistent window families u (equal
  marginals). On a forest, every such family extends (by compactness, gluing finite paths).
- Such a state factors through ring L iff u extends on ring L. That is the theory's open
  "extension on triangle-free graphs" question, not a new one.

**Degeneracy lemma (this is what changes the picture).**
- Let a group act on the slots, with an invariant window family u on the orbit windows {x, gx}.
  An *invariant* ideal point fits the state iff u(diagonal) = 1, that is, iff u lives on equal
  heights.
- Proof:
  - An invariant ultrafilter cannot contain the invariant set of non-fixed points, on which the
    action has no fixed point (Katětov's partition). So it lives on the fixed points, the
    orbit-constant height functions, which forces u(diagonal) = 1.
  - Conversely, if u = (a ↦ (a,a))₊q, then the constants, distributed by q, give an invariant
    ultrafilter. Locality makes it fit the whole state.
- **Consequence:** "invariant state with no invariant ideal point" holds for *every* non-diagonal
  family. That includes *possible* figures: u = (a ↦ (a, a+1))₊q, where the real building
  h_n = n exists. Invariance only detects *motion*, i.e. symmetry breaking, not impossibility.

**gate.dynamics_circle fired (a), with its "then" defeated.**
- On the irrational rotation the window graph is a union of ℤ-lines. So a rotation-invariant state
  exists, and is unique given the windows. By the degeneracy lemma it has no invariant ideal point.
- That is outcome (a) as stated. But the branch's reading, "a genuinely ergodic impossible
  figure", does not follow, since the same holds for possible figures.

**What the session says about the theory.**
- *The twist belongs to a loop in the window graph, not to a group acting on it.* A free cover
  (line over ring, circle orbits) is a forest. On a forest every consistent family extends, so
  the cover forgets the loop. The loop's twist shows up only downstairs (rings, triangle).
- What dynamics adds beyond motion is **regularity**: H4 (no *measurable* height on the irrational
  rotation). That is the coboundary question, owned by Anosov 1973, Gottschalk–Hedlund and
  Schmidt.
- The seam guess "invariant two-valued states on glued carriers" is real but degenerate. Its
  criterion is u(diagonal) ≠ 1.

**Recommendation (user's call).** PARK `conj.impossible_dynamics`.
- Bank: L∞, the degeneracy lemma, and the slogan "the twist lives in the loop, not the action".
- The guardrail is honoured: no standing check flipped toward a live question, and the
  regularity version is owned.
- Re-open only with a probe in which regularity is *finitely additive*, for example invariant
  charges on the glued carrier with a Borel or measurable condition. That is not owned as far as
  the scout saw. Bhaskara Rao's invariant charges are unread.
