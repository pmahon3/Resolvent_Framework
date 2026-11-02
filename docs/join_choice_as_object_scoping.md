# Join choice as object: scoping pass

*2026-11-02. Read-and-report. reviewed: false. Branch `join-choice-scoping`, from `main` at
a41cf31. No .tex, Lean or definition file was changed. Hand arguments are flagged ⟦HAND⟧.
Ledger entry: `site_regularity_prediction_ledger.md`, Entry JC-OBJ-1.*

## Headline: premise check

**The premise "admissibility makes the two joins coincide for orthogonal families" is
MISATTRIBUTED. The coincidence holds, but admissibility plays no part in it.**

- `formalization/QuerySystem/QuerySystem/Admissibility.lean` has no join content.
  - Grep `⋃|iUnion|[Uu]nion|[Jj]oin|⊔|sSup|iSup` gives one hit, line 37, the word "representability".
  - `Admissible` (l.82–83) is `EssentiallyIrreducible ∧ NonSegregated`. Both are centre and
    gluing conditions.
- The coincidence comes from the **carrier type**:
  - Lean: `MeasurableSpace.DynkinSystem` (`SigmaEssentialLocalization.lean:25–28`).
  - Paper: the σ-class axioms (`sigma_essential_body.tex:23–36`).
- States are *defined* by additivity over set unions:
  - `TwoValuedState.val_iUnion` (`SigmaEssentialLocalization.lean:52–55`);
  - `FinAddState.val_union` (`SigmaEssentialWitness.lean:55–56`);
  - paper l.39–46: "orthogonal joins lying in its domain" are unions.
- The paper's Adm (l.915–917) does list "concrete, σ-complete". The Lean side records that these
  two conjuncts hold of every σ-class and "define the category rather than cutting it down":
  `SigmaEssentialOpenCore.lean:262–273` and `Admissibility.lean:35–39`. So the premise is true
  only through conjuncts that are vacuous.

**Stronger structural fact ⟦HAND⟧.** Take any family 𝓛 ⊆ 𝒫(Ω) closed under countable disjoint
unions. If {Aₙ} ⊆ 𝓛 are pairwise disjoint, then ⋃Aₙ ∈ 𝓛 is an upper bound, and every upper
bound C ∈ 𝓛 contains it, so ⋃Aₙ = ⋁Aₙ. Consequences:
- An order-embedding of an OMP whose image is a σ-class is automatically σ-regular on orthogonal
  families. See (T3) below.
- Inside the corpus's category (σ-classes), the "space of choices" is **a single point**.
- A real choice exists only for representations whose image is *not* a σ-class, where
  ⋃φ(xₙ) ∉ φ(𝓛).

The coincidence fails only for non-orthogonal families (meets). The paper already makes that
failure visible as its named obstruction (Q3).

I judged the premise misattributed rather than false, since the coincidence itself holds, and
continued. A second premise is **stale**: "σ-essential ships first and alone" (Q5).

**Attribution note.** The brief credits Lemma R to Dvurečenskij–Neubrunn–Pulmannová.
`regularity_sigma_additivity_pullback.md:63–68` records that their "regular state" is a different
notion and that Lemma R is unlocated folklore (l.41–46, 307–311). DNP 1992 enters the corpus only
for the incomplete-inner-product example (`dilation_question_scoping.md:101–105`) and the
quotient remark (paper l.972).

## Puzzle first

Take the finite–cofinite subsets of ℕ, and ask "is n in the set?" for each n.
- In the algebra, the singletons {0}, {1}, … have join ℕ: the only cofinite upper bound is ℕ.
- Now draw the algebra as clopen sets of its Stone space ℕ ∪ {∞}. The union of the singleton
  clopens is ℕ, which misses ∞. The join, the closure of that union, includes ∞.
- The state "cofinite = 1" sums to 0 over the singletons but gives 1 to their join.

Where did the missing 1 go?
- Computed in the algebra, it is a **defect of the state**.
- Computed in the Stone space, it is **mass on the leftover point ∞**: s(g) = δ_∞({∞}) = 1.

Same answer pattern, two bookkeepings. (Scope: `regularity_sigma_additivity_pullback.md:285–290`.)

The σ-essential witness does the first bookkeeping. On a row α₀ the vote state m gives 0 to every
cell and 1 to the co-countable row union (Rem 5.17, l.867–876).

