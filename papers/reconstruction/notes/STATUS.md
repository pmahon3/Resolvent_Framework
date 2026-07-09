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
  conjecture + pruning lemma + the named k=2 phase gap (§6).
- **Consequences:** reconstruction guarantee, scoped to the tame classes;
  one-phenomenon-three-faces tie to Paper II + σ-essential (§7).
- **Method note:** verdict-grade discipline + Lean certification (§8).

## Provenance
All statements extracted faithfully from
`notes/unsorted/commensurability_classification_seed.md` (§§1, 2.2f, 2.2s,
2.2t, 2.2x–2.2z, 3) and the taxonomy
`notes/unsorted/commensurability_taxonomy.json`. Lemma 2 =
`formalization/QuerySystem/QuerySystem/WindingInjectivity.lean`.

## PHASE-4 PROOFS WRITTEN (2026-07-09) — ⟦HAND — unverified⟧, USER MUST VERIFY

The six PROVE-ORIGINALLY items (per `notes/PROOF_PROMPT.md`) are now written out
as full proofs in `reconstruction_body.tex` (builds clean, 12pp). All are
LLM-generated and NONE is independently verified. Verify before any of them
counts as proved. Ranked by verification priority:

1. **GATE LEMMA (`lem:gate`) — REASSESSED 2026-07-09: DEFINITIONAL, not a
   theorem-with-a-gap; hand/citation check, NOT Lean.** Advisor reassessment
   (corrected the prior "entire burden" framing): with arc-value = context
   cell-probability q_i(a,b), "inflow=outflow at (i,a)" IS the coherence identity
   ∑_b q_{i-1}(b,a)=∑_b q_i(a,b) term-for-term, and "adjacent-coherence = full
   EA-coherence" is exactly what the genericity gate SAYS. So (1a) is a
   definitional identity. In Lean it goes `rfl` — certifying it is theater (you'd
   build the conclusion into the definition). Recorded honestly as
   `coherence_is_conservation` (rfl-grade REMARK, docstring says so), NOT dressed
   as a theorem. **Remaining check is a HAND one: does the paper's stated
   genericity gate actually force "non-adjacent contexts share only trivial
   events"?** The phase gap (2.2z) does NOT bite here (it lives only in the §open
   pruning lemma, a surrogate for LISC, not this fixed-L statement).
2. **Flow decomposition (`lem:flowdecomp`)** — where the content sits (extreme
   circulation = SINGLE simple cycle; R = conv(winding-1); C≠R ⟺ ∃ winding-≥2
   vertex). General decomposition is classical (Ahuja–Magnanti–Orlin Thm 3.5),
   Mathlib-absent ⟹ AXIOMATIZED honestly. **KERNEL NOW LEAN-CERTIFIED (see below):
   the winding-1/config correspondence + fractional dichotomy are PROVEN on top
   of the axiom, 0-sorry, standard axioms only.**
3. **Layer-injectivity (`lem:injectivity`)** — ALREADY Lean-certified
   (WindingInjectivity.lean, 0-sorry). No action.
4. **Parity theorem (`thm:parity`)** — det(I+P)=1−(−1)^L via roots of unity;
   odd-case unique fractional vertex u≡½ (zero-coord⟹forest-face⟹integral, so
   all-positive⟹all edges tight⟹Mu=1). Machine-corroborated joints (2.2f).
5. **PR-box (`cor:prbox`)** — separating facet + contextual-fraction-1 (no
   exactly-one-per-edge cover on odd ring; 2∑v=L impossible). Check the CF=1
   sub-model support argument.
6. **θ-sweep / signable (`thm:taming7`)** — TU via Hoffman–Gale signing + the
   explicit anti-comonotone θ-sweep construction. Construction certified on 8
   ρ₅ vertices (2.2o); verify the general reproduce-q-exactly claim.
7. **Forest counting (`thm:forest`)** — cycle⟹kernel-vector⟹not-MD; the
   |ρ|≤2|A|−1 count. Bijection machine-checked over 1819 targets (2.2s).
8. **Taming (10) / phase decoupling (`lem:taming10`)** — fibered C=t·FSTAB⊕
   (1−t)·FSTAB; signature dim=1+2·15 confirmed on subdivided-K₅ (2.2s).

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
- **Independent verification of items 1–8 above** (Lean for formalizable, manual
  otherwise). Item 1 (gate lemma) is the priority.
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
