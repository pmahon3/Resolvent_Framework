# reconstruction paper — status

Created 2026-07-08. The formal write-up of the reconstruction / commensurability
structure theory (successor programme to the σ-essential witness).

## Scope (skeleton + proved core drafted)
- **Proved core, drafted at LaTeX quality:** framework + C=R geometry (§1);
  trichotomy (§2, free/acyclic + product + De Loera–Onn universality);
  parity theorem (§3, with PR-box corollary); taming catalogue + signable
  theorem + forest-counting + **symmetric Circuit Localization** (§4);
  winding characterisation + **Lean-certified layer-injectivity discriminant**
  (§5).
- **Fenced as conjecture (NOT claimed proved):** universal impossibility
  conjecture (§6) — specifically the *forcing lemma*, its one open step.
- **✎2026-08-21 — no longer fenced:** the **pruning lemma** is proved at general
  `k` and Lean-verified (`QuerySystem/PruningTheorem.lean`, receipts
  `[propext, Quot.sound]`), and **theorem-let B** with it
  (`QuerySystem/TheoremB.lean`): `Safe(ρ)` is eventually periodic and
  effectively computable. The **named k=2 phase gap** (seed §2.2z) is resolved
  in the statement rather than patched — the phase is absorbed by the strand
  decomposition, and quantifying over strand interleavings is quantifying over
  which rotation closes the linking, which is a generator exactly when
  `gcd(r,k)=1` (Lemma NG covers the non-generator case). What remains fenced is
  universal impossibility alone.
- **Consequences:** reconstruction guarantee, scoped to the tame classes;
  one-phenomenon-three-faces tie to Paper II + σ-essential (§7).
- **Method note:** verdict-grade discipline + Lean certification (§8).

## Provenance
All statements extracted faithfully from
`papers/reconstruction/notes/commensurability_classification_seed.md` (§§1, 2.2f, 2.2s,
2.2t, 2.2x–2.2z, 3) and the taxonomy
`papers/reconstruction/notes/commensurability_taxonomy.json`. Lemma 2 =
`formalization/QuerySystem/QuerySystem/WindingInjectivity.lean`.

## PHASE-4 PROOFS — ✅ ALL 8 HAND-VERIFIED 2026-07-09 (2 editorial fixes owed)

The six PROVE-ORIGINALLY items (per `notes/PROOF_PROMPT.md`) are written out as
full proofs in `reconstruction_body.tex`. **ALL 8 items now independently
hand-verified this session (advisor-cross-checked on the subtle ones: forest
directed-circulation, θ-sweep load-bearing split).** Every proof HOLDS. Two
EDITORIAL fixes owed (neither is a gap; both flagged in items 6–7 below):
  - #6 θ-sweep: DEMOTE "reproduces q exactly" to "illustrative on binary case"
    (soft for general alphabets, NOT load-bearing).
  - #7 forest: "alternating ±1 edge-flow" → "directed circulation (fwd +1/rev −1)".
Also worth noting (item 1): the genericity gate is VACUOUS for the size-2-window
ring the paper actually uses — candidate for de-hedging "under the genericity
gate" phrasing on thm:winding/lem:gate, or at least a footnote naming the vacuity.
Per-item verdicts, ranked by original verification priority:

