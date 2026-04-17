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

**Theorem (via Nikodym/Vitali–Hahn–Saks-type convergence):** If $(\mu_n)$ is a sequence of $\sigma$-additive probabilities on a $\sigma$-algebra $\Sigma$, then any pointwise ultralimit $\ell(A) = \lim_\mathcal{U} \mu_n(A)$ is itself $\sigma$-additive.

**Reference:** Dunford–Schwartz, *Linear Operators* I (1958), IV.9.8. *(The delicate step is interchanging the ultralimit with the countable sum $\sum_k \mu_n(A_k)$; this does not follow merely from the pointwise identity $\mu_n(A) = \sum_k \mu_n(A_k)$, and is where the real theorem lives.)*

**Consequence:** On a $\sigma$-algebra, no purely finitely additive charge is a pointwise ultralimit of $\sigma$-additive measures. This case is settled. The question is entirely about Boolean algebras that are not $\sigma$-complete — and this retroactively clarifies why the finite-cofinite algebra is not just a convenient example: it is the minimal setting where the Nikodym obstruction disappears and the ultralimit question becomes nontrivial.

#### Case 2: General Boolean algebras — OPEN

The Nikodym obstruction does not apply when $B$ is merely a Boolean algebra (not $\sigma$-complete). No theorem in either direction appears in the literature. The finite-cofinite algebra is the canonical example of this setting.

**What is known:**
- Yosida–Hewitt (1952): establishes ba = ca ⊕ pfa (orthogonal decomposition) but does not address representation by limits
- Rao–Rao (1983): covers classification and extension, no approximation of pfa by ca
- Cardona–Mejía–Uribe-Zapata (2025): local (finite-partition) approximation of free finitely additive measures by uniform probabilities on finite sets; does **not** address global pointwise ultralimit representation
- Duanmu–Weiss (2018): on totally bounded separable metric spaces, every finitely additive Borel probability is a weak limit (bounded uniformly continuous test functions) of $\sigma$-additive probabilities; Example 5.14 shows setwise ultralimit approximation fails for ultrafilter charges on discrete sets

#### Case 3: Weak* approximation — a different question

Every purely finitely additive measure is an accumulation point (in the product topology on $[0,1]^B$) of finitely supported (hence $\sigma$-additive) measures (Seidenfeld, cited in Duanmu–Weiss). But this uses nets, not sequences or ultrafilter limits. Weak* limit ≠ pointwise ultralimit.

#### Case 4: The βN perspective — likely the right geometric language

Every finitely additive probability on $\mathcal{P}(\mathbb{N})$ corresponds bijectively to a regular Borel measure on $\beta\mathbb{N}$ (Stone space). $\sigma$-additive charges ↔ measures supported on $\mathbb{N} \subset \beta\mathbb{N}$ (principal ultrafilters). Purely finitely additive charges ↔ measures supported on $\beta\mathbb{N} \setminus \mathbb{N}$.

This matches the geometry of the main paper exactly (principal ultrafilters = realised states; non-principal = ideal limit points). The fixed-algebra ultralimit problem can be restated geometrically as:

> Which regular Borel probability measures on the Stone space of $B$ arise as ultralimits of measures supported on principal points?

This is probably the right language for the investigation. It may not resolve the problem immediately, but it connects the question to the support geometry that drives Paper I's Stone construction and makes the βN picture load-bearing rather than illustrative.

Ultralimits of Dirac masses produce only {0,1}-valued ultrafilter charges — a proper subclass. General purely finitely additive charges (with values in $(0,1)$) are not of this form. Translating the ladder of sub-questions into the Stone/βN language is Priority 3 (see below).

### The Natural Ladder of Sub-Questions

Do not skip rungs. The first serious feasibility test is narrower than the full question.

1. **Ultrafilter-generated {0,1}-charges:** $\delta_\mathcal{U}(A) = \mathbf{1}_{A \in \mathcal{U}}$. Arise as ultralimits of Dirac masses on the finite-cofinite algebra. ✓ (the companion note proof already gives this)

2. **Free finitely additive probabilities on the finite-cofinite algebra** — **RESOLVED (positive).** ✓
   See `finite_cofinite_calculation.md` for the full argument. Key findings:
   - On $\mathcal{E}$, $\mathrm{pfa}(\mathcal{E})$ is one-dimensional: the only purely finitely additive (= free) probability is $\ell_{\mathrm{fc}}$ itself.
   - $\ell_{\mathrm{fc}}$ is the pointwise sequential limit of the uniform measures $\frac{1}{k}\sum_{n<k}\delta_n$, which are $\sigma$-additive on $\mathcal{E}$.
   - Hence every finitely additive probability on $\mathcal{E}$ is a pointwise sequential limit (a fortiori a pointwise ultralimit) of $\sigma$-additive probabilities on the same algebra.
   - Structural reason: the "spread mass thinly" construction works because $\mathrm{pfa}(\mathcal{E})$ is one-dimensional and $\ell_{\mathrm{fc}}$ has no atom structure to obstruct approximation.
   - In the βN picture: this is just weak* density of finitely supported measures in all Borel measures on $\beta\mathbb{N}$ — trivial in this case, confirming that the interesting structure begins with algebras where $\mathrm{pfa}(B)$ is multidimensional.

