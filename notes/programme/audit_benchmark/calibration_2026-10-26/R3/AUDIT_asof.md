## Audit: seed.md, a survey of recent progress in graph Ramsey theory (mode: full; as of 2026-01-07)

**Date discipline.** I audited as of 2026-01-07 and counted only sources dated on or before then. For papers revised later, I used v1. Date notes:
- An arXiv survey matching the seed's text (arXiv:2601.05221, v1 dated 8 Jan 2026) is the submission itself. Per AS_OF it is excluded, and it postdates the audit date in any case.
- GNNW arXiv:2407.19026 has a v2 dated 29 Aug 2026 by its abstract page. Only v1 (26 Jul 2024) is used here.
- Balister et al. arXiv:2410.17197 has a v2 dated 21 Jan 2026. Only v1 (22 Oct 2024) is used here.
- Hefty–Horn–King–Pfender arXiv:2510.19718 has a v3 dated 19 Feb 2026. Only v1 (22 Oct 2025) is used here.
- Wigderson's exposé is listed as appearing in Astérisque in 2026, and I could not tell whether that print version predates 2026-01-07. The arXiv v1/v2 (Nov/Dec 2024) do predate it, and those are what I use.
- The Umeå reading-course PDF has creation metadata of 27 Oct 2025, which predates the audit date.

**Bearing on WHY.md:** none directly. This is exposition of extremal combinatorics, and Ramsey theory's "local order forced in any large system" theme is a lens only.

### Declared contribution type(s): Type 6 (exposition)
The seed declares the type but does **not** state the per-type bars it commits to clearing. It names no audience, cites no inaccessible literature and claims no specific translation work. By the framework (Phase 1 requirement) it is not fully ready for Phase 2.

### Pure Verdict: KNOWN (by design; not a Type-1 claim)
The seed claims no new theorem. Every result it presents is published or preprinted prior work:
- **Diagonal:** Campos–Griffiths–Morris–Sahasrabudhe, arXiv:2303.09521 (Mar 2023), R(k) ≤ (4−ε)^k. Read level: abstract.
- **Near-diagonal / optimised:** Gupta–Ndiaye–Norin–Wei, arXiv:2407.19026 v1 (26 Jul 2024), R(k,k) ≤ 3.8^{k+o(k)}. Read level: abstract.
- **Multicolour:** Balister–Bollobás–Campos–Griffiths–Hurley–Morris–Sahasrabudhe–Tiba, arXiv:2410.17197 v1 (22 Oct 2024), R_r(k) ≤ e^{−δk} r^{rk}. Read level: abstract.
- **R(3,k), first improvement:** Campos–Jenssen–Michelen–Sahasrabudhe, arXiv:2505.13371 (May 2025), R(3,k) ≥ (1/3+o(1))k²/log k. Read level: snippet (search summary and talk abstract).
- **R(3,k), second improvement:** Hefty–Horn–King–Pfender, arXiv:2510.19718 v1 (22 Oct 2025), constant 1/2. Read level: abstract.
- **R(4,k):** Mattheus–Verstraete, "The asymptotics of r(4,t)", Ann. Math. 199 (2024) 919–941, arXiv:2306.04007 (Jun 2023). Read level: snippet.
- **Induced Ramsey:** Aragão–Campos–Dahia–Filipe–Marciano, arXiv:2509.22629 (Sep 2025), r^{Crk} bound, settling Erdős's 1975 conjecture for r=2. Read level: snippet (search summary and Cambridge talk listing, 22 Oct 2025).

No new statement is claimed, so there is nothing to kill on novelty.

### Applied Verdict: not evaluated (no Type 7 claim; no method or computation)

### Contribution Type Verdicts (mode=full):

**Type 6 (Exposition / translation): UNCLEAR, leaning CONDITIONAL PASS on the 2025 material and FAIL-risk on the diagonal material.**

- **(a) Target audience: not named.** "Accessible" implies non-specialists, probably graduate students and combinatorialists outside the probabilistic or Ramsey subcommunity, but the seed does not say so. This is a bar defect as written.

- **(b) Literature the audience cannot currently access: split verdict.**
  - **Diagonal upper bound (CGMS, plus the shorter BBCGHMST proof): already accessible.** Wigderson, "Upper bounds on diagonal Ramsey numbers [after Campos, Griffiths, Morris, and Sahasrabudhe]", Séminaire Bourbaki exposé no. 1230, arXiv:2411.09321 (v1 14 Nov 2024; v2 20 Dec 2024). It is a 48-page exposition of CGMS, and v2 adds the alternative, more conceptual proof of Balister et al. Read level: abstract and comments. GNNW v1 (Jul 2024) gives a shortened inductive proof, and Balister et al. v1 (Oct 2024) gives a shorter different proof for r=2. On this part, the framework's park clause applies: "well-explained in [Wigderson 2024]".
  - **Multicolour: partly accessible.** Wigderson v2 covers the follow-up only to the extent of the alternative r=2 proof (abstract-level evidence).
  - **R(3,k) lower bounds (May and Oct 2025), R(4,k) (2023/24) and induced Ramsey (Sep 2025): I found no expository treatment dated on or before 2026-01-07.** These results are scattered across primary papers, three of them under a year old at the audit date, with differing techniques: a seeded triangle-free process, a "two bites" random construction, a pseudorandom algebraic construction, and the induced-Ramsey argument. A single unified account is a genuine gap. Mild counter-evidence: the Umeå PhD reading course "Major breakthroughs in Ramsey Theory" (PDF metadata 27 Oct 2025; read level: link targets only) assigns the primary papers 2410.17197, 2303.09521 and 2507.12926 plus Wigderson 2411.09321 directly. That suggests graduate students can already access the upper-bound material from primary sources and Wigderson.

- **(c) Non-trivial conceptual work: cannot be assessed from the seed.** The seed gives no indication of the unifying viewpoint, for example a common thread between the book algorithm, the R(3,k) nibble-type constructions and the R(4,k) algebraic construction. Collecting proofs in sequence is not by itself non-trivial translation. To clear (c), the survey must show a simplification or connection not present in Wigderson, GNNW or the primary papers.

- **Bar applied:** (a) ✗ as written; (b) ✓ for the 2025 off-diagonal, R(4,k) and induced parts, ✗ for the diagonal part; (c) unverified.

### Cross-reference
- The components are known by design (Pure = KNOWN, as expected for a survey). The only live type is Type 6.
- Type 6 survives on the breadth of the assembly and the recency of the 2025 results, not on the diagonal material, which Wigderson's Bourbaki exposé already owns.
- **Most damaging prior source:** Wigderson, arXiv:2411.09321 (Nov/Dec 2024), Bourbaki exposé 1230, treatment of the CGMS book algorithm plus the BBCGHMST alternative proof (v2). Read at abstract level; section numbers not verified.

### Recommendation
**Proceed to Phase 3 scoped to Type 6, conditional** on three things:
1. naming the audience (for example, graduate students and non-Ramsey combinatorialists);
2. explicitly differentiating the diagonal and multicolour sections from Wigderson 2024 and GNNW 2024, either by compressing them to a pointer or by adding a viewpoint those works lack;
3. resting the (b) claim on the 2025 R(3,k), induced-Ramsey and R(4,k) material, where no prior exposition was found.

If (2) cannot be met and the 2025 material is only paraphrased, park. Venue class: an expository survey (for example, Bull. AMS, Notices, or ICM- or BCC-type survey proceedings).