1. **GATE LEMMA (`lem:gate`) — ✅ HAND-VERIFIED 2026-07-09 (verdict below).**
   REASSESSED earlier: DEFINITIONAL, not a theorem-with-a-gap; hand check, NOT Lean.
   With arc-value = context cell-probability q_i(a,b), "inflow=outflow at (i,a)" IS
   the coherence identity ∑_b q_{i-1}(b,a)=∑_b q_i(a,b) term-for-term. Recorded
   honestly as `coherence_is_conservation` (rfl-grade REMARK), NOT dressed as a
   theorem.
   **VERDICT (⟦HAND✓⟧, advisor-confirmed): lemma VALID. Both directions check.**
   - Dir 1 (coherent⟹circulation): the coherence eqn IS Kirchhoff conservation
     at (i,a), term-for-term. Definitional.
   - Dir 2 (circulation⟹coherent): valid — set q_i(a,b)=f(arc); nonneg✓,
     unit-mass-per-context✓ (conservation), adjacent agreement=conservation✓,
     non-adjacent=vacuous✓.
   - **KEY FINDING — the genericity gate is VACUOUS for the size-2-window ring.**
     Contexts = the L edge-windows W_i={i,i+1} (paper line 115-116). Then
     W_i∩W_j≠∅ ⟺ j∈{i-1,i,i+1}, i.e. OVERLAPPING⟺ADJACENT. Non-adjacent windows
     are DISJOINT ⟹ trivial common subalgebra ⟹ agreement vacuous, at EVERY L
     (incl. L=3, where ALL pairs are adjacent — nothing non-adjacent exists). So
     the gate "non-adjacent contexts share only trivial events" is automatically
     true, not a restriction. It is load-bearing ONLY for protocols with
     larger/overlapping contexts where two non-adjacent contexts can share a site.
   - **RESIDUAL CLOSED:** `thm:winding` + its layered-ring construction live
     ENTIRELY on the length-L ring (size-2 windows); the gate is never invoked on
     a larger-context frame. So its vacuity covers everything the paper uses.
   - ⚠ Do NOT round up to "gate lemma proven in full generality." It is
     proven-and-vacuous for size-2 rings — a stronger, narrower statement than the
     paper's "under the gate."
   The phase gap (2.2z) does NOT bite here (it lives only in the §open pruning
   lemma, a surrogate for LISC, not this fixed-L statement).
2. **Flow decomposition (`lem:flowdecomp`)** — where the content sits (extreme
   circulation = SINGLE simple cycle; R = conv(winding-1); C≠R ⟺ ∃ winding-≥2
   vertex). General decomposition is classical (Ahuja–Magnanti–Orlin Thm 3.5),
   Mathlib-absent ⟹ AXIOMATIZED honestly. **KERNEL NOW LEAN-CERTIFIED (see below):
   the winding-1/config correspondence + fractional dichotomy are PROVEN on top
   of the axiom, 0-sorry, standard axioms only.**
3. **Layer-injectivity (`lem:injectivity`)** — ALREADY Lean-certified
   (WindingInjectivity.lean, 0-sorry). No action.
4. **Parity theorem (`thm:parity`) — ✅ HAND-VERIFIED 2026-07-09.** All 4 steps
   check: (a) marginal-determination reduction p_10=u_i,p_01=u_{i+1},
   p_00=1−u_i−u_{i+1}, nonneg⟺edge constraint — arithmetic✓; (b) det(I+P)=
   ∏(1+ω^k)=1−(−1)^L via z^L−1 at z=−1, factor-out-(−1)^L step correct✓;
   (c) even⟹bipartite⟹TU⟹FSTAB=STAB✓ (König/H–K); (d) odd: zero-coord⟹path-
   face⟹TU⟹integral contra, so u*>0 all coords⟹all L edges tight⟹Mu=1
   (det=2≠0 unique)⟹cyclic flip u↦1−u applied L(odd) times⟹u_i=1−u_i⟹u≡½✓.
5. **PR-box (`cor:prbox`) — ✅ HAND-VERIFIED 2026-07-09.** Separating facet:
   α(odd C_L)=(L−1)/2, at u≡½ ∑u=L/2, rel. violation ½/((L−1)/2)=1/(L−1)✓.
   CF=1: admissible ν under u avoids (0,0) on every edge⟹v_i+v_{i+1}=1⟹2∑v=L
   impossible for odd-L integer⟹λ*=0✓.
