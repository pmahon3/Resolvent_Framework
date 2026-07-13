# Relay CLI

Commands: `doctor`, `status`, `candidate-start`, `candidate-run`, `candidate-report`, `candidate-next`, `validate`, `review`, `candidate-correct`, `candidate-accept`, `candidate-abandon`, and `archive-run`.

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
