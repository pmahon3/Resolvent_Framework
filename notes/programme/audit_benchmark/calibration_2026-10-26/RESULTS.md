# Audit calibration against community verdicts (2026-10-26)

Bank: `notes/programme/audit_calibration_bank.json` (14 items; X2, P4 dropped). Auditor: opus, mode full,
sandboxed (seed + skill + framework only; not enforced). P and R items audited "as of" their submission
date (AS_OF.md: the seed's own paper, later works and reception excluded). N and X items were run
without an as-of date.

| Item | Community verdict | Audit verdict | Match |
|---|---|---|---|
| N1 Banica–Schlenker (withdrawn) | known (Lam–Leung 2000) | KNOWN, Lam–Leung, 2-line reduction | yes* |
| N2 Hegarty (withdrawn) | known (Green 2005 Thm 9.3) | KNOWN, Green + Hancock–Treglown | yes* |
| N3 Werner–Lenz (withdrawn) | known (Gyárfás–Lehel 1970) | KNOWN, Gyárfás–Lehel, Kaiser 1997; caught seed misstatement | yes* |
| N4 Bagherian (withdrawn) | known (Blau 2013) | KNOWN, named own preprint; Blau partial | partial* |
| X1 Czelakowski (retracted) | wrong | proof invalid (R–S gives consistency, not truth) | yes |
| P1 diagonal Ramsey (Annals) | novel | NOVEL, Type 1 PASS (prior SOTA Sah) | yes (famous) |
| P2 Kelley–Meka (FOCS) | novel | NOVEL, Type 1 PASS; Type 3 FAIL | yes (famous) |
| P3 bunkbed false (PNAS) | novel | NOVEL, Type 1 PASS (precursor Hollom) | yes |
| P5 acyclic directed bunkbed (EJC) | novel | NOVEL, conditional PASS (Type 5) | yes (least famous) |
| R1 Bloom–Sisask exposition (Ess. Number Theory) | valued exposition/simplification | Type 6, Type 2 leaning FAIL; "needs deeper audit" | **no (likely false kill)** |
| R2 Abramsky–Brandenburger (NJP 2011, foundational) | highly valued framework | Type 4 conditional PASS, Type 3 leaning FAIL; proceed | partial (undervalued) |
| R3 Morris survey (2026) | survey (accepted genre) | Type 6 UNCLEAR, leaning conditional pass | soft yes |

\* N items leaked: web search found the seed's own arXiv page and withdrawal comment. They show the
auditor can locate and read sources, not that it finds unknown owners. Re-run with reworded seeds owed.

## What it says

1. **Kills of known/wrong work: reliable** (5/5, with the leak caveat; plus 6/6 in the owner-finding pilot).
2. **New theorems: not falsely killed** (4/4 P items pass as of their date). Famous items may pass by recall.
3. **Divergence from the community is on reframing/exposition/method**, not on theorems:
   - R1: a valued simplification judged leaning FAIL because the source was "already accessible";
   - R2: a foundational framework only conditionally passed;
   - P2: Type 3 FAIL on a paper praised for its method;
   - Livson (pilot item E): fails our bars, valued by press (and has an error in Thm 5).
   Our Type 6 bar ("literature inaccessible") and Type 3 bar ("method transfer between domains") are
   stricter than community practice, which also rewards simplification, clarity and new techniques
   within one field.

## Proposed audit change (not applied; user's call)

Report two verdicts: **(a) programme bar** (unchanged) and **(b) referee estimate**: would a competent
referee at a good venue in the field accept, counting simplification, clarity, new technique within a
field, and framework value. Calibrate (b) on a larger bank.

## Limits

n = 12 (+6 pilot). Combinatorics-heavy; nothing from algebraic statistics or orthomodular structures.
Famous P items (P1, P2) and R2 likely known to the model. As-of rule relies on the auditor's compliance.
No genuine journal rejections observable.
