# Fresh-context adversarial proof-read: `pruning_theorem_and_B.md`

**Date:** 2026-07-10 (session 10). **Clears:** the s7 proof-read debt
(shovel plan §Execution-order item 5). **Method:** independent
fresh-context reviewer (no prior exposure to the reconstruction thread),
instructed to refute; machine receipts committed under
`papers/reconstruction/oracles/proof_read_2026-07-10/`. Satisfies
verify-independently via independence of *context*, not of species
(s9b directive). User retains veto/ratification.

## VERDICT: SOUND

No finding above cosmetic. No counterexample found under adversarial
search including non-strongly-connected and multi-component targets
beyond the shipped 15, boundary cases (L=1, k=1, k=n), and the
non-generator-rotation overcount (Lemma NG).

## Per-step results (all VERIFIED)

| Step | Result |
|---|---|
| Lemma 0 (layer clock) + LISC_k def + layer-injectivity | Re-derived independently; matches. |
| Tuple digraph T_k, rotations σ_r, TR_k^(r) | Definitions align exactly with instrument's `tuple_digraph`/`sig`. |
| Safe/Unsafe (k≥2 union) | Matches instrument's `range(2, A+1)` exactly. |
| Theorem P statement | Confirmed computationally for r=1 and general generator r, k=2..8, on adversarial non-SC/multi-component graphs vs an independently-written raw-DFS oracle — zero mismatches. |
| Step 2 (extraction ⟹) | Brute-force cross-check raw LISC vs TR^(1), exact agreement incl. L=1. |
| Step 3 (assembly ⟸, simplicity) | Walks re-assembled from actual TR^(1) witnesses on 5 targets (incl. dense full4/full5 chosen to tempt collisions); simplicity, length kL, ring-consistency verified independently of the proof's own argument. |
| Step 4 (generator conjugation r↦1) | Key identity `P(σ_1(u))[j] = σ_r(P(u))[j]` (≡ r·r̄≡1 mod k) checked for all 21 (k,r) pairs with gcd(r,k)=1, k=2..8 — 0 failures. |
| Lemma NG (orbit decomposition) | Every non-generator firing (d=gcd(r,k)>1) on C4dir/C6dir/C8dir/two-disjoint-3-cycles had LISC_k false, LISC_{k/d} true — exactly NG's decomposition. |
| Remark k=1 | Tested with a genuinely non-simple figure-8 closed D-walk; lift is simple by Lemma 0 alone. |
| Theorem B (1) k-cap | Pigeonhole + Theorem P; matches instrument cap. |
| Theorem B (2) first-repeat minimality | 200 random finite functions: first-repeat (s,p) = true-minimal (s,p), 200/200. |
| Theorem B (3) union bookkeeping | threshold=max, period=lcm valid (not claimed minimal) — 100/100 synthetic pairs; `tr_value` indexing 200/200, no off-by-one. |
| §5 verification-log claims | Instrument re-run fresh: 15/15 anchored, 0 failures, log matches output verbatim (Safe(ρ₂₀)=6ℤ, Safe(ρ₁₃)={3} S=11 P=3, NAND=even L, C4dir≡0 mod 4 + NG discriminator). |

Citations (Wielandt/Schwarz/Dulmage–Mendelsohn) not independently
verified — correctly flagged in-text as non-load-bearing bridge facts;
the brute repeat-search is what is actually certified.

## Findings (both cosmetic, no repair owed)

1. `safe_rho_instrument.py` TARGETS: **adv2 and adv3 are graph-isomorphic**
   (relabeling (0,1,3,2)) — identical certificates (S=12, P=4) are
   redundancy, not a bug; "15 targets" slightly overstates independent
   diversity (2 of 15 are isomorphic twins).
2. The k=1 remark (proof lines 140–142) is logically inert w.r.t.
   Theorem P/B as stated (Unsafe already restricts to k≥2); it is
   reader-reassurance, clearly signposted as such.

## Definition-alignment (proof vs instrument)

- Unsafe union structure: exact match (proof line 52 / Theorem B(1) ↔
  instrument lines 151–161).
- Instrument uses **r=1 only**; Theorem P Step 4 proves TR^(1) ⟺ TR^(r)
  for every generator r, so this is a correctly-flagged specialization,
  independently re-derived by the reviewer — no information lost.
- Instrument's trusted anchor (`raw_lisc_windings`) cross-checked against
  the reviewer's from-scratch reimplementation (not copied): same results
  on all adversarial targets.

## Machine receipts (committed)

`papers/reconstruction/oracles/proof_read_2026-07-10/`:
`check_step4_algebra.py` (21/21), `brute_LISC_TR.py` (6 adversarial
non-SC graphs, L=1..8, exact match), `check_lemma_NG.py`,
`check_boundary.py` (4 probes), `check_k1_remark_directly.py`,
`check_minimal_sp.py` (200/200), `check_union_and_tr_value.py`
(100/100 + 200/200), `check_step3_simplicity_not_smaller_period.py`
(5 targets). Plus unmodified re-run of `safe_rho_instrument.py`
(15/15 anchored, 0 failures).

## Companion review (same session)

The §7c ⟦HAND⟧-glue check (attack note, theorem-let chain vs MPT 1992
primary) also returned **SOUND** — recorded at
`notes/open_questions/oml_attack/oml_lattice_regularity_attack.md` §7c(iii-c), with
the seven-property MO₂ check committed as
`notes/open_questions/verification/mo2_jp_check.py`.
