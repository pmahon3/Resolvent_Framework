# Mathematical Language: Coherence and Automatic Closure

**PARKED 2026-05-18.** See `paper_sketch.md` header for reason.

*Seed note - 2026-05-02*

## Structure

This note has three zones.  The probability/CE case runs through all three
as the seed example.

| Zone | Sections | Role |
|---|---|---|
| **A. Seed example** | Prototype through Four Faces of CE | The worked probability instance: language, witness, three layers, CE readings |
| **B. Abstract schema** | Minimal Abstract Schema through Public Wording | Formal skeleton: $(L,T,K,P,A)$, closure test, obstruction-passage pattern, expository discipline |
| **C. Generalization** | Beyond the Łoś Diagnostic through Immediate Next Step | Completion-descent, institution form, horizon plurality, coherence problem, compactness, candidate definitions and examples |

## Purpose

This note records the first mathematical language for the
coherence/completion direction.  The right starting point is the
submission-ready companion note:

`papers/archive/countable_additivity_retired/countable_additivity_not_first_order.tex`

That note gives the clean prototype:

- a first-order language;
- a first-order ambient theory of local structure;
- a global property not captured by first-order axioms;
- an ultraproduct witness showing failure of automatic closure;
- an admissibility condition, CE, that closes the intended probability horizon
  inside the observational framework.

The goal here is to abstract only what is mathematically doing work.

For the current note map and consolidation policy, see:

`notes/README.md`

For literature alignment, see:

`notes/unsorted/foundations/coherence_completion/logic_lit_review.md`

The main warning from that review is that the public mathematical language
should join existing conversations: abstract model theory, Stone
duality/support, categorical logic, and sheaf-style local-global obstruction.
The philosophical language of horizons and licensed closure should remain
scaffolding unless translated into those terms.

## Prototype: Countable Additivity

The companion note uses the language

$$
\mathcal L_{\mathrm{BA},\mu}
$$

of Boolean algebras with a normalized finitely additive charge encoded by
rational comparison predicates.

The ambient first-order theory is

$$
T_{\mathrm{fa}},
$$

axiomatizing:

- Boolean algebra structure;
- normalization;
- monotonicity;
- finite additivity;
- rational-cut coherence for the measure predicates, if desired.

The intended global property is

$$
P_{\sigma}
=
\text{``the charge is } \sigma\text{-additive.''}
$$

The theorem says:

> There is no first-order
> $\mathcal L_{\mathrm{BA},\mu}$-theory
> $T\supseteq T_{\mathrm{fa}}$ such that, among models of
> $T_{\mathrm{fa}}$,
> $T$ holds exactly when $P_\sigma$ holds.

Equivalently, $P_\sigma$ is not first-order axiomatizable over
$T_{\mathrm{fa}}$.

The witness is:

$$
M_n=(\mathcal P(\mathbb N),\delta_n),
$$

where each $M_n$ satisfies $P_\sigma$, but for a nonprincipal ultrafilter
$\mathcal U$ the ultraproduct

$$
\prod_{\mathcal U} M_n
$$

induces, on the diagonal copy of $\mathcal P(\mathbb N)$, the ultrafilter charge

$$
\ell(A)=\lim_{\mathcal U}\delta_n(A).
$$

This charge is purely finitely additive, hence not $\sigma$-additive.  Therefore
the class of $\sigma$-additive charge structures is not closed under
ultraproducts, and by Los's theorem cannot be first-order axiomatized.

## Reading of the Prototype

Mathematically, the proof shows:

$$
\text{local/first-order structure}
\nRightarrow
\text{intended global property}.
$$

Conceptually, this is a failure of automatic closure:

- every component is globally good;
- every first-order test is preserved in the ultraproduct;
- the intended global property fails in the limiting structure.

The failure is not contradiction.  It is non-compact failure of fit.

In the observational framework, CE is the admissibility condition that rules out
the corresponding failure mode:

$$
\text{finite additivity + compatibility + CE}
\Longrightarrow
\sigma\text{-additive observable probability}.
$$

Thus the prototype separates three layers:

| Layer | Mathematical role |
|---|---|
| $T_{\mathrm{fa}}$ | first-order/local structure |
| $P_\sigma$ | intended global completion property |
| CE | admissibility condition closing the horizon relative to $P_\sigma$ |

## Second Prototype: Paper I's Three Layers

Paper I already states the three-layer structure in mathematical terms:

> A finitely additive charge gives a coherent valuation on the Boolean algebra
> of observable distinctions; Stone duality completes that algebra into the
> space of all coherent distinction patterns, including nonprincipal ones; and
> collective exhaustion is the condition that determines when such a valuation
> extends to genuine probability.

