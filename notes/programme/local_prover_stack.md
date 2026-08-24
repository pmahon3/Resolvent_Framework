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

## 3b. ✎2026-08-22 — measured again, on real work: 1/28

The §3 numbers (43/43/56) are retrodiction against the *QuerySystem* corpus and
stand as recorded. They should not be generalised to new development, and this
document previously invited that reading.

Measured on `staging/AndersenJessen.lean` — 28 theorem bodies blanked, goals in
their real context — the hybrid loop closes **1 of 28** at budget 25, and
**7 of 28** at budget 150 (189 minutes). All seven from the model arm;
automation closes none at either setting. All seven verified by splicing them
back and compiling. Full detail in `formalization/tools/prover/README.md`.

The seven are structural — subset, antitone, closure under an operation, one
set equality. The analytic core is untouched: `repr_unique`, the two density
lemmas, and all four `volume … = 0` results. That is a usable division of
labour, and a more honest one than any framing in §3.

Why the difference from §3 is not surprising in hindsight: §3 filtered to
reference proofs ≤ 12 lines and took the shortest 100 of an existing corpus.
That is the easy end of already-written material. A file being actively
developed does not look like that.

Consequence for this document's ranking: at a budget large enough to matter the
local stack does absorb part of the mechanical tier — roughly a quarter of it
here, at about 27 minutes of unattended tower time per lemma and near-zero
subscription tokens. It absorbs none of the tier above. Every
result in this development since 2026-08-21 — Theorem B, the extension repair,
Lemma NG's orbit map, the thick tower — was hand-written. The stack's real
contribution has been the kernel gate, not tactic generation.

## 4. Work plan

### PRIMARY — Theorem B + Lemma NG (kit gap 5.3) — **DONE 2026-08-21**

`formalization/QuerySystem/QuerySystem/TheoremB.lean`, 360 lines, builds clean,
receipts `[propext, Classical.choice, Quot.sound]` — no `sorry`, no new axiom.

| Result | Name |
|---|---|
| `Safe ρ` eventually periodic (**Theorem B**) | `isEvPeriodic_safe` |
| `Unsafe ρ` eventually periodic | `isEvPeriodic_unsafe` |
| `k`-cap: `LISC_k(L)` ⟹ `k ≤ card α` | `le_card_of_isLISC` |
| `Unsafe = ⋃_{k=2}^{n} TR_k^{(1)}` | `unsafe_eq_biUnion` |
| per-`k` eventual periodicity | `isEvPeriodic_isTR` |
| Lemma NG, assembly half | `isLISC_of_isTR_of_orbit` |

**What changed versus the note's proof.** §3(2) runs through the monoid of
Boolean matrices. In Lean the matrix is unnecessary: `Reach ρ k n` is literally
the `n`-th iterate of one step operator on `Tup α k → Tup α k → Prop`, a finite
type when `α` is, so the note's first-repeat argument is just pigeonhole on a
deterministic orbit (`exists_evPeriodic_iterate`). The bridge between that
iterate and `IsTR`'s raw walk (`reach_iff_walk`) is where the actual work went.

**Controls, same discipline as the eval.** A formalization can be vacuous the
way a harness can be broken, so three checks ran before this was believed:
the empty relation admits no positive-length tuple walk (definitions have
content); powers of two are provably NOT `IsEvPeriodic` (the predicate is not
trivially satisfiable); `Safe ⊆ {L | 0 < L}`. All pass.

**Honest note on the stack's role here.** These proofs were written directly —
the BFS-Prover arm was not invoked. The local stack's contribution to this
result was the kernel gate (`lake build`, `lake env lean`), not tactic
generation. No claim is made about model contribution to Theorem B.

**Still open in NG:** the orbit-map construction at `m = k/gcd(r,k)`, pairwise
disjointness of the `d` cycles, and the refutation half (C4dir at `L = 2`) —
all instrument-covered, none load-bearing for B.

### (original plan entry, for the record) Theorem B + Lemma NG

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

**✎2026-08-22 — corrected; do not act on the paragraph below as written.**
`oml_lattice_regularity_attack.md` §32 (2026-08-04) exhausted the named 7-loop
removable-face relay grammar through every feasible finite class — up to
88.5M ordered interface pairs, zero operative — and states the licensed
conclusion as a directive: *do not re-enter undirected finite search without a
new structural discriminator, a theorem reducing the global problem to a new
finite class, or a finite grammar not covered there.* It also shifts weight
toward a genuinely infinitary mechanism (countable σ-closure, coherent inverse
systems, an uncountable hub). I wrote the item below without having read §32.
Mace4 is not forbidden — §32 covers one named grammar — but "genuine evidence
on the most visible open edge" oversells it, and as written it points back into
the closed route. Any Mace4 work must first name the grammar §32 does not
cover.

Finite OMLs are automatically σ-complete, so finite-model search for the
regularity-transition question is well-posed. This will not prove the
conjecture, but "no witness up to size N" is evidence, and Mace4 is CPU-bound —
it belongs on Fir's CPU partitions, not GPU, and costs nothing against the
subscription.

### NOT WORTH DOING NOW

**~~`stone_observational_extension` (the one real `sorry`)~~ — DONE 2026-08-22,
and the analysis below was wrong in every particular.** It was not an
infrastructure gap. Mathlib's lack of Yosida–Hewitt was irrelevant: the
statement was FALSE under its stated hypothesis (`UpperDirected`), refuted by
Andersen–Jessen 1948, because `ce_iff_levelwise_continuity` shows collective
exhaustion is only per-level σ-additivity. Corrected to
`SequentiallyUpperDirected`, it follows from `sp1_iff` plus the already-proved
`observational_extension` in about twenty lines, with no Stone space and no
charge theory. The development is now `sorry`-free and CI enforces it.

Worth keeping as a cautionary note on this document's own method: the item was
ranked "not worth doing" on a cost estimate for porting a theorem that was
never needed, to close a goal that could not be closed because it was false.
Neither the cost nor the target survived contact. What surfaced the error was
not the prover — it was writing the dependency chain out in the blueprint until
the hypotheses could be read side by side.

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
