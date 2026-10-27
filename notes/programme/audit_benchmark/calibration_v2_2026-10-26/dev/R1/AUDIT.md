## Audit: seed.md (mode: full)

Audit date per AS_OF.md: **2023-02-13**. Only sources on or before that date count as prior art. The seed's own work, under any title, is ignored.

### Declared contribution type(s): Type 6 (exposition), Type 2 (new proof)
The seed declares types but does not state the per-type bars it commits to clearing (the Phase 1 requirement). It also makes a claim it does not declare: the A+A+A improvement is a **Type 1** claim (see below).

### Pure Verdict: KNOWN (headline bound). The A+A+A corollary is UNCLEAR.
**Stripped statement.** If A ⊆ {1,…,N} has no nontrivial 3-AP, then |A| ≤ N·exp(−c(log N)^{1/12}).

**Owner.** Z. Kelley and R. Meka, "Strong bounds for 3-progressions", arXiv:2302.05537, v1 submitted 2023-02-10, three days before the audit date. Read level: abstract and v1 abs page fetched (2026-10-26). I also read part of the v5 HTML (stamped 2024-01-05), only to see how the paper is organised; nothing from v5 is used as prior art. The abstract states the bound as 2^{−O((log N)^β)}. The value β = 1/12 is attested only by secondary sources (talk slides, later citations). I did not verify it in v1 itself (snippet level). The seed credits the source ("We follow the main ideas of the known approach"), so the headline result is KNOWN and credited, not a hidden overlap.

**Context.** Before KM, the best bound was N/(log N)^{1+c} (Bloom–Sisask 2020, as reported in the KM abstract). The Behrend lower bound exp(−c(log N)^{1/2})N shows that the KM form is the right shape. KM handle the finite-field case first "partially for expository reasons". They describe the integer case, using spreadness substitutes such as Bohr sets or GAPs, as having "additional complications" (v5 HTML, partial read, used for structure only).

**A+A+A corollary.**
- The previous bounds for long APs in A+A+A, at abstract or survey-snippet level and not checked in the originals:
  - Freiman–Halberstam–Ruzsa (1992): length about N^{cα³}.
  - Green (2002): exponent about α^{2+o(1)}.
  - Sanders (2006–08, arXiv math/0605520): N^{cα} for α ≫ (log log N/log N)^{1/2}.
  - Henriot (2014, arXiv:1408.2568): small-doubling extensions.
- KM v1 proves a finite-field 3A result (Cor. 1.12: A′+A′+A′ is an affine subspace, answering Schoen–Sisask). In the part I read, I found no integer statement about long APs in A+A+A.
- So the integer A+A+A improvement appears new as of 2023-02-13. It is probably a fairly direct consequence of the KM almost-periodicity / Bohr-set machinery plus a standard Bohr-set-to-AP step. Whether an expert would call it "immediate given KM" cannot be settled without the seed's actual statement and bound: **UNCLEAR**.

**Could not date-check.** I found no other exposition of KM dated 2023-02-10 to 2023-02-13. Given the three-day window, none is likely.

### Applied Verdict: not evaluated (pure mathematics; no Type 7 claim)

### Contribution Type Verdicts (mode=full):

**Type 6 (Exposition / translation): UNCLEAR, leaning PASS if the bars are written down**

(a) **Audience.** The seed does not name one. The natural audience is analytic number theorists and additive combinatorialists who work in the Bohr-set density-increment tradition (Bourgain, Sanders, Bloom, Bloom–Sisask). The KM paper is written in TCS-flavoured language: spreadness, sifting, dependent random choice, Hölder lifting.

(b) **Inaccessible literature.** This is the weak point under the programme's strict bar. KM is a public arXiv preprint, and its integer section is written out. The case that it is "inaccessible" is about prerequisite depth and framing, not access:
- it is three days old;
- it is not yet refereed;
- the integer argument is presented as an adaptation of the finite-field one with "additional complications".

Under the programme's rule ("park if the existing literature is already accessible to the target audience"), this is contestable.