This gives a richer prototype than the lean first-order note alone.

### Layer 1: Coherence

Local observable data are compatible finitely additive charges on Boolean
algebras of observable distinctions.

Symbolically:

$$
\{\ell_i:B_i\to[0,1]\}_{i\in I}
$$

with compatibility along refinement maps.

This is local coherence.  It says the observable pieces fit together as a
finitely additive valuation.

### Layer 2: Completion

Stone duality completes the Boolean algebra of distinctions into a compact
space of coherent distinction patterns:

$$
B \leadsto \operatorname{St}(B).
$$

This completion includes principal/realised patterns and nonprincipal/ideal
patterns.  A finitely additive charge on $B$ becomes a regular Borel measure on
the Stone completion, but not automatically a probability measure supported on
realised states.

Thus completion is not yet admissibility.  It may add ideal points that satisfy
all coherent distinction constraints but are not realised by the intended
observable domain.

### Layer 3: Admissibility

CE is the support/admissibility condition.  In the Stone picture it requires
the completed measure to concentrate on the realised/principal part:

$$
\hat\mu(\operatorname{pure}(\Omega))=1.
$$

Equivalently, by the Yosida-Hewitt interpretation, CE says the purely finitely
additive part vanishes:

$$
\mu_p=0.
$$

Thus:

$$
\text{coherent finite additivity}
\quad+\quad
\text{Stone completion}
\quad+\quad
\text{CE}
\quad\Longrightarrow\quad
\text{genuine probability}.
$$

This is the most concrete model for:

> open horizon / licensed closure.

The Stone completion opens the horizon to all coherent distinction patterns.
CE licenses descent back to genuine probability on realised observable states.

## Four Faces of CE

A concrete way to avoid building a solution in search of a problem is to ask:

> What is CE really?

The answer is not a single slogan.  CE has several mathematically precise faces.

### 1. Measure-Theoretic Face

CE is continuity from above at the empty set:

$$
E_1\supseteq E_2\supseteq\cdots,
\qquad
\bigcap_n E_n=\varnothing
\quad\Longrightarrow\quad
\mu(E_n)\to0.
$$

This is the classical analytic condition that upgrades finite additivity to
countable additivity on the relevant algebra.

### 2. Yosida-Hewitt Face

CE says that the purely finitely additive part vanishes:

$$
\mu=\mu_c+\mu_p,
\qquad
\mu_p=0.
$$

This identifies the obstruction algebraically.  Failure of CE is not vague
pathology; it is the persistence of a purely finitely additive component.

### 3. Stone-Support Face

CE says that the completed measure is supported on realised/principal points:

$$
\hat\mu(\operatorname{pure}(\Omega))=1.
$$

Stone completion is generous: it contains all coherent distinction patterns,
including nonprincipal ones.  CE is the support/descent condition that prevents
mass from escaping to ideal ultrafilter points.

### 4. Model-Theoretic Face

CE, or equivalently sigma-additivity in the lean Boolean-algebra-with-charge
language, is not first-order forced:

$$
P_\sigma
\text{ is not first-order axiomatizable over }
T_{\mathrm{fa}}.
$$

The Dirac ultraproduct witness shows that every first-order/local test may be
preserved while the intended global property fails.

### Synthesis

The four faces answer the same question from different mathematical registers:

| Register | What CE says |
|---|---|
| Measure theory | continuity from above |
| Yosida-Hewitt | no purely finitely additive part |
| Stone duality | support on realised/principal points |
| Model theory | not replaceable by first-order local structure |

This is the disciplined mathematical substitute for looser internal/external
language.  CE is not already forced by finite coherence, but it is also not an
arbitrary convention.  It is the exact admissibility/support/descent condition
that licenses the probabilistic completion.

## Minimal Abstract Schema

The least abstraction suggested by the prototype is a tuple

$$
\mathfrak C=(L,T,K,P,A),
$$

where:

- $L$ is a first-order language;
- $T$ is an $L$-theory describing the local or ambient structure;
- $K=\operatorname{Mod}(T)$ is the class of admissible local structures;
- $P\subseteq K$ is the intended global property or completion property;
- $A\subseteq K$ is an admissibility condition intended to rule out the failure
  mode obstructing $P$.

In the probability prototype:

$$
L=\mathcal L_{\mathrm{BA},\mu},
\qquad
T=T_{\mathrm{fa}},
\qquad
K=\operatorname{Mod}(T_{\mathrm{fa}}),
\qquad
P=P_\sigma.
$$

The role of $A$ is played, in the observational framework, by CE.  Strictly
speaking, CE is formulated for directed observational systems rather than for
bare $\mathcal L_{\mathrm{BA},\mu}$-structures.  This is important: the
admissibility condition may live in an enriched setting even when the
non-axiomatizability witness is stated in a lean first-order language.

