# Reading Directions

*Not a syllabus. A list of questions to bring to specific sources.*

## The programme's questions

The programme reconstructs structure from relations, not spaces.
Point-spaces (the real line, Stone spaces, Hilbert spaces) are
outcomes of the reconstruction, not its starting material. This
is a bet: that the relational description — contexts, reference
frames, directed refinement — is the right starting point, and
that the structures usually assumed (points, σ-algebras, global
states) are *reconstructed* from it.

Three central questions organize the reading:

### 1. What must be added to observation to get structure?

The persistent question across all phases:

- Phase 1: observation → dynamics (semigroup)
- Phase 2-3: observation → geometry (curvature, metric, action)
- Phase 4-6: observation → probability (CE), realization (descent),
  value-definiteness (distributivity)

The reading form: *Where does someone identify the exact condition
that forces a valuation to behave — and what structure does that
condition live in?*

### 2. Reconstruction without points.

When can observation be modeled relationally — via contexts and
reference frames — rather than by presupposing an underlying
set-theoretic structure of points? Numerical identity
(point-evaluation) is the degenerate case where all contexts
contract to a single point.

Paper I does this for the Boolean case: probability is
reconstructed from directed refinement of finite Boolean algebras,
without assuming a sample space. The open question is whether this
extends beyond the Boolean case, and if so what plays the role of
"directed refinement" when the algebra is not distributive.

*(Sharpened by Zafiris, Ch. 6 of Foundations of Relational Realism:
the relational description is not a technical convenience but the
starting point; point-spaces are what you reconstruct, not what
you assume.)*

### 3. Local-to-global extension.

When does locally defined information (on each Boolean context)
determine a global object? What are the *conditions on the site*
— not the individual valuations — that control whether local data
extend globally?

CE is one instance: local charges always glue finitely additively
(Kolmogorov), but gluing to a σ-additive measure requires something
extra — and that "something extra" is not a sheaf condition on any
known topology (Zafiris 2006, Biesel 2024: dictionary translation,
not theorem). Paper II's EA/PR/VDR is another instance: the
obstruction to global state extension in the non-Boolean case is
non-distributivity rather than failure of σ-additivity.

The general form: both the Boolean and non-Boolean extension
problems are local-to-global questions on different categories.
What controls the answer is the structure of the site, not the
properties of individual states.

*(Sharpened by Zafiris, Ch. 6: the gluing conditions on overlapping
Boolean reference frames are the structural content; the topology
of the site is what does the work.)*

## Directions (ordered by contact with programme core)

### 1. Caramello — "Theories, Sites, Toposes" (2018)

**Question while reading:** Is there a Morita equivalence that
makes CE into a geometric (site-theoretic) condition?

**Why:** Caramello systematically translates model-theoretic
properties into topos-theoretic ones. The CE question — when
does a structural condition force σ-additivity? — is exactly
this kind of translation problem. If CE corresponds to a
topological/geometric property of the classifying topos, the
sheaf-condition seed becomes a theorem.

**Contact with programme:** CE-as-sheaf seed directly.

### 2. Vickers — "Topology via Logic" (1989) / constructive measure theory

**Question while reading:** In the locale corresponding to St(B),
what is the frame-theoretic characterization of "a valuation is
supported on the sublocale of principal ultrafilters (= realized
points)"? Is this expressible as a continuity/preservation
condition on the valuation itself, without reference to points?

**Why:** We are trading the algebraic formulation of CE (where the
sheaf approach stalled — emptiness invisible at the finitary level)
for a topological one. Stone duality converts:
- Boolean algebra B → compact Hausdorff space St(B)
- Finitely additive charge ℓ → regular Borel measure μ̂
- CE: E_n ↓ ∅ ⟹ ℓ(E_n) → 0  ↔  μ̂(pure(Ω)) = 1

The algebraic version is invisible finitely. The topological version
is a well-posed support condition. The locale version would express
CE as a frame-internal property of the valuation — structural (from
B via Stone duality) without being first-order (escaping Łoś).

If this exists, it's the non-circular characterization of coherence.

**Contact with programme:** CE characterization, the stalled sheaf
seed, the tetralemma (nailing leg 2), the definition of coherence.

### 3. Rédei & Summers — quantum probability structure

**Question while reading:** What do they identify as the
obstruction to extending states across non-Boolean joins?

**Why:** They work at the Boolean/non-Boolean boundary, which
is Paper II's territory. Their work on the structure of quantum
probability might identify the exact algebraic condition where
VDR fails — more precisely than "non-distributive + dim ≥ 3."

**Contact with programme:** Paper II (EA/PR/VDR), OML extension
problem.

### 4. Döring & Isham — "What is a Thing?" / topos quantum mechanics

**Question while reading:** Does daseinisation give a concrete
example of descent from Stone space to realization?

**Why:** Their topos approach makes contextual states into global
sections of a presheaf. This is adjacent to both the CE-as-sheaf
seed AND the OML extension problem. Daseinisation (approximating
quantum propositions by classical ones) is structurally similar
to "descending from St(C) to Ω."

**Contact with programme:** CE-as-sheaf, OML extension, Paper II.

### 5. Fremlin Vol 3 — measure algebras

**Question while reading:** Is there a known algebraic condition
on a Boolean algebra that forces every finitely additive charge
to be σ-additive?

