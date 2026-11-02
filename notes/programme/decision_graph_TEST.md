# Decision-graph tool: test record

reviewed: false. Protocol: `memory/decision_graph_plan.md` (user, 2026-11-02).

## 1. In-sample backtest (2026-11-02), the three 2026-10-27 reversals

Ground truth = files changed by the manual propagation commits (655dda1 Paper I; f60d256 + c430c18
Paper II; 857e5c2 + the blueprint line of a41cf31 σ-essential).

| Reversal | Manual files surfaced by `impact` | Extra files surfaced (candidate misses of manual propagation) |
|---|---|---|
| Paper I diagnosis | 3/3 | genealogy.md/.tex, genealogy_vision.md/.tex, program_overview.md:407, taxonomies_index.json:79, sigma_essential_reduction_writeup.md:26, sigma_essential_reduction_result.md:47 — the σ-essential re-audit had independently listed three of these as stale |
| Paper II verdict | 9/9 | genealogy.md:277, genealogy.tex:309, genealogy_vision.md:169/.tex:279 ("the survivor"), two_grades_of_pr.md, mb_primeness_check.md, coherence_terminology.md, verification/README.md, oml_lead_philosophical_reading.md (PR_dual / Bub–Clifton) |
| σ-essential | all relevant (others in those commits were unrelated cleanup) | CLAUDE.md:346 ("dissemination-ready" in the repo map), spine STATUS.md:56 ("ships first"), program_overview.md:752/757, several oml_attack receipts citing psi_ZFC |

In-sample change made: an ignore list (archives, `.py`, the reversal records themselves) after
the label "SURVIVOR" matched oracle code. Paper II undeclared files went 27 → 15.
Verdict (in-sample): recall 100% on relevant manual files; it also surfaces genuine misses.
The misses are NOT yet fixed (deliberately: fixing them is a separate, reviewed step).

## 2. FREEZE (this commit): out-of-sample protocol for the join-choice change

- Tool = `tools/cascade.py` at this commit. No changes until §3 is written.
- Test node `def.join_equals_union` in `decision_graph.json`, labels taken only from the brief's
  wording ("join = union", "⋁", "Lemma R", "collective exhaustion", "Admissible",
  "orthogonal famil"); no declared edges.
- Ground truth: the 23-row Q1 inventory in `docs/join_choice_as_object_scoping.md`.
  Disclosure: I read the agent's one-line summary (row count, the premise finding that the coincidence
  comes from the carrier type, not admissibility) but not the rows, before this freeze.
- Adoption rule (pre-registered): ADOPT if `impact def.join_equals_union` surfaces every inventory
  file (file-level) plus ≥1 relevant file the inventory missed; PAUSE if it misses any inventory file;
  DROP if it adds nothing beyond a plain grep of the same labels.

## 3. Out-of-sample result (2026-11-02, tool frozen at 1b708d5; no changes made after)

`impact def.join_equals_union` surfaced 56 files. The scoping inventory (Q1, 23 rows) names 12 files.

- Surfaced: 3/12 (program_overview.md, regularity_sigma_additivity_pullback.md, sigma_essential_body.tex).
- **Missed: 9/12.** Causes:
  1. Search scope: the Lean sources (`formalization/QuerySystem/QuerySystem/*.lean`: Admissibility,
     ConcreteOMLBlocks, KernelClosureCalculus, SigmaEssentialLocalization, SigmaEssentialOpenCore,
     SigmaEssentialWitness) are not in SEARCH_DIRS (only the blueprint is). 6 misses.
  2. In-sample tuning backfired: the ignore list drops `*REVERSAL_CHECK*`, which removed
     PAPER_I_REVERSAL_CHECK.md, a genuine inventory row. 1 miss.
  3. Implicit commitment: frontier_map.md and spine_body.tex commit to join = union without using
     the brief's words; no label grep can find an *implicit* commitment. 2 misses.
- Extra: ~53 files beyond the inventory, mostly broad label hits ("⋁", "Admissible"); not assessed
  for relevance.

**Pre-registered verdict: PAUSE** (misses inventory files). Not adopted as-is.

