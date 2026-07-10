# The frontier map (2026-07-08)

> **2026-07-10:** which veins get dug, and in what order, is now fixed —
> see `shovel_plan.md` (four theorems to prove + vacant lots as invitations).

The corpus's open problems are *layered*, not a single vein. Recorded here so the
next session opens from structure, not re-derivation. Two kinds of completion are
on offer — **completing the theory** vs **completing the programme** — and which
vein to open is a real choice between them.

---

## 1. Bridging layer (spine) — the latticehood family
**Claim:** latticehood ⟹ liftability ⟹ tameness, conjectured across all three
transitions (pasting / regularity / sharpness).
**Evidence:** the corpus's most persistent pattern — three independent
meet-destruction mechanisms; every wild object provably a non-lattice; every
lattice met provably tame.
**Difficulty:** the deepest, hardest thing the corpus owns. Needs a genuinely new
idea, not a refinement.
**Role:** the one claim that ties the three transitions together further. This is
"what would complete the *theory*."
**2026-07-10:** attack OPENED on the load-bearing case (regularity/OML =
shovel thm 2) — mechanisms collected, conjecture split, skeletons named:
`notes/open_questions/oml_lattice_regularity_attack.md`.
Nav: `papers/spine/` (single open bridging conjecture, §4).

## 2. Programme layer (reconstruction lane) — universal impossibility
**Claim:** the fork doesn't exist; Circuit Localization holds for the
strongly-connected non-symmetric class.
**Status (2026-07-09 attack — decomposed into 2 joints):**
- **JOINT 1 = pruning lemma (TR_k(rot-1)=LISC_k) ⟶ theorem-let B (eventual
  periodicity) ⟶ exchange-blocking: NOW CLOSED for all k** (⟦HAND⟧, 73728-check
  adversarial scan 0-fail). The seed's k=2 "phase gap" AND the anticipated k≥3
  "permutation gap" were both wrong-proxy artifacts, dissolved by labelling strands
  by traversal order (threading is forced cyclic). ⚠ proxy = rotation-by-GENERATOR
  (gcd(r,k)=1); any-rotation overcounts LISC_{k/d}. k≤|A| ⟹ unsafe set = finite
  union ∪_k LISC_k, each eventually periodic ⟹ theorem-let B.
- **JOINT 2 = exchange-blocking classification: the OPEN frontier.** grading⟺
  imprimitivity is a classical dictionary, but "residue-unsafe ⟹ grading" is FALSE
  without non-symmetry (golden-mean = primitive + parity-residue-unsafe). CENTRAL
  CRUX — **why NON-SYMMETRY forces primitive ⟹ cofinitely-unsafe** (Wielandt-shaped;
  4 candidates L≤30, 110 primitives L≤9) — needs an idea. PLUS 2 unexamined
  branches: (a) cofinitely-unsafe ⟹ not-rich-safe (girth-locking, separate from
  Wielandt finiteness); (b) potential/phase-code (seed names 3 mechanisms, only
  grading checked). Fork-free through 9 edges still holds.
**The rhyme (open):** latticehood = carrier-side; universal impossibility =
protocol-side. Joint-2 crux may connect to it. *Whether secretly one claim: open.*
  2026-07-10 UPGRADE: Joint 1 now a WRITTEN PROOF + effective Safe(ρ)
  certificate/instrument (shovel-plan Theorem 1 DONE) — statement of record
  `pruning_theorem_and_B.md`; instrument `oracles/safe_rho_instrument.py`.
Nav: `papers/reconstruction/notes/pruning_theorem_and_B.md` (statement of
record) + `pruning_k2_theorem.md` (discovery log + Lean tee-up) +
`joint2_wielandt_finding.md` (Joint 2 crux); taxonomy open_frontier.

## 3. σ-essential's named descendants — three, all genuinely open
- **No-singletons regime** (literal irreducibility): needs a rigidity mechanism
  we don't have (the witness's rigidity requires singletons; literal
  irreducibility forbids them).
- **Φ-characterization for exotic σ-classes:** the quarantine theorem
  (`thm:quarantine`) explicitly does NOT touch this — realization by exotic
  σ-classes generated inside a Borel structure is the σ-essential paper's open
  characterization question.
- **Positive-selection strength question** *(flagged as potentially the most
  beautiful standalone problem in the corpus):* can a non-principal coherent
  σ-additive selection exist on some admissible carrier? The witness theorem
  showed Ψ (the negative instance) costs NOTHING; this INVERTED question might
  cost a measurable cardinal. Where large-cardinal strength may still be hiding.
Nav: `notes/open_questions/sigma_essential_taxonomy.json`;
`sigma_essential_large_cardinal_bounds.md`.

## 4. The untouched applied layer — the statistics programme
**Where the ORIGINAL motivation lives:** practical reconstruction from univariate
data. Concentration for empirical window frequencies; the depth-selection rule;
the confidence-calibrated contextual fraction (CF_d).
**Why it's tractable now:** everything deterministic beneath it is floored and
certified (the structure theory + the quarantine); it's approachable with
standard tools (concentration inequalities, model selection); nobody has touched
it.
**Role:** turns the corpus from foundations into an instrument. This is "what
would complete the *programme*" — and if the question is highest-*value* open vein
rather than deepest, this is arguably it: the others are conjectures to attack,
this one is a programme to execute.
Nav: seed §2.3 (Layer-1 licensing, roadmap); Paper III δ̂ depth rule
(`paper_iii` taxonomy).

