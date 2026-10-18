# Claude Code Instructions for This Repository

## Who the user is

Independent mathematician/researcher. Deeply familiar with Lean 4,
Mathlib, measure theory, ergodic theory, Stone duality, delay
embeddings, OML theory. Philosophy undergrad + three years math
undergrad. Working outside academia. No advisor — uses LLM to
partially fill that gap.

## The why (read first; added 2026-10-17)

**`WHY.md` is the compass the mathematics answers to.** The question it holds: *when do local
views, each correct as far as it goes, add up to one world, and what do they say when they
don't?* Practically, what lights the fire is **ecology and anarchism**: how order arises from
local relations with no centre holding it together. The user wants the work to resurface in the
world, not to stay in an ivory tower. It is not mathematical content, but it guides every agent.

**Operational:**
- **At every checkpoint, say how the result bears on the question.** Use WHY.md's four questions:
  loop? unaskable joint question? hidden idealisation? circle, or composition?
- **Protect the user's own seeing.** The spark lives in puzzles and pictures understood by hand,
  not in machine output. Offer a puzzle before a proof dump. Don't bury the user in generated
  Lean or enumerations. Machines are the answer key.
- **Go at a human pace.** At most one new thread per checkpoint. If the user says they are lost,
  stop adding: orient in plain language, then offer a choice, including "pause".
- **Honest distance.** Name practical bridges (ecology, commons, inference, data merging) only as
  lenses and questions, with the gap to applicability stated. Never overclaim.
- **Reversals cost.** When a result overturns something recently framed as central, lead with
  that, plainly, and update every place that asserts it.

## The aim: build new mathematical theory (adopted 2026-10-16)

The programme builds **new mathematical theory**: definitions, invariants and
structure theorems. **Problems are probes placed at seams between existing
theories.** They locate where theory is missing, and solving them is a means, not
the end. This theory-first orientation replaces the earlier problem-first one.
**Proof is raw data for theory building** (user, 2026-10-16). A proof's value lies
in what it reveals about structure: which objects matter, which invariant is
working, where a theory is missing. Proofs are not the product.

