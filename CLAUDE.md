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

### The open-question lifecycle (sibling to the seed pipeline):

Open questions in `notes/open_questions/` are a *different unit* than
seeds — no claimed type, not headed for a draft, dormant until **new
input** (an adjacent question, source, or probe) triggers a re-audit.
On re-audit they exit to one of three outcomes: **promote-to-seed**
(enter Phase 1), **sharpen-in-place** (refine, stay), or **kill** (to
`covered_leads/`).

**Sharpen guardrail.** "Sharpen" is legitimate ONLY when BOTH: (a) a
standing check actually flipped OR a new hypothesis excludes the old
(now-false) instance — name the check that changed; (b) a concrete
witness keeps it live. Else it's a kill. Don't relabel a death as a
refinement.

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
- **Sharpen honestly.** Refining an open question is not a way to keep
  a dead one alive. Both guardrail conditions must hold (see lifecycle).
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

## Memory hygiene (the auto-memory at `~/.claude/.../memory/`)

The memory dir has a **hot path** (`MEMORY.md`, loaded into context
every session) and a **cold path** (topic files, loaded on demand).
Keep the hot path tiny; let the cold path hold detail. The failure
mode to prevent: appending a session log to the `MEMORY.md` index
line each session — paid on every startup, forever.

**Rules:**
- **`MEMORY.md` entry = one line: title + one-sentence current-status
  hook + pointer.** Hard target ~200 chars (the flagship active-thread
  entry may run ~400). NEVER a per-session log, NEVER a proof, NEVER a
  paragraph. If you're tempted, the content goes in the topic file.
- **Per-session detail lives ONLY in the topic file**, appended as a
  dated block. The index entry's hook gets *updated in place* to the
  new current status — it does not grow.
- **Preserve actionable specifics in the hook** (a citation gap, a
  file/line to fix, an open sub-question) — those are easy to lose and
  cheap to keep. Drop re-derivable narrative.
- **Topic-file cap ~40 KB.** Past that, `Read` truncates (~25 K tokens)
  and the file stops being usable whole. When a running log exceeds it,
  collapse the *oldest* sessions into a short "settled facts" summary
  at the top and keep recent sessions verbatim — ask first, since this
  discards reasoning-trail detail.
- **Before trimming index prose, verify the pointed-to file holds the
  detail** (it usually duplicates the index — then trimming loses
  nothing). Update the topic file's frontmatter `description` when the
  thread's status changes, so recall still matches.
- **Periodic check:** when `MEMORY.md` nears its size limit, scan for
  the longest lines (`awk '{print length": "NR}' MEMORY.md | sort -rn`)
  and collapse the offenders — they are almost always leaked session
  logs.

## Communication preferences

- Direct, concise. No preamble, no trailing summaries.
- **Concision is prioritized:** Be extremely brief. Sacrifice conversational formatting for the sake of brevity.
- **Direct Output:** Do not open responses with compliments, pleasantries, or validations of the idea.
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
  conceptual_sketches/← Informal exploratory sketches
  programme/          ← Orientation, synthesis, reception
  archive/            ← Dead ends and superseded
```
