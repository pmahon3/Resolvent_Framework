# Local prover stack — measurement and plan (2026-08-21)

Status of a zero-marginal-cost proving stack on `tower`, what it measurably
does and does not do against **this** development, and the resulting work
plan. Written after dropping to a single $20 Claude tier: the operative
constraint is now *routine subgoals are free, judgment is scarce*, so work is
ranked by its ratio of mechanical to architectural content.

Companion records: build/rot findings are in
`notes/archive/lean_flight_log.md` (2026-08-21 entry). Harness lives in
`formalization/tools/prover/`.

---

## 1. The stack

| Component | Detail |
|---|---|
| Tactic generator | `bfs-prover:7b-q4` — ByteDance BFS-Prover-V2-7B, q4_K_M, 4.7 GB |
| Placement | 100% on the RTX 3060 (5.1 GB of 12 GB), ~60 tok/s |
| Verifier | `leanprover-community/repl` @ tag `v4.29.0` — matches this project exactly |
| Project | Lean 4.29.0 + Mathlib v4.29.0, full olean cache |
| Interface | native step-level format: a tactic state terminated by `:::`, one tactic out |

The model is *not* a whole-proof generator. It proposes one tactic given one
goal state; `bfs.py` drives best-first search, the REPL applies each candidate
and returns the resulting goals. A proof is accepted only when the REPL reports
`goals == []` with no error and no `sorry`. **The kernel is the referee** — a
wrong proposal costs time, never correctness.

---

## 2. Method

Retrodiction against our own corpus: take a theorem we have already proved,
blank the proof body, and ask the stack to reconstruct it. `mkeval.py` extracts
**502 proved theorems/lemmas across 41 files** (median reference proof 9 lines,
p90 33; 370 tactic-mode, 157 term-mode).

Three controls, all of which changed the result:

1. **Ground truth must pass.** The first self-test run *failed* — the harness
   was missing submodule oleans. Had it been trusted, a broken harness would
   have read as a weak model. No eval runs until ground truth verifies.
2. **`sorry` and garbage must fail.** A kernel failure can return `goals: []`;
   without an explicit check that scores as a **false success**.
3. **The null baseline.** `exact?` is Mathlib's own library search. It closed
   **4/4** of the shortest theorems with no model involved. Any score not
   measured against this confound is meaningless.

So both arms run the **same search algorithm, same budget (10 expansions), same
cases**; the only variable is who proposes tactics — a fixed Mathlib automation
list (`exact?`, `aesop`, `simp_all`, `decide`, `omega`, `tauto`, `norm_num`,
`rfl`, `trivial`, `assumption`, `simp`, `positivity`) versus BFS-Prover.

Environments are committed per file *before* the target is stated, so the
target's own proof — and every later one — is absent from the kernel and cannot
be cited. (Without this, proof states inherit no constants from their defining
command and every tactic fails with `unknown constant`.)

---

## 3. Result (n = 100, reference proofs ≤ 12 lines)

| | |
|---|---|
| Mathlib automation | **43 / 100** |
| BFS-Prover-7B | **43 / 100** |
| Both | 30 |
| Automation only | 13 |
| BFS-Prover only | 13 |
| Neither | 44 |
| **Union** | **56 / 100** |

A dead tie on the headline, but on **26 different theorems**. They are
complementary, not redundant. On the 57 theorems automation could not close,
BFS-Prover closed **13 (22.8%)**.

**Contamination check: 0 of 43** model wins used a Mathlib search tactic; all 13
model-only wins are search-free. The delta is the model's own contribution.

Sample of proofs found that automation missed:

```
cEq_compl             simp only [CEq, Set.ext_iff] at h ⊢ ; simpa [← compl_symmDiff]
sel_compl             ext ; rcases b <;> simp [not_le, not_lt]
overlapEvents_subset  intro A hA ; obtain ⟨B, hB, hAB⟩ := hA ; exact B
sel_true              ext x ; unfold sel ; simp
```

Cost: automation 2.0 min, BFS-Prover 13.9 min for the same 100 — **7× slower for
the same headline score**. Hence the operational ordering: cheap list first,
model only on the failures (~10 min for 56/100).

### Honest limits

