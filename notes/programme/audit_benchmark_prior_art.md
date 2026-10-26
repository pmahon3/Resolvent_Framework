# Prior art for benchmarking the /audit skill

Date: 2026-10-26. reviewed: false. Scout run; web search standard mode, no extended pass.
Shelf check first: SHELF_INDEX.json had nothing on peer review or LLM reviewing (only the Livson et al. entry). Four open-access PDFs were added to the shelf with index entries (question key `audit_benchmark`).

Read levels: FULL = body read; ABS = abstract/intro of the PDF read in this session; SNIP = search-result snippet only (not opened); MEM = from memory, unverified.
Nothing below is FULL. Every number is as reported by an abstract or a search snippet and should be checked against the paper before it is cited.

## 1. Findings

### Q1. LLMs as reviewers and novelty assessors

| Item | Citation | Key finding | Level |
|---|---|---|---|
| Liang et al. | Liang, Zou et al., "Can large language models provide useful feedback on research papers? A large-scale empirical analysis", NEJM AI 1(8), 2024, DOI 10.1056/AIoa2400196; arXiv:2310.01783 | GPT-4 comments overlap with human reviewers' points at 30.85% (Nature journals) and 39.23% (ICLR), against 28.58% and 35.25% between two humans. Overlap is higher on weaker papers. 308-researcher user study: 57.4% found it helpful. The overlap metric is "points raised", not correctness. | SNIP (two snippets disagree on survey figures; the abstract figures are the ones quoted) |
| Liu & Shah | "ReviewerGPT? An exploratory study on using LLMs for paper reviewing", arXiv:2306.00622 (2023) | Planted errors: GPT-4 finds the inserted error in 7 of 13 short papers. Checklist verification 86.6% on 119 pairs. Picks the better abstract wrongly on 6 of 10 clear pairs. It also flags correct parts as wrong. Only GPT-4 worked among nine models tried. | ABS (on shelf) |
| Lu et al. | "The AI Scientist", arXiv:2408.06292 (2024); later Nature version | Automated reviewer (GPT-4o, NeurIPS form) on 500 ICLR 2022 papers: balanced accuracy 0.61 zero-shot, against 0.66 for human reviewers. Later version reports 0.69 before and 0.66 after the model cutoff, read by the authors as possible contamination. | SNIP |
| Si, Yang, Hashimoto | "Can LLMs generate novel research ideas? A large-scale human study with 100+ NLP researchers", arXiv:2409.04109 (ICLR 2025) | 79 expert reviewers; LLM ideas rated more novel than expert ideas (p<0.05) and slightly less feasible. Authors flag LLM self-evaluation as unreliable and note that even experts judge novelty with difficulty. This is evidence about humans rating novelty, not about LLM prior-art checking. | SNIP |
| Zhou, Chen, Yu | "Is LLM a reliable reviewer? A comprehensive evaluation of LLM on automatic paper reviewing tasks", LREC-COLING 2024, pp. 9340-9351 | GPT-3.5/4 on score prediction, review generation and a 197-question review-revision multiple-choice set from ICLR 2023 threads. Single-option accuracy above 60%, fully correct answers about 20%. Weak on long papers and critical feedback. | SNIP |
| MARG | D'Arcy, Hope, Birnbaum, Downey, arXiv:2401.04259 (2024) | Multi-agent review generation; generic comments fall from 60% to 29% in a user study. Measures comment helpfulness, not verdict accuracy. | SNIP |
| LLM-REVal; "When your reviewer is an LLM" | arXiv:2510.12367; arXiv:2509.09912 | LLM reviewers inflate scores for weaker papers and for LLM-written text; field-specific prompt injection shifts ratings; LLMs underweight novelty relative to humans (a KAIST/LG study is cited for that last point, not located). | SNIP |
| SchNovel | Lin, Peng, Fang, arXiv:2409.16605 (2024; AISD workshop 2025) | 15,000 arXiv pairs, six fields, 2-10 years apart; later paper assumed more novel (proxy label). Reports prompt-order and affiliation bias in LLM novelty judgments; RAG-Novelty baseline. Mathematics and physics are noted as hard. | ABS (on shelf) |
| RINoBench | arXiv:2603.10303 (2026) | 1,381 research ideas with expert novelty judgments; LLM rationales resemble human ones but verdicts are not reliably accurate. | SNIP (title not confirmed) |
| FLAWS | Xi, Rao, Payan, Shah, arXiv:2511.21843 | 713 LLM-inserted claim-invalidating errors in ICML 2025 papers; best of five frontier models, GPT 5, locates the error 39.1% of the time at k=10. Errors are synthetic. ML papers only. | ABS (on shelf) |

Not located: ReviewEval, DeepReview, Reviewer2 (the search returned nothing for them; they may exist, so this is unverified).
Patent prior art: examiner citations (EPO X/A categories) are the standard ground truth, evaluated with recall-oriented metrics such as PRES on CLEF-IP (CLEF-IP 2009-2012 tracks; Magdy & Jones PRES). The snippet notes that examiner citations are only "what one examiner found in the time available", so recall against them is a lower bound. No LLM-specific, examiner-grounded benchmark was found (SNIP; "none found" is not a proof of absence).

