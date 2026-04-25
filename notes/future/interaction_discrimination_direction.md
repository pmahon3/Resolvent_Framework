---
name: Interaction discrimination research direction
description: Separate future programme — two-entity discrimination theorem via joint query systems and predictive kernels; not part of the current four-paper arc
type: project
---

# Interaction from Observation: Separate Research Direction

**Candidate title:** *Interaction from Observation: An Observational Theory of Interaction Ecologies*

This is a new programme inspired by the Structure from Observationme, not part of the current four-paper arc. The four-paper series is structurally closed. This direction instantiates the same architectural ideas for a genuinely different object: interacting systems observed through joint query families.

---

## Central problem

The central mathematical problem is not whether interaction exists in some metaphysical sense, but whether interaction classes are **distinguishable**, **stable under refinement**, **reconstructible from delays**, and **certifiable from finite observations**. That is the question this programme addresses.

---

## Ontological hierarchy

$$\text{interaction ontology} \supset \text{economic ecology} \supset \text{market valuation}$$

The primary frame is a **general interaction ecology** — biological, social, informational, and economic systems all fall under it. Economics is a special ecology in which one important derived observable is price. Markets are a still narrower case in which pricing operators and surplus capture are layered on top. This ordering prevents price from becoming the primitive and makes the market application a real application rather than a motivating metaphor.

## Thesis

> We develop an observational theory of interaction ecologies: an interaction class is not a verbal label but a stable **predictive-effect signature**, defined relative to a joint query system and certified by refinement stability, reconstruction, and finite-sample witness.

## Relationship to classical ecology

Classical ecological models (Lotka-Volterra, niche theory, community matrices) assume state spaces and dynamics are known. This framework moves one level upstream: from modelled interaction dynamics to the observational conditions under which interaction classes are **inferable at all**. The contribution is not to replace ecological dynamics but to ask when interaction classes can be honestly discriminated from observation, without presupposing the state space. That is a genuine conceptual advance over the biological tradition, not a metaphorical borrowing from it.

## Relationship to May's random-matrix program

Robert May (1972) asked what global stability behavior follows generically from a structured ensemble of local interactions — stability as an emergent property of interaction topology, with the famous instability threshold for randomly assembled systems. That program remains central because it forced ecology and mathematics to co-develop rather than merely borrow from each other.

This framework is upstream of May in a precise sense: May assumes the community matrix (the interaction ensemble) is given; this program asks when that structure can be inferred from observation at all. The questions are complementary, not competing:

- **May:** given an interaction ensemble, what global behavior follows?
- **This program:** when is the interaction ensemble distinguishable, stable under refinement, reconstructible from delays, and certifiable from finite data?

The deeper motivation is the persistent ecological problem of local-to-global passage: when do local pairwise interactions assemble into stable higher-order organization? May showed this passage generates new mathematics. The next step is to ask not only when complex interaction structures are stable, but when they are *observable*.

---

## What the four papers already give

- **Paper I:** When is the joint observational object honest — surjective evaluation, discriminability, CE. Separates phantom interaction (coarse artifact) from genuine interaction (survives refinement).
- **Paper II:** Predictive kernels and minimal predictive states are the natural carrier of interaction effects. Non-factorization of the joint kernel signals interaction exists, relative to the chosen predictive observable and baseline — absolute non-factorization may be too blunt in the presence of nuisance dependencies.
- **Paper III:** Reconstructibility from delays via the density bridge. Joint delay algebra may separate interaction classes that marginal algebras cannot.
- **Paper IV:** Honest finite-sample witnesses and explicit separation diagnostics. Interaction class becomes empirically certifiable at finite lag.

---

## Candidate structure

1. General ontology of interacting systems — entities, joint query systems, predictive interaction
2. Interaction classes as predictive-effect signatures — neutrality, mutualism, competition, commensalism, parasitism
3. Refinement stability and reconstruction — when categories are honest rather than coarse artifacts
4. Finite-sample witnesses — certifying categories from data
5. Economic ecologies as a special case — firms, platforms, supply chains, complements
6. Markets as a still narrower special case — pricing operators, surplus capture, misvaluation of interaction structure

## Minimal formal scope

