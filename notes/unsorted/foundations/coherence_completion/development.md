# Development Log: Coherence and Completion

**PARKED 2026-05-18.** See `paper_sketch.md` header for reason.

Working log for the philosophy-math iteration on coherence, consistency,
failure modes, and admissibility.  Entries are chronological.  Material
graduates to the stable files when it stops changing.

---

## Core motivation (recorded 2026-05-17)

The programme's origin is NOT "study measure extension for its own sake."
It is:

> Can you build probability from the functional/relational structure of
> observations alone, without presupposing an underlying space?

This was motivated by time series / dynamical reconstruction: you observe
a sequence of values and want a probabilistic model, but the standard
approach assumes an underlying state space (manifold, attractor). The
question: what if you CAN'T assume a space — either fundamentally
(quantum, discrete) or due to insufficient a priori knowledge?

Paper I answers: start with a Boolean algebra of distinctions (relational:
"these outcomes are distinguishable") and charges (functional: valuations
on the algebra). The space (Ω, or St(B)) is DERIVED, not assumed. CE
determines whether the derived space carries genuine probability.

The 2×2 square connects this to the non-Boolean case:
- Left column (Boolean): observations compatible, a single space CAN be
  reconstructed, CE determines if it carries probability
- Right column (non-Boolean): observations INCOMPATIBLE, no single space
  embeds all contexts, but probability might still arise (Gleason) — you
  just can't get definite values on the derived space (KS blocks VDR)

The original motivation is MORE NATURAL on the right side, where "no
underlying space" is a mathematical fact (no Boolean embedding exists)
rather than a philosophical choice (choosing not to assume one).

The question for the reading (Kalmbach, Pták-Pulmannová):

> In the non-Boolean setting, where no underlying space exists, how does
> probability arise from the relational structure (orthocomplementation,
> partial ordering, orthogonality) of the observations alone?

This is the original question, asked in the setting where it's forced.

---

## 2026-05-03 — Initial state and overlap diagnosis

The cluster currently has three files with significant overlap:

- `conceptual_schema.md` — the seed note (2026-04-13).  Contains the
  three-component schema, the conceptual grammar (consistency / coherence /
  admissibility), the forcing vs permitting distinction, the failure-mode
  taxonomy, and the CE worked example.  Also contains objecthood-as-open-horizon
  and valuation-of-refinement — both philosophical in register.

- `paper_sketch.md` — the exposition plan (2026-05-02).  Walks through most of
  the same material: the schema, the grammar, the CE witness, objecthood, the
  taxonomy table, and the staging options (Version A / Version B).

- `mathematical_language.md` — the formal file (2026-05-02).  1370 lines.
  Contains the abstract schema, the probability instance as seed example
  throughout, and the institution/completion-descent generalization.  Now has a
  three-zone table of contents.

The overlap arose because `conceptual_schema.md` was the original working
surface where both philosophical and mathematical ideas were developed together.
When `paper_sketch.md` was created for the exposition plan, it needed the same
material as context, so it re-walked it.

### What needs to happen

1. Thin `conceptual_schema.md` to its proper role: the vocabulary and taxonomy
   that define the conceptual space.  Remove narrative, staging, and worked
   examples that now live better in `paper_sketch.md` or
   `mathematical_language.md`.

2. Make `paper_sketch.md` the sole home for: exposition plan, staging options,
   abstract draft, section outline, and the table comparing all five layers.

3. Keep `mathematical_language.md` as-is (with the new zone structure).

4. Future iteration on the concepts goes here in `development.md`, not into the
   stable files until it settles.

### Pending conceptual questions

These are the open edges where philosophy and math are still entangled:

- **Compactness as distinguishing consistency**: is contradiction the unique
  compact failure mode?  This is philosophically motivated (consistency as
  species of coherence) but needs a mathematical answer.  Currently stated as
  open question 3 in `conceptual_schema.md` and as Target 2 in
  `paper_sketch.md`.