6. **θ-sweep / signable (`thm:taming7`) — ✅ HAND-VERIFIED 2026-07-09 (with a
   demotion owed).** The LOAD-BEARING content = C=R via the integrality chain:
   sign V_− columns by −1 ⟹ each edge row's two nonzeros opposite-sign (edge
   joins V_+ to V_−) ⟹ Hoffman–Gale/Ghouila-Houri TU ⟹ integral vertices ⟹
   each a {0,1} config (edge-nonnegativity encodes legality: a {0,1} profile
   with all cells≥0 is legal, tight)✓. Attribution matches the landmine note
   (Hoffman–Gale APPENDIX to Heller–Tompkins). **The θ-sweep "reproduces q
   EXACTLY" is soft for general alphabets** — the sweep produces the
   (anti-)comonotone Fréchet coupling; marginal-determination only says q_e is
   SOME fixed function of the marginals, not the monotone one. EXACT for
   binary/golden-mean (p₁₁=0 IS the countermonotone Bernoulli coupling).
   ⟦OWED — editorial⟧: DEMOTE the sweep to "illustrative on the binary case"
   (NOT load-bearing — no downstream consumer uses the mixture; lines 361/376/
   386/403 all consume only C=R/FSTAB=STAB. Verified by grep.). Do NOT
   over-invest proving it tight in general.
7. **Forest counting (`thm:forest`) — ✅ HAND-VERIFIED 2026-07-09 (with a wording
   fix owed).** MD⟹forest: cells are ORDERED pairs (golden-mean pins it:
   p₀₁=u_{i+1}≠u_i=p₁₀), so the map is the DIRECTED incidence structure; a cycle
   carries a directed circulation (fwd +1/rev −1) with zero endpoint marginals
   ⟹ non-injective. Triangle test C₃: +ε fwd/−ε rev cells ⟹ tail & head
   marginals all 0 at each vertex ⟹ correctly excluded✓ (uses symmetric hyp:
   reverse cells legal). Forest⟹MD: tree recovers joint edge-by-edge, no cycle✓.
   ⟦OWED — editorial⟧: fix "alternating ±1 edge-flow" → "directed circulation
   (forward +1/reverse −1)" (the current phrasing reads as vertex-parity
   alternation, which FAILS on odd cycles; the directed circulation is right).
8. **Taming (10) / phase decoupling (`lem:taming10`) — ✅ HAND-VERIFIED
   2026-07-09.** Connected bipartite frame ⟹ exactly two global colourings by
   H's classes (masses t,1−t), phase t = single global DOF✓; conditioned on
   either, residual = FSTAB point, independent given t = fibered ⊕✓; FSTAB=STAB
   by taming7 (the load-bearing half, inherited cleanly) ⟹ C=R termwise in t✓.

## PHASE-5 LEAN (2026-07-09) — WindingDichotomy.lean, 0-sorry

`formalization/QuerySystem/QuerySystem/WindingDichotomy.lean` (builds clean under
Mathlib v4.29, 0 sorry). **CERTIFIES the finite combinatorial kernel of the
flow-decomposition step, and ONLY that:**
- `winding_one_isConfig` — a length-L (winding-1) trace IS the graph of a global
  configuration ZMod L → Fin A (holds for EVERY winding-1 trace; layer-injectivity
  not even needed — the layer map is auto-bijective at length L on L layers).
- `winding_ge_two_fractional` + `exists_layer_collision` — a simple (layer-inj)
  trace longer than L visits some layer in 2 distinct states ⟹ not a config ⟹
  marginal profile fractional. The contrapositive that makes winding-≥2 = fractional.
- `config_trace_layerInjective` — every config gives a simple winding-1 cycle (⟸).

**RECEIPTS (`#print axioms`): all four depend ONLY on [propext, Classical.choice,
Quot.sound] — NONE consumes `flow_decomposition`.** The kernel is pure finite
combinatorics; the axiom is stated for the paper's bridge but not used by the
kernel. Confirms the advisor's 3-point boundary test held:
1. Gate lemma NOT dressed as theorem (rfl-grade remark `coherence_is_conservation`).
2. `flow_decomposition` axiom = the GENERAL classical decomposition (AMO Thm 3.5),
   abstractly stated + cited — NOT the winding conclusion.
3. winding-1/config correspondence + fractional dichotomy PROVEN on top, receipts prove it.

