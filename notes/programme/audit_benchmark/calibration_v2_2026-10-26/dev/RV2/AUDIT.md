## Audit: seed.md — "A Gale-free short proof of Kneser's conjecture via Borsuk–Ulam" (mode: full)

**Audit date (AS_OF.md): 2002-01-01.** Only works existing on or before that date count as prior art. The seed's own work, under any title, is the submission and is not treated as prior art. Every source dated after 2002-01-01 was ignored, including secondary sources that mention the seed's own route. Web searches run 2026-10-26 (standard mode). Secondary sources from after 2002 were used **only** to confirm the bibliographic data of pre-2002 works, never as prior art.

**Limitation of the target.** The seed is a 5-sentence abstract. It contains **no proof**: it does not say which version of Borsuk–Ulam is used or what the "few short steps" are. Every verdict below that depends on the argument is therefore conditional on the full text.

### Declared contribution type(s): Type 2 (new proof of known result), Type 6 (exposition/translation)
The seed declares its types. It does not state the per-type bars it commits to clearing, which the framework requires ("The per-type bars I commit to clearing: …"). This is a minor readiness defect.

### Pure Verdict: KNOWN (theorem); the proof's novelty is UNCLEAR
- The statement χ(KG(n,k)) = n−2k+2 is **known**:
  - Lovász, *J. Combin. Theory Ser. A* 25 (1978) 319–324 (lower bound via the neighbourhood complex and Borsuk–Ulam). Read level: bibliographic/secondary. Date 1978.
  - The upper bound n−2k+2 is Kneser's elementary colouring (Kneser 1955, *Jber. DMV* 58). Read level: bibliographic. Date 1955.
- Type 1 is not claimed, which is correct.

Prior proofs a hostile referee would set against the seed's novelty and simplification claims:
1. **Bárány**, "A short proof of Kneser's conjecture", *JCTA* 25 (1978) 325–326. It derives the result from Borsuk–Ulam (Lyusternik–Shnirelmann form) plus Gale's lemma (2k+d points on S^d with every open hemisphere containing ≥k of them). This is the proof the seed improves on. Read level: secondary descriptions (MathWorld; survey descriptions), date 1978 confirmed. Primary text not fetched.
2. **Dol'nikov** (Sibirsk. Mat. Zh., 1988; earlier Yaroslavl collection 1981). It proves χ(KG(F)) ≥ cd₂(F) (colourability defect) by a geometric Borsuk–Ulam argument. For F = all k-subsets of [n], cd₂ = n−2k+2 is **trivial**, so Kneser follows **without Gale's lemma**. This is the most dangerous prior art for "avoids Gale's lemma". Whether Dol'nikov's own argument is as short and elementary as the seed's could not be settled: it is in Russian and I read it only through secondary descriptions. Date 1988 (some sources say 1981; one says 1993). The year is uncertain, but every candidate date is before 2002.
3. **Kříž** (1992; Trans. AMS per memory, venue not confirmed by search) gives the same cd₂ bound by box complexes. That is heavier machinery and not a short route. Read level: bibliographic via Ziegler 2001.
4. **Matoušek**, "A combinatorial proof of Kneser's conjecture". Received by *Combinatorica* 9 Aug 2000. KAM-DIMATIA preprint series 2000-460 (URL found, PDF not readable in this sandbox). It goes via Tucker's lemma and is fully combinatorial. This is a different direction (it removes topology rather than Gale), but it is a competing "elementary" proof that must be cited. Date: 2000 preprint, so it predates the audit date.
5. **Ziegler**, "Generalized Kneser coloring theorems with combinatorial proofs", arXiv:math/0103146, submitted 23 Mar 2001 (Invent. Math. 2002). It gives combinatorial proofs of Kneser, Dol'nikov, Alon–Frankl–Lovász, Sarkaria, Kříž and Schrijver. Read level: abstract. The arXiv date predates the audit date.
6. **Sarkaria**, "A generalized Kneser conjecture", *JCTB* 49 (1990). Read level: bibliographic.
7. Borsuk–Ulam equivalents: Bacon, "Equivalent formulations of the Borsuk–Ulam theorem", *Canad. J. Math.* 18 (1966), which shows the open-cover and closed-cover Lyusternik–Shnirelmann forms are equivalent. Read level: secondary mention. Date 1966. If the seed's "version of Borsuk–Ulam" is a covering form with some sets open and some closed, I found no pre-2002 statement of that mixed form (search 2026-10-26, negative). The mixed form would then be a small new lemma, easy to derive from the open/closed forms. It should be proved in the paper, not assumed.

Hostile summary: the theorem is known. The specific route (Borsuk–Ulam, no Gale, a handful of steps) is **not found stated in print before 2002-01-01**. However, it is close to Dol'nikov's cd₂ argument specialised to complete k-uniform families. Settling that requires reading Dol'nikov 1981/1988 in the primary source.

### Applied Verdict: not evaluated (no applied or methodological claim; Type 7 not claimed)

