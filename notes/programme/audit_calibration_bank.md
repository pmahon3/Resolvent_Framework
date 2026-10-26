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
