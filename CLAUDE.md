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
- **Keep the WHY sidecar (adopted 2026-11-06).** When a result refines, extends or tempers WHY.md, append a dated entry to
  `WHY_SIDECAR.md` (claim; status owned/ours/lens; where it lives). Never rewrite WHY.md's body: it stays in the author's voice.
- **Protect the user's own seeing.** The spark lives in pictures and concrete cases understood,
  not in machine output. Don't bury the user in generated Lean or enumerations.
  **Do not set puzzles or exercises for the user by default** (user, 2026-11-05): work the
  example out in the conversation, plainly, and let the user step in if they want to.
- **Go at a human pace.** At most one new thread per checkpoint. If the user says they are lost,
  stop adding: orient in plain language, then offer a choice, including "pause".
- **Honest distance.** Name practical bridges (ecology, commons, inference, data merging) only as
  lenses and questions, with the gap to applicability stated. Never overclaim.
- **Vocabulary.** In prose a window is a **query** (the repo's word; neutral about any reality
  behind it), and "measurement" is the physics translation. The board is "**the questions you can
  ask**" in prose and the **carrier** in formal text. Glossary: `theory_shape.md` §3 and §3a. Avoid
  private jargon like "board" without saying what it is. A query is a *context* (a jointly answerable
  set of questions); "measurement" is only a loose translation.
- **Established terms first (crosswalk 2026-11-07).** `notes/programme/TERMINOLOGY_CROSSWALK.md` maps
  internal words to community names and owners. In new text use: *not antibalanced* (not "frustrated"),
  *cause arity / factor width* (not a centre's "reach"; `lem:reach` keeps its name), *method (batch) effect*,
  *trek-rule closure*, *closure phase*, *globally glued / amalgamable* (not "flat"), *irreducible* (not
  "centre-free" for OMLs), *tensor product of ultrafilters*. Gloss the rest at first use. Lean names stay frozen.
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
- Read `notes/open_questions/cyclic_marginal/order_without_a_centre.pdf` (the
  current note: Part I theory, Part II lived; §9 "Three kinds of twist"), and
  `definitions_draft.md` §16–22 for the latest results. The older
  `pointless_coherence.pdf` opens with the window puzzle.
- State (2026-10-21): the finite triangle is classified. It hides
  a probabilistic twist iff not compressed (sorted r₂≥4, r₃≥3). **2026-10-26 audit: this
  equivalence is OWNED (Sullivant 2006 Thm 2.4(2) + Prop 5.8, plus Farkas); surviving kernel =
  carrier contains all 0/1 span vectors at compressed sizes** (`hidden_failure/AUDIT_PHASE2.md`). The yes/no
  pointless side needs infinity (Lean).
- **2026-11-10 (reversal of the open "triangle gate"): the triangle carrier is finitary.** D₃ = D_fin: every carrier
  set is three window events ⊔ one finite-grid pattern, so the window family determines the state. Evidence: hand proof, two independent checks; **fully machine-checked** the same day (`TriangleFinitary.lean`: `mem_dfin`, `state_ext`, `normal_form`, no `sorry`; alphabet ℕ); prior art: one weak scout pass, nearest sources unread; not claimed.
  Record: `notes/open_questions/views_across_records/TRIANGLE_D3_DFIN_REVERSAL_CHECK.md`. Pointless states on the triangle still exist (Lean).
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
- The ZFC witness is machine-checked, BUT (reversal 2026-10-27, confirmed): the Lean `Psi` statement
  is a routine consequence of Binder–Navara + a 4-point fibre; only the essentially-irreducible form is
  UNCLEAR; measurable-cardinal remarks false; not dissemination-ready
  (`papers/sigma_essential/SIGMA_ESSENTIAL_REVERSAL_CHECK.md`).
- A countable witness on every ring L ≥ 4 is Lean-checked; no owner found after
  four passes (entry-level NOVEL 2026-10-27); not in the paper. **Active lead:** branch
  `countable-ring-witness`, seed `notes/open_questions/cyclic_marginal/countable_ring_witness/SEED.md`
  (Gate 1: does the cheap Binder–Navara route go countable?).
- The OML/lattice and Φ forms are open.

**Other papers.** Paper I is parked (diagnosis corrected 2026-10-27). Paper II was "the survivor" until
2026-10-27: REVERSED, now PARKED (PR_dual = Jauch–Piron representability renamed; three central claims
false; `papers/paper_ii/PAPER_II_REVERSAL_CHECK.md`).
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
- **Principled method before ad-hoc fix (adopted 2026-11-05).** For any methodological problem (inference, calibration,
  estimation, testing at a boundary, multiple testing, resampling under dependence), first search the literature,
  cross-field, for the established method and read it. Only then design. Invented fixes are a last resort, and must say
  which established method was checked and why it doesn't apply. (Origin: ad-hoc calibrations of the V_G test failed
  twice; the problem was textbook non-differentiable-functional / moment-inequality inference, Fang–Santos and Andrews–Soares.)
