# Rigor-guard scope — Lean-detector pass for proposed σ-essential mechanisms

> **STATUS NOTE 2026-07-06 (verification session).** Two developments bear on
> this scope. (1) The detectors it targets are built on the OLD spine's witness
> predicate, which was proved UNSATISFIABLE as encoded
> (`EncodingDefectCheck.lean`: `psi_false`; pattern typed as a global
> σ-additive state) — every theorem routed through `WitnessAt`/`IsSigmaEssential`
> is vacuous, so a guard consuming them would certify nothing. Any build of this
> scope must target the AMENDED encoding (`SigmaEssentialAmended.lean`:
> `IsSigmaEssentialL`, coherence clause included). (2) The amended Ψ has since
> been RESOLVED in ZFC and machine-checked end-to-end
> (`UlamWitnessMain.lean : psiAmended_ZFC`), so the guard's original purpose —
> screening candidate mechanisms for THAT problem — is moot; the surviving use
> case is the successor problem (the lattice form, latticehood ⟹ Φ), where a
> detector suite would first need lattice-aware definitions. Park until that
> problem is taken up.

*2026-06-30. SCOPE ONLY (not built). A narrow CI-style guard that runs any newly
proposed witness-mechanism through the existing Lean detectors BEFORE it is believed.
Its purpose is overclaim-prevention, NOT frontier-advancement. Companion to
[[sigma_essential_taxonomy]], detectors in `SigmaEssentialOpenCore.lean` /
`SigmaEssentialConjectures.lean`.*

---

## 0. What this is, and what it is explicitly NOT

**IS:** a discipline that forces every future "candidate carrier" or "candidate
principle" to produce a Lean `def` of its defining property and run it past the
kernel-checked detectors, so a proposal that secretly reduces to a known death is
caught mechanically rather than by hope.

**IS NOT:** a search for the witness, a loss function, an ML metric, or an
accelerator of the actual open problem. The decisive test (advisor, 2026-06-30):
**none of this session's three real kills (GTW §3k, measured-groupoid §3l, masa-free
§3m) would have fired any existing detector** — they died on conceptual
wall-reductions (definability-vs-existence, masa gate, pure-vs-2-valued) that required
reading primary sources. The detectors catch ONE class (build-a-rescuer-state; routes
that *already provably* reduce to `IntersectionClosed`). Identifying the load-bearing
reduction is the expensive step and stays human. So this guard automates the CHEAP
check and prevents regressions/overclaims; it does not move toward the object.

**Why no ML:** AlphaProof-style RL needs a closed goal + kernel reward + positive
examples. This problem has none — undecided target, zero positive labels (no witness
exists), and the carrier isn't expressible in Lean (`TargetA_sharp` quantifies over
carriers via opaque axioms). A learned "σ-essentiality score" is costume #13 (a fake
metric laundering the disjointification wall). ML is downstream of a closed reduction;
producing that reduction is the open math.

## 1. The detectors that already exist (the guard's whole engine)

All kernel-checked, 0-sorry, in the committed Lean:

| Detector | File:thm | Fires when |
|---|---|---|
| Disjointification | `OpenCore:costume_kills_witness` | proposal's load-bearing step ⊢ `IntersectionClosed s₀ B` (Boolean-local) ⟹ no witness |
| Contrapositive | `OpenCore:witness_not_intersection_closed` | any witness ⊢ `¬IntersectionClosed` (records non-distributivity as a theorem) |
| Polish boundary | `OpenCore:witness_not_polish` | witness ⊢ `¬PolishRepresentable d` (DW cut) |
| Polarity | `Conjectures:builds_state_implies_not_witness` | proposal exhibits ANY global state extending `s₀` ⟹ rescuer, not witness |
| Center route | `OpenCore:center_route_fails` | obstruction routed through an `IntersectionClosed` center ⟹ contradiction |
| Band evasion (triage) | `Conjectures:atomlessBlock_evades_band_death` | candidate negates BOTH band hooks (`¬Countable Ω`, `noSingletons`) ⟹ survives band death |

**Coverage honesty:** these span the disjointification axis + the polarity axis. They
do NOT cover: definability-vs-existence (§3j/§3k), masa/pure-vs-2-valued (§3l/§3m),
sub-threshold cohomology (`fact.cohomology_subthreshold`). Those remain human audits.