**⚑ EXACT LABELING (do not let this get recalled as "winding Lean-certified"):**
what is certified = "winding-1/config correspondence + injectivity, GIVEN classical
flow-decomposition." It DOES NOT certify the winding characterisation
(`thm:winding`), whose polytope-vertex content (Mathlib-absent convex geometry)
and definitional gate identification remain a hand/citation check. This distinction
is written into the module docstring, the paper (§winding), and here in these words.

Queued Lean targets (method note), STILL OPEN: θ-sweep, phase-mixture, monotone
collapse, empty-intersection. Gate lemma is definitional (not a Lean target —
item 1 above). Prove on paper (done), then formalize.

## CONSOLIDATION PASS (2026-07-09) — tamings regrouped, winding foregrounded

Addressed "feels dispersed (trichotomy + ten lemmas)". Verdict (advisor-checked):
the universal-impossibility capstone would NOT clean this up — completeness
enshrines a catalogue, doesn't shrink it, and adds proof machinery. The real fix
was presentational + a structural regrouping, done now:
- **Winding criterion is the spine** — the ten tamings reframed as "routes by which
  the winding obstruction fails to form," not independent phenomena.
- **Two-axis dichotomy** (by C=R engine, NOT by realisation): 4 TERMINAL integrality
  certificates (chains, cliques, signability/TU, twin-expansion=below-TU) + 5
  REDUCTIONS to a terminal one (transient-branching, direct-sum, grading, monotone-
  collapse, phase-decoupling) + determinism as degenerate remainder.