## Q1. Inventory: where the corpus commits to join = union

Grep patterns run (full output read, nothing truncated):
- Paper body: `bigcup|bigsqcup|\\sqcup|\\cup|disjoint union|orthogonal join|\\bigvee|\\vee|join`
  (64 lines).
- Lean: `⋃|iUnion|[Uu]nion|[Jj]oin|⊔|sSup|iSup` on `Admissibility.lean`, plus the definitions of
  `TwoValuedState`, `FinAddState`, `IsConcreteCarrier`, `IsSigmaCompleteCarrier`, `MeetsExist`
  and `PolishRepresentable`.
- Programme docs, against `program_overview.md` (1350 lines) and `frontier_map.md` (934 lines):
  `[Jj]oin[s ]|[Uu]nion|⋃|bigcup|σ-class|sigma-class|Dynkin|set intersection|set-intersection|meet ≠|Loomis|tribe|regular embedding|non-?regular|σ-regular|sigma-regular|Lemma R|gap element`.
- Spine: `[Jj]oin|[Uu]nion|bigcup|bigvee|σ-class|sigma-class|Dynkin|set intersection|regular|quarantine|Loomis|tribe|concrete`
  on `spine_body.tex`.

Commitments (C = constitutive: the carrier or state is defined so; U = use; V = the corpus makes
the difference visible):

| # | File:line | Kind | What |
|---|---|---|---|
| 1 | `sigma_essential_body.tex:23–36` | C | σ-class = closure under countable disjoint ⋃, ordered by ⊆. "The σ-class axioms … are what every argument uses." |
| 2 | `sigma_essential_body.tex:39–47` | C | States additive over finite / countable disjoint families "with ⋃Aₙ ∈ 𝓛". Orthogonal join is written as union. |
| 3 | `sigma_essential_body.tex:290–294` | C | Bare form (b): "commutes with countable disjoint unions". |
| 4 | `sigma_essential_body.tex:528–548` | U | Lem 5.3, σ-class basics: every step is a set union or set difference. |
| 5 | `sigma_essential_body.tex:782–785` | U | Thm 5.13: "their union U_α lies in 𝓛 (σ-class closure), and Ω∖U_α is countable". |
| 6 | `sigma_essential_body.tex:842–843` | U | Thm 5.16: finite disjoint union "automatically in 𝓛". |
| 7 | `sigma_essential_body.tex:915–917` | C | Adm lists "concrete, σ-complete". |
| 8 | `sigma_essential_body.tex:341–346, 365–374` | V | "lattice meet failing to be set intersection" is named as THE obstruction, meet side; MO₂ atoms example. |
| 9 | `sigma_essential_body.tex:388–396` | V | Faithful σ-tribe representation route barred (Floor); σ-Loomis–Sikorski only σ-epimorphic. The representation is discussed as a route, not as an object. |
| 10 | `sigma_essential_body.tex:962–977` | V | The quotient 𝓛/ctble is the one abstract (non-concrete) σ-OMP in the paper. |
| 11 | `SigmaEssentialLocalization.lean:25–28, 36–56` | C | `Carrier d` over `DynkinSystem`; `val_iUnion` is stated over `⋃ i, f i`; Diracs are point evaluations of Ω. |
| 12 | `SigmaEssentialWitness.lean:43–56` | C | `FinAddState.val_union` is stated over `A ∪ A'`. |
| 13 | `SigmaEssentialOpenCore.lean:262–273` | C | `IsConcreteCarrier`, `IsSigmaCompleteCarrier` ("closure under countable disjoint unions"): "defines the category rather than cutting it down". |
| 14 | `Admissibility.lean:35–39, 54` | C | Records concreteness and σ-completeness as automatic; `variable {d : DynkinSystem Ω}`. No join content. |
| 15 | `ConcreteOMLBlocks.lean:321–330` | V | `MeetsExist`, plus `meetsExist_of_orderIso`: latticehood is a property of the carrier *poset*, invariant under order-isomorphism. This is a representation-invariance fact already banked. |
| 16 | `SigmaEssentialOpenCore.lean:175–185` | V | `PolishRepresentable`: an opaque axiom. It is the only existing predicate quantified over representations. |
| 17 | `program_overview.md:296–302` | C | "concreteness and σ-completeness hold of every σ-class". |
| 18 | `program_overview.md:144–152, 359, 759` | C | MO₂ as `DynkinSystem`; the countable σ-class question; "Ψ on σ-classes/OMPs". |
| 19 | `frontier_map.md:35, 156, 162, 475–478` | C | "generated σ-class"; "concrete σ-class OML"; Φ for "exotic σ-classes". Stale doc (Aug 2026). |
| 20 | `spine_body.tex:170–200` | **C, opposite convention** | Quarantine thm: on Clo(X), "σ-additivity … reduces to finite additivity" (l.196–200). Countable additivity is tested *only over unions that land in Clo(X)*. Abstract joins (closures of unions) are not tested, so failures go into the Stone gap, not onto the state. |
| 21 | `spine_body.tex:173–178, 221–231` | U | Applies the σ-essential "recipe" clauses (0), (i) to Clo(X), comparing across the two conventions. |
| 22 | `spine_body.tex:242–247` | C | Surviving question stated for "concrete, σ-complete … orthomodular lattice". |
| 23 | `program_overview.md:511, 1023–1326`; `frontier_map.md:286–933` (OML-attack campaigns) | V, meet side | Finite repair campaigns inside `DynkinSystem` carriers. Typical lines: "the missing meet equals the disjoint union of its two old maximal lowers" (FM 895); "latticehood forces a nonorthogonal-cover meet that ordinary orthogonal closure cannot generate" (PO 1312–1314); "universal shadows commute with intersection but not with complement or union" (FM 803; `KernelClosureCalculus.lean`). All presuppose join = union for disjoint families; their object is the abstract meet vs. set intersection. |

