---
name: CE non-derivability — general Boolean algebra version
description: Future note — metatheorem that countable additivity is not first-order axiomatizable in the language of Boolean algebras with finitely additive probability; complete proof via ultraproduct of Dirac masses on finite-cofinite algebra; subsumes Paper I Prop 3.9
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

## Language $\mathcal{L}_{\mathrm{BA},\mu}$

One-sorted first-order language with:

- **Boolean operations:** $\wedge, \vee, \neg, 0, 1$
- **Rational comparison predicates:** for each $q \in [0,1] \cap \mathbb{Q}$,
  unary predicate symbols $P_{\leq q}(x)$ and $P_{\geq q}(x)$

**Interpretation:** $P_{\leq q}(a)$ means $\mu(a) \leq q$; $P_{\geq q}(a)$ means
$\mu(a) \geq q$. This avoids a two-sorted language with a numeric sort.

**What is first-order in $\mathcal{L}_{\mathrm{BA},\mu}$:**

- Boolean algebra axioms (all standard identities)
- Normalization: $\mu(0) = 0$, $\mu(1) = 1$
- Order compatibility: $a \leq b \Rightarrow \mu(a) \leq \mu(b)$
- Rational consistency: $p < q \Rightarrow (P_{\leq p}(a) \Rightarrow P_{\leq q}(a))$, etc.
- Finite additivity: for each rationals $r, s, t$ with $t = r + s$,
  $a \wedge b = 0 \wedge \mu(a) = r \wedge \mu(b) = s \Rightarrow \mu(a \vee b) = t$

The class of Boolean algebras with normalized finitely additive probability is
**first-order axiomatizable** in $\mathcal{L}_{\mathrm{BA},\mu}$.

**What is not first-order:** Countable additivity requires quantification over
a countable sequence $(a_n)_{n \in \mathbb{N}}$ — not available in first-order
logic. So countable additivity is not a sentence of $\mathcal{L}_{\mathrm{BA},\mu}$.

---

## The theorem

> **Proposition.** Let $\mathcal{L}_{\mathrm{BA},\mu}$ be the first-order language
> of Boolean algebras together with rational comparison predicates for a normalized
> finitely additive probability. Then countable additivity is not first-order
> axiomatizable in $\mathcal{L}_{\mathrm{BA},\mu}$.

Equivalently: there is no set $T$ of $\mathcal{L}_{\mathrm{BA},\mu}$-sentences such
that $(B, \mu) \models T$ if and only if $\mu$ is countably additive.

---

## Proof

**Step 1.** Let $E$ be the Boolean algebra of finite-cofinite subsets of $\mathbb{Q}$.
Fix an enumeration $q : \mathbb{N} \to \mathbb{Q}$ and let $\delta_n$ be the Dirac
measure at $q(n)$. Each $(E, \delta_n)$ is an $\mathcal{L}_{\mathrm{BA},\mu}$-structure
in which $\delta_n$ is countably additive.

**Step 2.** Let $\mathcal{U}$ be a nonprincipal ultrafilter on $\mathbb{N}$ extending
the cofinite filter. For each $A \in E$, define
$$\ell(A) := \lim_\mathcal{U} \delta_n(A) = \lim_\mathcal{U} \mathbf{1}_{q(n) \in A}.$$
If $A$ is finite, $q(n) \in A$ for only finitely many $n$, so $\ell(A) = 0$.
If $A$ is cofinite, $q(n) \in A$ for cofinitely many $n$, so $\ell(A) = 1$ since
$\mathcal{U}$ extends the cofinite filter. Thus $\ell$ is the finite-cofinite charge.

**Step 3.** The sequence $A_m = \mathbb{Q} \setminus \{q(0), \ldots, q(m)\}$
satisfies $A_0 \supseteq A_1 \supseteq \cdots$ and $\bigcap_m A_m = \varnothing$,
but $\ell(A_m) = 1$ for all $m$. So $\ell$ is not countably additive.

**Step 4.** If countable additivity were first-order axiomatizable, Łoś's theorem
would imply that the ultraproduct of the $(E, \delta_n)$ — which carries the charge
$\ell$ on the diagonal copy of $E$ — is again countably additive. This contradicts
Step 3. Therefore countable additivity is not first-order axiomatizable. $\square$

**Subtlety.** For complete model-theoretic precision: the ultraproduct is another
$\mathcal{L}_{\mathrm{BA},\mu}$-structure; the charge $\ell$ is induced on the
diagonal copy of $E$ inside it. Phrasing it as "the ultraproduct induces the
finite-cofinite charge on the diagonal copy of $E$" avoids any quibble about
whether the ultraproduct is literally $(E, \ell)$ versus an elementary extension
carrying the same ultralimit charge. For an informal note, the shorter phrasing
is fine.

---

## Relation to Paper I Prop 3.9

Paper I Prop 3.9 is the query-system-specific version: the same Dirac-mass
ultraproduct argument runs inside the query-system language and shows no first-order
structural condition in that language can imply CE.

This proposition subsumes it: the obstruction is not a feature of query-system
language specifically, but of any finitary first-order description of Boolean
probability algebras. CE is non-derivable not merely from the structural axioms of
query systems, but from first-order algebraic description as such.

**In the paper:** keep Prop 3.9 as stated — it is the framework-intrinsic version.
This broader statement belongs in a companion note or appendix, with at most one
sentence in §3.4 noting the result is not specific to query systems.

---

## Ambitious target (separate, deferred)

**Classification question:** Which purely finitely additive charges arise as
ultraproducts or ultralimits of $\sigma$-additive probabilities?

The present proof needs only one witness (the Dirac-mass construction provides it).
The classification is a separate project.

---

## Key references

- Łoś's theorem: ultraproduct transfer theorem for first-order sentences;
  Keisler, *The Ultraproduct Construction*
- Yosida–Hewitt: finitely additive probability = $\sigma$-additive part + purely
  finitely additive part; CE $\Leftrightarrow \ell_p = 0$
- arXiv:2503.08910 — recent survey on finitely additive measures on Boolean algebras
