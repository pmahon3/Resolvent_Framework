# σ-nerve / torsor / lim¹ seed — normalization of CSS/no-GS obstructions

> **DISPOSITION: PARKED (user decision 2026-07-18) after Phase-2 audit
> verdict REVISE — kill condition (a), no leverage on ODBC-S/CODBC.
> Surviving components absorbed into
> `notes/open_questions/oml_attack/oml_odbc_sigma_nerve_absorption.md`
> (index-category fence, obstruction-shape restatement, binary
> regularity, acyclic-nerve falsifier, B1 attribution). Re-entry
> triggers listed there; do not resume this frame without them.**

> **PROVENANCE BANNER:**
> This frame is LLM-originated (design conversation, Claude Fable 5,
> 2026-07-17). Every literature claim inherited from that conversation is
> ⟦UNVERIFIED-LLM⟧ until primary-verified in this session. Design-session
> confidence is correlated across claims — the same prior underwrites the
> citations AND the novelty assessment, so verification must be independent
> per claim, never "the design session said so." Do not cite the design
> conversation as a source.

*Phase 1 seed, 2026-07-18, branch `explore/c-sigma-nerve`. Session scope:
seed + falsifiers only. No Phase-4 work on B2; no self-certified audit; no
campaign-chain writes.*

> **PHASE-2 AUDIT OUTCOME (2026-07-18, fresh-context opus, verdict in
> `SIGMA_NERVE_AUDIT_VERDICT.md`): REVISE — kill condition (a) fired on
> the headline.** "All live obstructions are T0" is near-tautological
> (by ODBC Lemma 2.1, CSS already keeps every countable-cofinality stage
> alive; T0 restates CSS∧¬GS) and vacuous (all four T0 rows fail
> realization gates; the ledger has ZERO actual admissible-OML ODBC
> failures). §5(iii) is well-posed only as an ω-tower statement; over
> [ω₁]^{≤ω} — where C needs its ZFC twist — the right object is limⁿ,
> not lim¹, so the well-posed regime is axiom-sensitive and the ZFC
> regime is ill-posed as drafted. **Surviving components:** the B2
> index-category/ML constraint (§3-1, certified correct), the T0
> cofinality repair, the canonical-involution repair, the acyclic-
> assembly falsifier prediction, and the appendix's proofs (sound; C.2/
> C.3 are KNOWN — Navara, Rep. Math. Phys. 20 (1984), confirmed — so
> only the D-localization is residue). Disposition decision owed to the
> user; see EXIT_MEMO post-audit block.

**Claimed type(s): INSTRUMENTAL — inherits from the σ-essential/Theorem-2
programme** (user directive 2026-07-18). This seed is not a standalone
contribution and is not headed for isolated publication; its type status
is whatever the parent problem's resolution earns. **Bar (the only one
that matters):** does the frame produce leverage on the current problem —
concretely, does the T0/T1/T2 normalization discriminate among ODBC-S /
CODBC attack routes, does B2 constrain what lattice closure can be made
to do, and does C name a buildable witness architecture? The original
Type-4 three-statements framing (Theorem A, B2, C + the B1 package) is
retained below as structure, but B1 novelty is demoted from bar-critical
to citation bookkeeping: B1 is infrastructure for the engine, and its
prior-art status (§4 P1/P3) matters for honest attribution, not for
whether this seed lives. Secondary contingent Type 5 if B2 later lands
remains noted.

**Falsifiers, declared up front (reweighted per the instrumental
framing):**
(a) the frame fails to discriminate among live attack routes on ODBC-S /
CODBC — no prediction it makes differs from what the corpus already
forces (kill condition);
(b) torsor/lim¹ identification ill-posed (§5) (kill condition);
(c) zoo typing finds substantial neither-T0-nor-T1-nor-T2 mass (§6)
(kills Theorem A as stated);
(d) prior-art hit on the B1 localization or the σ-scale torsor reading
(Navara/Šipoš/PP91 axis, §4) — **attribution fix, not a kill**: B1 is
infrastructure; a hit changes citations, not the seed's viability.

## 1. Foundation layer (Layer 0) — status: largely banked

Setting: concrete σ-class L on Ω (∅ ∈ L, complement-closed, closed under
countable disjoint unions, order = inclusion); "σ-complete OML" adds
latticehood. The following are **already banked** and are cited, not
re-proved: comparable differences are events (orthomodular difference);
every pairwise-orthogonal family extends to a block; blocks are σ-fields
of sets; two-valued σ-additivity is exactly blockwise σ-additivity
(attack note §9, Lemmas A1/A2/L0; **Lean-certified, axiom-free**, in
`formalization/QuerySystem/QuerySystem/ConcreteOMLBlocks.lean`).

