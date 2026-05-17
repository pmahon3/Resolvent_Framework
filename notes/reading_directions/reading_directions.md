# Reading Directions

*Not a syllabus. A list of questions to bring to specific sources.*

## The persistent question

Across all phases of this programme:

> What must be added to observation to get structure?

- Phase 1: observation → dynamics (semigroup)
- Phase 2-3: observation → geometry (curvature, metric, action)
- Phase 4-6: observation → probability (CE), realization (descent),
  value-definiteness (distributivity)

The reading question is not "learn more X." It is:

> Where does someone identify the exact condition that forces a
> valuation to behave — and what structure does that condition live in?

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

**Question while reading:** Does Zafiris's Boolean localization
(sheaves of Boolean algebras over a quantum event algebra) give a
sheaf-theoretic formulation of when local states glue to a global
σ-additive state? Is the gluing obstruction related to CE?

**Why:** Zafiris works on representing OMLs as sheaves of Boolean
algebras over a base site. This is the "sheaves over contexts"
approach to the non-Boolean setting. If the failure of global
σ-additive states is a cohomological obstruction (à la Abramsky-
Brandenburger for contextuality), that would connect CE to a
topological invariant — exactly what the locale approach tried
but from a different (contextual/sheaf-over-site) angle.

**Contact with programme:** CE-as-sheaf seed (revived from a
different direction), Square A vertical axis, the non-Boolean
column, the "what forces σ-additivity?" question.

**Checked out from SFU.**

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

## How to use this note

When reading, annotate here:
- What theorem/definition surprised you
- What connected to the programme
- What contradicted the knowledge map
- What suggested a concrete Phase 1 seed

When a reading direction produces a concrete claim worth auditing,
extract it to `notes/unsorted/` and run Phase 2.
