## Audit: seed.md (Butson-type Hadamard matrices, condition n ∈ p₁ℕ + … + p_sℕ) (mode: full)

### Declared contribution type(s): Type 1 (new theorem)

The seed states its type but not a per-type bar it commits to clearing. That is a minor readiness defect. It does not affect the verdict.

### Pure Verdict: KNOWN. Stated explicitly, for every s, in Lam–Leung (2000). The derivation is a two-line consequence.

**Stripped statement.** Let H be an n×n complex Hadamard matrix (HH* = nI) whose entries are l-th roots of unity (a Butson matrix BH(n,l)), and let l = p₁^{a₁}⋯p_s^{a_s}. Then n = Σ tᵢpᵢ with every tᵢ ∈ ℤ≥0.

**Three-line derivation from a known theorem.**
1. Take rows 1 and 2 of H. Orthogonality gives Σⱼ h₁ⱼ·conj(h₂ⱼ) = 0.
2. Each term of that sum is an l-th root of unity, so it is a vanishing sum of n l-th roots of unity.
3. By Lam–Leung, a vanishing sum of n m-th roots of unity exists **iff** n ∈ ℕp₁ + … + ℕp_s. This holds for **all** s, not only s ≤ 3.

Therefore:
- the seed's "theorem" (s = 2, 3) is a trivial consequence of Lam–Leung;
- its conjecture (s ≥ 4) is already a theorem;
- its "classical fact" (s = 1) is the prime-power case of the same result.

**Sources (read level marked):**
- **[Most damaging] T. Y. Lam and K. H. Leung, "On vanishing sums of roots of unity", J. Algebra 224(1) (2000), 91–109, MR1736695.**
  - Main theorem: W(m) = ℕp₁ + … + ℕp_r.
  - Read level: **abstract** (MSRI preprint 1995-082 abstract page). The bibliographic data come from the reference list of Winterhof–Yayla–Ziegler.
- **T. Banica and J.-M. Schlenker, "On Hadamard matrices at roots of unity", arXiv:0707.4175.**
  - Read level: **abstract page / withdrawal notice**. The withdrawn v1 text was not read.
  - The seed is, nearly word for word, the abstract of v1 (27 Jul 2007), as reported by a search snippet. v1 proved s = 2, 3 and conjectured s ≥ 4.
  - The authors **withdrew** the paper on 13 Dec 2007. Their stated reason: "the main result being known since Lam and Leung, J. Algebra 2000." The seed's own authors therefore conceded the kill.
- **A. Winterhof, O. Yayla and V. Ziegler, "Non-existence of some nearly perfect sequences, near Butson-Hadamard matrices, and near conference matrices", arXiv:1407.6548.**
  - Prop. 2.1 restates Lam–Leung. Cor. 2.2 applies it to BH-type matrices by exactly the row-orthogonality argument above.
  - Read level: **full text, §2 only** (ar5iv).
- **Secondary confirmations: search snippets only.**
  - Szöllősi, thesis, arXiv:1110.5590: attributes the iff criterion to Lam–Leung.
  - Schmidt, "BH Constructions" notes (NTU): states the same criterion.
- **Other obstructions the seed "comments on"**, such as de Launey's and Winterhof's conditions: these are explicitly prior art, the seed claims nothing about them, and they were not audited. A search snippet mentions them.

**Hostile checks.**
- *Is it a restatement?* Yes. It is the special case of Lam–Leung where the vanishing sum comes from two orthogonal rows.
- *Would an expert say "obvious"?* Yes, given Lam–Leung. The withdrawal notice is direct evidence of this.
- *Is any residue left?* None. The converse direction (existence of BH(n,l) for admissible n) is not claimed, and in any case it is false in general (for example, BH(6,6) obstructions and the de Launey conditions). So no open-question salvage arises from the stated content.

### Applied Verdict: not evaluated
The seed makes no Type 7 claim. Mode = full evaluates the declared types.

### Contribution Type Verdicts:

**Type 1 (new theorem): FAIL.** The statement is known: Lam–Leung 2000, main theorem, all s. It is also a trivial consequence: a two-step reduction via the orthogonality of two rows. The bar ("not known, not folklore, not a trivial consequence; non-routine proof") fails on every clause.

**Undeclared types, checked so the outcome is not chosen by type selection.** None of the following is claimed, and none would pass.
- **Type 2:** a partial (s ≤ 3) proof of a theorem known for all s gives no technique gain on the evidence available.
- **Type 5:** the obstruction is classical.
- **Type 6:** the material is already accessible. Szöllősi's thesis and the Winterhof et al. §2 both present it.

### Cross-reference
- There are no novel components and no novel assembly.
- The seed's entire content (s = 2, 3 theorem; s ≥ 4 conjecture) collapses into one prior theorem.
- Bearing on WHY.md: this is unrelated to the local-views question beyond a loose rhyme. Each pair of rows is a "local" vanishing-sum constraint. No loop or composition structure is involved.

### Recommendation
**Park** (to covered_leads/).
- Types evaluated: Type 1, which was declared, plus Types 2, 5 and 6 as a courtesy check.
- Bars failed: Type 1 fails on known / trivial consequence (Lam–Leung, J. Algebra 224 (2000), main theorem W(m) = Σ ℕpᵢ).
- Open-question status: none. The conjecture is settled.
- Prior authors of the same claim withdrew it for this exact reason (arXiv:0707.4175v2).