New to this seed (proved in the appendix,
`sigma_nerve_torsor_seed_appendix_b1.md`):

- **L0.1 (countable increasing sups).** In a concrete σ-class, every
  **countable** increasing chain has a sup equal to its union.
  ⚠ Countability is load-bearing: an ω₁-chain's union need not be an
  event; nothing here applies to chains of uncountable cofinality.
- **L0.2 (countable lattice-completeness).** A concrete σ-complete OML
  has all countable joins, ⋁ₙaₙ = ⋃ₙ(a₁∨…∨aₙ), and dually countable
  meets. Countable joins may strictly overshoot unions; the Campaign-19/20
  residue events (the banked four-residue squares of gate-avoiding
  terminals) are exactly finite instances of this overshoot.
- **L0.3 (blockwise assembly).** Blockwise σ-states agreeing on
  interfaces assemble to a σ-state on L; σ-additivity is only ever tested
  inside blocks (re-derivation of Φ ⟺ GSD ⟺ ODBC packaging at the level
  of states). Consequence: **latticehood acts on the incidence structure
  (forced meets, forced tails, new blocks), never on the state axioms
  directly.**

## 2. Objects (Layer 1) — matched to the exact ODBC formalism

All fibre definitions are those of
`oml_distributed_boundary_compactness.md`: pattern p, ambient fa witness
μ ∈ C_p, eligible fibre Y_B(p,μ), section spaces X_p(J) over the directed
poset 𝒥_{≤ω}(I) of countable subatlases, bonding = forget blocks, keep μ.
CSS and no-GS are exactly ODBC-S's and ODBC-G's clauses.

- **σ-nerve N(L):** vertices the maximal blocks, simplices finite block
  families with nontrivial joint interface (joint overlap σ-field ≠ {0,1}).
- **Interface fibre over an interface state:** fix a simplex σ, an
  eligible state τ on its joint interface, and an adjacent block B; the
  fibre is {v ∈ Y_B(p,μ) : v restricts to τ}.
- **Binary-regular interface:** every eligible interface state has
  **exactly two** lifts into each adjacent block. On a two-element fibre
  the swap involution is *canonical* (the unique nonidentity permutation),
  so no separate "definable involution" datum is required — the earlier
  draft condition is vacuous at cardinality 2 and is dropped. The
  substantive content of binary regularity is the cardinality condition
  plus bonding equivariance, which is automatic for the canonical swap.
- **Decision atlas:** all interface fibres binary-regular. Over a decision
  atlas the section system is a system of Z₂-torsors.

**Candidate identification (a theorem to prove or refute, not a
translation):** over a decision atlas, CSS/no-GS is equivalent to
σ-locally trivial but globally nonvanishing first derived limit (lim¹) of
the Z₂-torsor system over 𝒥_{≤ω}(I). ⚠ Well-posedness caveats in §5;
index-category caveat in §3.

## 3. The three statements

**Theorem A (candidate trichotomy; the third type is now explicit).**
Every CSS/no-GS instance on a concrete Boolean-block atlas is exactly one
of:

- **T0 (fibre death):** some chain (J_α)_{α<λ} in 𝒥_{≤ω}(I) — λ of
  **uncountable** cofinality, every countable initial segment retaining a
  nonempty inverse-limit fibre — has empty limit fibre. ⚠ Definition
  repaired this session: the design conversation's phrase
  "countable-cofinality chain" misfires on its own paradigm cases — in
  the Ulam evaluation, the club field, and the Cantor singleton cover,
  every countable-cofinality chain has nonempty limit (the union of a
  countable chain of countable subatlases is a countable subatlas, and
  CSS feeds it); death occurs only at uncountable cofinality.
- **T1 (torsorial class):** binary-regular throughout, sections exist
  σ-locally, and no-GS is a nonvanishing lim¹/H¹ class of the Z₂ system.
- **T2 (mixed regime):** interface fibres of mixed cardinality (0/1/2 or
  higher), neither pure death nor pure torsor. Evidence this type is
  genuinely inhabited: the Greechie-pentagon fibre census (§5: lifts
  number 1 or 2 depending on the interface value) and, at the finite
  shadow, the known **sufficient-but-not-necessary** gap of the
  Abramsky–Mansfield–Barbosa Čech obstruction — imported as evidence FOR
  the third type, not hidden.

