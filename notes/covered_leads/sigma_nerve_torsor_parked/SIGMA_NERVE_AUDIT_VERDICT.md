# Phase-2 audit verdict — σ-nerve / torsor / lim¹ seed (mode: `/audit full`, INSTRUMENTAL framing)

*Auditor: fresh-context Phase-2 run, 2026-07-18. Targets: `sigma_nerve_torsor_seed.md`,
`sigma_nerve_torsor_seed_appendix_b1.md`, `sigma_nerve_seed_EXIT_MEMO.md`,
`prediction_entry_DRAFT.md`. Context read: `oml_distributed_boundary_compactness.md`,
`CAMPAIGN_CHAIN.md`, `CURRENT_STATE.md`, attack-note §9. Web-verified citations where noted.
Wrote only this file; no campaign or main-checkout write.*

---

## VERDICT: **REVISE** (frame is mostly decorative *as currently stated*; one component survives)

The seed's own bar is LEVERAGE: does the frame produce a decision on ODBC-S / CODBC /
Campaign-20 that the corpus does not already force? On that bar the frame **fails its
headline claims** — the T0-typing result and the acyclic-forbids-T1 prediction are
non-actionable, and the T0 typing rests on treating realization-gate-failing skeletons as
"live obstructions" when the ledger explicitly records **zero** actual admissible-OML ODBC
failures. This is close to kill condition (a). It is not a clean KILL because **one** piece —
the B2 index-category / Mittag–Leffler constraint (§3 constraint 1) — is mathematically
correct, non-trivial, and supplies a genuine *guardrail* (a reason a whole class of B2 proof
attempts is dead over ω₁). That is real but modest leverage: it blocks a route rather than
opening one, and it re-derives a decision (ML dead) the ledger already made. Hence REVISE:
keep the index-category constraint and the (sound) L0/appendix infrastructure; retract or
heavily downgrade the "all live obstructions are T0 / frame discriminates" leverage claim and
the EXIT_MEMO's PROMOTE recommendation, which the audit does not support.

---

## Q0 — LEVERAGE (decisive)

Three leverage claims, each run against the bar "name one changed attack action not already
forced by the ledger":

**(1) "All live corpus obstructions are T0."** Two independent failures.

- **T0 is near-tautological.** T0 = "every countable stage alive, limit fibre empty at
  uncountable cofinality." Unwind against the ODBC formalism (`…boundary_compactness.md` §3):
  CSS = `X_p(J)≠∅` for every countable `J`; no-GS = `X_p(I)=∅`. By Lemma 2.1, `X_p(I)` **is**
  the inverse limit over `𝒥_{≤ω}(I)`, and the union of a countable chain of countable
  subatlases is itself a countable subatlas, so CSS already forces every countable-cofinality
  stage alive. "T0" therefore says almost exactly "CSS ∧ ¬GS with the death located at
  uncountable cofinality" — which is what CSS/no-GS *means* on this index poset. Typing an
  instance T0 restates its defining property; it is not a classification that discriminates
  routes. ⟦Hand — read directly off §3 + Lemma 2.1⟧
- **The four T0 rows are not live.** The counterexample ledger (`CAMPAIGN_CHAIN.md`) row
  *"actual admissible OML failure of ODBC — none"*; and each of the four §6 T0 rows is flagged
  in that same ledger / ODBC §7 as failing a realization gate: Cantor-singleton = "abstract
  fine control; common paste central and **not order-separating**"; club-field = "coarse
  incoherent control; **no compatible coarse lift**"; ω₁-cylinder = "**σ-completion open**…
  central in the raw/finite closure"; Cantor CSS-without-GS = "abstract relational
  countermodel; eligible spaces noncompact." So "every live σ-scale obstruction is T0" reads
  correctly as "every *abstract skeleton* is T0, and nothing is actually live." That does not
  reduce CODBC to a death-exclusion statement on any realized class, because there is no
  realized class of failures to exclude. ⟦Hand — cross-check of §6 rows vs ledger + ODBC §7⟧

  **Decision changed? No.** The seed itself concedes reading (ii): "nothing in the corpus was
  built to be a decision atlas." An empty class carries no attack redirection.

