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

This suggests that consistency captures only one class of failure of fit:
contradiction, which first-order compactness makes finitely detectable.  The Łoś boundary reveals
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
is not detectable by first-order conditions on the local data in the given
language.

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

## Conceptual grammar: continuation and closure

A useful working distinction:

> consistency = possible coexistence  
> coherence = structured continuation  
> admissibility = licensed completion

Equivalently:

> coherence is consistency under intended continuation.

Consistency says that the pieces can stand together without contradiction.
Coherence asks whether they can continue together toward the kind of global
form they are meant to disclose.  The failure of coherence is therefore not
always explosion or inconsistency.  It may be a failure of directional
integrity: the pieces coexist, and may pass every local test, but they do not
sustain the intended whole.

This gives a sharper reading of the probability example.  Finite additivity and
normalization are locally consistent.  They even support finitely additive
charges.  But without CE they do not sustain probabilistic continuation toward
a $\sigma$-additive measure.  The finite-cofinite/ultrafilter witness is not a
contradiction; it is a horizon that remains locally coherent while failing to
close in the intended probabilistic way.

The programme can therefore be read as a grammar of admissibility:

> coherent distinction does not eliminate assumptions; it locates the exact
> condition under which a richer mathematical structure becomes licensed.

Examples:

| Passage | Local structure does not force | Horizon condition |
|---|---|---|
| finite coherence $\to$ probability | $\sigma$-additive measure | CE |
| refinement $\to$ dimension | scale or valuation | valuation $\Lambda$ |
| observation $\to$ reconstruction | hidden-state recovery | faithfulness / exhaustion |
| population structure $\to$ finite-sample rate | concentration | sampling/mixing hypotheses |
| static law $\to$ dynamics | temporal evolution | temporal indexing/coherence |

The most compressed form is:

> open horizon / licensed closure.

## Forcing as strengthened coherence

The three-part schema distinguishes coherence notions by their failure modes.
But there is a further distinction within coherence notions: between those that
merely *permit* a global realization and those that *force* one.

A coherence notion **permits** a global realization when: local data satisfying
the coherence condition is compatible with at least one global realization.

A coherence notion **forces** a global realization when: local data satisfying
the coherence condition is compatible with *at most one* type of global
realization — the structure leaves no room for anything weaker.

This gives a refined hierarchy:

1. **Consistency** — excludes contradiction; permits any model (compact failure mode)
2. **Coherence** — excludes a specific non-first-order failure mode; may permit
   multiple completions
3. **Forcing** — the coherence condition is strong enough that the global
   realization becomes unavoidable; no admissible completion of the local data
   can fail to have the target property

In the probability setting, this is exactly the role CE plays.  Compatibility
alone permits probability but does not force it: the finite-cofinite content is
compatible yet fails CE and admits no $\sigma$-additive extension.  CE is the
condition that removes that slack.  Once CE holds, the purely finitely additive
part vanishes, and the data is forced to admit a probabilistic interpretation —
Theorem 4.10 of Paper I shows CE is both necessary and sufficient.

So CE upgrades observational coherence into forcing: it is the exact point at
which coherent finitely additive data leaves no room for anything weaker than
probability.

**Caution:** this is not forcing in the Cohen/Boolean-valued-model sense of
set theory.  It is an analogous conceptual pattern — constraint-driven necessity
— applied in a different domain.  Whether there is a formal connection to
set-theoretic forcing is an open question.

**The conceptual ladder:**

> consistency: nothing breaks  
> coherence: the pieces fit together (some global realizations are admitted)  
> forcing: the fit is now strong enough that a specific global structure is unavoidable

CE is where observational coherence becomes forcing.

## Objecthood as open horizon

The preceding schema suggests a sharper philosophical reading.  An object should
not be understood as a completed substrate behind its possible observations, nor
as a merely external target to which local data are later attached.  The object
is the horizon of coherent refinement: the structured field within which
distinctions can be made, related, extended, valued, and tested for admissible
completion.

This horizon is necessarily open.  If it were complete in itself, local
coherence would already determine every intended global realization.  The
probability case shows otherwise.  Normalization, finite additivity, and
first-order coherence do not force countable additivity.  The ultraproduct of
Dirac probabilities is locally indistinguishable, by first-order tests, from the
$\sigma$-additive structures from which it is built; nevertheless, on the
diagonal copy of $\mathcal P(\mathbb N)$, it induces a purely finitely additive
ultrafilter charge.

The failure is not contradiction.  It is a failure of automatic closure.  Thus
openness is not an empirical defect or a temporary lack of information.  It is a
structural feature of horizons of refinement.  The negation of openness would
identify local consistency with global realizability, but the Łoś-boundary
example shows that this identification is incoherent: the local tests all pass
while the intended global property fails.

CE closes one such horizon.  It is not merely another local consistency
condition; it is the admissibility condition that rules out a specific
non-compact failure mode, namely persistence of mass along globally vanishing
sequences.  In this sense, CE does not discover a probability already hidden
inside finite coherence.  It supplies the condition under which probabilistic
completion is forced.

The general pattern is:

> object = open horizon of coherent refinement  
> completion = attempted global realization  
> failure mode = way the horizon refuses automatic closure  
> admissibility = condition that closes the horizon relative to a target

