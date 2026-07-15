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
`StoneDualityExtension.lean`, `DelayEmbedding.lean`
(+ `TopologicalQuerySystem.lean`, `ProkhorovExtension.lean` — archived,
`formalization/QuerySystem/archive/`)

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
  `notes/open_questions/kits/oml_onboarding.tex`).

**OML campaign update (2026-07-13).** The active construction frontier is
the B′(i)/T4 boundary-selection residue. For the rotating graph triple,
same-type, and transversal trace invariants now exclude W events, graph
intersections, unintended singleton collectors, and collector restrictions
with uncountable variation modulo countable support. The global normal
form is exact: universal transversal anchors plus one cylinder and countable
local patching prove Gate N, but Gate L fails by a certified missing-profile
join obstruction. The earlier
proper-interface-twist language below is historical. Current index:
`notes/open_questions/oml_attack/CURRENT_STATE.md`.

The theorem-side continuation proves `Φ iff T4At` for at most countable
maximal-block atlases whose blocks are countably generated. Thus any surviving
fine-block counterexample is necessarily an uncountable distributed-atlas
phenomenon; finite relational interval saturation alone does not imply T4.
The endgame audit proves that T4At gives hereditary one-block boundary
escape, but a Cantor singleton cover realizes every local defect using a
countably generated Boolean sigma-block while every countable subatlas
escapes. Its common-interface paste is central and has no separating
sigma-states. Coarse restrictions characterize liftability only as a
coherent inverse system; the club field refutes naive local satisfiability.
Both halves reduce to OML distributed-boundary compactness. Campaign 1 now
records the exact theorem in `oml_distributed_boundary_compactness.md`:
ODBC-S supplies a common-global-f.a.-witness section on every countable block
subsystem, while CODBC globalizes these objectwise sections. Their
conjunction is GSD/Phi. CODBC alone is not sufficient, a quantifier gap
found by hostile review. The abstract section implication is Lean verified
in `ODBCSections.lean`.

Campaign 2 proves that finite profile cut-saturation, though necessary in
the typed closure calculus, does not imply any common-state Helly property.
Finite generated boundaries and exact two-block trivial-centre atlases
satisfy ODBC. A closed-relative-eligibility hypothesis yields global
compactness by FIP, but `P(N)` refutes that hypothesis generically. Tree and
cycle incidence, bonding-map surjectivity, Mittag--Leffler stabilization and
compact fibres provide no unconditional route. The next construction target
is the centre-free coarse three-block section hierarchy, whose singleton,
pair, and triple gates are separately open.

Campaign 3 constructs the exact Cantor CSS-without-GS system and proves the
standard-Borel relation realization formula `T_sigma=R`,
`T_fa=closure(R)`. Countably generated separating sigma-boundaries expose
the omitted singleton, invertible transports identify boundary ranges, and
repeated selector pairs cannot generate inequivalent embedded interfaces.
The live architecture is narrowed to nondeterministic nonclosed
correspondences with proper coordinate subalgebras; the 44-event survivor is
the lattice-completion control.

Campaign 4 banks the fine locally-countable/countable-subcover defect
theorem and the coarse countable-intersection-reflection theorem. The former
uses T4At plus Baire; the latter turns separately solvable countably
generated envelopes into one coherent Dirac lift. Point-countability and
the club field are exact controls. Coarse ODBC is canonically the full
ODBC/Phi statement, so only added CIR-like OML structure makes it a genuine
specialization.

Campaign 6 integrates the full implication graph and rejects ODBC itself as
a non-tautological final residue: `Phi`, GSD, ODBC, and coarse ODBC are
equivalent. The remaining decision programme requires normalization of every
failure to a transported-boundary presentation and a complete
realization-or-mixed-cut-collapse theorem. These BOC clauses are open;
conditional regime packaging is Lean verified in `ODBCRegimes.lean`.

Campaign 7 hostile audit finds no retraction but blocks completion:
the Lean section system is only abstract fixed-witness packaging; no
construction passes the OML/state gates; BOC is incomplete without both
failure modes and an effective branch criterion; and the linked chain had
only 44 meaningful pre-audit iterations.

Campaign 8 reaches the iteration threshold and advances the construction:
finite-degree N-G is impossible by countable components, while selectors
`0x000f` and `0x3300` give three independently verified finite
two-coordinate centre-free five-block OMLs. They are Phi-tame; the
arbitrary-base multi-coefficient lattice/maximal-block theorem is open.

Campaign 9 sharpens that theorem to outsider extremality (OE) plus a
five-form signature census. Complement closure is proved and sigma closure
is conditional on binary closure. Six finite grids pass, but the orthogonal
coordinates are alternative under every two-valued state and hence
conditionally Phi-tame. A non-atomic three-region pair is next.

