# Stateless research relay

This directory implements a fresh-session executor/reviewer relay. Git commits are the authoritative mathematical history; `STATE.md` is the compact theorem ledger, `CURRENT.json` is the state pointer, `HANDOFF.md` is the sole current assignment, and `LEDGER.jsonl` stores one compact audit record per completed cycle. Local result, review, validation, event, usage, log, lock, and worktree files live under ignored `.agent-relay-local/`.

Every executor and reviewer is a new `codex exec --ephemeral` process. The workflow never calls `resume`. The optional API reviewer sends `store=False` and no conversation or previous-response identifier. Token savings come from packets containing only the stable runbook, compact accepted state, current handoff, current diff/result, validations, and relevant controlling-file excerpts—not accumulated chats or old rollouts.

Executors run in linked Git worktrees. Such a worktree keeps its index under the main repository's `.git/worktrees/...` area and shares the common object database, refs, and logs. The relay therefore resolves the repository's common Git directory with `git rev-parse` and passes that exact absolute directory to the executor as `--add-dir`; it never assumes that the metadata is at `<worktree>/.git`. A disposable preflight confirms that both the linked-worktree Git directory and a probe directory under the common Git directory are writable before Codex starts.

## Setup and authentication

Requires Python 3.11+, Git, and Codex CLI authentication:

```bash
codex login status
cp .agent-relay/config.example.toml .agent-relay/config.toml
python3.11 .agent-relay/scripts/relay.py doctor
python3.11 .agent-relay/scripts/relay.py init
```

The default `review_backend = "codex"` reuses Codex CLI authentication but not a session. For `review_backend = "openai"`, install `openai`, choose `reviewer_model`, and export `OPENAI_API_KEY` in the shell. Never commit the key or put it in a tracked environment file.

## First real run

Commit the initialized relay before running it, then:

```bash
cat /path/to/current-handoff.md \
  | python3.11 .agent-relay/scripts/relay.py import-handoff -

python3.11 .agent-relay/scripts/relay.py run --max-iterations 1
python3.11 .agent-relay/scripts/relay.py status
```

The run creates `relay/run-0001` from the current clean branch `HEAD`, executes and validates there, obtains an independent review, and pauses. Inspect `.agent-relay-local/runs/run-0001/`, including the proposed state change, then run exactly one of:

```bash
python3.11 .agent-relay/scripts/relay.py accept
python3.11 .agent-relay/scripts/relay.py reject
```

Automatic acceptance is disabled by default. `accept` requires clean worktrees, an existing commit, and passing validation. It fast-forwards only; it does not push. `reject` leaves the accepted branch unchanged.

Finalized runs are immutable. A ledger row whose `human_decision` is `accept` or `reject` is authoritative even if `CURRENT.json` is stale. Repeating the same decision is a successful no-op and never adds a second row; asking for the opposite decision fails. In particular, `review` cannot be rerun after either acceptance or rejection, even with `--force`, and can never overwrite that run's authoritative review. Before finalization, `review --force` is the only way to replace an existing review.

Reviewer verdict policy is deliberately asymmetric:

- `accept`: a human may accept or reject.
- `accept_with_corrections`: reject, re-review after corrections, or accept with `--override-review --reason TEXT`.
- `reject`: reject, or accept only with `--override-review --reason TEXT`.
- `human_review`: acceptance likewise requires an explicit override and reason.

The reason and timestamp are stored in the ledger. A reviewer rejection is never silently accepted.

## Lifecycle

| Command | Required status | Result | Idempotent completion |
|---|---|---|---|
| `init` | `uninitialized` | `initialized` | `--force` is explicit |
| `prepare` | `initialized` | `prepared` | no |
| `execute` | `prepared` | `executed` or `executor_uncommitted` | no |
| `recover-commit` | `executor_uncommitted` | `executed` | no |
| `validate` | `executed` | `validated` | reports the existing result in `validated`/`awaiting_human` |
| `review` | `validated` | `awaiting_human` | reports the existing review in `awaiting_human`; `--force` permits pre-finalization replacement |
| `accept` | `awaiting_human` | `initialized` | same finalized decision is a no-op |
| `reject` | `awaiting_human` | `initialized` | same finalized decision is a no-op |
| `import-handoff` | `initialized`, no unfinalized run | unchanged | replaces the handoff explicitly |

