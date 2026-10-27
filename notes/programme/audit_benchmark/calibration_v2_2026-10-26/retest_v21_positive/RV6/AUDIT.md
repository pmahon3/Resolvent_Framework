## Audit: seed.md, an exposition of the Green–Tao theorem from an ergodic-theory point of view (mode: full)

**Audit date (AS_OF.md):** 2005-10-05. Only works dated on or before 2005-10-05 count as prior art. The submission itself is not prior art. Excluded as post-dating: Tao math/0512114 (Dec 2005), the Bourbaki volume's print date (Astérisque 307, 2006), journal versions from 2006–2008, and Conlon–Fox–Zhao (2014).
**Search date:** 2026-10-27 (WebSearch/WebFetch, standard mode).
**Read-level caveat:** every source below was read through WebFetch model summaries of the ar5iv HTML, not by direct reading of the PDF. Read levels are stated per source.
**WHY.md:** not in the audit directory, so I give no bearing on it.

### Declared contribution type(s): Type 6 (exposition / translation)

The seed declares the type but does **not** state the per-type bars it commits to clearing, which the framework's Phase 1 requires. The seed is a four-sentence abstract, not a full text.

### Pure Verdict: KNOWN (by design; Type 1 is not claimed)

**Routing.** The pure check is treated as a theorem-novelty check, following skill step 1 ("what is the actual mathematical statement?"). Any overlap with earlier *expositions* is assessed under Type 6(b) and under the referee's duplication clause, not here.

- **Mathematical statement:** the primes contain arbitrarily long arithmetic progressions. Owner: Green–Tao, "The primes contain arbitrarily long arithmetic progressions", arXiv math/0404188v1 (8 Apr 2004).
  - Read level: abstract only. The abs page now shows v6 (2007); I relied only on the v1 date and the abstract.
