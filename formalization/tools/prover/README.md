# Local prover harness

Retrodiction evaluation of a local Lean tactic model against this development:
blank a proof we have already written, have the stack reconstruct it, and let
the Lean kernel decide whether it succeeded.

Measurement, results and the resulting work plan:
`notes/programme/local_prover_stack.md`.

## Files

| File | Role |
|---|---|
| `mkeval.py` | extracts proved theorems into `evalset.json` (records the exact proof-body span so a candidate can be spliced in) |
| `verify.py` | splices a candidate into its source file and re-elaborates with `lake env lean`; also the harness self-test |
| `bfs.py` | best-first search: model proposes tactics, the Lean REPL applies them |
| `prove.py` | whole-proof generation via an instruct model (baseline for chat models; undersells step-level provers) |
| `compare.py` | matched comparison of two result files |
| `sorries.py` | separates real open goals from `sorry` in docstring prose |
| `Modelfile.bfs` | Ollama model definition — empty template so the `:::` format is not wrapped in chat markup |

## Environment note: Smart App Control (resolved 2026-08-22)

For a few hours on 2026-08-22 the REPL arm did not run on `tower`. Windows 11
**Smart App Control**, in enforce mode, refuses to execute `repl.exe`: it is
unsigned and locally built, so it has a unique hash with no cloud reputation,
which is precisely SAC's target. Under `lake env` the failure surfaces as
`error code: 4551`, and `bfs.py` sends REPL stderr to `DEVNULL` (the fix for the
64K-pipe deadlock), so the caller sees only `repl exited` or `BrokenPipeError`.
It looks like a REPL crash and is not one.

What misled the diagnosis: `lean.exe` and `lake.exe` are unsigned too and run
without complaint, because they are widely distributed and carry reputation.
SAC discriminates on reputation, not signature alone. `lake build`,
`lake env lean`, the sorry ratchet and `checkdecls` were never affected -- CI
stayed green throughout. Only the REPL search arm was dead.

**Resolved by disabling Smart App Control on `tower`.** Note this is a one-way
door on Windows 11: SAC cannot be re-enabled without reinstalling the OS. There
is no per-app allowlist -- SAC has no exception mechanism at all -- so no
narrower fix existed. Recorded here because anyone reproducing this harness on
a fresh Windows 11 machine will hit the same wall, and because the diagnosis
(`repl.exe` run directly from PowerShell, which reports *An Application Control
policy has blocked this file*) is not obvious from the symptom.

## The bug that will silently ruin a run

`grind.py` originally sent the whole file to the REPL as ONE `cmd` and worked on
the sorries it returned. Proof states obtained that way **cannot see that
command's own constants**: every tactic naming a local definition dies with
`unknown constant`, the search empties its queue in about three seconds, and the
run reports `0/N` as if the model were useless.

It is the same defect `bfs.file_envs` exists to prevent, rediscovered by not
applying the lesson. What masked it: a file whose goals mention only Mathlib
names works perfectly (`Smoke.lean` scored 4/4 throughout), so the harness looks
healthy exactly until it is pointed at real work.

Fixed by replaying declaration by declaration, committing each to the
environment before asking for the next one's goals. Measured on the same five
goals, same model, same budget:

| harness | closed |
|---|---|
| whole-file `cmd` (broken) | 0 / 5 |
| per-declaration replay | **3 / 5** |

The three include a five-component anonymous constructor with side conditions.
All three were re-checked by splicing them into `staging/ProbeCheck.lean` and
compiling — the REPL's verdict was not taken on trust.

**Do not read 3/5 as a capability estimate.** Those five goals were written to
be probe-like. See the next section for what happens on real work.

## What it actually scores

Retrodiction against `staging/AndersenJessen.lean` — every theorem body blanked
by `blank.py`, so the goals are exactly the ones already known provable, in
their real context, at the real level of difficulty.

| budget | closed | wall | mean/goal |
|---|---|---|---|
| 25 | 1 / 28 | 37 min | 77 s |
| **150** | **7 / 28** | 189 min | 404 s |

All seven from the model arm; **automation closed nothing at either budget**.
All seven were spliced back and compiled — zero errors, 21 sorries left — so
this is the compiler's verdict, not the REPL's.

