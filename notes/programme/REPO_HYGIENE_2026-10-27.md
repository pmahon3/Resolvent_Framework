# Repo hygiene scan, 2026-10-27 (report only; nothing changed)

Branch `hidden-failure-note`. Checklist: `.claude/agents/repo-hygiene.md` (structural parts) plus the six requested checks.

## Findings

1. **Untracked** (4 entries):
   - `notes/open_questions/cyclic_marginal/{intuition_kit,order_without_a_centre,pointless_coherence}.pdf` (150-364 KB): compiled outputs of tracked `.tex`. Other compiled PDFs in `notes/` ARE tracked (kits, genealogy, reconstruction.pdf), and CLAUDE.md tells the reader to open `order_without_a_centre.pdf`, so the repo convention is "track the PDF". These three are the odd ones out.
   - `tmp/` (7.7 MB, only `tmp/pdfs/`): 6 third-party PDFs plus `.txt` extracts and `gunji_methods-*.png` page images (abramsky_brandenburger_2011, bruns_kalmbach_free_oml_1973, burris_sankappanavar, fremlin_ch31, gunji_2026 arXiv 2603.22353, halmos). Nothing in the repo references `tmp/pdfs`. They are not in `SHELF_INDEX.json` and not on the shelf by those filenames (shelf has `bruns_1979_...`, `bruns_harding_2000_...`, `fremlin_2003/`). Last modified Sep 16.
2. **LaTeX artefacts**: none tracked (`git ls-files` finds no aux/log/out/bbl/blg/toc). Untracked .aux/.log/.out/.bbl/.blg/.toc exist on disk but `.gitignore` covers them. Missing patterns: `*.nav`, `*.snm`, `*.vrb`, `*.lof`, `*.lot`, `*.xdv`, `*.dvi`, `*-blx.bib`.
3. **Cross-references**:
   - `notes/taxonomies_index.json`: 0 broken paths.
   - `glued_carriers_taxonomy.json`: all 14 apparent "missing" paths resolve (the 12 `verification/*.py` are in `notes/open_questions/verification/`, and the 2 `case_*.md` are in `cyclic_marginal/`). They are written relative to `notes/open_questions/`. This is a convention to note, not a defect.
   - `SHELF_INDEX.json`: 129 entries, every `file` exists. Directory entries are covered (e.g. `caramello_2018/`). The PDFs listed under "unindexed" below are chapter splits and are probably covered by their directory entry; I did not verify this per file. Two files look genuinely unindexed: `ovchinnikov_1999_measures_finite_concrete_logics.pdf` and `ovchinnikov_sultanbekov_1998_finite_concrete_logics.pdf`. Check `desimone_navara_ptak_2015_states_symmetric_difference.pdf` too. Shelf PDFs are gitignored, so the CLAUDE.md rule "index entry in the same commit" applies to the JSON only.
   - CLAUDE.md: the only unresolved names are bare filenames (`frontier_map.md`, `shovel_plan.md`, `czech_school_prior_art_sigma_essential.md`) that exist under `notes/programme/` or `notes/open_questions/sigma_essential/`, plus `MEMORY.md` (outside the repo, by design).
4. **Audit benchmark duplication**:
   - `audit_calibration_bank.json` (14 items) is a strict subset of `_v2.json` (37 items, same ids plus NP/NR/OA/RN/RV). v1 is superseded. `audit_calibration_bank.md` says "Not committed" but is tracked (stale line).
   - `audit_calibration_validation_v21.json` (6 items) is a separate set; keep it.
   - `audit_benchmark/AUDIT_SKILL_v2_draft.md` is byte-identical to `.claude/skills/audit/SKILL.md`. `.claude/` is gitignored (0 tracked files there), so this is the only tracked copy of the live skill. "draft" is now misleading.
   - Layout: `audit_benchmark/{pilot_2026-10-26, calibration_2026-10-26, calibration_v2_2026-10-26}` plus top-level `notes/programme/audit_calibration_*` and `audit_benchmark_prior_art.md`. The benchmark files are split across two levels. Total 1.0 MB, 163 tracked files.
5. **Out-of-repo references**: `/tmp/...` appears in these tracked docs:
   - `hidden_failure/AUDIT_PHASE2.md` and `REAUDIT_v21.md`: `/tmp/audit_ce/ce1_test.py`, `ce1_vs_D.py`. These scripts back a quoted "exact upgrade at 3x3x3" result and are not in the repo (REAUDIT_v21.md says so itself).
   - `entry_audits/G5_forest_side.md`: `/tmp/g5dl` (Barr, CMU-Z downloads, not on the shelf).
   - `calibration_v2.../retest_v21_positive/OA3/AUDIT.md`: `/tmp/oa3dl`.
   - `sigma_essential_large_cardinal_bounds.md`: `/tmp/bw.txt`.
   - Census READMEs use `/tmp` only as build output (fine).