### Contribution Type Verdicts (mode=full)

**Type 2 (new proof of known result): UNCLEAR, a conditional PASS on (c) only**
- (a) A technique applicable elsewhere: not demonstrated in the seed. A general-position-on-the-sphere argument replacing Gale might transfer to Dol'nikov-type cd₂ bounds or to Schrijver graphs, but the seed claims nothing of this.
- (b) An unexpected cross-field connection: **no**. The Borsuk–Ulam ↔ Kneser connection is Lovász/Bárány 1978.
- (c) Substantial simplification: **plausible but unverified**. Bárány's proof is already about 2 pages. Removing Gale's lemma removes the one non-obvious construction (moment-curve or Gale-transform points), so the proof becomes self-contained given Borsuk–Ulam. That is a real but modest simplification of an already short proof. It clears (c) only if (i) the full text substantiates "a few short steps" with no hidden lemma of comparable weight (for example an unproved mixed open/closed covering lemma), and (ii) the paper shows the gain over Dol'nikov's Gale-free cd₂ route specialised to Kneser.
- Programme bar: "different but not better" would FAIL. The bar cannot be judged from an abstract.

**Type 6 (exposition/translation): FAIL**
- (a) Audience: named, "an undergraduate who knows Borsuk–Ulam".
- (b) Inaccessible literature: **not shown**. Bárány 1978 is two pages in English in *JCTA*. Gale's lemma is a short explicit construction. Lovász's proof is the harder one, but Bárány already bypasses it. The literature is accessible to that audience.
- (c) Non-trivial conceptual translation: none. The work is mathematical (removing a lemma), not translation. Any value it has is carried by Type 2(c), not Type 6. Claiming both types double-counts one contribution, which the framework's "one contribution per paper" rule cautions against.
- The sentence "We also point out where the earlier proofs used more than is needed" is a commentary claim. It is unverifiable without the text.

### Cross-reference
The result is known. Neither component (Borsuk–Ulam, the Kneser reduction) is new. The only candidate contribution is a **shorter, Gale-free route**, and that sits entirely under Type 2(c). Type 6 adds nothing independent. The Pure "UNCLEAR" on the route and the Type 2 "UNCLEAR" share one gap: comparison with Dol'nikov's cd₂ argument (Gale-free, pre-2002) and verification of the actual steps.

### Recommendation
**Needs deeper audit, then proceed scoped to Type 2 only if it survives.** Required before Phase 3:
1. Obtain the full proof. Check every step, in particular which Borsuk–Ulam form is used and whether a mixed open/closed covering form is proved.
2. Read Dol'nikov (1981/1988) in the primary source, and state precisely how the seed's route differs from it, specialised to Kneser.
3. Cite Matoušek (2000 preprint), Ziegler (arXiv 2001), Kříž, Sarkaria, Bacon.
4. Drop the Type 6 claim. It FAILS; the bars evaluated were Type 2 (a)/(b)/(c) and Type 6 (a)–(c).

Bearing on WHY.md (one line): none directly. A proof that local hemisphere data force a global colouring obstruction is a classic "local views cannot add up" topology argument, but the item is a re-proof and adds no new lens.

### Referee estimate: ACCEPT-LIKELY
Venue class: expository / short-note (Amer. Math. Monthly-type, or a short note in a combinatorics journal)
Value carried by: factor 2 (markedly shorter, more self-contained proof of a known theorem: Borsuk–Ulam alone, no Gale), with factor 4 as secondary (undergraduate accessibility)
Main risk a referee would raise: whether the Gale-free reduction is already implicit in Dol'nikov's colourability-defect proof (and how it compares with Matoušek's 2000 combinatorial proof). Also, the abstract gives no steps, so the "few short steps" and "earlier proofs used more than needed" claims must be substantiated and credited.

---
**Sources (searched 2026-10-26; pre-2002 works only as prior art):**
- MathWorld, Kneser's Conjecture (bibliographic data for Lovász 1978, Bárány 1978): https://mathworld.wolfram.com/KnesersConjecture.html (secondary)
- Ziegler, arXiv:math/0103146 (23 Mar 2001), abstract: https://arxiv.org/abs/math/0103146
- Matoušek, KAM-DIMATIA preprint 2000-460: https://kam.mff.cuni.cz/kamserie/clanky/2000/s460.pdf (URL located; content unreadable here; received date 9 Aug 2000 per the Combinatorica record)
- Dol'nikov cd₂ bound and Kříž: secondary descriptions found via search (post-2002 surveys, used only to confirm the pre-2002 attribution and statement)
- Lusternik–Schnirelmann open/closed forms and their equivalence (Bacon 1966): https://en.wikipedia.org/wiki/Lusternik%E2%80%93Schnirelmann_theorem and secondary mentions
- Date uncertainty: Dol'nikov's year (1981 / 1988 / 1993 across sources). All candidates predate 2002-01-01. Kříž's venue was not confirmed.
