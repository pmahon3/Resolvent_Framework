# Relay CLI

Commands: `doctor`, `status`, `candidate-start`, `candidate-run`, `candidate-report`, `candidate-next`, `validate`, `review`, `review-failed-validation`, `candidate-correct`, `candidate-accept`, `candidate-recover`, `candidate-snapshot-dirty`, `candidate-abandon`, and `archive-run`.

One candidate owns one branch and worktree for its full correction lineage. Model processes are always fresh and ephemeral. Run history is audit evidence, not lineage state.

Routine workflow:

```bash
relay.py candidate-run
relay.py candidate-report --watch
relay.py validate
relay.py review
relay.py candidate-report
```

Every successful candidate phase prints the compact report. Use these read-only views when more detail is needed:

```bash
relay.py candidate-report --full
relay.py candidate-report --diff
relay.py candidate-report --json
```

Git is authoritative for the accepted base, candidate tip, commit list, changed files, diff, and clean/dirty status. `--full` excludes event streams and raw build logs. `--diff` observes the configured review-size guard. `--json` prints only one machine-readable object. `candidate-next` performs at most the next mechanical phase and never accepts or abandons.

Ordinary review requires `validation_passed`. `review-failed-validation` is an explicit diagnostic path and cannot bypass the passing-validation requirement for acceptance. Reviewer diff omissions force a `human_review` verdict.

State-changing commands are locked and atomically persisted. After an interrupted executor, reviewer, or acceptance phase, run `candidate-recover`. If it reports dirty candidate work, run `candidate-snapshot-dirty` to create a labelled quarantine commit, then continue correction on the same lineage.
