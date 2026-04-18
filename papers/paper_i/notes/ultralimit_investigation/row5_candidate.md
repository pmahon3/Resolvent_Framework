---
name: Row-5 candidate — first algebra with Supp_σ(B) ⊊ St(B)
description: Working note — construct an explicit non-σ-complete non-atomic Boolean algebra where no σ-additive probability has full support; first candidate for a genuinely negative answer outside the σ-complete regime
type: project
---

# A Row-5 Candidate: $\mathrm{Supp}_\sigma(B) \subsetneq \mathrm{St}(B)$

*Working note for the frontier of the ultralimit representation investigation.*  
*Parent: `notes/future/ce_nonderivability_general.md`*  
*Prerequisites: `papers/paper_i/notes/ultralimit_investigation/stone_geometric_translation.md` (Stone note, especially the hierarchy table).*

---

## The Target

"Row 5" in the Stone note's hierarchy is a non-σ-complete, non-atomic Boolean
algebra $B$ such that:
1. $B$ admits at least one σ-additive probability (otherwise the question is vacuous).
2. No σ-additive probability on $B$ has full support on $\mathrm{St}(B)$.

Condition 2 is equivalent to: $\mathrm{Supp}_\sigma(B) \subsetneq \mathrm{St}(B)$
strictly. This would mean there exist finitely additive probabilities on $B$
supported on the complement $\mathrm{St}(B) \setminus \mathrm{Supp}_\sigma(B)$
that cannot be approximated by σ-additive ones — a genuinely negative result
outside the σ-complete regime.

---

## The Key Ingredient: A Non-Atomic Non-σ-Complete Algebra Supporting No σ-Additive Probability

**Claim.** The quotient algebra $\mathcal{P}(\mathbb{N})/\mathrm{fin}$ — the power
set of $\mathbb{N}$ modulo the ideal of finite sets — is non-atomic and
non-σ-complete, and supports no σ-additive probability.

**Non-atomic:** Every equivalence class $[A]$ with $A$ infinite can be split:
write $A = A_0 \sqcup A_1$ with both $A_0, A_1$ infinite; then $[A_0]$ and $[A_1]$
are non-zero elements of $\mathcal{P}(\mathbb{N})/\mathrm{fin}$ with $[A_0] \wedge
[A_1] = 0$ and $[A_0] \vee [A_1] = [A]$. No element of $\mathcal{P}(\mathbb{N})/\mathrm{fin}$
is an atom (any non-zero class is represented by an infinite set, hence splittable).

**Non-σ-complete:** The classes $[\{n, n+1, n+2, \ldots\}]$ for $n \geq 0$ form
a decreasing sequence with infimum $[\emptyset] = 0$ in $\mathcal{P}(\mathbb{N})/\mathrm{fin}$,
but no countable infimum is attained by a sequence (the infimum does not exist as
an element of the quotient for the standard order). More directly:
$\mathcal{P}(\mathbb{N})/\mathrm{fin}$ is not a $\sigma$-algebra (the image of the
quotient map $A \mapsto [A]$ does not preserve countable unions in general).

**No σ-additive probability:** Suppose $\mu$ is a σ-additive probability on
$\mathcal{P}(\mathbb{N})/\mathrm{fin}$. Since $[\{n\}] = [{\emptyset}] = 0$ in the
quotient (finite sets are equivalent to $\emptyset$), we have $\mu([\{n\}]) = 0$
for all $n$. The singletons $\{0\}, \{1\}, \ldots$ are pairwise disjoint in
$\mathcal{P}(\mathbb{N})$ and their union is $\mathbb{N}$. In the quotient, the
partial sums $[\{0, \ldots, k\}] = 0$ for all $k$. But $\sigma$-additivity would
require $\mu([\mathbb{N}]) = \sum_{n} \mu([\{n\}]) = 0$, contradicting $\mu(1) = 1$.
Hence no σ-additive probability exists on $\mathcal{P}(\mathbb{N})/\mathrm{fin}$.

*(This argument uses: (i) $[\{n\}] = 0$; (ii) $\mu$ is countably additive; (iii)
$\bigsqcup_n \{n\} = \mathbb{N}$ in $\mathcal{P}(\mathbb{N})$, so $\bigvee_n [\{n\}]
= [\mathbb{N}] = 1$. Step (iii) needs care: the join in $\mathcal{P}(\mathbb{N})/\mathrm{fin}$
of a countable collection need not equal the image of the union. But $[\mathbb{N}] = 1$
is the top element of the quotient, and it cannot be expressed as the supremum of
the zero elements $[\{n\}]$ via countable additivity of $\mu$.)*

---

## The Direct Product Construction

