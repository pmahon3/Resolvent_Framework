# Paper Sketch: Coherence, Completion, and Automatic Closure

*Seed note - 2026-05-02*

## Consolidation Status

This is the exposition-facing sketch for the coherence/completion direction.
It should not become the proof notebook.  For navigation across the active
future notes, see `notes/README.md`.

Working division:

- conceptual seed: `notes/future/foundations/coherence_completion/conceptual_schema.md`;
- formal language: `notes/future/foundations/coherence_completion/mathematical_language.md`;
- logic placement: `notes/literature/foundations/coherence_completion/logic_lit_review.md`;
- philosophical scaffold:
  `notes/literature/foundations/coherence_completion/philosophy_lit_review.md`;
- concrete Boolean/Stone frontier:
  `papers/paper_i/notes/ultralimit_investigation/strategy_d_dossier.md`.

## Source

This note extracts a paper-shaped suggestion from the May 2026 exchange on
observational resolution dimension, zeta, and object-as-horizon language.  The
suggestion is distinct from Paper III.  It points toward a separate
foundations/coherence paper downstream of the submission-ready companion
theorem note on countable additivity not being first-order axiomatizable:
`papers/paper_i/notes/countable_additivity_not_first_order.tex`.

Possible titles:

- *Coherence, Completion, and the Incoherence of Automatic Closure*
- *Objects as Open Horizons of Coherent Refinement*
- *Coherence Beyond Consistency*

## Core Thesis

The object should not be understood as a completed substrate behind its possible
observations, nor as a merely external target to which local data are later
attached.  The object is the horizon of coherent refinement: the structured
field within which distinctions can be made, related, extended, valued, and
tested for admissible completion.

This horizon is open, not complete.  Openness is not a temporary empirical
defect.  It is witnessed by non-compact failure modes: local or first-order
coherence may persist while the intended global realization fails.

In a freer register:

> the object is not what stands behind the horizon; the object is the horizon's
> stable way of opening.

Objecthood is not closure.  Objecthood is stable openness: the capacity to be
returned to coherently under refinement while still admitting further
distinctions, completions, obstructions, and failures of fit.  The object is not
a hidden kernel behind possible disclosures.  It is the structured possibility
of further disclosure.

This suggests a compact conceptual grammar:

> consistency = possible coexistence  
> coherence = structured continuation  
> admissibility = licensed completion

or:

> coherence is consistency under intended continuation.

Consistency says that the pieces can coexist.  Coherence asks whether they
continue together toward the kind of whole they are supposed to disclose.
Incoherence, in this sense, need not be contradiction.  It can be the failure of
locally compatible pieces to sustain the intended global form.

In slogan form:

> object = open horizon of coherent refinement  
> completion = attempted global realization  
> failure mode = way the horizon refuses automatic closure  
> admissibility = condition that closes the horizon relative to a target

The paired phrase to keep:

> open horizon / licensed closure

## Mathematical Witness

The probability case supplies the hard witness.

Each Dirac probability is $\sigma$-additive.  But an ultraproduct/ultralimit of
Dirac probabilities induces, on the diagonal copy of $\mathcal P(\mathbb N)$, a
purely finitely additive ultrafilter charge.  Thus every first-order/local test
may be passed while the intended global property, countable additivity, fails.

This is not contradiction.  It is failure of automatic closure.

Consequently:

> finite coherence does not force probability.

CE names the additional admissibility condition that closes this horizon
relative to $\sigma$-additive probability.

## Relation to Existing Notes

The submission-ready companion note should stay theorem-clean:

> language -> finitely additive probability structures -> Dirac structures ->
> ultraproduct -> ultrafilter charge -> not $\sigma$-additive.

The deeper philosophical/mathematical interpretation should not be inserted into
that note.  It belongs in the coherence/consistency direction and, eventually,
in this separate paper.  The countable-additivity note supplies the theorem
witness; the foundations paper explains the structural meaning of that witness.

Existing nearby notes:

- `notes/future/foundations/coherence_completion/conceptual_schema.md`: seed schema and
  primary home;
- `notes/future/foundations/ce_nonderivability/index.md`: related non-first-order direction;
- `notes/future/foundations/zeta/observational_question.md`: boundary probe for
  mathematical objects and horizon-internal valuation;
- `notes/future/finite_sample/observational_resolution/index.md`: valuation-of-refinement
  analogue;
- `notes/future/foundations/coherence_completion/mathematical_language.md`: first attempt
  at the notation and theorem-clean language extending the countable-additivity
  note;
- `notes/literature/foundations/coherence_completion/philosophy_lit_review.md`:
  philosophical scaffolding to help generate the mathematical concepts, to be
  discarded or compressed once the expository path is clear.

The most important older note is
`notes/future/foundations/coherence_completion/conceptual_schema.md`.  It already contains
the mathematical spine:

