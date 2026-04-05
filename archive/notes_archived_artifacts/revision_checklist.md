# Revision Checklist: Observational Foundations of Probability

*Generated from assumption audit + author review, 2026-03-17*

> **EXECUTED — 2026-03-22.** All items in this checklist are confirmed present in
> `observational_foundations_body.tex`. Key additions verified: governing-principle sentence
> (§1), `[Primitive structure]` remark (§3), `[Status of realizability]` remark (§3),
> realization space as derived object (§3), `[Assumptions versus derived structure]` (§6),
> σ-additivity propagated remark (§6), Ω not a hidden state space (§7). Abstract no longer
> uses "completion of observable compatibility" framing. No further action required.

**Scope:** Surgical fixes to the current manuscript — no proof rewrites, no formalism changes.
**Goal:** Align rhetoric with what the theorem actually establishes. Not a next-paper extension.

---

## Governing principle

The paper should present itself as:

> *A derivation of global probability from local observable probabilistic structure plus compatibility and interface assumptions* — not a derivation of probability from pure observation alone.

The key sentence to add (candidate location: end of §1 Introduction, or as a standalone remark after the main theorem):

> "The present paper does not derive local measurable structure or local countable additivity from observation alone. Rather, it shows that once queries are equipped with measurable outcome spaces and compatible countably additive observable laws, the remaining global probabilistic structure is canonically forced under explicit structural assumptions on the query system."

---

## Section-by-section checklist

---

### Abstract

- [ ] **Soften the main claim.** Replace:
  > "In this sense probability appears not as a primitive structure but as the completion of observable compatibility"

  with something like:
  > "Under explicit structural assumptions on the query system — developed in full below — global probability appears as the canonical extension of locally compatible observable laws."

- [ ] **Add a hypothesis flag.** After the statement of the main result, add a parenthetical or subordinate clause acknowledging that the result requires measurable outcome spaces, countably additive laws, and the structural conditions (directedness, realizability).

---

### §1. Introduction and motivation

- [ ] **Add hypothesis inventory early.** After the "Answer" paragraph (currently: "We show that compatibility of observable laws is precisely the condition required"), add a brief list:
  > "More precisely, the result requires: (i) measurable structure on each query outcome space (taken as primitive in this paper); (ii) compatible countably additive probability laws on each outcome space; (iii) directedness conditions on the query system; (iv) realizability of the projective limit."

- [ ] **Add the governing-principle sentence** (see above) at the end of the introduction, before "Structure of the paper."

- [ ] **Fix the intro-level theorem statement.** The theorem box in §1 currently says only "Let $(\mathcal{Q}, \preceq)$ be a query system equipped with a compatible family of observable laws." This looks unconditional. Add a parenthetical: "(under the structural hypotheses of §3 and §6)" or expand the hypotheses inline.

---

### §2. Classical uniqueness and extension

- [ ] No changes required. This section is descriptive and correctly scoped.

---

### §3. Observational generators

- [ ] **Definition 1 (Query): declare the primitive explicitly.**
  After the current definition, add a remark:

  > *Remark (Primitive structure).* In the present paper, the measurable structure $\mathcal{B}(O_Q)$ on each outcome space is taken as a primitive input. It represents the class of events distinguishable at resolution $Q$. A more foundational treatment would derive this $\sigma$-algebra from a designated class $\mathcal{E}_Q$ of admissible observable distinctions via $\mathcal{B}(O_Q) = \sigma(\mathcal{E}_Q)$; we regard this as a direction for future work.

- [ ] **Directedness definitions: add operational interpretations.**
  After each of the three directedness definitions, add a one-sentence interpretation:
  - Lower-directedness: *"This is the assumption that any two observational resolutions admit a joint coarser representation."*
  - Upper-directedness: *"This is the assumption that any two observational resolutions can be jointly refined by a third — an assumption about the richness of the observational interface."*
  - Sequential common refinements: *"This is the assumption that the observational interface is closed under countable joint refinement: however many query resolutions are specified, a single finer resolution exists that subsumes all of them. This is a substantive condition on the interface structure, not merely a technical regularity hypothesis."*

- [ ] **Realizability definition: elevate its status.**
  The current remark says realizability "is satisfied whenever the projective limit is non-degenerate." This is circular. Replace the current remark with:

  > *Remark (Status of realizability).* Realizability is a substantive assumption. It asserts that the projective limit $\Omega$ is non-degenerate in a strong pointwise sense: every locally consistent outcome extends to a globally coherent realization. This is used in an essential way in the premeasure well-definedness argument and in the $\sigma$-subadditivity step of the extension theorem — it is not a side condition. Without it, both steps fail.
  >
  > A natural measure-theoretic weakening — likely sufficient for the proof — is *almost-sure realizability*: for each $Q$ and $\nu_Q$-almost every $o \in O_Q$, there exists $\omega \in \Omega$ with $\mathrm{eval}_Q(\omega) = o$. We retain the stronger pointwise form here for clarity. A sufficient condition for full realizability is given in Corollary~6.1: when each $O_Q$ is Polish, refinement maps are continuous, and the index set is countable, the projective limit is Polish and realizability holds automatically.