Forcing is therefore local closure within an open horizon, not total completion
of the object.

## Valuation of refinement

The same pattern appears beyond probability.  A refinement system by itself does
not determine a scale, dimension, rate, or divergence.  It gives a hierarchy

$$
\mathcal G_0 \preceq \mathcal G_1 \preceq \mathcal G_2 \preceq \cdots,
$$

but not automatically a valuation of how costly, fine, distant, or informative
the passage from $\mathcal G_i$ to $\mathcal G_j$ is.

A **valuation of refinement** is a map

$$
\Lambda(i,j) =
\text{the scale, cost, divergence, proof-depth, or information distance
associated with refining } i \text{ to } j.
$$

In one-parameter examples this becomes a sequence $\Lambda(k)$.  In geometric
examples, $\Lambda(k)=\log(1/\varepsilon_k)$.  For the middle-thirds Cantor set,
$\Lambda(k)=k\log 3$.  In symbolic or hyperbolic dynamics, $\Lambda(k)$ is
supplied by cylinder scale or Lyapunov expansion.  In information geometry, it
may be KL/Fisher divergence.  In logical settings it may be formula depth,
quantifier rank, or type complexity.  In algorithmic settings it may be
description length.

Dimension-like quantities then have the general form

$$
D_\Lambda
= \limsup_{k\to\infty}
\frac{H(\mathcal G_k)}{\Lambda(k)},
$$

where $H(\mathcal G_k)$ measures the growth of distinguishable alternatives:
atom-count entropy, Shannon entropy, collision entropy, type entropy, spectral
counting entropy, or Kolmogorov complexity.

This shows that valuation, like probability, is not internal to the object as a
completed monad.  It is horizon-internal: it belongs to the object as an open
field of admissible refinement.  Once a horizon is fixed, the object may
strongly constrain which valuations are admissible; but the horizon is part of
the mathematical situation, not an accidental presentation.

The zeta critical-line curve is a natural boundary test for this view.  Its
zero-sensitive query system is highly structured, but it is not obvious that the
curve alone determines a canonical valuation of refinement.  Height, near-zero
thresholds, winding, zero density, functional-equation symmetry, normalized
zero spacing, and arithmetic structure each suggest different horizons.  The
question is therefore not whether zeta contains an intrinsic probability or
dimension in isolation, but whether a declared zero-sensitive horizon supports a
nonvacuous naturality class, a valuation of refinement, and a canonical
CE-satisfying charge.

## A provisional taxonomy of failure modes

The following are candidate failure modes, each generating a distinct coherence
notion.  This list is illustrative, not exhaustive.

| Failure mode | Coherence notion | Compact? |
|---|---|---|
| Contradiction (finite unsatisfiability) | Consistency | Yes (compactness thm) |
| Limit-instability (ultraproduct fails $P$) | Limit-coherence [placeholder] | No (by Łoś contrapositive) |
| Non-extension (local data admits no global realization) | Extension-coherence [placeholder] | Depends |
| Mass escape (measure escapes to ideal limit points) | CE / probabilistic coherence | No |

The central question is whether there is a uniform framework — perhaps
categorical, perhaps sheaf-theoretic, perhaps in terms of abstract model theory
— that organizes these failure modes and their associated coherence notions.

## Diagnostic example: the probability case

The finite-cofinite content on $\mathbb{N}$ (or $\mathbb{Q}$) is the canonical
witness for the Łoś-boundary failure mode in the probability setting.  It passes
every finite structural test: it is normalized, compatible, and free of local
contradiction.  It fails only the global condition: the
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

3. **Compactness as a special property of consistency** *(priority question).*
   The compactness theorem says the contradiction failure mode is always finitely
   detectable.  Is compactness the property that singles out the contradiction
   failure mode from all others?  Or are there other coherence notions — with
   different failure modes — that are also compact?  If compactness does single
   out contradiction-type failure, that would give a formal sense in which
   consistency is a distinguished instance of the schema, not merely one example
   among many.

4. **Priority formalization.** In what formal sense, if any, is "coherence" prior
   to "consistency"?  One candidate: consistency is definable as the coherence
   notion for the trivial global realization (a single model of the theory), but
   coherence notions in general are not so definable.

6. **Forcing vs admissibility.** CE is both an admissibility condition (it
   licenses the use of finitely additive data as probabilistic input) and a
   forcing condition (once satisfied, no weaker global structure is compatible).
   Are these always the same thing within the schema, or can a coherence notion
   be admissibility-granting without being forcing?  Is there a clean
   characterization of when a coherence notion forces rather than merely permits?

5. **Connection to abstract model theory.** Infinitary logics ($L_{\omega_1\omega}$,
   $L_{\infty\omega}$) can express some non-first-order conditions.  Does
   limit-instability become first-order expressible in an appropriate infinitary
   language?  If so, the failure mode taxonomy may be indexed by logical strength.

## Status

Seed only.  The central question is mathematically investigable but the formal
framework does not yet exist.  Develop after main papers are posted.  The
probability case (CE, Paper I) is the primary worked example; it should
constrain but not determine the general framework.

**First formal step (when ready):**

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
in which consistency is the unique compact coherence notion, and thereby a
precise statement of the priority claim.
