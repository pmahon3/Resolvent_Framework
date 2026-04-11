---
name: CE non-derivability — general Boolean algebra version
description: Future note — metatheorem that countable additivity is not first-order in the language of Boolean algebras with finitely additive probability; proof via ultraproduct of Dirac masses on finite-cofinite algebra; subsumes Paper I Prop 3.9
type: project
---

# CE Non-Derivability: General Boolean Algebra Version

**Status:** Research direction. Not in the current four-paper arc. Revisit after arXiv submission.

---

## Context

Paper I, Proposition 3.9 proves that no first-order structural condition in the
language of query systems can imply CE. The mechanism is Łoś: ultraproducts of
Dirac masses produce the finite-cofinite charge, which is purely finitely additive
and fails CE.

The natural generalisation is whether this holds at a strictly more general level —
in the first-order language of Boolean algebras equipped with a finitely additive
probability, independent of any query-system structure. The answer is yes, and the
proof stays close to the existing argument.

---

## The language $\mathcal{L}_\mu$

One-sorted first-order language with:

- **Boolean operations:** $\wedge, \vee, \neg, 0, 1$
- **Rational comparison predicates:** for each $q \in [0,1] \cap \mathbb{Q}$, relation
  symbols $R_{\leq q}(a)$ and $R_{\geq q}(a)$, interpreted as $\mu(a) \leq q$ and
  $\mu(a) \geq q$

**Why Option B (predicates) over Option A (function symbol into $[0,1]$):**
Staying one-sorted and using rational comparison predicates avoids a two-sorted
language with structure on the number sort. It is the cleaner first-order setting.

**What is first-order in $\mathcal{L}_\mu$:**

- Boolean algebra axioms: all standard Boolean identities
- Normalization: $\mu(0) = 0$, $\mu(1) = 1$ (via predicates)
- Finite additivity: for disjoint $a, b$, $\mu(a \vee b) = \mu(a) + \mu(b)$
  (encoded by rational inequalities for all rationals simultaneously)

The class of Boolean algebras with finitely additive probability is
**first-order axiomatizable** in $\mathcal{L}_\mu$. This is the key starting point.

**What is not first-order:**
Countable additivity requires quantification over an entire countable sequence
$(a_n)_{n \in \mathbb{N}}$ — not available in first-order logic, which can only
quantify over finitely many variables at a time. So countable additivity is not a
first-order sentence in $\mathcal{L}_\mu$.

---

## The metatheorem

> **Theorem.** In the first-order language $\mathcal{L}_\mu$ of Boolean algebras
> with normalized finitely additive probability, countable additivity is not
> first-order axiomatizable. Equivalently, no first-order sentence $\Phi$ in
> $\mathcal{L}_\mu$ is satisfied by exactly the countably additive models.

This is a metatheorem: a theorem *about* the expressive limitations of
$\mathcal{L}_\mu$, not a sentence *in* $\mathcal{L}_\mu$.

---

## Proof strategy (clean version, close to Paper I)

**Step 1 — Łoś's theorem as the engine.**
Any first-order sentence true in each factor of an ultraproduct is true in the
ultraproduct. So if countable additivity were first-order, an ultraproduct of
countably additive probability algebras would be countably additive.

**Step 2 — Build a bad ultraproduct from good Dirac masses.**
Take the Boolean algebra $\mathcal{E}$ of finite-cofinite subsets of $\mathbb{Q}$.
Fix an enumeration $q : \mathbb{N} \to \mathbb{Q}$ and let $\delta_n$ be the Dirac
mass at $q(n)$. Each $(\mathcal{E}, \delta_n)$ is a countably additive probability
algebra satisfying every $\mathcal{L}_\mu$ sentence.

Let $\mathcal{U}$ be a nonprincipal ultrafilter on $\mathbb{N}$ extending the
cofinite filter. The ultraproduct $\prod_\mathcal{U} (\mathcal{E}, \delta_n)$
assigns to $E \subseteq \mathbb{Q}$:
$$\ell(E) = \lim_\mathcal{U} \mathbf{1}_{q(n) \in E}$$
- If $E$ is finite: $q(n) \in E$ for finitely many $n$, so ultralimit is $0$
- If $E$ is cofinite: $q(n) \in E$ for cofinitely many $n$, so ultralimit is $1$
  (since $\mathcal{U}$ extends the cofinite filter)

The ultraproduct is therefore the finite-cofinite charge $\ell$ — finitely additive,
not countably additive.

**Step 3 — Conclude.**
By Step 1, any first-order $\Phi$ satisfied by all $(\mathcal{E}, \delta_n)$ is
satisfied by their ultraproduct $(\mathcal{E}, \ell)$. But $\ell$ is not countably
additive. Therefore no first-order sentence can imply countable additivity.

**Note:** This argument does not need the $(\mathcal{P}(n), \#/n)$ family or
nonstandard analysis machinery. The Dirac-mass construction stays entirely within
the finite-cofinite algebra and is the cleanest route. The tail-set construction
in $\mathcal{P}(n)$ works but requires more care about whether the intersection of
tail sets is truly zero in the raw ultraproduct (it is not, without Loeb completion).
Avoid that route.

---

## Why this subsumes Paper I Prop 3.9

Paper I Prop 3.9 is the query-system-specific version: the finite-cofinite charge
arises as an ultraproduct of Dirac masses within the query-system framework, and no
first-order structural condition in the query-system language can block this.

The general metatheorem subsumes it: the obstruction is not a feature of
query-system language specifically, but of any finitary first-order description of
Boolean probability algebras. CE is non-derivable not merely from the structural
axioms of query systems, but from first-order algebraic description as such.

**In the paper:** keep Prop 3.9 as stated — it is the framework-intrinsic version
and belongs there. The general version belongs in a companion note or appendix, with
at most one sentence in §3.4 noting the result is not specific to query systems.

---

## Ambitious target (separate, deferred)

**Classification question:** Which purely finitely additive charges arise as
ultraproducts or ultralimits of $\sigma$-additive probabilities?

This is a much stronger representation statement. The non-derivability metatheorem
needs only *one* witness (the Dirac-mass construction provides it). The
classification is a separate project — possibly true in some form, possibly
requiring nets rather than literal ultraproducts.

---

## Key references

- Keisler, *The Ultraproduct Construction* — standard reference for Łoś's theorem
- Yosida–Hewitt: finitely additive probability = $\sigma$-additive part + purely
  finitely additive part; CE $\Leftrightarrow \ell_p = 0$
- arXiv:2503.08910 — recent survey on finitely additive measures on Boolean algebras;
  closest contemporary treatment in this language
- Ultrafilter measures as canonical examples of purely finitely additive probabilities
