---
name: Finite-cofinite algebra — ultralimit representation calculation
description: Priority 2 working note — classify all finitely additive probabilities on the finite-cofinite algebra; determine which are ultralimits of σ-additive probabilities on the same algebra
type: project
---

# The Finite-Cofinite Algebra: Ultralimit Representation

*Working note for Priority 2 of the ultralimit representation investigation.*
*Parent: `notes/future/ce_nonderivability_general.md`*

---

## Setup

Let $\mathbb{N}$ carry the **finite-cofinite algebra**
$$
\mathcal{E} = \{ A \subseteq \mathbb{N} : A \text{ is finite or } A^c \text{ is finite} \}.
$$
This is the canonical example throughout the investigation: it is the minimal
Boolean algebra on a countably infinite set that is not a $\sigma$-algebra, and
it is exactly the setting where the Nikodym obstruction disappears.

---

## Step 1: Classify all normalized finitely additive probabilities on $\mathcal{E}$

**Claim.** Every normalized finitely additive probability $\mu : \mathcal{E} \to [0,1]$
is of the form
$$
\mu = (1-t)\,\delta_F + t\,\ell_{\mathrm{fc}},
$$
where $F \subseteq \mathbb{N}$ is finite, $\delta_F$ is a convex combination of
Dirac masses at points of $F$ (or $\delta_F = 0$ if $F = \emptyset$), $t \in [0,1]$,
and $\ell_{\mathrm{fc}}$ is the finite-cofinite charge ($\ell_{\mathrm{fc}}(A) = 0$
if $A$ finite, $1$ if $A$ cofinite).

More precisely:

**Structure theorem for $\mathcal{E}$.** Every normalized finitely additive
probability $\mu$ on $\mathcal{E}$ is uniquely determined by:

- its value $\mu(\{n\}) \geq 0$ for each $n \in \mathbb{N}$ (finitely many nonzero),
- and its value on cofinite sets, which is forced by:
  $\mu(A^c) = 1 - \mu(A)$ for finite $A$.

**Proof sketch.**
Every element of $\mathcal{E}$ is either finite or cofinite. If $A$ is finite,
$\mu(A) = \sum_{n \in A} \mu(\{n\})$ by finite additivity, since singletons are
disjoint and their union is $A$. If $A$ is cofinite, $\mu(A) = 1 - \mu(A^c)$
where $A^c$ is finite. So $\mu$ is completely determined by the sequence
$(\mu(\{n\}))_{n \in \mathbb{N}}$.

The constraint is: $\sum_{n \in \mathbb{N}} \mu(\{n\}) \leq 1$ (since any finite
sub-sum is bounded by $\mu(\mathbb{N}) = 1$). Let $t = 1 - \sum_n \mu(\{n\})
\in [0,1]$.

- If $t = 0$: $\mu$ is a countable convex combination of Dirac masses, hence
  $\sigma$-additive. (These are exactly the $\sigma$-additive probabilities on
  $\mathcal{E}$, since $\sigma(\mathcal{E}) = \mathcal{P}(\mathbb{N})$ and any
  $\sigma$-additive probability on $\mathcal{E}$ extends uniquely to $\mathcal{P}(\mathbb{N})$.)
- If $t > 0$: $\mu$ has a purely finitely additive component of mass $t$,
  concentrated on the "cofinite part." Specifically,
  $\mu = \sum_n \mu(\{n\}) \delta_n + t \cdot \ell_{\mathrm{fc}}$,
  where $\ell_{\mathrm{fc}}$ is the unique normalized purely finitely additive
  probability on $\mathcal{E}$ (the finite-cofinite charge).

**Observation.** The finite-cofinite charge $\ell_{\mathrm{fc}}$ is the *unique*
purely finitely additive probability on $\mathcal{E}$ (up to normalization). This
follows because the purely finitely additive part must vanish on all singletons,
and on $\mathcal{E}$ the only such normalized charge is $\ell_{\mathrm{fc}}$.

So: $\mathrm{pfa}(\mathcal{E})$ is one-dimensional, spanned by $\ell_{\mathrm{fc}}$.

---