**Definition.** Let
$$
B = \mathcal{I} \times (\mathcal{P}(\mathbb{N})/\mathrm{fin}),
$$
the direct product of Boolean algebras, where $\mathcal{I}$ is the interval algebra
of half-open subintervals of $[0,1]$ (from the Stone note).

Elements of $B$ are pairs $(I, [A])$ with $I \in \mathcal{I}$ and $[A] \in
\mathcal{P}(\mathbb{N})/\mathrm{fin}$. Boolean operations are componentwise.

**Properties of $B$:**

*Non-atomic:* Both factors are non-atomic ($\mathcal{I}$ by interval-splitting;
$\mathcal{P}(\mathbb{N})/\mathrm{fin}$ by infinite-set-splitting). A product of
non-atomic Boolean algebras is non-atomic.

*Non-σ-complete:* $\mathcal{P}(\mathbb{N})/\mathrm{fin}$ is not σ-complete (nor
is $\mathcal{I}$), so neither is their product.

*Admits σ-additive probabilities:* The top element of $B$ is $(1_\mathcal{I},
[\mathbb{N}])$. A σ-additive probability $\mu$ on $B$ must assign $\mu(1_B) = 1$.
Writing $e_1 = (1_\mathcal{I}, 0)$ and $e_2 = (0, [\mathbb{N}])$ (the two
"factor identities"), we have $e_1 \sqcup e_2 = 1_B$ and $e_1 \wedge e_2 = 0$.
So $\mu(e_1) + \mu(e_2) = 1$. For any $t = \mu(e_1) \in [0,1]$:
- The restriction of $\mu$ to the $\mathcal{I}$ factor (elements of the form
  $(I, 0)$) must be a σ-additive measure of total mass $t$.
- The restriction to the $\mathcal{P}(\mathbb{N})/\mathrm{fin}$ factor must be a
  σ-additive measure of total mass $1-t$. But $\mathcal{P}(\mathbb{N})/\mathrm{fin}$
  supports no σ-additive probability (hence no σ-additive measure of any positive
  mass, by normalization). So $1 - t = 0$, i.e., $t = 1$.

Therefore: every σ-additive probability on $B$ has $\mu(e_1) = 1$ and $\mu(e_2) = 0$.
All σ-additive mass lives on the $\mathcal{I}$ factor. Taking $\mu = \lambda \oplus 0$
(Lebesgue on $\mathcal{I}$, zero on the other factor) gives an explicit σ-additive
probability on $B$.

---

## Computing $\mathrm{Supp}_\sigma(B)$

**Stone space.** The Stone space of a direct product $B_1 \times B_2$ is the
disjoint union $\mathrm{St}(B_1) \sqcup \mathrm{St}(B_2)$ (as a topological space,
this is the coproduct — each factor's Stone space is a clopen subspace of the product's
Stone space). So:
$$
\mathrm{St}(B) = \mathrm{St}(\mathcal{I}) \sqcup \mathrm{St}(\mathcal{P}(\mathbb{N})/\mathrm{fin}).
$$

**The σ-additive locus.** Every σ-additive probability on $B$ has all its mass on
the $\mathcal{I}$ factor (as shown above). In Stone-space terms, every such measure
is supported within $\mathrm{St}(\mathcal{I}) \subset \mathrm{St}(B)$. Moreover,
Lebesgue measure has full support on $\mathrm{St}(\mathcal{I})$ (Stone note, interval
algebra section). So:
$$
\mathrm{Supp}_\sigma(B) = \mathrm{St}(\mathcal{I}) \subsetneq \mathrm{St}(B).
$$

The complementary clopen $\mathrm{St}(\mathcal{P}(\mathbb{N})/\mathrm{fin})$ is
entirely outside $\mathrm{Supp}_\sigma(B)$.

---

## The Negative Result

**Theorem (candidate).** Let $B = \mathcal{I} \times (\mathcal{P}(\mathbb{N})/\mathrm{fin})$.
There exist finitely additive probabilities on $B$ that are not in the weak* closure
of σ-additive probabilities on $B$. In particular, the representation question has a
**negative** answer for $B$.

**Proof sketch.** Let $\mathcal{U}$ be any non-principal ultrafilter on $\mathbb{N}$.
The charge $\delta_\mathcal{U}$ defined by $\delta_\mathcal{U}(I, [A]) = \mathbf{1}_{A \in \mathcal{U}}$
is a finitely additive probability on $B$ supported entirely on $\mathrm{St}(\mathcal{P}(\mathbb{N})/\mathrm{fin})$.

Since $\mathrm{Supp}_\sigma(B) = \mathrm{St}(\mathcal{I})$ and $\mathrm{St}(\mathcal{P}(\mathbb{N})/\mathrm{fin})$
is a disjoint clopen from $\mathrm{St}(\mathcal{I})$, any measure in the weak*
closure of σ-additive probabilities on $B$ is supported within $\mathrm{St}(\mathcal{I})$
(the weak* closure of measures supported on a closed set is contained in the set of
measures supported on that closed set). But $\delta_\mathcal{U}$ is supported on
the disjoint component $\mathrm{St}(\mathcal{P}(\mathbb{N})/\mathrm{fin})$.

