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
  unary predicate symbols $M_{\leq q}(x)$ and $M_{\geq q}(x)$

**Interpretation:** $M_{\leq q}(a)$ means $\mu(a) \leq q$; $M_{\geq q}(a)$ means
$\mu(a) \geq q$. This avoids a two-sorted language with a numeric sort.

**What is first-order in $\mathcal{L}_{\mathrm{BA},\mu}$:**

- Boolean algebra axioms (all standard identities)
- Normalization: $\mu(0) = 0$, $\mu(1) = 1$
- Order compatibility: $a \leq b \Rightarrow \mu(a) \leq \mu(b)$
- Rational consistency: $p < q \Rightarrow (M_{\leq p}(a) \Rightarrow M_{\leq q}(a))$, etc.
- Finite additivity: for each rationals $r, s, t$ with $t = r + s$,
  $a \wedge b = 0 \wedge M_{=r}(a) \wedge M_{=s}(b) \Rightarrow M_{=t}(a \vee b)$
  (where $M_{=q}$ abbreviates $M_{\leq q} \wedge M_{\geq q}$)

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

Let $E$ be the finite-cofinite Boolean algebra on a countably infinite set, and let
$\delta_n$ be the Dirac charges at an enumeration $q : \mathbb{N} \to \mathbb{Q}$ of
that set. Each $\delta_n$ is countably additive. For a nonprincipal ultrafilter
$\mathcal{U}$ extending the cofinite filter, the ultralimit
$$\ell(A) = \lim_\mathcal{U} \delta_n(A) = \lim_\mathcal{U} \mathbf{1}_{q(n) \in A}$$
is the finite-cofinite charge: $\ell(A) = 0$ for finite $A$ and $\ell(A) = 1$ for
cofinite $A$. This charge is finitely additive but not countably additive — the
sequence $A_k = \mathbb{Q} \setminus \{q(0), \ldots, q(k)\}$ satisfies
$\bigcap_k A_k = \varnothing$ but $\ell(A_k) = 1$ for all $k$. Since first-order
properties are preserved under ultraproducts by Łoś's theorem, countable additivity
cannot be first-order axiomatizable. $\square$

**Model-theoretic note.** The ultraproduct of the $(E, \delta_n)$ is another
$\mathcal{L}_{\mathrm{BA},\mu}$-structure; $\ell$ is the charge induced on the
diagonal copy of $E$ inside it. For an informal note, identifying the ultraproduct
with $(E, \ell)$ is fine; for full precision, say "the ultraproduct induces the
finite-cofinite charge on the diagonal copy of $E$."

---

## Corollary: CE is not first-order

Replacing "countably additive" by "satisfies CE" (equivalently, extends to a
$\sigma$-additive measure on the generated $\sigma$-algebra) gives:

> **Corollary.** In the first-order language $\mathcal{L}_{\mathrm{BA},\mu}$, no
> first-order condition implies the extension property characterised by CE.

The proof is identical: the finite-cofinite charge witnesses CE failure, and it
arises as an ultraproduct of CE-satisfying (in fact $\sigma$-additive) charges.

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
