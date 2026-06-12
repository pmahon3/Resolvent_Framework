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

**CE metatheorem (companion note):** The same ultraproduct argument shows the
obstruction is not an artifact of the query-system formalism — in the more primitive
first-order language of Boolean algebras with finitely additive charge, countable
additivity is likewise not first-order axiomatizable. Companion note (3 pages)
proves this in full.

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
  `notes/open_questions/oml_onboarding.{tex,md}`).

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
| Companion note | Complete, 3 pages |
| I | Synthesis, not novel. Complete, 7 pages |
| II | EA/PR/VDR framing novel; math classical. Complete, 9 pages |
| III | Withdrawn (rediscovery) |
| Fibre mixing | Dead (bridge theorem false) |

---

## Open Mathematical Frontiers

Ordered by downstream leverage:

**Status 2026-06-12 (two open problems, both uninhabited; no confirmed lead).**
After the L_MO₂ concreteness kill (2026-06-10), the descent axis had an *afterlife*
(2026-06-11/12): pursuing it under **Reading 1** (relational = no hidden
realisation; user's chosen framing) reduced the prize to a sharp, principled,
**uninhabited** open problem — *is there a σ-complete concrete OML carrying a
σ-essential contextual state?* — which reconnects to CE/Paper I (a compactness
failure). Simultaneously **Strategy D** advanced: its step 1 (is `Clop(Yₙ)`
σ-complete?) is now a GJ-grounded reduction to two precise sub-questions
(limit-branch witness; strong-zero-dim sub-lemma). So the frontier is **two
well-posed open problems with identified levers, neither inhabited** — not "no
leads," not "confirmed leads." Both are (a)-aligned (incompatibility face = OML
descent; anti-smuggler face = Strategy D). Working layer:
`notes/open_questions/{reading1_prize_reduction,direction2_gate_finding,subsession_sigma_essential_via_CE}.md`,
`papers/paper_i/notes/ultralimit_investigation/argyros_sigma_completeness_{handoff,scratch}.md`.

The L_MO₂ kill itself stands (6th death of the arc: L_MO₂ **IS** concrete —
conjecture "richness starves concreteness" FALSE as worded — but the witness is
trivial, ∏ₙ MO₂ has the bundle, and the Boolean boundary is Pták–Pulmannová 1994's
*subadditivity*). Canonical kill record (parked):
`notes/covered_leads/descent_axis_residue_post_kill.md`. The reframed live problem
supersedes it as the *open* question.

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
3. **Strategy D** — Does there exist
   a non-σ-complete non-atomic measure-free Boolean algebra?
   Equivalently: compact, totally disconnected, no isolated points,
   not basically disconnected, no strictly positive Radon probability.
   Likely independent of ZFC. Nearest examples (Argyros, Kunen,
   Fedorchuk) miss at least one condition. Plebanek (2024 survey)
   confirms the exact parameter regime is open.
   **Step 1 advanced 2026-06-12 (GJ-grounded):** "is `Clop(Yₙ)` σ-complete?"
   (the Argyros pre-Gleason candidate) reduces via Gillman–Jerison 1H/6M/6W to two
   precise sub-questions — a limit-branch witness (strictly increasing clopens with
   no least upper bound ⟹ ZFC example) and a named strong-zero-dim sub-lemma.
   See `papers/paper_i/notes/ultralimit_investigation/strategy_d_dossier.md`
   (+ `argyros_sigma_completeness_handoff.md`).
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
   problem). See the survey `notes/open_questions/oml_onboarding.{tex,md}`
   (archived predecessor: `notes/archive/oml_extension_problem_superseded.md`).

   **Descent-axis status — L_MO₂ KILLED 2026-06-10, then REFRAMED to a live open
   problem 2026-06-11/12.** The extension axis is fully closed on L(H) (no state
   extends, Prop 3.2). The L_MO₂ concreteness lead was killed by `/audit full` (the
   three findings below). **But the axis did not stay closed:** pursued under
   Reading 1 it reduced to a sharp, principled, *uninhabited* open problem (see the
   afterlife note at the end of this item). First the kill, then the reframe.

   The audit resolved the question — *is L_MO₂ concrete?* — and killed the lead on
   a cell the framing did not predict. **L_MO₂ IS concrete** (so "richness starves
   concreteness" is FALSE as worded), via three findings:
   - **The loaded premise was false.** V is a **Kalmbach horizontal sum (blocks
     glued only at {0,1})**, NOT atom-sharing Greechie pasting (Navara p. 428,
     read directly: "construct the horizontal sum 𝒱 … see [5] [=Kalmbach
     1983]"). Pure horizontal sums of concretes are concrete; **statelessness**,
     not the horizontal sum, was Navara's only source of non-concreteness, and
     the MO₂-swap removes it. Concreteness is then mechanical (MO₂ → 𝒯×MO₂ →
     hsum → W=∏V → L⊆W, order inherited / separation restricts).
   - **No contribution — trivial + occupied.** The full bundle (concrete +
     σ-orthocomplete + non-Boolean + (★)) is exhibited by plain **∏ₙ MO₂** with
     zero Navara scaffolding; the constancy-cut existed to extract non-σ-additive
     states from a *stateless* block and is inert once the block is stateful.
     Types 1/3/5 FAIL on triviality.
   - **Already characterized, more sharply.** **Pták–Pulmannová 1994**: an OML is
     Boolean iff it has a unital set of *subadditive* measures — the forcing
     property is **subadditivity**, not σ-additivity/concreteness. The conjecture
     named the wrong discriminator.

   6th death of the arc, NEW reason (triviality + prior-art, not decorative-σ and
   not the predicted concreteness-failure). The (★)=YES Lean structure stands as
   established but was always irrelevant to the kill. Nothing routed to Paper II.
   Canonical record (parked): `notes/covered_leads/descent_axis_residue_post_kill.md`;
   derivation history (archived): `notes/archive/oml_descent_inhabitation_dead/inhabitation_check.md`.

   **AFTERLIFE — the reframed live problem (2026-06-11/12).** Pursuing the descent
   question under **Reading 1** (relational = no hidden realisation; the user's
   chosen framing of the (a)/(b) fork) reduced it, via Fine's theorem, to a
   *contextuality* question: a relational measure ⟺ a **contextual** state (not
   spanned by the dispersion-free states). Bounded by Wright 1978 (a *finite*
   concrete OML with a contextual state), the only live cell is **σ-essential**
   contextuality — contextual in the σ-complete whole but in no finite sub-OML, a
   *compactness failure* that reconnects to CE/Paper I. Status: well-posed,
   principled, **uninhabited** (no witness — ∏ₙMO₂ fails it, Wright is finite — and
   no impossibility proof); two Phase-4 exits (build a σ-essential witness / prove
   a spanning-impossibility). The CE-routing subsession (2026-06-12) returned
   **GAP** — CE can't settle non-emptiness; the Boolean Stone-kill of ∏ₙMO₂ doesn't
   transfer (it controls only the Boolean center, vacuous off-center). This
   **sharpens both exits**: a witness must put its infinitary structure off-center
   (irreducible/non-central-infinite — products of finite blocks excluded; pasting
   constructions the place to look), and the impossibility direction can't reuse
   the ∏ₙMO₂ mechanism. The survey `notes/open_questions/oml_onboarding.{md,tex}`
   is committed to this Reading-1 framing; working layer:
   `reading1_prize_reduction.md`, `sigma_essential_nonemptiness_finding.md`,
   `direction2_gate_finding.md`, `subsession_sigma_essential_via_CE.md`.
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
