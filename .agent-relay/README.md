# Stateless mathematical relay

The relay uses fresh model processes and persistent Git candidates. A candidate has one branch, `relay/candidate-<slug>`, and one linked worktree, `.agent-relay-local/worktrees/candidate-<slug>`. Correction rounds start new `codex exec --ephemeral` processes in that same worktree; no backend is resumed and no candidate commit is cherry-picked again.

Live candidate phase state is stored in ignored `.agent-relay-local/CURRENT.json`, using the `candidate` object defined by `schemas/current-state.schema.json`. State-changing commands take a repository-wide lock and use atomic, fsynced replacement for JSON state. Active executor, reviewer, and integration phases record a PID, host, start time, candidate head, and packet hash. The tracked `CURRENT.json` is the durable accepted-state default and has `candidate: null`. Git history is the complete and authoritative correction lineage. Run directories contain audit evidence and the integration journal.

## Lifecycle

Start from a clean configured accepted branch:

```bash
python3.11 .agent-relay/scripts/relay.py candidate-start --name outcome-c \
  --cherry-pick 1fdacb491a64acf54a6cad1bae73eda719be19bd
```

`candidate-start` records the accepted `HEAD`, creates the branch and worktree once, canonicalizes every supplied commit with `git rev-parse`, and cherry-picks it once.

Run, validate, and review with:

```bash
python3.11 .agent-relay/scripts/relay.py candidate-run
python3.11 .agent-relay/scripts/relay.py candidate-report --watch
python3.11 .agent-relay/scripts/relay.py validate
python3.11 .agent-relay/scripts/relay.py review
python3.11 .agent-relay/scripts/relay.py candidate-report
```

Successful run, validation, review, and correction phases print the same compact candidate report automatically. The report reads local candidate state and optional run artifacts, but takes branch tips, commit lists, changed files, diffs, and cleanliness directly from Git. It degrades gracefully while result, validation, or review artifacts are not yet available.

For deeper inspection or scripting:

```bash
python3.11 .agent-relay/scripts/relay.py candidate-report --full
python3.11 .agent-relay/scripts/relay.py candidate-report --diff
python3.11 .agent-relay/scripts/relay.py candidate-report --json
```

`--full` expands claims, uncertainties, validation command summaries, review corrections, and the next handoff without reading event streams or full logs. `--diff` is guarded by `review_diff_limit_bytes`; use `--allow-large-diff` only after the size warning. `--json` emits one JSON object and no prose. `--watch --interval 5` refreshes an active executor/reviewer phase and exits when it finishes. `candidate-next` may advance only the next mechanical validation, review, or correction-handoff phase; it never accepts or abandons a candidate.

The run command records only `git rev-parse HEAD` as the executor commit and leaves the candidate in `executed`. Validation produces `validation_passed`, `validation_failed`, or `validation_error`; ordinary `review` is available only after `validation_passed`. Use `review-failed-validation` explicitly when independent analysis of a failed check is useful. Backend/process failures are recorded separately from `needs_correction`.

The Codex reviewer receives a read-only candidate checkout plus a cryptographic manifest of every changed file. Diff truncation occurs only at file boundaries and rewrites any model verdict to `human_review`. A packet-only review backend likewise forces `human_review` because it cannot inspect the checkout.

For corrections, use `candidate-correct`. It commits the reviewer's correction handoff on the candidate branch and keeps every candidate file, commit, and the existing worktree. The next `candidate-run` uses that same worktree.

Acceptance requires a passing validation and accepting verdict, or `--override-review --reason TEXT`. It requires clean worktrees, journals the old accepted head and candidate tip, rebases, reruns validation, and prepares the claim ledger, generated compact state, handoff, and durable current state as a control commit on the candidate branch. One `git merge --ff-only` then moves the accepted branch to both the mathematical work and its control state. Journaled phases make interruption before or after that ref move deterministic to recover with `candidate-recover`.

`CLAIMS.json` is the canonical, provenance-bearing theorem ledger. `STATE.md` is generated from its currently operative claims and canonical open gate; historical versions remain in Git rather than accumulating as repeated prompt sections.

If a process dies, run `candidate-recover`. It refuses a live local lease, derives completed work from Git and artifacts, and restores the appropriate phase. If interrupted execution left a dirty worktree, `candidate-snapshot-dirty` preserves all tracked and untracked changes in an explicitly labelled quarantine commit before returning the lineage to correction.

Abandonment requires confirmation (`--yes` for noninteractive use), preserves ignored run evidence, removes the candidate worktree and branch, clears candidate state, and never changes accepted history.

The old `prepare`, `execute`, `accept`, `reject`, `cycle`, `run`, and `carry-forward` interfaces are deprecated and fail with a pointer to this lifecycle. No pending-candidate list, copied-hash array, automatic re-cherry-pick, empty correction commit, or per-correction worktree exists.