Gap that matters for us: no source evaluates an LLM on a binary "is this already known" verdict with a ground truth of a known owner. SchNovel is the closest and uses a date proxy. This is a gap in what the scout found, not a demonstrated absence.

### Q2. Human reliability baselines

- NeurIPS 2014 experiment: Cortes & Lawrence (the "Inconsistency in conference peer review: revisiting the 2014 NeurIPS experiment" paper; arXiv ID not retrieved). Snippet: about half the variation in quality scores is subjective; among accepted papers, no correlation between score and later citations; process good at flagging poor papers, poor at identifying good ones. SNIP.
- NeurIPS 2021: Beygelzimer, Dauphin, Liang, Vaughan, arXiv:2306.03262. Two independent committees on 10% of papers disagree on accept/reject for 23% of papers; about half of the accepted list would change on a rerun; more selectivity means more arbitrariness. ABS (on shelf).
- Bornmann, Mutz, Daniel 2010, PLoS ONE 5(12):e14331, "A reliability-generalization study of journal peer reviews". 48 studies, 70 coefficients, 19,443 manuscripts; pooled Cohen's kappa 0.17, ICC about 0.34; larger studies show lower reliability. SNIP.
- Cicchetti 1991, Behavioral and Brain Sciences 14(1):119-135 (page range varies between sources). Referees agree more on what is unworthy than on what is worthy; low reliability overall. Full text paywalled. SNIP.

Use for us: the Lu et al. comparison (LLM balanced accuracy near the human 0.66) shows the standard framing of "as good as a noisy human". Our ground truth should not inherit that noise, because our kills are decided by a citable owner, not by committee opinion. A reviewer-style agreement statistic is the wrong yardstick for us.

### Q3. Bank-building methodology

- Planted errors: Liu & Shah (13 hand-built papers), FLAWS (713, LLM-inserted). Both show the planted-error approach works and both flag artifact risk (errors that are trivially detectable, or not truly invalid). Seeded faults and mutation testing are the software analogue: Jia & Harman, "An analysis and survey of the development of mutation testing", IEEE TSE 37(5), 2011 (MEM, not retrieved). The transferable idea is the equivalent-mutant problem: some perturbations do not change the ground truth, and you must check that your costume really is the same theorem.
- Contamination: Chen et al., "Benchmarking LLMs under data contamination: a survey from static to dynamic evaluation", EMNLP 2025, arXiv:2502.17521 (SNIP). It reports that dynamic benchmarks lack standardized evaluation criteria. The Lu et al. before/after-cutoff split is the one concrete example found of a post-cutoff control. Two closely related claims from the search: a 2026 review (arXiv:2608.14407, SNIP) says reproducing a known result is weak evidence of creativity and recommends temporally held-out tests, and Mossel (arXiv:2601.02380, SNIP, via a fetch of the abstract) argues that opaque training data makes novelty claims unverifiable.
- Ground truth from later reception: citations, retractions, examiner citations (see above). Multiple-discovery datasets (Merton 1961; Ogburn & Thomas 1922) were not searched and no machine-readable dataset was found. Treat this as open.
- Metrics: not found for novelty verdicts specifically. Standard ones apply (see section 2).
- LLM-reviewer failure modes: score inflation on weak papers, preference for LLM-written text, prompt-injection susceptibility, order and affiliation bias (SchNovel), weak long-document handling (Zhou), false flags on correct text (Liu & Shah). Sycophancy toward author claims and hallucinated citations were searched for and not found in a review-specific source; they remain plausible but unsupported here.

### Q4. Mathematics

- October 2025 Erdős episode (press accounts, SNIP): OpenAI staff announced GPT-5 had "solved" ten Erdős problems listed as open; Thomas Bloom (erdosproblems.com maintainer) said "open" there only means he knows of no paper, and that GPT-5 had found existing solutions in the literature; Bubeck conceded that only solutions already in the literature were found. Lesson: the literature search was the real result, and "open" labels are weak ground truth. An unverified LinkedIn post claims most later GPT-5.2 Pro Erdős solutions overlapped published work; not used.
- Frameworks proposed: pre-registered attempts on truly open problems with formal checking (arXiv:2608.14407, SNIP); an explicit catalog of prior results with a "domination test" to separate improvements from rediscovery (QuantumNovelty, arXiv:2608.16900, SNIP; physics, but the idea transfers).
- Not found: a benchmark of LLM judgments of mathematical novelty, or a Lean-based novelty check. FrontierMath and proof-verification benchmarks were not searched in this pass.
- Lessons for us: rediscovery is the dominant failure of LLM math claims, which is exactly the auditor's task run in reverse; our own repo records show the same pattern in humans-plus-LLM (Dravecký-Šipoš Ex. 6 and the Gudder additivity region "rediscovered" 2026-10-20).

