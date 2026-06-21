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
| Companion note | Complete, 3 pages |
| I | Synthesis, not novel. Complete, 7 pages |
| II | EA/PR/VDR framing novel; math classical. Complete, 9 pages |
| III | Withdrawn (rediscovery) |
| Fibre mixing | Dead (bridge theorem false) |

---

## Open Mathematical Frontiers

Ordered by downstream leverage:

**Status 2026-06-20 (NO plainly-open problem left; both prior leads resolved against
the literature). Strategy D KILLED on prior-art 2026-06-18 (Gaifman 1964 inhabits the
cell stronger). OML descent NOT PLAINLY OPEN as of 2026-06-20: prior-art
(Derr–Williamson 2023, arXiv:2302.03522, via Maharam 1972 §8) settles it NEGATIVELY in
the Polish-representable case — for a concrete σ-complete OML realised as regular Borel
sets of a Polish/Hausdorff point space, finite-non-contextuality ⟹ global
non-contextuality, so the σ-essential cell is EMPTY. The residue (a genuine but sharply
located open core): a witness must be NON-(topologically-)representable —
`S_df^σ` non-Polish / failing inner-regularity + Borel-σ-generation on its own
dispersion-free representation — which IS the σ-Loomis–Sikorski wall (route iii),
descriptive-set-theory-flavoured. Maharam §8 confirms the topological hypothesis is
load-bearing (topology-free σ-extension reaches only the enlarged Stone space). See
`oml_onboarding` Rmk `rem:dw` + `sigma_essential_prior_art_verdict.md`. The earlier
"LANDED structural dichotomy, uninhabited open problem" framing is SUPERSEDED by this
literature finding. ARTIFACT STATE (2026-06-21): the survey `oml_onboarding.tex` is now
a standalone, professional (amsart) survey — citation-fidelity-audited, prior-art-
verified-open, de-personalised, with two contextuality figures (MO₂ + pentagon,
`figures/`); a reader-facing companion essay (`companion_probability_without_a_joint_world.pdf`)
and a CE-leak intuition figure (`figures/ce_leak_intuition`) sit alongside as
orientation aids. Paper II checked, requires no updates (it cites Fine narrowly and
D–W only as a domain example; the descent material lives in the survey, not Paper II).
The remaining `mahon2025` "Preprint" cite needs an arXiv id before any posting.**