(c) **Non-trivial conceptual work.** Being self-contained and simplifying the Bohr-set arguments would count as non-trivial work, more than a notation change, because the Bohr-set regularity and size bookkeeping is exactly where integer-case density-increment arguments carry their technical weight. The seed asserts this but does not demonstrate it.

**Verdict.** UNCLEAR. The bar can be cleared, but the seed has not yet shown (a)–(c).

**Type 2 (New proof of known result): FAIL as stated**
- Bar: (a) a new technique, (b) an unexpected connection, or (c) a substantial simplification.
- The seed says it "follow[s] the main ideas of the known approach". That makes it the same proof, re-presented, so (a) and (b) are excluded by the seed's own words.
- (c) holds only if the Bohr-set simplifications are *substantial*. "Simplify some arguments" describes local streamlining, not a different or markedly shorter proof.
- Under the programme bar this is "different but not more revealing" unless shown otherwise. FAIL, with a reopen condition: a demonstrated large reduction in length or technicality of the integer case would move this to Type 6 territory anyway, not to Type 2.

**Undeclared Type 1 (new theorem: long APs in A+A+A): UNCLEAR**
- The claim is plausibly new as of 2023-02-13 (see the Pure Verdict).
- It needs to be declared, stated exactly, compared against Sanders, Green and Henriot by theorem number, and checked for whether it follows in a few lines from the KM integer machinery.

### Cross-reference
- The headline theorem is known and credited to KM (three days old).
- The value lies in the exposition and simplification (Type 6), not in a new proof (Type 2).
- The one possibly novel mathematical item is the A+A+A corollary, which the seed has not declared as Type 1.
- So: "known core, exposition-carried, with a small new-theorem rider."
- The programme's Type 6 bar (b) is stricter than community practice. It penalises re-expositions of public preprints even when the preprint is days old and written for a different community.

### Recommendation
**Needs deeper audit. Proceed to Phase 3 only, scoped to Type 6, once the seed:**
1. names the audience (number theorists working with Bohr sets);
2. states concretely which KM integer-case steps are simplified, and how;
3. declares the A+A+A result as Type 1, with an exact statement and comparison to Sanders (2006–08) and Henriot (2014).

Type 2 is parked as FAIL (same proof, local simplifications). Evaluated: Types 6, 2 and undeclared Type 1. Failed bar: Type 2 (no technique, no connection, simplification not shown to be substantial). Unresolved: Type 6 (b)/(c) and Type 1.

Bearing on WHY.md: none direct. This is additive combinatorics. At most it is a lens on how local Fourier/Bohr structure forces global progressions, with no stated bridge.

### Referee estimate: ACCEPT-LIKELY
Venue class: research journal (number theory or combinatorics; a fast, self-contained treatment of a breakthrough is routinely accepted)
Value carried by: factor 4 (a cleaner self-contained route to a fresh result, for the same experts), with factor 1 (the improved A+A+A bound) as support
Main risk a referee would raise: whether the treatment adds enough beyond KM's own integer section, and whether the A+A+A improvement is stated and proved correctly with the β = 1/12 dependence tracked.

### Sources (all accessed 2026-10-26)
- Kelley–Meka, arXiv:2302.05537 v1 abs page (submitted 2023-02-10). Abstract read. https://arxiv.org/abs/2302.05537v1
- Kelley–Meka, v5 HTML (2024-01-05; postdates the audit date, used only to see how the paper is organised, not as prior art). Partial read (first 100k characters). https://arxiv.org/html/2302.05537v5
- KM talk slides (Simons, 2023-08; postdates the audit date, used only to corroborate β = 1/12). Snippet. https://simons.berkeley.edu/sites/default/files/2023-08/3-Progressions-Presentation.pdf
- Sanders, arXiv:math/0605520 (2006). Snippet. https://arxiv.org/pdf/math/0605520v1
- Henriot, arXiv:1408.2568 (2014). Snippet. https://arxiv.org/pdf/1408.2568
- Freiman–Halberstam–Ruzsa (1992) and Green (2002): cited via the Sanders and Henriot snippets; not read.
