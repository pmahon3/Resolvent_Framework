## Audit: seed.md, a new short proof of Kneser's conjecture (mode: full)

Audit date (per AS_OF.md): **2002-01-01**. Only works on or before that date count as prior art. The
seed's own text is the submission. Search run on 2026-10-27, WebSearch standard mode.

### Declared contribution type(s): Type 2 (new proof of a known result), Type 6 (exposition / translation)

The seed declares types but states no per-type bar. That is a minor Phase-1 gap. The implied bars are
"shorter than Bárány, no Gale's lemma" for Type 2 and "self-contained for an undergraduate who knows
Borsuk–Ulam" for Type 6.

### What the statement actually is (vocabulary stripped)

- The theorem is χ(KG(n,k)) = n−2k+2, the Kneser conjecture. Lovász proved it in 1978, so this is not a
  Type-1 claim.
- The claimed novelty is a proof route: Bárány's 1978 Borsuk–Ulam / Lyusternik–Schnirelmann (LS)
  argument with Gale's lemma removed.
- The natural reconstruction of such a route, from the auditor's background knowledge, has three steps:
  1. Put n points in general position on S^d with d = n−2k+1, meaning no d+1 of them lie on a
     hyperplane through 0.
  2. Cover S^d by open sets U_i (the hemisphere centred at x contains a k-set of colour i) together with
     one closed leftover set A. That is d+1 sets on S^d.
  3. Use the LS / Borsuk–Ulam form for covers by sets that are each open or closed. If A contained an
     antipodal pair, the great sphere between the two hemispheres would hold at least d+1 of the points,
     which general position forbids.
- The seed text does not show its argument. **It is not verified that the seed's proof is this one.**
  Correctness can only be checked against a full text.

### Pure Verdict: UNCLEAR

The verdict splits into two parts:
- **Theorem:** KNOWN (Lovász 1978). The seed credits it, so the "owner not credited" cap does not apply.
- **Proof route (Gale-free Bárány-type argument):** UNCLEAR, for the reasons below.

**Sources and read levels:**

| Source | Date (pre-cutoff?) | Read level | Bearing |
|---|---|---|---|
| L. Lovász, "Kneser's conjecture, chromatic number, and homotopy," JCTA 25 (1978) 319–324 | 1978, yes | Citation only | Original proof (neighbourhood complex). Different route. |
| I. Bárány, "A short proof of Kneser's conjecture," JCTA 25 (1978) 325–326, doi 10.1016/0097-3165(78)90023-7 | 1978, yes | **Citation and metadata only.** ScienceDirect returned HTTP 403. Content known only from the auditor's background knowledge. | **Nearest prior work.** LS + Gale's lemma, with 2k+d points on S^d and every open hemisphere holding ≥k of them. |
| D. Gale, "Neighboring vertices on a convex polyhedron" (1956) | 1956, yes | Citation only | Gale's lemma. Its standard proof is itself a moment-curve / general-position construction. This matters for the size of the simplification. |
| G. M. Ziegler, "Generalized Kneser coloring theorems with combinatorial proofs," arXiv:math/0103146 | v1 23 Mar 2001, yes | Abstract page only. The PDF did not render. | Records Matoušek's 2000 combinatorial proof and the Dol'nikov, Alon–Frankl–Lovász, Sarkaria and Kriz generalisations. No sign of a Gale-free Bárány proof. |
| J. Matoušek, "A combinatorial proof of Kneser's conjecture," Combinatorica 24 (2004) 163–170 | Received 9 Aug 2000. **Unclear whether a public preprint existed before 2002-01-01.** Ziegler (Mar 2001) cites it, so the content was circulating. | Abstract-level, via search snippets | A self-contained proof through Tucker's lemma. A different route, but it bears on Type 6. |
| Lyusternik–Schnirelmann 1930 / Borsuk 1933, closed and open cover forms | Pre-cutoff | Background knowledge only | The mixed open-or-closed cover form follows from the closed form by shrinking open sets (normality and compactness). An expert would call it folklore-easy. |

**Searches run:**
- Bárány + Gale + hemisphere.
- "Kneser proof general position instead of Gale" (and variants).
- LS theorem with mixed open/closed covers.
- Matoušek combinatorial proof, with dates.
- Ziegler 2001.

**Findings:**
- No source on or before 2002-01-01 gives a Gale-free version of Bárány's proof.
- Hostile reading: the two ingredients are classical and owned. These are LS/Borsuk–Ulam for open or
  closed covers, and general-position point sets, which is how Gale's lemma is proved in the first
  place. An expert might say the proof inlines Gale's construction into one extra dimension. That would
  make it a re-packaging of Bárány, not a new idea.
