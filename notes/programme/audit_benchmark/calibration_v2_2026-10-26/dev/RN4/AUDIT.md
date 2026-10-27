## Audit: seed.md (scattering of n-th roots of unity mod p) (mode: full)

Audit date per AS_OF.md: 2014-10-09. Only sources dated on or before 2014-10-09 are used as prior art.
The seed's own preprint (found in search as arXiv:1410.2913, "Scattered Sets and Roots of Unity in Z/pZ",
all versions) is the submission itself and is ignored. Its arXiv number suggests a posting date of
about 2014-10-10. I could not confirm the exact day, but this does not matter, because it is excluded either way.

### Declared contribution type(s): Type 1 (new theorem). No per-type bar statement is given beyond the type number.

### Pure Verdict: KNOWN (classical; a direct corollary of Wendt 1894 + E. Lehmer 1935)

**Step 1: strip the vocabulary.** "Scatters" means "sum-free". Let H = μ_n(F_p), the subgroup of order n in
F_p^*, with n | p−1. Then H fails to be sum-free ⟺ there are a, b, c ∈ H with a+b=c. Dividing by a, this holds
⟺ there is ζ ∈ H with 1+ζ ∈ H. Taking a=b covers the case 2 ∈ H.

**Step 2: the standard object.** Wendt's binomial circulant determinant is
W_n = det circ(C(n,0), …, C(n,n−1)) = Res_t(t^n − 1, (t+1)^n − 1) = ±∏_{ζ^n=1} ((1+ζ)^n − 1).
For n | p−1, t^n−1 splits into distinct linear factors over F_p, and it is monic, so the resultant reduces
mod p. This gives
  p | W_n ⟺ ∃ ζ ∈ μ_n(F_p) with (1+ζ)^n = 1 ⟺ μ_n(F_p) is NOT sum-free.
⟦HAND, 3 lines; verified against the resultant identity recorded at OEIS A048954⟧

**Step 3: the seed's theorems drop out.**
- *6 | n ⇒ never sum-free.* W_n = 0 exactly when 6 | n (E. Lehmer 1935). The direct reason is a one-liner:
  ω a primitive cube root of unity gives 1+ω = −ω², which lies in μ_6 ⊆ μ_n. Folklore.
- *6 ∤ n ⇒ sum-free for all but finitely many p.* W_n ≠ 0 (Lehmer 1935), so the exceptions are among the
  finitely many prime divisors of W_n. Example: W_3 = 28 = 2²·7, so μ_3 fails only at p=7. W_5 = 11²·31, so
  μ_5 fails exactly at p=11 and p=31.
- *Smallest and largest non-scattering primes* are the smallest and largest prime factors p ≡ 1 (mod n) of W_n.
  Computing and bounding these is an established topic: Fee–Granville 1991 factored W_m for even m ≤ 200,
  Ford–Jha 1993 did related computations, and Frame 1980 found the 2^n−1 factor and the square cofactor.
  The density statement is trivial for fixed n, since the density is 1.
- Classical context: for q = 2kp+1, the Fermat congruence x^p+y^p+z^p ≡ 0 (mod q) has a solution with xyz ≢ 0
  ⟺ q | W_{2k}. This is Wendt's theorem and the Sophie Germain/Legendre condition "no two consecutive p-th
  power residues". The seed's question is exactly this condition, with H the group of p-th power residues. The
  failure when 3 | k was already known to Legendre/Dickson. An equivalent formulation counts the cyclotomic
  number (0,0) of order (p−1)/n being zero (Dickson 1935; Storer, *Cyclotomy and Difference Sets*, 1967), but
  I did not verify that source.

**What an expert would say:** this is "Wendt's determinant / the Sophie Germain condition, restated". Both main
theorems take three lines from the classical results, and the computational part repeats Fee–Granville-type
tables for a related range.

**Sources (read level, date):**
- OEIS A048954 (Wendt's determinant): page read 2026-10-26. It gives the resultant formula, "a(n)=0 iff 6|n", and
  the reference list. The page itself has post-2014 edits. Only the pre-2014 references and the classical
  resultant identity are relied on.
- E. Lehmer, "On a resultant connected with Fermat's last theorem", Bull. AMS 41 (1935) 864–867: NOT read
  (projecteuclid fetch returned empty). The statement "W_n = 0 ⟺ 6|n" is taken via OEIS and a
  search-result summary of Helou 1997.
- E. Wendt, *Arithmetische Studien über den letzten Fermatschen Satz*, 1894: not read. Cited through OEIS and Ribenboim.
- G. Fee, A. Granville, "The prime factors of Wendt's binomial circulant determinant", Math. Comp. 57 (1991)
  839–848: abstract read (via search summary), 2026-10-26.
- J. S. Frame, Fibonacci Quart. 18 (1980) 9–23; D. Ford, V. Jha, Exp. Math. 2 (1993) 113–120; C. Helou, Math. Comp.
  66 (1997) 1341–1346; A. Simalarides, Math. Comp. 71 (2002) 415–427: title/citation level only.
- P. Ribenboim, *13 Lectures on Fermat's Last Theorem* (1979) pp. 61–63; *Fermat's Last Theorem for Amateurs* (1999)
  pp. 126–136: citation level only (via OEIS). This is the textbook home of Wendt's theorem.
- Not used: the 2026 arXiv paper "Multiplicative subgroups of prime fields are not sumsets" and the 2025 Wendt-matrix
  paper, both post-date the audit date.

### Applied Verdict: not evaluated in depth / FAIL as a Type-7 claim
No method is proposed. The computations are factorizations of known determinants, already done (Fee–Granville).
A practitioner would ask "why not just factor W_n?", and the seed has no answer.

### Contribution Type Verdicts (mode=full only):
Type 1 (new theorem): FAIL. Both theorems are trivial consequences of Wendt's resultant identity and Lehmer's
vanishing theorem (Step 2 derivation above). The computational data duplicate known tables of prime factors of W_n.
Types 2–7: not claimed. Checked for completeness:
- Type 2 (new proof): FAIL. The natural proof is the classical one: a norm/resultant argument, with the cube-root
  identity for 6|n.
- Type 4 (vocabulary): FAIL. "Scatters" renames "sum-free" and adds no new statements.
- Type 6 (exposition): FAIL as written. The seed does not mention Wendt or Germain, so it translates nothing.
  A note that framed sum-free multiplicative subgroups through Wendt's determinant could be Monthly-style exposition,
  but Ribenboim already covers this accessibly.

### Cross-reference
The components are known and so is the assembly. The new vocabulary hides the fact that the object is classical.
Nothing survives except possibly larger computational tables, and those are not a contribution type the seed claims.

### Recommendation
PARK. Type 1 was evaluated and fails (KNOWN: Wendt 1894, Lehmer 1935, Fee–Granville 1991); Types 2/4/6 were
checked and fail. Lesson to record: run the stripped statement "1+ζ ∈ μ_n mod p" through resultant and Fermat-congruence
vocabulary before claiming anything.

Bearing on WHY.md (one line): small local relations (1+ζ=η) decide a global property of the subgroup. That is a
circle already closed by classical cyclotomy, and it offers no new composition.

### Referee estimate: REJECT-LIKELY
Venue class: none (at most a short note or expository piece, if rewritten to credit Wendt/Lehmer)
Value carried by: none. Factor 1 fails because the theorems are in print. Factor 4 is possible only with a full
rewrite that credits the classical literature.
Main risk a referee would raise: "This is Wendt's determinant / the Sophie Germain condition. Your theorem is Lehmer
1935 plus the resultant identity, and none of it is cited."
