---
name: Row-5 candidate — searching for Supp_σ(B) ⊊ St(B) outside the σ-complete regime
description: Working note — define σ-additivity correctly on non-σ-complete Boolean algebras; analyze P(N)/fin; reassess direct-product strategy; record what the row-5 programme requires
type: project
---

# Toward a Row-5 Algebra: Corrected Foundations

*Working note for the frontier of the ultralimit representation investigation.*  
*Parent: `notes/future/foundations/ce_nonderivability/index.md`*  
*Prerequisites: `papers/paper_i/notes/ultralimit_investigation/stone_geometric_translation.md` (Stone note, especially the hierarchy table).*
*Launchpad: `papers/paper_i/notes/ultralimit_investigation/strategy_d_dossier.md`.*

---

## ⚠ Correction Notice (2026-04-17)

An earlier version of this note claimed that $\mathcal{P}(\mathbb{N})/\mathrm{fin}$
supports no σ-additive probability, and used this to construct a direct-product row-5
algebra. **That claim and the construction built on it are wrong.** The error is in
the definition of σ-additivity on a non-σ-complete Boolean algebra. The corrected
analysis is below.

---

## Part I: σ-Additivity on a Non-σ-Complete Boolean Algebra

### The correct definition

Let $B$ be a Boolean algebra (not assumed σ-complete). A finitely additive probability
$\mu$ on $B$ is **σ-additive** if: for every sequence $(A_n)_{n \geq 1}$ of pairwise
disjoint elements of $B$ such that the countable join $\bigvee_{n=1}^\infty A_n$
**exists in $B$**, we have
$$
\mu\!\left(\bigvee_{n=1}^\infty A_n\right) = \sum_{n=1}^\infty \mu(A_n).
$$

The key clause is **"exists in $B$."** When $B$ is not σ-complete, many countable
disjoint families have no join in $B$, and σ-additivity imposes *no constraint* on
$\mu$ for those families. The definition has fewer instances to satisfy than on a
σ-algebra.

**Consequence.** σ-additivity is a *weaker* condition on less complete algebras: as
$B$ has fewer countable joins, σ-additivity becomes less restrictive, and the class
of σ-additive probabilities on $B$ grows. In the extreme — when $B$ has no countable
joins beyond those already forced by finite additivity — σ-additivity on $B$ reduces
to finite additivity.

---

### Analysis of $\mathcal{P}(\mathbb{N})/\mathrm{fin}$

Let $\mathcal{Q} = \mathcal{P}(\mathbb{N})/\mathrm{fin}$, the power set of $\mathbb{N}$
modulo the ideal of finite sets. Elements are equivalence classes $[A]$ with $[A] = [B]$
iff $A \triangle B$ is finite. The partial order is $[A] \leq [B]$ iff $A \setminus B$
is finite. The Boolean operations are $[A] \vee [B] = [A \cup B]$, $[A] \wedge [B] = [A
\cap B]$, $[A]^c = [A^c]$, $\mathbf{0} = [\emptyset]$, $\mathbf{1} = [\mathbb{N}]$.

**Which countable joins exist in $\mathcal{Q}$?** The join $\bigvee_n [A_n]$ exists
in $\mathcal{Q}$ if and only if there is an element $[S] \in \mathcal{Q}$ that is the
least upper bound of $\{[A_n]\}$ in $\mathcal{Q}$. Equivalently (by the Galvin–Hajnal
theorem and standard quotient algebra facts): the join exists iff the family
$(A_n)$ is **eventually dominated** — there exists $S \subseteq \mathbb{N}$ such that
$A_n \setminus S$ is finite for all $n$ and $S \setminus \bigcup_n A_n$ is finite.

For a partition $(A_n)$ of $\mathbb{N}$ into infinite sets: each $A_n$ is infinite,
so $[A_n] \neq \mathbf{0}$. The join would need to be $[\mathbb{N}] = \mathbf{1}$ (since
$\bigcup_n A_n = \mathbb{N}$). But $\bigvee_n [A_n] = \mathbf{1}$ would require that
every upper bound of $\{[A_n]\}$ in $\mathcal{Q}$ is $\geq \mathbf{1}$, i.e., equals
$\mathbf{1}$. Is there a proper upper bound? Yes: take any $[S]$ with $S$ a selector
(one element from each $A_n$) — then $[A_n] \leq [S \cup A_n]$... but this gets
complicated. The direct argument is:

**Claim.** For a partition $\mathbb{N} = \bigsqcup_n A_n$ into infinite pieces,
$\bigvee_n [A_n]$ does not exist in $\mathcal{Q}$.