- the Los boundary as diagnostic;
- the three-part schema of local data / global realization / failure mode;
- consistency as the compact contradiction case;
- CE as non-compact probabilistic coherence;
- forcing as strengthened coherence;
- objecthood as open horizon;
- valuation of refinement as a second instance.

This paper sketch should therefore be read as an extraction and expansion plan
for that note, not as a competing direction.

The fibre-mixing investigation is relevant but should be staged carefully.  It
may become a second worked example of the schema, with:

- local data: finitary observational/dynamical data;
- global realization: equivalence of algebraic and entropy witnesses;
- failure mode: fibre mixing fails, so the witnesses decouple;
- admissibility: whatever dynamical condition forces the needed fibre balance.

However, that investigation is not settled.  The notes currently identify a
two-step gap: an analytic lower bound for the large-fibre contribution
`kappa`, and a dynamical upgrade from positive-fraction balance to almost
everywhere balance.  Until those are resolved, fibre mixing should appear only
as a prospective second example, not as part of the core paper theorem.

## Proposed Paper Claim

The paper should not claim that coherence has been fully formalized as prior to
consistency.  A safer and sharper claim is:

> Consistency captures the contradiction failure mode, whose compactness is a
> theorem.  Other global realization failures are not contradiction failures and
> may be invisible to first-order/local tests.  These failures generate genuine
> coherence notions that require admissibility conditions beyond consistency.

The probability case is the worked example:

| Layer | Local structure | Desired completion | Failure mode | Admissibility |
|---|---|---|---|---|
| Logic | finite satisfiability | model | contradiction | consistency |
| Probability | finite additivity / compatibility | $\sigma$-additive measure | mass escape / limit instability | CE |
| Dimension | refinement sequence | scale/rate exponent | no valuation | $\Lambda$ |
| Dynamics | static law | time evolution / semigroup | no temporal coherence | temporal indexing/coherence |
| Fibre witnesses | finite reconstruction diagnostics | $\delta(L)\leftrightarrow H_2(\nu_L)$ | fibre imbalance / witness decoupling | fibre mixing or successor condition |

The first two rows are theorem-level now.  The dimension, dynamics, and fibre
rows are programme-level analogues unless their admissibility conditions are
proved in the relevant papers.

## Possible Abstract

This paper studies coherence conditions as conditions excluding specific
failure modes of global realization.  Consistency is treated as the special case
where the failure mode is contradiction, and first-order compactness explains
why contradiction is finitely detectable.  Other mathematical structures exhibit
non-compact failure modes: local data can remain compatible and first-order
well-behaved while failing to determine the intended global object.  The
probability case is the guiding example.  A directed system of coherent
finitely additive data need not force a $\sigma$-additive probability measure;
the missing condition is collective exhaustion, which rules out finitely
additive escape.  This motivates a general distinction between consistency,
coherence, and forcing/admissibility, and a philosophical reading of objects as
open horizons of coherent refinement rather than completed totalities.

## Candidate Theorem Shape

The exchange suggested a theorem schema:

Let $P$ be a global property not preserved under ultraproducts of
locally $P$-satisfying structures.  Then $P$ cannot be forced by any
first-order coherence condition in the local language.  Therefore any framework
that identifies objecthood with first-order/local coherence is incomplete with
respect to $P$.

In model-theoretic shorthand:

$$
(\forall i,\ M_i\models P)
\quad\text{but}\quad
\prod_U M_i\not\models P
\quad\Longrightarrow\quad
P\notin L_{\omega\omega}
$$

relative to the chosen signature/class of structures.

This is essentially the Los-boundary diagnostic, but reinterpreted as a failure
of automatic closure.

## More Specific Theorem Targets

### Target 1: Coherence Notion Schema

Define a coherence problem as a tuple

$$
(\mathsf{Loc},\mathsf{Glob},R,F)
$$

where:

- $\mathsf{Loc}$ is a class of local data;
- $\mathsf{Glob}$ is a class of candidate global realizations;
- $R$ relates local data to global realizations;
- $F$ is the intended failure mode.

A coherence condition is a predicate on local data excluding $F$.

Question:

> Can this be made precise enough to include consistency, CE, extension
> coherence, and valuation-of-refinement?

### Target 2: Compactness of Failure Modes

Define compactness for a failure mode:

> every failure instance is witnessed by a finite sub-instance.

Then:

- contradiction is compact by first-order compactness;
- CE/mass escape is not compact;
- valuation failure is generally not compact unless the valuation is finite-data
  prescribed.

Priority theorem:

> Under a suitable formalization, contradiction-type failure is the canonical
> compact failure mode, while CE-type mass escape is non-compact.

This would give a precise sense in which consistency is a special compact
coherence notion, not the whole genus.