**B2 (target only — NOT attempted here; Phase 4 is the user's).**
σ-lattice closure of a decision atlas enriches the bonding system (forced
meets, forced tails, the blocks they generate) enough to force a
Mittag–Leffler-type condition, hence lim¹ = 0, hence no T1 obstruction.
Three binding constraints, recorded so a future proof cannot cheat:

1. **Index-category constraint (added this session).** ML ⟹ lim¹ = 0 is
   an ω-tower theorem. Over ω₁-shaped or general σ-directed index posets
   — where Layer 5 locates the ZFC-nontrivial twists — surjective bonding
   does *not* kill lim¹ (that failure *is* the Talayco/gap phenomenon).
   Any B2 proof must either prove the relevant subatlas poset admits
   countably cofinal reduction for the specific system, or use derived-
   limit technology over general index posets. A B2 proof valid only at
   countable cofinality does not touch Theorem C's ω₁-indexed candidates,
   and must say so.
2. **Calibration constraint (binding).** Any proof must use tail events
   (L0.2) and hence visibly fail on the machine-checked product-Ulam OMP
   witness (`papers/sigma_essential/witness_candidate/`), where joins of
   Specker-incompatible sequences do not exist. The Fodor shape
   (trivializing data regressive on limit stages) is a hope, not an
   argument.
3. **Finite calibration instance (added this session).** The mechanism
   B2 posits — closure enriching bonding — has a machine-verified finite
   instance: on the full-grid branch, stage-2 complement/disjoint-union
   closure alone forced the nontrivial same-side meet
   `q0ᶜ∧q1 = F₀₁₀₁ ⊔ sel2`, invisible to every join-level descriptor
   (receipts `verification/full_grid_stage558_hull_gap_isolation*`,
   `*_meet_witness*`), and every gate-avoiding terminal carries the
   banked four-residue squares. Enrichment is real at finite scale; B2
   asks whether it is strong enough at σ-scale.

**C (witness brief — design constraints only).** Realize a ZFC-nontrivial
class — a Hausdorff-gap cohomology class in P(ω)/fin, or a nontrivial
coherent sequence on ω₁ — as the bonding twist of a concrete decision
atlas whose lattice closure adjoins only degenerate tails (0, 1,
countable-ideal-supported). Design law from the import sweep: **the twist
lives in the identifications, never inside a block** (in-block gap
structures are rescued, meet-closed, dead). DW compliance is automatic
(gap/club structures are natively non-Polish/coarse-riding); the named
wall is σ-Loomis–Sikorski realization, crossed in reverse. A ZFC witness
needs a ZFC twist, hence the ω₁-indexed source menu (§4 rows T1–T3), not
the axiom-sensitive ω^ω-indexed systems.

**Named well-posedness task (index category).** The seed must eventually
prove which index category 𝒥_{≤ω}(I) resembles for the atlases in play
([ω₁]^{≤ω} vs towers vs ω^ω): the derived-limits literature over general
index posets is the technology source. For |I| = ω₁ the poset [ω₁]^{≤ω}
is σ-directed of cofinality ω₁; nothing here identifies it with ω^ω, so
independence probes (§4 rows T5–T6) aim only at ω^ω-indexed systems.

## 4. Prior-art pass (Task 3) — per-claim verdict table

Verification state after this session. "Fetch" = absent from
`notes/literature_review/literature/`; do not trust memory for it.

| # | Claim / source | Verdict |
|---|---|---|
| P1 | Navara–Pták 1983, *Two-valued measures on σ-classes*, Čas. pěst. mat. 108(3) 225–229 | ⟦VERIFIED-primary this session, in library⟧ Gudder-integral additivity for two-valued states on σ-classes; does not state B1. **Its references surface two direct B1 threats:** Navara, *The integral on σ-classes is monotonic* (Rep. Math. Phys., ~1983) and Šipoš, *Integral with respect to a pre-measure* (Math. Slovaca 29 (1979)) — monotonicity/continuity of σ-class integrals. **FETCH BOTH before any B1 novelty claim.** |
| P2 | Pták–Pulmannová 1994, CMUC 35(1) 205–208 | ⟦VERIFIED-primary this session, in library⟧ Subadditive-state characterization of Boolean among OMLs. Adjacent axis (Boolean-vs-OML via subadditivity), does not contain B1's lattice/poset tail localization. |
| P3 | Pták–Pulmannová 1991 monograph (Orthomodular Structures as Quantum Logics) | ⟦UNVERIFIED-LLM; FETCH⟧ — the expected home of monotone continuity/Fatou at σ-OML generality. B1's bar rests here plus P1's two leads. |
| P4 | Kalmbach 1983 (in library); Dvurečenskij–Neubrunn–Pulmannová 1992 (in library) | ⟦IN-LIBRARY, unread this session⟧ — check state chapters for monotone continuity before the Phase-2 audit. |
| P5 | Abramsky–Mansfield–Barbosa, arXiv:1111.3620 (QPL 2011): finite Čech obstruction; sufficient but NOT necessary | ⟦VERIFIED-web 2026-07-17 (design session)⟧; primary PDF **absent — FETCH** (library's `abramsky_brandenburger_2011.pdf` is the *sheaf* paper, a different object). Successors to check: AvN 2015, Okay–Roberts–Bartlett–Raussendorf, Aasnæss, Caru. |
| P6 | Bergfalk–Lambie-Hanson, *The Cohomology of the Ordinals I*, arXiv:1902.02736 | ⟦VERIFIED-web THIS session: title/authors/abstract confirmed⟧ Čech cohomology of ordinals generalizes walks/coherent sequences on ω₁. **Novelty consequence accepted:** the ω₁ cohomology framework exists; this seed's novelty rests entirely on the OML/σ-state/lattice-closure side. |
| P7 | "Todorcevic's transformation interconverts coherent families and gaps (arXiv:2607.03995 §4)" | ⟦AUDIT-RESOLVED 2026-07-18⟧ arXiv:2607.03995 is **Bannister–Moore** (forcing paper); the "§4 presents the transformation" claim is **REFUTED** — no such transformation there. Attribute the gap ⟷ coherent-sequence interconstruction to **Todorcevic, *Walks on Ordinals* (2007)**. |
| T1 | Talayco, APAL 71 (1995) 69–106 (+ part II 1996); Morgan MLQ 1995: Hausdorff-gap cohomology classes ZFC-nonvanishing, not trivialized by MA(ω₁) | ⟦UNVERIFIED-LLM; FETCH⟧ |
| T2 | Walk-based coherent sequences give nontrivial Ȟ¹(ω₁) in ZFC | ⟦UNVERIFIED-LLM (rests on P6's framework); verify from P6's primary PDF⟧ |
| T5 | Mardešić–Prasolov TAMS 307 (1988): lim¹A ≠ 0 under CH; Dow–Simon–Vaughan 1989: lim¹A = 0 under PFA | ⟦UNVERIFIED-LLM; FETCH⟧ |
| T6 | Bergfalk–Lambie-Hanson Forum Math. Pi 2021 (weakly compact); Bergfalk–Hrušák–Lambie-Hanson JML 2023 (ℶω-Cohen); Veličković–Vignati 2024 | ⟦UNVERIFIED-LLM; FETCH⟧ |
| P8 | Harding 2004 (concrete OMLs, in library); Navara–Rogalewicz (pasting) | Harding ⟦IN-LIBRARY, unread this session⟧; Navara–Rogalewicz ⟦UNVERIFIED-LLM; FETCH⟧ — C's pasting side. |

**Standing verdict:** no fatal prior-art hit found this session; the
B1-component threat (P1's two leads + P3) is live and unresolved; the
frame's cohomological reading of ω₁ combinatorics is known (P6), as the
design session already conceded.

## 5. Well-posedness of the torsor/lim¹ identification (Task 4)

**Exact conditions.** (i) Binary regularity as in §2 (pure cardinality +
equivariance; involution canonical). (ii) σ-local triviality: over every
countable subatlas a section exists (= ODBC-S clause). (iii) The
obstruction datum: choose any σ-local section family; the failure of
global matching is a Z₂-valued difference 1-cocycle on the nerve of the
countable-subatlas cover; CSS/no-GS = the class is nonzero in the
appropriate derived limit. Statement (iii) is the candidate theorem; it
is NOT proved here.

**Test 1 — ω₁ cylinder atlas (ledger row: "omega-one cylinder common
hub").** The hub block is a coarse (not countably generated) σ-field of
countable/co-countable type; its eligible σ-lifts include one
non-principal state and a proper class of Diracs constrained by μ.
Interface fibres are not two-element: binary regularity **fails**, so the
atlas is not a decision atlas and the lim¹ identification does not apply
to it. Its CSS/no-GS mechanism is emptiness of the limit fibre at
uncountable cofinality with all countable stages alive — **T0 under the
repaired definition**, as predicted. ⟦HAND, from the banked architecture
description; a fibre-cardinality census is the named finite check⟧

**Test 2 — punctured-Cantor star.** Eligible fibres are
continuum-sized (sections avoid the point defects); binary regularity
fails; moreover the hub is impossible in a concrete σ-complete OML
(banked theorem), so the architecture never reaches the decision-atlas
question. T0-shaped at the abstract level; not applicable as an OML.

**Test 3 — finite torsor shadows (pentagon / MO3 cells).** In a 3-atom
Boolean block, an interface state τ on a shared atom a has **one** lift
if τ(a) = 1 and **two** lifts if τ(a) = 0. The Greechie pentagon is
therefore *conditionally* binary — a Z₂ system over the odd 5-cycle on
the τ(a) = 0 locus, interrupted by unique-lift branches — and its
odd-cycle holonomy never becomes a CSS/no-GS obstruction at finite scale
(Φ trivially holds). This is the concrete finite exhibit of **T2** and
the finite shadow of the AMB sufficient-not-necessary gap. The MO3
conditional cell's fibre census is left as a named finite computation.

**Outcome (which signal, and why).** No known σ-scale architecture in
the corpus satisfies uniform binary regularity. This is recorded as a
**Φ-side signal, not an early kill of T1**: every architecture in the zoo
was built for other purposes, and none was designed to be a decision
atlas; C's design brief (twist in the identifications of a deliberately
binary-regular atlas) is exactly the untried construction. A kill would
require showing binary regularity is *unattainable* at σ-scale, which
nothing here shows.

## 6. Zoo typing run (Task 5) — the frame's primary falsifier

Typed against `CAMPAIGN_CHAIN.md` **working-tree state, sha256
e9c02777…** (uncommitted relay state at typing time; worktree HEAD
`c110c4d`) and `CURRENT_STATE.md` sha256 `7da7ce47…`. Types: T0 / T1 /
T2 / tame (Φ-tame or gates fired; frame satisfied vacuously) / n.a. (not
a CSS/no-GS instance: nonlattice, artifact, refuted, or impossible) /
open.

| Ledger row | Type | One-line justification |
|---|---|---|
| Cantor singleton Boolean boundary atlas | T0 | every countable subfamily escapable; limit fibre empties only at uncountable cofinality |
| club-field local lifts | T0 | each countable envelope solvable; coherence dies at the ω₁ limit (CIR failure) |
| actual admissible OML failure of ODBC | n.a. | none exists |
| abstract two-fibre cut-saturated Helly-2 failure | T2 (abstract shadow) | width-2 pairwise-consistency death, not a torsor class; not an OML, fails realization gates |
| Cantor singleton CSS-without-GS model | T0 | same mechanism as row 1; eligible spaces noncompact, death at the top |
| standard-Borel local realization | n.a. | local realization complete; fails OML transport gates, no CSS/no-GS instance |
| two-selector P2xP2 / P2xP3 / P3xP2 | tame | finite, Φ-tame |
| orthogonal two-atom arbitrary-base family | tame | σ-complete, conditionally Φ-tame; no CSS/no-GS instance |
| non-atomic independent completion | tame | finite centre-free OML, Φ-tame |
| non-atomic diagonal completion | tame | finite centre-free OML, Φ-tame |
| punctured-Cantor shared hub | n.a. | hub impossible in a concrete σ-complete OML (countable-meet contradiction) |
| omega-one cylinder common hub | T0 | the flagship CSS/no-GS instance; fibre death at uncountable cofinality (§5 Test 1); not binary-regular |
| unconditional state-normal omega-one completion | n.a. | impossible (no σ-states, no order separation) |
| incompatible conditional omega-one transport | open | blueprint only; cell and completion open — untypeable until built |
| incompatible pentagon conditional cell | tame (T2 shadow) | finite Φ-tame; conditional-binary fibres = the T2 finite exhibit (§5 Test 3) |
| literal MO3 conditional cell | tame | finite Φ-tame; fibre census = named finite computation |
| fixed-interface two-cell closure | tame | finite Φ-tame |
| fixed-pattern k-cell scaling | tame | finite evidence k ≤ 3, Φ-tame |
| arbitrary-index one-hub family | tame | St_fa = St_σ hence Φ; no obstruction to type |
| bipartite grouped coordinate core | n.a. | nonlattice |
| full conditional 2x2 grid | n.a. | nonlattice (repair substrate, not an OML) |
| stripped rectangle terminal repairs | tame | OMLs but gate A fires (Bool reconstructed) |
| stripped K22 macro completions | n.a. | exhaustive reconstruction theorem, not an instance |
| full-grid fine-fibre repairs (558) | n.a. | nonlattice stages |
| same-carrier distributed terminal OML (18676 events) | tame | finite gate-avoiding OML, Φ-tame; carries banked residue squares = B2's finite calibration, not a torsor |
| full-cycle MDD grammar | n.a. | closure artifact |
| stage-558 splitter family | n.a. | nonlattice stage |
| IC-1 `MO2 × P(3)` proper-joint completion | tame | finite, 16-element centre, Φ-tame |
| IC-2 three-block noncentral transverse triangle | tame | finite Φ-tame; boundaries saturate |
| IC-3 44-event seven-block survivor | tame | 12 point states give the full relation, Φ-tame |
| IC-4 inflated five-block survivor | tame | σ-complete centre-free; Φ-tame via common-fibre point replacement |
| IC-5 whole-interface `P(2)` triangle twists | tame (T1 shadow, trivialized) | the one genuine finite twist family: odd parity nonfaithful, even parity **gauge-trivial** — finite twists die, consistent with B2 |
| IC-6 literal substitutions / single-pullback route | tame | Φ-tame under stated hypotheses |

**Verdict of the run:** the falsifier does **not** fire — there is no
substantial unclassifiable mass. Every live σ-scale CSS/no-GS instance in
the corpus (4 rows) is **T0**; **T1 is empty**; T2 is inhabited only by
finite shadows and one abstract skeleton; the rest are tame or not
applicable. Two readings, both recorded: (i) supports B2 (lattice-side
mechanisms so far only produce fibre death, and the one finite twist
family is gauge-trivial); (ii) exposes that the T1 class is untested —
nothing in the corpus was built to be a decision atlas, so C is a genuine
construction question, not a survey question.

## 7. Re-audit triggers memo (Task 6)

**(a) BOC normalization (open question, boundary-obstruction
completeness).** Theorem A is its candidate promote-to-seed exit: if the
trichotomy lands, BOC's "which obstructions are complete" question
acquires the normal form it lacked. New input = this seed + the typing
run. Recommendation: hold BOC dormant until Theorem A survives the
Phase-2 audit; then re-audit BOC with the trichotomy as the triggering
input.

**(b) Campaign-2 Mittag–Leffler dead lead — sharpen guardrail applied
honestly.** Guardrail condition (a): has a standing check flipped, or
does a new hypothesis exclude the old refuting instance? The binary-
regular (decision-atlas) hypothesis **does** exclude the `P(N)` control:
its whole-boundary lift fibres are state spaces of infinite Boolean
algebras, cardinality ≫ 2, so the old refutation instance is outside the
new hypothesis class — this exclusion is verified by inspection of the
fibre definition, not asserted. Guardrail condition (b): is there a
concrete witness keeping the lead live? **No.** The typing run (§6) shows
the decision-atlas class is currently EMPTY at σ-scale; a hypothesis
class with no inhabitants cannot carry a live lead. Verdict: **the lead
stays dead.** It may re-enter only as part of B2 (which needs the
general-poset ML-type technology anyway, §3 constraint 1) and only if C
or another construction populates decision atlases. This is a
conditional re-entry note, not a sharpen.

## 8. Evidence-class ledger for this seed

| Claim | Class |
|---|---|
| L0.1–L0.3 | Hand proved (appendix); foundations cited to Lean-certified §9 layer |
| B1 package | Hand proved (appendix); **novelty OPEN** (P1/P3 threats) |
| B1 calibration on the OMP witness | Hand proved against the machine-checked witness |
| Theorem A trichotomy | Open (candidate normalization; T2 evidenced, not proved exhaustive) |
| torsor/lim¹ identification | Open (candidate theorem; well-posed only on decision atlases) |
| B2 | Open target; not attempted; three binding constraints recorded |
| C | Design brief only |
| Zoo typing table | Hand classification against banked descriptions; anchored to the shas in §6 |
| Pentagon fibre census | Hand proved (3-atom block lift count) |
| ω₁-cylinder binary-regularity failure | Hand argued from banked architecture; fibre census not yet computed |
