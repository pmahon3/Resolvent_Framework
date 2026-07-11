# open_questions/ — layout (reorganized 2026-07-11, s16)

Open questions are dormant-until-new-input units (see CLAUDE.md, the
open-question lifecycle). This folder also hosts the ACTIVE thm-2
attack thread and the σ-essential hub documents it leans on.

| Path | What lives here |
|---|---|
| `oml_attack/` | OML taxonomy, active working note, and proof-read receipts. |
| `sigma_essential/` | σ-essential hub/verdict documents: taxonomy leaves (`sigma_essential_*`), prior-art verdicts (`czech_school_*`, `sharp_skeleton_*`), reduction writeups, reading notes (`navara_ptak_*`), `rigor_guard_scope.md`. |
| `kits/` | Pen-and-paper artifacts (tex+pdf): `oml_onboarding`, `problemset_oml_descent` (+ `references_oml.bib`, `figures/`), `ratification_kit_2026-07-11`, `companion_probability_without_a_joint_world`. |
| `verification/` | Machine oracles and from-scratch proof-read scripts (`proof_read_*/` subdirs are per-review, written blind to repo scripts). |
| `sigma_essential_taxonomy.json` | Stays at top level: registered in `notes/taxonomies_index.json`; its `detail` pointers are relative to THIS directory. |

Conventions: receipts live next to the note they audit; verification
scripts stay flat in `verification/` (referenced by absolute
`notes/open_questions/verification/...` paths from outside, and by
`../verification/...` from the subfolders).