## First-Order Closure Test

Given $(L,T,K,P)$, define:

> $P$ is first-order closed over $T$ if there exists an $L$-theory
> $T_P\supseteq T$ such that, for all $M\in K$,
> $M\models T_P$ iff $M\in P$.

Equivalently, $P$ is first-order axiomatizable relative to $T$.

By Los's theorem:

> If there are structures $(M_i)_{i\in I}$ with each $M_i\in P$ but some
> ultraproduct $\prod_{\mathcal U}M_i\notin P$, then $P$ is not first-order
> closed over $T$.

This is the Los-boundary diagnostic.

## Failure of Automatic Closure

Define a **failure of automatic closure** for $(L,T,K,P)$ as a family
$(M_i)_{i\in I}$ and an ultrafilter $\mathcal U$ such that:

1. $M_i\in K$ for all $i$;
2. $M_i\in P$ for all $i$;
3. $\prod_{\mathcal U}M_i\in K$;
4. $\prod_{\mathcal U}M_i\notin P$.

Such a witness says that $P$ is unstable under the limiting operation that
preserves all first-order $L$-facts.  Therefore no purely first-order
strengthening of the local theory can force $P$.

In the probability prototype:

$$
M_i=(\mathcal P(\mathbb N),\delta_i),
\qquad
P=P_\sigma.
$$

The ultraproduct failure is the ultrafilter charge.

## First Formal Foothold

The theorem-clean part can be developed entirely in the following language.

### Definition: Relative First-Order Closure

Let $L$ be a first-order language, $T$ an $L$-theory, and
$P\subseteq\operatorname{Mod}(T)$.

Say that $P$ is **first-order closed over $T$** if there exists an $L$-theory
$T_P\supseteq T$ such that

$$
P
=
\{M\in\operatorname{Mod}(T):M\models T_P\}.
$$

Equivalently, $P$ is first-order axiomatizable relative to the ambient local
theory $T$.

### Definition: Los Obstruction

A **Los obstruction** to $P$ over $T$ is a family
$(M_i)_{i\in I}$ in $P$ and an ultrafilter $\mathcal U$ on $I$ such that

$$
\prod_{\mathcal U}M_i\in\operatorname{Mod}(T)
\quad\text{but}\quad
\prod_{\mathcal U}M_i\notin P.
$$

When $T$ is first-order and every $M_i\models T$, the first condition follows
from Los's theorem.  It is still useful to state it explicitly because later
examples may use enriched languages, continuous logic, or nonstandard
categories where the closure theorem has to be checked separately.

### Lemma: Obstruction Implies Non-Closure

If $P$ has a Los obstruction over $T$, then $P$ is not first-order closed over
$T$.

Proof sketch:

If $P$ were first-order closed over $T$, say by $T_P$, then every $M_i$ would
model $T_P$.  By Los's theorem, the ultraproduct would model $T_P$, hence would
belong to $P$, contradiction.

### Prototype Corollary

For

$$
L=\mathcal L_{\mathrm{BA},\mu},
\qquad
T=T_{\mathrm{fa}},
\qquad
P=P_\sigma,
$$

the Dirac-mass construction gives a Los obstruction.  Hence
$P_\sigma$ is not first-order closed over $T_{\mathrm{fa}}$.

This is precisely the theorem of the countable-additivity companion note.

## What This Does and Does Not Prove

The relative non-closure result proves:

$$
T_{\mathrm{fa}}
\text{ plus any first-order local strengthening}
\nRightarrow
P_\sigma.
$$

It does not prove that probability is impossible, arbitrary, or merely imposed.
It proves that the passage from local finite coherence to countable additive
probability requires a non-first-order admissibility condition.

In Paper I, CE supplies that condition in the observational framework.

Thus the mathematical pattern is:

$$
\text{Los obstruction}
\quad\Rightarrow\quad
\text{automatic first-order closure fails}
$$

but

$$
\text{exact admissibility condition}
\quad\Rightarrow\quad
\text{licensed closure}.
$$

This two-part pattern is the candidate engine for the coherence/completion
programme.

## Expository Discipline

The mathematical exposition should not try to define "the middle" as a new
object.  It should instead formalize:

1. an obstruction to false closure;
2. an exact passage condition;
3. the equivalence of that condition across established mathematical
   languages.

For the probability case:

| Task | Mathematical form |
|---|---|
| Obstruction | $P_\sigma$ is not first-order closed over $T_{\mathrm{fa}}$ |
| Passage condition | CE is necessary and sufficient for observable extension |
| Analytic face | continuity from above |
| Algebraic face | $\mu_p=0$ in Yosida-Hewitt |
| Stone face | support on realised/principal points |
| Model-theoretic face | non-closure under ultraproducts |

