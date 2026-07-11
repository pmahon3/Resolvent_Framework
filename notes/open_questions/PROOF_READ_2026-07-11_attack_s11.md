# Fresh-context adversarial proof-read: attack note §11 (B′(i) direct attempt)

**Date:** 2026-07-11 (session 16). **Clears:** the s15 §11 proof-read
debt (opened in §11's header and the s15 handoff). **Target:**
`oml_lattice_regularity_attack.md` §11 — theorem-lets 2BR (+ OMP
fragment), monotonicity, cluster normal form, atomicity of countably
generated blocks, P⁼, kernel-FIP correction, representation-dependence
bank, Φ-density, in-block 4(i) + compact-transport criterion, ω₁
scoping bank, no-cheap-union, T4 ladder — reviewed as claims C1–C12;
plus every §11e Marczewski attribution. **Method (s12 standard):** two
independent fresh-context agents, neither exposed to the thread —
(1) adversarial math reviewer given claim STATEMENTS ONLY (definitions
self-contained; A1/L0/A2/T3 supplied as assumable, previously-verified
facts), instructed to refute; all twelve claims re-derived from
scratch, then in stage 2 line-checked against §11's actual proof text;
from-scratch machine receipts, no repo script read or reused;
(2) adversarial source-checker re-verifying every reading claim
verbatim against `marczewski_1951_almost_independent.pdf`,
`marczewski_1953_on_compact_measures.pdf`,
`marczewski_ryll_nardzewski_1953_compactness_products.pdf`. Satisfies
verify-independently via independence of *context* (s9b directive).
User retains veto/ratification. Orchestrator ran its own derivation of
2BR, monotonicity, cluster normal form, P⁼ (both directions),
Φ-density, in-block 4(i), and the ω₁ class before spawning (same
conclusions), and independently re-ran all reviewer scripts (exit 0).

## VERDICT: SOUND

No wrong step anywhere; no real gap threatening a stated conclusion;
no claim refuted. Three findings above cosmetic — all wording/scope,
all fixed in place (✎s16): the compact-transport criterion and the
banked intrinsic-wall statement said "refines the value-1 filter"
where the mathematics requires Marczewski *approximation*; the
5(iii)/(iv) attribution conflated two theorems; a credit misplacement
in M–RN §4. 424,509/424,509 from-scratch machine checks pass.

## Math re-derivation (reviewer 1, stage 1 — statements only)

| Claim | Verdict | Notes |
|---|---|---|
| C1 (2BR) | SOUND | Route identical; ⊥-closure of the pattern is essential and stated; ∩∅ = Ω handles V inside one block. Only A2 + in-block ultrafilter fact used. |
| C1′ (OMP, \|V\| ≤ 2) | SOUND | Genuinely lattice-free; machine-confirmed on a non-lattice σ-class (even-cardinality sets on 6 points). |
| C2 (monotonicity) | SOUND — hypothesis superfluous | Holds on EVERY concrete σ-class in two lines (μ(E)=1, μ(A)=0 ⟹ μ(E⊍Aᶜ)=2); OM machinery unnecessary. Strengthening banked ✎s16. |
| C3 (cluster normal form) | SOUND | (i) via A1a/A2/L0/ultrafilter; ∩-preservation under grouping and merges verified; (ii) needs only C2 + ⊥-closure; (iii) ⟹ uses "a cluster is itself a pattern" (elision E6). |
| C4 (atomicity) | SOUND | Cells-in-block, partition, saturated-σ-field argument, cells = atoms all re-derived. |
| C5 (P⁼) | SOUND | Cycle (σ ⟹ kernel ≠ ∅ ⟹ charges atom ⟹ σ); the kernel⟹atom bridge is the one nontrivial step (E4); (⟸) leg needs NO countable generation. |
| C6 (kernel-FIP ≩ coherence) | SOUND | Witness confirmed on the unique reduced rep; 5 witnessing kernel-triples found; kernels = charged atoms verified. |
| C7 (representation-dependence) | SOUND | Canonical rep: exactly 11 states, each Dirac-at-itself, empty-kernel configs exhaustively impossible; reduced rep: 10 empty-kernel-pattern witnesses, non-Dirac rescue confirmed pointwise. (iv) sound as "into"; injectivity would need point-separation (O1). |
| C8 (Φ-density) | SOUND | Closedness + Tychonoff (BPI-strength, unflagged — fine in ZFC); pattern↦trace map onto but not injective (K1); density ⟺ Φ exact. |
| C9 (compact transport) | SOUND | The value-1 INNER witness D ⊆ K is load-bearing — see O2. "One class for all blocks" is a harmless strengthening of the hypothesis. |
| C10 (ω₁ scoping) | SOUND | ∅ must be adjoined for the approximation of null sets (source-check deviation 1, fixed ✎s16); reviewer strengthened the topological-leg failure from all-Polish to all-Hausdorff (arbitrary-FIP argument); note ω₁ is Polish-topologizable at all only under CH. |
| C11 (no cheap union) | SOUND | Two-class witness on ℕ: 𝒦₁ = {{0}∪[n,∞)}, 𝒦₂ = {{1}∪[n,∞)}. |
| C12 (T4 ladder) | SOUND | Necessity via C3(ii) + P⁼; finite case machine-verified (471 clusters × 5 blocks, both reps); Zorn frame sound as stated but see O3. |

No misuse of A1/L0/A2/T3 anywhere. Flagged dependencies: ⊥-closure of
patterns (C1/C1′/C3/C7ii), Zorn for blocks (A1), BPI/Tychonoff
(C8/C12iii), ACω (C10).

## Stage 2 (line-check of §11's actual proofs) — findings, ranked

**Wrong steps: none.**

**Overstatements (all fixed in place, ✎s16):**

- **O2 (the consequential one).** §11e's compact-transport criterion
  and the banked intrinsic-wall statement said "refin(es/ing) the
  value-1 filter(s)". Read literally this is FALSE: the class of all
  singletons of Ω is countably compact and refines every ultrafilter,
  which would make every two-valued f.a. state σ-additive
  (contradiction: any nonprincipal ultrafilter state on P(ℕ)). The
  truth needs Marczewski *approximation* — the value-1 inner sandwich
  D ∈ Bl, μ(D) = 1, D ⊆ K ⊆ A — which is exactly what powers the FIP
  step in the same subsection. Since the wall statement is exported as
  the coarse factor's conjecture target and the two readings are
  INEQUIVALENT as targets, fixed at all three sites (§10e engine
  shape, §11e criterion, §11e wall statement) + taxonomy + planning
  docs + memory hook.
- **O3.** §11f's "everything reduces to the successor step" vs the
  crux box's "finitely many pointed blocks": the Zorn run's maximal
  element can have infinite support, and pointing a further block is
  an infinite union of closed conditions (blocks may have infinitely
  many atoms), so finite-𝒮 crux + compactness alone does not close the
  limit stage — the note's own parenthetical concedes this. Scope
  annotation added at the slogan; T4 (the 𝒮 = ∅ instance) unaffected.
- **O1.** §11c "Ω ↪ St_σ(L)": hook arrow claims injectivity, false for
  non-separating σ-classes (L = {∅, Ω}, |Ω| ≥ 2). Fixed to → with
  separation caveat.

**Elisions (one-liners, all verified fillable; recorded, not edited
except where noted):** E1 ∩∅ = Ω convention in 2BR when V sits in one
block; E2 monotonicity's silent steps (A∧Eᶜ = A∩Eᶜ; orthogonal join =
literal ⊍) — superseded by the banked two-line general proof ✎s16;
E3 §11c states "partition Ω" but not "every member is a union of
cells / cells = atoms" (needed for "equivalently: charges an atom");
E4 P⁼'s kernel-nonempty ⟹ charges-atom bridge asserted as
"equivalently", never derived (two lines: ω ∈ D_Bl, ν(A(ω)) = 0 would
force ω ∈ A(ω)ᶜ); E5 §11e 4(i) treats only the μ(E)=1/μ(Eₙ)≡0 failure
mode — that it is the ONLY mode is elided; E6 Φ ⟺ cluster form's
"a cluster is itself a pattern" direction elided.