## Step 2: Which charges are free / purely finitely additive?

**Definition.** A charge $\mu$ on $\mathcal{E}$ is:
- **$\sigma$-additive** iff $t = 0$, i.e., $\mu = \sum_n \mu(\{n\})\delta_n$
  with $\sum_n \mu(\{n\}) = 1$.
- **Purely finitely additive** iff $t = 1$, i.e., $\mu(\{n\}) = 0$ for all $n$.
  On $\mathcal{E}$, this forces $\mu = \ell_{\mathrm{fc}}$.
- **Free** (assigns zero to all finite sets) iff $\mu(\{n\}) = 0$ for all $n$,
  same condition. So on $\mathcal{E}$: free $\Leftrightarrow$ purely finitely additive
  $\Leftrightarrow$ $\mu = \ell_{\mathrm{fc}}$.
- **Mixed** ($0 < t < 1$): has both a $\sigma$-additive part (atoms) and a
  purely finitely additive part.

**Key finding.** On the finite-cofinite algebra, there is only *one* free finitely
additive probability up to normalization: the finite-cofinite charge $\ell_{\mathrm{fc}}$
itself. The ladder's rung 2 therefore reduces to a single question:

> **Is $\ell_{\mathrm{fc}}$ a pointwise ultralimit of $\sigma$-additive probabilities on $\mathcal{E}$?**

---

## Step 3: σ-additive probabilities on $\mathcal{E}$

The $\sigma$-additive probabilities on $\mathcal{E}$ are exactly the countable
convex combinations $\mu = \sum_n p_n \delta_n$ with $p_n \geq 0$ and
$\sum_n p_n = 1$. These are discrete probability measures supported on $\mathbb{N}$.

On $\mathcal{E}$:
- For finite $A$: $\mu(A) = \sum_{n \in A} p_n$.
- For cofinite $A$: $\mu(A) = 1 - \sum_{n \in A^c} p_n$.

---

## Step 4: Can $\ell_{\mathrm{fc}}$ be a pointwise ultralimit of $\sigma$-additive probabilities on $\mathcal{E}$?

**The question.** Does there exist a sequence $(\mu_k)$ of $\sigma$-additive
probabilities on $\mathcal{E}$ and a nonprincipal ultrafilter $\mathcal{U}$ on
$\mathbb{N}$ such that
$$
\ell_{\mathrm{fc}}(A) = \lim_{\mathcal{U}} \mu_k(A) \quad \text{for all } A \in \mathcal{E}?
$$

**Unpacking the condition.** Write $\mu_k = \sum_n p_n^{(k)} \delta_n$ with
$\sum_n p_n^{(k)} = 1$, $p_n^{(k)} \geq 0$.

The condition $\lim_\mathcal{U} \mu_k(A) = \ell_{\mathrm{fc}}(A)$ requires:
- For every finite $A$: $\lim_\mathcal{U} \sum_{n \in A} p_n^{(k)} = 0$.
  In particular, for each singleton $\{n\}$: $\lim_\mathcal{U} p_n^{(k)} = 0$.
- For every cofinite $A$: $\lim_\mathcal{U} \mu_k(A) = 1$.

The second condition follows from the first by complementation: if
$\lim_\mathcal{U} \mu_k(F) = 0$ for all finite $F$, then
$\lim_\mathcal{U} \mu_k(F^c) = \lim_\mathcal{U}(1 - \mu_k(F)) = 1$.

So the condition reduces to: **$\lim_\mathcal{U} p_n^{(k)} = 0$ for every fixed $n$.**

**Answer: YES.** $\ell_{\mathrm{fc}}$ is a pointwise ultralimit of $\sigma$-additive
probabilities on $\mathcal{E}$.

**Explicit construction.** Let $\mu_k = \frac{1}{k} \sum_{n=0}^{k-1} \delta_n$
(uniform on $\{0, 1, \ldots, k-1\}$). Then $p_n^{(k)} = \frac{1}{k}$ for $n < k$
and $p_n^{(k)} = 0$ for $n \geq k$.