This avoids turning the passage itself into an essence-bearing object.  The
rigorous content is carried by obstruction theorems and exact equivalences, not
by a new metaphysical definition.

## Generalization Without Loss of Rigour

The safe transition from the CE case to a broader description is not:

> every mathematical object has an open horizon and licensed closure.

That is too broad for theorem language.

The safe transition is:

> Some mathematical passages have the following two-part form: an obstruction
> theorem shows that a target global property is not forced by local structure,
> while an exact admissibility theorem identifies the additional condition under
> which the target passage is licensed.

This can be stated as a **pattern**, not yet as a universal theory.

## Obstruction-Passage Pattern

An **obstruction-passage pattern** consists of:

1. local data class $\mathsf{Loc}$;
2. target class/property $\mathsf{Target}$;
3. an obstruction theorem showing that $\mathsf{Target}$ is not forced by the
   chosen local structure;
4. an admissibility condition $A$;
5. a passage theorem showing that $A$ is necessary and sufficient, or at least
   sufficient and sharp, for the intended passage.

The CE case instantiates this as:

| Component | CE instance |
|---|---|
| Local data | finitely additive compatible observable charges |
| Target | $\sigma$-additive observable probability |
| Obstruction theorem | non-first-order axiomatizability / ultraproduct witness |
| Admissibility $A$ | CE |
| Passage theorem | CE characterisation / observable extension theorem |

This is rigorous because each component has theorem-level content in the CE
case.

## Relative Form

For a fixed formal setting, use:

$$
(L,T,P,A)
$$

where:

- $L$ is a language or formal environment;
- $T$ is the local/ambient theory;
- $P\subseteq\operatorname{Mod}(T)$ is the target property;
- $A$ is an admissibility condition in the relevant, possibly enriched,
  setting.

The pattern is valid when there are two results:

### Obstruction

$$
T
\nRightarrow_{\mathrm{local}}
P.
$$

In the first-order case, this may mean:

$$
P\text{ is not first-order closed over }T.
$$

### Passage

$$
T + A
\Longrightarrow
P,
$$

ideally with necessity:

$$
P
\Longrightarrow
A
$$

or with a precise equivalence after translating $P$ into the correct
extension/realization problem.

## Completion-Descent Form

For local/global settings, use:

$$
(\mathsf{Loc},\mathsf{Comp},\Gamma,\mathsf{Real},A).
$$

This form is valid when:

1. local data $x\in\mathsf{Loc}$ has a canonical or natural completion
   $\Gamma(x)$;
2. the completion is broader than the intended realised object;
3. there is a mathematically specified realised part
   $\mathsf{Real}(\Gamma(x))$;
4. the admissibility condition $A(x)$ is equivalent to descent/support on the
   realised part.

The CE/Stone case satisfies this:

$$
B\mapsto\operatorname{St}(B),
\qquad
A(B,\mu)\Longleftrightarrow
\hat\mu(\operatorname{pure}(\Omega))=1.
$$

Other cases should not be forced into this form unless they have genuine
completion and descent objects.

## Institution / Abstract-Logic Form

At the most abstract mathematical-logic level, the obstruction-passage pattern
can be stated in institution-style language.

Let

$$
\mathbb I=(\mathsf{Sign},\mathsf{Sen},\mathsf{Mod},\models)
$$

be a logical environment, where:

- $\mathsf{Sign}$ is a category of signatures;
- $\mathsf{Sen}(\Sigma)$ is the set/class of sentences over a signature
  $\Sigma$;
- $\mathsf{Mod}(\Sigma)$ is the category/class of $\Sigma$-models;
- $\models_\Sigma$ is the satisfaction relation.

This should be read broadly: it may be an institution in the strict
Goguen-Burstall sense, an abstract logic, a continuous logic, or another
structured semantic environment.

Fix:

- a signature $\Sigma$;
- a theory $T\subseteq\mathsf{Sen}(\Sigma)$;
- the ambient model class

$$
K=\mathsf{Mod}_\mathbb I(\Sigma,T);
$$

- a target subclass

$$
P\subseteq K;
$$

- a class of semantic operations $\mathcal O$ preserving the sentences of
  $\mathbb I$.

For first-order logic, $\mathcal O$ includes ultraproducts.

### Abstract Closure

Say that $P$ is **$\mathbb I$-axiomatizable over $T$** if there exists a theory
$T_P\supseteq T$ in $\mathbb I$ such that

$$
P
=
\{M\in K:M\models_\Sigma T_P\}.
$$

