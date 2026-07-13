# Stateless mathematical relay

The relay uses fresh model processes and persistent Git candidates. A candidate has one branch, `relay/candidate-<slug>`, and one linked worktree, `.agent-relay-local/worktrees/candidate-<slug>`. Correction rounds start new `codex exec --ephemeral` processes in that same worktree; no backend is resumed and no candidate commit is cherry-picked again.

Live candidate phase state is stored in ignored `.agent-relay-local/CURRENT.json`, using the `candidate` object defined by `schemas/current-state.schema.json`. The tracked `CURRENT.json` is the durable accepted-state default and has `candidate: null`. Git history is the complete and authoritative correction lineage. Run directories are audit evidence only.

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
python3.11 .agent-relay/scripts/relay.py validate
python3.11 .agent-relay/scripts/relay.py review
```

The run command records only `git rev-parse HEAD` as the executor commit. Validation and review compare the current configured accepted branch `HEAD` to the candidate branch `HEAD`. Every executor and reviewer invocation is fresh.

For corrections, use `candidate-correct`. It commits the reviewer's correction handoff on the candidate branch and keeps every candidate file, commit, and the existing worktree. The next `candidate-run` uses that same worktree.

Acceptance requires a passing validation and accepting verdict, or `--override-review --reason TEXT`. It requires clean worktrees, rebases the candidate onto the current accepted branch, reruns independent validation, and integrates with `git merge --ff-only`. It then applies the state patch and next handoff, commits relay control state, removes the worktree, deletes the branch, and clears candidate state. A rebase conflict preserves both histories and prints exact continue/abort commands.

Abandonment requires confirmation (`--yes` for noninteractive use), preserves ignored run evidence, removes the candidate worktree and branch, clears candidate state, and never changes accepted history.

The old `prepare`, `execute`, `accept`, `reject`, `cycle`, `run`, and `carry-forward` interfaces are deprecated and fail with a pointer to this lifecycle. No pending-candidate list, copied-hash array, automatic re-cherry-pick, empty correction commit, or per-correction worktree exists.