For any fixed $n$: $p_n^{(k)} = \frac{1}{k} \to 0$ as $k \to \infty$. So for
any nonprincipal ultrafilter $\mathcal{U}$, $\lim_\mathcal{U} p_n^{(k)} = 0$
(since the sequence converges to $0$ in the ordinary sense, ultrafilter limit
agrees). Hence $\lim_\mathcal{U} \mu_k(F) = 0$ for every finite $F$, and
$\lim_\mathcal{U} \mu_k(A) = 1$ for every cofinite $A$.

This is just an ordinary sequential limit, so in fact we do not even need an
ultrafilter: $\mu_k \to \ell_{\mathrm{fc}}$ pointwise on $\mathcal{E}$ as
$k \to \infty$.

---

## Step 5: What about mixed charges?

Every charge $\mu = \sum_n p_n \delta_n + t \cdot \ell_{\mathrm{fc}}$ on
$\mathcal{E}$ ($t \in [0,1]$, $\sum_n p_n = 1-t$) is a pointwise ultralimit of
$\sigma$-additive probabilities on $\mathcal{E}$.

**Construction.** Let $\mu_k^{(t)} = (1-t) \cdot \mu_{\mathrm{atoms}} + t \cdot
\frac{1}{k}\sum_{n=0}^{k-1}\delta_n$, where $\mu_{\mathrm{atoms}} = \frac{1}{1-t}\sum_n p_n \delta_n$
(normalized). Each $\mu_k^{(t)}$ is $\sigma$-additive, and
$\lim_{k \to \infty} \mu_k^{(t)}(A) = \mu(A)$ for every $A \in \mathcal{E}$.

So **every** finitely additive probability on $\mathcal{E}$ is a pointwise
(sequential) limit of $\sigma$-additive probabilities on $\mathcal{E}$.

---

## Conclusion for rung 2

**On the finite-cofinite algebra, every finitely additive probability is a
pointwise sequential limit (hence pointwise ultralimit) of $\sigma$-additive
probabilities on the same algebra.**

This is a **positive** answer to rung 2.

The key structural reason: $\mathrm{pfa}(\mathcal{E})$ is one-dimensional
(spanned by $\ell_{\mathrm{fc}}$ alone), and $\ell_{\mathrm{fc}}$ is
approximated by the uniform measures $\frac{1}{k}\sum_{n<k}\delta_n$.
The approximation works because mass can be spread arbitrarily thinly over
the atom structure.

---

## Implications for rung 3 and beyond

**Why rung 3 is harder.** On a general Boolean algebra $B$, $\mathrm{pfa}(B)$
need not be one-dimensional, and purely finitely additive charges need not have
the simple "spread mass thinly" approximation available. The finite-cofinite
algebra is special because it has only one purely finitely additive probability,
and that one is visibly approximable.

**The real question for the next rung.** For a general Boolean algebra $B$ with
a rich $\mathrm{pfa}(B)$, the spreading construction need not work. A first
candidate for a harder test case: a free Boolean algebra on $\omega_1$ generators,
or an algebra where purely finitely additive charges are parameterized by
non-principal ultrafilters in a more complex way.

**The βN reformulation (Priority 3).** In the βN picture, the result says: every
regular Borel measure on $\mathrm{St}(\mathcal{E}) = \beta\mathbb{N}$ is a weak
limit of measures supported on the principal points $\mathbb{N} \subset \beta\mathbb{N}$.
That is just weak* density of finitely supported measures in all Borel measures on
$\beta\mathbb{N}$, which is standard. So the finite-cofinite case in the βN language
is trivial — confirming that the interesting question begins with algebras where
$\mathrm{pfa}(B)$ is genuinely multidimensional.

---

## Status

- [x] Classify all finitely additive probabilities on $\mathcal{E}$
- [x] Identify free / purely finitely additive charges (unique: $\ell_{\mathrm{fc}}$)
- [x] Characterize $\sigma$-additive probabilities on $\mathcal{E}$
- [x] Determine ultralimit representability: **YES, positive answer**
- [ ] Identify next test case beyond the finite-cofinite algebra
- [ ] Translate positive result into βN / Stone language explicitly
- [ ] Determine whether the positive answer extends to larger / richer Boolean algebras
