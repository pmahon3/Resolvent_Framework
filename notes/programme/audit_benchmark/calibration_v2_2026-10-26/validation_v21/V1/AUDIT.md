## Audit: seed.md, "covering numbers s(k,n) of k-th powers mod n" (mode: full)

Audit date per AS_OF.md: **2016-09-06**. Sources after that date, and any version, withdrawal notice or comment on the seed's own work, are excluded as prior art. One post-date source (Demiroğlu Karabulut, arXiv:1709.04428, 2017) was used **only as a pointer** to locate pre-2016 citations. It is not cited as prior art. The arXiv record 1609.02090 (posted 2016-09-07) matches the seed's text, so it was treated as the submission itself, and its withdrawal comment was ignored.

### Declared contribution type(s): Type 1 (new theorem), Type 2 (new proof)
Undeclared claim: "We regard the covering numbers as the main new object" is a Type 4 (vocabulary) claim. The seed does not declare Type 4, so it is evaluated below for completeness and flagged.

### Pure Verdict: KNOWN
**Stripped statement.** Here s(k,n) is the least s such that every residue mod n is a sum of s k-th powers. The seed computes s(k,n) for all n and k ≤ 10 by three steps: reduce to prime powers with CRT, lift with Hensel, and run a finite check at small primes.

**Owner.** The object is Waring's number modulo n, g(k,n). It is classical, and its determination is in print:
- **C. Small, "Waring's problem mod n", Amer. Math. Monthly 84 (1977), no. 1, 12–25.** It poses exactly this problem and solves it completely for k = 2, 3. Per a secondary pointer, Small later observed that the same techniques solve it for all k. *Read level: bibliographic record plus secondary description; full text not read (checked 2026-10-26).*
- **C. Small, "Sums of powers in arithmetic progressions", Canad. Math. Bull. 21(4) (1978), 505–506.** Its extract defines g(k,n) as "the smallest r with the property that every integer is a sum of r kth powers mod n". It says the function was studied in the author's earlier papers, and it identifies max_n g(k,n) with Hardy–Littlewood's Γ(k). *Read level: publisher extract plus reference list (checked 2026-10-26).*
- **G. H. Hardy, J. E. Littlewood, "Some problems of 'Partitio Numerorum' (VIII): The number Γ(k) in Waring's problem", Proc. London Math. Soc. (2) 28 (1928), 518–542.** It is the p-adic/Hensel analysis of local solvability of x₁^k+…+x_s^k ≡ N (mod p^m) for all prime powers. *Read level: bibliographic only (checked 2026-10-26).* Caveat: Γ(k) carries a primitivity (unit-variable) condition, so it is not literally max_n g(k,n). Small's 1978 note supplies the identification.
- The method, CRT then Hensel lifting then a finite check at p | k or small p, is the standard route to local solvability in Waring's problem (Hardy–Littlewood; textbook singular-series treatments). Experts would call it routine.

**"New object" claim.** It fails. "Covering number s(k,n)" is g(k,n) under a new name.

**Application (Erdős–Falconer over Z_n^d).** The nearest prior work is Covert–Iosevich–Pakianathan, "Geometric configurations in the ring of integers modulo p^ℓ", Indiana Univ. Math. J. 61 (2012); arXiv:1105.5373 (2011). It gives distance-set thresholds in Z_{p^ℓ}^d. Covert's later work extends it to Z_n^d for odd n. *Read level: abstract and secondary summaries (checked 2026-10-26).* Feeding a known Waring number into such a threshold looks like a corollary. The seed gives no bound, so I could not assess whether it improves on these.

**Correctness.** The text gives no explicit values, so I could not check its claims. Two points need care. Published tables of g(k,n) have had errors at specific moduli, so any table for k ≤ 10 must be checked against Small. The case p | k, where Hensel needs higher congruences (p = 2 with k even, p = 3 with k = 3, 6, 9, p = 5 with k = 5, 10, p = 7 with k = 7), is where a "finite check" can silently fail. No error was found, but nothing was verified.

### Applied Verdict: not evaluated (no methodology claim; Type 7 not declared)

### Contribution Type Verdicts (mode=full):
**Type 1 (new theorem): FAIL.** The determination of g(k,n) is Small (1977), building on Hardy–Littlewood (1928). Restricting to k ≤ 10 is weaker than the "all k" solution Small reports. The seed cites neither. Bar: "not known, not folklore". Not met.

**Type 2 (new proof): FAIL.** CRT reduction plus Hensel lifting plus a finite check is the established route. It is Small's elementary technique and the Hardy–Littlewood local analysis.
- (a) No new technique transfers elsewhere.
- (b) No new cross-field connection: the Erdős–Falconer use is an application, not a proof connection.
- (c) It is not a substantial simplification. A table limited to k ≤ 10 is narrower, not simpler.

**Type 4 (vocabulary; undeclared): FAIL.** "Covering numbers" rename Waring's number mod n. No statement is offered that the standard g(k,n) vocabulary cannot state. This is failure mode #2 (rediscovery as synthesis).

### Cross-reference
The components are known and the assembly is known. The only possible residue is the Z_n^d distance bound. It would need a stated bound shown to beat Covert–Iosevich–Pakianathan-type thresholds, and the seed offers none.

### Recommendation
**Park.** Types 1, 2 and 4 (undeclared) were evaluated, and all failed:
- Type 1: known (Small 1977; Hardy–Littlewood 1928).
- Type 2: standard route with no gain.
- Type 4: renaming.

The Erdős–Falconer application could re-enter only as its own seed: an explicit bound for Z_n^d, compared against Covert–Iosevich–Pakianathan (2012) and Covert's Z_n^d extension.

**Why (one line):** this bears on WHY.md's local-to-global question only as a textbook case of composition. Local (p-adic) solvability glues by CRT with no obstruction, so no loop and no hidden idealisation. It is not a seam.

### Referee estimate: REJECT-LIKELY
Venue class: none (at best a short note, only if recast with full credit to Small and a new Z_n^d bound)
Value carried by: none. Factor 1 is owned by Small 1977. Factor 2 is the standard CRT+Hensel route. Factor 3 is renaming.
Main risk a referee would raise: "This is Waring's problem mod n, solved by Small (Amer. Math. Monthly 1977), with Γ(k) by Hardy–Littlewood (1928). Neither is cited, and the 'new object' is g(k,n) renamed."
Cap applied: the owner of the main result is found in print and not credited, and no clearly substantial residual is exhibited. The distance-set application is stated without a bound. Read-level caveat: Small 1977 and Hardy–Littlewood 1928 were not read in full text. The identification rests on Small's 1978 CMB extract (primary) and secondary pointers. A full-text read would refine the "all k" claim, but it cannot rescue the object, which the 1978 note defines verbatim.
