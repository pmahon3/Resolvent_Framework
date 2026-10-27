## Audit: seed.md (non-congruent numbers with all prime factors ≡ 3 mod 8, via an F₂ Legendre matrix) (mode: full)

Audit date (per AS_OF.md): **2012-12-01**. Only sources on or before this date count as prior art.

**Excluded as the submission itself:** arXiv:1212.0196, "On non-congruent numbers with 3 modulo 8 prime factors". Searches surfaced it. Its title and content match the seed, and its ID dates it to Dec 2012. It was not read and is not used.

**Excluded as post-date:**
- the Reinholz–Spearman–Yang papers (Colloq. Math. 2015; Funct. Approx. 2018; Rend. Padova 2022);
- the Reinholz thesis (UBC 2019);
- arXiv 2604.23482, 2604.23450, 2604.26183, 2210.01678, 2105.01450, 2005.02385.

Search snippets from these sources described Iskra's theorem and Monsky's matrix. **None of that is used as evidence here.** Where the content of a pre-date work is stated below, its read level is given honestly.

**Date-ambiguity points:**
1. ar5iv reported the date of arXiv:0706.4344 (Rhoades) as "August 8, 2026". That is the render date. The arXiv ID places the paper in June 2007, so it is pre-date.
2. No other ambiguity affects the verdict.

WHY.md is not in the audit directory, so the why-line is n/a. In one line: a local-to-global (2-descent / Selmer) rank-zero criterion, with no bearing on the bars.

### Declared contribution type(s): Type 1 (new theorem). No per-type bar is stated; the seed only names the type.

### Pure Verdict: KNOWN. The headline family is owned (Iskra 1996), and the general criterion is a trivial consequence of Monsky's 1994 formula ⟦HAND⟧.

**1. What the seed actually states, with vocabulary stripped.** Let m = p₁⋯p_t be squarefree with every p_i ≡ 3 (mod 8). Let A ∈ M_t(F₂) be the usual Legendre-symbol matrix: off-diagonal a_ij = 1 iff (p_j/p_i) = −1, with the diagonal chosen so that row sums vanish. Then:

- (a) If A² + A + I is invertible over F₂, then Sel₂(E_m) is minimal, so rk E_m(Q) = 0 and m is non-congruent.
- (b) The "in particular" clause: all pairwise Legendre symbols equal 1 ⟹ m is non-congruent.
- (c) An analogue holds for 2m when t is even.
- (d) Examples: 3, 11, 83, 107.

**2. Owners found.**

- **Iskra, B., "Non-congruent numbers with arbitrarily many prime factors congruent to 3 modulo 8", Proc. Japan Acad. Ser. A 72 (1996) 168–169, DOI 10.3792/pjaa.72.168.**
  - Read level: bibliographic record only, via search results on 2026-10-26. The Project Euclid landing page and PDF, and the J-STAGE page, all returned empty or errored.
  - The theorem as recalled (from memory, not from a primary read): if p_i ≡ 3 (mod 8) and (p_j/p_i) = −1 for all j < i, then p₁⋯p_t is non-congruent. The proof is by 2-descent.
  - The paper's title alone already states the seed's headline claim: an infinite family, with arbitrarily many prime factors, all ≡ 3 mod 8, non-congruent.
  - Seed clause (b) is Iskra's theorem. The seed asks for all symbols to be 1 under an ordering; Iskra asks for all to be −1 under the reverse ordering. By quadratic reciprocity for primes ≡ 3 (mod 4), (p/q) = −(q/p), so reversing the order turns one condition into the other.