- This is the **easy end**: filtered to reference proofs ≤ 12 lines, shortest
  100 taken. Full-corpus p90 is 33 lines. **56% describes routine lemmas, not
  the frontier.**
- 44/100 defeated both arms — and those were still short proofs.
- Failure modes were `exhausted` (40) and `budget` (17): the model proposes 6
  candidates, all fail, dead end. More samples or larger budget recovers some.
- Nothing here approaches `stone_observational_extension`.

**Conclusion.** The stack reliably absorbs the mechanical tier at zero marginal
cost, with kernel-guaranteed correctness. It does not do research.

---

## 4. Work plan

### PRIMARY — Theorem B + Lemma NG (ratification kit gap 5.3)

Shovel-plan item 1 was "pruning lemma, phase-parametrized **+ theorem-let B**".
Per `99ba415` (s18), Theorem P Steps 2–4 are formalized at general `k`,
axiom-free, receipts `[propext, Quot.sound]` — and that commit's own honest list
records **Lemma NG + Theorem B (5.3) as NOT formalized**. B is the open half.

Structure (`papers/reconstruction/notes/pruning_theorem_and_B.md` §3):

1. `Unsafe(ρ) = ⋃_{k=2}^{n} TR_k^{(1)}` — **already proved** (Theorem P)
2. each `TR_k^{(1)}` recognized by iteration in the finite monoid of Boolean
   matrices, hence eventually periodic (pigeonhole)
3. finite unions and complements of eventually periodic sets are eventually
   periodic
4. Lemma NG: orbit decomposition of `j ↦ j + r` on `ℤ_k` when `gcd(r,k) = d > 1`

**Mathlib blocker: none.** Pigeonhole is available
(`Finite.exists_ne_map_eq_of_infinite`, `isOfFinOrder_of_finite`).
`IsEventuallyPeriodic` is absent but is a definition to write, not missing
mathematics. Everything is finite and combinatorial, the proof is already
written out in prose, and step 1 is banked.

Why this one under the new tier: highest ratio of routine subgoals to
architecture decisions in the repo. The routine half is what the local stack
closes free. Payoff is the stated one — Safe(ρ) provably eventually periodic and
effectively computable, the instrument an outsider runs on their own examples.

### SECONDARY — CI

`lake build` covered 1 of 47 files until 2026-08-21 (`ce55bb4`). The failure
mode is not hypothetical: `PredictiveState.lean` never compiled and this went
unnoticed for months behind a green build. Now that `globs` is set, a GitHub
Actions job running `lake exe cache get && lake build` plus a `sorry` ratchet is
a real gate. Zero subscription cost.

### SECONDARY — Mace4 bounded search on shovel item 2

Finite OMLs are automatically σ-complete, so finite-model search for the
regularity-transition question is well-posed. This will not prove the
conjecture, but "no witness up to size N" is genuine evidence on the most
visible open edge, and Mace4 is CPU-bound — it belongs on Fir's CPU partitions,
not GPU, and costs nothing against the subscription.

### NOT WORTH DOING NOW

**`stone_observational_extension` (the one real `sorry`).** Mathlib has
`AddContent` but no Yosida–Hewitt decomposition. Closing it does not mean
finding a proof — it means porting Yosida–Hewitt to Mathlib, a separate project.
No prover can help: there is no lemma to cite. The existing honest documentation
of it as an infrastructure gap stands.

**Shovel item 2 as a proving target.** "Difficulty is real" is the standing
assessment; it is architecture-heavy, the worst ratio under a $20 tier. Gather
evidence with Mace4 instead of spending judgment turns on it.

---

## 5. Reproduction

From `formalization/tools/prover/`, with `ollama` serving `bfs-prover:7b-q4`:

```
python mkeval.py                                            # -> evalset.json (502 cases)
python verify.py 4                                          # harness self-test; must print TRUSTWORTHY
python bfs.py --model __baseline__      --n 100 --budget 10  # Mathlib automation arm
python bfs.py --model bfs-prover:7b-q4 --n 100 --budget 10 --k 6
python compare.py                                           # matched comparison
```

`sorries.py` separates real open goals from `sorry` occurring in docstring
prose — as of 2026-08-21, **1 real, 29 prose**.

Paths in these scripts are absolute to the tower checkout and need editing
elsewhere.
