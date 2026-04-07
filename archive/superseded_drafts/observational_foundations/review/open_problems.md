# Open Problems: Closing the Gap Between Philosophy and Formalism

*2026-03-17; updated 2026-03-22*

> **Status update (2026-03-22).** Stopping Point 1 (measurable structure from primitive
> distinguishability) has been addressed by Paper −1 (*Discriminability and the Origin of
> the σ-Algebra*). The SP1 theorem (`thm:sp1`) proves that collective exhaustion is the
> exact characterisation of when σ-additive extensibility holds — establishing that
> measurable structure arises from index-layer coherence plus the valuation-layer condition,
> not from σ-additivity assumed as input. The key result: C1 of the tetralemma is false
> (counterexample: `fcContent_not_sigmaSubadditive`), and C4 is the only live option.
> Stopping Points 2–4 remain open as described below.

---

The paper's stated philosophy is:

> Probability arises from compatible observable experience — not as a primitive but as a derived structure.

The current formalism does not fully achieve this. Four stopping points remain where structure is assumed rather than derived. Each one corresponds to a deeper question the framework is pointing toward.

These are not gaps in the current paper — they are the research program that the current paper opens.

---

## Stopping Point 1: Measurable structure on outcome spaces

**What the paper currently does**

Every query $Q$ comes equipped with a full $\sigma$-algebra $\mathcal{B}(O_Q)$. This is imported silently and never explained.

**What is being assumed**

- That there is already a definite class of observable events at each resolution
- That this class is closed under countable operations
- That measurability is given, not earned

**The question the philosophy demands**

> What makes an event at resolution $Q$ observable?

A fully observational treatment would start from a primitive class $\mathcal{E}_Q \subseteq 2^{O_Q}$ of reportable distinctions — things an observer at resolution $Q$ can actually distinguish — and derive:
$$\mathcal{B}(O_Q) := \sigma(\mathcal{E}_Q)$$

The research problem is:

> **What closure properties must $\mathcal{E}_Q$ satisfy for the resulting $\sigma(\mathcal{E}_Q)$ to support the construction?**

More ambitiously:

> **Can $\sigma$-closure itself be derived from compatibility across refinements, rather than assumed at each query level?**

The conjecture is that if observable event classes $\mathcal{E}_Q$ are stable under finite Boolean operations and compatible under the refinement maps, then $\sigma$-closure is forced by the requirement that compatible families of events admit a global realization. This would make measurable structure a theorem of observational compatibility, not an assumption.

---

## Stopping Point 2: Countable additivity of observable laws

**What the paper currently does**

Each $\nu_Q$ is assumed to be a countably additive probability measure on $(O_Q, \mathcal{B}(O_Q))$.

**What is being assumed**

- That probability already exists locally at each query level
- That $\sigma$-additivity is present before the construction begins

**What the paper actually proves**

Global $\sigma$-additivity is propagated from local $\sigma$-additivity. The compression argument (Step 2 of the extension theorem) reduces $\sigma$-subadditivity of the global premeasure to $\sigma$-subadditivity of a single local measure $\nu_{Q_*}$. This is the mechanism — but it runs on assumed fuel.

**The question the philosophy demands**

> Can $\sigma$-additivity of the $\nu_Q$ itself be derived from compatibility?

The research problem is:

> **Start with only finitely additive set functions $\ell_Q : \mathcal{E}_Q \to [0,1]$ satisfying normalization and finite compatibility under refinement. Under what conditions is countable additivity forced?**

The compression argument already hints at the answer: if the query system is sequentially upper-directed, then any countable covering of a cylinder can be compressed to a single query level. If the finitely additive $\ell_{Q_*}$ cannot be finitely additive and simultaneously consistent with all finite compressions of a countable cover, then $\sigma$-additivity is forced.

Making this precise is the central analytic problem of the deeper theory. It would mean:

> $\sigma$-additivity is not assumed locally — it is the only globally consistent completion of finite compatibility under sequential refinement.

---

## Stopping Point 3: Realizability

**What the paper currently does**

Realizability — surjectivity of all evaluation maps $\mathrm{eval}_Q : \Omega \to O_Q$ — is assumed as a hypothesis.

**What is being assumed**

- That the projective limit $\Omega$ is non-degenerate
- That every locally consistent outcome extends to a globally coherent realization
- That there are no "phantom outcomes" — outcomes consistent at one level but blocked globally

**What realizability is actually doing**

Two distinct roles in the proof:

1. *Premeasure well-definedness:* equality of two cylinders in $\Omega$ implies equality of their base sets in $O_{Q_*}$ (used via surjectivity to push the set equality down)
2. *$\sigma$-subadditivity:* covering of cylinders in $\Omega$ implies covering of base sets in $O_{Q_*}$

In both cases the argument needs: what happens in $\Omega$ faithfully reflects what happens in $O_{Q_*}$.

**The question the philosophy demands**

> Can realizability be derived from compatibility?

The research problem is:

> **Under what purely observational conditions on the compatible family $\{\nu_Q\}$ and the query system is the projective limit $\Omega$ guaranteed to be non-degenerate?**

This is a Kolmogorov-type existence theorem without topology. The classical route (Polish spaces + tightness) works but imports topology. The observational route would need to find a purely measure-theoretic or logical condition on the compatible family that forces $\Omega \neq \emptyset$ and realizability.

Candidate directions:
- **Almost-sure realizability as the right weakening:** for $\nu_Q$-a.e. $o \in O_Q$, $o$ is globally realizable. This may be derivable from compatibility alone and is sufficient for the measure-theoretic arguments.
- **Ultrafilter / compactness arguments:** logical consistency of the compatible family forces a realization via a model-theoretic construction.
- **Inner regularity:** if each $\nu_Q$ is tight, compatible families force a tight global measure, from which realizability follows.

The deepest version of the question is:

> Is realizability a theorem of compatibility, or an independent axiom?

The current paper treats it as an axiom. Whether it is actually independent is unknown.

---

## Stopping Point 4: Directedness as an axiom rather than a consequence

**What the paper currently does**

Three directedness conditions are assumed:
- Lower-directedness (common coarsenings)
- Upper-directedness (common refinements)
- Sequential upper-directedness (countable common refinements)

**What is being assumed**

These are axioms about the structure of the query system. They say: the observational interface is rich enough to jointly coarsen, jointly refine, and jointly refine countably many resolutions simultaneously.

**The question the philosophy demands**

> Should directedness be derived from more primitive operational facts about observations?

The research problem is:

> **Can the directedness conditions be grounded in operational or compositional properties of the query system — things that should hold whenever experiments can be jointly performed or simulated?**

The intuition:
- If two experiments $Q_1, Q_2$ can always be performed together, there is a joint experiment $Q_1 \times Q_2$ that refines both — upper-directedness.
- If countably many experiments can always be jointly performed (or their outcomes jointly simulated), sequential upper-directedness follows.

This points toward a **categorical or operational reformulation** of directedness:

> Directedness is the closure property of the observational interface under joint experiment formation.

Under this framing, directedness is not an axiom about the poset $(\mathcal{Q}, \preceq)$ — it is a consequence of the closure of the experimental repertoire under product or composition operations.

Making this precise would require:
- A notion of "product query" or "joint observation"
- A demonstration that the natural class of jointly-performable experiments is directed
- A recovery of the current directedness hypotheses as special cases

---

## The central mechanism: compression

All four stopping points are connected by a single mechanism in the current proof: **compression**.

The $\sigma$-subadditivity argument works by compressing a countable family of cylinders to a single query level $Q_*$, reducing a global statement to a local one. This is where the global structure is forced from the local structure.

The deeper program asks:

> Can compression do more?

Specifically:

- Can compression force $\sigma$-closure of event classes (Stopping Point 1)?
- Can compression force $\sigma$-additivity of local laws (Stopping Point 2)?
- Can compression force realizability (Stopping Point 3)?
- Can compression be derived from joint experiment formation (Stopping Point 4)?

If the answer to all four is yes, the compression argument would become the engine of a fully observational derivation of probability — not just a step in a proof.

---

## Summary

| Stopping point | Currently | Goal |
|---|---|---|
| Measurable structure on $O_Q$ | Assumed ($\sigma$-algebra given) | Derived from primitive event classes $\mathcal{E}_Q$ via compatibility |
| Countable additivity of $\nu_Q$ | Assumed | Forced by compatibility + sequential refinement |
| Realizability | Assumed | Derived from compatibility (or identified as genuinely independent) |
| Directedness | Assumed | Derived from operational closure of the experimental repertoire |

The current paper establishes the mid-layer:

$$\text{local probability} + \text{compatibility} + \text{interface structure} \;\Longrightarrow\; \text{global probability}$$

The fully uncompromising version would establish:

$$\text{observable distinctions} + \text{compatibility} \;\Longrightarrow\; \text{probability}$$

Each stopping point above is one step on that path.