Say that $P$ is **$\mathcal O$-closed** if it is preserved by every operation in
$\mathcal O$ whenever the operation is defined on models in $P$.

If every $\mathbb I$-axiomatizable class is $\mathcal O$-closed, then failure
of $\mathcal O$-closure obstructs $\mathbb I$-axiomatizability.

For first-order logic:

$$
\mathbb I=\mathbb{FO},
\qquad
\mathcal O=\{\text{ultraproducts}\},
$$

and this recovers the Los obstruction.

### Enriched Admissibility

Often the admissibility condition does not live in the original logical
environment $\mathbb I$.  It lives in a richer environment

$$
\mathbb J
$$

with a forgetful or reduct map

$$
U:\mathbb J\to\mathbb I.
$$

Then an admissibility condition is a subclass

$$
A\subseteq \mathsf{Mod}_\mathbb J(\Sigma',T')
$$

such that, after forgetting to the lean environment, it licenses the target
property:

$$
N\in A
\quad\Longrightarrow\quad
U(N)\in P.
$$

Ideally, the passage theorem is sharper:

$$
N\in A
\quad\Longleftrightarrow\quad
U(N)\in P
$$

inside the intended extension/realization problem.

For the CE case:

- $\mathbb I$ is first-order Boolean algebras with rational charge predicates;
- $P=P_\sigma$ is sigma-additivity;
- $P$ fails ultraproduct closure, so it is not $\mathbb I$-axiomatizable;
- $\mathbb J$ is the enriched directed observational extension setting;
- $A$ is CE;
- the passage theorem says CE is exactly the condition for sigma-additive
  observable probability.

This gives a rigorous abstract version of:

> not forced in the lean logic; licensed in the enriched horizon.

### Why This Avoids Arbitrariness

The abstract schema is not arbitrary if each layer is named in an existing
mathematical-logic register:

- $\mathbb I$: an abstract logic/institution;
- $P$: a semantic target class;
- $\mathcal O$: preservation operations of the logic;
- obstruction: failure of preservation;
- $\mathbb J\to\mathbb I$: enrichment/reduct of logical environments;
- $A$: exact admissibility condition in the enriched environment;
- passage theorem: equivalence or sharp implication connecting $A$ to $P$.

The schema becomes empty only if these ingredients are chosen post hoc.  A real
instance must specify them independently and prove both obstruction and passage.

## What Counts as a Legitimate General Example

A future example should be admitted into the general schema only if it supplies
at least one obstruction theorem and one passage theorem.

Minimum checklist:

- What is the local data?
- What is the target passage/property?
- What is the false closure claim?
- What theorem refutes that false closure?
- What is the admissibility condition?
- What theorem shows that the admissibility condition licenses the passage?
- In what established mathematical language is this stated?

If an example lacks either the obstruction theorem or the passage theorem, it is
only an analogy.

## Public Wording

Safe:

> The CE case exhibits an obstruction-passage pattern: finite/first-order
> coherence does not force countable additivity, but CE is the exact
> support/descent condition under which finitely additive observational data
> becomes $\sigma$-additive probability.

Speculative but acceptable in notes:

> Similar obstruction-passage patterns may govern valuation, reconstruction,
> dynamics, and finite-sample certification.

Unsafe:

> All mathematical objecthood has the form open horizon / licensed closure.

Use the unsafe sentence only as private philosophical scaffolding, not as a
mathematical claim.

## Beyond the Los Diagnostic: Completion with Descent

The Los-obstruction language captures the negative theorem-clean point:

$$
\text{automatic first-order closure fails}.
$$

But it does not yet capture the richer positive structure suggested by Paper I:

$$
\text{local coherence}
\quad\leadsto\quad
\text{generous completion}
\quad\leadsto\quad
\text{admissible descent}.
$$

This may be the more faithful mathematical template for the philosophical
scaffold.

## Three-Layer Completion Template

A **completion-with-descent problem** should consist of data

$$
\mathfrak D=(\mathsf{Loc},\mathsf{Comp},\Gamma,\mathsf{Real},A),
$$

where:

- $\mathsf{Loc}$ is a class/category of local coherent data;
- $\mathsf{Comp}$ is a class/category of completed objects;
- $\Gamma:\mathsf{Loc}\to\mathsf{Comp}$ is a completion operation;
- $\mathsf{Real}$ specifies the realised/admissible part of a completed object;
- $A$ is an admissibility condition ensuring that the completed object descends
  to, or is supported on, the realised part.

The guiding picture is:

$$
x\in\mathsf{Loc}
\quad\mapsto\quad
\Gamma(x)\in\mathsf{Comp}.
$$

