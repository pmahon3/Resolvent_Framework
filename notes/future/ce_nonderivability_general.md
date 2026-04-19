---
name: CE non-derivability — general Boolean algebra version
description: Future note — metatheorem that countable additivity is not first-order axiomatizable; plus full investigation of ultralimit representation of purely finitely additive charges
type: project
---

# CE Non-Derivability and the Ultralimit Representation Problem

*Extended 2026-04-17 to include literature findings and paper sketch*

---

## Part I: The Non-Axiomatizability Theorem (complete)

**Status:** Done. Written up as companion note (`countable_additivity_not_first_order.tex`), targeting APAL.

The companion note proves: in the first-order language $\mathcal{L}_{\mathrm{BA},\mu}$ of Boolean algebras with normalized finitely additive charge, no first-order theory characterizes those models whose charge extends to a $\sigma$-additive measure. The proof is the Dirac-mass ultraproduct construction.

See `papers/paper_i/notes/countable_additivity_not_first_order.tex` for the full proof.

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
   See `papers/paper_i/notes/ultralimit_investigation/finite_cofinite_calculation.md` for the full argument. Key findings:
   - On $\mathcal{E}$, $\mathrm{pfa}(\mathcal{E})$ is one-dimensional: the only purely finitely additive (= free) probability is $\ell_{\mathrm{fc}}$ itself.
   - $\ell_{\mathrm{fc}}$ is the pointwise sequential limit of the uniform measures $\frac{1}{k}\sum_{n<k}\delta_n$, which are $\sigma$-additive on $\mathcal{E}$.
   - Hence every finitely additive probability on $\mathcal{E}$ is a pointwise sequential limit (a fortiori a pointwise ultralimit) of $\sigma$-additive probabilities on the same algebra.
   - Structural reason: the "spread mass thinly" construction works because $\mathrm{pfa}(\mathcal{E})$ is one-dimensional and $\ell_{\mathrm{fc}}$ has no atom structure to obstruct approximation.
   - In the βN picture: this is just weak* density of finitely supported measures in all Borel measures on $\beta\mathbb{N}$ — trivial in this case, confirming that the interesting structure begins with algebras where $\mathrm{pfa}(B)$ is multidimensional.

3. **General purely finitely additive probabilities on Boolean algebras:** Partially open. The Stone-space analysis (Priority 3) gives the right framework:
   - **Atomic $B$:** positive uniformly — density of $\mathrm{Prin}(B)$ in $\mathrm{St}(B)$ (equivalent to atomicity) implies every finitely additive probability is approximable. Covers $\mathcal{E}$, $\mathcal{E}_k$, $\mathcal{E}_\omega$. See `papers/paper_i/notes/ultralimit_investigation/rung3_multidimensional_pfa.md`.
   - **Non-atomic, full-support $\sigma$-additive measure exists:** positive — $\mathrm{Supp}_\sigma(B) = \mathrm{St}(B)$. First example: the interval algebra $\mathcal{I}$ of half-open subintervals of $[0,1]$; Lebesgue measure has full support. See `papers/paper_i/notes/ultralimit_investigation/stone_geometric_translation.md`.
   - **σ-complete non-atomic $B$:** negative (Nikodym / companion note §2).
   - **Non-σ-complete, few countable joins (e.g., $\mathcal{P}(\mathbb{N})/\mathrm{fin}$):** positive (vacuously) — σ-additivity reduces to finite additivity when too few joins exist; every finitely additive probability is σ-additive. See `papers/paper_i/notes/ultralimit_investigation/row5_candidate.md`.
   - **Non-σ-complete non-atomic $B$, intermediate join structure:** open — reduces to **Strategy D**. By the canonical decomposition theorem ($B \cong (B{\upharpoonright}A) \times (B{\upharpoonright}A^c)$ at every $A$), any failure of $\mathrm{Supp}_\sigma(B) = \mathrm{St}(B)$ is witnessed by a measure-free direct-product factor. "Indecomposable row-5" is provably impossible. The open question reduces to: does a non-σ-complete non-atomic measure-free Boolean algebra exist?

4. **The full representation question and classification:** The question is now reformulated as: for which $B$ is $\mathrm{Supp}_\sigma(B) = \mathrm{St}(B)$? The hierarchy is organized by a **completeness gradient** — how many countable joins $B$ has:
   - σ-complete: maximal joins → Nikodym → negative.
   - Intermediate joins: σ-additivity is a genuine but limited constraint → open frontier (Strategy D).
   - Minimal joins (like $\mathcal{Q}$): σ-additivity vacuous → positive trivially.
   
   **Canonical decomposition theorem:** $B \cong (B{\upharpoonright}A) \times (B{\upharpoonright}A^c)$ canonically at every element $A$. If $\nu$ is σ-additive on $B{\upharpoonright}A$, then $\tilde\nu(C) = \nu(C \wedge A)$ is σ-additive on $B$ (meets distribute over existing joins). Consequence: any gap in $\mathrm{Supp}_\sigma(B)$ is a direct-product decomposition with a measure-free factor. Strategies A, B, C (indecomposable constructions) are eliminated. See `papers/paper_i/notes/ultralimit_investigation/row5_candidate.md` Parts III–IV.
   
   **Subalgebra embedding lemma:** any non-σ-complete $B$ that embeds join-preservingly into a σ-algebra $\Sigma$ where some σ-additive probability charges all non-zero elements of $B$ has $\mathrm{Supp}_\sigma(B) = \mathrm{St}(B)$. Covers all "concrete" algebras. See `papers/paper_i/notes/ultralimit_investigation/subalgebra_embedding_lemma.md`.
   
   **Strategy D (sole remaining open question):** does there exist a non-σ-complete non-atomic Boolean algebra admitting no σ-additive probability? If yes: pair with a positive factor for a negative instance. If no: the open row collapses and all non-σ-complete non-atomic algebras are positive. See `papers/paper_i/notes/ultralimit_investigation/row5_candidate.md` Part V.

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

