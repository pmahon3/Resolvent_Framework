# Paper I Integration Plan

> **Status:** Draft plan, 2026-04-02.
> **Task:** Integrate Papers −1, 0, and A into a single Paper I: *Probability from Observation*.

---

## Source papers

| File | Title | Role in Paper I |
|------|-------|-----------------|
| `discriminability_foundations` | *Extension of Charges on Directed Systems of Boolean Algebras* | §3: CE theorem and irreducibility |
| `observational_foundations` | *Observational Foundations of Probability* | §2: framework setup; §4: Carathéodory route |
| `stone_duality_extension` | *A Stone Duality Route to the Observable Extension Theorem* | §2: refined setup; §5: Stone route; §6: bridge |

---

## Proposed structure of Paper I

### Abstract

The abstract states: compatible charges on a query system extend to a unique global
probability measure if and only if they satisfy collective exhaustion (CE). The proof
is given by two independent routes — Carathéodory and Stone — illuminating complementary
aspects. CE is shown to be irreducible: no finitary or structural condition implies it.
The Stone space of the observable algebra, introduced as a technical device, is the
canonical compact completion of the sample space and reappears in reconstruction.

Draw on all three abstracts; weight toward Paper A's framing (most current).

---

### §1 Introduction — *New writing*

Four paragraphs:

1. The question: when does a coherent family of observations determine a unique
   probability measure?

2. The answer: CE is the necessary and sufficient condition. Two independent routes
   both land at CE in different forms — valuation-layer condition (Route 1) vs.
   support condition on the Stone compactification (Route 2). Under shared hypotheses,
   the two measures coincide.

3. What is new: the identification of CE as irreducible (not provable from any
   structural or finitary condition), and the explicit roles of Discriminability and
   CE in the Stone route.

4. Organisation paragraph (list of sections).

Draw on: Paper 0 intro (problem framing), Paper A intro (Stone route motivation),
Paper −1 intro (structural analysis framing), and `program_overview.md` Route 1/2
descriptions.

---

### §2 Setup: query systems and charges — *From Paper A, with Paper 0 cross-check*

Use **Paper A's notation** throughout (cleaner and more recent):
- Index set $(\iota, \leq)$
- Sample space $\Omega$
- Outcome spaces $(\mathrm{Out}(i), \mathcal{F}_i)$
- Evaluation maps $\mathrm{eval}_i : \Omega \to \mathrm{Out}(i)$
- Refinement maps $\pi_{ij} : \mathrm{Out}(j) \to \mathrm{Out}(i)$
- Coherence: $\pi_{ij} \circ \mathrm{eval}_j = \mathrm{eval}_i$

Cylinder sets, $B_i$, $\mathcal{C}$ (CylGen), $\sigma(\mathcal{C})$ — from Paper A §2.

Connecting maps $\varphi_{ij}$ — from Paper A §2.

Compatible charges — from Paper A §2.

**Three hypotheses** (state all three upfront, explain each):
- **EvalSurjective**: ensures connecting maps are injective; structural, not a constraint
  on the charges
- **Discriminability**: queries separate points; ensures Stone embedding is injective
- **CE (Collective Exhaustion)**: the irreducible valuation-layer condition; defined
  here, characterized in §3

Add a **Remark on Paper 0's notation** (one line): Paper 0 uses $\mathcal{Q}, \preceq,
O_Q, \pi^{Q_2}_{Q_1}$ for the same objects; all results are equivalent under the
renaming $\iota = \mathcal{Q}$, $\leq\, =\, \preceq$, etc.

---

### §3 The CE theorem — *From Paper −1*

This section establishes CE as the correct and irreducible characterization of
σ-additive extensibility. It is self-contained and does not yet involve the full
query system structure (only single-level Boolean algebras and directed systems).

**§3.1 Single-algebra extension** — Paper −1 §2 (Boolean charge space, gap, extension
criterion). The extension criterion (continuity at ∅ ↔ σ-additive extendibility) is
the single-algebra foundation.