OE has since been proved: the greatest per-block floor dominates every
outsider coefficient, and all 16 finite truth-region kernels, including the
1220-event `P(4)xP(4)` case, are independently verified. The arbitrary-base
two-atom family is therefore a concrete sigma-complete OML. Maximal blocks,
centre, and the unconditional state theorem remain open.

Campaign 10 completes that finite test. Raw non-atomic substitution fails
latticehood, while canonical mixed-cut completion produces a centre-free
nine-block OML. An independently verified diagonal variant preserves its
conditional diagonal relation after completion. Both are finite and
Phi-tame. The single-edge density theorem forces the next construction to
be a genuinely distributed uncountable-incidence network.

Campaign 11 realizes the punctured-Cantor star locally but proves a two-cell
countable-meet obstruction to every shared faithful countably generated hub,
without using centrality. Maximal-block state gluing must use L-relative
sigma-additivity because maximal blocks need not be sigma-complete. The live
assembly routes are distributed nonseparating quotient copies or a genuinely
uncountably generated separating boundary.

Campaign 12 realizes that second escape at Boolean-atlas level. The
`2^{omega1}` countable-support cylinder sigma-algebra embeds faithfully into
every puncture powerset; the missing evaluation has an fa but no sigma
extension by Ulam's theorem. Countably generated faithful boundaries cannot
do this at all. The common boundary is central under finite algebraic closure;
whether sigma-completion or incompatible conditional transport can
de-centralize it while preserving MBRC is open.

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