- **Credit.** The seed credits the theorem to Green and Tao by name. It claims no new theorem, so no uncredited owner exists.
- **Ergodic parallels as content.** The parallels themselves (structure versus randomness, energy increment as an analogue of Furstenberg's structure theorem, Gowers norms against Host–Kra seminorms) are already stated in print by Tao (May 2005) and Host (March 2005); see below. They are known motivation, not new statements.

### Applied Verdict: not evaluated (no Type 7 claim; no method or computation)

### Contribution Type Verdicts (mode=full):

**Type 6 (Exposition / translation): UNCLEAR**

- **(a) Target audience: PASS.** The seed names it: ergodic theorists who do not know additive combinatorics.

- **(b) Literature the audience cannot currently access: PARTLY UNDERCUT.** Pre-2005-10-05 expositions:
  1. **Green–Tao, math/0404188v1 (Apr 2004).** Written in combinatorial and Fourier language. Read level: abstract only.
  2. **Tao, "Arithmetic progressions and the primes – El Escorial lectures", math/0411246 (11 Nov 2004).**
     - Fourier- and uniformity-based, aimed at analysts and additive combinatorialists.
     - §5 mentions an "ergodic perspective" only in passing.
     - Read level: §1–6 at body-summary level. **§7 ("Szemerédi strategy"), the ergodic-flavoured part, was unread.**
  3. **Tao, "Obstructions to uniformity, and arithmetic patterns in the primes", math/0505402 (19 May 2005).**
     - Explicitly "motivated by ergodic theory". §6, "Ergodic obstructions to uniformity", gives a partial dictionary:
       - weak mixing ≈ Gowers uniformity;
       - almost-periodic functions as the obstructions;
       - a structure decomposition "in the spirit of Furstenberg's structure theorem";
       - the energy increment;
       - Host–Kra and Bergelson–Host–Kra nilsequences as the ergodic input.
     - It states that **no direct correspondence principle links the ergodic and the finitary results**.
     - It is aimed at number theorists: it assumes the von Mangoldt function, Siegel–Walfisz and the circle method.
     - It does not mention the Furstenberg correspondence or characteristic factors.
     - Read level: §1–7, body skim.
  4. **Green, "Long arithmetic progressions of primes", math/0508063 (Aug 2005).**
     - For a general mathematical audience; harmonic-analytic and combinatorial.
     - Ergodic theory appears only in attributions: Furstenberg's spirit, Furstenberg–Weiss on quadratic phenomena, and the Host–Kra origin of "soft obstructions" in §8.
     - No correspondence principle, no characteristic factors, no weak-mixing/compact framing.
     - Read level: section titles plus body summary.
  5. **B. Host, "Progressions arithmétiques dans les nombres premiers [d'après B. Green et T. Tao]", Séminaire Bourbaki exposé no. 944, dated March 2005.** This is the nearest neighbour.
     - Written in French by an ergodic theorist.
     - It follows the proof's structure: pseudorandom weights, Gowers norms, σ-algebras on Z_N, dual functions, a recursion.
     - It addresses ergodic theorists directly: "Les ergodiciens reconnaîtront la façon dont les « facteurs » interviennent".
     - It names the Furstenberg correspondence principle and calls the role of the Host–Kra seminorms "très proche" to that of the Gowers norms.
     - It does **not** name characteristic factors as an organising concept.
     - Read level: section-level and passage summary.
     - **Date flag:** I saw its content only through the arXiv version math/0609795 (Sept 2006, after the audit date) and assumed it matches the March 2005 seminar text. Print publication was 2006. I could not confirm independently that the 2005 text was publicly distributed before 2005-10-05 (Bourbaki texts are normally handed out at the session).

  **Net for (b).** No English exposition existed that is *organised by ergodic concept* (correspondence principle, structure/randomness, characteristic factors) for ergodic theorists. But the audience is not cut off:
  - Host gives a proof-ordered walkthrough with explicit asides to ergodic theorists, in French, which that community largely reads.
  - Tao §6 already supplies a partial dictionary.

  The literature is therefore partly, not fully, accessible.

- **(c) Non-trivial conceptual work: CANNOT BE ASSESSED.**
  - In principle the translation is non-trivial. The correspondence principle has no direct finitary counterpart (Tao 2005 says so), so mapping it onto the transference/pseudorandom-measure step, and mapping characteristic factors onto Gowers-norm-controlled σ-algebras and dual functions, would take real conceptual work.
  - A four-sentence abstract does not show whether the text does this or only lists analogies. The "pattern-coincidence" failure mode cannot be ruled out without the full text.

**Undeclared types:** none implied beyond Type 6. Types 1–5 and 7 are not claimed.

### Cross-reference

- The content is known by design (Type 1 not claimed; pure KNOWN, credited).
- Everything rests on Type 6. Its bar is half-met: (a) passes, (b) is partly undercut by Host 2005 and Tao 2005 §6, and (c) is unverifiable from the seed.
- The differentiators that would carry (b) and (c):
  - written in English;
  - organised by ergodic concept rather than by proof step;
  - characteristic factors and the correspondence principle made the organising spine, where Host only alludes to "facteurs" and Tao §6 denies a direct correspondence.

### Recommendation

**Needs deeper audit.** Do not proceed and do not park.
- Get the full text.
- Check that the ergodic parallels are worked translations (for each parallel: what is transferred, and where the analogy breaks), not a list of resemblances.
- Require explicit differentiation from Host (Bourbaki 944, March 2005) and Tao (math/0505402 §6), and citation of both.
- The seed must also add its per-type bar commitments (Phase 1).
- If the full text only restates Tao §6 and Host in English, Type 6 FAILS and the seed parks (types evaluated: 6; bar failed: (b)/(c)).

### Referee estimate: ACCEPT-LIKELY
Venue class: expository (Bulletin AMS-type survey)
Value carried by: factor 4. It translates a fresh (2004) result for a neighbouring field, ergodic theory. Under the referee standard the original's accessibility does not disqualify it; what counts is the added reach and organisation.
Added value over Host, in one line: an English, concept-organised dictionary (correspondence principle, structure/randomness, characteristic factors) for ergodic theorists, where Host is a French, proof-ordered seminar report with occasional asides.
Main risk a referee would raise: Tao (May 2005) states that no direct correspondence principle connects the ergodic and finitary settings. A referee will ask whether the "Furstenberg correspondence" parallel is a real translation or only an analogy, and will require that Host 2005 and Tao 2005 be cited and differentiated.

**Caps:**
- UNCLEAR-pure cap: **not engaged**. The pure verdict is KNOWN-by-design under the routing stated above. Had Host been treated as a partial owner under Pure, the verdict would be UNCLEAR and the estimate capped at BORDERLINE.
- Read-beyond-abstract cap: **not applicable**. It governs factors 1 and 2 only; the value here is factor 4.
- Uncredited-owner cap: **not engaged**. The theorem is credited to Green–Tao and no prior exposition owns this framing.

The referee estimate does not change the programme verdict (Type 6 UNCLEAR, needs deeper audit).
