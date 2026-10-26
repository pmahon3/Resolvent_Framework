## Audit: seed.md (mode: full)

### Declared contribution type(s): Type 1 (new theorem), Type 2 (new proof of known result)

Types are declared, but the seed does not state the per-type bars it commits to clearing (the framework requires them). Declaring Type 2 is also inconsistent: the twin prime conjecture (TPC) is not a known result, so there is nothing for a "new proof" to re-prove.

### Pure Verdict: KNOWN (method) / claimed theorem NOT ESTABLISHED. Fatal correctness failure.

**Stripped statement.** "Use a Rasiowa–Sikorski (R–S) generic filter on a countable Boolean algebra of arithmetic sentences to build a model of PA. Conclude that TPC holds in the standard model N." The companion claim is the same with "infinitely many Mersenne primes".

**Status of the conclusions.** Both are famous open problems.
- TPC: the best unconditional bound is H₁ ≤ 246 (Polymath8b, building on Zhang and Maynard). H₁ = 2 is TPC, and it is not proved. Source: Polymath, "The 'bounded gaps between primes' Polymath project — a retrospective", arXiv:1409.8361 [snippet/abstract]. Also Polymath, "Variants of the Selberg sieve…", arXiv:1407.4897, main theorem H₁ ≤ 246 [snippet]. A Sept. 2026 preprint claims H₁ ≤ 236 [snippet, unverified]. None of these claims H₁ = 2.
- Infinitude of Mersenne primes: open. It is conjectured via Lenstra–Pomerance–Wagstaff heuristics. Source: Wikipedia, "Mersenne prime" [snippet]; t5k.org "Heuristics Model for the Distribution of Mersennes" [snippet].

**Method status: KNOWN, classical.** Rasiowa–Sikorski (Fund. Math. 37, 1950) proved the completeness theorem algebraically. Their argument takes an ultrafilter on the Lindenbaum algebra that preserves countably many infinitary joins (the quantifier sups), and builds a term/Henkin model from it. [Not re-read this session; the classical attribution is confirmed by the topology.lmf.cnrs.fr blog post on the R–S lemma, snippet.] The lemma itself, in the dense-set form, is in Kunen, *Set Theory* (1980), Lemma VII.2.3, and Jech, *Set Theory* (3rd ed.), Lemma 14.4 [standard textbook statements, not re-read this session]. See also arXiv:2008.07460 and arXiv:2604.05554 Lemma 2.13 [snippet].

**Why the argument cannot work.** These are hand checks. Each one is fatal on its own.

1. **R–S cannot decide sentences that PA leaves undecided.** Let B be the Lindenbaum algebra of PA. A generic filter G meets the given countable family of dense sets. It yields a complete consistent T ⊇ PA and a model M with M ⊨ φ iff [φ] ∈ G. Suppose PA does not decide TP. Then [TP] ≠ 0 and [¬TP] ≠ 0, and R–S can start below either one: some generic G contains [TP] and some generic G′ contains [¬TP]. So "forcing the statement" only shows that TP is *consistent* with PA. It says nothing about truth. TP gets Boolean value 1, so that every generic contains it, iff PA ⊢ TP. Showing that is exactly the open problem, so the method assumes what it has to prove.

2. **"Standard model" is unjustified, and once you assume it the method becomes idle.** A Henkin/R–S model of PA is in general nonstandard. Nothing in the construction certifies that it is isomorphic to N. If M ≅ N, then Th(M) is True Arithmetic, which is fixed in advance. Then "M ⊨ TP" is the same statement as "N ⊨ TP", and the generic filter added nothing. Choosing a filter with [TP] ∈ G and then declaring M standard is circular. It also might be false: if TP fails in N, that filter gives a nonstandard model.