- **Forcing vs permitting**: the distinction is clear for CE (CE forces, not
  merely permits).  Is this always the case for admissibility conditions?  Or
  can there be admissibility that permits without forcing?  This affects whether
  the schema has two levels (coherence / admissibility) or three (coherence /
  permitting / forcing).

- **Horizon plurality and valuation**: the zeta example suggests multiple
  horizons for one object.  The mathematical language file has a "Horizon
  Plurality" section but it is still philosophical.  The question is whether
  horizon comparison is a formal object (functors between completion-descent
  data?) or just a naming convention.

- **Fibre mixing as second worked example**: blocked on the derivability
  question.  If fibre mixing turns out to be irreducible (like CE), then the
  two-example Version B becomes natural.  If derivable, it's still an example
  but a less interesting one for the coherence paper.

### First formal steps (from original conceptual_schema.md seed)

1. Write a provisional formal definition of a "coherence notion" within the
   three-part schema (local data / global realization / failure mode).
2. Define what it means for such a notion to be *compact*: every instance of
   the failure mode is detectable by a finite sub-instance.
3. Verify that consistency/contradiction is the canonical compact case under
   this definition.
4. Test whether CE or any non-extension coherence notion can also be compact
   in a nontrivial way — or prove it cannot.

Step 4 is the priority theorem target.  A positive answer (another compact
coherence notion exists) would force a richer taxonomy; a negative answer
(compactness singles out contradiction-type failure) would give a formal sense
in which consistency is the unique compact coherence notion.

---

## 2026-05-15 — The consistency/coherence punnet square

Consistency has two faces: syntactic (no proof of ⊥) and semantic (exists
a model), connected by the completeness theorem.  Does coherence have two
faces?  Unclear — coherence might be inherently semantic (the failure mode
is non-compact, so no finitary proof system captures it).

More productive than asking "what is the syntactic face of coherence" may
be asking what fills the 2×2 of consistent/inconsistent × coherent/incoherent:

| | Consistent | Inconsistent |
|---|---|---|
| Coherent | ??? | ??? |
| Incoherent | ??? | ??? |

Working candidate population:

- **Consistent + Coherent:** Classical probability. Local data embeds
  in one Boolean algebra, CE holds, σ-additive measure exists.
  (Paper I, the good case.)

- **Consistent + Incoherent:** The ultrafilter charge. No contradiction
  anywhere — every first-order test passes — but σ-additivity fails.
  CE fails. The Łoś cell. This is where Paper I's obstruction lives.

- **Inconsistent + Coherent:** Quantum probability? Incompatible
  observables "contradict" (can't be jointly measured / no single
  Boolean embedding), but Gleason gives a global σ-additive state
  anyway. The non-distributive structure forces local incompatibility
  while the quantum state provides global coherence.

- **Inconsistent + Incoherent:** Kochen-Specker. Non-Boolean (local
  incompatibility) AND no dispersion-free global state. Both axes fail.

If this is right, the axes are:
- Consistency axis = distributivity / Boolean embeddability
- Coherence axis = state extension / σ-additivity / CE-type condition

And the programme's papers map onto the square:
- Paper I: top row (Boolean), distinguishing coherent from incoherent
- Paper II: left column (state exists), distinguishing consistent from
  inconsistent (i.e., Boolean from non-Boolean)
- The diagonal from top-left to bottom-right is the full filtration:
  VDR → PR → EA → nothing

### Caution

This is an intuition pump, not a theorem. The identification of
"inconsistency" with "non-Boolean / contextual" is suggestive but
not rigorous. Classically, inconsistency means a contradiction is
derivable; here it means something weaker — non-embeddability into a
single Boolean context. Whether this is really "inconsistency" or
merely "incompatibility" is exactly the question.

The reading directions (Caramello, Vickers, Kalmbach, Hodges) should
be read with this square in mind:
- Does the author's formalism give a definition of coherence?
- Does the author distinguish consistency from coherence?
- Where would the author place CE in their framework?
- Does the non-Boolean case (quantum) fit naturally, or require
  a separate treatment?

### Status

Intuition pump. Do not promote to stable files until a definition
crystallizes. Hold lightly while reading.