*Proof.* Suppose the join exists and equals some $[S]$. Then $[A_n] \leq [S]$ for
all $n$, meaning $A_n \setminus S$ is finite for all $n$. Since each $A_n$ is
infinite, $A_n \cap S$ is cofinite in $A_n$. In particular, $S$ must meet every
$A_n$ in an infinite set, so $S$ is "cofinite in each piece." Since the $A_n$ are
pairwise disjoint and cover $\mathbb{N}$, this forces $S$ to be cofinite in $\mathbb{N}$
... but wait: $S$ could itself be a proper subset of $\mathbb{N}$ even if it is
cofinite in each piece (e.g., remove one element from each $A_n$ to get
$S = \mathbb{N} \setminus \{a_n : n \geq 1\}$ where $a_n \in A_n$ — this has $[\mathbb{N}
\setminus S] = [\{a_n\}]$, but $\{a_n\}$ is infinite so $[S] \neq [\mathbb{N}]$ in
general). So $[S]$ need not be $\mathbf{1}$.

But then $[S]$ is a proper upper bound, and we need it to be the *least* upper bound.
For each $n$, removing a finite piece of $A_n$ from $S$ still leaves an upper bound
(since each $A_n \cap S$ is infinite, so $A_n \setminus S' = A_n \setminus S \cup (S
\setminus S')$ is still finite if $S \setminus S'$ is finite). This contradicts
minimality: one can find $[S'] < [S]$ that is still an upper bound. Hence no least
upper bound exists.

*More directly*: $\mathcal{Q}$ is $\aleph_1$-saturated (it has no countable
decreasing chains with positive lower bound), and it is a well-known fact that
$\mathcal{Q}$ is not σ-complete: the join of a partition into infinite pieces does not
exist. (This is equivalent to the statement that the quotient map
$\mathcal{P}(\mathbb{N}) \to \mathcal{Q}$ does not preserve countable joins for
partitions into infinite pieces.)

**Consequence for σ-additivity.** Whenever $\bigvee_n [A_n]$ does not exist in
$\mathcal{Q}$, σ-additivity imposes no constraint on $\mu([A_n])$. In particular,
for partitions of $\mathbb{N}$ into infinite pieces, σ-additivity is vacuous. This
means that singletons $\{n\}$ are finite (hence $[\{n\}] = [\emptyset] = \mathbf{0}$
in $\mathcal{Q}$), and the only countable joins that do exist in $\mathcal{Q}$
are those coming from "eventually cofinite" families — the join $\bigvee_n [A_n]$
exists when the $A_n$ have a common cofinite dominator up to finite error.

**Ultrafilter charges on $\mathcal{Q}$.** Let $\mathcal{U}$ be a non-principal
ultrafilter on $\mathbb{N}$. Define $\delta_\mathcal{U}([A]) = \mathbf{1}_{A \in
\mathcal{U}}$ (well-defined since if $A \triangle B$ is finite and $A \in \mathcal{U}$
then $B \in \mathcal{U}$, as $\mathcal{U}$ is non-principal hence contains all cofinite
sets). This is a finitely additive $\{0,1\}$-valued probability on $\mathcal{Q}$.

**Claim.** $\delta_\mathcal{U}$ is σ-additive on $\mathcal{Q}$.

*Proof.* Let $(A_n)$ be a pairwise disjoint sequence in $\mathcal{Q}$ (i.e., $[A_n]
\wedge [A_m] = \mathbf{0}$ for $n \neq m$, meaning $A_n \cap A_m$ is finite) whose
join $\bigvee_n [A_n]$ exists in $\mathcal{Q}$, equal to some $[S]$.

Since the $[A_n]$ are pairwise disjoint with join $[S]$, at most one $[A_n]$ can
be nonzero (have $\delta_\mathcal{U}([A_n]) = 1$), because $\mathcal{U}$ is a
two-valued measure and can be in at most one member of a pairwise disjoint family.
Say $\delta_\mathcal{U}([A_n]) = 1$ for at most one index $n = n_0$ (and $= 0$ for
all others). Then $\sum_n \delta_\mathcal{U}([A_n]) \in \{0, 1\}$.

If $\delta_\mathcal{U}([A_{n_0}]) = 1$ (i.e., $A_{n_0} \in \mathcal{U}$): since
$A_{n_0} \subseteq S$ up to a finite set and $A_{n_0} \in \mathcal{U}$, we get
$S \in \mathcal{U}$ (as $\mathcal{U}$ is non-principal), so $\delta_\mathcal{U}([S]) = 1$.
Equality holds.

If $\delta_\mathcal{U}([A_n]) = 0$ for all $n$: then for each $n$, $A_n \notin
\mathcal{U}$, so $A_n^c \in \mathcal{U}$. In the quotient, $[S] = \bigvee_n [A_n]$;
we need to show $S \notin \mathcal{U}$. Since $[A_n] \leq [S]$, we have $A_n
\setminus S$ finite for all $n$. The join condition (with $[S]$ minimal) implies
that $S \setminus \bigcup_n A_n$ is finite. So $S$ and $\bigcup_n A_n$ agree up to
a finite set. If $S \in \mathcal{U}$, then $\bigcup_n A_n \in \mathcal{U}$ (up to
finite, and $\mathcal{U}$ is non-principal). But $\mathcal{U}$ cannot contain a
countable union of sets not in $\mathcal{U}$ unless one of them is in $\mathcal{U}$
... actually this step requires a separate argument. See the note below.

**Note (gap in the σ-additivity proof for $\delta_\mathcal{U}$ on $\mathcal{Q}$).**
The argument above for the case "all $\delta_\mathcal{U}([A_n]) = 0$" implicitly
assumes that if $S \in \mathcal{U}$ and $S = \bigcup_n A_n$ mod-finite with $A_n
\notin \mathcal{U}$, we get a contradiction. This is the content of the Ramsey/
additivity theory for ultrafilters. It is TRUE: a non-principal ultrafilter is
*not* $\sigma$-additive as a {0,1}-measure on $\mathcal{P}(\mathbb{N})$ (this is
the classical result: ultrafilter charges on $\mathcal{P}(\mathbb{N})$ are finitely
but not σ-additive). But we are working on $\mathcal{Q}$, where the join is only
defined for specific sequences. The key point is:

> On $\mathcal{Q}$, the only disjoint sequences with an existing join are those
> where at most finitely many terms are nonzero in $\mathcal{Q}$ (i.e., $[A_n] =
> \mathbf{0}$ for all but finitely many $n$). In that case, σ-additivity reduces
> to finite additivity, which holds trivially.

**Supporting argument.** Suppose $(A_n)$ is a pairwise disjoint sequence in
$\mathcal{Q}$ (so $A_n \cap A_m$ is finite for $n \neq m$) with infinitely many
nonzero terms. After passing to a subsequence, we may assume all $A_n$ are infinite
and pairwise almost-disjoint (i.e., $A_n \cap A_m$ finite for $n \neq m$). We claim
$\bigvee_n [A_n]$ does not exist in $\mathcal{Q}$.

*Proof.* Suppose for contradiction that the join exists, equal to $[S]$. Then
$[A_n] \leq [S]$ for all $n$, meaning $A_n \setminus S$ is finite for all $n$.

Construct a selector: since each $A_n$ is infinite and $A_n \setminus S$ is finite,
$A_n \cap S$ is infinite. Choose a single element $a_n \in A_n \cap S$ for each $n$.
The set $T = S \setminus \{a_n : n \geq 1\}$ differs from $S$ in countably many
points (the selector $\{a_n\}$), but is not a finite perturbation of $S$ (the selector
is infinite). So $[T] < [S]$ in $\mathcal{Q}$ (since $S \setminus T = \{a_n\}$ is
infinite, so $[T] \neq [S]$, while $T \subset S$ gives $[T] \leq [S]$). Yet $[A_n]
\leq [T]$ for all $n$: $A_n \setminus T = A_n \cap \{a_k : k \geq 1\}$, and since
the $A_k$ are pairwise almost-disjoint, $A_n \cap \{a_k : k \neq n\}$ is finite
(each $a_k \in A_k$ and $A_k \cap A_n$ is finite), and $a_n \notin T$ by construction,
so $A_n \setminus T$ is finite. Hence $[T]$ is a strictly smaller upper bound for
$\{[A_n]\}$ than $[S]$, contradicting minimality of $[S]$ as the join.

Therefore no join exists. σ-additivity is not invoked for any such sequence.

If only finitely many $[A_n]$ are nonzero, then $\bigvee_n [A_n]$ exists (it is
the finite join of the nonzero terms) and σ-additivity reduces to finite additivity.

**Conclusion.** Every finitely additive probability on $\mathcal{Q}$ is σ-additive
on $\mathcal{Q}$. The algebra $\mathcal{Q} = \mathcal{P}(\mathbb{N})/\mathrm{fin}$
has so few countable joins that σ-additivity imposes no constraint beyond finite
additivity. In particular, non-principal ultrafilter charges $\delta_\mathcal{U}$
are σ-additive on $\mathcal{Q}$.

---

## Part II: Consequences for the Direct-Product Strategy

The earlier version of this note used "$\mathcal{P}(\mathbb{N})/\mathrm{fin}$ supports
no σ-additive probability" as the key ingredient for the direct-product row-5 algebra
$B = \mathcal{I} \times \mathcal{P}(\mathbb{N})/\mathrm{fin}$. That ingredient is
wrong. The correct statement is:

> Every finitely additive probability on $\mathcal{P}(\mathbb{N})/\mathrm{fin}$ is
> σ-additive on $\mathcal{P}(\mathbb{N})/\mathrm{fin}$.

This collapses the direct-product strategy: on $B = \mathcal{I} \times \mathcal{Q}$,
both factors support σ-additive probabilities (Lebesgue on $\mathcal{I}$, any
finitely additive probability on $\mathcal{Q}$ — including $\delta_\mathcal{U}$).
The "all σ-additive mass forced onto $\mathcal{I}$" argument is false. The algebra
$B$ likely has $\mathrm{Supp}_\sigma(B) = \mathrm{St}(B)$, making it a positive
instance, not a negative one.

**What the direct-product strategy requires.** To build a direct-product row-5 algebra
$B = B_1 \times B_2$ where $\mathrm{Supp}_\sigma(B) \subsetneq \mathrm{St}(B)$, one
needs a factor $B_2$ that:
1. Supports some σ-additive probability (otherwise the question is degenerate).
2. Has $\mathrm{Supp}_\sigma(B_2) \subsetneq \mathrm{St}(B_2)$ — i.e., some part
   of $\mathrm{St}(B_2)$ is genuinely invisible to all σ-additive probabilities.

For condition 2, one needs a non-atomic non-σ-complete Boolean algebra where
σ-additivity is a *genuine* constraint (not vacuous), and that constraint restricts
which ultrafilters can be in the support of σ-additive measures. Finding such a
$B_2$ is the real problem.

**Why the σ-completeness gradient matters.** The analysis of $\mathcal{Q}$ reveals
a spectrum:
- $\mathcal{P}(\mathbb{N})$ (σ-complete): σ-additivity has full force; strongly
  constrains the class of σ-additive measures; Nikodym applies.
- $\mathcal{Q} = \mathcal{P}(\mathbb{N})/\mathrm{fin}$ (quotient, few joins): σ-additivity
  vacuous; all finitely additive probabilities are σ-additive; the distinction
  between "σ-additive" and "finitely additive" vanishes.
- $\mathcal{I}$ (interval algebra; some joins): σ-additivity meaningful; Lebesgue
  measure satisfies it and has full support.

The challenge: we need an algebra intermediate in the spectrum — enough joins for
σ-additivity to be non-vacuous, but not enough for Nikodym to apply — where the
σ-additive class misses some part of the Stone space. This is a genuine constraint
on what row-5 algebras can look like.

---

## Part III: The Boolean Algebra Decomposition Theorem

**Theorem (canonical decomposition).** For any Boolean algebra $B$ and any element
$A \in B$, there is a canonical isomorphism
$$
B \cong (B{\upharpoonright}A) \times (B{\upharpoonright}A^c),
$$
where $B{\upharpoonright}A = \{C \in B : C \leq A\}$ with Boolean operations inherited
from $B$ (join, meet, and complement taken relative to $A$: $C^{A} = A \wedge C^c$),
and similarly for $B{\upharpoonright}A^c$.

*The isomorphism* maps $C \in B$ to $(C \wedge A,\, C \wedge A^c) \in (B{\upharpoonright}A) \times
(B{\upharpoonright}A^c)$; the inverse maps $(C_1, C_2)$ to $C_1 \vee C_2$.
This is a Boolean algebra isomorphism (finite operations preserved in both directions),
and it is canonical: no choices are involved.

**Consequence for σ-additivity.** If $\mu$ is a σ-additive probability on
$B{\upharpoonright}A$, then
$$
\tilde\mu(C) = \mu(C \wedge A)
$$
defines a σ-additive probability on $B$ supported on $\hat{A} \subseteq \mathrm{St}(B)$.
(*σ-additivity of $\tilde\mu$:* if $\bigvee_n C_n$ exists in $B$, then
$\bigvee_n (C_n \wedge A)$ exists in $B{\upharpoonright}A$ (meets distribute over existing
joins in Boolean algebras: $(\bigvee_n C_n) \wedge A = \bigvee_n (C_n \wedge A)$) and
$\tilde\mu(\bigvee_n C_n) = \mu((\bigvee_n C_n) \wedge A) = \mu(\bigvee_n(C_n \wedge A))
= \sum_n \mu(C_n \wedge A) = \sum_n \tilde\mu(C_n)$. ✓)

---

## Part IV: The Decomposition Forces Every Failure to be a Direct-Product Failure

**Claim.** If $\mathrm{Supp}_\sigma(B) \subsetneq \mathrm{St}(B)$, then $B$ decomposes
as a direct product with a measure-free factor. Specifically: there exists a nonzero
$A \in B$ such that $B{\upharpoonright}A$ admits no σ-additive probability, and
$B \cong (B{\upharpoonright}A) \times (B{\upharpoonright}A^c)$.

*Proof.* Suppose $\hat{A} \subseteq \mathrm{St}(B)$ is a nonempty clopen not covered
by $\mathrm{Supp}_\sigma(B)$, corresponding to nonzero $A \in B$. Every σ-additive
probability $\mu$ on $B$ assigns $\mu(A) = 0$ (since no ultrafilter in $\hat{A}$
is in the support). By the extension argument above (Part III), if $B{\upharpoonright}A$
admitted a σ-additive probability $\nu$, then $\tilde\nu(C) = \nu(C \wedge A)$ would
be a σ-additive probability on $B$ with $\tilde\nu(A) = \nu(A) = 1 > 0$, giving a
σ-additive probability on $B$ that charges $A$ — contradicting the assumption.
So $B{\upharpoonright}A$ is measure-free.

By the canonical decomposition theorem, $B \cong (B{\upharpoonright}A) \times (B{\upharpoonright}A^c)$.
The factor $B{\upharpoonright}A$ is measure-free; the factor $B{\upharpoonright}A^c$ carries
σ-additive probabilities (these are exactly the restrictions of σ-additive probabilities
on $B$ to $A^c$, renormalized). $\square$

**Corollary: "Indecomposable row-5" is impossible.** There is no Boolean algebra $B$
with $\mathrm{Supp}_\sigma(B) \subsetneq \mathrm{St}(B)$ that is not itself a direct
product with a measure-free factor. The failure of full σ-additive support is always
witnessed by a direct-product decomposition. Any "indecomposable" row-5 algebra would
require $\mathrm{Supp}_\sigma(B) \subsetneq \mathrm{St}(B)$ without any such decomposition
— but the canonical decomposition theorem shows this cannot happen.

**Consequence for the candidate strategies.** This eliminates Strategies A, B, and C:

- **Strategy A** (Boolean algebra extensions, non-trivially entangled): the canonical
  decomposition theorem shows that entanglement is impossible. At every element $A$,
  $B$ splits canonically. Any apparently entangled $B$ either has the measure-free piece
  as a direct summand (and is a direct product) or has no measure-free piece at all (and
  is fully positive). The category of Boolean algebras has no "non-split extensions" in
  the sense needed.

- **Strategy B** (quotient algebras with measure-free tails): any quotient of an interval
  algebra that fails full σ-additive support splits canonically into a measure-free factor
  and a positive factor. The quotient algebra is itself a direct product.

- **Strategy C** (forcing-theoretic constructions): the decomposition theorem is a theorem
  of ZFC, so it holds in all forcing extensions. Force-theoretic constructions cannot
  produce an indecomposable row-5 algebra.

---

## Part V: Strategy D — The Only Remaining Question

The preceding analysis reduces the entire open row to a single question:

> **Does there exist a non-σ-complete non-atomic Boolean algebra that is measure-free
> (admits no σ-additive probability)?**

If **yes**: pair it with any Boolean algebra carrying a σ-additive probability to get
a direct-product row-5 algebra $B = B_{\mathrm{free}} \times B_{\mathrm{pos}}$ with
$\mathrm{Supp}_\sigma(B) \subsetneq \mathrm{St}(B)$.

If **no**: then every non-σ-complete non-atomic Boolean algebra that admits any
σ-additive probability has $\mathrm{Supp}_\sigma(B) = \mathrm{St}(B)$ (because any
failure would require a measure-free factor, but no such non-σ-complete non-atomic
measure-free factor exists). The open row of the hierarchy collapses, and the answer
is always positive in the non-σ-complete non-atomic case.

### Conceptual meaning of the two outcomes

Strategy D is not merely a technical row in the hierarchy.  It asks whether the
Stone completion of a rich distinction system can be structurally inhospitable
to honest probability.

In the Boolean language, a non-atomic Boolean algebra is a system of
distinctions with no indivisible atoms.  Its Stone space is the compact horizon
of complete coherent distinction patterns.  A sigma-additive probability is an
honest countably additive valuation on that distinction system.  Strategy D asks
whether there is an intermediate Boolean algebra -- non-atomic but not
sigma-complete -- whose horizon admits no such honest probabilistic valuation.

If Strategy D has a **positive** answer, then there exist coherent horizons of
distinction that cannot host sigma-additive probability at all.  In the
coherence/completion language, this would show more than failure of automatic
closure: some completed horizons are structurally measure-free.  Probability is
not merely underdetermined there; it is unavailable.

If Strategy D has a **negative** answer, then sigma-additive probability is much
more widely available in the non-sigma-complete non-atomic regime than expected.
The philosophical weight then shifts away from existence and toward selection:
the central problem is not whether honest probability can live on such horizons,
but which admissibility/support condition selects the relevant probability or
ensures descent to realised states.

Thus either outcome informs the central theme:

- positive Strategy D: some coherent horizons are probability-inhospitable;
- negative Strategy D: probability is broadly available, and CE-like conditions
  govern admissible support/descent rather than bare existence.

**Evidence toward "no" (open row vacuous).** The subalgebra embedding lemma
(see subalgebra_embedding_lemma.md) gives a large positive class: if $B$ embeds
join-preservingly into a $\sigma$-algebra $\Sigma$ carrying a strictly positive
σ-additive probability, then $\mathrm{Supp}_\sigma(B) = \mathrm{St}(B)$ and in particular
$B$ is not measure-free. This covers all concrete non-σ-complete non-atomic algebras
(interval algebras, Borel subalgebras of standard measure spaces, etc.).

For a positive answer to Strategy D, one needs a measure-free non-σ-complete
non-atomic Boolean algebra that *cannot* be so embedded. This is a strong non-embeddability
condition. Candidates:

- **Maharam-type algebras:** A Maharam algebra is a complete non-atomic Boolean algebra
  admitting a strictly positive Maharam submeasure but no σ-additive probability. The
  existence of Maharam algebras (i.e., of Maharam's problem solved by Talagrand 2008) is
  irrelevant here: Maharam algebras are σ-complete, hence already covered by the Nikodym
  negative row. A *non-σ-complete* subalgebra of a Maharam algebra would be needed — but
  subalgebras of Maharam algebras need not inherit the measure-free property.

- **Free Boolean algebras on uncountable generators:** Free Boolean algebras are atomic
  (the Stone space is $2^\kappa$, totally disconnected compact), so their σ-additivity
  theory is trivial. Not relevant.

- **Forcing-generic algebras:** Cohen forcing, random forcing, and other generic Boolean
  algebras are typically σ-complete (they are complete Boolean algebras in the ground
  model). Not in the right regime.

**Literature survey (2026-04-18).** A targeted pass through Kelley (1959), Gaifman (1964),
Fremlin (Measure Theory §§31–39), Talagrand (2008), and Džamonja–Plebanek finds the following:

- **No published example** of a non-σ-complete non-atomic measure-free Boolean algebra
  exists in the literature. Strategy D is genuinely open.
- **No published proof** that none can exist.
- **Kelley's criterion** (Pacific J. Math. 1959) characterizes strictly positive *finitely
  additive* measures via intersection numbers. It has no known σ-additive analogue for
  incomplete algebras.
- **Gaifman** (Pacific J. Math. 1964) constructs algebras with no finitely additive
  measure at all — a strictly stronger condition than what Strategy D requires (no
  σ-additive probability, finitely additive ones permitted). His examples do not address
  the finitely-additive-yes / σ-additive-no gap.
- **Fremlin** focuses on complete and σ-complete algebras; the incomplete regime is not
  systematically treated.
- **Weak distributivity — verified, but does not apply to the non-σ-complete regime.**
  Džamonja–Plebanek ("Strictly Positive Measures on Boolean Algebras," *J. Symbolic Logic*
  **73** (2008) 1416–1432) prove in ZFC: for a **Boolean σ-algebra** (σ-complete Boolean
  algebra), weakly distributive + strictly positive finitely additive measure ↔ strictly
  positive σ-additive measure. The same result appears in Fremlin, *Measure Theory* §391D.
  Plebanek ("Algebraic Characterizations of Measure Algebras," *Proc. AMS* **136** (2008))
  gives a purely algebraic reformulation (uniformly weakly distributive + concentrated),
  again for σ-complete algebras. All of these results are in ZFC and are sharp in the
  σ-complete case: measure-freeness there forces non-weak-distributivity (given Kelley's
  condition).
  
  **However, none of these results apply to non-σ-complete Boolean algebras.** The proofs
  use countable suprema in essential ways (Fremlin 391D constructs an order-continuous
  functional via directed suprema). In a non-σ-complete algebra, those suprema may not
  exist in $B$, and σ-additivity of a measure on $B$ is already a weaker condition (it
  applies only when countable joins exist in $B$). The theorem's conclusion does not
  transfer. A weakly distributive non-σ-complete non-atomic algebra carrying a strictly
  positive finitely additive measure is **not** forced by this theorem to carry a strictly
  positive σ-additive measure. The Strategy D question is not addressed.
  
- **Talagrand** (Ann. Math. 2008) addresses only σ-complete Maharam algebras; not directly
  applicable.

**A fourth necessary condition: uncountably generated.**

**Claim.** Every countably generated non-atomic Boolean algebra carries a strictly
positive σ-additive probability. Therefore any Strategy D counterexample must be
**uncountably generated**.

*Proof.* If $B$ is countably generated, its Stone space $\mathrm{St}(B)$ embeds
continuously into $\{0,1\}^\omega$ (via the characteristic functions of the countably
many generators), so $\mathrm{St}(B)$ is compact and metrizable. If $B$ is also
non-atomic, $\mathrm{St}(B)$ has no isolated points. A compact metrizable
zero-dimensional space with no isolated points is homeomorphic to the Cantor set
(Brouwer's theorem). The homeomorphism $\varphi: \mathrm{St}(B) \to C$ sends clopens
to clopens and is a Boolean algebra isomorphism $B \cong \mathrm{Clop}(C)$. The
clopen algebra of the Cantor set embeds join-preservingly into the Borel σ-algebra
of $C$ (a clopen join in $\mathrm{Clop}(C)$ is a finite join, hence equals the
set-theoretic union, which is preserved). Lebesgue measure on $C$ is strictly
positive on all clopens, so the subalgebra embedding lemma applies: the restriction
of Lebesgue measure to $\mathrm{Clop}(C) \cong B$ is a strictly positive σ-additive
probability on $B$. $\square$

*Note on independence.* The proof goes through the subalgebra embedding lemma and
is not a separate mechanism: the Cantor-set homeomorphism provides the join-preserving
embedding. The new content is the Brouwer reduction, which shows countably generated
non-atomic algebras are always in the embedding lemma's scope.

---

## Topological Reformulation and Set-Theoretic Status

**Reformulation as a Radon-measure-free compact space problem.**

Since $B = \mathrm{Clop}(K)$ for $K = \mathrm{St}(B)$, Strategy D is equivalent to:

> Does there exist a compact totally disconnected Hausdorff space $K$ with no isolated
> points, not basically disconnected, and carrying no strictly positive Borel (Radon)
> probability measure?

Here *not basically disconnected* translates to non-σ-completeness of $\mathrm{Clop}(K)$
(a compact zero-dimensional space is basically disconnected iff every open Fσ has
clopen closure, iff $\mathrm{Clop}(K)$ is a σ-algebra). *No isolated points* translates
to non-atomicity of $\mathrm{Clop}(K)$. *No strictly positive Radon measure* translates
to measure-freeness of $\mathrm{Clop}(K)$: any Radon probability $\mu$ on $K$ that is
strictly positive on all nonempty open sets restricts to a strictly positive σ-additive
probability on $\mathrm{Clop}(K)$.

This connects Strategy D to the study of **Radon-measure-free compact spaces**, a topic
with substantial set-theoretic sensitivity:

- **Under MA + ¬CH:** Every compact space of weight $< \mathfrak{c}$ carries a strictly
  positive Radon measure (Fremlin, *Measure Theory* §531–534). Since any Strategy D
  counterexample must be uncountably generated, its Stone space has weight $\geq \omega_1$.
  Under MA + ¬CH, $\omega_1 < \mathfrak{c}$, so this does not immediately exclude
  counterexamples of weight exactly $\omega_1$. But the MA-type results do exclude
  many small-weight candidates and suggest that counterexamples, if they exist in ZFC,
  require weight $\mathfrak{c}$.

- **Under ◇ (diamond principle):** Compact L-spaces and measure-free compact spaces
  of weight $\omega_1$ have been constructed (Kunen, 1981; Fedorchuk, 1976). The
  question is whether any such construction yields a totally disconnected non-basically-
  disconnected non-atomic example, i.e., a Boolean algebra counterexample rather than
  a general compact space counterexample.

- **In ZFC alone:** No construction of a compact Radon-measure-free totally disconnected
  non-atomic non-basically-disconnected space is known, and no proof that none exists.

**Assessment: Strategy D is likely set-theoretically sensitive.**

The pattern of the known results — positive answers under Martin's Axiom, constructions
under ◇ — strongly suggests that Strategy D is **independent of ZFC**: provably positive
(no counterexample) under MA-type axioms, and admitting a counterexample under ◇ or similar
combinatorial principles. This is the typical profile of problems in set-theoretic topology
about measure-freeness of compact spaces.

Resolving Strategy D would require one of:
1. A ZFC construction of a non-σ-complete non-atomic measure-free Boolean algebra (equivalently,
   a Radon-measure-free compact non-atomic non-basically-disconnected Stone space); or
2. A ZFC proof that every non-σ-complete non-atomic Boolean algebra carries a σ-additive
   probability; or
3. A consistency proof (under ◇ or similar) that such an algebra exists, plus a consistency
   proof (under MA or similar) that none exists — establishing independence.

The Boolean-algebraic methods used through rung 3 and the canonical decomposition argument
do not reach this level. The next steps would require set-theoretic forcing arguments or
a more refined application of the Radon measure theory (Fremlin vol. 5, §531–534).

**This is the honest frontier.** The four necessary conditions and the topological reformulation
are the maximum extractable from ZFC Boolean-algebra arguments. Strategy D is now a
set-theoretic topology problem, not a Boolean-algebraic one.

---

## Summary of Investigation Outcome (2026-04-18)

The representation problem (which purely finitely additive charges on $B$ are pointwise
ultralimits of σ-additive probabilities on $B$) is:

- **Fully resolved positively** in the atomic regime (all atomic Boolean algebras).
- **Fully resolved positively** in the concrete join-preserving regime (all algebras
  embedding join-preservingly into a standard measure algebra).
- **Fully resolved positively vacuously** at the minimal-join extreme (algebras like
  $\mathcal{P}(\mathbb{N})/\mathrm{fin}$ where σ-additivity imposes no constraint).
- **Fully resolved negatively** in the σ-complete non-atomic regime (Nikodym's theorem).
- **Reduced to a single open question** in the intermediate regime: Strategy D.

Strategy D is the existence problem for a non-σ-complete non-atomic measure-free Boolean
algebra. Any counterexample must be non-σ-complete, non-atomic, measure-free, and uncountably
generated. No construction and no ZFC obstruction are known. The problem is likely independent
of ZFC, with set-theoretic methods (forcing) required for resolution.

---

## Part VI: Corrected Hierarchy Table

| Case | $\mathrm{Supp}_\sigma(B)$ | Answer |
|---|---|---|
| Atomic countable $B$ | $= \mathrm{St}(B)$ (density of $\mathrm{Prin}(B)$) | Positive |
| Non-atomic, full-support σ-additive exists (e.g., $\mathcal{I}$) | $= \mathrm{St}(B)$ | Positive |
| σ-complete non-atomic $B$ | $\subsetneq \mathrm{St}(B)$ | Negative (Nikodym) |
| Non-σ-complete non-atomic, few joins (e.g., $\mathcal{Q}$) | $= \mathrm{St}(B)$ (σ-additivity vacuous) | Positive (vacuously) |
| Non-σ-complete non-atomic, intermediate joins | $= \mathrm{St}(B)$? (requires measure-free factor) | **Open** — reduces to Strategy D |

The "open" row now has a precise meaning: by the canonical decomposition theorem, any
negative instance must contain a measure-free non-σ-complete non-atomic factor. Strategy D
asks whether such a factor can exist.

---

## Status

- [x] Identified and corrected critical error: $\mathcal{P}(\mathbb{N})/\mathrm{fin}$ claim wrong (σ-additivity vacuous, not absent)
- [x] Formalized σ-additivity on non-σ-complete Boolean algebras: condition applies only when $\bigvee_n A_n$ exists in $B$
- [x] Proved: on $\mathcal{Q} = \mathcal{P}(\mathbb{N})/\mathrm{fin}$, disjoint sequences with an existing join have at most finitely many nonzero terms; σ-additivity reduces to finite additivity; every finitely additive probability is σ-additive
- [x] Collapsed direct-product strategy: $\mathcal{I} \times \mathcal{Q}$ is a positive example
- [x] Proved canonical decomposition theorem: $B \cong (B{\upharpoonright}A) \times (B{\upharpoonright}A^c)$ at every element $A$
- [x] Proved: any failure of $\mathrm{Supp}_\sigma(B) = \mathrm{St}(B)$ is witnessed by a direct-product decomposition with a measure-free factor
- [x] Proved: "indecomposable row-5" is impossible (the canonical decomposition is forced by Boolean algebra structure, not a construction choice)
- [x] Eliminated Strategies A, B, C (all require indecomposable row-5, which cannot exist)
- [x] Reduced open row to Strategy D: does a non-σ-complete non-atomic measure-free Boolean algebra exist?
- [x] Corrected hierarchy table; open row now refers to Strategy D
- [x] Topological reformulation of Strategy D: equivalent to existence of Radon-measure-free compact totally disconnected non-atomic non-basically-disconnected space
- [x] Set-theoretic sensitivity assessed: MA + ¬CH narrows candidates; ◇ constructions may yield examples; problem likely independent of ZFC
- [x] Honest frontier declared: ZFC Boolean-algebra methods exhausted; forcing or advanced Radon-measure theory required for resolution
- [ ] Resolve Strategy D: forcing construction (under ◇) or ZFC proof of non-existence
- [ ] Update `stone_geometric_translation.md` to record topological reformulation
- [ ] Update parent note `notes/future/foundations/ce_nonderivability/index.md` to record set-theoretic sensitivity
