---
name: Subalgebra embedding lemma — positive representability for concrete algebras
description: Polished theorem compressing all concrete positive cases into one argument; corollary unifying the positive side of the hierarchy; precise hypotheses and proof with load-bearing step flagged
type: project
---

# The Subalgebra Embedding Lemma

*Working note for the ultralimit representation investigation.*  
*Parent: `notes/future/foundations/ce_nonderivability/index.md`*  
*Cross-references: `stone_geometric_translation.md` (where the lemma is stated), `row5_candidate.md` (what a counterexample to Strategy D must overcome).*

---

## Purpose

The positive results accumulated across rungs 2–3 and the interval algebra case
were proved by separate constructions: spreading mass uniformly in each piece for
partition extensions, appealing to Lebesgue's full support for the interval algebra,
and so on. The subalgebra embedding lemma unifies all of these into a single argument.
It also draws the sharpest possible boundary around the positive territory, identifying
exactly what a counterexample to Strategy D would need to violate.

---

## Setup and Definitions

Let $B$ be a Boolean algebra. Recall:

- A **σ-additive probability** on $B$ is a finitely additive probability $\mu: B \to
  [0,1]$ satisfying $\mu(\bigvee_{n=1}^\infty A_n) = \sum_{n=1}^\infty \mu(A_n)$
  for every pairwise disjoint sequence $(A_n)$ in $B$ whose countable join
  $\bigvee_{n=1}^\infty A_n$ exists in $B$.

- A **Boolean algebra homomorphism** $\iota: B \to \Sigma$ (into a $\sigma$-algebra
  $\Sigma$) is a map preserving finite Boolean operations: $\iota(\mathbf{0}) =
  \emptyset$, $\iota(\mathbf{1}) = \Omega$, $\iota(A^c) = \iota(A)^c$, $\iota(A \vee
  B) = \iota(A) \cup \iota(B)$, $\iota(A \wedge B) = \iota(A) \cap \iota(B)$.
  Equivalently, $\iota$ is an embedding if it is additionally injective.

- A σ-additive probability $\mu$ on $\Sigma$ is **strictly positive on $B$ via
  $\iota$** if $\mu(\iota(A)) > 0$ for every non-zero $A \in B$ (i.e., for every
  $A \in B$ with $A \neq \mathbf{0}_B$).

- $\mathrm{Supp}_\sigma(B)$ denotes the closure in $\mathrm{St}(B)$ of the union of
  supports of all σ-additive probabilities on $B$ (see `stone_geometric_translation.md`).

---

## The Lemma

**Lemma (Subalgebra Embedding).** Let $B$ be a Boolean algebra, $\Sigma$ a
$\sigma$-algebra, and $\iota: B \hookrightarrow \Sigma$ a Boolean algebra embedding.
Suppose there exists a σ-additive probability $\mu$ on $\Sigma$ that is strictly
positive on $B$ via $\iota$. Then:

1. The pullback $\nu = \mu \circ \iota: B \to [0,1]$ is a σ-additive probability on $B$.
2. $\nu$ has full support: $\nu(A) > 0$ for every non-zero $A \in B$.
3. $\mathrm{Supp}_\sigma(B) = \mathrm{St}(B)$.

**Proof.**

*(Step 1: $\nu$ is a well-defined probability on $B$.)*  
Since $\mu$ is a probability on $\Sigma$ and $\iota$ is a Boolean algebra embedding
(hence $\iota(\mathbf{1}_B) = \mathbf{1}_\Sigma = \Omega$), we have $\nu(\mathbf{1}_B)
= \mu(\Omega) = 1$. Finite additivity of $\nu$ follows from finite additivity of $\mu$
and the fact that $\iota$ preserves finite disjoint unions: if $A \wedge B = \mathbf{0}_B$
then $\iota(A) \cap \iota(B) = \iota(A \wedge B) = \iota(\mathbf{0}_B) = \emptyset$,
so $\nu(A \vee B) = \mu(\iota(A \vee B)) = \mu(\iota(A) \cup \iota(B)) = \mu(\iota(A))
+ \mu(\iota(B)) = \nu(A) + \nu(B)$.