---

## 2026-05-15 — Literature search: who has formalized the gap?

Deep research audit on whether the consistency/coherence distinction has
been formalized. Result: the territory is real, recognized implicitly in
4+ traditions, but never unified under one name.

### Direct hit

- **Howson (2008)** "De Finetti, Countable Additivity, Consistency and
  Coherence" — BJPS 59(1):1-23. Uses exactly our terminology for exactly
  our distinction. De Finetti drew the line: coherence = finite additivity
  (Dutch book), σ-additivity is beyond — an additional structural
  requirement not groundable in the same way. READ THIS FIRST.

### The topos-theoretic encoding (unnamed but structural)

- "Coherent theory" (technical term in categorical logic) = finitary
  geometric theory whose classifying topos has enough points. This IS
  the compactness boundary.
- σ-additivity requires infinitary axioms → theory is non-coherent →
  classifying topos may lack enough points.
- **Frot (2013)** arXiv:1309.0389 — Deligne's completeness theorem =
  Gödel's completeness theorem for toposes. The bridge between
  model-theoretic and topos-theoretic reading directions.
- **Espíndola (2017)** arXiv:1709.01967 — generalizes Deligne to
  infinitary logics (κ-coherent toposes for weakly compact κ).
  Directly relevant to whether the gap can be indexed by logical
  complexity.

### The quantum angle

- **Abramsky-Brandenburger (2011)** — contextuality as obstruction to
  global sections of a presheaf. Their hierarchy:
  - Local sections exist and glue → non-contextual (consistent+coherent)
  - Local sections exist but don't glue → contextual (consistent+incoherent)
  - No local sections → logical contextuality / KS (inconsistent+incoherent)
  - Missing: "inconsistent+coherent" cell (Gleason). They don't have it.

### The imprecise probability angle

- **Conglomerability** (Walley, Zaffalon-Miranda 2017) is "σ-coherence"
  in all but name. Coherence = finite additivity (Dutch book). Full
  conglomerability = additional condition forcing countable additivity.
  Same gap, different dress.

### The sidestep strategy

- **Ben Yaacov — continuous model theory** makes probability algebras
  first-order axiomatizable by changing the logic (metric semantics).
  Compactness is restored. This dissolves rather than names the gap.
  A third strategy beyond (a) naming the obstruction and (b) adding CE.

### What this means

The opportunity: nobody has unified the de Finetti/Howson philosophical
distinction, the topos-theoretic "coherent vs non-coherent" classification,
the Abramsky contextuality obstruction, and the conglomerability condition
into a single framework. The schema (L,T,K,P,A) aims at that unification.

The risk: the unification might be terminological packaging rather than
a theorem. The test: does the unified framework prove something new about
one instance that wasn't visible from within its home tradition alone?

### Key references to obtain

1. Howson (2008) — BJPS, likely online. Read immediately.
2. Frot (2013) — arXiv:1309.0389. Deligne = Gödel.
3. Espíndola (2017) — arXiv:1709.01967. Infinitary Deligne.
4. These supplement, not replace, the library book directions
   (Caramello, Vickers, Hodges, Kalmbach, Pták-Pulmannová).

---

## 2026-05-16 — The topological trade and the question for Vickers

### The tetralemma on the Boolean side (precise formulation)

Target: CE holds for a compatible directed system of charges.

| Leg | Status | Mechanism |
|-----|--------|-----------|
| 1. CE is derivable | Refuted | Łoś (mathematical) |
| 2. CE is false | NOT refuted | Only operational/semantic argument |
| 3. Both | Refuted | Bivalence |
| 4. Neither (underdetermined) | Standing | Stone construction exhibits it |

Leg 2 is the gap. CE-failure means mass persists on events that shrink
to empty. The observer's structure says "nothing is here" while the
valuation says "something weighing c is here." This LOOKS contradictory
but isn't formally ⊥ because the emptiness is at the σ-level, invisible
to the finitary charge.

### The algebraic dead end (recap)

The sheaf approach on the directed system failed because:
- Naive topology J (witnessing-by-emptiness): too coarse, ∩E_n = ∅ is
  invisible at finite levels
