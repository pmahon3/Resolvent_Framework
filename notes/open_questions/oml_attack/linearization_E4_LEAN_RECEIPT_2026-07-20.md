# E4 row Lean-certified: FIP fails at stage exactly 3, on the witness (2026-07-20)

**What.** The E-thread's corpus-level necessary condition (the E4 row banked
into `CAMPAIGN_CHAIN.md`) — *a σ-essential witness state is non-extendable; its
value-1 family fails FIP at a finite stage ≥ 3* — is now machine-certified on
the **actual product-Ulam witness**, at stage exactly 3, in Lean.

**Where.** `formalization/QuerySystem/QuerySystem/UlamWitnessCore.lean` §7
(new): `coreAB_nonempty`, `coreAC_nonempty`, `coreBC_nonempty`, and the
packaged `fip_fails_at_stage_three`. Receipt line added to
`UlamWitnessReceipts.lean`.

**Statement.** For the witness cores `coreA = M×{0,1}`, `coreB = M×{0,2}`,
`coreC = M×{1,2}` (the pattern's value-1 family — `corePattern_val_core{A,B,C}`
prove `s₀` is 1 on each):

    (A∩B).Nonempty ∧ (A∩C).Nonempty ∧ (B∩C).Nonempty ∧ (A∩B∩C = ∅)

i.e. the triple intersection is empty (FIP fails — this is the pre-existing
`cores_inter_empty`, consumed by `kernel_empty`) while all three pairwise
intersections are nonempty (no 2-subfamily fails ⇒ **stage 3 is minimal**). The
pairwise-nonempty half is the genuinely new fact; the triple-empty half already
existed. Together = "fails FIP at stage *exactly* 3."

**Axiom receipt (the deliverable).**

    'SigmaEssential.Ulam.fip_fails_at_stage_three' depends on axioms:
        [propext, Quot.sound]

**No `Classical.choice`. No `Lean.ofReduceBool`. No `sorry`.** Strictly cleaner
than every other theorem in `UlamWitnessReceipts.lean` (all of which carry
`Classical.choice` from the ambient witness machinery). This confirms the
E4-verdict / E1 claim that *this* direction (non-extendability via empty
kernel + stage structure) is **choice-free** — pure finite `Fin 4` fiber
arithmetic. The BPI/ultrafilter dependency lives ONLY in the converse leg
(FIP ⟹ extendable) of the E1 TFAE lemma, which is deliberately **not**
formalized here.

**Scope — honest (what this is NOT).**
- Certifies **clause (i)** only: no *Dirac* extends (empty kernel), with its
  sharp FIP-stage structure. Full non-extendability = clause (i) ∧ clause (ii);
  **clause (ii)** (σ-point-selection / no non-Dirac extension) is the separate
  open-mathematics part — untouched, correctly excluded.
- Does **not** re-derive that a state realizing this pattern *exists*. That is
  `corePattern` + the coherence side (`psiAmended_ZFC`, upstream) — **imported,
  not re-proved** by this row. So this row certifies the *mechanism on the
  witness cores*, and the witness's existence is the surrounding ZFC theorem it
  sits inside — not a fresh existence proof.
- The *general* "σ-essential ⇒ FIP fails at a finite stage" is the hand-proved
  E1 lemma (on an infinite carrier `K=∅` does not by itself give finite-stage
  failure); this Lean row is the concrete Ψ instance, decidable precisely
  because the triple is literally empty.

**Build.** Gate-1 environment: worktree `.lake` symlinked to the main
checkout's built Mathlib (v4.29.0) after a full-disk incident (the worktree's
own 5.6 GB Mathlib build filled the disk; removed + symlinked). Whole package
rebuilds clean: `lake build QuerySystem.UlamWitnessReceipts` → 1079 jobs,
exit 0, downstream `psiAmended_ZFC` unaffected.
