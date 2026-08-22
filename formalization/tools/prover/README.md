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