The completion $\Gamma(x)$ is generous: it contains all coherent completions
allowed by the local data, not only the realised ones.  The admissibility
condition $A(x)$ says that $\Gamma(x)$ is concentrated on or compatible with
$\mathsf{Real}(\Gamma(x))$.

### Paper I Instance

Local coherent data:

$$
x=(B,\mu)
$$

or a directed compatible family of finite observable Boolean algebras with
finitely additive charges.

Completion:

$$
\Gamma(B)=\operatorname{St}(B).
$$

The charge $\mu$ extends to a regular Borel measure $\hat\mu$ on
$\operatorname{St}(B)$.

Realised part:

$$
\mathsf{Real}(\operatorname{St}(B))
=
\operatorname{pure}(\Omega),
$$

the principal/realised ultrafilters coming from actual observable states.

Admissibility:

$$
A(B,\mu)
\quad\Longleftrightarrow\quad
\hat\mu(\operatorname{pure}(\Omega))=1.
$$

This is CE in Stone form.  Equivalently:

$$
\mu_p=0
$$

in the Yosida-Hewitt decomposition.

Thus Paper I has the shape:

$$
\text{finite coherent charge}
\quad\mapsto\quad
\text{measure on Stone completion}
\quad\xrightarrow{\mathrm{CE}}
\text{probability on realised states}.
$$

### Why This Is Better Than Bare $(L,T,P)$

The model-theoretic tuple

$$
(L,T,P)
$$

asks whether a property is forced by first-order local structure.

The completion-with-descent tuple

$$
(\mathsf{Loc},\mathsf{Comp},\Gamma,\mathsf{Real},A)
$$

asks how local coherent data naturally completes, why that completion may be too
large, and what condition licenses descent to the intended object.

This captures:

- stable openness: $\Gamma(x)$ contains coherent but possibly unrealised
  continuations;
- failure of automatic closure: $\Gamma(x)$ may place mass outside
  $\mathsf{Real}$;
- licensed closure: $A$ forces support/descent to the realised part.

In short:

> completion is generous; admissibility is selective.

## Objecthood as a Completion-Descent Pattern

This suggests a more mathematical form of "object as open horizon."

An object-horizon is not only a local datum $x$.  It is the structured pair:

$$
(x,\Gamma(x)),
$$

together with the question of which parts of $\Gamma(x)$ are realised or
admissible.

The local datum $x$ gives coherent finite distinctions.  The completion
$\Gamma(x)$ gives the horizon of possible coherent continuations.  The realised
part $\mathsf{Real}(\Gamma(x))$ identifies the intended domain of genuine
objectivity.  The admissibility condition $A$ says when the completed structure
actually descends to that realised domain.

This is a candidate mathematical translation of:

> objecthood is stable openness under coherent refinement.

It is still provisional, but it is closer to the philosophical scaffold than the
bare Los diagnostic.

## Horizon Plurality

The completion-descent template also makes room for multiple horizons.

For the same underlying mathematical object $X$, one may have several local
horizons

$$
x_\alpha\in\mathsf{Loc}_\alpha
$$

with completions

$$
\Gamma_\alpha(x_\alpha)
$$

and admissibility conditions

$$
A_\alpha.
$$

This is relevant for zeta and valuation examples.  Height, zero-spacing,
near-zero thresholds, argument/winding, proof depth, and spectral scale may
define different horizons.  They need not collapse to a single master
valuation.

The right comparison question is then:

> when do two horizons induce equivalent completions, compatible realised parts,
> or comparable admissibility conditions?

This is not needed for the probability prototype, but it prevents the framework
from falsely assuming one unique horizon for every object.

## Coherence Problem

A more conceptual object is a **coherence problem**

$$
\mathcal H=(\mathsf{Loc},\mathsf{Glob},R,F),
$$

where:

- $\mathsf{Loc}$ is a class of local data;
- $\mathsf{Glob}$ is a class of possible global realizations;
- $R\subseteq \mathsf{Loc}\times\mathsf{Glob}$ is a realization relation;
- $F$ is a specified failure mode for realization.

A coherence condition is a predicate

$$
C\subseteq \mathsf{Loc}
$$

that excludes $F$.

An admissibility or forcing condition is stronger: it does not merely say that
some realization is possible, but that the intended kind of realization is
forced.

For the probability case:

- $\mathsf{Loc}$: compatible finitely additive observable data;
- $\mathsf{Glob}$: measures on the generated observable $\sigma$-algebra or
  Stone/Caratheodory completion;
- $R$: extension/realization of local charges by a global measure;
- $F$: mass escape along globally vanishing sequences;
- $C$: CE.

## Compactness of a Failure Mode

The next definition needed is compactness of a failure mode.

Provisional version:

> A failure mode $F$ is compact if every instance of $F$ is witnessed by finite
> local data.