The remaining paper-body hits are of two kinds. Most are set computations inside the σ-class
(Lem 5.6 table l.589–631, Lem 5.7 l.641–661, Thm 5.8 trimming l.672–681), which presuppose rows
1–2. The rest are false positives ("jointly" l.80, 122, 231, 241, 1021).

**Finding.** The corpus already makes the choice **both ways**:
- The σ-essential paper uses join = union, so the defect lands on the state.
- The spine's quarantine uses union-only testing on a non-σ-closed clopen carrier, so the defect
  lands in the gap.
- Lemma R Phase 2 (`regularity_sigma_additivity_pullback.md:178–297`, Clo ↪ Baire) is exactly the
  bridge between them.

Nothing in the inventory rests on Paper I or Paper II for the join convention:
- The spine's filtration S ⊇ S_σ ⊇ S_df is notation inherited from Paper II (now parked), but
  S_σ there is abstract σ-additivity.
- Paper I's corrected diagnosis (per-level vs glued σ-additivity, Andersen–Jessen;
  `PAPER_I_REVERSAL_CHECK.md:115–120, 160–173`) is itself an instance of *where* countable joins
  are computed: within each level, or in the ambient σ(𝒞). See Q3.

## Q2. Dependence of the main results

**Operational test, fixed before grading.**
- **CONSUMES**: the proof applies σ-additivity at a countable orthogonal family *and then uses
  that family's join as the set union*, for example its complement is countable or a point lies
  in it. Such a proof would break in a representation with a nonempty gap, because mass could sit
  on the gap (Lemma R).
- **DOES NOT**: the proof uses only closure of 𝓛 under ⋃ and complement, order = ⊆, or finite
  disjoint unions. Finite orthogonal joins are preserved by every OMP embedding, so they carry no
  choice.

Numbering is from `sigma_essential.aux`. **"Thm 3.5" does not exist in the current paper.**
- 3.5 is `rem:np-builds-rescuer`, a Remark.
- In `witness_candidate/sigma_essential_witness.md:111`, Theorem 3.5 is the Normal Form, which is
  paper Thm 5.8. So the brief's list double-counts it.
- Both readings are graded below, and Localization (Thm 3.2) is added as the likely intended
  §3 theorem.

