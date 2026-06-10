# HANDOFF — programme-doc consolidation (deferred task ticket)

> **TRANSIENT FILE. DELETE THIS once the consolidation lands.** It is a task
> ticket, not a permanent doc. (Lesson from the stale `RESUME_bell_research.md`:
> finished work left in place under a live-sounding label becomes confusing
> cruft.)

## The task (one sentence)

Deduplicate the scattered programme-state narration so orienting costs 1–2 reads
instead of six — by **merging/demoting** the overlapping docs DOWN to one
authoritative state file, NOT by adding a new summary on top.

## Why (the token diagnosis, settled 2026-06-10)

Orientation is expensive because the *same* programme state is re-narrated in
~6 places. This session the identical descent result had to be edited into
`genealogy.md`, `program_overview.md`, `knowledge_map_body.tex`,
`genealogy_vision.md`, `oml_onboarding.{md,tex}`, and two memories. That
redundancy is simultaneously the token cost, the maintenance burden, and the
flip-flop surface. Dedup = lossless density (the only kind that exists for
LLM-read prose; there is no dense *encoding* win).

## The decisions (already made — do NOT re-litigate)

- **`program_overview.md` = AUTHORITATIVE** for current programme state (central
  question + paper status + live frontiers + open problems). This is the file a
  cold session reads to know "where are we now."
- **`genealogy.md` = HISTORY ONLY** (the Lakatosian eras/deaths narrative). It
  must STOP re-stating current status; trim its terminal/status lines to a
  pointer at `program_overview.md`.
- **`knowledge_map/` and `genealogy_vision.md` → POINTERS.** Demote their
  live-state paragraphs to one-line pointers at `program_overview.md`. Vision
  keeps its motivational voice but not operational status claims.
- **THE TRAP (the advisor's load-bearing warning):** do **NOT** create a new
  top-level `STATE.md` or any new summary doc layered ON TOP of the existing
  narrators. That makes a 7th doc to keep in sync and re-grows the scatter. The
  win is merge/demote DOWN, not add-on-top. (A `STATE.md` is acceptable ONLY if
  every other narrator is genuinely hard-demoted to history in the same pass —
  default to making `program_overview.md` itself the authoritative file.)

## Sequencing vs. the L_MO₂ audit (robust to either order)

- The **historical-narration dedup (the bulk of the work)** does NOT depend on
  the audit — run it anytime.
- The **live-frontier paragraph** (descent axis status) DOES depend on the
  `/audit full` concreteness outcome. If you consolidate BEFORE the audit,
  re-touch only that one paragraph once the audit settles. Don't block the whole
  consolidation on the audit, and don't ship a live-frontier para that the audit
  is about to rewrite.

## Definition of done

1. A cold session can orient on the programme by reading `program_overview.md`
   alone (+ one file per live axis, e.g. `descent_axis_residue_post_kill.md`).
2. `genealogy.md`, `knowledge_map/`, `genealogy_vision.md` no longer duplicate
   current-state claims — they narrate history / motivation / pointers only.
3. No new always-loaded or top-level summary file was added.
4. `MEMORY.md` index stays one-line-per-memory (do not re-bloat).
5. **This file is deleted**, and its MEMORY.md pointer line removed.

## Source of the diagnosis
This session's token-economy discussion; `[[feedback_token_economy]]`. The
descent entry point that already works as a single-source-of-truth model is
`notes/open_questions/descent_axis_residue_post_kill.md` — replicate that pattern
at the programme level.