**(2) Acyclic-assembly-forbids-T1 prediction (`prediction_entry_DRAFT.md`).** Genuine
falsifier, zero forward guidance — the prediction *itself* states acyclic assemblies "cannot
test T1 either way," and the Campaign-20 two-copy assembly tests GS directly (via the
56-event shared-cell closure) regardless of any typing. It changes no action; it only labels
an outcome the assembly run produces anyway. ⟦Hand⟧

**(3) B2 index-category / ML constraint (§3 constraint 1) — the survivor.** Correct and
non-trivial (see Q5). It *does* constrain the B2 proof space: it rules out any
"surjective-bonding ⟹ ML ⟹ lim¹=0" argument at the ω₁ cofinality where C wants the twist.
But (a) `CURRENT_STATE.md` Campaign 2 already records "Mittag–Leffler … yield no further
theorem," and the seed's own §7(b) keeps ML dead; so the frame supplies a *reason* for a
decision already made. (b) Its positive half — "use derived-limit technology over
`[ω₁]^{≤ω}`" — is not actionable because the §5(iii) identification it would run through is
not even well-posed at ω₁ (Q2). Net: a valid guardrail against a dead route, not a new route.

**Q0 verdict:** leverage claims (1) and (2) are **decorative** (kill condition (a) substantially
fires); claim (3) survives as a correct-but-modest guardrail. The frame does not redirect the
ODBC-S/CODBC proof space in any forward direction. This is the REVISE driver.

---

## Q1 — CORRECTNESS of the appendix hand proofs

All at concrete-σ-class / σ-complete-OML generality, sitting on the **Lean-certified §9 base**
(A1/L0/A2 — `ConcreteOMLBlocks.lean`, axiom-free). Findings:

- **A.1 (L0.1, countable increasing sups): SOUND.** `⋃aₙ = a₁ ⊍ ⨆dₙ` with `dₙ=aₙ₊₁∖aₙ`
  comparable differences (banked), countable disjoint-union closure gives membership; least
  upper bound is immediate. The scope warning ("countability load-bearing twice; ω₁-chain
  union need not be an event") is **correct and correctly propagated** — it is exactly the
  A2/T3 dividing line in attack §9 (the countable/co-countable field on ω₁ is the standing
  counterexample). ⟦Hand — matches §9 base⟧
- **B.1 (L0.2, countable lattice-completeness): SOUND.** `bₙ=a₁∨…∨aₙ` exists by latticehood,
  increases, A.1 gives the sup = `⋃bₙ`; overshoot-over-union is the banked Campaign-19/20
  residue-square data. Correct. ⟦Hand⟧
- **Remark after B.1 ("all overshoot is finitary in origin"): CORRECT but scope-trapped.**
  True for the joins that exist (countable joins reduce to finite joins + a union step that
  adds nothing). **Trap the seed half-flags but leans on anyway:** at uncountable cofinality
  **no joins exist at all** (A2/T3), so "enrichment created by binary joins, propagated, not
  created at limits" is *vacuous at the ω₁ scale that B2/C actually need*. The real ω₁
  behaviour is not "finitary enrichment propagated" but the (nonvanishing) derived-limit
  obstruction. The Remark is fine as a finite-scale localization; it must not be read as a B2
  mechanism at σ-scale. Flag AT RISK. ⟦Hand⟧
- **C.2 (monotone continuity), C.3 (Fatou): SOUND, and classical** (Q4). Orthogonal family
  `{a₁,d₁,d₂,…}` confines to one block (A1); blockwise σ-additivity gives the limit. These are
  the classical Boolean proofs transported; the appendix correctly claims no novelty for the
  *statements*. ⟦Hand⟧
- **D.1 (construction fails at C.1 on the product-Ulam witness): SOUND at the stated
  generality.** The witness's banked, machine-checked feature is Specker-incompatibility —
  relevant finite subfamilies have no join, a fortiori no countable tail `bₘ`, so C.1's tails
  / limsup / Fatou are unavailable while §A and blockwise theory survive (they need only
  σ-class axioms). This matches attack §9 T3's own statement that inner regularity "dies on
  the product Ulam carrier" precisely because the `Fₙ` intersections leave `L`. The
  localization sentence ("latticehood is used exactly at tail-event existence") is a correct
  reading of where the lattice hypothesis bites. ⟦Hand — corroborated by §9 T3⟧

**Countability-scope discipline:** respected everywhere it is needed. Every "sup = union" step
carries the A.1 restriction; the ω₁ escape is never silently used inside a countable argument.
No scope violation found.

---

## Q2 — WELL-POSEDNESS

- **Canonical-involution repair: SOUND.** Binary regularity = (cardinality-2 fibres) +
  (bonding equivariance). On a 2-element fibre the swap is the unique non-identity permutation,
  so a separate "definable involution" datum is genuinely vacuous — dropping it is correct.
  **One condition to state explicitly:** equivariance is automatic only if the bonding maps
  between adjacent 2-element fibres are bijections; on a decision atlas (all interface fibres
  2-element) the bonding forgets blocks but must restrict to a bijection on the retained
  2-element coordinate for "system of Z₂-torsors" to hold. The seed should assert bijectivity
  of bonding-on-fibres, not leave it implicit. Minor; not a well-posedness failure.
- **T0 cofinality repair: SOUND — and this is the seed's best technical move.** The design
  conversation's "countable-cofinality chain dies" was self-refuting on its own paradigms;
  the repair (death only at uncountable cofinality) is *forced* by Lemma 2.1 exactly as in Q0:
  a countable chain of countable subatlases has countable union, CSS gives a section there,
  and Lemma 2.1 says that section **is** the compatible family — so countable-cofinality death
  is impossible under CSS. The repair dodges precisely the ML-gap Lemma 2.1 warns of. Correct.
- **§5(iii) torsor/lim¹ identification: WELL-POSED ONLY AS AN ω-TOWER STATEMENT — this is the
  headline well-posedness finding.** The difference-1-cocycle / "nonzero in the appropriate
  derived limit" reading is standard and well-posed over an ω-indexed tower. Over `[ω₁]^{≤ω}`
  — *exactly* where C wants the ZFC twist — it is **not** well-posed as a lim¹ statement: the
  right object is the higher derived limits / `limⁿ` apparatus (Bergfalk–Lambie-Hanson;
  Bannister–Moore is a `limᵏ, k≥1` forcing paper, confirming lim¹ alone is the wrong single
  invariant over ω₁). The seed half-sees this (its own §3 constraint 1 and the "named
  well-posedness task"), but the identification in §5(iii) is still written as a lim¹
  statement. **Structural tension the seed does not resolve:** the well-posed regime (ω-tower)
  is the axiom-*sensitive* one (T5/T6: lim¹≠0 under CH, =0 under PFA); the ZFC-nonvanishing
  regime C needs (ω₁) is exactly the regime where §5(iii) is not yet well-posed. Until the
  index-category identification (§ "named well-posedness task") is settled, C's design brief
  rests on an un-well-posed invariant.

---

## Q3 — ZOO TYPING spot-check (≥6 rows, incl. 4 T0 + IC-5)

Typing itself is **faithful to the ledger**; the problem is what it shows (Q0), not accuracy.

| §6 row | Seed type | Ledger check | Verdict |
|---|---|---|---|
| Cantor singleton Boolean boundary atlas | T0 | CC ledger "abstract fine control; central, not order-separating"; CURRENT_STATE Campaign 3 | ✔ typing consistent; but skeleton, gate-failing |
| club-field local lifts | T0 | CC "coarse incoherent control; no compatible coarse lift"; CIR violated (Campaign 4) | ✔ consistent; not a realized OML |
| Cantor singleton CSS-without-GS model | T0 | CC "compact-ambient abstract relational countermodel; eligible spaces noncompact" | ✔ consistent; abstract only |
| omega-one cylinder common hub | T0 | CC "σ-completion open… central in raw/finite closure"; Campaign 12 | ✔ consistent; **σ-completion open**, not established live |
| IC-5 whole-interface `P(2)` triangle twists | tame (T1 shadow, trivialized) | CURRENT_STATE item 5 + CC "eight smallest whole-interface twists closed: odd nonfaithful, even gauge-trivial" | ✔ exact match |
| actual admissible OML failure of ODBC | n.a. ("none exists") | CC counterexample ledger row "none" | ✔ exact match |
| incompatible pentagon conditional cell | tame (T2 shadow) | CC "22-event centre-free OML; every nonzero event has off-pattern escape"; §5 Test 3 pentagon fibre count | ✔ consistent with 3-atom lift census |

Falsifier (c) does **not** fire — no unclassifiable mass. But the survival is hollow: three of
four T0 rows are abstract skeletons and the fourth (ω₁ cylinder) has σ-completion *open*, so
"T1 empty / all live = T0" is really "no live σ-scale instance is realized at all." Typing
accurate; leverage conclusion overstated. ⟦Hand cross-check⟧

---

## Q4 — PRIOR-ART (per-claim, web-verified; bookkeeping, non-kill)

- **Talayco APAL 71 (1995) 69–106 — CONFIRMED.** "Applications of cohomology to set theory I:
  Hausdorff gaps" (preprint math/9311205, 1993). First result **ZFC** (gap cohomology theory,
  equivalence of gaps, simultaneous gaps); incollapsible-gap existence is **independent of
  ZFC**. Seed's ZFC-nonvanishing characterization is broadly right; note the *independence*
  result is the ⋄-club-hypothesis half, not ZFC — the seed's "ZFC-nonvanishing, not
  trivialized by MA(ω₁)" should be pinned to the *first* (ZFC) result, not conflated with the
  incollapsible-gap independence. ⟦VERIFIED-web⟧
- **Coherent-families ⟷ gaps transformation attribution — SEED'S CORRECTION CONFIRMED, ITS
  §4-LOCATION REFUTED.** arXiv:2607.03995 **is** Bannister & Justin Tatch Moore, "Merging
  lim¹A≠0 with other nonvanishing constructions" — a **forcing** paper (extends
  Mardešić–Prasolov / Casarosa / Lambie-Hanson `limᵏ≠0`, adapts Kamo). Its abstract shows **no
  coherent-families⟷gaps transformation**; the claim that "its §4 presents the transformation"
  is **unsupported** — likely a design-session confabulation. True origin of the
  interconstruction: the **Todorcevic-school walks-on-ordinals apparatus** (Walks on Ordinals,
  PiM 263, 2007) constructs both Hausdorff gaps and coherent sequences uniformly; there is no
  clean single "transformation theorem" cleanly attributable to a one-line citation. Verdict:
  cite Todorcevic (Walks, 2007) for the apparatus; **do not** cite Bannister–Moore §4 for a
  transformation. ⟦VERIFIED-web (abstract) + primary-attribution reasoning⟧