| Result | Grade | Reason |
|---|---|---|
| Main thm 1.4 / 5.18 (`thm:main`, l.880–893) | **CONSUMES** | Part (1) is finite (via 5.16). Part (2) runs through 5.13. |
| Thm 5.13 rigidity (l.772–793) | **CONSUMES** | σ-additivity at singletons gives s = 0 on the countable set Ω∖U_α. That set is the join of singletons *as a set*. Then σ-additivity at the row: U_α = ⋃D_{α,n} is co-countable, so s(U_α) = 1, so one cell. In a gapped representation the row's mass can sit on the gap, which is exactly how m escapes (Rem 5.17). |
| "Thm 3.5" read as Normal Form = Thm 5.8 (l.663–683) | **DOES NOT** | Membership induction: P̃ is closed under complement and countable exactly-disjoint ⋃. No state, no join-vs-union comparison. |
| "Thm 3.5" read as Localization Thm 3.2 (l.221–244) | **DOES NOT** (countable joins) | Unfolds Def 1.2 by the Dirac/non-Dirac split. It depends on the **point set** (K(s₀) = ⋂, Lemma 3.1), which is the same choice seen from the point side (Q4, T4). |
| Cor 5.9 missing meet region (l.685–699) | **DOES NOT** | Consumes only 5.8 (membership). |
| Cor 5.11 incompatibility, not a lattice (l.720–734) | **DOES NOT** | Finite disjoint decompositions plus lower bounds under ⊆. It concerns the *meet* side, where abstract meet ≠ intersection, and exhibits that difference rather than assuming coincidence. |
| (extra) Thm 5.16 state (l.841–865) | DOES NOT | Finite pairs only. |
| (extra) Rem 5.17 (l.867–876) | CONSUMES | Books the row defect on m at the set union U_{α₀}. |

**Summary.** Only the rigidity chain (5.13 → 5.18(2), 5.17) consumes the coincidence. The normal
form, its corollaries and the state construction use only closure properties.

## Q3. Prior art inside the corpus

| Item | Where | What is banked | Bearing |
|---|---|---|---|
| Lemma R | `docs/regularity_sigma_additivity_pullback.md` (verdicts l.5–9; identity l.151–157; Boolean l.255–290; D-pointer l.313–317); ledger R-SA-1 (`site_regularity_prediction_ledger.md:179–240`) | Exact defect identity s(φ(⋁xₙ)) = Σs(φ(xₙ)) + s(g), OMP-valid, **FOLKLORE**. Boolean case: every finitely additive state lifts to Stone/Baire, defect = μ(G). | The accounting identity of the proposal, already banked and graded. |
| Dilation question D | `docs/dilation_question_scoping.md`; ledger D-DIL-1 (l.242–285) | Is every fa state a pullback s∘φ along a (deliberately non-regular) embedding into a σ-orthocomplete OMP? **OPEN — ADJACENT — PARKED, no months-scale commitment.** Checkpoint: Navara's 𝓛_ℕ. | This is the proposal's only live mathematical question, and it is already scoped and parked. |
| Site-regularity Phase A | `docs/site_regularity_intrinsic_and_state_coupling.md:19–199`; memo `site_regularity_decision_memo.md` (**DETOUR**) | Non-regular ambient embeddings reconcile meets that regular ones cannot. "Ambient repair ≠ regular-site repair." | The meet-side version of "make the choice visible", already run and closed as DETOUR. |
| Site-regularity Phase B / ULAM-B-1 | same doc l.201–356; ledger l.125–177 | Adjoining A∩B to L₁ destroys finite coherence. σ-essentiality is **not invariant under same-base completion**. | A change of *logic*, not of representation. It shows the logic-side movement. |
| Resolution antitonicity | `docs/resolution_dependence_scoping.md`; ledger RES-ANTI-1 (l.446–506) | Coherence is antitone in same-base carrier inclusion. "**Nonprincipality itself is representation-relative**" (l.98). "**No representation-invariant canonical block resolution is present in the corpus**" (l.114–115). Closed, CORPUS-INTERNAL. | The nearest existing statement that Dirac-ness depends on representation. |
| Quarantine | `spine_body.tex:170–231`; mechanism audit `dilation_question_scoping.md:226–285` | On compact clopen carriers, fa two-valued states are point restrictions and charges are premeasures. | Boolean instance of the move "represent so that all states are points; gaps absorb the defect" (T4 below). |
| Meet ≠ intersection | paper l.341–346, 365–374 | The paper's own one-obstruction thesis (meet side). | The choice is already visible on the meet side. |
| CE irreducibility | `notes/unsorted/foundations/ce_nonderivability/ce_taxonomy.json` (`fact.ce_irreducibility`; registry `notes/taxonomies_index.json:79`) | No index or algebraic condition implies CE; an ultrafilter observer satisfies all of them and fails CE. Folklore (Łoś, Loeb, FHM). | CE is a property of the *charge* (per-level σ-additivity under Stone completion). The Paper I reversal (`PAPER_I_REVERSAL_CHECK.md:115–120`) moved the operative defect to glued vs per-level. **The step "hence finite data cannot fix the join choice" is not established anywhere in the corpus.** See Q4 (T7) for the one-line version that does hold. |
| "Non-neutral" | `grep -rniI 'neutral'` over the whole repo (archives excluded; 18 hits, all read) and over the memory dir (4 hits). Plus `privileged|by convention|a convention` over docs, programme, cyclic_marginal, sigma_essential, spine, WHY.md. **No non-neutrality claim found.** Hits are vocabulary ("query … neutral about any reality", CLAUDE.md:29; `theory_shape.md:34`), ecology "neutrality", dynamics "neutral fixed points", the archived neutral-operator framework, and editorial "neutral voice". | No banked non-neutrality claim exists. The nearest is RES-ANTI-1's "representation-relative" and "no representation-invariant canonical resolution". | The non-neutrality claim is new to the corpus *as wording*. Its content is RES-ANTI-1 plus the quarantine/σ-class convention split. |
| Paper II PR_dual | `papers/paper_ii/PAPER_II_REVERSAL_CHECK.md:15, 287–289` | Lattice homomorphisms "respect meets of questions nobody can jointly ask". | Adjacent, meet side. Parked. |