Budget is the binding constraint, as the failure profile said it would be
(25 of 28 hit the budget rather than exhausting at the low setting; 19 of 21 at
the high one). More budget will probably buy a little more.

**What it closes** — structural lemmas:

    B_subset_A      B α k ⊆ A α
    B_antitone      Antitone (B α)
    B_neg_mem       -x ∈ B α k
    A_mem_sub       x - y ∈ A α
    C_zero_eq       C α 0 = (1 + ·) '' Aeven α
    C_subset_A      C α k ⊆ A α
    tail_antitone   Antitone (tail α)

**What it does not** — everything with analytic content: `repr_unique`,
`Aeven_dense`, `C_zero_dense`, `V_unique`, `V_covers`, `M_zero_compl`,
`Afull_countable`, and all four `volume … = 0` lemmas.

That is the real division of labour, and it is worth planning around: the loop
takes the connective tissue, the arguments with content stay hand-written. It
is an overnight tool — roughly 27 minutes of unattended tower time per lemma
closed, and near-zero subscription tokens.

Read the numbers with the caveat that these are proofs already written, in a
file already decomposed into small lemmas. Whether it performs like this on
lemmas nobody has proved is not something this experiment can answer.

### On UNPROVEN goals: 5 / 9

Everything above is retrodiction — proofs that already existed. The honest test
is goals whose proofs do not. `staging/Prop14.lean` states nine lemmas toward the
trace measure on a thick set; overnight at budget 600 the loop closed **five**,
two by automation and three by the model, all confirmed by compiling.

That is a *higher* rate than the 7/28 retrodiction, which is worth explaining
rather than celebrating. The Prop14 statements are phrased in Mathlib vocabulary
— `Set` operations, `volume`, `Disjoint`. The AndersenJessen ones are phrased
over project-local definitions — `A`, `B`, `C`, `V`, `M`. The model cannot see
local definitions; it guesses names and hallucinates lemmas.

**The hit rate tracks vocabulary more than difficulty.** The clearest evidence is
`thick_X`, the most trivial goal in the file — nearly a direct application of
`AndersenJessen.X_thick`, which is in scope. It exhausted in six seconds,
because `Thick` is a local `def` and `X_thick` is a name the model has never
seen. Meanwhile `Thick.disjoint_trace`, which needs a real argument, closed.

Authoring lesson, and it is cheap to act on: state lemmas in Mathlib vocabulary
where the mathematics allows, and expect nothing on goals over your own
definitions.

### Identify results by `decl` or `index`, never by `line`

The REPL's chunk-relative positions came back off by a declaration, so a
line-based splice put three proofs into the wrong theorems and produced
compile errors that looked like bad proofs. Sorries are reported in file order,
so `results[i]` is the i-th `sorry`; each also carries `decl`, the declaration
name. Both are reliable. `line` is kept only for reading and is not.

## Prerequisites

- Ollama serving `bfs-prover:7b-q4`
  (`ollama pull zeyu-zheng/BFS-Prover-V2-7B` — 15 GB f16 — then
  `ollama create bfs-prover:7b-q4 --quantize q4_K_M -f Modelfile.bfs`, 4.7 GB)
- `leanprover-community/repl` built at tag **`v4.29.0`** — the tag must match
  `lean-toolchain` or oleans will not load
- This project built: `lake exe cache get && lake build`

## Run

```
python mkeval.py                                             # -> evalset.json
python verify.py 4                                           # must print TRUSTWORTHY
python bfs.py --model __baseline__      --n 100 --budget 10
python bfs.py --model bfs-prover:7b-q4 --n 100 --budget 10 --k 6
python compare.py
```

## Three things that will silently corrupt results

1. **Run the self-test first.** If ground truth does not verify, a broken
   harness is indistinguishable from a weak model.
2. **A kernel failure can return `goals: []`.** Check `proofStatus` or it scores
   as a success.
3. **`exact?` is proof search, not a null control.** It alone closes ~43% of
   short lemmas here. Score any model against the automation baseline, never
   against zero.

Paths are absolute to the tower checkout; edit `PROJ` / `REPL` / `SRC` for
another machine.