## 2. Pilot design (6 items)

Purpose: estimate, with only six items, whether the auditor (a) finds owners it should find, and (b) does not kill new work. Six items cannot give rates. They can only expose gross failure and test the harness. Say so in any report.

Items:
1. Countable-additivity note (owner: FHM 1990). Pre-kill version of the seed.
2. Strategy D (owner: Gaifman 1964). Pre-kill seed.
3. A third own kill with a different owner type. Candidates in `notes/covered_leads/`: Boolean-factoring (Akemann-Weaver), or the hidden-failure triangle equivalence (owner Sullivant Thm 2.4(2) + Prop 5.8; but that kill is only days old and the owner is on the shelf, so its blinding is weakest). Prefer an older one.
4. One planted costume: a known theorem, ideally from the repo's own area but absent from the shelf and the taxonomies, restated in fresh vocabulary with a new notation. Write a matching equivalence check (a few lines) so the costume cannot be a non-equivalent mutation.
5. One recent known-good: a post-cutoff, genuinely new result whose novelty a later source confirms. Pick one dated after the auditor model's stated cutoff (June 2026 for the current model), e.g. a result the user's field has accepted and cited since. Candidate not chosen here; needs a user decision.
6. Livson, Pritam, Prokopenko, arXiv:2601.07283. Not a ground-truth kill. Use as a calibration case: the repo's own read says "neighbour, not owner". Check that the auditor reaches an equivalent verdict, and keep it out of the aggregate metrics.

Blinding (what to hide):
- Strip the kill: reconstruct the seed note as of the commit before the kill (use `git log`/`git show`; commit hashes not looked up). Remove every later note, the taxonomy entry, covered_leads file, MEMORY entries and the shelf index. The auditor reads files, so run it in a clean worktree at the pre-kill commit, or in a directory containing only the seed and `.claude/skills/audit/` plus `contribution_evaluation.md`.
- Shelf-first is part of the live workflow. In the blind run, the shelf at that date is what the auditor gets; the shelf must not contain the owner PDF if it was added after the seed.
- Do not tell the auditor it is being benchmarked, the item's origin, or the expected verdict. Use the same invocation as live (opus Agent, per `feedback_audit_invocation`).
- The owner must not appear in the seed text. If the seed already cites it, the item is not usable.
- Freeze: record model ID, date, tool set (web search on or off). Run twice per item to see within-item variance, but count only the first run in the headline.

Metrics (descriptive, not tested; n=6):
- Owner hit: did it name the owner or an equally good one (yes/no, with the cited theorem number checked by a human)? For items 1-3 and the costume.
- Verdict vs truth: KNOWN/NOVEL/UNCLEAR against the label; count UNCLEAR separately, not as correct.
- False kill: on item 5, any KNOWN verdict, and any type FAIL not justified by a cited source.
- Citation validity: share of cited sources a human confirms exist and say what is claimed (hallucination check).
- Cost: tokens, tool calls and wall time per item.
- Consistency between the two runs.

Pitfalls:
- Contamination: FHM 1990 and Gaifman 1964 are well known to the model, so a hit may be recall rather than search. Add a no-web-search arm to separate memory from retrieval.
- The recent known-good may also have leaked into training despite the cutoff; verify the date.
- Own kills are a biased sample (cases where the owner was eventually found, usually by an LLM-assisted scout); they cannot measure misses on rediscoveries nobody has found yet. The false-pass rate measured this way is a lower bound: it only counts rediscoveries someone has already identified.
- Costume equivalence: a mutated restatement may differ subtly (the equivalent-mutant problem), so the "known" label can be wrong. Hand-check.
- The seed's wording is itself a hint. Writing the pre-kill seed from the git version is cleaner than rewriting it.
- n=6: do not report rates or confidence intervals as findings.
- The auditor is also a type-bar judge. A KNOWN verdict with a wrong owner is not a hit.

## 3. Established vs open

Established (as reported by the sources, with read levels above):
- Human review is noisy: kappa about 0.17 (meta-analysis), 23% committee disagreement at NeurIPS 2021.
- LLM reviewers come close to human accuracy on accept/reject at conference scale (Lu et al.) but are weak at planted-error detection (about half in a 13-paper study, about 39% in FLAWS), at novelty, and are biased by style, order and injected text.
- Planted-error and date-split designs exist and have been used; contamination is a recognized threat.
- AI "math discoveries" have repeatedly been rediscoveries (Erdős episode).

Open / not found:
- Any evaluation of an LLM's binary "already known" verdict against a known owner, in mathematics or elsewhere.
- Multiple-discovery datasets as ground truth.
- Calibration of KNOWN/NOVEL verdicts; false-kill rate on genuinely new mathematics.
- Whether a reviewer-agreement benchmark transfers to a tool that is told to be hostile (the skill's design pushes toward KNOWN, so false kills are the main risk, and nothing found measures that).
- ReviewEval, DeepReview, FrontierMath/proof-verification benchmarks, Merton-style multiples, mutation-testing details: not read or not searched.
