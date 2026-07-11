# Fresh-context adversarial proof-read: attack note §10 (Skeleton A read)

**Date:** 2026-07-10 (session 14). **Clears:** the s13 §10 proof-read
debt (opened in the s13 handoff; the same-session s13 check —
`SKELETON_A_READ_2026-07-10_receipt.md` — was below the s12 standard).
**Target:** `oml_lattice_regularity_attack.md` §10 (theorem-lets R and
P incl. the inline P0 decomposition and the localization gloss; Maharam
reading claims M1–M3; DW reading claims D1–D3; consequence C = §10d(i)
"escapes D.6 on every Polish representation"). **Method:** two
independent fresh-context agents, neither exposed to the thread or to
any repo note — (1) adversarial math reviewer given the claim
STATEMENTS ONLY (no proofs), instructed to refute, all five claims
re-derived from scratch, then in a second stage line-checked against
§10's actual proof text; from-scratch machine receipts for every
finitely instantiable component (no repo script read or reused);
(2) adversarial source-checker re-verifying every reading claim
verbatim against `maharam_1972.pdf` and `derr_williamson_2023.pdf`.
Satisfies verify-independently via independence of *context*, not of
species (s9b directive). User retains veto/ratification.

## VERDICT: SOUND

No wrong step anywhere; no real holes. One genuine finding above
cosmetic (the scope of "exactly" in §10d(i) — fixed, ✎s14 below); all
else one-line gaps or paraphrase drift. 11,686/11,686 from-scratch
machine checks pass (re-run independently by the orchestrator, all
exit 0). Orchestrator additionally ran its own third derivation of R,
P0, P before spawning the reviewers (same conclusions).

## Math re-derivation (reviewer 1, stage 1 — statements only)

| Item | Verdict | Notes |
|---|---|---|
| R | SOUND | Independent proof identical in route (𝒦₁ filter base → FIP inside a fixed compact → sandwich). Choice-free; no σ-additivity — confirmed. **Hausdorff proved load-bearing by counterexample:** ℕ with cofinite topology, finite/cofinite field, cofinite state — everything compact, (8.1) trivial, no Dirac. |
| P0 | SOUND | Decomposition + uniqueness re-derived. **Flag:** atom-set countability uses ACω(fin) on abstract X; eliminable on Polish X (definable order) — moot in context. |
| P | SOUND | Sub-claim (closed co-countable ⊇ perfect kernel) and main argument re-derived. **"x ∈ perfect kernel" proved load-bearing by counterexample:** X = [0,1] ⊍ {isolated p}, x = p breaks it. |
| L (localization gloss) | SOUND | Formalization pinned: 𝒜_B = {A Borel : A∩B ctble or B∖A ctble}, ν_B well-defined iff B uncountable. Concrete witness needs the perfect set property for Borel sets; the (8.1)-failure itself needs only "B uncountable" via R's contrapositive (survives even Bernstein B). |
| C | SOUND | Application of R + P correct; non-principality is topology-free, so all-Polish-representations quantification is legitimate; "silent, not refuted" modality right. Reading-equivalence used silently (not-a-restricted-Dirac ⟺ empty measure-1 filter core) is true — proved + machine-checked; needed because δ-representations are non-unique on coarse fields. |

**Free strengthening (banked, not yet used in §10):** P's diffuse-mass
failure extends from all-Polish to ALL-HAUSDORFF topologies, by
reduction to R — any in-field compact K ⊆ F with μ(K) > μ(F) − c must
be co-countable, so the co-countable component ν would itself satisfy
(8.1), contradicting R (ν non-principal). So c > 0 kills (8.1) on every
Hausdorff topology, matching the R-leg's generality.

## Stage 2 (line-check of §10's actual proofs)