**§3.2 Finitary conditions do not suffice** — Paper −1 §3 (exhaustiveness trivial,
continuity at ∅, regress, no-finitary corollary). This motivates why CE must be an
irreducible axiom.

**§3.3 Nontrivial refinement** — Paper −1 §4 (incompleteness: nontrivial refinement
introduces new events, gap nonemptiness). Condensed; this section can be shortened
relative to Paper −1's treatment.

**§3.4 CE characterises σ-additivity** — Paper −1 §5 (independence of layers,
finite-cofinite counterexample, CE definition, Thm sp1). This is the main result
of §3.

**§3.5 CE is irreducible** — Paper −1 §5 (CE irreducibility proposition: particular
case + universal case via ultraproducts; Yosida-Hewitt). Can be condensed relative to
Paper −1 by citing the particular case and stating the universal case as a remark.

**Closing remark:** CE resolved, we proceed to two independent proofs that CE suffices
to build the global measure. The two routes illuminate the same theorem from opposite
sides.

**Note on site-theoretic perspective (Paper −1 §6 Remark):** Keep as a Remark at
the end of §3.5, clearly flagged as optional/supplementary.

---

### §4 Route 1: The Carathéodory extension — *From Paper 0*

**§4.1 Observational determination** — Paper 0 §4 (π-λ uniqueness for query systems).
Short section; establishes that P is unique if it exists.

**§4.2 Observable content** — Paper 0 §5 (construction of finite observational content
from compatible laws). This is the finitely additive cylinder measure.

**§4.3 Carathéodory extension** — Paper 0 §6 (the realizability/Carathéodory route:
countably additive marginals → global measure). The main result: given CE (= per-level
σ-additivity via §3.4), the content extends.

**What to omit from Paper 0:** The Prokhorov route (Paper 0 §7) — condense to a
**Remark** noting the alternative. Prokhorov assumes topological structure on outcome
spaces; it is a third route but adds hypotheses and is less central.

**What to omit from Paper 0:** The statistical experiment theory discussion — condense
to a sentence in the introduction.

---

### §5 Route 2: The Stone extension — *From Paper A*

Keep Paper A's structure essentially intact. The section headings become:

**§5.1 Step A: Stone space of the direct limit** — Paper A §3 (EvalSurjective →
injective connecting maps → St(colimit) ≅ inverse limit).

**§5.2 The inverse limit measure** — Paper A §4 (compatible charges → Stone measures
→ Choksi → measure on inverse limit).

**§5.3 Step B1: structural identification** — Paper A §5 (discriminability → pullback
= σ(CylGen)).

**§5.4 Step B2: CE and the support condition** — Paper A §6 (CE ↔ μ_p = 0 via
Yosida-Hewitt → support on principal ultrafilters).

**§5.5 The Stone extension theorem** — Paper A §7 (assembly). State the main theorem
and proof chain. Add the two remarks from Paper A (relation to Carathéodory route;
CE is not bypassed by compactness).

---

### §6 The bridge — *New writing, drawing on `program_overview.md` and Paper A intro*

This section is new writing. Three subsections:

**§6.1 Two routes, one theorem.** Under shared hypotheses (σ-additive marginals +
CE + Discriminability + EvalSurjective), Carathéodory and Stone produce the same
measure. Proof: both agree on CylGen; observational determination forces equality.
This confirms: the two routes are genuinely independent proofs of the same theorem.

**§6.2 CE's two faces.** In Route 1, CE appears as a condition on the charge: the
observer's assignments do not escape to infinity. In Route 2, CE appears as a support
condition: the Stone measure concentrates on the image of Ω inside its compactification.
These are the same condition seen from inside the algebra (Route 1) and from outside
it (Route 2).

**§6.3 The Stone space as compact completion.** The Stone space St(CylGen) constructed
here as a technical device is the canonical compact Hausdorff completion of Ω for the
observable topology. It is not a construction but a revelation: it is the space that the
observable algebra already generates. Under the reconstruction condition of Paper III —
when the observation function is a cyclic vector for the Koopman operator — this compact
space is measure-theoretically isomorphic to the state space itself. We develop this
elsewhere. (One paragraph; not a full development.)