**Cosmetic:** K1 §11d "correspond exactly" — pattern↦trace onto, not
injective (forced values); K2 Tychonoff/BPI unflagged; K3 "purely
finitary" for T4 — σ-free yes, objects not finite; K4 the reduced rep
is the UNIQUE valid one among all 2046 proper subsets (sharpening
applied ✎s16); K5 §11a's product-Ulam reference and §11e's source
summaries were outside reviewer 1's scope (covered by reviewer 2).

## Source re-check (reviewer 2 — verbatim, all three PDFs)

All eight attributions CONFIRMED in substance; the ω₁ reading (A) and
the union-closure reading (B) both SURVIVE Marczewski's actual
definitions — his §2 compact classes are purely set-theoretic ("By
eliminating non-essential topological concepts from this proof, I
arrived at the notion of compact measure", p. 113), and closure under
countable intersections/finite unions is PROVED (2(i)–(iii)), not
required, while union-of-classes is exactly what 5(i)'s hypotheses
buy — so "union of per-block compact classes need not be compact" is
structurally presupposed by his §5. Verbatim anchors on record:
compact class §2 p. 115 (sequence form ⟺ countable-FIP form); approximation
§3 p. 116 (η-form, ALL E ∈ M — deviation 1 below); compact measure §4
p. 118; 4(i) p. 118 "Every compact measure is countably additive";
5(iii)/5(iv) p. 120 verbatim (deviation 2); "countably
pseudo-independent" is the paper's term (§5 p. 119); M–RN §1(i)
p. 166, §1(ii) p. 167 with (6) m_e(Z) = m_e(Z′) = 1 verbatim
("Bernstein-type" is our gloss, accurate); §3(ii) p. 170 "A purely
atomic σ-measure μ is compact"; §4 p. 170 (deviation 3). Meta-claims
confirmed: machinery lives entirely in M 1953 (Fund. Math. 40,
113–124); M–RN = 6 printed pages (165–170), explicitly the follow-up
("quoted below as C"); M 1951 contains NO compact classes (almost
independent fields, multiplicative extensions, Thm I) — nothing in
§11e belongs to it. Dating nuance on record: M 1953's footnote [11]
cites a one-page 1951 Coll. Math. announcement of the same notion.

**Deviations requiring an edit (all applied ✎s16):**

1. Approximation definition rescoped (η-form over all E ∈ M; null sets
   included ⟹ ∅ must be in the witness class; two-valued
   specialization stated as such). Consequence for the ω₁ bank: co-countable
   filter + {∅}; corroboration added via M–RN §3(ii) (the state is
   purely atomic, ω₁ a single atom).
2. 5(iii) vs 5(iv): the clean "independent σ-fields + compact partials
   ⟹ compact" statement is 5(iv); 5(iii)'s hypotheses sit on the
   approximating classes and partial-compactness alone is explicitly
   insufficient. Both are compactness-transfer, not
   extension-existence (that is M 1951 Thm I).
3. M–RN §4 credit: positive half = M 1953 4(ii) (quoted as "C 4
   (ii)"); M–RN §4's own contribution is the converse-false example.

## Machine receipts (committed)

`notes/open_questions/verification/proof_read_2026-07-11_s15/`
(written from scratch by reviewer 1; no repo script read; orchestrator
re-ran all, exit 0):
`pentagon_core.py` (shared module — pentagon from the block recipe, 11
states, rep machinery: order-iso, σ-class + OM law, blocks via
Bron–Kerbosch, exhaustive f.a.-state enumeration),
`check_canonical_c7i.py` (2,233 — canonical rep is a 22-element
concrete σ-class OML; C7(i)/(iv); empty-kernel configs exhaustively
impossible), `check_reduced_c6_c7ii.py` (1,671 — all 2046 proper
subsets tried, UNIQUE valid reduced rep = drop the all-odd state; 5 C6
witnesses + 10 C7(ii) witnesses), `check_c1_c2_c3_c5_pentagon.py`
(415,653 — C1/C1′/C2/C3/C5 + C12(ii)/T4 on both reps, all states, all
value-1 subfamilies; 471 clusters × 5 blocks),
`check_c1prime_c2_small.py` (4,152 — all 26 concrete σ-classes on
|Ω| ≤ 4 + a targeted non-lattice σ-class), `check_c11_truncation.py`
(800 — C11 witness bookkeeping, finite shadow). Total **424,509
checks, 0 failures**.

**Honest coverage gaps (hand-proof-only, not scriptable):** everything
involving genuinely infinite countably generated σ-fields (C4, C5's
T3 route, C9, C12(i)); all topology in C8 (closedness,
Tychonoff/BPI, density ⟺ Φ); everything on ω₁ (C10, including the
all-Hausdorff strengthening); C11's empty TOTAL intersection (script
checks the finite shadow); C12(iii)'s Zorn/compactness frame; the
general-Ω halves of C1/C1′/C2/C3.