**⚑⚑ AMENDED Ψ = MACHINE-CHECKED ZFC THEOREM (2026-07-06)
⟦LEAN — 0-sorry end-to-end; axioms = [propext, Classical.choice, Quot.sound] only⟧.**
The **Product Ulam Carrier** (`papers/sigma_essential/witness_candidate/`) cleared
adversarial verification (two independent proof passes, no mathematical error; verdict —
outcome (i), qualified — in `witness_candidate/VERIFICATION_VERDICT.md`) and was then
**formalized end-to-end in Lean the same day**: `psiAmended_ZFC`
(`formalization/QuerySystem/QuerySystem/UlamWitnessMain.lean`) proves Ψ on
**σ-classes/OMPs, coherence-amended, irreducible mod the countable ideal, in ZFC** — the
full chain (encoding fix `SigmaEssentialAmended`; Ulam matrix + rigidity Thm 5.1 + empty
kernel `UlamWitnessCore`; ω₁ instantiation `UlamWitnessOmega1`; §3 trace invariant with
the complete disjointness table `UlamWitnessInvariant`; §6 vote state + coherence
`UlamWitnessState`), receipts in `UlamWitnessReceipts.lean`. The Ω₇ example — the
amendment-forcing counterexample refuting [M] Prop 2.1 as literally stated — is also
machine-checked (`Omega7Counterexample.lean`), so the coherence amendment's
**repair-not-retreat** status is itself certified. Per-statement:
Ψ (OMP + coherence + irred-mod-ctble) — **ZFC theorem, Lean-certified**;
Ψ on **lattices (OML)** — OPEN, conjectured *opposite* (latticehood ⟹ Φ);
attack ACTIVE 2026-07-10 s8–s12 (shovel thm 2): banked ⟦HAND⟧ theorem-lets
(blocks are σ-fields; singleton/product-Ulam mechanism unavailable on
lattices; Dirac realization on ctbly generated blocks), conjecture
sharpened to B′(i)/(ii), s12 proof-read SOUND —
`notes/open_questions/oml_attack/oml_lattice_regularity_attack.md` §9;
current construction frontier (2026-07-13): the approved 44-event finite
proper-boundary survivor has a hand-proved centre-free sigma-complete
one-interval inflation with a noncompact eligible slice, but common-fibre
point replacement proves it Phi-tame; a global 60-form finite-pattern audit
confirms the arbitrary-base five-block classification beyond the earlier
centralizer checks, sigma-completeness remains hand-proved, and the smallest
`P(2)` whole-interface triangle twist is either nonfaithful or gauge-trivial;
the next gate is a proper-interface twist or a second inequivalent
coordinate;
Ψ with **literal irreducibility** (no-singletons regime) — OPEN
(s11: now waits on the same missing coarse-rigidity engine as the
lattice case; attack note §9d).
**Remaining before "SOLVED" in full**: (1) definitional-fidelity read (~15 min: the Lean
definitions vs paper v2 Defs 1.2–1.4 — the only remaining trust surface; note
`LocalState`'s weaker constraint is harmless, coherence forces full statehood); (2) gate
β — hand-check Pták–Pulmannová 1991 + Navara's Handbook survey (novelty, not
correctness; scout verdict was ADJACENT/apparently-empty — "new assembly of classical
parts closing the beyond-Polish Derr–Williamson cell"); (3) Phase-2 `/audit full` for
the write-up question. Reversal trigger (binding): downgrade only on a prior-art hit or
a located definitional-fidelity flaw.

**⚑ NEW ACTIVE THREAD (2026-07-06): reconstruction / commensurability classification.**
With the amended Ψ machine-checked, the programme reorients toward **practical
reconstruction, foundations-first** (user decision, design session = the witness
capture session continued). Division of labour: design session does mathematical
planning/design via discussion; this repo verifies (Lean + audit tools); writing
after verification. Vocabulary locked: **EA/PR(𝓡)** — coherent window data = EA;
realisability relative to a *declared* realisation class 𝓡 = PR(𝓡) (the observer's
commitment lattice); **commensurability** of a protocol = EA ⟹ PR(𝓡) universally.
Seed (full round-log) + declared types:
`papers/reconstruction/notes/commensurability_classification_seed.md`. **NAV: load
`papers/reconstruction/notes/commensurability_taxonomy.json` FIRST** (the load-first index —
26 anchors, 65-entry ledger, all detail pointers).

**STATE 2026-07-08 (the early "open queue" below is superseded — axis-reduction /
T1 / Bonferroni were all resolved or refuted in the atlas rounds; see taxonomy).**
A proved structure theory now exists: the **parity theorem** (golden-mean ring
commensurable ⟺ L even), the **free/acyclic theorem** (= Vorob'ev), the
**trichotomy** (variety-typed protocols are De Loera–Onn universal), **ten taming
mechanisms**, and **symmetric-loopless Circuit Localization** (the fork excluded by
structure). **Lemma 2** (the layer-injectivity discriminant) is **certificate-grade
in Lean** (`formalization/QuerySystem/QuerySystem/WindingInjectivity.lean`,
0-sorry). OPEN: the **universal impossibility conjecture** (fork never exists) ⟶
pruning lemma ⟶ a k=2 residual with a named **phase gap**, resting/incubating.
*[UPDATE 2026-07-10: the phase gap was a wrong-proxy artifact, dissolved —
pruning is now **Theorem P**, proved for all k with the effective Safe(ρ)
instrument (shovel thm 1 DONE, s7, fresh-context proof-read SOUND s10);
lock-avoidance lemma proved s5 (L-B half-closed, bar-D aperiodic half open).
Current joint-2 state: frontier map §2 + `pruning_theorem_and_B.md`.]*
FORMAL WRITE-UP: **`papers/reconstruction/`** (8pp; hostile prior-art pass done ⟹
contribution is **Type 6** bridge, the novel core = the observational/dynamical
EA/PR framing + winding criterion + CL assembly, the polyhedral facts classical;
owed proof-writing + verdict in `papers/reconstruction/notes/STATUS.md`). Method
signature: five instrument near-misses all caught pre-record by ground-truth
cross-check ⟹ a verdict-grade ladder (witness-unsafe > exact/theorem-safe >
screening). σ-essential frontier triple (OML conjecture / no-singletons /
positive-selection strength) stands separately in the taxonomy.

**[SUPERSEDED-IN-PART 2026-07-06]** The block below stands as the record for the
**literal (lattice / literal-irreducibility) forms only**. Its mathematical content
(walls, import-sweep kills) is unrefuted; its strategic judgment ("not close") is
falsified for the amended/OMP form — the 13-carrier sample contained no two-layer design
(Boolean rigidity layer ⊗ native parity incompatibility, coupled only through the
countable ideal). Not a verdict swing: the prior swings re-read one proposition; this
update splits it on new evidence (a verified object).

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
  SIMULTANEOUSLY). **Reading plan WRITTEN:** `notes/reading_directions/realization_technique/realization_technique_reading.tex`
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
  `localization`, 0-sorry). Full statement: `notes/open_questions/sigma_essential/sigma_essential_reduction_writeup.md`.
- **Derr–Williamson Polish boundary (`rem:dw`) — amended s13.** On a Polish-representable
  carrier with **blockwise inner-regular** restrictions every finitely-coherent pattern
  globalises — no witness (DW 2023 Thm D.6, via Maharam §8; topological hypothesis
  load-bearing). *s13 (2026-07-10):* the inner-regularity leg is independently binding
  (an (8.1)-regular two-valued state is a compactly witnessed Dirac restriction), so a
  witness must be **non-Polish / non-standard-Borel OR coarse-riding** (some blockwise
  restriction non-principal — escapes D.6 on every Polish rep). Backing:
  `notes/open_questions/sigma_essential/sigma_essential_prior_art_verdict.md` (Addendum s13);
  `oml_lattice_regularity_attack.md` §10; survey `oml_onboarding.tex` (`rem:dw`).
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
   problem). See the survey `notes/open_questions/kits/oml_onboarding.tex`
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

