# Chain-level hostile audit (Campaign 20 boundary, 2026-07-20)

**Provenance.** Run as an opus subagent (hostile referee), findings-only, at
the Campaign-20 boundary just after the W-P/perspectivity route was falsified.
The previous chain-level hostile audit was Campaign 7 (~iteration 44); the
chain is now 300+. Triggered by E5 handoff §5.3. Read-only over
`CAMPAIGN_CHAIN.md`, `CURRENT_STATE.md`, `linearization_E4_verdict.md`,
`STRATEGY_ADVERSARIAL_REVIEW_2026-07-18.md`, and the specific notes/receipts
they point to.

## Verdict

**NO MATHEMATICAL RETRACTION — chain is sound as claimed.** No counterexample
gate passes beyond finite/tame controls; the load-bearing HAND proofs survive
hostile reading; the three new E4 rows survive. One stale header caveat and
one honestly-labelled conditional verdict noted, neither a retraction.

## Findings (most severe first)

1. **Stale header, ledger correct.** `oml_arbitrary_two_atom_inflation.md:3-4`
   still caveats "arbitrary-base latticehood remains open," but §1–§2 (OE lemma
   + executable kernel exhausting all 16 `L(P(k),P(l))`, `k,l≤4`; binding
   `P(4)×P(4)` = 1220 events, 744,810 pairs, all pass) actually PROVE
   latticehood + σ-completeness. Ledger row 70 ("proved") is correct; the
   header line is stale/misleading. **ACTION: fix the header caveat.** The open
   items are the state gates and the §6 further constructions, not this
   family's latticehood.

2. **Charter A — the one conditional Phi-tame verdict.** The "orthogonal
   two-atom arbitrary-base family" is the sole INFINITE construction whose
   Phi-tameness is conditional, not proved (`CAMPAIGN_CHAIN.md:155`,
   `CURRENT_STATE.md:156-157`): honestly labelled "state gates open;
   conditionally Phi-tame." Not an overclaim, but it is the answer to "any tame
   verdict resting on an unaudited step" — the state-classification/
   order-separation gates are open. The two PROVED infinite tameness claims
   (arbitrary-base inflation common-fibre point replacement; one-hub
   `St_fa=St_sigma`, C15) accepted as stated, not independently re-derived.

3. **Charter B — Campaign-11 puncture-meet theorem SURVIVES** (the
   highest-value generalization target). The crux `⋀_L j(U_n)` restricting to
   `0` in `B_i` but `{i}≠0` in `B_j` is a genuine contradiction in a concrete
   σ-complete lattice (`oml_distributed_relation_cell_assembly.md:61-90`).
   Correctly scoped: kills only the countably-generated SEPARATING shared
   boundary. The two live escapes (uncountably-generated separating boundary;
   distributed nonseparating quotients) are self-flagged. **Strategic caveat:
   "generalize C11 to prove Phi" has a large self-flagged gap — the uncountable
   case is exactly C12's central ω₁ cylinder, which C11 does NOT exclude. Do
   not oversell this pivot.**

4. **Charter B — C12 extension + C13 normality trichotomy SURVIVE.** Both
   carefully scoped: C12 states its σ-homomorphism/faithfulness hypotheses as
   load-bearing and marks σ-completion de-centralization open
   (`oml_omega1_cylinder_hub.md:9-37,118-130`); C13's trichotomy explicitly
   does not close face-local MBRC
   (`oml_puncture_normality_and_incompatible_transport.md:84-99`). No
   finite-to-infinite extrapolation presented as theorem.

5. **Charter B — T4At conditional + Campaign-20 kernel-retraction rows:
   dispositioned, low severity.** T4At-⇒-Phi accepted as conditionally stated
   (hypotheses explicit). The C20 kernel-retraction/re-basing rows are finite
   two-copy assembly; their failure mode is "transport architecture is wrong,"
   not "Phi is false" (strategy review F2). Named for completeness.

6. **Charter C — all three E4 rows SURVIVE hostile reading.**
   (1) Non-extendability ("value-1 FIP fails at finite stage ≥3"): underlying
   lemma is BPI-exact and the choice principle is honestly flagged everywhere
   (E1 "BPI-only exact"; (3⟹2) uses exactly the ultrafilter lemma). E1
   proof-read is genuinely hostile — it CAUGHT and downgraded the "exactly C11
   Lemma C2" claim to "set-intersection shadow" (partial match). E2b locator is
   exact: A={1,2},B={1,3},C={2,3} → pairwise singletons, triple empty → FIP
   fails at stage exactly 3.
   (2) "perspectivity = ODBC bond — refuted": scrupulously scoped
   (non-selectivity rep-invariant; the 10 co-charging-proxy pairs flagged as
   illustration, not a ρ-theorem).
   (3) Localization ("reach localized to the second inclusion"): honestly
   labelled a frontier-narrowing, NOT progress toward proving Phi. **Flag: the
   localization is CONTINGENT on the unverified paywalled DNP-2015 lead**
   ("holds exactly when the screen turns up no lattice σ-complete
   non-extendable carrier"). Honestly flagged as promote-on-confirmation, so
   not an overclaim — but conditional, not established.

## Strategic call (Charter D)

The chain is NOT purely witness-hunting: the puncture-meet theorem, the C13
normality trichotomy, and "Phi ⇔ T4At (countable atlas)" are all Phi-FORCING
results, and the base rate (C11/12/13 + the W-P detour, all producing
obstructions) leans obstruction. **The decision being avoided is a framing
inversion:** the adopted roadmap files Stage 3 as "witness-hunt, obstruction as
fallback," when the accumulated yield is on the obstruction side. The honest
call: keep the ω₁ witness object as the FALSIFICATION TEST, but make PROVING
Phi on the two surviving escapes (uncountably-generated separating boundary;
distributed nonseparating quotients) the PRIMARY target — those two escapes are
simultaneously the last witness-hunt targets and exactly what a Phi-proof must
close. Same frontier, inverted priority. Secondary avoided decision: strategy
review F2/F3 warn the finite ARR grammar cannot touch Phi and no stopping rule
is in force at 300+ iterations — the grammar engine should be gated hard
against the (still uncreated) `SIGMA_LAYER_TARGET.md` clauses before more finite
rule-discovery iterations are spent.

## Disposition for E5 / next session

- **ACTION (cheap):** fix the stale latticehood-open header in
  `oml_arbitrary_two_atom_inflation.md:3-4` (finding 1).
- **Consider (user's call):** the framing inversion — Phi-proof primary,
  witness object as falsification test. NOT executed here; recorded for the
  thesis-advisor checkpoint.
- **Gate:** hard-gate the grammar engine against the Stage-0 clauses before
  more finite rule-discovery iterations (finding, strategy review F2/F3).
- No retraction; no ledger edit required by the audit beyond finding 1.