- Revised topology J' (witnessing-by-charge-decay): circular, restates CE

The fundamental bind: the obstruction (mass on σ-empty set) is invisible
to any finitary/structural condition. This IS the Łoś theorem.

### The topological trade

Stone duality converts:
- B (Boolean algebra) ↔ St(B) (compact Hausdorff space)
- ℓ (finitely additive charge) ↔ μ̂ (regular Borel measure)
- CE: E_n ↓ ∅ ⟹ ℓ(E_n) → 0  ↔  μ̂(pure(Ω)) = 1

The trade: replace "does the charge see σ-algebraic emptiness?"
(invisible finitely) with "does the measure live on the realized
points?" (a well-posed topological support condition).

Key point: pure(Ω) is dense in St(B) but not closed/open/G_δ in
general. So "support on pure(Ω)" is NOT the same as "support ⊆
closure of pure(Ω)" (which is vacuous since pure(Ω) is dense).

### The question for Vickers / locale theory

In the locale O(St(B)):

> Is there a frame-theoretic characterization of "a valuation is
> supported on the sublocale of principal ultrafilters" that is
> expressible purely in terms of the frame structure, without
> reference to points?

If yes → CE is a frame-internal property of the valuation. Since the
frame is determined by B (Stone duality), this would be a STRUCTURAL
characterization of CE — not first-order (escaping Łoś) but structural
(determined by the algebra). The sheaf/site approach failed because it
tried to stay algebraic; the locale approach moves to topology, which
is where the distinction lives.

If no → CE really is irreducibly about *which points* carry mass, and
no frame-internal characterization exists. Then coherence has no
structural definition and must remain a bare commitment.

### Why this might work where the sheaf approach failed

The sheaf approach stayed on the algebraic side of Stone duality and
tried to define a topology on the index category ι. But ι is too
coarse — the events at each level don't see their own σ-completion.

The locale approach works on the DUAL side (St(B)) where:
- The full topological structure is present
- pure(Ω) vs non-principal is a concrete geometric distinction
- The frame O(St(B)) encodes all the topological information
- Valuations on frames are the locale-theoretic replacement for measures

The crucial question is whether "supported on pure(Ω)" can be stated
without naming the points of pure(Ω) — i.e., frame-internally.

### Stone's maxim

"One must always topologize." The algebraic approach to CE hit a wall
because the relevant distinction (σ-emptiness) isn't algebraically
visible. Stone duality moves it to a topological setting where it IS
visible. The locale approach then asks: is it visible frame-internally
(without points), or only via the point-set topology?

---

## 2026-05-16 — The locale research: layered answer

Deep research on whether CE can be expressed frame-internally on
O(St(B)) without reference to points. The answer has three layers.

### Layer 1: Shallow positive (it CAN be stated frame-internally)

The clopens of St(B) = the complemented elements of the frame O(St(B)).
"Complemented" is frame-definable (∃b: a∧b=⊥, a∨b=⊤). So B is
recovered from O(St(B)) purely frame-internally.

CE = "μ restricted to complemented elements is σ-additive" =
"for every decreasing sequence (c_n) of complemented elements with
⋀_n c_n = ⊥, μ(c_n) → 0."

This uses only: frame structure + valuation + "complemented element" +
countable meets. No points mentioned. Frame-internal.

But it SINGLES OUT the clopens. It's CE restated in frame language,
not CE derived from frame structure.

### Layer 2: Deep negative (invisible on general opens)

On a compact Hausdorff space, EVERY finite Borel measure (CE or not)
gives a perfectly Scott-continuous (τ-additive) valuation on O(St(B)).
Compactness forces this. The CE/non-CE distinction is invisible to:
- Scott continuity
- Regularity / τ-additivity  
- Any monotonicity or continuity property on the full frame

Both σ-additive and purely finitely additive charges produce valuations
that are INDISTINGUISHABLE at the level of "how μ behaves on directed
joins of opens." The distinction lives ONLY on the clopens.

