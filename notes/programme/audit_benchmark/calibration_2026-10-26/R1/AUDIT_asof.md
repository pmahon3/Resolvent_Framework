## Audit: seed.md (self-contained treatment of the exp(-c(log N)^{1/12}) Roth bound; Bohr-set simplifications; long APs in A+A+A) (mode: full)

**Audit date (as-of): 2023-02-13.** Only sources dated on or before 2023-02-13 are used as prior art. The seed's own text (under any title/author) is treated as the submission and excluded. Searches run 2026-10-26; read levels marked per source.

### Declared contribution type(s): Type 6 (exposition), Type 2 (new proof of known result)
Undeclared but present: a **Type 1** claim (improved lower bounds for long APs in A+A+A). Noted per skill rule ("if the seed claims types it did not declare, note this"). The seed declares types but does not state the per-type bars it commits to clearing.

### Pure Verdict: KNOWN (main bound). UNCLEAR, narrow margin (A+A+A corollary)

**Stripped statement.** (i) If A ⊆ {1,…,N} has no nontrivial 3AP, then |A| ≤ N·exp(−c(log N)^{1/12}). (ii) The same machinery gives longer APs in A+A+A for dense A than were previously known.

**(i) KNOWN.** Kelley–Meka, "Strong Bounds for 3-Progressions", arXiv:2302.05537v1, submitted **2023-02-10**, three days before the audit date.
- Thm 1.1: if A ⊆ [N] has density δ and no nontrivial 3AP, then δ ≤ 2^{−Ω((log N)^β)} for some absolute β > 0.
- Thm 1.2 (restated as Thm 6.1): density ≥ 2^{−d} gives ≥ 2^{−O(d^{11})}N² solutions of x+y=2z.
- This forces a nontrivial 3AP unless log N ≤ O(d^{11}). Hence 3AP-free implies δ ≤ 2^{−c(log N)^{1/11}}.
- That is *stronger* than the seed's exponent 1/12.

[Read level: abstract page in full; v1 HTML full text via a text-extraction tool, in two passes covering 162k/162k characters. d^{11} was read consistently in Thm 1.2 and Thm 6.1. Not cross-checked against the PDF typesetting.]

So the seed's theorem (i) is KM's theorem, re-derived with a slightly *weaker* explicit exponent.

The integer setting is not new either. KM v1 already argues the integer case with Bohr sets and GAPs:
- §6: integer overview.
- §7: GAPs, Bohr sets and their properties, translation invariance for approximate subgroups, Freiman homomorphisms.
- §8: density increment and configurations.
- App. C: Sanders' invariance lemma and the Croot–Sisask lemma.

The seed's own content is a *simplification* of those Bohr-set arguments.

**(ii) UNCLEAR, narrow margin.**
- Schoen–Sisask, "Roth's theorem for four variables and additive structures in sums of sparse sets", arXiv:1408.2568, **2014-08-11** (Forum Math. Sigma 2016). [abstract, full]
  - It already proves that A+A+A contains long APs for A ⊆ [N] of density as low as exp(−c(log N)^{1/7}).
  - That threshold is *sparser* than the seed's exp(−c(log N)^{1/12}).
  - So the quasi-polynomial density regime for long APs in 3A was owned before 2023.