---

### Bibliography

Merge all three bibliographies. Key references:
- Stone (1936), Daniell (1918)
- Halmos (1950), Fremlin (2003)
- Choksi (1958)
- Yosida-Hewitt (1952)
- Cardona-Mejía-Uribe-Zapata (2025)
- Johnstone — *Stone Spaces*
- Kolmogorov (extension theorem)
- Prokhorov (1956) [retained as a remark citation]

---

## Notational unification decisions

All notation follows Paper A. The renaming from Paper 0 and Paper −1 is:

| Paper 0 | Paper −1 | Paper I (= Paper A) |
|---------|----------|---------------------|
| $\mathcal{Q}, \preceq$ | $\mathcal{I}, \leq$ | $\iota, \leq$ |
| $O_Q$ | $O_i$ | $\mathrm{Out}(i)$ |
| $\pi^{Q_2}_{Q_1}$ | $\pi_{ij}$ | $\pi_{ij}$ |
| $\nu_Q$ | $\ell_i$ | $\mu_i$ |
| $\sigma(\mathcal{Q})$ | $\sigma(\mathcal{E}_i)$ | $\sigma(\mathcal{C})$ |

Paper −1 also uses $\mathcal{E}_i$ for what Paper A calls $B_i$ (the Boolean algebra
of cylinder sets at level $i$). In §3 (which is drawn from Paper −1), $\mathcal{E}_i$
can stand for a generic Boolean algebra (Paper −1's more abstract setting). A transition
paragraph at the start of §4 can reintroduce the $B_i = \mathcal{E}_i$ identification.

---

## Scope decisions

| Content | Decision |
|---------|----------|
| Paper −1: site-theoretic remark | Keep as optional remark in §3.5 |
| Paper 0: Prokhorov route | Condense to a Remark in §4 |
| Paper 0: statistical experiment theory | One sentence in §1 |
| Paper 0: Kolmogorov comparison | Keep (two paragraphs in §4 intro) |
| Paper A: bridge paragraph in intro | Promote to §6 |
| Paper A: "relation to prior work" paragraph | Keep in §5.5 or as a §5 remark |

---

## What is genuinely new writing

- §1 Introduction (complete rewrite)
- §6 The bridge (§6.1 and §6.2 are new; §6.3 expands the one-paragraph bridge in Paper A)
- Transition paragraphs between sections
- Abstract (merging and extending)
- Unified closing remarks and discussion

---

## Recommended workflow

1. **Create `papers/paper_i/`** with `paper_i.tex` and `paper_i_body.tex`.
2. **Draft §2** first: copy Paper A §2, add Paper 0 notation remark.
3. **Draft §3** from Paper −1, with condensation decisions noted above.
4. **Draft §4** from Paper 0 §4-6, omitting §7 (replace with Remark).
5. **Draft §5** from Paper A §3-7 essentially verbatim (it is clean).
6. **Write §6** (new).
7. **Write §1** (new, after §§2-6 are stable).
8. **Merge bibliography.**
9. **Audit**: check all cross-references work, notation is consistent, no duplicate theorem statements.

---

## Open questions for decision before drafting

1. **Title**: *Probability from Observation* (from `program_overview.md`) or a more
   technical title closer to Paper 0's *Observational Foundations of Probability*?
   Recommendation: *Probability from Observation: Carathéodory and Stone Routes to the
   Observable Extension Theorem* (descriptive, connects to prior work).

2. **Author list**: single author (Patrick S. Mahon) throughout, consistent with
   Paper A and Paper 0.

3. **Prokhorov route**: the current recommendation is to condense to a Remark. If you
   want it as a full §4.4, that's also defensible. It shows that topological
   compactness is an alternative to CE, which is conceptually interesting.

4. **Length target**: Papers −1+0+A total roughly 60–70 pages. Paper I should be
   tighter: target ~40 pages. The main compressions are: §3.3 (nontrivial refinement,
   reduce to one proposition + remark), Paper 0's §7 (Prokhorov → Remark), and
   Paper 0's statistical experiment discussion (→ sentence).