**Why:** Measure algebras (Boolean algebras with strictly positive
countably additive measures) are exactly the algebras where CE
holds automatically. Fremlin's characterization of when a Boolean
algebra admits such a measure might be CE in algebraic language.

**Contact with programme:** Paper I, CE irreducibility, the
"exact boundary" question.

## Papers (arXiv / online — read before library books)

### 6. Howson — "De Finetti, Countable Additivity, Consistency and Coherence" (2008)

**Question while reading:** Does de Finetti's refusal of σ-additivity
as a coherence constraint map exactly onto our consistency/coherence
gap? Does Howson formalize it or just philosophize?

**Why:** Uses exactly our terminology for exactly our distinction.
De Finetti: coherence = finite additivity (Dutch book), σ-additivity
is beyond. Howson clarifies why this position is internally consistent.

**Contact with programme:** The punnet square, Paper I's CE, the
question of whether "coherence" has a definition.

### 7. Frot — "Gödel's Completeness and Deligne's Theorem" (2013, arXiv:1309.0389)

**Question while reading:** Is Deligne's theorem literally the
compactness theorem for toposes? If so, is CE's failure exactly
"the classifying topos lacks enough points"?

**Why:** This is the bridge between the model-theoretic reading
(Hodges) and the topos-theoretic reading (Caramello). Makes the
connection Gödel completeness = Deligne completeness explicit.

**Contact with programme:** CE-as-sheaf seed, the compactness
boundary, the "coherent theory" technical term.

### 8. Espíndola — "Infinitary Generalizations of Deligne's Completeness Theorem" (2017, arXiv:1709.01967)

**Question while reading:** Can the hierarchy of failure modes
(first-order → L_{ω₁ω} → beyond) be indexed by properties of
κ-coherent toposes?

**Why:** If CE is expressible in L_{ω₁ω} and Espíndola generalizes
Deligne to that level, then CE might correspond to a specific
topos-theoretic property. That would be a definition of coherence.

**Contact with programme:** Open question #6 (logical hierarchy of
failure modes), the punnet square's vertical axis.

### 12. Epperson & Zafiris — "Foundations of Relational Realism" (2013)

**READ (2026-05-17). Verdict: does not address CE.**

Read Chapters 6, 8, 9, 10 of the book and Zafiris (2006) J. Math.
Phys. 47, 092103 (the paper that puts measures on the site). The
Grothendieck topology J (epimorphic families) does not grade covers
by cardinality — finite, countable, and uncountable covers satisfy J
uniformly. The finite/countable boundary where CE lives is invisible.
States are finitely additive throughout; σ-completeness is an axiom,
not a sheaf condition. No cohomology is computed; the paper proves a
*reconstruction* theorem (counit is iso), not an obstruction theorem.
The H¹ unification with Abramsky-Brandenburger does not appear.

**Original question:** Does Zafiris's Boolean localization give a
sheaf-theoretic formulation of when local states glue to a global
σ-additive state? **Answer: No.**

## Papers to obtain (OML σ-additivity — populates bottom-right cell)

### 9. Pták — "Exotic logics" (1987, Colloquium Mathematicae 54(1), 1–7)

**Question while reading:** What exactly is the construction? Is the
obstruction purely from the center, or is there a genuinely non-Boolean
mechanism?

**Why:** This populates the bottom-right cell of the square. Constructs
σ-orthocomplete OMPs with finitely additive states but no σ-additive
states. The primary reference for "Gleason is the exception."

**Contact with programme:** Square A directly. The OML extension problem.

### 10. Navara — "Regularity and σ-additivity of states" (1992, Proc. AMS 115(2), 427–429)

**Question while reading:** Under what conditions does regularity force
σ-additivity? Is this the "admissibility condition" for the right column?

### 11. Navara & Rüttimann — "A characterization of σ-state spaces" (1991, Expo. Math. 9, 275–284)

**Question while reading:** How does the σ-state space sit inside the
full state space? What's the geometric/convex relationship?

### 13. Biesel — "Sheaves of Probability" (2024, arXiv:2401.01968)

**READ (2026-05-17). Verdict: confirms dictionary translation.**

Proves measures form a sheaf for finite covers (Thm 8), probability
measures likewise (Thm 11). Countable covers explicitly excluded
(Remark 7: uniform measures on {1,...,n} fail to glue to N). Section 5
states explicitly that results hold for merely finitely additive
charges. For countable covers, σ-finiteness is needed — standard
measure theory, no hidden structure.

**Original question:** Is the step from finite to countable covers
exactly the CE boundary? **Answer: Yes, but tautologically.** Finitely
additive = sheaf for finite covers; σ-additive = sheaf for countable
covers. Restatement, not characterization.

**Useful residue:** Thms 8 and 11 are clean citations for Paper I's CE
discussion. Ref [2] (Ross 2012, "All roads lead to violations of
countable additivity," *Phil. Studies*) relevant for Howson/de Finetti
direction.

## How to use this note

When reading, annotate here:
- What theorem/definition surprised you
- What connected to the programme
- What contradicted the knowledge map
- What suggested a concrete Phase 1 seed

When a reading direction produces a concrete claim worth auditing,
extract it to `notes/unsorted/` and run Phase 2.
