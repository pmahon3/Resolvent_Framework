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

**Status 2026-06-17 (two open problems; OML descent now carries a LANDED structural
dichotomy, not a verdict; no confirmed lead).**
After the L_MO₂ concreteness kill (2026-06-10), the descent axis had an *afterlife*
(2026-06-11/12): pursuing it under **Reading 1** (relational = no hidden
realisation; user's chosen framing) reduced the prize to a sharp, principled,
**uninhabited** open problem — *is there a σ-complete concrete OML carrying a
σ-essential contextual state?* — which reconnects to CE/Paper I (a compactness
failure). A multi-day hand+compute+lit+advisor push (2026-06-17) then **landed a
structural dichotomy** (see `[[sigma_essential_construction_attempt]]` memory):
the **sharp theorem** `S_df^σ(L) = S_df ∩ ⋂_{block B} O_B` (O_B = principal-on-B,
open) gives **≤ℵ₀ atomic blocks ⟹ μ(fakes)=0 ⟹ no leak / Exit B** (any ground
set) — conullity via per-block-nullity + countability, *not* via G_δ-ness (G_δ
⟹ conull is false in general; `S_df^σ` G_δ is a parallel topological restatement,
not the cause). A **necessary condition** for any witness: *uncountably many infinite
atomic blocks* (S_df^σ non-G_δ). The escape routes were pinned: **(A)** a single
non-atomic block is **struck** (Boolean ⟹ reducible + distributive, violating the
irreducible + non-Boolean prize constraints); **(B)** *uncountably many atomic
blocks on ℕ* (|L|=𝔠, countable ground set — the partition-logic non-G_δ question)
is the **only** live route, and is the old "(1)+(2) frontier" correctly relabeled.
Retracted en route (flag discipline, ~9 reversals): the "RESOLVED ⟺ measurable
cardinal" verdict, the barycenter-cancellation question (not truth-apt), "Strategy D
= same object" (NO at the lattice level — SD is Boolean/distributive, the OML leak
needs non-distributivity; the `[[mixing_barycenter_transfer_rhyme]]` RHYME verdict
stands — but right-flavored at the *measure* level), and "ℕ likely Exit B" (illusory:
|Ω| countable ⇏ |L| countable). So the descent frontier is now **one landed theorem +
a single well-posed research-level construction target (B)**, not "two Phase-4 exits."
Simultaneously **Strategy D** advanced: its step 1 (is `Clop(Yₙ)`
σ-complete?) is now a GJ-grounded reduction to two precise sub-questions
(limit-branch witness; strong-zero-dim sub-lemma). So the frontier is **two
well-posed open problems with identified levers, neither inhabited** — not "no
leads," not "confirmed leads." Both are (a)-aligned (incompatibility face = OML
descent; anti-smuggler face = Strategy D). Strategy D's strictly-positive-measure
machinery is now the right toolkit for (B)'s *measure-level* obstruction (the one
honest reconnection between the two problems — at the measure axis, not the lattice).
Working layer:
`notes/open_questions/{reading1_prize_reduction,direction2_gate_finding,subsession_sigma_essential_via_CE}.md`,
`papers/paper_i/notes/ultralimit_investigation/argyros_sigma_completeness_{handoff,scratch}.md`;
full session reasoning in the `[[sigma_essential_construction_attempt]]` memory.

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
   (+ `argyros_sigma_completeness_handoff.md`). **Pen-and-paper kit:**
   `problemset_strategy_d.{tex,pdf}` (self-contained working problem-set).
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
   the ∏ₙMO₂ mechanism.

   **STRUCTURAL DICHOTOMY LANDED (2026-06-17, hand+compute+lit+advisor; full record
   in the `[[sigma_essential_construction_attempt]]` memory).** Not a verdict — but
   the question now has proved structure:
   - **Sharp theorem.** `S_df^σ(L) = S_df ∩ ⋂_{block B} O_B`, where `O_B = {s :
     s principal on B}` is open in the compact space `S_df`. Hence **≤ℵ₀ atomic
     blocks ⟹ μ(fakes)=0 ⟹ every σ-additive state is non-contextual (Exit B)**,
     on *any* ground set — conullity via per-block-nullity + countability (each
     `{free on B}` null by the cofinite tail-chain + Step A; countable union of
     nulls is null), **not** via `S_df^σ` being `G_δ` (`G_δ ⟹ conull` is false in
     general; the `G_δ` characterization is a parallel topological sibling, see
     the caveat below). On *any* ground set. (Corrected "countable-block
     theorem": the hypothesis is *atomic* blocks — free on ℕ, a genuine extra
     condition off ℕ; via the proved Steps A,B + F1 block-σ-closure, with no
     cross-block intersection. F1 is the single load-bearing lemma.)
   - **Necessary condition for any witness:** *uncountably many infinite atomic
     blocks* (so the 𝔠-fold `⋂_B O_B` is non-`G_δ` — leak room). The would-be
     "Exit B on ℕ" is the *boundary* of the theorem, not a fixable gap.
   - **Escape routes pinned.** **(A)** a single non-atomic block is **struck** — it
     is Boolean ⟹ reducible + distributive, violating *irreducible + non-Boolean*;
     its statelessness is the atomless-measure-algebra (distributive) kind, not the
     non-distributive kind an OML-descent witness needs. **(B)** *uncountably many
     atomic blocks on ℕ* (|L|=𝔠, countable ground set; the partition-logic
     non-`G_δ` question) is the **only** route respecting the prize constraints —
     it *is* the old "(1)+(2) frontier" relabeled. Compute cannot touch (B): finite
     truncations have finite atomic blocks ⟹ `S_df = S_df^σ` ⟹ Exit B by König; it
     is infinitary hand-analysis.
   - **Caveat for (B):** `S_df^σ` is *not* just the point-evaluations `{δ_n}` — a
     consistent atom-thread is principal-on-every-block (σ-additive by F1) even when
     it is no point of ℕ, and `w` must be separated from `closed-conv` of *all*
     such threads.
   - **Honest reconnection to Strategy D:** at the *lattice* level the two problems
     are different objects (Strategy D Boolean/distributive — the
     `[[mixing_barycenter_transfer_rhyme]]` verdict stands); at the *measure* level,
     "can μ dodge an uncountable union of fake-sets on the compact zero-dim `S_df`"
     is strictly-positive-measure-flavoured, so Strategy D's machinery is the right
     toolkit for (B)'s obstruction.
   - **Lit read this session (from PDF):** Tkadlec 1998 (concrete σ-logic +
     3-covering ⟹ Boolean; escape = fail finite-covering, which MO₂ already does;
     c-orthocomplete ⟺ σ-orthocomplete on countable Ω), Müller 1993 (non-Boolean
     all-states-Jauch–Piron needs |L|=ω₁, MPT Thm 4.1 = no countable *L*; Thm 2 needs
     *complete* not merely σ-complete — the σ-complete crack is where a witness lives).

   **SESSION 2 (2026-06-17) — RE-VERIFIED + LATTICE LEVEL CLEARED + FRONTIER SHARPENED.**
   Re-verified F1, Step A, and the measure conclusion by hand + advisor (one method
   fix: μ(fakes)=0 routes through per-block nullity + countability, *not* through
   G_δ-ness — `G_δ ⟹ conull` is false in general; the G_δ statement is a topological
   *sibling*, not the premise). **Lean ruled out:** Mathlib v4.29.0 has no
   orthomodular-lattice / Foulis–Holland infrastructure, and F1 (= Kalmbach) and
   Step A (= standard OML measure theory) are known ⟹ axiom-with-citation, not
   formalize. Attacked Exit (B) by construction (failure-mode = impossibility proof):
   - **The lattice level is NOT where the verdict lives.** Retrieved the verbatim
     lattice gate (Svozil–Tkadlec Thm 2.5: "no order-4 loop ⟺ lattice"; astroid =
     4-cycle, Dichtl 1984). Lattice-ness and proper below-top cross-block *binding*
     **coexist** (astroid-free regime; n-cycle pastes n≥5 are lattices). The verified
     pentagon is irreducible + binding + lattice + genuinely contextual *finitely* ⟹
     substrate mechanics are achievable, not the obstruction.
   - **Load-bearing negative:** the entire pasting lattice theory is *uniformly
     chain-finite* (Harding–Heunen–Lindenhovius–Navara arXiv:1711.03748: "Greechie
     diagrams apply only to chain-finite OMPs"). **No published lattice criterion for
     infinite-chain pasting, no σ-completeness criterion for any infinite paste** —
     a genuine gap, no prior art to collide with.
   - **Loops are MOOT for the verdict:** a loop has *countably many* blocks ⟹ by the
     landed theorem, Exit B both branches. The Greechie/loop intuition driving the
     whole arc *cannot reach* the uncountable-block regime. Route B is **not a loop**
     — it is an uncountable *family* of countable partitions of ℕ sharing atoms.
   - **Two-block germ retired:** irreducible + proper binding is impossible at two
     blocks (any shared non-{0,1} element is central ⟹ reducible; share only {0,1} ⟹
     no binding). The germ is ≥3 blocks. *Not* Exit-B evidence — wrong block count.
   - **Errors caught at the threshold (not hardened):** the singleton-collapse horn
     (`{n}=⋂{S∋n} ⟹ Boolean`) is *Boolean reasoning* — in the binding/non-distributive
     case lattice-meet is strictly below set-intersection, so the meet-gap can keep
     `{n}` out; the horn bites only where there is no binding (= MO_𝔠, dead). So the
     antagonism is **not** proven forced.
   - **Five-property death map** (the accurate "why this is hard"): a witness needs
     five orthogonal properties — *count* (uncountably many blocks), *size* (infinite
     atomic blocks), *binding* (proper below-top cross-block joins), *irreducible*,
     *concrete + σ-complete*. Each prior death secured all but one: loops — count ✗
     (countable); MO_{ω₁} — size ✗ (finite blocks); ω₁-horizontal-sum of P(ℕ) —
     binding ✗ (cross-joins collapse to top); two-block — irreducible ✗ (centrality);
     Navara-over-concrete — concrete ✗ (statelessness needs the exotic base).
   - **★ The sharpest open frontier (Route B, tied to its closest near-miss):** the
     ω₁-horizontal-sum of P(ℕ) already secures count + size + irreducible + concrete +
     σ-complete and dies *only* on binding. So the frontier is precisely: **can genuine
     below-top binding be added to the ω₁-horizontal-sum of P(ℕ) without (a) collapsing
     cross-joins to top, (b) breaking the lattice, (c) breaking σ-completeness, or (d)
     reintroducing singletons** — carrying a σ-additive `w` off `closed-conv(S_df^σ)`?
     Only attacks left: a pure-hand explicit construction, or a forcing/impossibility
     theorem — both research-level. Deliverable = a sharpened Exit-B *lean*, **not a
     verdict**.

   **SESSION 3 (2026-06-17) — SINGLE COUNTABLE JOINS ARE TAME; *IF* there is an
   obstruction it is state-level (transfinite-completion still open).** A new structural
   theorem and a state-level reformulation, turning the lean into a three-layered "why
   this is hard" map:
   - **Block-local-join theorem (new, hand-verified):** in a σ-complete *lattice* OML,
     *every* countable join lies in a single block (orthogonal-increment construction
     `e_{n+1}=J_{n+1}∧J_n^⊥` + F1). Hence orthocomplements of countable joins are clean
     set-complements, interior overshoot cannot happen infinitarily (only inherited from
     finite astroid-level joins), and there is **no OML-lattice analogue of the
     Strategy-D limit branch at the single-join level**. NOTE the hypothesis is "*in* a
     σ-complete lattice OML" — the theorem shows joins are tame *given* the substrate; it
     does **not** show the substrate *exists*. **The transfinite-completion question —
     does a binding paste σ-complete to a concrete non-Boolean irreducible *lattice*?
     (Harding: an OMP need not embed in any σ-complete OMP) — remains OPEN and is still
     substrate/lattice-level.**
   - **(d) fully closed, binding-independent:** countable meets can't make singletons
     (`⋀A_k =` largest L-elt `⊆⋂A_k = ∅` when `{n}∉L`) and the dual kills co-singletons;
     the non-distributive meet-gap protects singleton-freeness for free, robust through
     transfinite iteration.
   - **Tkadlec route dead:** binding ⟺ covering-*failure* (a proper cross-block `A∩B`
     with no L-element below it *is* the covering failure; σ-completion preserves the gap
     permanently), so the covering theorems can never trigger.
   - **State-level reformulation (where the verdict actually lives):** the σ-essential
     leak ⟺ a finite consistent partial atom-selection across blocks that extends to a
     global df-state but to **no full σ-additive thread** — a **non-compact**
     inverse-limit obstruction on the 𝔠-family (each factor `atoms(B)` is
     countable-discrete, non-compact, so the Bourbaki–Steenrod argument that gives
     `w∈closed-conv(S_df)` fails for `S_df^σ`; the missing compactness is the
     free-ultrafilter room). Equivalent to the earlier Hahn–Banach necessary condition;
     not finitely checkable; family-dependent.
   - **Net:** *if* there is an obstruction it is neither single-join-lattice nor
     measure-on-ℕ but a **non-compact thread-extension** phenomenon on the 𝔠-family —
     with the transfinite-completion (Harding) lattice question still open alongside it.
     Verdict unchanged (sharpened Exit-B lean, not a verdict; could still be Exit A);
     the two research-level attacks stand. Stopped per the armed stop-gate. Full record:
     `[[sigma_essential_construction_attempt]]` memory.

   **SESSION 4 (2026-06-17) — PRIMARY-SOURCE READ: Surface 1 (transfinite completion)
   is a STUDIED problem with PUBLISHED negative results.** Read Harding–Wang
   arXiv:2108.09819 §3 in full (now in the library). Findings, decisive for the
   construction side:
   - **Concrete OMLs form a variety that is NOT closed under MacNeille *or* canonical
     completions** (Harding–Wang Rmk 3.14 / Thm 3.13). Completing a concrete OML
     generically leaves the concrete class — exactly the Surface-1 collapse risk,
     confirmed.
   - **No *regular* (join-preserving) completion exists for OMLs** (Cor 3.9); there is
     an OMP that cannot be regularly embedded into a σ-complete OMP (Thm 3.8).
   - **The natural iteration I would have tried is addressed and shown to fail**
     (Rmk 3.18): iterating Boolean amalgamation "requires that we preserve joins
     completed at an early stage, and [it] does not do this"; "one particular join can
     always be inserted" — they lean toward non-completability.
   - **The positive completion results (Thm 3.15, Bugajska–Bugajski/Guz) require
     atomistic / strong-state structures** and "will not hold in a non-atomic Boolean
     algebra" — the well-behaved regime, not the exotic binding paste.
   - **General embedding (their Problem 2, "can every oml/omp embed in a σ-complete
     one?") is OPEN** — so this is *not* a proof of Exit B, but it removes the natural
     construction routes and confirms substrate-existence is genuinely hard.
   - **HHLN arXiv:1711.03748 is a reconstruction paper (Sub-poset / directions /
     hypergraphs), not a completion paper** — only confirms the chain-finite scope of
     Greechie diagrams; firewall it from Surface 1.
   - **Net reweighting:** Surface 1 is no longer "open, no prior art" — it is studied
     with published negatives, materially **strengthening the Exit-B inclination** (the
     construction side lost its natural tools to a published obstruction) without
     proving Exit B.
   - **Harding [34] tracked down + read** ("Canonical completions of lattices and
     ortholattices," Tatra Mt. Math. Publ. 15 (1998) 85–96; converted from PostScript,
     now in the library). It pins the obstruction to the exact object:
     • **Prop 3.4(5):** the canonical completion of an OML carrying *two increasing
       sequences* `xₙ↑, yₙ↑` (with `x_{n+1}^⊥∧yₙ=0`) has `x^⊥∧y=0` while `x<y` —
       **fails orthomodularity** — built via *Kalmbach's construction on `(ω+1)×2`*, a
       countable ascending-chain-driven OML. That is precisely the
       infinite-ascending-cross-block regime a σ-essential witness needs; its
       completion breaking orthomodularity is the published shadow of the Surface-1
       collapse.
     • **Cor 4.2:** "A variety of OMLs admits a regular completion iff it is closed
       under MacNeille completions." Combined with Rmk 3.14 (concrete OMLs not
       MacNeille-closed) ⟹ **the variety of concrete OMLs admits no regular
       completion**; and (Prop 4.1, after Palko) MacNeille is the *only* candidate for a
       regular completion, so a sharp/join-preserving σ-completion staying concrete
       provably does not exist as a variety operation.
   - **Net:** Surface 1's natural and sharp routes are **closed by published results.**
     The only surviving construction route is a *non-regular* embedding into a larger
     concrete σ-complete OML — which generically adds joins/states that dilute the
     binding or the contextuality (the point-rich/point-poor antagonism, at the
     completion level), and has no published tool. This does not formally prove Exit B
     (Harding–Wang Problem 2 is open; non-regular over-embedding not excluded) but
     leaves the Exit-B inclination strongly literature-grounded. Per "understanding,
     not shipping," this is a clean stopping point.

   The survey `notes/open_questions/oml_onboarding.{md,tex}`
   is committed to this Reading-1 framing; working layer:
   `reading1_prize_reduction.md`, `sigma_essential_nonemptiness_finding.md`,
   `direction2_gate_finding.md`, `subsession_sigma_essential_via_CE.md`.
   **Pen-and-paper kit:** `problemset_oml_descent.{tex,pdf}` (self-contained
   working problem-set; note the contextuality definition there should be read
   against the landed `S_df^σ`/`G_δ` characterization above).
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