- **R:** correct; four one-line elisions (sup ∅ = 0 at the 𝒦₁ ≠ ∅ step;
  inclusion–exclusion behind ν(K∩K′) = 1; FIP needs the members closed
  inside one compact member; the complement step in "two-valuedness
  finishes"). ✎s14: statement rewritten to assert 𝒦₁ ≠ ∅ and D ≠ ∅ as
  conclusions (the old "(nonempty) intersection" definite description
  misparses under the ∩∅ = X convention); FIP step now names K∩K₀.
- **P:** correct; inline-P0 compression noted (ACω(fin) flag moot on
  Polish); ✎s14: localization gloss now cites the perfect set property;
  c = 1-via-R remark now says failure *somewhere*, not at the specific F.
- **§10d(i) "fails *exactly* on the locus" — the one real finding.**
  Earned only *among σ-states on coarse blocks*: there the converse is a
  theorem (purely atomic σ-states satisfy (8.1) via finite in-field
  atom-truncations, any Hausdorff topology), so fails ⟺ c > 0 ⟺
  non-principal. At general-block scope it was an overstatement: a
  compact-poor block fails (8.1) even at a Dirac restriction —
  δ_ω↾{∅, irrationals, ℚ, ℝ}, ω irrational; only in-field compact is ∅.
  ✎s14: "exactly" scoped in §10d(i); same fix propagated to the
  prior-art verdict banner (item (b) gloss) and the MEMORY hook. The
  s13 CONCLUSIONS are unaffected: the failure direction (non-principal
  ⟹ escapes D.6 on every Polish rep) is what Skeleton A's demotion and
  the Theorem-2 factoring use, and it stands.

## Source re-check (reviewer 2 — verbatim, both PDFs)

M1–M3, D1–D3 all CONFIRMED; nothing rose to misread or overstated.
Key verbatim anchors now on record: Maharam (8.1) p. 145 has
"K ∈ 𝓕_α" displayed; her Thm 6.1(iv) = gamble-positivity = her (8.2);
proof of 8.1 p. 146 uses (8.1) only for the compact/open sandwich
("applied both to Aᵢ and to its complement") and the K ⊂ G₁∪…∪Gₙ
σ-additivity step; Remark p. 146 verbatim; §8.3 = Kellerer 1964
(marginals, finitely many). DW Thm D.6 p. 48 five legs verbatim
(blockwise inner regularity a distinct leg); footnote 29 verbatim,
complete, and membership-free — **the definitional gap is confirmed in
the DW text, with no repair anywhere in Appendix D** (proof p. 49 only
says "all restrictions μᵢ are inner regular"). Four minor deviations,
none requiring an edit:

1. (M1) The Hahn–Banach engine is her **Lemma 6.1**; Thm 6.1 is the
   extendability criterion invoking it. §10a's compression is fair.
2. (M2) "Aᵢ from different blocks" is the reader's framing — her step
   is any finite intersection, including n = 1. Mechanism as claimed.
3. (M3) Her Remark says the m_α "have countably additive extensions,"
   not "are σ-additive" — equivalent for finite f.a. measures on a
   field.
4. (D3) DW's Carathéodory step is redundant against Maharam's *stated*
   8.1 (which already concludes c.a. on the generated σ-field); DW
   track her proof's internal structure instead. Not substantive.

## Machine receipts (committed)

`notes/open_questions/verification/proof_read_2026-07-10_s13/`
(written from scratch by reviewer 1; no repo script read):
`r_dirac_finite_fields.py` (2369 — all fields on |X| ≤ 4, all two-valued
f.a. states brute-forced, full R mechanics + D = ∩{measure-1 sets}),
`p0_decomposition_model.py` (585 — flag-model of ctble/co-ctble;
nullspace dimension proof of the finite content of P0),
`p_arithmetic_gap.py` (3743 — μ(K) ≤ μ(F) − c exhaustive + random, gap
strict iff c > 0), `c_nonprincipal_equiv.py` (3223 — non-principality
reading-equivalence; non-unique δ-representative exhibited; threshold
lemma), `l_field_mechanics.py` (1766 — 𝒜_B/ν_B mechanics; countable-B
provably ill-defined). All re-run by the orchestrator: exit 0.

**Honest coverage gaps (verified by hand proof only, not scriptable):**
R's FIP step for infinite 𝒦₁ + the cofinite-ℕ counterexample; P0's
atom-countability and all infinite σ-additivity steps; P's topological
content (Cantor–Bendixson, perfect-set uncountability, compact ⟹
closed); L's perfect set property; the topological conclusion of the
all-Hausdorff strengthening (its threshold arithmetic is checked).
