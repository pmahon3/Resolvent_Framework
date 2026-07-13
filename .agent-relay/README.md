# Stateless research relay

This directory implements a fresh-session executor/reviewer relay. Git commits are the authoritative mathematical history; `STATE.md` is the compact theorem ledger, `CURRENT.json` is the state pointer, `HANDOFF.md` is the sole current assignment, and `LEDGER.jsonl` stores one compact audit record per completed cycle. Local result, review, validation, event, usage, log, lock, and worktree files live under ignored `.agent-relay-local/`.

Every executor and reviewer is a new `codex exec --ephemeral` process. The workflow never calls `resume`. The optional API reviewer sends `store=False` and no conversation or previous-response identifier. Token savings come from packets containing only the stable runbook, compact accepted state, current handoff, current diff/result, validations, and relevant controlling-file excerpts—not accumulated chats or old rollouts.

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

The run creates `relay/run-0001` from the accepted commit, executes and validates there, obtains an independent review, and pauses. Inspect `.agent-relay-local/runs/run-0001/`, including the proposed state change, then run exactly one of:

```bash
python3.11 .agent-relay/scripts/relay.py accept
python3.11 .agent-relay/scripts/relay.py reject
```

Automatic acceptance is disabled by default. `accept` requires clean worktrees, an existing commit, and passing validation. It fast-forwards only; it does not push. `reject` leaves the accepted branch unchanged.

## Recovery and operations

`status` reports the last durable phase. Resume with the next idempotent phase (`execute`, `validate`, `review`, `accept`, or `reject`) rather than resuming a model thread. Use `git worktree list` to inspect interrupted worktrees. After preserving needed commits and run records, remove an abandoned tree with `git worktree remove PATH`; never delete a worktree containing uncommitted research.

Local run logs may be archived outside the repository or deleted after their compact ledger record and commits are verified. They are ignored and must never be committed. To disable automation safely, stop invoking `relay.py`; optionally rename/remove the untracked local config. No daemon or scheduled process is installed.

Security: use least-privilege sandboxes, review prompts for sensitive content, keep credentials only in the environment, do not track model JSONL streams, and never enable danger-full-access or bypass approvals. Large diffs are bounded; omitted files are recorded for human inspection.

See `RUNBOOK.md` for mathematical rules and `RUNBOOK.md`/`CURRENT.json` for recovery state.