- Against that reading: one auxiliary lemma really is removed, and no source before the cutoff records
  the observation.

**Why UNCLEAR and not NOVEL (entry-level cap):** the nearest prior work, Bárány 1978, was **not read
beyond citation level**. Its full text could not be retrieved. Lovász 1978 was not read either. A NOVEL
verdict is therefore barred. Unread sources: **Bárány 1978 (primary)**, and Lovász 1978 §§ on
alternative formulations.

Retrieval routes tried on 2026-10-27, all failed:
- the ScienceDirect article page (403);
- the ScienceDirect `/pdf` link (403);
- the doi.org → linkinghub redirect, which returned only a redirect stub;
- the CORE API search (403);
- the Unpaywall API (422).

**Owner status:** no owner was found in print before 2002-01-01. Candidate region to record:
`owned_by` = Bárány 1978 + Gale 1956 + LS 1930 for the ingredients. The assembly (Gale-free) is
residual and unowned as far as was searched.

### Applied Verdict: not evaluated
No Type 7 is claimed, and the seed has no computational content.

### Contribution Type Verdicts (mode=full):

**Type 2 (new proof of a known result): UNCLEAR, leaning PASS on bar (c)**
- (a) A technique applicable elsewhere: weak. Trading "one closed leftover set + general position" for
  a point-configuration lemma is a reusable trick in Borsuk–Ulam proofs, but the seed does not show it
  being used anywhere else.
- (b) An unexpected cross-field connection: no. The topology–combinatorics bridge has been owned by
  Lovász and Bárány since 1978.
- (c) Substantial simplification: plausibly yes. Gale's lemma is the only non-trivial auxiliary in
  Bárány's proof, and removing it leaves Borsuk–Ulam plus one line of linear algebra.
- Hostile counterpoint on size: Bárány's proof is already about one page, and Gale's lemma has a short
  proof. The absolute gain is small.
- What blocks PASS:
  1. The pure audit is UNCLEAR (Bárány not read).
  2. The proof itself is not visible in the seed, so correctness is unverified.

**Type 6 (exposition / translation): FAIL**
- (a) Audience: undergraduates who know Borsuk–Ulam. Named.
- (b) Literature they cannot access: none. Bárány's proof (2 pp., JCTA) plus Gale's lemma is already
  readable by that audience. Matoušek's self-contained combinatorial proof, circulating by 2000–2001 per
  Ziegler, removes even the topology.
- (c) Non-trivial translation work: the self-containment comes from the new proof (a Type 2 matter),
  not from translating any material.
- The programme bar says to park if the literature is already accessible, and it is.

### Cross-reference
- The value, if any, is entirely Type 2: a known theorem and known ingredients, with one auxiliary lemma
  removed.
- Type 6 rides on Type 2 and adds nothing on its own.
- Both verdicts are hostage to two checks: a read of Bárány 1978 at primary level, and sight of the
  actual proof.
- Secondary claim to check: "We point out where the earlier proofs used more than is needed." For
  Bárány this is just the Gale point again. For Lovász it would need a specific claim, and none is
  given.

### Recommendation
**Needs deeper audit**, which is two cheap steps:
1. Obtain the full proof from the seed's author and check it, especially the claim that the dimension
   count makes the closed leftover set antipode-free.
2. Read Bárány 1978 at primary level, and confirm that neither it nor Lovász 1978 remarks that general
   position suffices.

If both checks are clean, the item proceeds under Type 2(c) only, at an expository/short-note venue.
Type 6 parks: the bar failed because the literature is already accessible.

WHY.md line: no bearing on the programme question beyond the general theme of local constraints (the
hemispheres) forcing a global obstruction. It is a lens, not a link.

### Referee estimate: BORDERLINE
Venue class: expository (Amer. Math. Monthly or similar short-note venue)
Value carried by: factor 2 (a markedly shorter, lemma-free proof of a known result); factor 4 secondarily
Main risk a referee would raise: "This is Bárány's proof with Gale's construction absorbed into one extra dimension. Is the saving more than a few lines, and has anyone already remarked that general position suffices?"

**Caps engaged:**
- *Pure UNCLEAR ⇒ at most BORDERLINE.* This engaged, because Bárány 1978, the nearest prior work, could
  not be read beyond citation level.
- *ACCEPT-LIKELY on factor 2 requires the nearest prior work read beyond abstract.* This also engaged
  for the same reason (unread: Bárány 1978).
- Without the caps, the uncapped judgement would lean ACCEPT-LIKELY for the Monthly, given that no
  pre-2002 owner was found.
- The owner-found cap did not engage, since no pre-2002 owner was found.
