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