Contradiction is compact in first-order logic by the compactness theorem:

$$
\Gamma\text{ inconsistent}
\Longrightarrow
\exists \Gamma_0\subseteq_{\mathrm{fin}}\Gamma
\text{ inconsistent}.
$$

CE-type mass escape is not compact: every finite stage may look harmless, while
the failure appears only along a countable decreasing sequence

$$
A_0\supseteq A_1\supseteq\cdots,
\qquad
\bigcap_n A_n=\varnothing,
\qquad
\mu(A_n)\not\to0.
$$

This is the first technical place where the slogan

> consistency is the compact contradiction case

might become mathematically precise.

## Admissibility vs First-Order Axiomatizability

The prototype suggests a key distinction:

> A property may be non-first-order over a lean local language and nevertheless
> have an exact admissibility condition in the enriched framework.

For probability:

- $P_\sigma$ is not first-order axiomatizable in
  $\mathcal L_{\mathrm{BA},\mu}$;
- CE is an exact admissibility condition in the observational extension
  problem.

Thus non-axiomatizability is not defeat.  It identifies the boundary at which a
new admissibility condition is genuinely doing work.

This is the mathematical form of:

> open horizon / licensed closure.

## Candidate Definitions to Stabilize

### Definition: Local Horizon

A local horizon is a pair

$$
(L,T)
$$

where $L$ is a language and $T$ is an ambient theory specifying the local
structure preserved by the intended notion of observation or refinement.

### Definition: Completion Property

A completion property over $(L,T)$ is a class

$$
P\subseteq\operatorname{Mod}(T)
$$

whose members are the structures admitting the intended global realization.

Examples:

- $\sigma$-additivity for finitely additive charge structures;
- existence of a faithful reconstruction factor;
- existence of a valuation compatible with a refinement sequence;
- equivalence of algebraic and entropy witnesses under a fibre condition.

### Definition: Los-Obstruction

A Los-obstruction to $P$ over $T$ is an ultraproduct of $P$-structures in
$\operatorname{Mod}(T)$ that remains in $\operatorname{Mod}(T)$ but leaves $P$.

Such an obstruction proves $P$ is not first-order axiomatizable over $T$.

### Definition: Admissibility Condition

An admissibility condition for $P$ is a condition $A$ in the relevant enriched
setting such that:

1. $A$ excludes the identified failure mode;
2. $A$ is necessary and sufficient for the intended completion theorem, when
   such a theorem is available;
3. $A$ is not merely another local consistency condition in the original lean
   language.

CE is the model example.

## First Lemmas to Aim For

### Lemma 1: Los-Obstruction Implies Non-Axiomatizability

Let $L$ be first-order, $T$ an $L$-theory, and
$P\subseteq\operatorname{Mod}(T)$.  If $P$ has a Los-obstruction over $T$, then
$P$ is not first-order axiomatizable over $T$.

This is immediate from Los's theorem, but it is the formal bridge.

### Lemma 2: Countable Additivity Has a Los-Obstruction

In

$$
L=\mathcal L_{\mathrm{BA},\mu},
\qquad
T=T_{\mathrm{fa}},
$$

the property $P_\sigma$ has a Los-obstruction, witnessed by the Dirac
probabilities and the induced ultrafilter charge.

This is exactly the submission-ready companion note.

### Lemma 3: CE Is Not a First-Order Local Condition

In the lean language $\mathcal L_{\mathrm{BA},\mu}$, no first-order condition on
finitely additive charge structures can be equivalent to CE insofar as CE
forces $P_\sigma$.

Precise formulation needed:

- CE is formulated for observational systems, not bare Boolean charge
  structures.
- The correct statement may be: any enriched CE condition whose satisfaction
  implies $P_\sigma$ cannot be reducible to a first-order
  $\mathcal L_{\mathrm{BA},\mu}$-theory on the induced charge structures.

This needs care.

## Open Formal Choices

1. Should the general schema be stated in model-theoretic terms
   $(L,T,P)$, or in categorical/local-global terms
   $(\mathsf{Loc},\mathsf{Glob},R,F)$?

   Likely answer: start with $(L,T,P)$ for the theorem-clean part, then use
   $(\mathsf{Loc},\mathsf{Glob},R,F)$ as the broader conceptual schema.

2. Should "compact failure mode" be defined syntactically, semantically, or
   categorically?

   Candidate syntactic form: every failure is witnessed by finite fragments of
   the local diagram.

3. Should admissibility be a predicate on local data, on local-global pairs, or
   on the realization relation?

   CE suggests a predicate on local data strong enough to force a target
   realization.

