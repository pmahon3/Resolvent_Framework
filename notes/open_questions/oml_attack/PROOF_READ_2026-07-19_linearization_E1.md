# Fresh-context adversarial proof-read: linearization/extension-screen seed §§1–2 (E1)

**Date:** 2026-07-19 (E-thread unit 1). **Clears:** E1 of
`notes/unsorted/linearization_extension_screen_seed.md` §7. **Target:**
seed §1 (the FIP ⟺ extendable ⟺ point-limit lemma, BPI-only claim,
pairwise remark) and §2 (reduction chain, C11-Lemma-C2 identification,
layer separation, rep-relativity caveat). **Method (s12 standard):** one
fresh-context adversarial reviewer (Opus 4.8, high — per seed §7:
independence over horsepower), NOT exposed to the thread — stage 1:
claims re-derived from self-contained STATEMENTS ONLY (definitions +
assumable banked facts F1 δ_ω σ-additive, F2 St_fa closed/compact
[s18 Lean], F3 blocks ∩-closed [A2], F4 in-block ultrafilters/finite
kernels), instructed to refute, with from-scratch machine checks (no
repo script read or reused); stage 2: line-check of the seed's actual
§1–§2 text; stage 3: read-only verification of the C11 Lemma C2 record
(memory `oml_lattice_attack_thread.md`, "Settled facts — C11" block) and
the s15 record (`oml_lattice_regularity_attack.md` §11c +
representation-dependence bank). Orchestrator ran its own derivation of
all three TFAE legs, the pairwise remark, and both chain inclusions
before spawning (same conclusions). User retains veto/ratification.

## VERDICT: SOUND-WITH-FINDINGS — no wrong step; E2 authorized

The lemma is correct and the seed's proof text is valid, not just the
statements. "BPI only" is exact: (1)⟺(3) and (2)⟹(3) are ZF(C);
(3)⟹(2) uses exactly the ultrafilter lemma. Pairwise remark sound
(disjoint value-1 pair ⟹ orthogonal ⟹ additivity gives value 2).
Reduction chain sound: points ⊆ St_σ by F1 gives the first inclusion;
F2 gives the second; ¬closure(St_σ) ⟹ ¬closure(points) ⟹ ¬FIP ⟹
failure at finite stage ≥ 3. Degenerate cases all pass (∅ ∈ L forced;
value-1 family never empty; Dirac states satisfy all three legs).
Reviewer machine checks: Boolean carrier, MO2, and an 8-state witness
family on 4 points (non-point states with value-1 triangles, pairwise
meet, empty triple) — all PASS, scripts in the job tmp dir
(ephemeral; the E2a receipt is the durable machine artifact).

## Findings (ranked)

1. **REAL (conceptual overclaim, seed §2 bullet 1) — fixed in place
   ✎E1.** "Identifies C11's Lemma C2 … as exactly the boundary" is too
   strong. The recorded C2 (memory, C11 settled-facts block:
   "counterexample pattern MUST have empty literal set-intersection
   with nonzero blockwise meets") has TWO legs. The seed's necessary
   condition reproduces the *set-intersection* leg (empty finite
   literal intersection, pairwise nonzero = stage ≥ 3) but says nothing
   about the *blockwise-meet* leg — lattice/blockwise meet diverges
   from set intersection exactly on non-co-blocked meet-zero pairs
   (the phantom-hub mechanism). The condition is the set-theoretic
   shadow of C2's boundary, not "exactly" C2. Verdict on the
   identification: PARTIAL MATCH, corrected wording applied to the
   seed; leverage claim survives (the shadow is still a new corpus-level
   necessary condition on the witness).
2. **Wording (seed §1 clause 2).** "(equivalently, to an ultrafilter on
   Ω)" conflates an ultrafilter of the generated field with an
   ultrafilter on P(Ω); interchangeable under a second BPI extension,
   so harmless. Noted here, no edit needed.
3. **Cosmetic (seed §1, (1⟹3)).** Telegraphic but correct.
4. **Scope note (seed §2 bullet 3 / §3 E2a).** The rep-relativity
   conditional "if that pattern extends to a full state" is ALREADY
   discharged affirmatively by the s15 record: §11c's kernel-FIP
   correction exhibits "some σ-additive state" (the dropped state on
   the unique reduced rep, non-Dirac, D3/D4-reduced machine-verified)
   with three block-kernels pairwise intersecting and empty triple
   intersection — on a finite carrier, where kernels are finite value-1
   intersections, that is value-1-family FIP failure in a full σ-state.
   Consequence: **latticehood does not force FIP** is already banked at
   finite scale, and E2a is *confirmatory* (independent re-derivation
   with the E-thread's own quantities), not decisive. E2a retains value
   as the calibration receipt for the screen's quantities (kernels,
   FIP stage, point-representability per state, both reps).

## Stage-3 record verification

- **C11 Lemma C2:** record located (sole record = memory settled-facts
  block, ⟦HAND⟧); match verdict PARTIAL as in finding 1.
- **s15:** seed's paraphrase of K(s)=∅ rep-relativity accurate;
  deciding lines quoted from §11c ("some σ-additive state has three
  block-kernels pairwise intersecting with EMPTY triple intersection
  (D3-reduced)"; "the dropped state becomes a non-Dirac σ-state …
  (D4-reduced)").

## Consequences for the thread

- E2a predictions stand as written in seed §3 (now expected-confirm on
  both reps; any deviation is an anomaly to escalate).
- E2b unaffected.
- E3 charter unaffected; no novelty claim on the lemma (unchanged).
- The C2 identification's corrected form feeds E4/E5: the screen's
  necessary condition is the set-intersection shadow; the blockwise-meet
  leg remains C2's own (⟦HAND⟧, unratified) content.