## Current OML frontier (2026-07-14)

Unconditional state-normal completion of the omega-one puncture atlas is
excluded, while face-local nonnormal completion remains open. The decisive
finite gate is direct incompatible conditional transport (`111 => q=r`) with
order-separating off-pattern escape states. See
`notes/open_questions/oml_attack/oml_puncture_normality_and_incompatible_transport.md`.

The finite gate now passes: a literal `MO3` conditional cell and its shared
fixed-pattern closure are verified through three cells. The exact residue is
arbitrary-finite repair followed by countable-disjoint-union closure; finite
formulas have not been promoted to that theorem.

Campaign 15 now proves the one-hub arbitrary-index family sigma-complete and
Phi-tame. The live construction is two-dimensional: the stripped grouped
coordinate K22 core has an explicit crossed-rectangle lattice failure, so the
full four-cell conditional grid was tested in Campaign 16.  Its semantics
survive but latticehood still fails.  A single literal repair never suffices;
two known iterated coordinate-core completions are OMLs only after rebuilding
the same-side `q0,q1` Boolean boundary.  Whether all distributed-preserving
repair branches fail is now one exact finite search problem; no universal
reconstruction theorem is yet claimed.

Campaign 17 supplies that theorem for literal macro completions: exhaustive
interval branching proves that every `P(16)` OML completion reconstructs the
`q`-side or `r`-side Boolean algebra. This closes the stripped architecture,
but not repairs varying inside the conditional cells' auxiliary fibres. The
next construction gate is the smallest fine-fibre rectangle repair on the
full `2x2` carrier.

Campaign 18 passes that gate at two nonterminal depths: 64/128-point first
repairs and a four-point second repair preserve both distributed boundaries
and off-activation order-separation witnesses. They do not yield a lattice,
and the next interval widens. The active problem is to identify a finite
repair grammar or a monotone obstruction, not to enumerate arbitrary subsets
of million-point intervals.

Campaign 19 replaces the putative infinite repair grammar by an exact finite
terminal problem. A third repair reaches 558 events and refutes monotone gap,
width, and gap-descriptor recurrence models. Since the full-grid carrier is
finite, unrestricted repair chains necessarily terminate, and every
same-carrier completion contains a terminal repair family. T-FIN asks whether
all such terminals reconstruct a same-side Boolean boundary or create an
activation-supported event. Coordinate-closed completions already reconstruct
a side; non-profile-measurable joins and larger-carrier sigma-completions are
the remaining escapes.

At the 558-event checkpoint, simple hull-gap laminarity fails and no nested
hull pair isolates one profile fibre. A same-side lattice meet nevertheless
appears as a whole profile fibre plus a four-point escape block. This
fattened-fibre meet, not further arbitrary repair depth, is the current exact
T-FIN test object. Its remaining interval is executable-classified into 160
whole macrofibres; terminal saturation for this partition is open, so the
next discriminating question is partial-macrofibre splitting rather than
enumeration of the saturated subclass.

The terminal residue calculus further packages both same-side boundaries as
two four-residue squares with event-valued line and total unions but no event
singletons or triples in a preserving terminal. This finite shadow is only a
necessary descriptor: coherent lifting of within-fibre subsets, or a theorem
forcing collapse when the two squares couple through the edge cells, remains
open.

The minimal bare square is the six-event `MO2` set OML, so its identities
alone cannot collapse. Profile-join-hull closure (PJH) is sufficient: it makes
the saturated events a concrete `P(16)` completion and forces reconstruction.
The current exact computation is therefore certificate-local PJH along the
finite stripped-core forcing DAG.

That DAG now yields a self-audited finite first-defect atlas with 31 internal
states and 64 candidate hull edges; all 17 no-defect terminals reconstruct a
side. The remaining fixed-carrier problem is whether any recorded nonevent
hull type survives terminal latticehood and activation escape.

Only 33 nonlower hull edges can actually be first defects. A full coordinate
symmetry audit finds the lex atlas stabilizer trivial, and all sixteen profile
fibres occur. The residue is therefore provenance-sensitive rather than a
coordinate-orbit classification.

The first nonevent-hull join is nevertheless activation-escaping: it contains
at least three complete profile fibres, each with off-activation points for
both rows. Any activation collapse must be generated later in the repair
closure. This focuses the finite route on one-fibre split cores and their
derived cuts rather than on the first join itself.

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