> **ORIENTATION POLE (2026-06-18).** The standing OML-descent target is **route (iii)**
> of `oml_onboarding` §4.3: *is there a countable-join-preserving σ-Loomis–Sikorski /
> σ-Stone duality for **concrete** OMLs?* (= the §5 σ-essential open problem). Fences:
> the *faithful* σ-tribe (∧,∨→∩,∪) is Boolean-forcing, CLOSED; the open object is the
> non-faithful concrete logic. The obstruction is **not** the representation/join
> (∏ₙMO₂ has a concrete non-union join and still fails) — it is **off-center σ-essential
> contextuality on an irreducible concrete σ-complete OML** (non-band generators, HW
> Problem 2, untooled). Exit A / Exit B are two *outcomes* of one (tetralemma-shaped)
> question, not rival goals; the faithful position is the inclination, held open. Full
> orientation in the `[[sigma_essential_construction_attempt]]` memory's "THE POLE" block.
>
> **Route status (updated 2026-06-19, two literature-reads of §4.3).** (i) RDP —
> CLOSED by theorem, *including* the sharp-skeleton evasion (Jenča 2001: RDP ⟹
> sharp = center = Boolean). (ii) MacNeille — CLOSED. (iii) σ-Stone duality — the
> sole OPEN route, but the one existing point-free-σ-additive machinery
> (topos/Bohrification) was read and **sidesteps** it (σ-additivity lives on a
> distributive object / per-context Boolean blocks — HLS Def 6.17(a), Döring via
> daseinisation; the topos analogue of faithful ⟹ Boolean). So route (iii) stays
> open, known candidate-machinery exhausted as a *crack*. **Four independent framings
> now converge on the one wall** (tetralemma; Loomis–Sikorski; openness/coherence;
> topos) — strong diagnostic grip on *why/where*, NOT an impossibility proof. See
> `oml_onboarding` §4.3(i), §4.4 + `verification/topos_route_read_2026-06-19.md`.
>
> **UPDATE 2026-06-20 — prior-art settles the Polish-representable case NEGATIVELY.**
> Derr–Williamson 2023 (arXiv:2302.03522, via Maharam 1972 §8): on a concrete
> σ-complete OML realised as regular Borel sets of a Polish/Hausdorff point space,
> the σ-essential cell is EMPTY (finite-non-contextual ⟹ global non-contextual). So
> route (iii) is no longer "plainly open" — it is open ONLY in the
> non-(topologically-)representable case, i.e. exactly where a σ-Loomis–Sikorski
> representation FAILS. The four-framing wall and this finding agree: the open core is
> precisely the absence of a (regular, Borel-σ-generating) point representation. See
> `oml_onboarding` Rmk `rem:dw` + `sigma_essential_prior_art_verdict.md`.
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
**Strategy D KILLED ON PRIOR-ART 2026-06-18** (/audit full, hostile-referee,
primary-source; see [[strategy_d_resolved]] + `strategy_d_AUDIT_VERDICT.md`). The
math is TRUE — `Clop(Y,𝔗)` (Argyros 1983 pre-Gleason) is NOT σ-complete (gap family
`A_k=[0^{k-1}11]` at `0̄∉` any `V_Σ`, no LUB) — but it clears **no contribution
bar**: **Gaifman 1964** (PJM 14(1):61–73, Thm 2.2 + property (†)) already exhibits,
IN ZFC and 19 years prior, an atomless BA with **no strictly-positive FINITELY-
additive measure** — strictly STRONGER than the "no σ-additive" leg. non-σ-complete
+ atomless are conceded-trivial; the only hard ingredient (measure-freeness) is
Argyros's published theorem. "Strategy D" was the programme's **PRIVATE name**,
never field-open; the "likely ZFC-independent" prior was a LOCAL MISREADING
(σ-completeness read off the completion/Gleason cover — Comfort–Negrepontis 6.23
Gaifman / 6.25 Argyros record the *completed* forms — not the trivially-non-σ-complete
base). **L_MO₂-shape kill (true + trivial + occupied) — the first kill of the Strategy-D (a)-line, NOT a descent-arc death.** So **ONE
open problem remains** — OML descent (the (b)/incompatibility face). The
(a)/anti-smuggler line's delivered result is **CE/Paper I ONLY**; Strategy D was its
candidate extremal-Boolean-floor frontier and it is now retired (the cell was
already inhabited in ZFC). Survives: a one-line Gaifman-1964 citation, no contribution.
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
   `papers/paper_i/notes/ultralimit_investigation/strategy_d_AUDIT_VERDICT.md`;
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
   a spanning-impossibility). *(Historical 2026-06-12 framing; superseded by the
   Session-8 dichotomy below — now "one construction target," not "two exits," per
   the Status block above.)* The CE-routing subsession (2026-06-12) returned
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

   **SESSIONS 5–6 (2026-06-17) — THE HARDING LEVER IS SUBSUMED; A REAL CRACK AT THE
   ω₁ CONSTRUCTION PROPER CONVERGES (bottom-up) TO THE HARDING–WANG WALL.**
   - **Session 5 (Harding [3] lever, subsumed):** the suggested Exit-B lever — adapt
     Prop 3.4(5)'s non-orthomodularity construction — crosses neither gap. Porting the
     *configuration* (not the argument): in a genuine OML, OM is automatic ⟹ `x<y`
     forces `x^⊥∧y > 0`, so the question is *joint realizability*, never "meet 0." The
     meet computes to `W>0, W≤⋁yₙ, W∧yₙ=0 ∀n` = **meet-continuity failure** (Harding's
     own Prop 3.4(2)), achievable via the non-distributive meet-gap. The config is two
     *countable* chains ⟹ block-local ⟹ **finitely many blocks** ⟹ caught by the
     landed countable-block theorem (Exit A = tame curiosity); as Exit B it only
     re-derives completion-failure (HW Problem 2 untouched). The gadget is lattice-level
     / finitely-many-blocks; the frontier is uncountable-block / state-level — no
     crossing.
   - **Session 6 (the ω₁ construction proper, real crack):** vehicle = a partition-logic
     on ℕ (Route B — concreteness and "every point is a σ-additive df-state" are free).
     The **band family** (`ℕ≅ℕ×ℕ`; blocks `B_S = {rows i∉S} ∪ {S×{j}:j∈ℕ}`, `S` ranging
     over an almost-disjoint index) is the first to carry a genuine
     *incompatible-not-orthogonal* pair (`a=S_α×{0}`, `b=S_β×{0}` with `S_α∩S_β` finite
     nonempty). The **band-family trichotomy** — a whole-family verdict, exhaustive over
     the index choice:
     • **(a) index not finite-union-closed** ⟹ `cl(a∪b)` needs `S_α∪S_β` in the index,
       which escapes ⟹ **not a lattice** [the AD case; Strategy-D limit-branch on the OML
       side];
     • **(b) finite-union-closed with a comparable-finite-difference pair** ⟹ points enter
       `L` as *differences of comparable cross-block elements* (`ℕ×{0}` and `(ℕ∖{0})×{0}`
       comparable, different blocks ⟹ `{(0,0)}∈L`), forcing all singletons ⟹ **Boolean**
       [the all-infinite-sets case]; the meet-gap shields only *incompatible* pairs, not
       comparable ones;
     • **(c) finite-union-closed, no such pair** ⟹ [**SUPERSEDED BY SESSION 8 — regime (c)
       is BOOLEAN too, see below; the trichotomy collapses to a dichotomy.** Original
       Session-6 reading, now corrected:] the paste survives, so the mixed-column
       orthogonal join `X = ⊔ⱼ(S_{αⱼ}×{j})` (σ-completeness demands `X∈L`) escapes ⟹ not
       σ-complete.
     ⟹ **no band index yields a concrete σ-complete non-Boolean lattice.** Three "forced
     squeezes" (region-count, AD-count, ∪-closure) each failed at their own flagged link
     (e.g. the union block is a *container, not a merger* — binding survives).
     **Convergence = the finding:** regime (c)'s repair (adjoin `X`) is a σ-completion of
     a concrete non-Boolean irreducible OMP = **exactly Harding–Wang Problem 2 / the
     Session-4 wall**, now reached bottom-up with a concrete witness join. Win condition
     (a definite substrate verdict on explicit families) **met**; **not** an Exit verdict
     (the σ-completion is HW Problem 2, open; a non-regular over-embedding adjoining `X`
     is not excluded, just untooled). Inclination unchanged in strength. Open sub-question
     (set-theorist, *moot* here given `X` — it asks only whether regime (c) is non-empty):
     does a `𝔠`-AD family with no member almost-covered by countably many others exist in
     ZFC? Full record: `[[sigma_essential_construction_attempt]]` memory (Sessions 5, 5b, 6).
   - **Session 7 (lever 1 — the σ-completion adjoining `X`, re-framed + sharpened):**
     "interrogate the σ-completion" was a trap (the named MacNeille/canonical completions
     are already answered; building one re-derives a known negative). The real lever = a
     one-round closure computation: *does adjoining `X` force a singleton* (regime-(b)
     Boolean collapse)? Round-1 generator meets (`X` vs rows / cells / a second join `X′`)
     force **no** singleton — `X` is a disjoint ∪ of whole cells, subdividing no atom; the
     row-vs-column-cutter meet-gap that *defines* regime (c) shields them. **But the
     dichotomy was backwards** (advisor): *existence is free* — `P(Ω)` is a σ-complete
     concrete OML over `L∪{X}`; the crux is **(σ-complete ∧ lattice ∧ non-Boolean ∧
     regular-over-`L`) simultaneously** = non-regularity of the smallest closure = HW
     Problem 2. **A circularity was caught (reversal #21, retracted):** "same-column cells
     incompatible ⟹ meet `∅` ⟹ no singleton" assumes the conclusion — "meet `∅` in `L̄`"
     *is* "(S∩S′)×{0} ∉ `L̄`" = the non-Booleanness to prove; σ-closure is exactly what
     might add the intersection. **The genuine increment (sharper than "regime (c) = HW
     Problem 2"):** `Ω=ℕ×ℕ` is *countable* and the generators *separate points* ⟹ they
     generate the full `P(Ω)`, so **`L̄` non-Boolean ⟺ `L̄ ⊊ P(Ω)` ⟺ disjoint-union-closure
     is proper ⟺ the finite sets `(S∩S′)×{0}` stay out**. Single-axis invariants can't
     decide it (row-trace and column-slice are each σ-homomorphisms *onto* `P(ℕ)`); the
     obstruction is irreducibly joint/2D. Non-circular target = an intrinsic class `𝒦`
     (closed under complement + disjoint ∪, omitting the finite column-sets); its existence
     is open both ways (construct = witness substrate; refute = regime (c) collapses Boolean
     too) — not a hand-session task. Substrate ≠ witness: the state `w` is untouched.
     Inclination unchanged in strength. Full record: `[[sigma_essential_construction_attempt]]`
     memory (Session 7).
   - **Session 8 (the band-family trichotomy collapses to a dichotomy — Exit-A-via-band
     CLOSED):** the Session-7 "regime (c) = HW Problem 2, open both ways" target was settled
     on the **smallest explicit regime-(c) family**, and the answer overturns the trichotomy.
     A **two-relative-complement chain** forces the forbidden finite set into `L̄` at the
     *finite pre-σ level*, for **every** finite-∪-closed index: for a binding pair `S_α,S_β`,
     finite-∪-closure puts `S_α∪S_β∈ℐ`, so (1) `S_α ⊆ S_α∪S_β` comparable ⟹ `(S_β∖S_α)×{j}∈L̄`,
     then (2) `(S_β∖S_α) ⊆ S_β` comparable ⟹ `(S_α∩S_β)×{j}∈L̄`. Relative complement of a
     comparable pair is legal in any sub-OML closed under complement + disjoint ∪
     (`B∖A=(B^c⊔A)^c`, `A⊥B^c`), **at any difference size** — so the (b)/(c) finite-difference
     cut was spurious. By Session-7's equivalence (`L̄` non-Boolean ⟺ those finite sets stay
     out), this forces **Boolean**. The trichotomy collapses to a **dichotomy**: ∪-closed ⟹
     **Boolean**; not-∪-closed ⟹ not-a-lattice. **No band index yields a concrete σ-complete
     non-Boolean lattice** — the Exit-A-via-band route is closed, and regime (c)'s recorded
     "not σ-complete" death is superseded (the relative-complement closure manufactures the
     finite sets first; the X-escape was computed on the pre-closure object). This is the
     strict generalization of Session-6 DEATH 2 (finite-diff/one-step/ℕ-union → any-diff/
     two-step/any-in-`ℐ`-union) that closes the gap (b) left open. **Correctly scoped — NOT
     a verdict:** this kills *one* concrete construction route (the one Sessions 6–7 converged
     on), **not** global Exit B; HW Problem 2 in general and non-band pasting are untouched;
     the σ-essential state `w` was never reached (substrate-level throughout). The most
     promising concrete handle is gone ⟹ Exit-B inclination **strengthened, still an
     inclination**. Full record: `[[sigma_essential_construction_attempt]]` memory (Session 8).
   - **Session 8b (the Lean-as-search-container pivot — formalization restarts):**
     because Session 8 turned on a *verifiable* object (a two-step set-theoretic
     chain), the substrate is being formalized in Lean to contain the search — each
     construction piece a small bite, "have we hit the object" a `lake build` rather
     than a token-cloud judgment. Key unlock: the substrate is pure `Set (ℕ×ℕ)`
     combinatorics (a concrete logic à la Kalmbach is just a complement-and-disjoint-∪-
     closed subset collection), so **no orthomodular-lattice typeclass is instantiated**
     and the standing "Mathlib v4.29 has no OML/Foulis–Holland" wall is *escaped* (that
     wall is about abstract OML). **Bites 1–2 landed** —
     `formalization/QuerySystem/QuerySystem/BandClosure.lean` (0 sorry, 0 axiom):
     *Bite 1* — the `InClosure` predicate, the `relCompl` workhorse (which makes the by-hand
     disjointness legality-check non-skippable), and `band_chain_inter` certifying the
     Session-8 chain. *Bite 2* — `csUnion` (countable disjoint union, the σ-step) and
     `forces_boolean` (all singletons ⟹ *every* subset = `P(Ω)`, via **assembly by disjoint
     union**, NOT intersection — Session-7's "{x}=countable ∩" was the wrong route, it would
     silently compute the *Boolean* σ-algebra instead of the concrete-logic σ-closure, which
     is the open crux); `band_forces_boolean` composes the two mechanisms. **What Lean
     certifies (correctly scoped):** the forcing+assembly *mechanism* (triple → meet cell →
     singleton → all sets), **conditional on singleton-production** — the family-specific
     step (finite-∪-closed index ⟹ a binding pair localizes at every point) remains the
     Session-8 hand-argument, not in Lean. The constructor set is held to *exactly*
     {complement, countable disjoint ∪}. Frontier bite (bite 3, the **user's call** — no
     candidate on the table): a candidate `𝒦` for an *infinite* regime-(c) family as a Lean
     predicate, which either checks (witness substrate) or returns the exact breaking step
     (the transpose-catch, mechanized). The σ-essential **state `w`** is out of Lean scope
     (heavy measure wiring; already Exit B on countable substrates). Full record:
     `[[formalization_status]]`, `[[sigma_essential_construction_attempt]]` (Sessions 8b/8c).

   The survey `notes/open_questions/oml_onboarding.tex`
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