This is the deep negative: you cannot detect CE from the valuation's
behavior on general opens. The frame is "too rich" — compactness has
already forced good behavior everywhere.

### Layer 3: Open problem (Simpson's sublocale)

Simpson (2012) "Measure, Randomness and Sublocales" (APAL 163):
Every probability valuation on a fitted σ-locale has a smallest
σ-sublocale of full measure. This is frame-constructible.

Natural conjecture (UNPROVEN, not in the literature):

> CE holds ⟺ Simpson's smallest measure-1 σ-sublocale is SPATIAL
> (has enough points).

This would be genuinely frame-internal and non-trivial. But:
- St(B) itself is always spatial (sober compact Hausdorff)
- The smallest measure-1 sublocale might or might not be spatial
- Connecting spatiality of this sublocale to σ-additivity on clopens
  is non-trivial and unproven

### The Loomis-Sikorski angle (intermediate)

For σ-COMPLETE B: CE ⟺ every meager Baire set gets measure zero.

"Meager" is close to frame-internal: nowhere dense = below the double-
negation nucleus (Isbell's density theorem). A meager set = countable
union of nowhere dense closed sets.

So: CE ⟺ "μ vanishes on countable joins of closed sublocales below
the double-negation nucleus." This is frame-internal in spirit but
requires σ-completeness of B.

### Assessment

| Version | Frame-internal? | Satisfying? |
|---------|----------------|-------------|
| Layer 1 (σ-additive on clopens) | Yes | No — restates CE |
| Layer 2 (detect from general opens) | N/A — impossible | N/A |
| Layer 3 (Simpson's spatial sublocale) | Yes (if proved) | Yes — but OPEN |
| Loomis-Sikorski (meager null) | Partially | Requires σ-completeness |

### What this means for the programme

The DEEP frame-internal characterization is an open problem. The pieces
exist (Simpson 2012, Ball 2023 on spatial/pointless decomposition,
Loomis-Sikorski) but nobody has assembled them.

Options:
1. Accept Layer 1 as the answer: CE = σ-additivity on complemented
   elements. Frame-internal but not "derived from frame structure."
   This is honest — CE is an additional condition on the clopens,
   visible in the frame but not forced by it.

2. Pursue the Simpson conjecture as a theorem target: prove or
   disprove that CE ⟺ spatial smallest-measure-1-sublocale. This
   would be a genuine contribution to locale-theoretic measure theory.

3. Use the Loomis-Sikorski angle for σ-complete algebras only: CE =
   meager-null. Frame-internal, but limited scope.

### Key references to obtain

- Simpson (2012) "Measure, Randomness and Sublocales" APAL 163(11)
- Ball (2023) "Pointless Parts of Completely Regular Locales" arXiv:2305.00096
- Lehner (2025) "Measure Theory via Locales" arXiv:2510.08826
- Picado & Pultr (2012) "Frames and Locales" (textbook)

### Connection to the tetralemma

Layer 2 explains WHY leg 2 can't be nailed down purely frame-
theoretically: the valuation's behavior on opens doesn't distinguish
CE from non-CE. The distinction is "below" the level of open-set
behavior — it's about the clopens specifically.

This might mean: coherence (= CE) is not a continuity condition
at all. It's an ADDITIVITY condition on a specific sublattice. The
topological trade didn't dissolve the problem — it clarified WHERE
the condition lives (on clopens, inside the frame, detectable but
not derivable from the frame's own continuity structure).

---

## 2026-05-16 — Simpson conjecture: DEAD

Audit completed. The conjecture "CE ⟺ Simpson's smallest measure-1
σ-sublocale is spatial" collapses:

- ⟸ FALSE: δ_U (Dirac at free ultrafilter on P(ω)) is purely finitely
  additive but gives a one-point (hence spatial) measure-1 sublocale.
- ⟹ TRIVIALLY TRUE for ALL measures: compact Hausdorff + classical
  logic + Radon = support is always a spatial closed subspace.

Root cause: Simpson's non-spatiality phenomenon is constructive
(algorithmic randomness). Classically it vanishes. We work classically
(Stone duality, AC, ultrafilters). The machinery doesn't bite.

### What this rules out

The "deep" frame-internal characterization of CE (Layer 3) does not
exist via Simpson's route. The condition μ̂(pure(Ω)) = 1 is
inherently point-set-topological. Locale theory abstracts away from
points, which is exactly what makes it unable to see CE.

### Where this leaves us

We are back to Layer 1 as the best available answer:

> CE = σ-additivity on the complemented elements of the frame.

This IS frame-internal (complemented elements are frame-definable).
It IS detectable from frame + valuation. But it SINGLES OUT the
clopens rather than deriving CE from general frame structure.

The honest conclusion may be: **CE is irreducibly about the Boolean
sublattice (clopens).** It cannot be expressed as a property of the
valuation on the full frame because both CE and non-CE valuations
are indistinguishable at the open-set level (Layer 2). The
topological trade CLARIFIED this (the distinction lives on clopens)
but did not DISSOLVE it (no deeper characterization exists).

### Implications for the definition of coherence

If CE cannot be expressed as a frame-continuity condition or a
locale-theoretic support condition, then "coherence" may not be
a topological concept at all. It may be irreducibly algebraic:
a condition on a specific sublattice (the clopens = the Boolean
algebra = the observable distinctions) that the ambient topology
sees but cannot generate.

This is consistent with the Łoś picture: CE is not first-order,
but it IS about the Boolean algebra specifically. The topology
(Stone space) is a tool for REPRESENTING the condition but not
for GENERATING it. The condition lives at the algebraic level.

### Does this kill the Vickers direction?

Partially. The specific hope ("CE is frame-continuity") is dead.
But Vickers might still be useful for:
- Understanding what locale theory CAN see about charges
- The non-Boolean generalization (where the frame isn't generated
  by complemented elements alone)
- The constructive setting (where the distinction IS visible —
  but we work classically)

The Vickers reading is still worth doing but the SPECIFIC QUESTION
("is CE frame-internal beyond Layer 1?") has been answered: no,
classically.

---

## 2026-05-16 — Devil's advocate: serious objections

### Objection 1: Q3 is likely a category error

CE adds a hypothesis (to get σ-additivity). Gleason has NO hypothesis
— the lattice structure alone forces σ-additivity. A "unified condition
C" that's substantive for Boolean algebras and vacuous for L(H) isn't
a unification. It's CE with an escape clause.

The two cases may not be "the same phenomenon at different generality":
- CE: charge + condition → σ-additive extension
- Gleason: lattice geometry alone → every charge is already σ-additive

For Q3 to survive, I need to articulate WHY these should be instances
of the same thing beyond "both produce σ-additivity." If the connection
is only at the output level, Q3 dissolves.

Possible rescue: maybe the "condition" in the Gleason case is built
into the lattice itself (irreducibility + covering property + atomicity
= the lattice is so rigid it has no room for non-σ-additive charges).
Then "C" would be: "the lattice doesn't ADMIT pathological charges"
— which for Boolean algebras requires an external condition (CE) and
for L(H) is automatic. But this is still just restating "Gleason holds
for L(H)" — not explaining WHY.

### Objection 2: The square organizes, doesn't predict

Until it produces a theorem of the form "given lattice property X,
forcing holds iff Y," it's a filing system for known results. The
test: does the square PREDICT anything about an OML I haven't checked
yet? Currently: no.

### Objection 3: "Irreducibly algebraic" is premature

One failed locale approach (Simpson) doesn't prove non-expressibility.
The conclusion "CE can't be expressed frame-internally beyond Layer 1"
rests on thin evidence. A hostile referee would say: "tried one thing,
declared the problem closed."

Fair criticism. The conclusion should be weakened to: "the most natural
locale-theoretic characterization doesn't work classically; whether ANY
frame-internal characterization beyond Layer 1 exists remains open."

### Objection 4: The practical path is formalization, not OML theory

The Lean formalization is nearly done (1 sorry). ITP/CPP conferences
are clear venues. The OML direction requires years of expertise. The
lowest-risk publishable output is the formalization contribution, not
a new theorem in OML state theory.

### Assessment: serious but not fatal

Q3 needs a non-trivial answer to the category error before the OML
reading becomes a theorem hunt rather than education. The square needs
to predict, not just organize. The "irreducibly algebraic" conclusion
should be held as tentative.

### What survives

- The 2×2 square as INTUITION PUMP (honest label)
- The reading directions (Kalmbach, Pták-Pulmannová) for EDUCATION
  about what Gleason actually uses
- The question "why does L(H) force σ-additivity?" as EDUCATION
  (the answer is known — dimension ≥ 3 + lattice structure)
- The practical path: ship papers, close Lean sorrys, consider
  formalization venues (ITP/CPP)

### What should be demoted

- Q3 as a "theorem target" → demote to "question to hold while
  reading" until a non-vacuous mechanism-level connection is found
- The Simpson conjecture → dead (already marked)
- "Irreducibly algebraic" → weaken to "tentative conclusion pending
  further investigation"

---

## 2026-05-16 — Square A: bottom-right cell is populated

Literature search confirms: non-Boolean OMLs admitting finitely additive
states but no σ-additive states DO exist.

### Primary reference

- **Pták (1987)** "Exotic logics," Colloquium Mathematicae 54(1), 1–7.
  Constructs σ-orthocomplete OMPs with finitely additive states but no
  σ-additive states.

### The structural argument (center obstruction)

Take a σ-complete OML L whose center C(L) ≅ a Boolean algebra with no
σ-additive probability (e.g., P(ω)/fin). Any σ-additive state on L
restricts to a σ-additive state on C(L), which doesn't exist. But L
can admit finitely additive states (each Boolean block has them by Zorn).

This means the obstruction in the bottom-right cell can come from
the CENTER (the Boolean part!) — the non-Boolean structure is compatible
with finitely additive states but the center blocks σ-additive ones.

### Consequence for the square

All four cells are populated:

| | Boolean | Non-Boolean |
|---|---|---|
| σ-additive exists | Paper I (CE) | Gleason (L(H) special) |
| σ-additive fails | Ultrafilter charge | Pták 1987 |

### Gleason is the exception, not the rule

L(H) is special: its geometric/continuum structure forces σ-additivity.
General OMLs (pasting constructions, Greechie diagrams) do NOT have
this property. Gleason-type rigidity requires something like:
irreducibility + atomlessness + manifold structure of projective space.

### Question 3 sharpens

The admissibility condition for the top row:
- Left column: CE (support on principal ultrafilters)
- Right column: whatever structural property L(H) has that Pták's
  exotic logics lack

Identifying that property = identifying the "coherence condition" for
non-Boolean lattices. This is the open theorem target.

### Papers to obtain

1. Pták (1987) "Exotic logics" — Colloq. Math. 54(1), 1–7
2. Navara (1992) "Regularity and σ-additivity of states" — Proc. AMS 115(2), 427–429
3. Navara & Rüttimann (1991) "A characterization of σ-state spaces" — Expo. Math. 9, 275–284

### Note on the center obstruction

The center argument is striking: the bottom-right obstruction can be
EXACTLY the bottom-left obstruction (CE failure on the Boolean center),
just embedded in a non-Boolean wrapper. This suggests Question 3 might
have a clean answer: the admissibility condition for non-Boolean OMLs
IS CE applied to the center. If so, "coherence" (in our sense) is
always a Boolean/center phenomenon, even in non-Boolean structures.

But this needs checking: does Gleason's success for L(H) correspond to
C(L(H)) being trivial (= {0,1})? Yes — L(H) is a factor, its center
is {0, H}, which trivially admits a σ-additive state. So the center
obstruction is vacuous for L(H), and Gleason provides σ-additivity
from the lattice structure itself.

Tentative picture:
- Center non-trivial → CE on center is the obstruction (same as Boolean case)
- Center trivial (factor) → lattice geometry forces σ-additivity (Gleason)
- Center trivial but lattice too discrete → ??? (possible third case)
