# Structure from Observation — Programme Overview

## The Central Question

When an observer makes structured observations of a system — querying it at
increasing levels of refinement, recording outcomes, building a picture of the world
through measurement — what does coherence require of them?

The programme shows that coherence, pursued to its conclusion, requires probability,
dynamics, and reconstruction. Not as additional assumptions, but as what the
structure of observation already contains.

---

## The Three Papers

### Paper I — Probability from Observation

> **⚠ AUDITED + FIXED + PARKED 2026-06-23.** A two-pronged hostile audit found a
> FATAL proof error in the headline Stone-route claim (Prop "Support condition":
> it inferred the Stone measure concentrates on the *principal* ultrafilters
> `pure(Ω)` from concentration on the *countably-complete* ultrafilters Σ — the
> missing step is the σ-Loomis–Sikorski realization gap, the same failure mode
> that retired the companion note) and folklore contribution pieces (the Stone
> dichotomy is owned by Lacy 1974 / Bhaskara Rao 1983 = the paper's own cite /
> Choksi / Mallory–Sion; CE is a name for continuity-at-∅ by the paper's own
> remark). THE VISE: the realization hypothesis that fixes the proof collapses
> the Stone route to Kolmogorov, so no regime is both correct and novel. The
> paper's claims have been MADE HONEST (abstract, B2, Stone-main, Corollary now
> realization-conditional; CE demoted to a Proposition) and the paper is PARKED —
> no submission as a novelty/theorem paper. The CE/geometric-commitment content
> survives as honest exposition only. **The description below is the pre-audit
> framing and overstates the contribution; see banner + `PAPER_I_AUDIT_VERDICT.md`
> + memory `paper_i_audited_parked.md`.** (Paper II is unaffected.)

**What it shows:** A coherent family of observations determines a unique probability
measure on the observable σ-algebra.

**The argument has three routes, each illuminating a different facet:**

1. **Carathéodory route:** Bounded discriminability forces the observable distinctions
   to have σ-algebraic structure. Collective exhaustion (CE) — the condition that mass
   does not persist in events the completed observation sees as empty — is the
   irreducible condition that bridges structural coherence and probability. CE cannot
   be derived from any structural condition (proved via Łoś's theorem + finite-cofinite
   counterexample); it is a commitment the observer makes about the infinite, not a
   consequence of finite consistency. Given CE, compatible marginals extend uniquely to
   a global measure via Carathéodory.

2. **Stone duality route:** The same extension theorem approached from the other
   direction. Finite additivity on the cylinder algebra, combined with the compactness
   of the Stone space, yields σ-additivity without assuming it. CE reappears here not
   as an algebraic condition but as a support condition: the measure concentrates on
   the principal ultrafilters — on the image of the sample space inside its Stone
   compactification. The two routes illuminate the same theorem from opposite sides.

3. **The bridge:** The Stone space of the observable algebra is the natural compact
   completion of the sample space. This observation connects Paper I to Paper II: when
   reconstruction holds, the Stone space *is* the state space.