- Two groupings are PROVEN (flagged as such): grading ⟺ Perron–Frobenius
  imprimitivity (this session's Joint-2 finding); phase-decoupling ⟹ signable
  (Lemma taming). Rest honestly "grouped by mechanism."
- ⚠ AVOIDED a trap the advisor caught: #8 twin-expansion is BELOW-TU (own record),
  NOT TU-adjacent — the θ-sweep is a shared REALISATION of (3),(4),(9), not a shared
  invariant. Grouped by C=R engine, said so explicitly in the text.
- Tamings renumbered (determinism moved to end); downstream refs fixed
  (phase-decoupling now taming (9), SCC/monotone-collapse taming (8)). Builds clean
  10pp, no undefined refs.

## EDITORIAL PASS (2026-07-09) — 12pp → 10pp

Structural polish applied inline (16 editorial rules + advisor keep/cut list).
Cut: process-narration ("seed §2.2f/o/s/h", "the harness read off",
"machine-corroborated", "8/8", "1819 targets", "3434-section"), ceremony
("Results." roadmap, "We record honestly", "scoped honestly", "claim no novelty"),
normative register, subsection headers where thin. Narrative now foregrounds the
novel elements (winding criterion, CL assembly, parity, tamings) with classical
results compressed to one contextualizing paragraph. Every proof step preserved
(all 8 thms / 4 lemmas / 1 cor / 2 conj intact; 10 proof envs balanced).
**Claim-inventory verified post-cut: ALL load-bearing qualifiers survive** —
loopless scope, genericity gate, "evidence not proof", finite-scale verification,
the winding Lean guard ("cited axiom not proved; does not certify the winding
characterisation; ... remain on paper"), and all 4 differentiating cites (Araújo,
Weller, Barto–Kozik, Thapper–Živný). Emphasis shift did NOT upgrade epistemic
status (forward direction still hand-written; gate lemma still definitional).

## STILL NOT DONE (owed before any submission)
- ~~Independent verification of items 1–8~~ ✅ DONE 2026-07-09 (all hold; 2
  editorial fixes owed — see items 6/7). Item 1 gate lemma VERIFIED + found
  vacuous for the size-2 ring.
- **Two editorial fixes** (from verification): θ-sweep demotion (#6), forest
  "directed circulation" wording (#7); optional: de-hedge the vacuous gate.
- **The k=2 pruning residual** stays open; §6 (`conj:universal`,
  `conj:pruning`) must not harden into a proof until settled structurally. The
  named phase gap is intact in the draft (labelled EVIDENCE not proof).
- **Phase-7 re-audit** (`/audit full`): the winding proof's novelty is what the
  second audit probes hardest — run it after item-1 verification.

## PRIOR-ART VERDICT (2026-07-08, hostile scout — see PRIOR_ART_VERDICT.md)

**Headline: the polyhedral core is KNOWN; novelty is the observational/dynamical
layer + winding criterion + Circuit-Localization assembly. Contribution TYPE 6
(bridge/translation), clearing TYPE 3 only if parity/winding are unobtainable
without the EA/PR framework.** Must state this verdict IN the paper.

Per-result: R1 framework = Wainwright–Jordan LOCAL/MARG + Abramsky–Brandenburger
(known translation). 2a acyclic⟹tame = **Vorob'ev 1962** (drop "free theorem"
framing; do NOT cite Kellerer for the iff). 2c universality = De Loera–Onn +
**Průša–Werner 2013/2015** (exact-object universality, was OFF-SHELF). Parity =
Nemhauser–Trotter + Chvátal + Hoffman–Kruskal/König (mechanism classical; only
the golden-mean/recurrence dressing new). Tamings = TU/König/perfect-graph
renamed. R5 Circuit Localization = NOVEL assembly + winding criterion, but must
differentiate from **Thapper–Živný** (BLP-tight iff fractional symmetric
polymorphism — the tamings are plausibly its shadows), not just Barto–Kozik.

**Owed before drafting proofs (per-step cite-vs-prove now RESOLVED):**
- CITE-CLASSICAL (short reduction + citation, do NOT write original proofs):
  acyclic (Vorob'ev/BFMY), 2c universality (De Loera–Onn/Průša–Werner/Pitowsky),
  parity mechanism (Nemhauser–Trotter/Chvátal/Hoffman–Kruskal/König), signable
  (Hoffman–Gale-appendix/Ghouila-Houri/König), cliques+holes (SPGT/CCLSV/CSW).
- WRITE-ORIGINAL (genuinely ours): the EA/PR framing, the reduction lemmas
  (golden-mean homs⟺independent sets; marginal-determination affine lift), the
  **winding/primitive-orbit criterion + covering-space proof**, the
  Circuit-Localization assembly.
- MANDATORY CITATION FIXES: add Průša–Werner, Thapper–Živný, Leggett–Garg+NSIT,
  Vorob'ev, BFMY, Abramsky 2012, Nemhauser–Trotter, Chvátal, Hoffman–Kruskal,
  Ghouila-Houri, König, SPGT, CCLSV, Fine 1982. **Attribution landmine:
  signability⇒TU is the Hoffman–GALE APPENDIX to Heller–Tompkins 1956, NOT the
  main text — cite correctly or it gets caught.**
- SHELF GAPS to close: (1) Leggett–Garg/NSIT is the nearest competitor
  (temporal contextuality) — differentiate the cyclic-time/subshift-orbit
  reading explicitly. (2) Průša–Werner (exact-object universality).
- CONTRIBUTION-TYPE SELF-TEST to run: are parity + winding re-derivable directly
  in stable-set / graphical-models language? If yes → Type 6; if no → Type 3.
  Answer decides the paper's positioning.

## 2026-07-10 ADDENDUM (session 4 + repo consolidation)

- **Crossed-cycle attack advanced past this ledger's frontier:** EQUIVALENCE
  proved ⟦HAND+machine⟧ (crossed ⟺ antipodal-free even closed walk); no-cross ⟹
  no loops + all simple cycles odd; walk family explains 100% of primitives A≤5.
  Open gap = ONE lock-avoidance lemma. Current state of record =
  `HANDOFF_2026-07-10_session4.md` + `joint2_wielandt_finding.md` (MASTER LEMMA
  section). This ledger's Phase-4 per-item verdicts above remain valid.
- **Consolidation (2026-07-10):** the working files moved out of
  `notes/unsorted/` — hubs/taxonomies now in `papers/reconstruction/notes/`,
  all oracles + atlas data in `papers/reconstruction/oracles/` (flat, imports
  preserved). Superseded handoffs (07-09, 07-09_session2, 07-10 session 3) and
  the pre-reskeleton body are in `notes/archive/` here.
