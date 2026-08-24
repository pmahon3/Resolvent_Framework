# Paper Sketch: Coherence, Completion, and Automatic Closure

**PARKED 2026-05-18.** Hostile-referee audit found Howson (2008, BJPS)
already made the core observation (consistency has compactness,
σ-additivity doesn't; "missing completeness theorem" p. 17). Paper
would restate Howson with ultraproduct proof. Salvage: Howson citation +
KVP footnote added to companion note. See plan for full audit.

*Seed note - 2026-05-02*

## Role

Exposition-shaped sketch for a possible coherence/completion paper downstream of
the companion note.  Not the proof notebook.  For the full cluster map, see
`index.md`.

Possible titles:

- *Coherence, Completion, and the Incoherence of Automatic Closure*
- *Objects as Open Horizons of Coherent Refinement*
- *Coherence Beyond Consistency*

## Core Thesis

(For vocabulary definitions, see `conceptual_schema.md`.)

The object is the horizon of coherent refinement — open, not complete.  Openness
is structural, not defect: it is witnessed by non-compact failure modes where
local coherence persists while the intended global realization fails.

In a freer register:

> the object is not what stands behind the horizon; the object is the horizon's
> stable way of opening.

The paper's conceptual grammar:

> consistency = possible coexistence;
> coherence = structured continuation;
> admissibility = licensed completion.

The paired phrase: **open horizon / licensed closure**.

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

## Relation to Other Notes

For the full cluster map, see `index.md`.

The companion note supplies the theorem witness; this paper explains its
structural meaning.  Do not insert philosophical/mathematical interpretation
into the companion note itself.

Fibre mixing may become a second worked example (Version B), but only after
the derivability question is settled.  See
`notes/archive/dynamics_reconstruction_dead/fibre_mixing/index.md`.

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

Three positions rejected:

- **Monadic:** the object contains all admissible completions internally.
- **Naive empiricist:** the object is external; observations accumulate toward it.
- **Proposed:** the object is the open structure of possible coherent refinement.

The mature programme statement:

> The framework does not found probability, dynamics, or dimension by reducing
> them to observation.  It gives a grammar of admissibility: it says what must
> be added to coherent distinction for each richer form of objectivity to become
> licensed.

This protects against overclaiming: assumptions are relocated and made
structurally visible, not eliminated.

## Relation to Valuation and Zeta

The pattern recurs: refinement alone does not force valuation, just as finite
coherence does not force probability.  The zeta critical-line curve is a
boundary test — see `notes/unsorted/foundations/zeta/observational_question.md`.

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

Paper-shaped but not paper-ready.  Next steps and iteration tracked in
`development.md`.