**CE metatheorem (now Paper-I internal synthesis; standalone note RETIRED
2026-06-23):** In the first-order language of Boolean algebras with finitely
additive charge, countable additivity is not first-order axiomatizable. This fact
holds and is used inside Paper I (cited to FHM 1990 / Łoś). The **standalone
companion note is RETIRED — do not submit**: its proof was broken (same defect it
was withdrawn for) and the corrected result is FOLKLORE (stated in FHM 1990, the
note's own cited ref; proved via Loeb 1975 saturation). Clears no contribution
bar. See memory `countable_additivity_note_proof_broken.md`.

**Lean:** `DiscriminabilityFoundations.lean`, `QuerySystem.lean`,
`StoneDualityExtension.lean`, `TopologicalQuerySystem.lean`,
`ProkhorovExtension.lean`, `DelayEmbedding.lean`

**LaTeX:** `papers/paper_i/probability_from_observation.tex` (complete, 8 pages;
revised 2026-05-09 — four-way main equivalence theorem added in §6)

---

### Paper II — Distributivity and the Commensurability of Empirical Adequacy and Realism

**What it shows:** Whether an empirically adequate theory admits a realist
completion depends on the algebraic structure of the observation algebra.
Distributivity is the exact dividing line.

**Vocabulary:** Three positions, each a constraint on where the dual-space
measure lives:
- **Empirical Adequacy (EA):** measure on the dual space agrees with all
  observations. No claim about an underlying Ω.
- **Probabilistic Realism (PR):** descent from the dual-space measure to a
  measure on an underlying realisation space.
- **Value-Definite Realism (VDR):** a global 2-valued homomorphism on the
  observation algebra — every observable simultaneously has a definite value.

These are nested: VDR ⟹ PR ⟹ EA. (PR itself splits into two grades —
PR_lattice / PR_dual — that the Boolean case fuses; see below.)

**The commensurability theorem (Theorem 4):**
- *Boolean case:* all three positions are commensurable. Every EA-theory
  admits a VDR-completion (via ultrafilters). The realisation is unconstrained.
- *OML case (dim ≥ 3) — CORRECTED 2026-06-03:* VDR is blocked
  (Kochen–Specker); partial VDR is context-dependent (Bub–Clifton). PR does
  NOT stay simply commensurable with EA: it splits. PR_lattice (σ-additive
  measure on the lattice) holds for L(H) via Gleason; but **PR_dual**
  (descent to a measure on the dual S₀(L(H)) concentrating on P(A)) **FAILS
  for every normal state** — the clustering argument (#1) shows no normal
  state extends to a charge on S₀(L(H)). So EA holds, PR_lattice holds,
  PR_dual fails. The earlier "EA and PR remain commensurable (Gleason)" line
  was the L(H) PR error, corrected in Paper II and the open-questions note.
  See `papers/paper_ii/two_grades_of_pr.md` (the two-grades vocabulary and
  the pending Paper II decision; the problem statement itself is the survey
  `notes/open_questions/oml_onboarding.tex`).

**Coherence filtration:** S(A) ⊇ S_σ(A) ⊇ S_df(A) with three transitions
of different character: pasting (topological), regularity (analytic),
sharpness (algebraic).

**Mathematical content:** Assembled from Stone duality, Kochen–Specker,
Gleason, Bub–Clifton, and McDonald–Bimbó (2023) OML duality. The paper
self-acknowledges: "the individual ingredients are known; what has not been
stated is the synthesis."

**Contribution type:** Type 4 (vocabulary — EA/PR/VDR enable the
commensurability theorem and coherence filtration) + Type 6 (exposition —
translates between algebraic logic, quantum foundations, and philosophy
of science). Strongest contribution in the programme.

**LaTeX:** `papers/paper_ii/distributivity_and_realism.tex` (~15 pages, complete)

**Lean:** `Commensurability.lean` (0 sorrys)

*Previous Paper II (dynamics/reconstruction) withdrawn 2026-05-11;
see `papers/archive/paper_ii_withdrawn/`. Withdrawal reason: all results
classical (Rokhlin, Doob, Chapman–Kolmogorov); the "disclosure" framing
was mis-stated (T assumed throughout, not derived from the measure).*

---

### Paper III — WITHDRAWN

**Status:** Canned (2026-05-13). Novelty audit revealed rediscovery throughout:
residual autocorrelation = Billings-Voon (1986), FNN noise sensitivity =
Rhodes-Morari (1997), elbow stopping = Lepski (1991).

**LaTeX:** `papers/archive/paper_iii_withdrawn/` and `papers/archive/paper_iii_canned/`

**Updated 2026-04-29:**
- `\ifdraft` conditional: `\draftfalse` in standalone (sketch proofs for arXiv),
  `\drafttrue` in `combined.tex` (full proofs for monograph). Three standard-technique
  proofs gated (McDiarmid/Rademacher concentration, NW bias, Sard-Smale d_eff);
  all conceptually novel proofs remain inline in both builds.
- Abstract compressed to 3 paragraphs (was 4); transitional paragraph merged into
  theorem-list paragraph.
- `Remark III:rem:info-horizon` (§3): information horizon L* = ⌊log₂n⌋ derived
  from first principles; makes fibre-dilution explanation explicit.
- `Remark III:rem:lyapunov` (§9): observable separation exponent λ_h = λ_1 μ-a.e.
  under bi-Lipschitz reconstruction; Paper III closes the deferred Lyapunov claim
  from Paper II Remark II:rem:lyapunov.
- **Re-evaluation resolved (Direction 1):** fibre-dilution picture made explicit
  via the information horizon remark; no structural reframing. Three-theorem spine
  retained.

---

## The Through-Line

Each paper takes the output of the previous as input:

```
Structured observations
    → [Paper I]   → probability measure P on (Ω, σ(CylGen))
                    Stone space St(C) as compact completion of Ω
    → [Paper II]  → conditional regularity kernel κ_Q; semigroup {Π_t}; K_t
                    reconstruction: St(𝒪_h) ≅ X when 𝒪_h = ℬ(X) mod μ
    → [Paper III] → finite-sample: δ̂ stopping rule achieves minimax rate
                    three witnesses certify reconstruction from data alone
```

The unifying object across all three papers is **observational indistinguishability**:
- Paper I: events that never separate across refinements (failure of CE)
- Paper II: identical conditional regularity (κ_Q(q,·) = κ_Q(q',·)); same delay orbit (Φ_h(x) = Φ_h(x'))
- Paper III: same delay vector at lag L — (x,x') ∈ R_L

The programme is complete when δ(L) → 0: the observable σ-algebra generates
the full σ-algebra. Note: this is strictly stronger than collision convergence
(μ⊗μ)(R_L) → 0, which only measures geometric fibre refinement. The bridge
theorem claiming their equivalence under fibre mixing is false (2026-05-14).

---

## The Three Obstructions

| Paper | Obstruction | Status |
|-------|------------|--------|
| I | Lack of CE | Proved irreducible (Łoś + finite-cofinite counterexample) |
| II | Lack of density (𝒪_h ≠ ℬ mod μ) | Characterised by density bridge |
| III | Hidden factor obstruction | Bridge theorem false; geometric ≠ algebraic |

**Updated 2026-05-14:** The bridge theorem (algebraic ↔ geometric reconstruction
under fibre mixing) is false. The core identity has a disintegration error (p_z
vs p_z² weighting). The skew-product counterexample (X = A^Z × B^Z, h(a,b) = a₀)
shows collision → 0 while δ = 1/4. The active direction is now a
negative/clarification note proving geometric and algebraic reconstruction are
inequivalent.

---

## Paper Status (updated 2026-05-18)

| Paper | Status |
|-------|--------|
| Companion note | ⛔ RETIRED 2026-06-23 (broken proof + folklore result; do not submit) |
| I | Synthesis, not novel. Complete, 7 pages |
| II | EA/PR/VDR framing novel; math classical. Complete, 9 pages |
| III | Withdrawn (rediscovery) |
| Fibre mixing | Dead (bridge theorem false) |

---

## Open Mathematical Frontiers

Ordered by downstream leverage:

**⚑ CURRENT STATUS 2026-07-02 — σ-essential: the frontier is now LOCALIZED to a named
technique, not "invent from scratch." The sharpening phase is DONE; what remains is human
mathematics.** This session took the 2026-07-01 "invent a non-distributive primitive"
frontier and localized it three notches. To be caught up on WHERE TO FOCUS, read THIS block.

- **IMPORT SWEEP COMPLETE** (`fact.import_sweep_complete`), stronger than "literature
  closed": every EXISTING object-class proposed as the skeleton bottoms at Wall A via a
  two-reason partition — **R1** Boolean-ambient ⟹ meet-closed ⟹ rescued, or **R2**
  non-concrete-where-non-distributive ⟹ fails C1 by Kochen–Specker. Swept: set-theory catalog
  [R1], manuals/Feldman–Wilce, pBAs + Abramsky–Barbosa duality [R2, atom-founded], **quantum
  relations/graphs** [R2, non-commutativity of M⊆B(H) = exactly what fails C1; II₁/tracial buys
  measure- not set-concreteness]. Geometric/topological variants foreclosed as a FAMILY
  (`fact.geometry_forecloses_family`): inside a block, Cantor uniqueness makes all refinement
  orders isomorphic; between blocks, topological gluing (Möbius = ℤ/2 twist = cohomology class)
  is razor-rescued. ⚠ import-complete ≠ impossibility.
- **THE FRONTIER HAS A NAME + A TECHNIQUE.** The missing object = a **combinatorial
  (non-operator-algebraic) source of NON-SEGREGATED non-distributivity** — the "fourth cell"
  past R1 / R2 / R3-segregated-∏ₙMO₂ (`fact.fourth_cell_spec`). The order-combinatorial gluing
  space is a **5-axis map** (`fact.gluing_axis_map`): 4 axes pinned by deaths (overlap
  richness, closure type, block size = **infinite ATOMIC**, centrality = non-central); the
  ONE open axis is **incidence shape**, and all that is known is **NOT a tree**. The positive
  route is the **realization-theorem push** (Navara–Rogalewicz / Harding–Navara build
  non-simplex/non-segregated state spaces by Boolean-block pasting → carry to concrete + σ
  SIMULTANEOUSLY). **Reading plan WRITTEN:** `notes/reading_directions/realization_technique_reading.tex`
  (dependency-ordered, anchored to the conjunction gap; Harding 2004 in hand confirms the
  concreteness half + locates the finiteness dependency).
- **WHY IT'S HARD, at max sharpness — the 3↔5 tension:** you need infinite ATOMIC blocks
  whose overlap-incidence is NOT a tree, but the only known way to BUILD infinite atomic
  blocks is iterated refinement, which IS a tree → Dirac-domination (the recursive-MO₂ death,
  `carrier.recursive_mo2_substitution`, now a Lean detector `TreeIncidence`, 0-sorry, axiom-clean).
  The tree that makes blocks infinite is the tree that makes σ-states Dirac.
- **IMPOSSIBILITY side: BLOCKED, not near.** The only live ¬Ψ lane = force state-concrete
  (i) → σ-tribe (iii); NO importable route (RDP⟺MV confines the machinery to the Boolean
  complement of the Ψ config; `strat.impossibility_i_to_iii`). The false universal "(A)
  infinite-atomic+non-central+concrete ⟹ tree" is strictly STRONGER than ¬Ψ (probably false —
  tree is a property of the construction, not the object), NOT a stepping-stone.
- **NARROWING IS DONE.** New-world and impossibility stay indistinguishable because ONE object
  gates both (a non-tree infinite-atomic gluing: build it → witness; prove none exists → ¬Ψ).
  "Keep tightening the lasso" now returns sampled points, not the theorem. The next move is the
  **investment decision**: learn the realization/pasting technique (plan written) or attempt the
  non-RDP (i)→(iii) theorem. Neither is manufacturable at the schematic.

**NET: the frontier is one named object — a concrete σ-complete OML built by INFINITE
NON-TREE pasting of infinite atomic Boolean blocks (= the realization-theorem push), OR a
non-RDP (i)→(iii) impossibility theorem.** Both are human learn-then-try; the paper
(`papers/sigma_essential/`) is the stable boundary map (unchanged — this session's directional
findings are correctly NOT in it, being search-navigation not Ψ-boundary). Zoom-out nav =
`sigma_essential_taxonomy.json`; trails = `sigma_essential_construction_runs.md` (2026-07-02
blocks); Lean scaffold 0-sorry incl. the tree-detector. (The prior "invent from scratch"
framing this localizes, and the earlier dated status blocks, are folded into the settled
results + session-history pointers below.)

### Settled results (de-dated — stated once, detail in the pointed-to files)

- **Localization / reduction (the spine, verified).** A concrete σ-essential witness
  exists iff **(i)** no point-evaluation (Dirac) extends the finite pattern *and* **(ii)**
  no non-Dirac σ-additive two-valued state does — and (i) is freely arrangeable
  (Navara–Pták), so the entire content is clause (ii) = Wall A. Machine-checked (Lean
  `localization`, 0-sorry). Full statement: `notes/open_questions/sigma_essential_reduction_writeup.md`.
- **Derr–Williamson Polish boundary (`rem:dw`).** On a Polish-representable carrier every
  finitely-coherent pattern globalises — no witness (DW 2023 Thm D.6, via Maharam §8, the
  topological hypothesis load-bearing). A witness must therefore be **non-Polish /
  non-standard-Borel**. Backing: `notes/open_questions/sigma_essential_prior_art_verdict.md`;
  stated in the survey `oml_onboarding.tex` (`rem:dw`).
- **Import sweep complete + the fourth-cell spec + the 5-axis gluing map** — the current
  frontier's structural results; see the 2026-07-02 block above and the taxonomy facts
  `fact.import_sweep_complete`, `fact.fourth_cell_spec`, `fact.gluing_axis_map`.

### Session history (trails, not current state — pointers only)

The reasoning trails behind the frontier live in the leaves, not this overview:
`sigma_essential_construction_runs.md` (2026-06-25 → 07-02 trails, incl. the import
sweep, the recursive-MO₂ death, the geometry foreclosure), `sigma_essential_taxonomy.json`
(zoom-out index of every recorded approach), `sigma_essential_large_cardinal_bounds.md`
(§3f–§3s move-space sweep = the 06-27 "literature closed" + 07-01 "invent from scratch"
framings, both superseded by the 2026-07-02 frontier), `forcing_programme_status.md`
(forcing parked-as-premature), and `notes/archive/sigma_sessions_1_8b_narration.md` +
`archive/sigma_duality_targets_superseded.md` (the earliest sessions, archived). The
forcing scout, σ-duality two-hull probe, and B–W masa-transfer threads all bottomed at
the same Wall A and are recorded there.

Previously listed directions closed or parked:
- **Mechanistic feasibility from observational coherence** — PARKED
  (2026-06-08). Type 6/4 audit FAIL. The "descent ladder unifies four
  feasibility literatures" reading is afternoon's relabeling: R1–R3
  (marginal problem / set identification / specification testing) are one
  field, R1↔R2 bridge already in Molinari (Handbook of Econometrics Vol 7A,
  2019, via Artstein); only R2↔R4 (set ID ↔ Takens) is unstacked, and it's
  unstacked because nobody needs it — the dynamics side already answers
  feasibility natively (functional observability 2301.04108;
  Botvinick-Greenhouse JSP 2025). σ-additivity layer DECORATIVE for
  feasibility (CE non-derivability ⟹ invisible to finite tests). Fourth
  death of the empirical-reconnection arc, same R4 rock as
  relational-reconstruction. Never touched the live OML descent frontier.
  See `notes/covered_leads/descent_ladder_mechanistic_feasibility.md`.
- **Five-traditions unification** — DEAD (2026-05-18). Abramsky
  inclusion is a category error (compact contextuality ≠ non-compact
  σ-closure). Candidate theorem assembles KVP (1950) + Seidenfeld et
  al. (1984) + vacuous reduction — no new equivalence. Removing
  Abramsky reduces thesis to Howson (2008) with fancier coordinates.
- Geometric ≠ algebraic reconstruction — known/obvious (audited)
- Entropy witness concentration — dead (depended on false bridge theorem)
- Fibre mixing derivability — dead (bridge theorem false)
- **Coherence/completion paper** — PARKED (2026-05-18). Howson (2008,
  BJPS) already identified the core observation (de Finetti's consistency
  has compactness; σ-additivity lacks it; "missing completeness theorem"
  p. 17). Thread restates Howson with ultraproduct proof. Salvage: 2-3
  sentences in companion note intro. See plan for full audit.
- **KVP + non-axiomatizability merger** — DEAD (2026-05-18). Headline
  theorem is 5-line Tarski corollary (folklore). Salvage: footnote in
  companion note.

Dead signposts:
1. **CE as sheaf condition** — DEAD (2026-05-17). Dictionary
   translation per Biesel/Zafiris/Caramello. Archived.

Open directions — the extension boundary:

> **Core question:** What structural conditions on an algebra of
> propositions force honest (σ-additive) probability?

2. **Ultralimit question** — SCOPED (2026-05-18). Reduces to
   Strategy D via canonical decomposition. Settled in all regimes
   except non-σ-complete non-atomic (where measure-free factor
   iff failure). On P(N), trivially answered (Krein-Milman).
   Duanmu-Weiss (2018), Cardona et al. (2025), Fremlin §326-328
   checked — none address this question. Not an independent
   direction.
3. **Strategy D** — Does there exist a non-σ-complete non-atomic measure-free
   Boolean algebra? **KILLED AS A CONTRIBUTION 2026-06-18 (/audit full, prior-art).**
   The answer is YES in ZFC and the worked witness (`Clop(Y,𝔗)` not σ-complete,
   gap family `A_k=[0^{k-1}11]` at `0̄`) is correct math — but it clears **no
   contribution bar**. **Gaifman 1964** (PJM 14(1):61–73, Thm 2.2 + property (†))
   already exhibits, IN ZFC and 19 years prior, an atomless BA with no strictly-
   positive FINITELY-additive measure — strictly stronger than the no-σ-additive
   leg. The non-σ-complete + atomless conditions are trivial; the only hard
   ingredient (measure-freeness) is Argyros's published theorem. "Strategy D" was
   this programme's PRIVATE name, never a field-recognized open problem; the
   "likely ZFC-independent" prior was a local misreading (σ-completeness read off
   the completion/Gleason cover, not the base algebra — C–N 6.23/6.25 record the
   completed forms). L_MO₂-shape kill (true + trivial + occupied) — the first kill of the Strategy-D (a)-line, NOT a descent-arc death.
   RETIRED as a research target. Survives: a one-line Gaifman-1964 citation, no
   contribution. Verdict:
   `notes/archive/strategy_d_killed/ultralimit_investigation/strategy_d_AUDIT_VERDICT.md`;
   the `..._RESOLVED.md` writeup carries an AUDIT-KILL banner (math retained);
   memory [[strategy_d_resolved]].
4. **OML extension problem** (algebraic face) — What replaces
   Carathéodory when the algebra isn't Boolean? Pták-Pulmannová
   (1994): conditions strong enough to force σ-additivity collapse
   OMLs to Boolean. Gleason handles L(H); general case open.
   Sharpened 2026-06-02: extension splits into two axes — the
   *extension axis* (state → charge on the full clopen Boolean
   algebra of S₀(A)) is blocked by non-distributivity and is NOT
   governed by σ-additivity; σ-additivity governs only the *descent
   axis* (concentration on physical points). Boolean fuses them
   (extension free); OML separates them (extension is the open
   problem). See the survey `notes/open_questions/oml_onboarding.tex`
   (archived predecessor: `notes/archive/oml_extension_problem_superseded.md`).

   **Descent-axis history (Sessions 1–8b, 2026-06-10 → 06-17) — ARCHIVED.** The full
   reasoning-trail (L_MO₂ kill+reframe, the five-property death map, band-family
   trichotomy→dichotomy, the Harding–Wang wall, the Lean bites) is relocated verbatim
   to `notes/archive/sigma_sessions_1_8b_narration.md` (it predates the 2026-06-25
   reduction and the 2026-07-02 frontier — read as history). Current state: the
   frontier block at the top of this section + `sigma_essential_taxonomy.json`. Later
   trails (06-25 → 07-02): `sigma_essential_construction_runs.md`.
5. **Foundational topology / zeta** — speculative.

---

## Repository Layout

- `papers/paper_i/` — Paper I (synthesis, expository)
- `papers/paper_ii/` — Paper II (EA/PR/VDR, strongest contribution)
- `papers/archive/` — all withdrawn/canned/dead papers
- `formalization/QuerySystem/QuerySystem/` — Lean source files
- `notes/knowledge_map/` — research control panel
- `notes/open_questions/` — precise, open, dormant (re-audit on new input)
- `notes/reading_directions/` — guided reading with questions
- `notes/programme/` — programme-level docs
- `.claude/agents/` — 7 custom agents
