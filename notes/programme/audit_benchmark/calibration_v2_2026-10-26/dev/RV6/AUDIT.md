## Audit: seed.md, "Green–Tao theorem from an ergodic point of view" (mode: full)

Audit date per AS_OF.md: **2005-10-05**. Only sources dated on or before that day count; the seed's own
text and any later versions or coverage of it are ignored. Search performed 2026-10-26.

### Declared contribution type(s): Type 6 (exposition / translation)
The seed declares the type but does not spell out the per-type bar it commits to (it names an audience
only implicitly: "readers who know ergodic theory but not additive combinatorics"). That is enough to
audit, but it is a weak declaration.

### Sources consulted (read level, date of source, pre-cutoff status)
| # | Source | Date | Read level | Pre-2005-10-05? |
|---|---|---|---|---|
| S1 | Green & Tao, "The primes contain arbitrarily long arithmetic progressions", arXiv:math/0404188 (v1) | 8 Apr 2004 | abstract + arXiv page | yes (v1); later versions to 2007 ignored |
| S2 | Tao, "A quantitative ergodic theory proof of Szemerédi's theorem", arXiv:math/0405251 | 13 May 2004 | abstract | yes |
| S3 | Tao, "Arithmetic progressions and the primes — El Escorial lectures", arXiv:math/0411246 (Collect. Math. 2006) | Nov 2004 | arXiv abstract/listing | yes (preprint); harmonic-analysis audience |
| S4 | Host, "Progressions arithmétiques dans les nombres premiers [d'après B. Green et T. Tao]", Sém. Bourbaki exp. 944 | talk Mar 2005; Astérisque 307 (2006); arXiv math/0609795 (Sep 2006) | numdam abstract only (full text not readable) | **talk and seminar text: yes (Bourbaki texts are distributed at the session, March 2005). The printed Astérisque and arXiv versions are dated after the cutoff. I could not confirm the exact date the text was distributed.** |
| S5 | Tao, "Obstructions to uniformity, and arithmetic patterns in the primes", arXiv:math/0505402 | 19 May 2005 | abstract | yes |
| S6 | Green, "Long arithmetic progressions of primes", arXiv:math/0508063 (Gauss–Dirichlet conference) | 2 Aug 2005 | abstract | yes |

Background known to the field before the cutoff (cited from general knowledge; not re-read): Furstenberg 1977
(the correspondence principle and the ergodic proof of Szemerédi), and Host–Kra, "Nonconventional ergodic
averages and nilmanifolds" (Annals 2005; preprint 2002), the characteristic-factor theory.

### Pure Verdict: KNOWN (no Type 1 claim)
Once the vocabulary is stripped away, the article's mathematical content is the Green–Tao theorem and its proof
(S1). Nothing new is asserted. The parallels it promises (Furstenberg correspondence ↔ transference/relative
Szemerédi; structure vs randomness ↔ compact/weak-mixing dichotomy; characteristic factors ↔ Gowers-norm
control and dual functions) are already flagged by the originators themselves. S2 is Tao's explicit
quantitative transcription of the Furstenberg ergodic proof, which the Green–Tao argument uses. S5 is
described in its own abstract as an expository account of a method "motivated by ergodic theory". S4's
abstract says the proof is presented "dans un esprit proche de la théorie ergodique", in the line of
Furstenberg's proof. That is correct and appropriate for an exposition, and it is not a theorem claim.

### Applied Verdict: not evaluated (Type 7 not claimed; no method or algorithm)

### Contribution Type Verdicts (mode=full):
**Type 6 (exposition / translation): UNCLEAR (leaning FAIL under the programme's strict bar)**
- (a) Audience: named, namely ergodic theorists without additive-combinatorics background. PASS.
- (b) Inaccessible literature: S1 is a 50+ page combinatorial and Fourier-analytic paper whose ergodic
  analogies are mostly implicit, so for this audience it is plausibly hard going. But by 2005-10-05 at
  least four expository accounts exist (S3, S4, S5, S6). Two of them, S4 and S5, are pitched explicitly
  along ergodic lines, and S4 is by a leading ergodic theorist (Host, of Host–Kra) for a general audience
  that includes ergodic theorists. S4 is in French, which is not a real barrier for this community. The
  "already accessible" park condition therefore partly bites.
- (c) Non-trivial conceptual work: a systematic dictionary between the combinatorial objects and the
  ergodic ones is real conceptual work, not just a change of notation. One example is matching the
  Gowers-norm/dual-function machinery to characteristic factors and nilsystems, and the transference step
  to a relative correspondence principle. Whether it is *new* work turns on how far S4 and S5 already carry
  out that mapping. I could read only their abstracts, so I cannot settle this.
- **Gap that decides the verdict:** read S4 (the Bourbaki text) and S5 in full, and check whether each
  already pairs the steps of the proof with Furstenberg correspondence, the structure/randomness
  decomposition and characteristic factors. If either does, Type 6 FAILS ("well-explained in Host 2005").
  If neither does, and the seed's dictionary is item by item and more explicit, (b) and (c) pass and Type 6
  CLEARS.

### Cross-reference
No theorem novelty (Pure KNOWN), and none is claimed. The whole contribution rests on Type 6, which in turn
rests on whether it adds something over S4 and S5. Here the components are known, and the value is in the
organisation and in reaching a neighbouring field.

### Recommendation
**Needs deeper audit** (full read of S4 and S5) before proceed or park. If it survives, **redirect to an
expository venue** (Bulletin AMS, Notices, Expositiones), and position it explicitly against Host's
Bourbaki exposé and Tao's expository articles.
Types evaluated: 6 (UNCLEAR). Type 1 KNOWN, but not claimed. Types 2–5 and 7 not claimed.

Bearing on the WHY (one line): this is a translation between two local views of one theorem (the
combinatorial and the ergodic). The puzzle it serves is whether the two pictures compose into one
understanding. It is an example of composition, not of a twist; it does not affect any bar.

### Referee estimate: ACCEPT-LIKELY
Venue class: expository (Bulletin AMS / survey)
Value carried by: factor 4 (it translates a very recent major result for a neighbouring field, ergodic
theory, and adds organisation through an explicit dictionary)
Main risk a referee would raise: overlap with existing expositions that are already framed in ergodic
terms, namely Host's Bourbaki exposé 944 (March 2005) and Tao's "Obstructions to uniformity" (May 2005).
The article must cite them and say what its dictionary adds.
