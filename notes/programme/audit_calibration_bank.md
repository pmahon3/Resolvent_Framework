# Audit calibration bank (community-verdict ground truth)

Date: 2026-10-26. Companion: `audit_calibration_bank.json` (14 items). Not committed.

## Counts
N 4 (arXiv self-withdrawals citing a named owner), X 2, P 5 (4 asked + 1 bonus), R 3. Livson et al. excluded as instructed.

## Method
- N: arXiv comment search (`arxiv.org/search/?searchtype=comments`; queries "withdrawn" + "already known" / "previously known" / "already proved" / "known result"). Fetched abstract pages for the four with a named owner in near-repo areas.
- X: Retraction Watch (fetched); Springer retraction note (snippet only).
- P: fetched Annals page, arXiv abstract pages, Quanta, Wikipedia (bunkbed).
- R: arXiv abstract pages.
- Seeds paraphrase fetched abstracts with owner/venue/reception removed. Several paraphrase tool summaries, not verbatim abstracts; re-read arXiv v1 before use.

## What was hard
- No 2024-2026 withdrawal-for-duplication found. The search tool does not handle arXiv listings; comment search gave mostly 2005-2018 items (newest 2020). arXiv:2608.14669 reports ~26 such withdrawals but its page did not list them; its dataset is the next place to look.
- MathOverflow cannot be fetched. No MO "is this known" item confirmed; the Czelakowski MO thread is cited via Retraction Watch only.
- No Notices/Bulletin/Monthly exposition in the repo's areas; no Quanta piece in quantum foundations / OML / social choice.
- Nothing in contingency tables / algebraic statistics, finitely additive measures, OML or topological social choice. The bank is combinatorics-heavy.

## Honest limits
- All items predate the June 2026 cutoff. P1, P2, X1, R2 are famous: expect recall over retrieval. No post-cutoff item (latest is R3, Jan 2026, no reception).
- N labels rest on the authors' own withdrawal comments (author-as-community). Owner theorems were not hand-checked.
- P: only P2 has a fetched expert-reception quote. P3 relies on Wikipedia for PNAS and Quanta. P4 evidence is a search snippet.
- X2 is weak: snippet only, seed from title, proof gap invisible to a seed. Drop unless abstract fetched. X1 tests soundness, not novelty.
- R2 and R3 lack reception evidence; R1 is the only fairly clean R.
- Correlated: P3/P4/P5 (one thread); P2/R1 (one result).
- n is small; report no rates.

## 2026-10-26 expansion: `audit_calibration_bank_v2.json` (37 items, not committed)

Counts: old 14 (N4 X2 P5 R3) + RV 8, RN 4, OA 5, NR 4, NP 2 (spare, near-cutoff withdrawals). Split: dev 18 / test 19 in total. By category (dev/test): RV 4/4, RN 2/2, OA 2/3, NP 1/1, NR 0/4, old as assigned (N 0/4, X 2/0, P 3/2, R 2/1).

Method: Wikipedia (Conant, Fulkerson, Godel, Kneser, ASM, algebraic statistics) for community-valued items; arXiv abstract pages and arXiv comment search (`searchtype=comments`, which works via fetch) for withdrawals; Retraction Watch for the Johnson case; Gill's Entropy paper for Christian. NR seeds are rewordings, not re-verified against the originals.

What was hard:
- zbMATH Open returns HTTP 403 to fetch; no zbMATH review text obtained. Retraction Watch math category lists almost no "already known" cases (one: Johnson 2017).
- RN is the weakest category. Real unvalued-reframing evidence is nearly all author withdrawals, so RN items are mostly "known" or "re-proof already published", not "framework nobody wanted". No published rebuttal showing a new framework is a relabelling was found.
- Nothing found in finitely additive measures (searches returned only a 2025 paper with no verdict). OA has no FA item; contingency tables/algebraic statistics has one (OA4), model theory one (OA5, snippet only), contextuality/KS three.
- RV evidence is prize listings (Conant, Fulkerson, Godel, Morgan), a stricter proxy than reception text. Several seeds (RV2, RV5, RV6, RV7, OA4, OA5, RN1) are reconstructed from titles and descriptions, not abstracts; flagged in `notes`.

Limits:
- Famous items (RV3, RV4, OA1, OA4): recall expected. as_of dates for pre-arXiv items are approximate.
- Small n per cell; no rates. OA1 and OA2 test soundness, not novelty.
- Prize-winning surveys test the auditor's Type 6 bar; RV 3/4 items also test the Type 3 bar.
- Ground truths not hand-checked beyond the quoted comments. Dev/test split is by category balance, not randomised.