- [ ] **Realization space: add a note on nondegeneracy.**
  After the definition of $\Omega = \varprojlim O_Q$, add:

  > *Note.* The realization space $\Omega$ is a derived object: it is determined entirely by the query system and carries no structure beyond what the refinement maps force. It is not assumed as a latent state space. However, $\Omega$ can be empty or degenerate without additional hypotheses on the query system — realizability (Definition~6) is precisely the condition asserting non-degeneracy.

---

### §4. Observational determination

- [ ] No changes required. The theorem and proof are correctly scoped. The remark already notes "no compactness or topological assumptions enter."

---

### §5. Finite observational content

- [ ] **Theorem 5.1 hypothesis list: add a note on countable additivity.**
  After the theorem statement, add:

  > *Remark.* Hypothesis (3) requires each $\nu_Q$ to be a countably additive probability measure. This is assumed, not derived: the countable additivity present in the global extension theorem (§6) is propagated from this local assumption, not constructed from below.

---

### §6. Observational extension theorem

- [ ] **Add the assumption-vs-derivation remark after the main theorem.**
  After the proof, add the following remark (this is the most important single addition):

  > *Remark (Assumptions versus derived structure).* The theorem assumes: (i) measurable structure on each outcome space; (ii) countable additivity of each observable law $\nu_Q$; (iii) lower-directedness, sequential upper-directedness, and realizability of the query system. It derives: a canonical $\sigma$-additive probability measure on $(\Omega, \sigma(\mathcal{Q}))$ whose evaluation marginals recover all observable laws. Countable additivity of $P$ is not constructed from first principles but propagated from the countable additivity of the $\nu_{Q_*}$ via the compression argument. Assumptions (i) and (ii) are inputs from classical measure theory; a more foundational treatment would aim to derive them from the structure of observable distinctions. Assumptions (iii) are substantive conditions on the query system: they express joint coarsenability, closure under countable joint refinement, and non-degeneracy of the realization space.

- [ ] **Remark on structure of the proof (already present):** Good as-is. No change needed.

- [ ] **Corollary 6.1 (topological setting):** Add one sentence flagging its role:
  > "In particular, Corollary~6.1 provides the main route to verifying realizability: under Polish outcome spaces and a countable cofinal chain, all four hypotheses of Theorem~6.1 are automatically satisfied."

---

### §7. Representation and experiment-theoretic interpretation

- [ ] **Add a sentence clarifying the status of \Omega.**
  In the paragraph beginning "Different measurable realizations may support the same observable laws," add:
  > "In particular, $\Omega$ is not a hidden state space postulated independently of the observable interface: it is the canonical consistency object determined by the query system, carrying exactly the structure forced by the refinement maps and no more."

- [ ] No other changes. The Le Cam correspondence table and discussion are correctly framed.

---

### §8. Approximate compatibility

- [ ] No changes required for the current revision scope.

---

### §9. Outlook and connections

- [ ] No changes required for the current revision scope.

---

## Summary of changes by type

| Type | Count | Location |
|---|---|---|
| Soften/correct rhetorical overclaim | 2 | Abstract, §1 theorem box |
| Declare primitive explicitly | 1 | §3 Definition 1 |
| Operational interpretation of directedness | 3 | §3 after each directedness def |
| Elevate realizability status | 1 | §3 Realizability remark (full rewrite) |
| Nondegeneracy note on $\Omega$ | 1 | §3 after realization space def |
| Hypothesis inventory | 1 | §1 Introduction |
| Governing-principle sentence | 1 | §1 end |
| Note on $\sigma$-additivity propagation | 1 | §5 after Theorem 5.1 |
| Assumption-vs-derivation remark | 1 | §6 after main theorem (most important) |
| Corollary 6.1 framing | 1 | §6 |
| Status of $\Omega$ as derived object | 1 | §7 |

**Total: ~13 targeted additions/revisions. No proof changes. No formalism changes.**

---

## What this revision does NOT do (next-paper scope)

- Does not redefine queries via event classes $(O_Q, \mathcal{E}_Q)$
- Does not weaken realizability to almost-sure realizability (proof change required)
- Does not relax coherence to a.e. coherence
- Does not derive $\sigma$-additivity of $\nu_Q$ from any more primitive structure
- Does not address the deeper question of what makes an event "admissible"

These are flagged as future work directions in the new remarks above.