- **Monsky, P., Appendix to D. R. Heath-Brown, "The size of Selmer groups for the congruent number problem II", Invent. Math. 118 (1994) 331–370.**
  - Read level: not read. The EuDML search returned nothing, and post-date secondaries were excluded.
  - The matrix form below is **from memory**. It is consistent with the 2007 pre-date secondary (Rhoades, arXiv:0706.4344, read via ar5iv on 2026-10-26). That source confirms only that Monsky computes the 2-Selmer rank as an F₂-rank of a larger matrix; it does not give the form.
  - For odd n = p₁⋯p_t: s(n) = 2t − rank_{F₂} M, with M = [[A + D₂, D₂], [D₂, A + D₋₂]], where D_ℓ = diag([(ℓ/p_i) = −1]).
- **Genocchi (1855):** primes p ≡ 3 (mod 8) are non-congruent. This is classical, textbook-level, recalled from memory. Seed item (d) consists of single primes, all covered by Genocchi. None of the examples exercises the multi-prime criterion.
- **Related pre-date work in the same method family**, which owns neither (a) nor (b):
  - Feng, Acta Arith. 75 (1996) 71–83, odd graphs. Read level: bibliographic record plus description in Ouyang–Zhang.
  - Li–Tian, 2000, primes ≡ 1 mod 8.
  - Ouyang–Zhang, arXiv:1208.2149 (v1 10 Aug 2012, pre-date), primes ≡ 1 mod 4. Read via ar5iv on 2026-10-26, intro and §4 level. It contains no 3 mod 8 criterion and does not mention Iskra or Monsky.
  - Lemmermeyer, Acta Arith. 110 (2003) / math/0202311 (2002), primes ≡ 1 mod 8. Abstract read on 2026-10-26.

**3. Clause (a) is a three-line consequence of Monsky ⟦HAND; Monsky's matrix form from memory⟧.**

1. For p ≡ 3 (mod 8): (2/p) = −1, so D₂ = I. Also (−2/p) = (−1/p)(2/p) = (−1)(−1) = +1, so D₋₂ = 0.
2. Hence M = [[A + I, I], [I, A]].
3. Row-reduce using the identity block: rank M = t + rank((A + I)A − I) = t + rank(A² + A + I), since −I = I in characteristic 2.
4. So s(m) = t − rank(A² + A + I). In particular s(m) = 0 iff A² + A + I is invertible. Here s(m) is the 2-Selmer rank beyond torsion, so s(m) = 0 gives rank zero.

This is exactly the seed's criterion. An expert in this area (Heath-Brown, Monsky, Swinnerton-Dyer, Kane, Xiong–Zaharescu) would call it an immediate specialisation of Monsky's formula.

**4. Clause (b) checked against (a) ⟦HAND⟧.**
- Under the ordered reading, A is strictly triangular off the diagonal, up to the diagonal fill.
- Then A² + A + I is triangular with diagonal entries a² + a + 1 = 1 over F₂ (true for a = 0 and a = 1).
- So it is invertible, and (b) follows from (a). Correct.

**5. Clause (c), the 2m case.**
- The requirement that t be even is forced by Monsky's parity rule:
  - if t is odd, 2m ≡ 6 (mod 8), so s is odd and s ≥ 1, and no such criterion can hold;
  - if t is even, m ≡ 1 (mod 8) and 2m ≡ 2 (mod 8), so s is even.
  - So the restriction is consistent.
- The even-n Monsky matrix involves Aᵀ. By reciprocity, Aᵀ = A + (J + I) + diagonal correction for primes ≡ 3 mod 4. It is therefore not obvious that the same polynomial appears.
- **⟦HAND — unverified⟧.** This is the only candidate residual. It too is a mechanical specialisation of Monsky's even matrix, but I have not derived it.

**6. Searched:**
- Iskra; the Monsky matrix and 2-Selmer rank; Feng's odd graphs; Lemmermeyer; Reinholz–Spearman–Yang (all post-date, excluded); Li–Tian; Ouyang–Zhang 2012.
- Under "non-congruent", "Selmer rank zero", "Legendre symbol matrix F₂", "primes 3 mod 8".
- Textbooks were not opened (Koblitz, *Introduction to Elliptic Curves and Modular Forms*, Ch. I covers Genocchi-type cases; recalled only).