- **Navara, "The integral on σ-classes is monotonic," Rep. Math. Phys. 20 (1984) 417–421 —
  CONFIRMED real.** Monotonicity / monotone continuity of the integral on σ-classes is a
  **published classical** result. This substantiates the B1 prior-art *threat*: monotone
  continuity at σ-class generality is in the literature. ⟦VERIFIED-web⟧
- **Monotone continuity / Fatou at σ-OML generality in PP91 monograph / Handbook of Quantum
  Logic — UNCONFIRMED at the section level** (search returned the monograph's existence and
  scope, not the specific theorems). Expected outcome stands: **C.2/C.3 statements are
  classical** (the appendix already concedes this and Navara 1984 corroborates for σ-classes).
  Residual B1 novelty, if any, is **only** the tail-existence localization sentence + the
  witness certification. FETCH PP91 state chapters + Handbook to close attribution; not
  bar-critical under the instrumental framing. ⟦UNVERIFIED-primary; expected KNOWN⟧

**Prior-art net:** no fatal hit (correctly non-kill here). One factual correction to the seed:
the Bannister–Moore §4 transformation claim is unsupported and should be struck; attribute the
gap/coherent-sequence interconstruction to Todorcevic's walks apparatus.

---

## Q5 — INDEX CATEGORY (§3 B2 constraint 1)

**CORRECT as stated — certify.** "ML ⟹ lim¹=0 is an ω-tower theorem; over ω₁-shaped /
general σ-directed index posets surjective bonding does not kill lim¹" is right:

- Mittag–Leffler / surjective ω-towers ⟹ lim¹=0 is the standard homological-algebra fact
  (surjective inverse sequences over ω are lim¹-acyclic).
- Over `[ω₁]^{≤ω}` (σ-directed, cofinality ω₁) surjectivity does **not** force vanishing —
  this *is* the Talayco/Hausdorff-gap phenomenon and the whole point of the
  Bergfalk–Lambie-Hanson / Bannister–Moore derived-limit literature (nonvanishing under
  surjective-type systems over ω₁).

The seed's separation of `[ω₁]^{≤ω}` from `ω^ω` from ω-towers, and its insistence that any B2
proof "must either prove countably cofinal reduction for the specific system or use
derived-limit technology over general index posets," is appropriately hedged and correct. This
is the frame's one genuinely load-bearing correct constraint (see Q0(3)). ⟦Hand + web-corroborated⟧

---

## Cross-reference

- Type-4 three-statements bar (Theorem A / B2 / C) is **explicitly demoted** by the user
  directive to non-bar-critical; not evaluated as a standalone kill.
- Under the instrumental (leverage) bar: Q0 shows two of three leverage claims decorative, one
  a correct-but-route-blocking guardrail. Q1/Q2 confirm the *infrastructure* (L0/appendix,
  cofinality repair, involution repair) is sound; Q2 shows the *engine* (§5(iii) lim¹
  identification) is not well-posed in the regime C needs. Q3 confirms no wastebasket mass but
  hollow survival. Q4/Q5 are bookkeeping + one certified constraint.
- The EXIT_MEMO's PROMOTE recommendation is the **author's** view and is **not supported** by
  this audit: the memo's grounds (a) "the frame discriminates" and (c) "no unclassifiable
  mass" are exactly the claims Q0/Q3 hollow out.

---

## RANKED FIX LIST

1. **Retract or downgrade the leverage headline** ("all live obstructions are T0 / the frame
   discriminates"). State plainly: T0 is (near-)definitionally CSS∧¬GS at uncountable
   cofinality, and all four T0 rows fail realization gates, so the typing classifies
   *skeletons*, not live obstructions. This is the REVISE-vs-KILL hinge. **(Q0)**
2. **Re-pose §5(iii) as a `limⁿ` / derived-limit statement over `[ω₁]^{≤ω}`, not lim¹.**
   Acknowledge the well-posed regime (ω-tower) is axiom-sensitive and the ZFC regime (ω₁) is
   the one the invariant is not yet defined for. Until the index-category identification is
   settled, C's brief rests on an un-well-posed object. **(Q2)**
3. **Scope-fence the B.1 Remark:** "all overshoot finitary in origin" is vacuous at uncountable
   cofinality (no joins exist); it is a finite-scale localization, not a σ-scale B2 mechanism.
   Mark AT RISK where §3 constraint 3 leans on it. **(Q1)**
4. **Fix the citation:** strike "Bannister–Moore §4 presents the transformation" (unsupported);
   attribute the coherent-sequence⟷gap interconstruction to Todorcevic (Walks, 2007). Pin
   Talayco's ZFC claim to his *first* result; keep incollapsible-gap as independence. **(Q4)**
5. **Keep and promote §3 constraint 1** (index-category/ML) as the frame's one real output — a
   correct guardrail forbidding surjective-ML B2 proofs at ω₁. Note it re-derives, not
   discovers, the ledger's dead-ML verdict. **(Q0/Q5)**
6. **State bonding-on-fibre bijectivity explicitly** in the binary-regular / decision-atlas
   definition so "system of Z₂-torsors" is licensed. **(Q2)**
7. **Close B1 attribution** (fetch PP91 state chapters + Handbook of Quantum Logic; Navara 1984
   already confirms σ-class monotone continuity is classical). Non-bar-critical. **(Q4)**
8. **Do NOT promote to Phase 3/4 as a leverage frame** on the current write-up. The sound
   infrastructure (L0.1–L0.3, appendix C, cofinality repair) may be **absorbed directly** into
   the ODBC note as banked lemmas without carrying the σ-nerve/torsor superstructure, which
   currently earns no forward decision.