**2026-07-09 — activated as a scoped lead (ChatGPT orientation, `C=R` made
statistical).** The layer reframed sharply: a finite-sample *inferential* theory
over the reconstruction paper's population `C=R`, best-framed as a
**pre-reconstruction licensing diagnostic** (test whether delay-window statistics
are globally realizable in the target class BEFORE claiming a state space is
reconstructed): decide p∈C (coherent) / p∈R (realizable) / p∈C\R (obstructed) /
underpowered, under DEPENDENT single-trajectory sampling, with separation
certificates + decision taxonomy. Declared types for the eventual seed: **6+7**.
STATUS: prior-art deep-research OUT (prompt = `scratchpad/deep_research_prompt.md`,
run in ChatGPT w/ the 4 PDFs; quarantines the already-settled population geometry,
forces the relabeling test). NEXT (gated on that verdict): Phase-1 seed → `/audit
full`. No seed/draft yet. Verdict-decider = is the finite-sample layer a
non-trivial synthesis or a relabeling of {polytope GOF/chi-bar-square, Elkouss–
Wehner finite-sample Bell testing, Paulin/Marton dependent concentration + block
bootstrap, PSR/OOM/HMM realization}? Landmine: 𝓡 is NOT a polytope universally
(semialgebraic for HMM/OOM/fixed-order-Markov). Expect "publishable but only with
narrow framing" (the first Downloads report self-graded exactly that).

**Separable philosophy thesis carried by the same orientation — SETTLED, OWNED
(2026-07-09).** The conversation also carried a *foundational* "probability
before realism" thesis (sample space = earned representation theorem, not
primitive; σ-additivity not observationally free). Hostile scout on the
operational-probability surface: **OWNED — cite, don't claim** (Foulis–Randall
test spaces own sub-claims 1–2; de Finetti owns σ-additivity-not-free; Gelfand/
algebraic-probability owns Ω-as-representation). Type-6 positioning only; the one
non-relabeling residue is the σ-essential witness the corpus already owns
(`prop:ladder`). Recurring rock, 4th confirmation. Detail:
`notes/covered_leads/probability_before_realism_owned.md`.

---

## The choice, framed
- **Complete the theory** → latticehood family (deepest; needs a new idea) or its
  protocol-side rhyme, the pruning-lemma stack (incubating, refinement-shaped).
- **Complete the programme** → the statistics layer (tractable, high-value,
  where the motivation started).
- **The sharp unasked question** → are the carrier-side (latticehood) and
  protocol-side (impossibility) tameness claims secretly one theorem?

Sequencing (dissemination) is a separate decision, orthogonal to which vein opens
next: σ-essential ships first + alone (standing recommendation; spine §5).
Nothing decays while any of this waits.

---

## The two-front programme (2026-07-09)

For a fullsome programme, theory and application each have one *completing*
target — and they are **decoupled** (a rhyme, not a bridge; the transfer was
already parked, see below).

**Theory front → latticehood family.** The right target because it *closes*
rather than extends: it ties the three transitions into one statement
(latticehood ⟹ liftability ⟹ tameness, uniformly, in all three coordinate
systems). Proving it makes the corpus's central theorem "the boundary is
latticehood, everywhere" — a completed theory, not three papers + a spine.
CAVEAT: also the *hardest* thing the corpus owns; needs a genuinely new idea,
not a refinement. "Address it" = OPEN THE ATTACK (collect the three
meet-destruction mechanisms into one frame; ask what a unified
liftability-from-latticehood argument needs; find where it first breaks) —
a design/reasoning session likely yielding a sharpened conjecture + a named
obstruction rather than a proof this session.

**Applied front → the statistics layer.** Two things at different maturity:
- *Concrete instance (MITACS, `~/Research/Dynamics/MITACS`):* variable selection
  after single-variable delay optimization is CONCEPTUALLY SOLVED — a four-level
  ladder (L1 existence: not κ_Q-discriminable, provably; L2 localization:
  ATTAINABLE, executed — S11 α̂_L landslide says the missing structure lives in
  **hour_of_week**, hot zone Fri 10:00–Sun 23:00; L3 within-data refinement:
  EXHAUSTED, S12–S14 show it can't close the gap; L4 auxiliary info: routes to
  **T1, the temperature arm**). Status: down to ONE next-action — acquire ECCC
  hourly weather data, run the pre-registered within-cell lag-1 ACF-drop test
  (predicted +0.67 → 0 if temperature is the admissible 2nd variable). Blocked
  on ECCC acquisition (deferred 2 sessions). The κ_Q *framing* was PARKED
  framework-side (audit: Type-7 CONDITIONAL, revival trigger = T1 execution;
  no framework novelty claimed — canonical Diggle/Heckman-Singer/Manski-Pearl);
  MITACS uses it operationally, UNAFFECTED by the park.
- *General theory (this map's item 4):* concentration for window frequencies,
  depth-selection rule, calibrated contextual fraction — the general layer MITACS
  is one instance of. "Completes the programme": turns the certified deterministic
  floor into an instrument with error bars. Tractable with standard tools.

**Decoupling (a feature, keep it):** the two fronts do not depend on each other —
MITACS runs on published machinery unaffected by any theory result; a latticehood
proof doesn't change ECCC acquisition. They RHYME (both = "when does local/finite
information determine the global object") but the transfer is NOT established —
the κ_Q framework-side seed was parked precisely because it was a rhyme, not a
bridge (the mixing/barycenter scar, again). Pursue both, keep decoupled, let
"are they secretly one programme?" stay an honest open question, not a premise.

**Front-opening actions (separate sessions, different character):**
- Theory: open the latticehood attack (design/reasoning).
- Applied: ECCC acquisition + T1 execution (small, concrete, unblocks the parked
  revival trigger), and/or scope the general statistics layer as its own seed.