3. **Forcing cannot change arithmetic truth.** ω is absolute between transitive models of ZFC, so every first-order arithmetic sentence has the same truth value in V and in any forcing extension V[G]. Shoenfield absoluteness (Σ¹₂/Π¹₂) covers much more than this. Source: Wikipedia, "Absoluteness (logic)" [snippet]; Jech Thm 25.20 / Kunen [textbook, not re-read]. So TP is forced by 1 iff it is true in V. Any valid forcing proof of TP could be converted into an ordinary ZFC proof. Forcing gives no leverage on Π₂ number theory. That is precisely why it is used only for independence results about statements that are *not* absolute.

4. **The twin case and the Mersenne case look exactly alike to the method.** The same "method" would just as well "force" ¬TP, or "only finitely many Mersenne primes", by starting from the complementary condition. A method that proves a sentence and its negation proves nothing.

**Hostile-referee summary.** Strip the vocabulary and the content is: "the completeness theorem via R–S, plus the open conjecture, assumed through the choice of filter and the label 'standard model'." An expert in logic would reject this immediately. The method is known (1950). The conclusion is not proved.

### Applied Verdict: not evaluated (no applied/methodology claim; Type 7 not declared; no computational component)

### Contribution Type Verdicts (mode=full only):

**Type 1 (New theorem): FAIL.** The bar asks for a previously unknown true statement *with proof*. The statement (TPC) is not known to be true, and the proof is invalid by checks 1–3 above: it certifies at most consistency with PA, not truth in N. The only novel element is the conclusion, and that element is unsupported. The companion Mersenne claim fails the same way.

**Type 2 (New proof of known result): FAIL.** There is no known result to re-prove: TPC is open. If one reads Type 2 generously as "a new proof of the completeness theorem via R–S", that proof *is* Rasiowa–Sikorski 1950, the textbook route. It offers (a) no new technique, (b) no new connection (the logic and Boolean-algebra link is the 1950 paper's), and (c) no simplification.

Undeclared types: none plausibly applies. It is not Type 5 (no impossibility shown), not Type 6 (the R–S completeness proof is in Rasiowa–Sikorski, *The Mathematics of Metamathematics*, 1963, and in standard texts), and not Type 3 or 4.

### Cross-reference
The method is known and the claimed theorem is false-as-proved. No assembly is left to evaluate. The failure is a correctness failure, not a novelty miss: the argument confuses "consistent with PA" (what a generic filter delivers) with "true in N" (what was claimed). Arithmetic absoluteness also rules out any forcing route to Π₂ statements about N.

**Bearing on WHY.md:** none. The seed's only structural content (local conditions → one global filter/model) is the classical R–S/Baire picture, and here it is misused: local consistency is read as global truth. That is a hidden idealisation, specifically the unearned word "standard".

### Recommendation
**PARK (kill).** Types evaluated: 1, 2 (both FAIL); 7 not claimed. Bars failed: Type 1, no valid proof of the claimed statement; Type 2, no known result, and the method is Rasiowa–Sikorski 1950 verbatim. **Not an open question** under the framework's criterion (b): TPC and the Mersenne infinitude problem are already posed everywhere. Do not proceed to Phase 3.

### Sources and read levels
- Polymath, arXiv:1409.8361 (retrospective) — snippet/abstract
- Polymath, arXiv:1407.4897 (H₁ ≤ 246) — snippet
- Song–Yue eprint 2026 (claims H₁ ≤ 236) — snippet, unverified
- Wikipedia, "Mersenne prime"; t5k.org Mersenne heuristics — snippet
- Wikipedia, "Absoluteness (logic)" (Shoenfield) — snippet
- Rasiowa–Sikorski, Fund. Math. 37 (1950); *The Mathematics of Metamathematics* (1963) — not read this session (classical attribution; corroborated by topology.lmf.cnrs.fr post, snippet)
- Kunen, *Set Theory* (1980) Lemma VII.2.3; Jech, *Set Theory* 3rd ed., Lemma 14.4, Thm 25.20 — textbook, not re-read this session
- arXiv:2008.07460; arXiv:2604.05554 Lemma 2.13 (R–S lemma statement/proof) — snippet
