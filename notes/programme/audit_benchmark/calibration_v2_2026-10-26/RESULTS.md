# Audit v2 (referee estimate) calibration — interim (2026-10-26)

Rubric: `../AUDIT_SKILL_v2_draft.md` (frozen at 7f5c6fd after dev). Bank: `../../audit_calibration_bank_v2.json`.

## Dev half (rubric written from these; 9 of 10 run)

| Item | Community | Programme bar | Referee estimate | Match |
|---|---|---|---|---|
| R1 Bloom–Sisask (v1 false kill) | valued simplification | T6 unclear, T2 fail | ACCEPT-LIKELY, research journal | yes (v1: no) |
| R3 Morris survey | survey | T6 unclear→pass | ACCEPT-LIKELY, expository | yes |
| RV1 Kuperberg ASM | valued new proof | T2 PASS | ACCEPT-LIKELY, research journal | yes |
| RV2 Greene Kneser | valued short proof (Monthly) | T2 conditional, T6 fail | ACCEPT-LIKELY, Monthly-type | yes |
| RV6 Kra (Bull. AMS) | valued exposition | T6 leaning fail | ACCEPT-LIKELY, expository (Bull. AMS) | yes |
| OA4 Diaconis–Sturmfels | foundational | T3, T4 PASS | ACCEPT-LIKELY, research journal | yes |
| OA1 Christian (Bell "disproof") | wrong | correctness FAIL | REJECT-LIKELY | yes |
| RN4 Parberry (withdrawn) | known + wrong | KNOWN (Wendt/Lehmer) | REJECT-LIKELY | yes |
| RN1 Johnson (retracted, renaming) | unvalued renaming | renaming found (Cohn) | BORDERLINE | partial → rule added |
| RV4 Lovász–Szegedy | valued framework | NOVEL, T4 pass | ACCEPT-LIKELY, research journal | yes |

Dev: 9/10 match, 1 partial. Change after dev: renaming rule (REJECT-LIKELY when the central notion is
an existing one renamed and no new statement is shown).

## Test half (held out, frozen rubric 7f5c6fd; 17 items)

| Item | Community | Referee estimate | Match |
|---|---|---|---|
| R2 Abramsky–Brandenburger | valued framework | ACCEPT-LIKELY, research journal | yes |
| RV3 Moser–Tardos | valued constructive proof | ACCEPT-LIKELY, research journal | yes |
| RV5 Hoory–Linial–Wigderson | valued survey (Bull. AMS) | ACCEPT-LIKELY, expository (Bull. AMS) | yes |
| RV7 Diaconis MCMC | valued survey (Bull. AMS) | ACCEPT-LIKELY, expository | yes |
| RV8 Cohn sphere packing | valued exposition (Notices) | ACCEPT-LIKELY, expository (Notices) | yes |
| OA3 Cabello–Severini–Winter | valued framework (PRL) | ACCEPT-LIKELY, letters | yes |
| OA5 Laskowski | valued bridge | ACCEPT-LIKELY, research journal | yes |
| P2 Kelley–Meka | novel | ACCEPT-LIKELY, top journal | yes |
| P5 acyclic directed bunkbed | novel | ACCEPT-LIKELY, short paper | yes |
| OA2 Rajan–Visser v1 | wrong | REJECT-LIKELY (measurability gap) | yes |
| NR1 Banica–Schlenker (reworded) | known (Lam–Leung) | REJECT-LIKELY, owner found, no leak | yes |
| NR3 Werner–Lenz (reworded) | known (Gyárfás–Lehel/Kaiser) | REJECT-LIKELY, owner found, no leak | yes |
| RN2 Glivenko re-proof | known (re-proof in print) | BORDERLINE (Seldin found) | partial |
| NP1 Holmsen et al. 2026 | known | BORDERLINE (t=1 known) | partial |
| NR2 Hegarty (reworded) | known (Green Thm 9.3) | BORDERLINE (owner found; residual case from rewording) | partial |
| RN3 Thilliez | known (similar result in print) | ACCEPT-LIKELY (owner located, unreadable) | **miss** |
| NR4 Bagherian (reworded) | known (Blau 2013) | ACCEPT-LIKELY (Blau not found) | **miss** |

Test positives (valued/novel): **9/9**. Test negatives (known/wrong): **3/8 match, 3 partial, 2 miss**.

## Conclusions

1. v2 removes v1's harshness: every valued exposition, simplification, framework and new theorem in
   dev+test (18/18) gets ACCEPT-LIKELY in a plausible venue class, while the programme bar stays strict.
2. v2 is **too lenient on already-known work when the owner is obscure**: it hedges (BORDERLINE) when it
   finds a partial owner, and passes when it cannot find or read the owner (RN3, NR4). The weakness is
   owner-search depth under an as-of date, not the value factors. v1's earlier "4/4 known" on N items
   relied on the leaked withdrawal notices; with the leak removed, the auditor found 3 of 4 owners.
3. Candidate fix (NOT validated; derived after seeing test results, so it needs fresh items): cap the
   referee estimate at BORDERLINE whenever the pure novelty verdict is UNCLEAR, and require the main
   result's nearest neighbour to be read beyond abstract level before ACCEPT-LIKELY. It would turn both
   misses into partials.

## Limits
n = 27 runs (10 dev, 17 test) + 12 v1 + 6 pilot. Many valued items are famous (recall likely). Negative
reframing items are thin (no zbMATH review text). Seeds for some items were written from titles/notices.

