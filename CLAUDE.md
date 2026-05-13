# Claude Code Instructions for This Repository

## Who the user is

Mathematician/researcher. Deeply familiar with Lean 4, Mathlib,
measure theory, ergodic theory, Stone duality, delay embeddings.
Philosophy undergrad + three years math undergrad. Working outside
academia.

## Current state of the programme

Two active leads (see `notes/active_leads/`):
1. **Entropy characterization of reconstruction** — novel, needs
   rigorous proof
2. **Fibre mixing condition** — novel, open derivability question
   (Step B). Paper drafted at `papers/paper_fibre_mixing/`.

Everything else is either covered (known results, well-expressed)
or unsorted. See `notes/covered_leads/` and `notes/unsorted/`.

## The research workflow (FOLLOW THIS)

### Before any mathematical development:

**AUDIT FIRST.** Before drafting LaTeX, writing Lean, or exploring
a direction, run a skeptical novelty audit:
- Search for the claim under every plausible name
- Check the 3-5 most relevant textbooks
- Check the 3-5 most relevant recent papers
- Ask: "what would a hostile referee say?"

If the audit says "known": tell the user immediately. Move the
idea to `notes/covered_leads/`. Do NOT draft it.

### The 8-phase pipeline:

1. **Seed note** (md, 30 min) → `notes/unsorted/`
2. **Skeptical audit** (deep research) → GATE: stop if known
3. **Problem statement** (md) → `notes/active_leads/`
4. **Mathematical work** (user does this, not you)
5. **Formalization** (Lean, novel results ONLY)
6. **Draft** (LaTeX, editorial principles)
7. **Second audit** (before submission)
8. **Submit or park**

### Key rules:

- **Never draft LaTeX for unaudited claims.** The audit comes first.
- **Never formalize known results.** Use `axiom` or `sorry` with
  citation for classical theorems. Lean time is for novel results.
- **Name things last.** Don't name a concept until you've verified
  it's not already named in the literature.
- **Park honestly.** If the audit says "known," stop immediately.
  Don't try to rescue with framing.

## Editorial principles (when drafting)

### Subtractive pass first:
1. Strip subsection headers (sections suffice)
2. Kill connective prose that paraphrases math
3. Kill normative register ("important," "key," "deserves")
4. Kill ceremony ("Contributions" lists, "We now show that")
5. Scope-hedge universal claims
6. Neutralize spatial/ontological bias
7. Proofs: cite and move on

### Constructive pass second:
8. Section openings bridge from previous result
9. "This X, but Y" pivots (argumentative, not navigational)
10. Terse load-bearing sentences
11. Displayed math as narrative anchors
12. Running examples revisited
13. Names at first use inside formal definitions
14. Closing reframes, doesn't summarize

### Section minimization:
15. Merge until breaks are earned
16. Don't add transitions to clean breaks

### Process:
- Subtractive first (rules 1-7): cut length
- Constructive second (rules 8-14): add structure
- Section minimization last (rules 15-16): merge
- Deletions > additions

## Communication preferences

- Direct, concise responses. No preamble, no trailing summaries.
- Stop and reassess at natural checkpoints.
- Honest sorry tracking: precise proof sketches, not "TODO."
- One conceptual layer at a time.
- Never push to remote without explicit request.
- Use Edit for existing files, Write only for new files.

## What the LLM is good for here

- Literature search and skeptical audits (Phase 2, 7)
- Problem statement precision (Phase 3)
- Lean debugging and Mathlib API lookup (Phase 5)
- Editorial passes (Phase 6)
- Organizing notes and tracking state

## What the LLM is NOT good for here

- Mathematical proof (Phase 4) — this is the user's work
- Generating "novel" directions (often rediscovery)
- Assessing its own novelty claims (needs external audit)
- Replacing domain expertise with plausible-sounding synthesis
- **Any mathematical claim produced by the LLM must be verified
  by Lean or manual proof before acceptance.** LLMs hallucinate
  freely in mathematics (Buzzard: "LLMs will lie to you").

## Tool stacking discipline (from Tao's workflow)

- **LLM:** literature search, drafting, editorial, code
- **Lean:** ground truth for correctness
- **Human:** mathematical architecture, proof strategy, judgment
- Never skip the Lean step for novel results
- Never trust an LLM proof without independent verification

## Lean as credential (for independent researcher)

Zero-sorry Lean proofs substitute for institutional credibility.
A paper with machine-checked proofs is harder to dismiss than
one relying solely on peer review trust. Prioritize closing
sorrys on novel results.

Consider adopting **leanblueprint** (Massot) to connect LaTeX
to Lean with dependency tracking and public progress visibility.

## arXiv for priority

Post to arXiv to establish priority and visibility before
journal submission. Independent researchers benefit from the
public record.

## Repository structure

```
papers/
  paper_i/          ← Synthesis (ready but not novel as research)
  paper_ii/         ← EA/PR/VDR vocabulary (incremental)
  paper_fibre_mixing/ ← ACTIVE: novel bridge theorem + open problem
  archive/          ← Withdrawn papers

formalization/
  QuerySystem/      ← Lean 4 / Mathlib (1 sorry total)

notes/
  active_leads/     ← 2 items: entropy characterization, fibre mixing
  covered_leads/    ← Known results, well-expressed (reference only)
  unsorted/         ← Tier 3 pile (needs individual assessment)
  archive/          ← Dead ends
  future/           ← Fibre mixing source material
```
