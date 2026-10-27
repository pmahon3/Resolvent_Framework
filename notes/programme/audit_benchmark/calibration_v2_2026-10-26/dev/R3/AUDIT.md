## Audit: seed.md, "accessible overview of recent progress in graph Ramsey theory" (mode: full)

Audit date (per AS_OF.md): **2026-01-07**. Only sources dated on or before this date count as prior art. Searches surfaced the seed's own text (a January 2026 arXiv survey, "Some recent results in Ramsey theory"). Following AS_OF it is treated as the submission itself, not as prior art, and its contents were not used.

### Declared contribution type(s): Type 6 (exposition/translation)
The type is declared, but the per-type bars are not stated: the seed does not name a target audience (bar a) and does not name the literature that is inaccessible (bar b). I have reconstructed both below. Under the framework's Phase 1 rule this is a readiness defect.

### Pure Verdict: KNOWN (by design; no Type 1 claim)
The seed claims no new theorem. Every result it lists is prior work, and each has an owner:
- Diagonal R(k) ≤ (4−ε)^k: Campos–Griffiths–Morris–Sahasrabudhe, arXiv:2303.09521 (2023). [Read level: abstract/metadata via search, checked 2026-10-26.] The constant was optimised by Gupta–Ndiaye–Norin–Wei (2024) [title-level via search snippet only].
- Multicolour bound, plus a significantly shorter proof of the r = 2 case: Balister–Bollobás–Campos–Griffiths–Hurley–Morris–Sahasrabudhe–Tiba, arXiv:2410.17197 (Oct 2024; JAMS 39(3), 2026). [Abstract-level via search, checked 2026-10-26.]
- Near-diagonal / off-diagonal exponential improvement: the 2023 CGMS paper treats R(ℓ,k) for ℓ ≤ ck. [Abstract-level.]
- R(3,k) ≥ (1/3+o(1))k²/log k: Campos–Jenssen–Michelen–Sahasrabudhe, arXiv:2505.13371 (May 2025). [Abstract-level via search, checked 2026-10-26.]
- R(4,k) = Ω̃(k³): Mattheus–Verstraete, Annals of Math. 199 (2024) 919–941. [Citation-level via search, checked 2026-10-26.]
- Induced Ramsey numbers R_ind(H;r) ≤ r^{Crk}: Aragão–Campos–Dahia–Filipe–Marciano, arXiv:2509.22629 (Sep 2025). [Abstract-level via search, checked 2026-10-26.]
Every one of these predates 2026-01-07. Type 1 is not claimed, and nothing in the seed would pass it.

### Applied Verdict: not evaluated (no Type 7 claim; pure mathematics)

### Contribution Type Verdicts (mode=full):

**Type 6 (Exposition/translation): UNCLEAR, leaning PASS**
- **(a) Audience.** The seed does not name one. The plausible audience is graduate students and combinatorialists outside the probabilistic and extremal Ramsey subcommunity. "Accessible overview" implies this audience but does not state it.
- **(b) Inaccessible literature.** This bar is plausibly met. The primary literature consists of six or more technical papers from 2023–2025, scattered across different methods: the book algorithm, the geometric and Gaussian approach, the seeded triangle-free process, finite-geometry and unital constructions with containers, and induced-Ramsey methods. The CGMS original is long. The only pre-2026-01-07 exposition located is Wigderson, "Upper bounds on diagonal Ramsey numbers [after Campos, Griffiths, Morris, and Sahasrabudhe]", Séminaire Bourbaki exposé 1230, arXiv:2411.09321 (Nov/Dec 2024). [Abstract-level, fetched 2026-10-26.] It covers **only the diagonal two-colour case**. The pre-breakthrough survey, Conlon–Fox–Sudakov, "Recent developments in graph Ramsey theory" (Surveys in Combinatorics 2015) [citation-level], cannot cover any of these results. I found no single accessible source that covers the multicolour, R(3,k), R(4,k) and induced results together. One search hit (an ems.press PDF) could not be read, so I could not identify it or tell whether it is a competing survey; this is an open gap.
- **(c) Non-trivial conceptual work.** This cannot be verified from a three-line seed. Presenting proofs, not merely statements, of six recent breakthroughs, and showing what their methods share, is substantial synthesis if it is done. The overlap with Wigderson is a risk for the diagonal portion only.
- **Bar applied.** The framework's park condition reads "already accessible to the target audience". For the diagonal case alone that would trigger (Wigderson). For the collection as a whole it does not. The verdict is UNCLEAR rather than PASS only because bars (a) and (c) are not documented in the seed.

**Undeclared types.** None are implied. The seed makes no Type 2 claim: the shorter diagonal proof is credited to the Balister et al. paper, not to the survey.

### Cross-reference
The components are known (Pure: KNOWN, as intended). Any value lies entirely in the assembly and presentation (Type 6). The programme's Type 6 bar fails partly against Wigderson for the diagonal piece. It is plausibly cleared for the multicolour, off-diagonal, R(3,k)/R(4,k) and induced material, which has no prior unified exposition that I could locate.

### Recommendation
**Redirect to expository venue** (proceed scoped to Type 6), on two conditions:
1. Name the audience.
2. Position the piece explicitly against Wigderson (Bourbaki 2024) and Conlon–Fox–Sudakov (2015), stating what it adds beyond the diagonal case.

There is nothing to park, because the seed does not claim novelty. Evaluated: Type 1 (KNOWN, not claimed) and Type 6 (UNCLEAR, leaning PASS). No bar failed outright.

Bearing on WHY.md (one line, per skill; WHY.md is not in this directory): Ramsey theory asks when local colour constraints force global order. That is a loose lens on "order without a centre". It is not a bridge, and it does not change any bar.

### Referee estimate: ACCEPT-LIKELY
Venue class: expository (survey: e.g. Surveys in Combinatorics, Bulletin AMS, or a proceedings or survey volume)
Value carried by: factor 4 (it synthesises scattered recent work, from 2023–2025, into one accessible treatment)
Main risk a referee would raise: the diagonal part overlaps Wigderson's Bourbaki exposition (arXiv:2411.09321), and the selection and depth of proofs must add organisation beyond restating the original papers.

Undetermined dates: the unidentified ems.press PDF (date and content unknown).