**Correctness problem: statement precision.**
- Taken literally (unordered pairs), "all pairwise Legendre symbols equal 1" is **impossible for t ≥ 2**, because (p/q)(q/p) = −1 for p, q ≡ 3 (mod 4). Read that way, clause (b) is vacuous beyond t = 1.
- The ordered reading, (p_i/p_j) = 1 for i < j, is correct and equals Iskra's condition.
- This is a precision flaw, not a mathematical error. A referee would require the fix.

### Applied Verdict: FAIL (not applicable)
- Practitioner test: "Why not just compute the F₂-rank of Monsky's 2t×2t matrix directly?" The seed's criterion only halves the matrix size: a t×t determinant instead of 2t×2t.
- There is no computational comparison and no regime analysis.
- This is not a methodology contribution.

### Contribution Type Verdicts (mode=full only):

**Type 1 (new theorem): FAIL.**
- Bar: not known, not folklore, not a trivial consequence, and the proof non-routine.
- The headline family and clause (b) are Iskra 1996. The t = 1 case is Genocchi.
- The general criterion (a) is a three-line specialisation of Monsky 1994 (derivation in §3). If the seed's proof runs a full 2-descent instead, that proof is routine (Iskra's method).
- The possible residual (c), the 2m case with t even, is ⟦unverified⟧ and is also expected to be a Monsky specialisation.
- Caveat on read levels: neither owner's primary text was read. Iskra's statement and Monsky's matrix form are from memory, and the §3 derivation is ⟦HAND⟧.

**Undeclared types implicitly claimed:** none. One could argue Type 2 (a new proof of Iskra via the matrix). It fails the bar because the route is a direct specialisation of Monsky's formula, which already exists. It brings no new technique, no cross-field connection, and no substantial simplification over Monsky plus linear algebra.

### Cross-reference
- Correct mathematics, known components, and an assembly that is a mechanical specialisation.
- The only content not owned outright is (i) the clean polynomial form A² + A + I (immediate from Monsky) and (ii) the 2m family (unverified, likely also immediate).
- The seed credits neither Iskra nor Monsky. As a six-sentence abstract, that absence is weak evidence of non-crediting, but a submission would have to credit both.

### Recommendation
**Park.** The only type evaluated was Type 1 (declared), plus Type 2 implicitly; both fail. The Type 1 bar fails on "known (Iskra 1996) / trivial consequence (Monsky 1994)", and the Type 2 bar fails on "no technique, connection or simplification gain".

If revived, the questions are:
- Does the 2m case with t even give a criterion not visible from Monsky's even matrix in a few lines?
- Do the families outside Iskra's (A non-triangular, A² + A + I invertible) have density or structure worth a theorem?

Either would need a primary read of Monsky's appendix and of Iskra first.

### Referee estimate: REJECT-LIKELY
Venue class: short-note or letters at most. That would require repositioning: credit Iskra and Monsky, frame the result as a Monsky-matrix corollary with explicit new families, and fix the "all pairwise symbols equal 1" wording.
Value carried by: none clearly. Factor 1 (new statement) is limited to the families beyond Iskra and the 2m case. These are correct, but each is a near-immediate specialisation of Monsky's formula.
Main risk a referee would raise: the criterion is immediate from Monsky's 2t×2t matrix (D₂ = I, D₋₂ = 0 gives s = t − rank(A² + A + I)), and the headline family and the "in particular" corollary are Iskra (1996), uncredited.

(The caps were applied as follows. The pure verdict is KNOWN, so the UNCLEAR cap does not bind. An owner of the main result was found and is uncredited in the seed, and no clearly substantial residual is verified, so the rule gives REJECT-LIKELY. If the primary texts of Monsky or Iskra differ from the recalled forms, the verdict reopens and the estimate would cap at BORDERLINE.)