The refined source the user points to is 3Blue1Brown, "There's never been a better
time to go into math" (2026-10-16). Its frame:
- The research stack is: proving theorems → choosing what is worth asking
  (conjectures, taste) → **theory building** (Descartes' coordinates, Galois'
  groups, Grothendieck's rising sea). Then come applications and *motivated*
  exposition.
- "Good mathematicians prove theorems, great ones make conjectures, the greatest
  write definitions."
- Proof was long the proxy for understanding. It is now losing that role and
  becoming raw data, "like numerical calculation" or more digits of π.

**Operational consequences:**
- Treat LLM and Lean proofs as data. Read them for the *elements of simplicity*
  that recur, and weave those into definitions and theory.
- At each step ask: **is the bottleneck one more proof, or my understanding of
  the proofs I already have?** Often the right move is to close the laptop and
  rebuild the understanding by hand.
- Use proof machines like the answer key at the back of a textbook: available,
  but do the problem yourself first.
- Credit ideas that machine output reuses. This is the prior-art discipline.
- Explanation is part of the work: a theory is not a list of definitions but a
  motivated case for why these are the right structures.
Publication is not a goal. Papers may be shared eventually.

## Current state of the programme

**Authoritative state doc: `notes/programme/program_overview.md`.** Its
2026-10-16 addendum wins over anything older. `frontier_map.md` and
`shovel_plan.md` are stale (August 2026).

**Theory in construction: pointless coherence on glued carriers.** It concerns
finitely additive two-valued states on carriers glued from window events, and
which window-graph shape lets them be pointless.
- Load `notes/open_questions/cyclic_marginal/glued_carriers_taxonomy.json` (the
  first theory-shaped collection).
- Read `notes/open_questions/cyclic_marginal/pointless_coherence.pdf`, which
  opens with the window puzzle.
- The seam: cycle × infinity.
- **Stance: answers first.** Questions and states (consistent answer patterns) are
  primitive. Points and ideal points are derived, earned or not. Only the
  possibility space Ω is assumed, as scaffold, not ontology. Keep every
  construction, puzzle and Lean definition consistent with this.

**Cycle side (former flagship, `papers/reconstruction/`).**
- The fixed-length winding criterion is prior art (Kharoof–Ipek–Okay 2024), so it
  is cited, not claimed.
- The open core is the reach lemma.
- Detail: `notes/open_questions/cyclic_marginal/cyclic_marginal_scoping.md`.

**Infinity side (σ-essential, `papers/sigma_essential/`).**
- The ZFC witness is machine-checked.
- A countable witness on every ring L ≥ 4 is Lean-checked; no owner found after
  three prior-art passes; not in the paper.
- The OML/lattice and Φ forms are open.

**Other papers.** Paper I is parked. Paper II is the survivor (Type-6).
`papers/spine/` is reference-only.

Zoom-out navigation: `notes/taxonomies_index.json` (load FIRST).

## The research workflow: theory first (FOLLOW THIS)

**The unit of work is a theory-shaped collection**, a taxonomy with objects,
theorems, conjectures, probes, examples and owned regions. See
`notes/TAXONOMY_SCHEMA.md` § Theory-shaped collections.

1. **Locate the seam.** Find where existing theories each own part of a region
   and none covers the joint.
   - Map what is owned first: hostile, cross-field prior art.
   - Record it as `owned_regions` with `owned_by`.
   - A framing that turns out to be owned is useful: it says where the seam is
     *not*.
2. **Sketch the theory.** State the objects, the candidate invariants, and the
   target structure theorem, all as conjectures in the collection.
3. **Choose probes.** Pick small, sharp cases that *discriminate* between
   conjectures. Pre-register each as a gate (outcomes → affected conjecture ids)
   before running it.
4. **Run probes.** Use oracles and computation, and hand proofs (flagged
   ⟦HAND⟧).
   - Check every puzzle or example claim against the instantiated mathematics,
     and record `scope`.
5. **Bank theory items.**
   - Theorems: Lean or ⟦hand⟧, with `uses` and `scope`.
   - Fire gates, dated, and update the conjectures.
   - Never auto-propagate a fired gate.
6. **Prior-art gate before *claiming* any item.** Run it hostile and
   cross-field, and never exclude a field as "already known".
7. **Formalize** novel items in Lean (ground truth).
8. **Write** a note once the theory has a shape: puzzle first, then mathematics.
   Papers are optional.

**Evaluation.**
- Theory items are measured against **Type 3** (method transfer) and **Type 4**
  (three new statements + one non-trivial result).
- Probes need no type.
- The full 7-type audit applies when a piece of work is written up for others.
- See `notes/programme/contribution_evaluation.md`.

### Subordinate: isolated problems (the former default pipeline)

A question not yet attached to any theory goes through the seed pipeline:
1. seed note in `notes/unsorted/` declaring its claimed contribution type(s) and
   bar;
2. `/audit full` (Phase 2 gate);
3. problem statement;
4. mathematical work;
5. Lean (novel results only);
6. draft;
7. second audit;
8. complete or park.

**Open questions** in `notes/open_questions/` stay dormant until new input, then
exit by promote / sharpen / kill.
- **Sharpen guardrail:** only when a standing check actually flipped and a
  concrete witness keeps the question live. Otherwise it is a kill.
- A seed or open question that turns out to probe a seam **moves into the
  theory's collection** as a probe or conjecture (re-parent by `id`).

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

- **Theory first.** Ask what a result says about the theory and which seam it
  probes before asking whether it is novel. Problems are probes.

- **Audit before you draft.** Never draft LaTeX for unaudited claims.
- **Declare types before you audit.** Seeds must commit to claimed
  contribution types; the audit evaluates each type's bar. (Applies to seeds and
  to write-ups for others; theory items use Types 3/4.)