3. **General purely finitely additive probabilities on Boolean algebras:** Open. The finite-cofinite case is positive but special — $\mathrm{pfa}(\mathcal{E})$ is one-dimensional. The next test case should be an algebra where $\mathrm{pfa}(B)$ is genuinely multidimensional (e.g., a free Boolean algebra on countably many generators, or the algebra of clopen sets of $\beta\mathbb{N}$).

4. **The full representation question and classification:** Is every charge in pfa(B) an ultralimit of $\sigma$-additive charges on $B$? If not, what characterizes the representable ones? Set-theoretic sensitivity is a plausible downstream horizon but remains speculative until rung 3 is probed.

### Key Distinctions

- **Fixed algebra vs varying algebra:** Fixed = same $B$ throughout. Varying = $\ell$ arises on a diagonal copy inside an ultraproduct of different $(B_n, \mu_n)$. These are different questions. The companion note produces its witness through an ultraproduct, but the resulting bad charge is analyzed on the diagonal copy of a fixed algebra $E$. The present representation problem asks for a genuine fixed-algebra ultralimit from the start: $\ell(A) = \lim_\mathcal{U} \mu_n(A)$ with each $\mu_n$ $\sigma$-additive on the same $B$.

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

### Claims to resolve

- [x] On the finite-cofinite algebra: every finitely additive probability is a pointwise sequential limit of σ-additive probabilities on the same algebra. (Positive. See `finite_cofinite_calculation.md`.)
- [ ] On a Boolean algebra where pfa(B) is multidimensional: does the positive answer persist?
- [ ] Is there a purely finitely additive charge on some Boolean algebra that is provably NOT a pointwise ultralimit of σ-additive probabilities on the same algebra?
- [ ] Does the βN / Stone geometric reformulation give a characterization for general B?
- [ ] Is the answer set-theoretically independent for some class of algebras?

### References to add to bib

- Duanmu, H. and Weiss, W. (2018). Finitely-additive, countably-additive and internal probability measures. *Comment. Math. Univ. Carolin.* **59**(4), 467–485.
- Dunford, N. and Schwartz, J. T. (1958). *Linear Operators*, Part I. Interscience.
- Lauwers, L. (2010). Purely finitely additive measures are non-constructible objects. DPS 10.10, KU Leuven.
- Cardona, Mejía, Uribe-Zapata (2025). arXiv:2503.08910.

### Investigation priorities

**Priority 1 — σ-algebra obstruction (write up carefully):**
State the exact Dunford–Schwartz IV.9.8 theorem. Do not present the interchange $\lim_\mathcal{U} \sum_k = \sum_k \lim_\mathcal{U}$ as self-evident from the pointwise identity; that is where the real theorem lives. Keep the conclusion; attribute the delicate step to the reference.

**Priority 2 — finite-cofinite algebra — DONE (positive).** ✓
Every finitely additive probability on $\mathcal{E}$ is a pointwise sequential limit
of $\sigma$-additive probabilities on $\mathcal{E}$. The key: $\mathrm{pfa}(\mathcal{E})$
is one-dimensional (only $\ell_{\mathrm{fc}}$), and $\ell_{\mathrm{fc}}$ is the
limit of $\frac{1}{k}\sum_{n<k}\delta_n$. See `finite_cofinite_calculation.md`.

**Next target (Priority 2b) — algebra with multidimensional pfa:**
Find a Boolean algebra $B$ where $\mathrm{pfa}(B)$ is genuinely multidimensional
and test whether all purely finitely additive charges are still representable.
Candidate: $\mathcal{P}(\mathbb{N})/\mathrm{fin}$ (the quotient of all subsets
by the finite sets), or the clopen algebra of $\beta\mathbb{N}$.

**Priority 3 — Stone/βN geometric reformulation:**
Translate the fixed-algebra ultralimit problem into the Stone/βN language explicitly. The geometric form is: which regular Borel measures on $\mathrm{St}(B)$ arise as ultralimits of measures supported on principal points? This matches the support geometry of Paper I and is probably the right language for the general investigation.

**Priority 4 — set-theoretic sensitivity (downstream):**
Revisit only after Priorities 2–3. Currently a plausible horizon, not an active target.