- KM v1: no integer A+A+A or long-AP corollary in the full text. There is an F_q^n corollary only (Cor. 1.12: A'+A'+A' contains an affine subspace).
- Earlier chain [snippet level, via search summary and the comparison table in 1408.2568]:
  - Freiman–Halberstam–Ruzsa (1992): length N^{cα³}.
  - Green, GAFA 12 (2002): N^{cα^{2+o(1)}}.
  - Sanders, Math. Proc. Camb. Phil. Soc. 144 (2008): N^{cα^{1+o(1)}}.
  - Henriot, "On arithmetic progressions in A+B+C", arXiv:1211.4917 (2012).
- The seed's "improve lower bounds" must therefore be an improvement in the *length* of the AP, or in the length–density trade-off inside the regime Schoen–Sisask already reach. It cannot be an extension into a new density regime.
- Whether that gain is a routine substitution of a KM-type almost-periodicity input into the Schoen–Sisask argument could not be decided from the seed. No pre-cutoff source with the exact improved bound was found.

**Expert "obvious?" test.**
- (i): yes, it is KM.
- (ii): an expert would expect it once KM exists. Schoen–Sisask supplies the template.

### Applied Verdict: not evaluated (no Type 7 claim; pure mathematics).

### Contribution Type Verdicts (mode=full):

**Type 6 (Exposition / translation): UNCLEAR, leaning FAIL on bar (b).**
- (a) *Audience:* additive combinatorialists in the integer Bohr-set tradition (Bourgain, Sanders, Bloom–Sisask).
- (b) *Inaccessible literature:* the only source is KM arXiv:2302.05537v1, three days old.
  - The bar asks for an access barrier: language, prerequisite depth, or scattered sources. None holds.
  - KM is public and written for this same expert audience.
  - Its integer argument is already in Bohr-set and GAP language (§§6–8).
  - "Sole, new and long" is not an access barrier. The "already accessible" kill condition is close to firing.
  - Not "well-explained in a textbook", because nothing secondary exists yet. But the primary source is itself accessible to the named audience.
- (c) *Non-trivial conceptual work:* plausible if the simplifications substantively restructure the Bohr-set steps. Unverifiable from the seed.
- A self-contained exposition of a brand-new breakthrough has real value at an expository venue. Under this framework, though, Type 6 clears only if (b) is rescued, e.g. a different audience such as non-specialists or students.

**Type 2 (New proof of known result): UNCLEAR, leaning FAIL.**
- (c) *Simplification:* claimed only as "simplify some arguments involving Bohr sets". The reported exponent 1/12 is weaker than KM v1's implicit 1/11. The simplification costs quantitative strength, and the seed shows no other measurable gain (length, parameters, fewer lemmas).
- (a) *Technique applicable elsewhere:* the A+A+A application is the only evidence. But KM's technique transfers by itself, and Schoen–Sisask 2014 already supplies the sumset template. The seed must show its own Bohr-set reworking is what makes the transfer go through.
- (b) *Unexpected connection:* none claimed.
- The FAIL condition ("alternative route with no gain") is likely unless the seed exhibits a concrete simplification.

**Type 1 (New theorem, undeclared): UNCLEAR.** The bound in (i) is KNOWN: Kelley–Meka 2023-02-10, Thms 1.1–1.2. The A+A+A length improvement in (ii) may be new, but within a density regime Schoen–Sisask 2014 already owns. It should be declared and audited separately.

### Cross-reference
- The headline theorem is owned outright by Kelley–Meka, three days earlier, with a slightly better exponent as read.
- The Bohr-set integer setting is already in KM.
- The quasi-polynomial regime for long APs in A+A+A is already in Schoen–Sisask 2014.
- What remains is an exposition of a fresh but accessible result (Type 6 weak on bar (b)), a simplification without demonstrated gain (Type 2 weak on (c)), and a quantitative A+A+A corollary (an undeclared Type 1 candidate, narrow margin).
- Known components, re-packaged, plus one plausibly new quantitative corollary.

### Recommendation
**Needs deeper audit. Do not proceed under the declared types as stated. If pursued, redirect to an expository venue or rescope to the A+A+A corollary as Type 1.** Before any Phase 3:
1. Declare (ii) as Type 1. State the exact length/density bound and compare it at full-text level with Schoen–Sisask 2014 (arXiv:1408.2568) and Henriot (arXiv:1211.4917).
2. For Type 2, name which KM integer steps (§7.4, §8.2–8.3) are replaced and what is concretely gained.
3. Drop the exponent 1/12 as a selling point. KM v1 Thm 1.2 implies 1/11 as read.
4. For Type 6, name an audience for whom KM is genuinely inaccessible, or the bar fails.

Evaluated: Types 6 and 2 (declared) and Type 1 (undeclared). No bar is cleared outright.

**Most damaging prior source:** Kelley & Meka, *Strong Bounds for 3-Progressions*, arXiv:2302.05537v1, 2023-02-10, Thms 1.1–1.2 (the integer Bohr-set proof in §§6–8). Second: Schoen–Sisask, arXiv:1408.2568 (2014-08-11), long APs in A+A+A down to density exp(−c(log N)^{1/7}).

**Dating uncertainties:** KM v1 date is 2023-02-10 (arXiv abstract page, read in full). Later KM versions (v2–v5) postdate the audit and were not used. Schoen–Sisask v1 date 2014-08-11 from the arXiv abstract page; Henriot arXiv:1211.4917 (2012, from the identifier), Sanders 2008, Green 2002 and FHR 1992 dates from search snippets. Background works (Bourgain 1999, Sanders 2011, Bloom 2016, Bloom–Sisask 2020, Tao–Vu 2006) were not fetched and are not load-bearing. No source used was of uncertain date relative to 2023-02-13.

**WHY line:** A purely internal additive-combinatorics result. Its only bearing on the programme's question (local views → one world) is methodological: almost-periodicity as a local-to-global density-increment engine. No direct link.