What this says: the tool is a good worklist for EXPLICIT assertions (in-sample: 100% recall, and it
found real manual misses), but it cannot find implicit commitments, which is exactly what the join-choice
question was about. The scoping read remains necessary; the tool complements it.
Fixes to consider for v1 (each needs a fresh out-of-sample test, not this one): include Lean sources;
drop reversal records only for the node they record, not globally; declared `rests_on` edges for
foundational definitions (implicit commitments must be declared, since they cannot be grepped);
rank grep hits by label specificity to cut noise.

## 4. v1 fixes + DEVELOPMENT re-run on join-choice (2026-11-02; NOT out-of-sample — misses were known)

Fixes: (1) Lean sources searched; (2) reversal records skipped only per node (`records`), not globally;
(3) foundational-definition node `def.carrier_sigma_class` (labels + `code_labels` searched in Lean only)
with declared `rests_on` from papers/spine/state docs — two of those edges (spine, frontier_map) were
written KNOWING they were misses (disclosed in `edge_provenance`); (4) specificity ranking (label
file-counts; labels hitting >25 files marked broad, listed last).

Result vs the 12 inventory files (union of `impact def.join_equals_union` and `impact def.carrier_sigma_class`):
- 11/12 covered (SigmaEssentialWitness.lean is the carrier node's own declared file).
- Remaining miss: KernelClosureCalculus.lean — it never names the carrier; it inherits it through Lean
  imports. A general v2 mechanism would be the Lean import graph (modules importing the carrier's module
  rest on it), not another label.
- Ranking: carrier run puts frontier_map, sigma_essential_body, spine_body, program_overview in the top 5
  (declared edges); the join run's label grep is still noisy (72 files; inventory items at ranks 4–72).
Reading: declared edges carry implicit commitments; label grep remains a broad worklist.

## 5. Next out-of-sample test (pre-registered; tool FROZEN at the commit that adds this section)

Case: the next real change that triggers propagation — first candidate, the dilation-question flag
(D affirmative for two-valued states on σ-orthocomplete OMPs) if its independent check CONFIRMS a change.
Protocol: the propagation is done by hand first (independent agent, file:line list) WITHOUT the tool;
then `impact` on the changed node with v1 as frozen here; same adoption rule as §2 (ADOPT if every
manual file found + ≥1 relevant missed; PAUSE if any manual file missed; DROP if no gain over grep).

## 6. Out-of-sample result for v1 (2026-11-02): the dilation-question change

Ground truth: `docs/dilation_propagation_MANUAL.md` (independent agent, tool not used; 14 MUST-UPDATE hits
in 3 files; SHOULD-NOTE in 6 files). Tool: v1 frozen at 84d46d2 (verified unchanged); node pre-registered
at 931d5f1 before the check and before the manual inventory.

| Manual file (class) | Tool |
|---|---|
| docs/site_regularity_prediction_ledger.md (MUST) | found (l.242, 277, 285, 523, 547, 549; manual also has l.8–10, 256, 544 — summary rows without the labels) |
| docs/join_choice_as_object_scoping.md (MUST) | found |
| docs/dilation_question_scoping.md (MUST) | node's own file (declared) |
| docs/regularity_sigma_additivity_pullback.md (SHOULD) | found |
| docs/state_of_play_2026-08.md (SHOULD) | found |
| notes/literature_review/literature/SHELF_INDEX.json, Navara entry (SHOULD) | **missed** (mentions Navara's 𝓛_ℕ, not the labels) |

Extras: the change record itself (CHECK doc) and the tool's own data files (self-reference noise). No
relevant file beyond the manual inventory.

**Pre-registered verdict: PAUSE** (one manual file missed; and no relevant file found beyond the manual
pass). File-level recall 5/6 (all MUST-UPDATE files found); line-level recall partial.

Reading across §1–§6: with no declared edges, the tool is exactly a label grep — useful as a quick
worklist, no gain over grep. Its added value appeared only where edges were declared (implicit
commitments, §4). Recommendation (for the user): do not adopt as a propagation authority; keep
(a) the manual independent inventory as the propagation step, (b) `decision_graph.json` only for
foundational definitions and strategic decisions whose dependents are implicit, and (c) `cascade.py
check` for justification cycles and dangling references (it found a real dangling id).