- **Verify reversals before propagating them (adopted 2026-10-27).** When an audit
  overturns a recorded verdict, first run an independent check (a fresh agent,
  hostile to both sides, quoting the exact statements) and write it to
  `*_REVERSAL_CHECK.md`. Only when it is CONFIRMED, update every place that asserts
  the old verdict: CLAUDE.md, the dated addendum in `program_overview.md`, the
  collection taxonomy and `taxonomies_index.json` row, a banner on the old verdict
  file, dependent docs (grep for the claims themselves, not just the label), and
  memory. Never edit the paper text itself for a reversal; list fixes in
  `KNOWN_ISSUES.md`.
  **Propagation step (adopted 2026-11-04):** the list of places to update comes from a
  fresh agent's manual inventory (file:line, MUST-UPDATE / SHOULD-NOTE / MENTION-ONLY,
  searching synonyms and the mathematics, not only labels). `tools/cascade.py impact`
  is NOT the authority: tested twice out-of-sample, it equals a label grep unless edges
  are declared (`notes/programme/decision_graph_TEST.md`). Keep
  `notes/programme/decision_graph.json` only for foundational definitions and strategic
  decisions whose dependents are implicit, and run `tools/cascade.py check` as a lint
  (justification cycles, dangling ids).
- **Library access.** The user's SFU library session works in the browser
  (Claude in Chrome): proxy hosts such as `link-springer-com.proxy.lib.sfu.ca`,
  `onlinelibrary-wiley-com.proxy.lib.sfu.ca`; AMS back issues are free. Save PDFs
  through the browser, then shelve and index them. Never enter credentials, never
  spoof a user agent, never complete a CAPTCHA (ScienceDirect shows one: ask the
  user to download).
- **Search the shelf before the web.** `notes/literature_review/literature/`
  holds the PDF library. Its tracked index is
  `notes/literature_review/literature/SHELF_INDEX.json` (citation, what it
  proves, read level, programme links, by-question map). Grep **that index and
  every `*_taxonomy.json` (`owned_regions`)** FIRST for any author or result,
  then the read-trail in `*_byhand_read.md`, `*_SOURCE_CHECK_*.md` and
  `czech_school_prior_art_*.md`. Do this before a web search, and before calling
  anything a new lead. Every PDF saved to the shelf gets an index entry in the
  same commit. On 2026-10-20 Dravecký–Šipoš Ex. 6 and the Gudder additivity
  region were "rediscovered" although both were already in the taxonomy. On 2026-08-31 two papers were announced as unread leads that were both
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
audit results don't flood the main conversation. It has
`disable-model-invocation: true`: run it as an opus Agent given the skill text.

**v2.1 (calibrated 2026-10-26/27 against community verdicts; live).** Every audit
reports two things: the **programme bar** (unchanged, deliberately strict) and a
**referee estimate** (ACCEPT-LIKELY / BORDERLINE / REJECT-LIKELY + venue class),
which counts new theorems, better proofs within a field, frameworks that yield a
new statement, and exposition that adds organisation or reach. Caps: novelty
UNCLEAR ⇒ at most BORDERLINE; ACCEPT-LIKELY on a new theorem or proof needs the
nearest prior work read beyond abstract; an uncredited owner in print ⇒
REJECT-LIKELY. A BORDERLINE produced only by a cap means "read the named source
first", not "weak". Taxonomy entries get the entry-level mode (pure + Types 3/4,
no referee estimate; NOVEL needs the nearest neighbour read past abstract).
`.claude/` is gitignored: the tracked copy of the skill is
`notes/programme/audit_benchmark/AUDIT_SKILL_tracked_copy.md` (keep them identical).
Calibration data and method: `notes/programme/audit_benchmark/` (blind sandboxes,
"as-of" submission dates, dev/test split; results in
`calibration_v2_2026-10-26/RESULTS.md`).

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

Each agent has its own system prompt with detailed instructions. If a custom
agent type is not available in a session, run a `general-purpose` agent with the
role brief (and the agent file's text) instead.

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
- **Concrete example first.** Lead with a concrete worked case (windows, answer pattern,
  staircase, triangle), then the formal statement. Work it out yourself; don't pose it as a
  puzzle for the user (2026-11-05). Check every example claim against the instantiated
  mathematics and state its scope.
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
  paper_ii/           ← EA/PR/VDR vocabulary (PARKED 2026-10-27; was the survivor)
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