## 2. The surface a proposal must produce (the contract)

A proposal = a candidate carrier OR a candidate principle. To pass the guard it must
supply, in a new `def`/`structure`, ALL of:

1. **A defining property** `P : DynkinSystem Ω → Prop` (or on `(s₀, B)`), as the
   atomless-block candidate did (`AtomlessBlockCandidate`, a `structure ... : Prop`).
2. **A triage obligation** — ONE of:
   - `P d → ¬ IntersectionClosed s₀ B`  (survives the disjointification detector), OR
   - a proof `P d → IntersectionClosed s₀ B`  (AUTO-DEAD, detector fires — honest kill).
3. **A polarity obligation** — the proposal must NOT, anywhere, exhibit a
   `TwoValuedState d` extending `s₀` (that would trip `builds_state_implies_not_witness`).
   Stated as: the construction yields no `Extends s s₀ B` term.
4. **A boundary obligation** — `P d → ¬ PolishRepresentable d` (else DW kills it), and
   evidence of `¬Countable Ω` if the band hook is in play.

**Verdict computation (mechanical):**
- If (2) is dischargeable as `→ IntersectionClosed` → **DEAD (costume)**, log + done.
- If (2) is `→ ¬IntersectionClosed` AND (3) holds AND (4) holds → **SURVIVES TRIAGE**
  (necessary-not-sufficient; gap = Wall A, by `intrinsicK_gap_is_wallA`). NOT a witness.
- Else → **MALFORMED** (proposal under-specified; bounce back to proposer).

⚠ "Survives triage" means ONLY "evades the known deaths." It does NOT approach the
witness — `intrinsicK_gap_is_wallA` proves the entire remaining content is the open
`WallA`. The guard cannot and must not report progress beyond triage-survival.

## 3. The loop (if ever built — minimal, no ML)

```
LLM proposer ──► emits Lean `def P` + the 4 obligations (§2)
      │
      ▼
`lake build` the proposal file ──► kernel verdict
      │
      ├─ typechecks `P → IntersectionClosed`  ─► DEAD, append costume to taxonomy
      ├─ typechecks the survive-triage bundle ─► SURVIVES, log candidate + "gap=WallA"
      └─ fails to typecheck                    ─► MALFORMED, return errors to proposer
```

Loss signal = the kernel's hard 0/1 on the **decidable side-questions** (does it reduce
to `IntersectionClosed`? does it exhibit a state?), NEVER a soft σ-essentiality score.
The LLM's only job is generating well-typed proposals + their triage proofs; it has no
route to the witness (that's the open problem), so the loop EXHAUSTS the costume space,
it does not solve.

## 4. The genuine value (and the honest cost)

**Value:** catches the proposer's (and the human's) OWN overclaims before they enter
the record. Two this session would have been class-flagged by a forced-through-kernel
discipline: the mis-stated B–W Prop 2.3 biconditional, and the "trivialise-KS ⟹
impossibility foreclosed" leap (both were caught only by advisor review). The guard
makes "did you actually run this past the detectors?" a precondition for belief.

**Cost:** ~1 day to wire a `SigmaEssentialGuard.lean` that (a) re-exports the detector
entry points as a checklist, (b) provides a `CandidateProposal` structure bundling the
4 obligations, (c) a worked DEAD example + a worked SURVIVES example (the atomless
block) as regression tests. No new mathematics, no proposer automation in v0 — the
human/LLM fills the structure by hand and `lake build` is the guard.

**Recommendation:** build ONLY if the overclaim-prevention is judged worth the day.
It does NOT advance the frontier; the frontier needs a closed reduction or a new object,
both upstream of any tooling. Default: leave as scoped, revisit if proposal volume rises.

## 5. Pointers
- Detectors: `formalization/QuerySystem/QuerySystem/SigmaEssentialOpenCore.lean` §4,§5,§6;
  `SigmaEssentialConjectures.lean` §1b,§1c.
- Candidate template precedent: `AtomlessBlockCandidate` (Conjectures §1b).
- Why ML is downstream: this file §0; taxonomy `$meta.the_shape`.
- The gap the guard cannot cross: `open.wall_A`, `intrinsicK_gap_is_wallA`.