### Target 3: Forcing vs Permitting

Distinguish:

- coherence that permits at least one global realization;
- admissibility/forcing that makes a target realization unavoidable.

Probability example:

> finite additivity and compatibility may permit finitely additive charges, but
> CE forces the $\sigma$-additive probabilistic completion.

Question:

> When does a coherence condition merely permit a completion, and when does it
> force the target completion?

## Philosophical Payoff

The exchange framed this through the contrast with monadic and totalizing
rationalist pictures.

The rejected monadic view:

> the object contains all admissible scales, completions, valuations, and
> relations internally.

The rejected naive empiricist view:

> the object is external, and observations merely accumulate toward it.

The proposed middle view:

> the object is the open structure of possible coherent refinement.

In this view, probability, dimension, rates, dynamics, and valuation are not
inside the object in isolation.  They are licensed when the relevant horizon
satisfies the relevant admissibility condition.

Merleau-Ponty is useful here because the mathematical structure is not raw data
and not pure form.  It is structured access under a horizon.

The phrase "structured accessibility" may be the cleanest nontechnical
expression.  It avoids both extremes:

- not a completed object containing all admissible completions internally;
- not arbitrary access imposed from outside;
- rather, objecthood as constrained openness under a horizon of possible
  refinement.

This gives a mature statement of the programme:

> The framework does not found probability, dynamics, or dimension by reducing
> them to observation.  It gives a grammar of admissibility: it says what must
> be added to coherent distinction for each richer form of objectivity to become
> licensed.

This is the line that protects the programme from overclaiming.  It does not
pretend assumptions disappear.  It relocates assumptions and makes them
structurally visible.

## Relation to Valuation and Zeta

The valuation discussion is a second instance of the same pattern.

Refinement alone gives

$$
\mathcal G_0\preceq\mathcal G_1\preceq\cdots,
$$

but does not force a scale $\Lambda(k)$.  Thus:

> refinement does not force valuation.

This mirrors:

> finite coherence does not force probability.

The zeta critical-line curve is therefore a boundary test.  The question is not
whether zeta contains an intrinsic probability or dimension in isolation, but
whether a specified query horizon supports:

- a nonvacuous naturality class;
- a valuation of refinement;
- a canonical CE-satisfying compatible charge.

## Proposed Structure

1. Introduction: coherence beyond consistency.
2. The local/global/failure-mode schema.
3. Consistency as the compact contradiction case.
4. Probability as non-compact failure of automatic closure.
5. CE as admissibility/forcing.
6. Objecthood as open horizon.
7. Valuation of refinement as a second instance.
8. Zeta and rational mathematical objects as boundary probes.
9. Open formal problems.

## Staging Options

There are two viable versions of the paper.

### Version A: Probability-Only Core

This is the safer first paper.

- Main theorem witness: countable additivity is not first-order axiomatizable.
- Main conceptual payoff: automatic closure fails; CE is admissibility/forcing.
- Scope: consistency, coherence, forcing, object-as-open-horizon.
- Other layers: dimension, zeta, and fibre mixing appear only as future
  analogues.

This version can be written downstream of the companion note because the hard
mathematical witness already exists and is already in submission-ready form.

### Version B: Two-Example Coherence Paper

This version waits for the fibre-mixing investigation.

- Worked example 1: CE / countable additivity.
- Worked example 2: fibre mixing / witness equivalence.
- Main payoff: the same local/global/failure/admissibility pattern recurs in
  probability and finite-sample reconstruction.

This would be stronger, but it should wait until the fibre-mixing derivability
question has a clean theorem or counterexample.

Current recommendation:

> Develop Version A as the foundations/coherence paper.  Keep Version B as the
> natural expansion if fibre mixing becomes theorem-clean.

## What Not To Do

Do not:

- put this whole discussion into the short countable-additivity companion note;
- claim that the formal schema is complete before it is defined;
- claim that coherence is mathematically proven prior to consistency;
- overstate the philosophical conclusion as a theorem;
- conflate this use of forcing with Cohen forcing;
- make Merleau-Ponty carry mathematical weight.

The mathematics should be carried by:

- Los's theorem;
- ultraproduct failure;
- non-first-order axiomatizability;
- CE as the exact admissibility condition;
- a formal compact/non-compact taxonomy of failure modes, if developed.

## Status

This is paper-shaped but not yet paper-ready.

Minimum next step:

1. Make the local/global/failure-mode schema formal.
2. Define compactness of a failure mode.
3. Prove the probability/CE case is a non-compact failure mode.
4. Decide whether there is a theorem separating contradiction-type compact
   failures from CE-type non-compact failures.

If those steps work, this could become a serious foundations/coherence paper
after Papers I-III or as a companion essay with one hard theorem and several
formal open problems.
