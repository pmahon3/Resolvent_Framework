---
name: CE non-derivability — general Boolean algebra version
description: Future note — metatheorem that countable additivity is not first-order axiomatizable; plus full investigation of ultralimit representation of purely finitely additive charges
type: project
---

# CE Non-Derivability and the Ultralimit Representation Problem

*Extended 2026-04-17 to include literature findings and paper sketch*

---

## Part I: The Non-Axiomatizability Theorem (complete)

**Status:** Done. Written up as companion note (`ce_nonderivability_companion.tex`), targeting APAL.

The companion note proves: in the first-order language $\mathcal{L}_{\mathrm{BA},\mu}$ of Boolean algebras with normalized finitely additive charge, no first-order theory characterizes those models whose charge extends to a $\sigma$-additive measure. The proof is the Dirac-mass ultraproduct construction.

See `papers/paper_i/notes/ce_nonderivability_companion.tex` for the full proof.

---

## Part II: The Ultralimit Representation Problem (investigation underway)

### The Question

Given a purely finitely additive probability charge $\ell$ on a Boolean algebra $B$, does there exist a sequence $(\mu_n)$ of $\sigma$-additive probabilities on $B$ and a nonprincipal ultrafilter $\mathcal{U}$ such that
$$\ell(A) = \lim_{\mathcal{U}} \mu_n(A) \quad \forall A \in B?$$

This arises naturally from the companion note: the non-axiomatizability proof needs only *one* witness (the finite-cofinite charge), but the broader question is which purely finitely additive charges are ultralimits.

### Literature Findings (2026-04-17)

**Key sources checked:** Yosida–Hewitt (1952), Rao–Rao (1983), Duanmu–Weiss (2018), Cardona–Mejía–Uribe-Zapata (2025), Dunford–Schwartz (1958), Keisler (1985), Swierczynska (2024).

#### Case 1: σ-algebras — CLOSED (negative)

**Theorem (Nikodym/Vitali–Hahn–Saks):** If $(\mu_n)$ is a sequence of $\sigma$-additive probabilities on a $\sigma$-algebra $\Sigma$, then any pointwise ultralimit $\ell(A) = \lim_\mathcal{U} \mu_n(A)$ is itself $\sigma$-additive.

*Proof sketch:* For disjoint $(A_k)$ with union $A$: $\ell(A) = \lim_\mathcal{U} \mu_n(A) = \lim_\mathcal{U} \sum_k \mu_n(A_k) = \sum_k \lim_\mathcal{U} \mu_n(A_k) = \sum_k \ell(A_k)$, where the interchange holds because $\mu_n(A) = \sum_k \mu_n(A_k)$ exactly for each $n$.

**Consequence:** On a $\sigma$-algebra, no purely finitely additive charge is a pointwise ultralimit of $\sigma$-additive measures. This case is settled.

**Reference:** Dunford–Schwartz, *Linear Operators* I (1958), IV.9.8.

#### Case 2: General Boolean algebras — OPEN

The Nikodym obstruction does not apply when $B$ is merely a Boolean algebra (not $\sigma$-complete). No theorem in either direction appears in the literature. The finite-cofinite algebra is the canonical example of this setting.

**What is known:**
- Yosida–Hewitt (1952): establishes ba = ca ⊕ pfa (orthogonal decomposition) but does not address representation by limits
- Rao–Rao (1983): covers classification and extension, no approximation of pfa by ca
- Cardona–Mejía–Uribe-Zapata (2025): local (finite-partition) approximation of free finitely additive measures by uniform probabilities on finite sets; does **not** address global pointwise ultralimit representation
- Duanmu–Weiss (2018): on totally bounded separable metric spaces, every finitely additive Borel probability is a weak limit (bounded uniformly continuous test functions) of $\sigma$-additive probabilities; Example 5.14 shows setwise ultralimit approximation fails for ultrafilter charges on discrete sets

#### Case 3: Weak* approximation — a different question

Every purely finitely additive measure is an accumulation point (in the product topology on $[0,1]^B$) of finitely supported (hence $\sigma$-additive) measures (Seidenfeld, cited in Duanmu–Weiss). But this uses nets, not sequences or ultrafilter limits. Weak* limit ≠ pointwise ultralimit.

#### Case 4: The βN perspective

Every finitely additive probability on $\mathcal{P}(\mathbb{N})$ corresponds bijectively to a regular Borel measure on $\beta\mathbb{N}$ (Stone space). $\sigma$-additive charges ↔ measures supported on $\mathbb{N} \subset \beta\mathbb{N}$ (principal ultrafilters). Purely finitely additive charges ↔ measures supported on $\beta\mathbb{N} \setminus \mathbb{N}$.