- [x] On the finite-cofinite algebra: every finitely additive probability is a pointwise sequential limit of σ-additive probabilities on the same algebra. (Positive. See `papers/paper_i/notes/ultralimit_investigation/finite_cofinite_calculation.md`.)
- [x] On Boolean algebras where pfa(B) is multidimensional: positive for all partition extensions $\mathcal{E}_k$ and $\mathcal{E}_\omega$. (All atomic; follows from density of $\mathrm{Prin}(B)$.)
- [x] Stone/βN geometric reformulation: $\mathrm{Supp}_\sigma(B) = \mathrm{St}(B)$ is the condition; positive for atomic and full-support non-atomic cases; negative for σ-complete non-atomic (Nikodym); see stone_geometric_translation.md.
- [x] Direct-product strategy: collapsed. $\mathcal{P}(\mathbb{N})/\mathrm{fin}$ has σ-additivity vacuous — every finitely additive probability there is σ-additive. Direct products using this factor are not negative examples.
- [x] Canonical decomposition theorem: $B \cong (B{\upharpoonright}A) \times (B{\upharpoonright}A^c)$ at every $A$; any $\mathrm{Supp}_\sigma$ gap is a direct-product gap with a measure-free factor; indecomposable row-5 impossible; Strategies A, B, C eliminated.
- [x] Weak distributivity thread: Džamonja–Plebanek / Fremlin §391D give a ZFC theorem (weakly distributive + s.p.f.a. ↔ s.p. σ-additive) but only for **σ-complete** algebras. Does not constrain Strategy D. Non-weak-distributivity is not a necessary condition on a Strategy D counterexample.
- [ ] **Strategy D (sole remaining open question):** Does there exist a non-σ-complete non-atomic Boolean algebra admitting no σ-additive probability? No known construction, no known obstruction. **Topological reformulation** (2026-04-18): Strategy D is equivalent to the existence of a compact totally disconnected non-atomic non-basically-disconnected Radon-measure-free space. **Set-theoretic sensitivity** (2026-04-18): MA + ¬CH narrows candidates (compact spaces of weight $< \mathfrak{c}$ carry strictly positive Radon measures); ◇-type constructions may yield counterexamples. Problem is likely **independent of ZFC**; forcing or advanced Radon-measure theory is required. ZFC Boolean-algebra methods are exhausted.

### Summary of Investigation Outcome

> The representation problem is fully resolved in the atomic regime (positive, by density of $\mathrm{Prin}(B)$), in the concrete join-preserving regime (positive, by the subalgebra embedding lemma), at the vacuous minimal-join extreme (positive, since σ-additivity reduces to finite additivity on $\mathcal{P}(\mathbb{N})/\mathrm{fin}$), and in the σ-complete negative regime (negative, by Nikodym). What remains is a single genuinely open Boolean-algebraic existence problem — **Strategy D** — which is equivalent to a set-theoretic topology question (Radon-measure-free compact totally disconnected non-atomic non-basically-disconnected spaces). It is likely independent of ZFC. ZFC Boolean-algebra methods are exhausted; the next step requires forcing. No further internal reorganization is needed. The frontier is clean.

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
limit of $\frac{1}{k}\sum_{n<k}\delta_n$. See `papers/paper_i/notes/ultralimit_investigation/finite_cofinite_calculation.md`.

**Priority 2b — algebras with multidimensional pfa — DONE (positive).** ✓ See `papers/paper_i/notes/ultralimit_investigation/rung3_multidimensional_pfa.md`.

Key findings:
- $\mathcal{P}(\mathbb{N})/\mathrm{fin}$ and $\mathrm{Clop}(2^\omega)$ ruled out as test cases (wrong for rung 3; see row5_candidate.md for corrected analysis of $\mathcal{P}(\mathbb{N})/\mathrm{fin}$).
- Correct family: partition extensions $\mathcal{E}_k$ = algebra generated by $\mathcal{E}$ and a $k$-partition of $\mathbb{N}$ into infinite pieces. $\mathrm{pfa}(\mathcal{E}_k) \cong \Delta_{k-1}$ (the $(k-1)$-simplex) — genuinely multidimensional for $k \geq 2$.
- Representability on $\mathcal{E}_k$ for all finite $k$: **positive** (spread the $\alpha_i$ mass uniformly within each piece $P_i$).
- Countably many pieces ($\mathcal{E}_\omega$): **positive** (no second-order pfa residual; same construction works).
- Strategic lesson: positivity for all atomic algebras follows from density of $\mathrm{Prin}(B)$ in $\mathrm{St}(B)$; the interesting question lies entirely outside the atomic regime.

**Priority 3 — Stone/βN geometric reformulation:**
Translate the fixed-algebra ultralimit problem into the Stone/βN language explicitly. The geometric form is: which regular Borel measures on $\mathrm{St}(B)$ arise as ultralimits of measures supported on principal points? This matches the support geometry of Paper I and is probably the right language for the general investigation.

**Priority 4 — set-theoretic sensitivity (now the active frontier, 2026-04-18):**
Strategy D has been topologically reformulated as the Radon-measure-free compact Stone space question. ZFC Boolean-algebra arguments are exhausted. The next step is either a forcing construction (under ◇ or similar) of a measure-free compact totally disconnected non-atomic non-basically-disconnected space, or a consistency proof that none exists. Relevant literature: Fremlin *Measure Theory* §531–534; Kunen (1981) compact L-spaces under ◇; Fedorchuk (1976). This is genuinely a set-theoretic topology problem; standard Boolean-algebra methods do not apply.
