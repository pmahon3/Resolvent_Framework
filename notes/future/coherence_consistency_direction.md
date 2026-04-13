# Coherence, Consistency, and Failure Modes of Fit

*Seed note — 2026-04-13*

## Central question

Given a first-order language $L$, a class of $L$-structures $K$, and a
non-first-order global property $P$, when does failure of $P$ define a genuine
notion of incoherence not reducible to contradiction?

More concretely: which non-first-order properties generate genuine coherence
notions by separating local first-order satisfiability from stable global
realizability?

## The Łoś boundary as the key diagnostic

Łoś's theorem gives a precise one-way boundary: first-order properties are
preserved under ultraproducts.  The contrapositive is the diagnostic: if a
property $P$ fails in an ultraproduct of structures that individually satisfy
$P$, then $P$ is not first-order expressible.  The failure is not a contradiction — each member of the family is
individually $P$-satisfying — but the family *as a whole*, in the limit sense
given by the ultraproduct, is not.  This is a failure of fit that first-order
logic cannot see.

This suggests that consistency (non-contradiction, first-order satisfiability)
captures only one class of failure of fit: the class detectable at the
level of finite subsets of sentences in the language.  The Łoś boundary reveals
that there are structurally stable families — consistent, even individually
well-behaved — that fail a global condition invisible to finitary logic.

## Towards a general schema

A **coherence notion** should be specified by three components:

1. **Local data.** A family of $L$-structures, or local sections, or compatible
   valuations — whatever is given finitely or locally.

2. **Global realization.** A target: a global structure, a limit object, an
   extension to a larger domain.  What the local data is supposed to jointly
   determine or approximate.

3. **Failure mode.** The specific way in which local data can fail to sustain
   the global realization.  Not all failures are contradictions.

A coherence condition then excludes the relevant failure mode.  The coherence
notion is genuine — i.e., not reducible to consistency — when the failure mode
is not detectable by any first-order condition on the local data.

Under this schema:

- **Consistency** is the coherence notion where the global realization is a
  model of a theory, and the failure mode is contradiction (unsatisfiability of
  a finite subset of sentences).  The compactness theorem — a separate result —
  says this particular failure mode is always finitely detectable: every
  unsatisfiable set of sentences has a finite unsatisfiable subset.  That
  compactness is a theorem about the contradiction failure mode, not a general
  feature of coherence notions.

- **Probabilistic coherence / CE** is the coherence notion where the global
  realization is a $\sigma$-additive measure, and the failure mode is
  limit-instability: persistence of mass on sequences of events whose global
  intersection is empty.  The Łoś argument (Paper I, Prop. 4.11) shows this
  failure mode is not detectable by any first-order condition — probabilistic
  coherence is not compact.

## The priority claim — deferred but not abandoned

The claim that "coherence is more fundamental than consistency" is a natural
orientation, but should not be stated as a mathematical result until the schema
above has a precise formalization.  What can be said now, mathematically, is:

> Consistency captures exactly one failure mode — contradiction — and its
> compactness (every inconsistent set has a finite inconsistent subset) is a
> theorem, not a general feature of coherence notions.  Other failure modes
> generate coherence notions that are not compact, and which cannot be reduced
> to consistency by any first-order theory.

Whether "coherence" names a genus of which "consistency" is a species —
rather than a simple strengthening — is the philosophical claim the formal
framework should eventually support.

## A provisional taxonomy of failure modes

The following are candidate failure modes, each generating a distinct coherence
notion.  This list is illustrative, not exhaustive.

| Failure mode | Coherence notion | Compact? |
|---|---|---|
| Contradiction (finite unsatisfiability) | Consistency | Yes (compactness thm) |
| Limit-instability (ultraproduct fails $P$) | Limit-coherence [placeholder] | No (by Łoś contrapositive) |
| Non-extension (local data admits no global realization) | Extension-coherence | Depends |
| Mass escape (measure escapes to ideal limit points) | CE / probabilistic coherence | No |

The central question is whether there is a uniform framework — perhaps
categorical, perhaps sheaf-theoretic, perhaps in terms of abstract model theory
— that organizes these failure modes and their associated coherence notions.

## Diagnostic example: the probability case

The finite-cofinite content on $\mathbb{N}$ (or $\mathbb{Q}$) is the canonical
witness for the Łoś-boundary failure mode in the probability setting.  It is
individually consistent (no finite contradiction), compatible (commutes with
refinement maps), and normalized.  It fails only the global condition: the
sequence $A_k = \mathbb{N} \setminus \{0,\ldots,k\}$ decreases to $\emptyset$
but carries mass $1$ at every stage.

This is not a diagnostic for CE specifically.  It is a diagnostic for a general
phenomenon: a family of structures that individually satisfy a property $P$
(here: $\sigma$-additivity, carried by each Dirac charge $\delta_n$), whose
ultraproduct fails $P$ (the ultraproduct is the finite-cofinite content, which
fails $\sigma$-additivity).  By Łoś's theorem, $P$ is therefore not first-order
expressible.  CE names the gap: the non-first-order condition whose satisfaction
is equivalent to $P$.

## Open questions

1. **Formal schema.** Can the three-component schema (local data / global
   realization / failure mode) be made precise in a way that encompasses all
   four entries in the provisional taxonomy?  A categorical or sheaf-theoretic
   formulation may be natural.

2. **Classification of failure modes.** Is there a useful classification of
   non-first-order failure modes — by type, complexity, or relationship to the
   Łoś boundary — analogous to the arithmetical hierarchy for definability?

3. **Compactness as a special property of consistency.** Consistency is compact
   (compactness theorem).  Is compactness the property that distinguishes the
   contradiction failure mode from all others?  Or are there other compact
   coherence notions?

4. **Priority formalization.** In what formal sense, if any, is "coherence" prior
   to "consistency"?  One candidate: consistency is definable as the coherence
   notion for the trivial global realization (a single model of the theory), but
   coherence notions in general are not so definable.

5. **Connection to abstract model theory.** Infinitary logics ($L_{\omega_1\omega}$,
   $L_{\infty\omega}$) can express some non-first-order conditions.  Does
   limit-instability become first-order expressible in an appropriate infinitary
   language?  If so, the failure mode taxonomy may be indexed by logical strength.

## Status

Seed only.  The central question is mathematically investigable but the formal
framework does not yet exist.  Develop after main papers are posted.  The
probability case (CE, Paper I) is the primary worked example; it should not
drive the general framework.
