---
name: CE non-derivability — general Boolean algebra version
description: Future note — generalising Prop 3.9 from query-system language to first-order Boolean algebras with finitely additive probability; safe target is a metatheorem that countable additivity is not first-order in that language
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

The natural question is whether this non-derivability result holds at a strictly
more general level — in the first-order language of Boolean algebras equipped with
a finitely additive probability, independent of any query-system structure.

---

## The general language

Let the language contain:

- Boolean operations: $\wedge, \vee, \neg, 0, 1$
- A function or predicate coding a finitely additive probability:
  either a function symbol $\mu : B \to [0,1]$, or relation symbols
  $\mu(a) \leq q$ and $\mu(a) \geq q$ for rational $q \in [0,1]$

The axioms of a Boolean probability algebra (finite additivity, normalization,
non-negativity) are first-order in this language.

---

## Safe target

**Metatheorem:** No first-order sentence in the language of Boolean probability
algebras implies countable additivity.

**Proof strategy:**

1. The finite probability algebras $(\mathcal{P}(n), \#/n)$ — powerset of an
   $n$-element set with normalized counting measure — are genuine $\sigma$-additive
   probability algebras satisfying every first-order sentence that holds in all of
   them.
2. Take a nonprincipal ultraproduct $\prod_\mathcal{U} (\mathcal{P}(n), \#/n)$
   over a nonprincipal ultrafilter $\mathcal{U}$ on $\mathbb{N}$.
3. By Łoś's theorem, the ultraproduct satisfies every first-order sentence true in
   all finite stages.
4. Construct internally a descending sequence $(A_k)$ with empty Boolean
   intersection but $\mu(A_k) = 1$ for all $k$ — witnessing failure of
   countable additivity. (This uses the hyperfinite/internal structure of the
   ultraproduct; the sequence is constructed externally and then shown to certify
   non-$\sigma$-additivity.)
5. Conclude: countable additivity is not first-order, since it fails in a model
   satisfying every first-order consequence of $\sigma$-additive algebras.

**Why this works:** Countable additivity requires quantification over countable
sequences — not available in first-order logic. Łoś preserves only first-order
sentences. So the ultraproduct can satisfy all first-order structure while failing
the infinitary condition.

---

## Relation to Paper I Prop 3.9

Paper I Prop 3.9 is the query-system-specific version: the finite-cofinite charge
arises as an ultraproduct of Dirac masses, witnesses CE failure, and no first-order
structural condition in the query-system language can block this.

The general metatheorem would *subsume* Prop 3.9 rather than merely parallel it:
the obstruction is not a feature of query-system language but of finitary first-order
structure as such.

**In the paper:** keep Prop 3.9 as stated (framework-specific, intrinsic to the
paper's own language). The general version belongs in a companion note or appendix,
with a sentence in §3.4 noting the result is not specific to query systems.

---

## Ambitious target (separate, deferred)

**Classification question:** Which purely finitely additive charges arise as
ultraproducts or ultralimits of $\sigma$-additive probabilities?

This is a much stronger representation statement. It may be true in some form, or
only after allowing approximating nets rather than literal ultraproducts. Do not
assume without proof. The non-derivability metatheorem needs only *one* witness
(which the finite-$\mathcal{P}(n)$ construction provides); the classification is
a separate project.

---

## Key references

- Łoś's theorem: the standard ultraproduct transfer theorem for first-order sentences
- Yosida–Hewitt decomposition: every finitely additive probability = $\sigma$-additive
  part + purely finitely additive part; CE $\Leftrightarrow \ell_p = 0$
- Ultrafilter measures as standard examples of purely finitely additive probabilities
  on Boolean algebras
- Keisler, *The Ultraproduct Construction* — standard reference for Łoś
- arXiv:2503.08910 — recent survey on finitely additive measures on Boolean algebras;
  closest contemporary treatment of extension criteria in this language

---

## Recommended next step

Write down the exact language and prove:

$$\text{countable additivity is not first-order in Boolean algebras with probability charge.}$$

That is the mathematical core. Once that is clean, the connection to Paper I can be
stated as a one-paragraph note in §3.4 or an appendix.