Ultralimits of Dirac masses produce only {0,1}-valued ultrafilter charges — a proper subclass. General purely finitely additive charges (with values in $(0,1)$) are not of this form. The βN picture gives a clean geometric statement of the problem but does not resolve it.

### The Natural Ladder of Sub-Questions

1. **Ultrafilter-generated {0,1}-charges:** $\delta_\mathcal{U}(A) = \mathbf{1}_{A \in \mathcal{U}}$. Arise as ultralimits of Dirac masses. ✓ (finite-cofinite witness is of this type)

2. **Free finitely additive probabilities** (assigning zero to all finite sets): Cardona et al. give local approximation; global ultralimit representation unknown.

3. **General purely finitely additive probabilities:** Unknown. May depend on set-theoretic axioms (existence of certain ultrafilters, Ramsey-type properties).

4. **The full representation question:** Is every charge in pfa(B) an ultralimit of $\sigma$-additive charges on $B$? If not, what is the characterization of the representable ones?

### Key Distinctions

- **Fixed algebra vs varying algebra:** Fixed = same $B$ throughout. Varying = $\ell$ arises on a diagonal copy inside an ultraproduct of different $(B_n, \mu_n)$. These are different questions. The companion note uses the fixed-algebra setting.

- **Ultralimit vs ultraproduct:** Ultralimit keeps $B$ fixed and takes $\ell(A) = \lim_\mathcal{U} \mu_n(A)$. Ultraproduct produces a new structure with $\ell$ induced on a diagonal copy. The fixed-algebra ultralimit is the more natural first target.

- **Approximation vs exact representation:** Local finite-partition approximation (Cardona et al.) vs global pointwise ultralimit (the question here). Approximation holds more broadly.

---

## Part III: Paper Sketch

**Working title:** *Which Purely Finitely Additive Charges are Ultralimits of σ-Additive Probabilities?*

**Branch:** `paper-ultralimit-representation`

### Proposed structure

**§1 Introduction**
- State the representation question cleanly
- Motivation: arises from the non-axiomatizability proof; the Dirac-mass construction produces one witness, but which charges are representable?
- Summary of results (to be determined as investigation proceeds)

**§2 Background**
- Yosida–Hewitt decomposition: ba = ca ⊕ pfa
- Stone duality and the βN picture
- The Nikodym convergence theorem
- Key definitions: ultralimit, ultraproduct, fixed-algebra vs varying-algebra

**§3 The σ-Algebra Case: A Complete Obstruction**
- Theorem: on a σ-algebra, no pfa charge is a pointwise ultralimit of σ-additive measures
- Proof via Nikodym / Vitali–Hahn–Saks
- Corollary: the question is entirely about Boolean algebras (not σ-complete)

**§4 Ultrafilter-Generated Charges**
- Every {0,1}-valued pfa charge is an ultralimit of Dirac masses ✓
- Proof: the finite-cofinite construction generalizes
- βN interpretation: these are the "point masses" on βN \ N

**§5 Free Finitely Additive Measures**
- Cardona et al. local approximation result
- Question: can local approximation be upgraded to a global ultralimit?
- First test case: the uniform measure on an ultrafilter base

**§6 The General Case**
- Conjectural theorem or counterexample
- Possible connection to Ramsey theory / set-theoretic combinatorics
- Relationship to Lauwers (2010): pfa measures are non-constructive

**§7 Open Questions**
- Classification of representable charges
- Set-theoretic independence questions
- Connection to Keisler measures in model theory

### Claims to resolve (open)

- [ ] Is every free finitely additive probability an ultralimit of σ-additive probabilities on the same Boolean algebra?
- [ ] Is there a purely finitely additive charge on a Boolean algebra that is provably NOT an ultralimit?
- [ ] Does the βN picture give a characterization?
- [ ] Is the answer set-theoretically independent?

### References to add to bib

- Duanmu, H. and Weiss, W. (2018). Finitely-additive, countably-additive and internal probability measures. *Comment. Math. Univ. Carolin.* **59**(4), 467–485.
- Dunford, N. and Schwartz, J. T. (1958). *Linear Operators*, Part I. Interscience.
- Lauwers, L. (2010). Purely finitely additive measures are non-constructible objects. DPS 10.10, KU Leuven.
- Cardona, Mejía, Uribe-Zapata (2025). arXiv:2503.08910.

### Next steps

1. Prove or disprove: every free finitely additive probability on the finite-cofinite algebra is an ultralimit of σ-additive probabilities on that algebra.
2. Investigate the βN / Stone space reformulation more carefully.
3. Determine whether the general question is set-theoretically sensitive.
4. Decide scope of paper based on what can be proved.
