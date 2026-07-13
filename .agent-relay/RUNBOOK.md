# Stateless research relay runbook

## Programme and conjecture

The active relay concerns the OML regularity boundary: **does a concrete σ-complete orthomodular lattice carry a σ-essential state?** The standing conjecture is no. The accepted repository state, not a model conversation, controls the question and its scope.

Read `CLAUDE.md`, `notes/taxonomies_index.json`, `notes/programme/program_overview.md`, `notes/programme/frontier_map.md`, `notes/programme/shovel_plan.md`, and the current OML taxonomy before changing mathematical claims. Preserve the repository's seed/audit/open-question lifecycle, links, taxonomy entries, and formalization boundary.

## Epistemic ledger

Keep these categories distinct:

- theorem: a correctly scoped mathematical statement with an accepted proof;
- hand proof: independently proof-read but not machine checked;
- executable evidence: a reproducible computation over its stated domain;
- finite approximant/census: bounded evidence only, never an infinite theorem;
- Lean certificate: exactly the declaration compiled by Lean, with its assumptions.

Never overstate bounded results, silently widen quantifiers, or treat an LLM proof as verified. Stop when centre, σ-completeness, latticehood, state separation, or maximal-block classification is unresolved in a claimed construction. Preserve counterexamples and scope qualifications.

## Validation and formalization rules

- Python receipts must run from documented commands and generated JSON must parse.
- JSON certificates/taxonomies must parse and their dedicated validators must pass.
- `git diff --check` must pass.
- Run applicable repository checks discovered from changed files and the handoff.
- Run `lake build` in `formalization/QuerySystem` for Lean-relevant work.
- New substantive Lean results must contain no `sorry`, `sorryAx`, or undeclared axiom. Existing documented classical axioms require citations.
- Do not formalize known results merely to manufacture novelty.

## Stop and escalation

Require human review for a claimed proof/refutation of the main conjecture, a new counterexample, broad impossibility/classification theorem, changed conjecture, substantive Lean theorem, any axiom/sorry, failed validation, material scope correction, repeated rejection or stagnation, or the iteration limit. Do not push, rewrite accepted history, or merge automatically unless configuration and the human gate explicitly permit it.
