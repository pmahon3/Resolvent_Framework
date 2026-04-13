# Coherence, Consistency, and the Probability Gap

*Seed note — 2026-04-13*

## Central claim

Consistency is not conceptually prior to coherence; it is one codified instance
of coherence — the shadow cast when the relevant domain is propositional logic
and the relevant failure of fit is contradiction.  Coherence is the more
fundamental notion.

## The diagnostic case

The finite-cofinite content is locally consistent: no finite collection of its
values contradicts any structural condition on the query system.  Yet it fails
CE.  This shows that consistency and probabilistic coherence are not on the same
continuum with consistency at the weak end.  They are different kinds of
conditions: consistency is a local, negative, finitary notion; probabilistic
coherence is a global, positive, limiting notion.

## Three levels, not two

1. **Consistency** — local, negative; excludes contradiction; generates no
   positive structure.

2. **Finitary coherence** — mutual compatibility under refinement;
   first-order expressible; still finitary.

3. **Probabilistic coherence** — finitary coherence + CE; governs limiting
   behaviour across the whole refinement hierarchy; not first-order expressible.

CE is the exact gap condition between levels 2 and 3.  The non-derivability
result (Prop. 3.9 / Prop. 4.11 of Paper I) says this gap is real and
irreducible: no accumulation of finitary conditions closes it.

## Sharpest formulation

> Contradiction is one mode of incoherence.  Consistency is one shadow of
> coherence, cast in the propositional domain.  CE marks a different shadow:
> the shadow cast when the domain is finitely additive families and the relevant
> failure is persistence of mass on globally vanishing events.

## Coherence-priority argument

Coherence, at its most general, is a condition of *joint fit*: a family of
constraints, valuations, or observations fits together when it sustains a stable
global interpretation.  Failure of coherence is failure of such fit.

Contradiction is one mode of failure of fit.  Consistency — the exclusion of
contradiction — is coherence as it appears in propositional logic.  But failure
of fit is not always contradiction.  The finite-cofinite content fails to fit
together probabilistically not because any two of its values contradict each
other, but because the whole family fails to stabilize in the limit.  No finite
subtest can detect it; only the infinite limiting behaviour reveals it.

This suggests a reversal of the standard ordering.  Coherence is not a
strengthening of consistency.  Consistency is a special case of coherence.

## Implication for foundations of probability

Foundational disputes (frequentist, subjectivist, objective Bayesian) are not
terminological.  They are disputes about which extra structure licenses the
passage from finitary coherence to probability.  All positions implicitly
recognise the gap; they disagree about how to bridge it:

- Subjectivists: Dutch book / coherence norms on betting behaviour
- Frequentists: limiting relative frequency
- Present framework: CE

What these positions share is that they all recognize some extra structure is
unavoidable.  The non-derivability result makes this precise: no finitary
condition suffices.  CE is the answer adopted here, with clear conceptual
content independent of any particular interpretation of probability.

## Open questions

1. **General framework for coherence levels.** The three-level picture is
   specific to this setting.  Are there analogues in sheaf theory (local vs
   global sections), category theory (diagram commutativity vs limits/colimits),
   or logic (first-order satisfiability vs compactness phenomena)?

2. **Dynamical analogue of CE.** The companion papers extend the framework to
   dynamics and delay-coordinate reconstruction.  What is the gap condition
   there, and is it non-derivable by similar means?

3. **Formal priority of coherence over consistency.** The argument here is
   conceptual.  Is there a formal sense in which coherence is prior — e.g.,
   can consistency be *defined* in terms of coherence but not vice versa, in
   some appropriate formal framework?

4. **Representation question.** Which purely finitely additive charges arise as
   ultraproducts or ultralimits of σ-additive probabilities?  (Left open in the
   CE non-derivability companion note.)

## Status

Seed only.  Develop into a philosophical companion note once the main papers
are posted.
