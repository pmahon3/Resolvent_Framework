# Seed: the peeling lemma for coherent views

**Setting.** A finite set V of variables, each with a finite value set. A *view* is a subset w ⊆ V;
a *view family* is a set W of views covering V. A *view law* assigns to each w ∈ W a probability
law on the values of the variables in w. The family is *coherent* if any two view laws agree on
the variables their views share.

**Definition.** W is *peelable* if its views can be listed w₁, …, w_m so that for each k ≥ 2 the
overlap w_k ∩ (w₁ ∪ … ∪ w_{k−1}) is contained in a single earlier view w_j (j < k).

**Peeling lemma (claim).** Every coherent view family on W is the set of restrictions of one joint
law on all of V iff W is peelable (after discarding views contained in other views).

**Proof idea.** If peelable, glue view by view: at step k, take the conditional law of w_k given the
overlap and multiply. If not peelable, the views contain a "cycle" of overlaps, and one builds
coherent view laws (e.g. parity-twisted laws on a cycle) with no joint.

**Declared types.** Type 1 (new theorem); Type 4 (vocabulary: views, peelability).