Every active-run phase also checks the ledger first. No model, validation, merge, state write, ledger append, or worktree removal occurs after ledger finalization.

## Commits and run bases

`base_commit` is the clean control-plane branch `HEAD` recorded by `prepare` and used as the executor worktree base and diff parent. `executor_commit` is the mathematical commit produced in that worktree. `final_accepted_commit` in the ledger—and `CURRENT.accepted_commit`—is that mathematical executor commit on acceptance, or null in the ledger on rejection. Branch `HEAD` is authoritative for the next worktree and normally points to a later control-plane commit; the relay does not try to store a commit's own hash inside that commit.

After integration, `accept` commits `STATE.md`, `HANDOFF.md`, `CURRENT.json`, and `LEDGER.jsonl` as `Finalize relay run RUN_ID: accept`. `reject` does not integrate the executor commit, preserves its worktree and evidence, writes the review's correction handoff, increments the rejection count once, and creates the analogous control commit. Both paths leave the main worktree clean. Acceptance banks the reviewed state patch; rejection never banks rejected mathematical claims.

The relay reports executor/review packet bytes, estimated tokens, included-file count, and largest included files. It warns above the configured `packet_warning_tokens` and refuses packets above `packet_hard_limit_tokens` unless the phase is explicitly rerun with `--allow-large-packet`.

## Recovery and operations

`status` reports the last durable phase. Resume with the next idempotent phase (`execute`, `validate`, `review`, `accept`, or `reject`) rather than resuming a model thread. Use `git worktree list` to inspect interrupted worktrees. After preserving needed commits and run records, remove an abandoned tree with `git worktree remove PATH`; never delete a worktree containing uncommitted research.

If an executor modifies files but cannot commit, the relay records `executor_uncommitted`, preserves the worktree and exact changed-file list, and stops before validation or review. Inspect the worktree, then run:

```bash
python3.11 .agent-relay/scripts/relay.py recover-commit
```

Recovery refuses any change-set drift, displays the diff summary, runs configured validations, and requires interactive confirmation (or explicit `--yes`) before staging only the recorded files and committing. It records the recovered hash once, after which `validate` and `review` may continue.

If a crash or an older relay leaves `CURRENT.status` inconsistent with a finalized ledger row, inspect without changing anything:

```bash
python3.11 .agent-relay/scripts/relay.py reconcile
```

Then repair tracked state explicitly:

```bash
python3.11 .agent-relay/scripts/relay.py reconcile --apply
```

Reconciliation preserves the ledger decision and accepted mathematical history, restores `initialized`, and never interprets a review written after finalization. If such a later `REVIEW.json` is detected, the applied repair archives it locally as `REVIEW.post-finalization.json` and reports it as non-authoritative. It does not add a ledger row. Commit the repaired control state if reconciliation is being used outside an already pending control-plane change.

Local run logs may be archived outside the repository or deleted after their compact ledger record and commits are verified. They are ignored and must never be committed. To disable automation safely, stop invoking `relay.py`; optionally rename/remove the untracked local config. No daemon or scheduled process is installed.

Security boundary: the executor may modify only its isolated worktree plus the resolved common Git directory needed for worktree metadata, objects, refs, and logs. It cannot write arbitrary directories outside those roots. The reviewer remains read-only and receives no Git write root. The relay never enables danger-full-access, never bypasses approvals or the sandbox, and never pushes a remote automatically. Review prompts for sensitive content, keep credentials only in the environment, and do not track model JSONL streams. Large diffs are bounded; omitted files are recorded for human inspection.

See `RUNBOOK.md` for mathematical rules and `RUNBOOK.md`/`CURRENT.json` for recovery state.
