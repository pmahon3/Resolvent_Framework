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
2. **Skeptical audit** → GATE: stop if known
3. **Problem statement** (md) → `notes/active_leads/`
4. **Mathematical work** (user does this, not LLM)
5. **Formalization** (Lean, novel results ONLY)
6. **Draft** (LaTeX, editorial principles)
7. **Second audit** (before declaring complete)
8. **Complete or park**

### Key rules:

- **Audit before you draft.** Never draft LaTeX for unaudited claims.
- **Don't formalize known results.** Use `axiom` with citation.
- **Name things last.** Don't name until you've checked the literature.
- **Park honestly.** If known, stop. Don't rescue with framing.
- **Verify LLM proofs independently.** Lean or manual check only.

## Custom agents (`.claude/agents/`)

## Skill: `/audit` (`.claude/skills/audit/`)

Unified research audit with mode argument. Gates the pipeline
at Phase 2 and Phase 7.

| Invocation | What it does |
|------------|-------------|
| `/audit pure [target]` | Skeptical novelty audit (hostile referee) |
| `/audit applied [target]` | Applied utility assessment (practitioner test) |
| `/audit both [target]` | Both evaluations, cross-referenced |

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
  covered_leads/      ← Known results + dead leads (reference)
  unsorted/           ← Needs individual assessment
  knowledge_map/      ← Research control panel
  reading_directions/ ← Guided reading with questions
  literature_review/  ← LaTeX lit review + PDF library
  programme/          ← Orientation, synthesis, reception
  archive/            ← Dead ends and superseded
```
