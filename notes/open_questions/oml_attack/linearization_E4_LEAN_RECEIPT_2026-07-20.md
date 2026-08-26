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
  `corePattern` + the coherence side (`psi_ZFC`, upstream) — **imported,
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
exit 0, downstream `psi_ZFC` unaffected.

---

## Gap-filling scan verdict (2026-07-20) — what else is Lean-cheap, and what is not

Task was "fill as many gaps as we can besides the irreducible creative
problems." After Row 1 landed, a scan of the Lean package for more
Row-1-shaped facts (small decidable facts on *already-constructed* objects)
returned **nothing else cheap**:

- **`ConcreteOMLPatterns.lean` / `ConcreteOMLBlocks.lean`** — the C4/C11-adjacent
  maximal-block / MBRC / Φ⇔dense machinery is **already Lean-certified and
  closed** (15 + 26 `#print axioms` receipt lines; `two_block_rescue`,
  `pointed_iff_sigma`, `phi_iff_dense`, `cluster_extension`, `t4At_of_phi` all
  proved). This is *why* the hostile audit found these rows sound. No gap.
- **`Omega7Counterexample.lean`** — fully certified finite Boolean-carrier
  Specker triple (`omega7_no_sigma_extension`). It is the Boolean analogue of
  the witness cores; the E4 row is exactly the contrast (same {01/02/12}
  Specker pattern, but the witness carrier is non-`InterClosed`). Closed.
- **Pentagon / 22-event (E2a)** — **zero Lean presence**; Python-census only.
  Formalizing it is a *from-scratch finite-OML build* (new object), NOT a
  missing-fact-on-existing-object — not Row-1-cheap.

**The one genuine remaining non-creative gap = OE (outsider-extremality).**
Non-vacuous (concrete `L(P(k),P(l))`, `k,l≤4`; not routed through the opaque
`IsConcrete`/`IsSigmaComplete` predicates of `SigmaEssentialOpenCore.lean`),
proved-not-open. BUT: its honest Lean deliverable is the **formalized
hand-lemma** (block floors/ceilings over five named blocks, flexible-fibre
sections as Boolean expressions in the input coefficients, arbitrary-base
bound domination — `oml_arbitrary_two_atom_inflation.md` §2). It must NOT be
`native_decide`d over the 744,810-pair exhaustion — that injects
`Lean.ofReduceBool` and destroys the clean-receipt property that is the whole
point. So OE is a **multi-hour / standalone formalization unit**, not a cheap
gap-fill. **Flagged as the scoped next Lean unit; not started this session.**

**Correctly excluded as irreducible-creative (per the task):** C11 puncture-meet
in its *valuable* universal form (quantifies over the opaque
`IsConcrete`/`IsSigmaComplete` axioms ⇒ any Lean statement of it is vacuous —
the vacuity burn; the non-vacuous form needs the hub *constructed*
at `UlamWitnessOmega1` scale with the countable-meet crux on the infinitary
line); C12 σ-state extension (infinitary); clause (ii) / σ-point-selection (the
file itself flags this open); the grand Φ.

**Net:** one row filled cleanly (the cheapest real gap); the remaining
non-creative gap (OE) is scoped and deferred as too large for this pass; the
rest are correctly the creative problems the task excluded.
