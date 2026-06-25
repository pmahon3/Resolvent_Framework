# Conceptual Vocabulary: Coherence and Failure Modes

*Seed note — 2026-04-13; thinned to vocabulary and taxonomy 2026-05-03*

## Role

This file defines the conceptual vocabulary for the coherence/completion
direction.  It does not contain worked examples, narrative, staging, or
exposition — those live in `paper_sketch.md`.  Action items and iteration
live in `development.md`.

## Central question

Given a first-order language $L$, a class of $L$-structures $K$, and a
non-first-order global property $P$, when does failure of $P$ define a genuine
notion of incoherence not reducible to contradiction?

## The Łoś boundary as diagnostic

First-order properties are preserved under ultraproducts (Łoś).  Contrapositive:
if $P$ fails in an ultraproduct of $P$-satisfying structures, then $P$ is not
first-order expressible.  The failure is not contradiction — each member
individually satisfies $P$ — but the family as a whole, in the limit sense, does
not.

## Three-component schema

A **coherence notion** is specified by:

1. **Local data** — a family of structures, local sections, compatible
   valuations; whatever is given finitely or locally.
2. **Global realization** — the target: a global structure, limit object, or
   extension.
3. **Failure mode** — the specific way local data can fail to sustain the global
   realization.  Not all failures are contradictions.

A **coherence condition** excludes the relevant failure mode.  It is genuine
(not reducible to consistency) when the failure mode is not detectable by
first-order conditions.

## Conceptual grammar

> consistency = possible coexistence
> coherence = structured continuation
> admissibility = licensed completion

Equivalently: coherence is consistency under intended continuation.

## Forcing vs permitting

A coherence notion **permits** when local data is compatible with at least one
global realization.  It **forces** when the local data leaves no room for
anything weaker than the target — the intended realization becomes unavoidable.

CE is forcing: once CE holds, the purely finitely additive part vanishes
(Theorem 4.10 of Paper I).

**Caution:** this is not forcing in the Cohen/Boolean-valued-model sense.

## Failure mode taxonomy

| Failure mode | Coherence notion | Compact? |
|---|---|---|
| Contradiction (finite unsatisfiability) | Consistency | Yes (compactness thm) |
| Limit-instability (ultraproduct fails $P$) | Limit-coherence [placeholder] | No (by Łoś contrapositive) |
| Non-extension (no global realization) | Extension-coherence [placeholder] | Depends |
| Mass escape (measure on ideal limit points) | CE / probabilistic coherence | No |

## Object as open horizon

The object is the horizon of coherent refinement: a structured field within
which distinctions can be made, related, extended, valued, and tested for
admissible completion.  Openness is structural, not an empirical defect —
witnessed by non-compact failure modes.

Compressed:

> object = open horizon of coherent refinement
> completion = attempted global realization
> failure mode = way the horizon refuses automatic closure
> admissibility = condition closing the horizon relative to a target

## Valuation of refinement

A refinement system alone does not determine scale, dimension, or divergence.
A **valuation of refinement** is the additional quantitative structure:

$$
\Lambda(i,j) = \text{scale, cost, divergence, or information distance of
refining } i \text{ to } j.
$$

Dimension-like quantities then have the form

$$
D_\Lambda = \limsup_{k\to\infty} \frac{H(\mathcal G_k)}{\Lambda(k)}.
$$

Valuation is horizon-internal, not object-internal in a completed monadic sense.

## Open questions

1. **Formal schema.** Can the three-component schema be made precise enough to
   encompass consistency, CE, extension coherence, and valuation-of-refinement?

2. **Classification of failure modes.** Is there a useful classification of
   non-first-order failure modes analogous to the arithmetical hierarchy?

3. **Compactness as distinguishing consistency.** Is contradiction the unique
   compact failure mode?  A positive answer would give a formal sense in which
   consistency is a distinguished species of coherence.

4. **Priority formalization.** In what formal sense, if any, is coherence prior
   to consistency?  Candidate: consistency is the coherence notion for the
   trivial global realization (a single model), but coherence notions in general
   are not so definable.

5. **Forcing vs admissibility.** Are admissibility and forcing always the same
   within the schema?  Can a coherence notion be admissibility-granting without
   being forcing?

6. **Connection to abstract model theory.** Does limit-instability become
   first-order expressible in an appropriate infinitary language
   ($L_{\omega_1\omega}$, $L_{\infty\omega}$)?  If so, the failure mode
   taxonomy may be indexed by logical strength.