4. Is "forcing" just uniqueness/existence of the intended completion, or a
   stronger modal claim?

   Keep it modest: forcing means that once the condition holds, no admissible
   completion of the relevant kind can fail the target property.

## Candidate Next Examples

The probability example is theorem-clean now.  Other examples should enter only
when they can provide the same ingredients:

1. a local language or local data category;
2. an ambient local theory/compatibility condition;
3. an intended global property;
4. a failure mode;
5. either a Los-style obstruction or another precise non-compactness witness;
6. an admissibility condition that rules out the failure mode.

### Dimension / Valuation

Local data:

$$
\mathcal G_0\preceq\mathcal G_1\preceq\cdots
$$

Target global property:

> a well-defined resolution dimension or rate exponent.

Failure mode:

> refinement has no scale; different valuations produce different exponents.

Admissibility:

> a valuation $\Lambda$ compatible with the refinement system.

Status:

Programme-level analogue.  No Los obstruction yet.  The first theorem should
probably be the valued-refinement rate theorem, not a non-axiomatizability
claim.

### Reconstruction / Faithfulness

Local data:

> finite observable algebras or finite delay observations.

Target global property:

> faithful recovery of the observable factor or hidden state up to the intended
> equivalence.

Failure mode:

> nonfaithfulness: distinct states remain observationally identified.

Admissibility:

> exhaustion / separation / faithfulness condition.

Status:

Likely belongs to Papers II-III, but the coherence schema can explain its role.

### Fibre Witness Equivalence

Local data:

> finite reconstruction diagnostics, such as separation defect and collision
> entropy.

Target global property:

$$
\delta(L)\to0
\quad\Longleftrightarrow\quad
H_2(\nu_L)\to\infty.
$$

Failure mode:

> fibres are imbalanced in a way that decouples algebraic and entropy
> witnesses.

Admissibility:

> fibre mixing or a successor condition.

Status:

Potential second worked example only after the fibre-mixing investigation is
settled.  Current gap: analytic lower bound for the large-fibre contribution
and dynamical upgrade from positive-fraction balance to almost-everywhere
balance.

### Zeta / Rational Mathematical Objects

Local data:

> zero-sensitive query fragments of the critical-line curve.

Target global property:

> canonical probability, valuation, or observable dimension attached to the
> declared horizon.

Failure mode:

> the object constrains many possible horizons but does not select a unique
> valuation or naturality class.

Admissibility:

> a nonvacuous naturality class and horizon-internal valuation.

Status:

Boundary probe.  Useful for the philosophy of objecthood, not a theorem source
yet.

### Propositional Probability

*Cut from Paper I body 2026-05-09.*

Local data:

> Finite Lindenbaum algebras $\mathcal{E}_n = \mathrm{Lind}(\phi_1, \ldots,
> \phi_n)$ of a consistent countable propositional theory $T$, with restriction
> as refinement.

Target global property:

> a $\sigma$-additive probability on complete consistent extensions of $T$.

Canonical instantiation:

$$
\Omega = \varprojlim_n \mathrm{atoms}(\mathcal{E}_n)
= \{\text{complete consistent extensions of } T\}.
$$

Surjective evaluation is the Lindenbaum extension lemma.  A compatible family
of normalised charges is a coherent system of finite-level probability
assignments.  CE requires assigned masses to drain on finite conditions that
collectively vanish; the CE characterisation theorem yields a unique
$\sigma$-additive measure exactly when CE holds.

Status:

Theorem-clean instance of the schema in a non-empirical setting.  Shows the
framework applies to logical probability, not only to physical observation.

## Working Notation

Use:

- $L$ for a first-order language;
- $T$ for an ambient/local theory;
- $K=\operatorname{Mod}(T)$ for local structures;
- $P\subseteq K$ for the target global property;
- $A$ for an admissibility condition;
- $F$ for a failure mode;
- $\mathcal U$ for an ultrafilter;
- $\prod_{\mathcal U}M_i$ for an ultraproduct;
- $\mathsf{Loc}$, $\mathsf{Glob}$, $R$ for the broader local-global schema.

Avoid overloading $C$: it can mean both coherence and compactness.  Use
$A$ for admissibility and reserve $C$ only when explicitly defining a coherence
predicate.

## Immediate Next Step

Write a one-page theorem-clean note with:

1. Definition of first-order closure over an ambient theory.
2. Definition of Los-obstruction.
3. Lemma: Los-obstruction implies non-axiomatizability.
4. Example: countable additivity in
   $\mathcal L_{\mathrm{BA},\mu}$ over $T_{\mathrm{fa}}$.
5. Remark: CE is an enriched admissibility condition, not a first-order local
   closure property.

That would be the first mathematical foothold for the coherence/completion
programme.