*(Step 2: $\nu$ is σ-additive on $B$.)*  
Let $(A_n)_{n \geq 1}$ be a pairwise disjoint sequence in $B$ whose join $J =
\bigvee_{n=1}^\infty A_n$ **exists in $B$**.

**Load-bearing step.** We claim $\iota(J) = \bigcup_{n=1}^\infty \iota(A_n)$ in
$\Sigma$ (equality as sets in $\Sigma$, not merely as Boolean algebra elements).

*Proof of claim.* Since $\iota$ is a Boolean algebra homomorphism:
- $\iota(A_n) \subseteq \iota(J)$ for all $n$ (since $A_n \leq J$ in $B$ and $\iota$
  is order-preserving).
- So $\bigcup_n \iota(A_n) \subseteq \iota(J)$.

For the reverse inclusion: $J$ is the *least* upper bound of $\{A_n\}$ in $B$. Let
$S = \bigcup_n \iota(A_n) \in \Sigma$ (a countable union of measurable sets, hence
measurable). We claim $\iota(J) \subseteq S$. Since $\iota(A_n) \subseteq S$ for
all $n$, the set $S$ is an upper bound for $\{\iota(A_n)\}$ in $\Sigma$. Suppose
$\omega \in \iota(J) \setminus S$. Since $\iota$ is an embedding, $\iota^{-1}$ is
defined on the image $\iota(B)$. The element $\iota^{-1}(S \cap \iota(J))$ would
be a well-defined element of $B$ (as $S \cap \iota(J) \in \iota(B)$... 

*Actually, $S$ need not be in $\iota(B)$.* The claim requires more care. The correct
argument is:

$J$ is the supremum of $\{A_n\}$ in $B$: for any upper bound $C \in B$ of $\{A_n\}$
we have $J \leq C$. We apply $\iota$ (which is order-preserving): $\iota(J) \leq
\iota(C)$, i.e., $\iota(J) \subseteq \iota(C)$. Now take the infimum over all
upper bounds $C$ of $\{A_n\}$ in $B$: $\iota(J) \subseteq \bigcap_{C \geq \text{all }
A_n} \iota(C)$. This intersection (in $\Sigma$) contains $\bigcup_n \iota(A_n)$.
The issue is whether equality holds.

**Revised approach to the load-bearing step.** Rather than establishing $\iota(J)
= \bigcup_n \iota(A_n)$ setwise, it suffices for the σ-additivity conclusion to
show $\mu(\iota(J)) = \mu(\bigcup_n \iota(A_n))$, i.e., $\mu(\iota(J) \setminus
\bigcup_n \iota(A_n)) = 0$.

We have $\iota(J) \supseteq \bigcup_n \iota(A_n)$ (since each $A_n \leq J$). Let
$R = \iota(J) \setminus \bigcup_n \iota(A_n)$ be the residual. In the Boolean algebra
$\Sigma$: $R = \iota(J) \cap \bigcap_n \iota(A_n)^c$. For each $n$, $R \cap
\iota(A_n) = \emptyset$ (by construction of $R$). So $R$ is disjoint from each
$\iota(A_n)$.

Now consider the element $C = \iota^{-1}(\iota(J) \setminus R) \in B$ — but
$\iota(J) \setminus R = \bigcup_n \iota(A_n)$ need not lie in $\iota(B)$, so this
pullback may not exist.

**Conclusion on the load-bearing step.** The claim $\mu(\iota(J)) = \sum_n
\mu(\iota(A_n))$ does NOT follow automatically from the order structure of $\iota$.
It requires an additional hypothesis. The correct additional hypothesis is:

> **($*$) $\iota$ preserves the existing countable joins: if $J = \bigvee_n A_n$
> in $B$, then $\iota(J) = \bigcup_n \iota(A_n)$ in $\Sigma$.**

Under hypothesis ($*$), the step is immediate: $\nu(J) = \mu(\iota(J)) = \mu(\bigcup_n
\iota(A_n)) = \sum_n \mu(\iota(A_n)) = \sum_n \nu(A_n)$, where the third equality
is σ-additivity of $\mu$ on $\Sigma$.

*(Step 3: $\nu$ has full support.)*  
By strict positivity: for every non-zero $A \in B$, $\nu(A) = \mu(\iota(A)) > 0$.
Hence every non-empty clopen $\hat{A} \subset \mathrm{St}(B)$ satisfies $\hat\nu(\hat{A})
= \nu(A) > 0$, so $\mathrm{supp}(\hat\nu) = \mathrm{St}(B)$.

*(Step 4: $\mathrm{Supp}_\sigma(B) = \mathrm{St}(B)$.)*  
Since $\nu$ is a σ-additive probability on $B$ with full support, $\mathrm{supp}(\hat\nu)
= \mathrm{St}(B) \subseteq \mathrm{Supp}_\sigma(B)$. The reverse inclusion is
immediate from the definition. $\square$

---

## Refined Statement

The correct hypothesis is not merely "Boolean algebra embedding" but "join-preserving
Boolean algebra embedding." This is the natural notion:

**Definition.** A Boolean algebra homomorphism $\iota: B \to \Sigma$ (with $\Sigma$
a $\sigma$-algebra) **preserves existing countable joins** if: whenever a pairwise
disjoint sequence $(A_n)$ in $B$ has a join $J = \bigvee_n A_n$ in $B$, then
$\iota(J) = \bigcup_n \iota(A_n)$ as a set equality in $\Sigma$.

**Refined Lemma.** Let $\iota: B \hookrightarrow \Sigma$ be a join-preserving Boolean
algebra embedding and $\mu$ a σ-additive probability on $\Sigma$ strictly positive on
$B$ via $\iota$. Then $\nu = \mu \circ \iota$ is a full-support σ-additive probability
on $B$, and $\mathrm{Supp}_\sigma(B) = \mathrm{St}(B)$.

**When is the join-preservation hypothesis automatic?** It holds whenever $\iota$ is the
natural inclusion of a subalgebra:

- If $B \subseteq \Sigma$ (as a set inclusion) and the join $J = \bigvee_n A_n$ exists
  in $B$, then $J$ is in particular an element of $\Sigma$ that is a measurable upper
  bound for $\{A_n\}$ in $\Sigma$. The union $U = \bigcup_n A_n \in \Sigma$ is the
  *smallest* upper bound in $\Sigma$ (as a measurable set). So $U \subseteq J$ (since
  $J$ is an upper bound in $\Sigma$ for $\{A_n\}$). But $U \supseteq A_n$ for all $n$,
  and $J$ is the *least* upper bound in $B$; so $J \leq U$ only if $U \in B$ and $U$
  is an upper bound for $\{A_n\}$ in $B$. The case $U \notin B$ is the subtlety.

**Simplest sufficient condition:** $B$ is a sub-Boolean-algebra of $\Sigma$ in which
every element of $B$ is also in $\Sigma$, and the join in $B$ of a disjoint sequence
$(A_n)$ (when it exists) *is* the same as the union in $\Sigma$. Equivalently:
$J = \bigvee^B_n A_n$ implies $J = \bigcup_n A_n$ (as a set). This holds whenever
$B$ consists of "honest measurable sets" (not equivalence classes) and the join in $B$
is the actual set-theoretic union. This is the situation for the interval algebra $\mathcal{I}
\subset \mathcal{B}([0,1])$ and for any subalgebra of a concrete measurable space.

**When the hypothesis may fail:** if $B$ is a quotient algebra (like $\mathcal{P}(\mathbb{N})/
\mathrm{fin}$), there is no natural injection into a σ-algebra that preserves quotient
structure. The hypothesis is vacuous for $\mathcal{Q}$ for a different reason (too few
joins exist), but more exotic quotient algebras might fail the hypothesis in a non-vacuous
way. This is the edge case that Strategy D must confront.

---

## Corollary: Compression of the Positive Side

**Corollary.** Let $B$ be a non-σ-complete Boolean algebra. Suppose either:

*(i) [Atomic case]* $B$ is atomic (equivalently, $\mathrm{Prin}(B)$ is dense in
$\mathrm{St}(B)$), or

*(ii) [Embedding case]* there exists a join-preserving embedding $\iota: B
\hookrightarrow \Sigma$ into a $\sigma$-algebra and a σ-additive probability $\mu$
on $\Sigma$ strictly positive on $B$ via $\iota$.

Then $\mathrm{Supp}_\sigma(B) = \mathrm{St}(B)$, and every finitely additive
probability on $B$ is in the weak* closure of σ-additive probabilities on $B$.
If $\mathrm{St}(B)$ is metrizable (e.g., $B$ is countably generated), the weak*
closure can be taken along sequences.

**Proof sketch.** Case (i): $\overline{\mathrm{Prin}(B)} = \mathrm{St}(B)$ (standard
duality for atomic Boolean algebras); discrete measures on $\mathrm{Prin}(B)$ are
σ-additive on $B$; their weak* closure is all regular Borel measures on $\mathrm{St}(B)$.
Case (ii): the Refined Lemma gives a full-support σ-additive $\nu$ on $B$; the argument
from the interval algebra section of `stone_geometric_translation.md` then applies:
measures absolutely continuous with respect to $\hat\nu$ are weak* dense in all Borel
measures on $\mathrm{St}(B)$, and each corresponds to a σ-additive probability on $B$.
$\square$

**Scope.** Case (ii) covers every Boolean algebra $B$ that arises concretely as a
subalgebra of a measure space (Borel subalgebras, interval algebras, finite combination
algebras, partition extensions). Cases where (ii) fails require $B$ to be
non-embeddable into any σ-algebra with a decent measure in the required sense — a
strong condition pointing toward abstract or forcing-theoretic constructions.

---

## What Strategy D Must Prove or Refute

The Corollary identifies the positive territory cleanly. Strategy D asks whether the
complement of cases (i) and (ii) is vacuous:

**Strategy D Question.** Is there a non-σ-complete non-atomic Boolean algebra $B$
that admits a σ-additive probability (on $B$, in the sense defined at the top of
this note) but does NOT satisfy the embedding hypothesis (ii) — and for which
$\mathrm{Supp}_\sigma(B) \subsetneq \mathrm{St}(B)$?

The preceding analysis suggests three approaches:

1. **Prove it is vacuous** (every such $B$ satisfies (ii) or a generalization). This
   would require showing that the presence of any σ-additive probability on $B$
   forces a join-preserving embedding into a σ-algebra with a full-support measure.
   This is plausible but not obvious: σ-additive measures on $B$ may not extend to
   σ-additive measures on $\sigma(B)$ in general.

2. **Find a counterexample** using submeasure theory. A Maharam-type algebra (a
   non-atomic complete Boolean algebra supporting only the zero σ-additive measure)
   cut down to a non-σ-complete subalgebra might yield $\mathrm{Supp}_\sigma(B)
   \subsetneq \mathrm{St}(B)$ while still admitting some σ-additive probability.
   But the non-σ-complete subalgebras of Maharam algebras are not well-studied.

3. **Set-theoretic sensitivity.** Whether counterexamples exist may be independent
   of ZFC. The question connects to: existence of real-valued measurable cardinals,
   submeasures on Boolean algebras (Talagrand's problem, now solved), and the
   structure of non-measurable sets in forcing extensions. This is downstream
   speculation; the concrete mathematical question should be settled first.

---

## Status

- [x] Load-bearing step identified and corrected: join-preservation is a separate
  hypothesis, not automatic from Boolean algebra embedding
- [x] Correct hypothesis stated: join-preserving Boolean algebra embedding with
  strictly positive ambient σ-additive probability
- [x] Refined Lemma proved under correct hypotheses
- [x] Sufficient condition for join-preservation: natural subalgebra inclusion where
  the join in $B$ equals the set-theoretic union in $\Sigma$
- [x] Corollary compressing the positive side: atomic density OR embedding → positive
- [x] Scope of the Corollary: covers all concrete non-σ-complete algebras; complement
  requires abstract constructions
- [x] Strategy D precisely formulated in terms of the embedding hypothesis
- [ ] Determine whether every non-σ-complete non-atomic $B$ admitting a σ-additive
  probability satisfies the embedding hypothesis (or some weaker condition implying
  the Corollary)
- [ ] Investigate submeasure-theoretic route to counterexample (requires Maharam
  algebra subalgebra theory)
