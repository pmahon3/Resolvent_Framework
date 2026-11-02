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