6. **Large tracked files (>5 MB)**:
   - `notes/open_questions/verification/census_2026-07-12_s38/s38_p3_k1_checkpoint.json` (17 MB).
   - `archive/articles/old/Theoretical Framework Discussion.pdf` and `archive/notes_archived_artifacts/conceptual_predecessors/neutral_operator_theory_article/Theoretical Framework Discussion.pdf` (7.8 MB each, byte-identical).

## Action list (priority order)

1. **NEEDS-USER** Decide on the three cyclic_marginal PDFs. Convention says track them (the note is the current deliverable):
   `git add notes/open_questions/cyclic_marginal/{intuition_kit,order_without_a_centre,pointless_coherence}.pdf`
   Alternative: gitignore them and change CLAUDE.md lines 81-84 to say "compile from .tex".
2. **NEEDS-USER** `tmp/pdfs`: move the 6 PDFs to the shelf and add SHELF_INDEX entries, or delete. Either way nothing should stay in `tmp/`.
   - To keep: `mv tmp/pdfs/<name>.pdf notes/literature_review/literature/`, add an index entry (the `.txt` extracts are optional).
   - To discard: `rm -r tmp/pdfs && rmdir tmp`.
   - To keep it local and untracked: add `tmp/` to `.gitignore`.
   - `gunji_2026` is already cited (memory: arXiv:2603.22353), so it should be shelved.
7. **SAFE** Add to `.gitignore`, after the LaTeX block: `*.nav`, `*.snm`, `*.vrb`, `*.lof`, `*.lot`, `*.dvi`, `*.xdv`, `*-blx.bib`.
2. **SAFE** Remove the duplicate 7.8 MB archive PDF (keep one): `git rm "archive/notes_archived_artifacts/conceptual_predecessors/neutral_operator_theory_article/Theoretical Framework Discussion.pdf"`. Confirm that nothing links to it (`grep -r "Theoretical Framework Discussion" .`); I did not check.
3. **NEEDS-USER** Rename the live-skill copy. It is the only tracked copy of an ignored file, so it needs a stable name and a sync note:
   `git mv notes/programme/audit_benchmark/AUDIT_SKILL_v2_draft.md notes/programme/audit_benchmark/AUDIT_SKILL_tracked_copy.md`
   Alternatively use `notes/programme/audit_skill/SKILL.md`. Then update the references in `program_overview.md`, `audit_benchmark/*/RESULTS.md` and `.claude/skills/audit/SKILL.md` (grep `AUDIT_SKILL_v2_draft`). Optionally un-ignore the skill with `!.claude/skills/` in `.gitignore` instead of keeping a copy.
4. **NEEDS-USER** Supersede bank v1. Either `git rm notes/programme/audit_calibration_bank.json` (v2 contains all 14 ids; first check that no v1 fields are absent from v2), or move both banks and the validation JSON into `audit_benchmark/banks/`. Fix the stale "Not committed" line in `audit_calibration_bank.md`.
5. **NEEDS-USER** Rescue the `/tmp/audit_ce/ce1_test.py` and `ce1_vs_D.py` scripts if they still exist on disk, by copying them to `notes/open_questions/cyclic_marginal/hidden_failure/verification/` and fixing the paths. Otherwise annotate the two audit docs "scripts lost". Add a one-line note on `/tmp/g5dl`, `/tmp/oa3dl` and `/tmp/bw.txt` (downloads, non-reproducible).
6. **NEEDS-USER** The 17 MB checkpoint JSON is tracked. Options: leave it, `git lfs`, or compress (`gzip` plus update the README). Do not rewrite history without asking.
7. **SAFE** Check the 3 possibly unindexed shelf PDFs (the two `ovchinnikov_*` and `desimone_navara_ptak_2015_*`) with `grep -c ovchinnikov notes/literature_review/literature/SHELF_INDEX.json`, then add entries if missing (an entry needs a read level, so NEEDS-USER for the content).
8. **SAFE** Note the path convention: taxonomy `detail` fields are relative to the taxonomy's own directory or to `notes/open_questions/`. Optionally add this to `TAXONOMY_SCHEMA.md`.