1. Set up a joint query system for two entities $(A, B)$.
2. Define four conditional kernels:
   $$\Pi_{A\mid A},\quad \Pi_{A\mid A,B},\quad \Pi_{B\mid B},\quad \Pi_{B\mid A,B}.$$
3. Define signed interaction functionals by comparing predictive laws with and without the partner:
   $$\Delta^g_{A \leftarrow B}(q_A, q_B) = \int g \, d\Pi_{A|A,B}(q_A, q_B, \cdot) - \int g \, d\Pi_{A|A}(q_A, \cdot)$$
4. Define interaction classes by predictive-effect signatures. Sign is the first-pass classifier, but a full signature includes:
   - sign (positive/negative/zero effect)
   - magnitude (strength of effect)
   - symmetry (relative effect in each direction)
   - persistence under refinement (stable vs. artifactual)
   - robustness to query choice

   Sign-pattern classes as a first pass: mutualism (both positive), competition (both negative), commensalism (one positive, one near zero), parasitism (one positive, one negative), neutrality (both near zero).
5. Prove stability of signatures under refinement or delay enrichment.
6. State reconstruction and finite-sample witness analogues as the empirical layer.

That is sufficient for a standalone paper. ~10–15 pages.

## Three proposed results (theorem sketch)

1. **Interaction existence theorem:** kernel non-factorization / predictive-effect nontriviality, relative to a chosen observable and baseline.
2. **Interaction signature stability theorem:** signature is invariant or covariant under observational refinement and delay enrichment.
3. **Interaction witness theorem:** finite-sample certification of class separation, analogous to Paper IV's pairwise witness.

---

## The key conceptual distinction (load-bearing)

The framework yields a **discrimination theorem**, not a **valuation theorem**.

It can establish when an interaction class is:
- observationally honest (Paper I layer)
- dynamically meaningful (Paper II layer)
- reconstructible from delays (Paper III layer)
- empirically detectable at finite sample (Paper IV layer)

It does **not**, by itself, determine who captures the surplus, whether it is already priced, or whether it is investable. The surplus-capture layer is genuinely separate.

---

## Market application (deferred companion note)

Undervalued mutualisms arise where the market uses a too-coarse observable algebra, pricing marginals while value lives in the joint predictive structure. The practical question — who captures the mutualistic surplus, is it durable, is it already priced — belongs in a companion note, not in the mathematical paper.

---

## Line graphs and the relation ontology (speculative)

There may be a nontrivial theory-level connection between interaction graphs and line graphs.

For an entity graph $G = (V, E)$, the line graph $L(G)$ has one vertex per edge of $G$, with two vertices adjacent when the corresponding edges share an endpoint. This is exactly the construction that promotes relations to objects — entity ontology → relation ontology — which is structurally parallel to this programme's shift from entity-level kernels to interaction-level structure:

- **Entity graph $G$:** who can directly interact
- **Line graph $L(G)$:** which pairwise interactions can condition or constrain each other (they share an entity)
- **Predictive interaction graph:** a weighted enrichment of $L(G)$, where vertices are interaction-effect signatures $\Delta^g_{A \leftarrow B}$ and weights encode kernel-kernel dependence, e.g. $w(e, e') = D(\Pi_e, \Pi_{e'})$

**Connection to refinement:** passing from $G$ to $L(G)$ is itself a form of observational refinement — enriching the observable algebra from entity-level to relation-level — and may be a concrete combinatorial instance of the Paper I refinement framework.

**Diagnostic use:** if interaction classes behave well on the line-graph lift, the system is essentially pairwise. Breakdown signals that the real ontology is hypergraphic (coalition effects, triadic complementarities, shared bottlenecks) rather than graph-theoretic.

**Caution:** the line graph is a combinatorial toy model — a first categorical shadow of an interaction ontology. The full framework is measure/predictive-law based and generalizes beyond pairwise interactions to hypergraphs and simplicial complexes. The connection plausibly defines a natural special case, though this remains to be made precise.

**Toy verification:** a useful first test is three or four entities — compare the entity graph, its line graph, and the predictive interaction graph built from $\Delta^g_{A \leftarrow B}$ to see exactly what is preserved and what is lost.

---

## Status

Deferred. Not part of the core programme. Revisit after arXiv submission of Papers I–IV.