## Q4. Mathematics or taxonomy?

**Falsifier (Patrick's, from the brief, registered before this pass).** "The reframing is
taxonomy only" is refuted iff a nontrivial statement quantified over choices of representation
exists that is not a restatement of Lemma R.

**Bins (added by this pass, after hand exploration had begun, so not a clean pre-registration).**
A candidate is substantively empty if it is:
- (i) trivial transfer along an isomorphism or a σ-regular embedding;
- (ii) Lemma R or Fremlin 313C/416Q restated;
- (iii) the parked dilation question D;
- (iv) the standard representation of a concrete logic by its two-valued states (Gudder;
  Pták–Pulmannová);
- (v) an existing corpus theorem restated.

**Setting ⟦HAND⟧.**
- 𝓛 is a σ-orthocomplete OMP with a separating set of two-valued states.
- St₂ denotes its finitely additive two-valued states, and St₂^σ those σ-additive for *abstract*
  joins.
- A set representation is φ: 𝓛 → 𝒫(X), injective, sending ⊥ to complement and finite orthogonal
  joins to disjoint unions.
- φ_St(a) := {t ∈ St₂ : t(a) = 1} is the representation by all two-valued states.

| # | Statement | Status | Bin |
|---|---|---|---|
| T1 | **Every representation is a pullback of φ_St.** The point map π: X → St₂, π(x)(a) = [x ∈ φ(a)], gives φ = π⁻¹∘φ_St. The gap at an orthogonal family (xₙ) with join a is φ(a)∖⋃φ(xₙ) = π⁻¹(N), where N = {t : t(a)=1, t(xₙ)=0 ∀n}. So "the choice" is exactly **which answer patterns are promoted to points**, T = π(X) ⊆ St₂. | PROVED ⟦HAND⟧, folklore | (iv) |
| T2 | φ is gap-free on orthogonal families ⟺ T ⊆ St₂^σ. | PROVED ⟦HAND⟧, one line from T1 | (iv) |
| T3 | For order-embeddings, φ(𝓛) is a σ-class ⟺ φ is gap-free. **The σ-class axiom is precisely the selection of gap-free representations.** | PROVED ⟦HAND⟧ (headline argument plus order-reflection) | (i)/(iv) |
| T4 | Kernel in representation φ: K_φ(s₀) = π⁻¹(Ext(s₀)), with Ext(s₀) = {t ∈ St₂ : t↾B = s₀}. Hence s₀ is σ-essential ⟺ Ext(s₀) ≠ ∅ ∧ Ext(s₀) ∩ St₂^σ = ∅ ⟺ **s₀ has a point in some representation (φ_St) but in no order-embedding σ-class representation.** For ⟸, a σ-additive t ∈ Ext gives the σ-class representation Ω ⊔ {t}. Scope: the "no σ-class representation" half needs order-reflection, via T3. | PROVED ⟦HAND⟧ | (v) Def 1.2 + Lemma 3.1 + Thm 3.2 restated |
| T5 | **σ-essentiality is invariant across σ-class representations of the same logic, and not invariant otherwise.** Invariance comes from T3 plus Lemma R(a). Non-invariance: in φ_St(L₁), every finitely coherent pattern has a nonempty kernel (m ∈ K). φ_St(L₁) is not a σ-class, because m ∉ ⋃φ_St(D_{α₀,n}) while m ∈ φ_St(U_{α₀}). | PROVED ⟦HAND⟧ | (i) and (iv); the Boolean case is quarantine (i) |
| T6 | **Rigidity as uniqueness ⟦HAND⟧.** For L₁, every order-embedding σ-class representation is a point-inflation π⁻¹(L₁) with π: X ↠ Ω. Points are σ-additive (T2), hence Dirac (Thm 5.13); surjectivity follows from singletons. Conversely, a non-Dirac σ-state t would give the non-inflation representation Ω ⊔ {t}. So **Thm 5.13 ⟺ L₁ has a unique σ-class representation up to inflation.** Side-remark, ⟦HAND — unverified⟧, under the Derr–Williamson reading only (`PolishRepresentable` is an opaque axiom): Polish-representability of L₁ would reduce to a question about σ(L₁) alone. New thread; not pursued. | PROVED ⟦HAND⟧ | (v) Thm 5.13 restated |
| T7 | **Gap mass is an invariant of the state, not of the pair.** For any (φ, s) with m = s∘φ, s(g) = m(a) − Σm(xₙ). | PROVED, = Lemma R rearranged | (ii) |
| T8 | **Existence of a pair for a given m** is D. For **two-valued m on any σ-orthocomplete OMP P, D is trivially YES.** Take φ(a) = (m(a), a) into Q = 2 × P (σ-orthocomplete; injective through the second coordinate) and s = first projection, which is σ-additive. At the witness, φ_St into 𝒫(St₂) with s = δ_m also works, and gives s(g) = 1 on row α₀. Neither construction is recorded in `dilation_question_scoping.md`. The open part of D concerns non-two-valued states (and non-σ-orthocomplete P, through Harding–Wang Problem 2). | PROVED ⟦HAND⟧ (two-valued); general case OPEN | (iv); (iii) for the open part |
| T9 | **Finite data cannot fix the choice.** OMP embeddings preserve finite orthogonal joins, and a finite sub-orthoposet has no infinite orthogonal family. So the restriction of any representation to a finite B is gap-free, and no finite datum distinguishes σ-class from gapped representations. | PROVED ⟦HAND⟧, trivial | (i) |

**Verdict on the falsifier.**
- **By the letter: FIRES.** T1–T6 and T8–T9 are statements quantified over representations, and
  none is a restatement of Lemma R.
- **In substance: REFUTED as new mathematics.** Every candidate falls into bins (i)–(v): folklore
  representation theory, Lemma R, or restatements of Def 1.2 / Thm 3.2 / Thm 5.13.
- The falsifier as worded was too weak, since it excluded only Lemma R.
- The only non-folklore question in the region is D for non-two-valued states. It is already
  parked as ADJACENT and is not specific to this framing.

**Gradings.**
- "Taxonomy only": REFUTED (letter) / SUPPORTED (substance).
- σ-essentiality representation-invariant: PROVED within σ-class representations; REFUTED across
  all representations (T5).
- s(g) an invariant of the pair: REFUTED as stated. It is an invariant of m alone, which is
  Lemma R (T7).

**Flag: possible reversal on a parked item (D-DIL-1's named checkpoint), ⟦HAND — unverified⟧.**
The checkpoint is Navara's 𝓛_ℕ with a free-ultrafilter state. I read `navara_1992.pdf` (3 pp.,
on the shelf) in full. Notation from the paper: 𝒱 = 𝒯 × 𝒮 with 𝒮 finite and stateless, and
u = (1, 0); elements of 𝓛 are f = ⋁ v_C|C over disjoint C ⊆ M. Let E_f = {m : f(m) ≥ u in its
copy}.
- f ↦ E_f is an OMP morphism 𝓛 → 𝒫(M).
- Every state ω satisfies ω(f) = μ(E_f), where μ = ω↾{1|C}. The (0,s)-residues carry zero mass
  because s ↦ ω(⋁ᵢ(0,s)|Cᵢ) is a measure on the stateless 𝒮.
- So the unique extension of a two-valued state is two-valued, and T8 covers the checkpoint.
- More generally φ(f) = (Ê_f, f) into Baire(β M) × 𝓛 with s = ν(first coordinate) (Fremlin
  416Q) would dilate **every** state on 𝓛_ℕ.

Entry D-DIL-1 was not edited (one-entry rule). This needs an independent check before anything
is changed.

What the framing does buy is one sentence of exposition (T1/T3): **the σ-class axiom is the
choice "only σ-additive answer patterns may be points".**
- The paper never states this.
- Under the answers-first stance (points derived, not assumed) it is the correct reading of what
  the carrier type silently assumes.

## Q5. Placement

**The premise is stale.** "Ships first and alone" is recorded only in:
- `papers/spine/spine_body.tex:256–258` ("travels first and alone … Lean-certified");
- `papers/spine/notes/STATUS.md:56`;
- `notes/programme/shovel_plan.md:378` (stale, Aug 2026);
- `notes/programme/frontier_map.md:545` (stale, Aug 2026).

The authoritative `program_overview.md` 2026-10-27 addendum (l.14–15) and
`papers/sigma_essential/KNOWN_ISSUES.md:3–5` say:
- the Lean `Psi` is routine (Binder–Navara + 4-point fibre);
- the essentially-irreducible form is UNCLEAR;
- the measurable-cardinal remarks are false;
- the paper is **not dissemination-ready**.

So the paper is already delayed by its own fix list, not by anything here. Spine l.257
("Lean-certified") also contradicts KNOWN_ISSUES ("formalized in full" overclaims) and has not
been updated.

**Placement verdict.**
- **Not the σ-essential paper.** Putting the framing there would change its object. Its
  definitions are states over ⋃ on σ-classes, where the choice is a single point (T3). That would
  conflict with the paper's revision list and add scope to a paper that already has to shrink its
  claims. No delay should be taken on.
- **Not a spine section.** The spine is reference-only and its order section is stale. At most,
  one remark could note that quarantine (Clo(X), union-testing) and σ-essential (σ-class,
  join = union) sit at the two ends of T1's choice, with Lemma R Phase 2 as the bridge.
  Optional.
- **Programme docs only.** Two ways to file it:
  - a pointer from `dilation_question_scoping.md` to T8, since the two-valued concrete case of D is
    trivial;
  - this doc as the record.

  If Patrick wants it in the theory collection, the natural home is a single `concept` entry in
  `glued_carriers_taxonomy.json` ("points are a choice: T ⊆ St₂"), not a probe or conjecture.

**Conflict with "ships first and alone": NONE in effect.** The framing does not touch the paper,
and the recommendation is in any case superseded: the paper cannot ship until KNOWN_ISSUES is
cleared.

## Disposition

**FRAMING-ONLY.**
- The framing's mathematical content is already in the corpus (Lemma R, D, quarantine,
  RES-ANTI-1, site-regularity Phase A/B) or is folklore representation theory (T1–T9).
- Its one live route, D, is parked as ADJACENT. D is trivial for every two-valued state (T8), and
  possibly for D-DIL-1's named checkpoint too (flag in Q4, unverified).
- Not a NEW FRONT: no open statement specific to it.
- Not a DETOUR in the memo's sense: it costs nothing, and it surfaced one gap in the dilation doc
  (T8 and the checkpoint flag).
- Its keepable yield is exposition, T1/T3: the σ-class axiom is the silent choice "points =
  σ-additive answer patterns".

## WHY.md bearing

Question 3, hidden idealisation.
- The σ-class axiom quietly decides which consistent answer patterns count as points: only the
  σ-additive ones.
- Promote every consistent pattern to a point (φ_St) and the σ-essential pattern has a point; its
  failure moves into a gap.
- Nothing about the world changed. Only the bookkeeping of where "the rest of the row" lives
  changed.

Honest distance: this is a lens on the existing result, not a new one.