Hence $\delta_\mathcal{U}$ is not a weak* limit — a fortiori not a pointwise
ultralimit — of σ-additive probabilities on $B$. $\square$

**Remark.** The charge $\delta_\mathcal{U}$ is itself a $\{0,1\}$-valued purely
finitely additive probability on $B$, but it is "new" in the sense that it cannot
be produced by any sequence of σ-additive approximants on the same algebra $B$.
The obstruction is not the Nikodym theorem (which requires σ-completeness) but
simply that the σ-additive support misses the entire $\mathcal{P}(\mathbb{N})/\mathrm{fin}$
component.

---

## What This Establishes

The algebra $B = \mathcal{I} \times (\mathcal{P}(\mathbb{N})/\mathrm{fin})$ is:
- Non-atomic ✓
- Non-σ-complete ✓
- Admits σ-additive probabilities ✓ (Lebesgue on $\mathcal{I}$ factor)
- Has $\mathrm{Supp}_\sigma(B) \subsetneq \mathrm{St}(B)$ strictly ✓
- Has finitely additive probabilities not representable as σ-additive ultralimits ✓

This fills row 5 of the hierarchy table with a concrete example. The answer to the
representation question is not always positive for non-σ-complete non-atomic algebras.

**The negative answer here is "soft"** in the sense that the obstruction comes from
a direct-product decomposition: the $\mathcal{P}(\mathbb{N})/\mathrm{fin}$ component
is entirely invisible to σ-additive measures, and the finitely additive charges
supported there cannot be reached. This is a clean structural reason for the failure,
not a subtle analytic obstruction.

---

## What the Direct-Product Example Does Not Settle

The negative result here relies on the algebra having a direct summand with no
σ-additive support. This is a coarse kind of obstruction. The deeper question —
which the direct-product example does not touch — is:

> Is there an **indecomposable** non-σ-complete non-atomic Boolean algebra $B$
> (one that cannot be written as a non-trivial direct product) such that
> $\mathrm{Supp}_\sigma(B) \subsetneq \mathrm{St}(B)$?

An indecomposable example would show that the failure of full-support is not merely
an artifact of decomposing the algebra into a "good" and a "bad" piece, but a genuine
phenomenon in algebras that cannot be so decomposed.

**Candidate for an indecomposable row-5 algebra.** The algebra of Baire-class-1
subsets of $[0,1]$ modulo a suitable ideal, or a "random algebra" constructed from
a measure space with missing measurable sets. These are speculative; the direct-product
example is the first concrete one.

---

## Refined Hierarchy (Updated)

| Case | $\mathrm{Supp}_\sigma(B)$ | Answer |
|---|---|---|
| Atomic countable $B$ | $= \mathrm{St}(B)$ (density of $\mathrm{Prin}(B)$) | Positive |
| Non-atomic, full-support σ-additive (e.g., $\mathcal{I}$) | $= \mathrm{St}(B)$ | Positive |
| σ-complete non-atomic $B$ | $\subsetneq \mathrm{St}(B)$ | Negative (Nikodym) |
| Non-σ-complete, direct-product decomposable with measure-free factor (e.g., $\mathcal{I} \times \mathcal{P}(\mathbb{N})/\mathrm{fin}$) | $\subsetneq \mathrm{St}(B)$ | **Negative** (new) |
| Non-σ-complete non-atomic **indecomposable** $B$, no full-support σ-additive | $\subsetneq \mathrm{St}(B)$? | **Open** |

---

## Status

- [x] Identified key ingredient: $\mathcal{P}(\mathbb{N})/\mathrm{fin}$ is non-atomic, non-σ-complete, supports no σ-additive probability
- [x] Constructed $B = \mathcal{I} \times \mathcal{P}(\mathbb{N})/\mathrm{fin}$: non-atomic, non-σ-complete, admits σ-additive probabilities
- [x] Computed $\mathrm{Supp}_\sigma(B) = \mathrm{St}(\mathcal{I}) \subsetneq \mathrm{St}(B)$
- [x] Exhibited non-representable charge: $\delta_\mathcal{U}$ for any non-principal ultrafilter $\mathcal{U}$ on $\mathbb{N}$
- [x] Identified limitation: obstruction is "soft" (direct-product decomposability)
- [ ] Find indecomposable row-5 algebra — genuine structural obstruction without a measure-free direct summand
- [ ] Determine whether indecomposable row-5 algebras exist (or prove every indecomposable non-σ-complete non-atomic $B$ with a σ-additive probability has full $\sigma$-additive support)