- **Don't formalize known results.** Use `axiom` with citation.
- **Name things last.** Don't name until you've checked the literature.
- **Park honestly.** If no type's bar is cleared, stop. Don't rescue
  with framing or by switching to a more permissive type.
- **Sharpen honestly.** Refining an open question is not a way to keep
  a dead one alive. Both guardrail conditions must hold (see lifecycle).
- **Verify LLM proofs independently.** Lean or manual check only.
- **Search the shelf before the web.** `notes/literature_review/literature/`
  holds the PDF library, and the read-trail lives in `*_byhand_read.md`,
  `*_SOURCE_CHECK_*.md` and `czech_school_prior_art_*.md`. Grep those FIRST for
  any author or result before a web search, and before calling anything a new
  lead. On 2026-08-31 two papers were announced as unread leads that were both
  already in the library with primary-source verdicts recorded.
- **Check prior art before calling a result a contribution.** A statement can be
  correct, machine-checked, and still be a gate the programme already applies
  informally. `czech_school_prior_art_sigma_essential.md` and the bounds hub
  record which regimes are already known-excluded.

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
- **Explain puzzle first.** Lead with a concrete brain-teaser (windows, answer pattern,
  staircase, triangle), then the formal statement. Check every puzzle claim
  against the instantiated mathematics and state its scope.
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

## Compute constraints (laptop; kernel panic 2026-10-17)

The machine is a laptop with limited RAM and swap. On 2026-10-17 a memory blow-up
caused a watchdog kernel panic: `scipy.linalg.null_space` on a 46,656-row matrix
allocated about 17 GB for the full SVD, while other hunts were also running.
- **Estimate memory before running.** Dense m×n float64 takes 8mn bytes. A full SVD
  also allocates m×m. Cap any single job at about 2 GB.
- **No full SVD or `null_space` on tall matrices.** Use sparse matrices
  (`scipy.sparse`), exact rank over a prime field, or deduplicate the rows first.
- **One heavy job at a time.** No parallel hunts locally. Long or many-process
  runs go to the tower, after asking the user.
- **Grow box or threshold sizes one step at a time**, checking the time and memory
  of the previous step first. Stop at the smallest size that answers the question.
- **Lean is the exception.** A Mathlib-importing Lean compile of
  `TriangleCyclic.lean` peaks at 2.2–3.8 GB (measured 2026-10-17). That is expected: run
  one compile at a time and nothing heavy alongside it.
- **Use `ulimit -v` or a timeout** on exploratory scripts, so that runaway jobs die
  instead of freezing the machine.

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
  reconstruction/     ← ACTIVE flagship (skeleton + notes/ hubs + oracles/)
  sigma_essential/    ← Ψ witness paper (machine-checked; dissemination-ready)
  spine/              ← Corpus-level umbrella (reference-only)
  paper_i/            ← Synthesis (audited, parked)
  paper_ii/           ← EA/PR/VDR vocabulary (the survivor, Type-6)
  archive/            ← Withdrawn/canned/dead papers

formalization/
  QuerySystem/        ← Lean 4 / Mathlib

notes/
  taxonomies_index.json ← Zoom-out registry (load FIRST)
  open_questions/     ← Precise, open, dormant (re-audit on new input)
  covered_leads/      ← Known results + dead leads (reference)
  unsorted/           ← Needs individual assessment (Tier 3)
  knowledge_map/      ← Research control panel
  reading_directions/ ← Guided reading with questions
  literature_review/  ← LaTeX lit review + PDF library
  conceptual_sketches/← Informal exploratory sketches
  programme/          ← program_overview + frontier_map + shovel_plan
  archive/            ← Dead ends and superseded

archive/              ← Pre-programme material (articles, thesis,
                        superseded drafts, phase 1–3 artifacts)
```
