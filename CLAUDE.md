# Claude Code Instructions for This Repository

## Who the user is

Independent mathematician/researcher. Deeply familiar with Lean 4,
Mathlib, measure theory, ergodic theory, Stone duality, delay
embeddings, OML theory. Philosophy undergrad + three years math
undergrad. Working outside academia. No advisor — uses LLM to
partially fill that gap.

## Current state of the programme

**No active standalone leads as of 2026-05-18.**
Dynamics/reconstruction remains a source of examples and
contrasts, but not a current research direction.

Papers I and II are synthesis/positioning. Paper II (EA/PR/VDR,
van Fraassen-to-duality) is the strongest novelty zone.
Publication is not a goal of this repo — the work is
research-oriented. Papers may be shared eventually but the
driver is understanding, not shipping.

See `notes/covered_leads/` and `notes/knowledge_map/` for full state.
No active standalone leads as of 2026-05-18.

## The research workflow (FOLLOW THIS)

### The 8-phase pipeline:

1. **Seed note** (md, 30 min) → `notes/unsorted/`
   Declare claimed contribution type(s) and per-type bars.
   Format: `**Claimed type(s):** Type N (name). **Bar:** [what
   this seed must demonstrate to clear that type's bar].`
   Pre-existing seeds without declarations are grandfathered;
   declarations are added when next audited.
2. **Skeptical audit** → GATE: evaluate against each claimed type's bar.
   Default: `/audit full` for Phase 2. Use `pure`/`applied` for
   targeted re-audits only.
3. **Problem statement** (md) → `notes/active_leads/`
4. **Mathematical work** (user does this, not LLM)
5. **Formalization** (Lean, novel results ONLY)
6. **Draft** (LaTeX, editorial principles)
7. **Second audit** (before declaring complete)
8. **Complete or park**

### Contribution types (see `notes/programme/contribution_evaluation.md`):

Seeds are evaluated against 7 types, each with its own bar:
1. New theorem — is it known?
2. New proof — new technique, unexpected connection, or major simplification?
3. Unifying framework — does it enable method transfer (not just analogy)?
4. Vocabulary — three-statements test (3 new statements + 1 non-trivial result)
5. Impossibility — closes off an active direction or sharpens non-trivially?
6. Exposition/translation — named audience, inaccessible literature, non-trivial work?
7. Methodology — demonstrated advantage, sharp regimes, reproducible?

Broader lens, not broader standard. Each type has a concrete bar.

### Key rules:

- **Audit before you draft.** Never draft LaTeX for unaudited claims.
- **Declare types before you audit.** Seeds must commit to claimed
  contribution types; the audit evaluates each type's bar.
- **Don't formalize known results.** Use `axiom` with citation.
- **Name things last.** Don't name until you've checked the literature.
- **Park honestly.** If no type's bar is cleared, stop. Don't rescue
  with framing or by switching to a more permissive type.
- **Verify LLM proofs independently.** Lean or manual check only.

## Custom agents (`.claude/agents/`)

## Skill: `/audit` (`.claude/skills/audit/`)

Research audit with mode argument. Gates the pipeline at Phase 2
and Phase 7. Evaluates theorem novelty, applied utility, and/or
contribution type bars.

| Invocation | What it does |
|------------|-------------|
| `/audit pure [target]` | Skeptical novelty audit (hostile referee) |
| `/audit applied [target]` | Applied utility assessment (practitioner test) |
| `/audit both [target]` | Pure + applied, cross-referenced |
| `/audit full [target]` | All contribution types evaluated against per-type bars |

The skill runs in a forked context (opus, with web search) so
audit results don't flood the main conversation.

## Custom agents (`.claude/agents/`)

Six specialized agents for non-audit advisory and review:

| Agent | Role | When |
|-------|------|------|
| `literature-scout` | "Find everything under every name." | Phase 2, ad hoc |
| `devils-advocate` | "Argue against this before I commit." | Phase 2/4 gates |
| `thesis-advisor` | "Persist or pivot? Right problem?" | Any checkpoint |
| `editorial-pass` | "Apply the 16 editorial rules." | Phase 6 |
| `lean-reviewer` | "Debug Lean, find Mathlib APIs." | Phase 5 |
| `repo-hygiene` | "Orphans, stale refs, structural issues." | Periodic / after reorg |

Each agent has its own system prompt with detailed instructions.

Run `repo-hygiene` periodically (after major reorganizations,
before commits that touch many files, or when the repo feels
cluttered) to catch orphaned files, stale cross-references,
and structural drift.

## Communication preferences

- Direct, concise. No preamble, no trailing summaries.
- Stop and reassess at natural checkpoints.
- Honest sorry tracking: precise proof sketches, not "TODO."
- One conceptual layer at a time.
- Never push to remote without explicit request.
- Use Edit for existing files, Write only for new files.

## Tool stacking discipline

- **LLM:** literature search, drafting, editorial, Lean debugging
- **Lean:** ground truth for correctness
- **Human:** mathematical architecture, proof strategy, judgment
- Never skip the Lean step for novel results
- Never trust an LLM proof without independent verification

## Lean as verification

Zero-sorry Lean proofs are the ground truth for novel results.
Prioritize closing sorrys on **novel** results. Classical
infrastructure sorrys can remain honestly documented.

## Repository structure

```
.claude/
  agents/             ← 6 custom agents + 1 skill (/audit)
  skills/             ← /audit (pure, applied, or both)

papers/
  paper_i/            ← Synthesis (expository, not novel)
  paper_ii/           ← EA/PR/VDR vocabulary (strongest contribution)
  archive/            ← Withdrawn/canned/dead papers

formalization/
  QuerySystem/        ← Lean 4 / Mathlib (1 sorry total)

notes/
  open_questions/     ← Precise, open, dormant (re-audit on new input)
  covered_leads/      ← Known results + dead leads (reference)
  unsorted/           ← Needs individual assessment
  knowledge_map/      ← Research control panel
  reading_directions/ ← Guided reading with questions
  literature_review/  ← LaTeX lit review + PDF library
  programme/          ← Orientation, synthesis, reception
  archive/            ← Dead ends and superseded
```
