## Audit: seed.md, prescribed diagonal in the similarity class of a non-scalar matrix (mode: full)

Audit date (per AS_OF.md): **2012-07-02**. Sources were consulted on 2026-10-26. Only works dated on or before 2012-07-02 count as prior art. Later works are used **only as pointers** to what an earlier work contains, and are never cited as owners.

**Excluded.** arXiv:1207.0631 (C. de Seguins Pazzis, "On the diagonal of the matrices in a similarity class", v1 submitted 3 July 2012; abstract-level metadata only). It matches the seed and is dated after the audit date, so it is treated as the submission itself. Its attributions (Mirsky for R/C, Djoković for arbitrary fields) were seen only in a search snippet and are not used as evidence.

### Declared contribution type(s): Type 1 (new theorem), Type 2 (new proof)

The seed declares the types but states no per-type bar. That is a minor procedural gap.

### Pure Verdict: KNOWN (owner: Fillmore 1969, read at secondary level)

**Stripped statement.** Let K be any field and A ∈ M_n(K) non-scalar. Then (d_1,…,d_n) ∈ K^n is the diagonal of some matrix similar to A iff Σd_i = tr A. Necessity is trivial, so the content is sufficiency.

**Owner.** P. A. Fillmore, "On similarity and the diagonal of a matrix", *Amer. Math. Monthly* 76(2) (1969) 167–169.
- *Date confirmed.* Crossref metadata, read 2026-10-26.
- *Read level: secondary.* The primary text returned 403 from Taylor & Francis, and zbMATH also returned 403. Three later works independently restate Fillmore's theorem with the same scope. They are used only as pointers to the content of the 1969 paper:
  - Borobia, arXiv:1704.08037 (2017), read in full via ar5iv: "Let A be a nonscalar matrix of order n over a field F … γ_1+…+γ_n = tr A. Then there is a matrix similar to A with diagonal (γ_1,…,γ_n)."
  - Stasinski, arXiv:2502.11636 (2025), read in full via ar5iv: "any non-scalar matrix A ∈ M_n(K) over a field K". No characteristic restriction is mentioned.
  - Julio–Soto, arXiv:1804.05738 (2018), snippet only: it states Fillmore's theorem over a field F.
- *Proof route.* Per Borobia's description, Fillmore inducts on n using a vector x with x and Ax independent (that is, x is not an eigenvector). He takes the basis {x, Ax − γx, …} to place γ on the diagonal, then passes to the complementary block. This is the seed's route.

**Residual uncertainty.** One pointer (Julio–Soto 2018, snippet) says the special case diag(tr A, 0, …, 0) was "proved independently by Fillmore for complex numbers, and Gibson for an arbitrary field". That leaves a small chance that Fillmore's original is restricted (for example to C, or with a characteristic caveat). The seed's only distinguishing phrase, "no restriction on the characteristic", would then carry some residual. Against this, the two fuller restatements both quote Fillmore's theorem over an arbitrary field F. This does not reach UNCLEAR, but the primary text is unread, and an editor would need to check its first page.

**Partial owners before the audit date:**
- **Mirsky**, "Matrices with prescribed characteristic roots and diagonal elements", *J. London Math. Soc.* 33 (1958) 14–21. Citation level only, read 2026-10-26. Over C, it covers prescribed eigenvalues plus diagonal. That determines the similarity class only for non-derogatory A.
- **D. Ž. Djoković**, arXiv:1206.3744, v1 17 June 2012, before the audit date; abstract read 2026-10-26. It extends Mirsky to any field, with a companion-type solution. This owns the seed's separately treated **cyclic/companion case**. It does not own the derogatory case, where an equal characteristic polynomial does not imply similarity.
- **P. M. Gibson**, "Matrix commutators over an algebraically closed field", *Proc. AMS* 52 (1975) 30–32. Abstract read 2026-10-26; the PDF returned 403. A pointer says its Theorem 1 gives the (tr A, 0, …, 0) special case over arbitrary fields. Not verified.
- **Folklore.** The zero-diagonal special case, used in the Shoda / Albert–Muckenhoupt (1957) "trace zero ⇒ commutator" arguments, is classical. This was recalled from memory and not re-read here.

**Expert reaction.** "This is Fillmore's theorem (Monthly 1969)." Standard linear algebra; the answer is KNOWN.

### Applied Verdict: not evaluated (no Type 7 claim; pure linear algebra)

### Contribution Type Verdicts (mode=full):

**Type 1 (new theorem): FAIL.** The statement is Fillmore 1969, as stated over an arbitrary field per three consistent restatements. The "iff" adds only the trivial necessity, and the cyclic case is also owned by Djoković (June 2012). No strengthening of hypothesis or conclusion is visible in the seed.

**Type 2 (new proof): FAIL.** The bar is (a) a new technique, (b) a cross-field connection, or (c) a substantial simplification.
- The sketched route is the one attributed to Fillmore: induction on n via a non-eigenvector x, adjusting one diagonal entry, then a complementary block.
- Splitting off the companion case is a case organisation, not a new technique.
- Characteristic-freeness is a scope point, belonging to Type 1 if anything, not a proof-method gain.
- The seed is only a sketch, so no simplification can be demonstrated against Fillmore's three-page proof.

**Undeclared types.** None are implied.

**Correctness.** No error found at sketch level. The non-scalar hypothesis is necessary (a scalar A = cI only has diagonal (c,…,c)), and necessity is correct. A small-case spot check over GF(2), n = 2: [[0,1],[0,0]] is similar to [[1,1],[1,1]], so the diagonal (1,1) is attained with sum 0 = tr. The delicate step is keeping the complementary block non-scalar, which is why companion or small-field cases need care. The sketch is **unverifiable in detail**: the inductive step and the companion case are asserted, not written out.

### Cross-reference

The theorem and the proof route are both owned, Fillmore 1969 (secondary read). The only possible residual is the explicit characteristic-free scope. That holds only if Fillmore's original turns out to be restricted, and the evidence points against it. Djoković (2012-06-17) independently owns the companion sub-case over any field. No type bar clears.

**WHY.md line.** WHY.md is not in this directory. The item is classical matrix theory and has no bearing on the local-to-global question beyond being a "local data (diagonal) to global object (similarity class)" rhyme. That rhyme is not a contribution.

### Recommendation

**Park.**
- Types evaluated: 1 (FAIL, known: Fillmore 1969) and 2 (FAIL, same route as Fillmore).
- If revived, credit Fillmore 1969, Mirsky 1958 and Djoković 2012. Then show either (i) that Fillmore's original carries a characteristic or field restriction the seed removes (read the primary first), or (ii) a demonstrably shorter or more structural proof. Neither is currently shown.

### Referee estimate: REJECT-LIKELY
Venue class: short-note or letters (at most), otherwise none
Value carried by: none. Factor 2 is not shown, because the route matches Fillmore's. Factor 1 survives only if Fillmore's original is restricted, which is unconfirmed (primary unread).
Main risk a referee would raise: the main result and its proof are Fillmore's theorem (Amer. Math. Monthly 1969), uncredited; the companion case is also in Djoković (arXiv June 2012).

The "owner in print, not credited" cap applies. A clearly substantial residual would lift it, and none is exhibited.
