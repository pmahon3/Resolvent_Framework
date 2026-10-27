## Audit: seed.md, "weak finiteness" for group rings (mode: full)

Audit date per AS_OF.md is **2017-03-07**. Only sources dated on or before that day are used. Every source cited below predates it. No source of uncertain date was relied on.

### Declared contribution type(s): Type 1 (new theorem), Type 4 (vocabulary)
The seed declares its types but gives **no per-type bar commitments**. It also states no theorem: it gives neither the definition of "weak finiteness" nor the group conditions or classes. In framework terms it is not fully ready for Phase 2. The audit therefore judges the claims that the seed's text allows.

### Pure Verdict: UNCLEAR, leaning KNOWN (the name is KNOWN; the theorems cannot be checked)

**The statement with the vocabulary stripped.** For a field K and group G, the seed asks whether a one-sided inverse in K[G] is automatically two-sided. That is **direct finiteness** (Kaplansky's direct finiteness conjecture). The seed adds a property called "weak finiteness", proves it for K[G] under conditions on G, and compares it with direct finiteness.

**Hostile findings (all predate 2017-03-07):**
1. **The name is taken.** "Weakly finite" is P. M. Cohn's standard term, from Cohn 1966, *Some remarks on the invariant basis property*, Topology 5, and his free-rings books. It means: for all n, AB = I_n ⇒ BA = I_n in M_n(R). Synonyms are "stably finite" (Wikipedia, *Stably finite ring*) and Losey's "strongly finite" (Losey, *Are one-sided inverses two-sided inverses in a matrix ring over a group ring?*, Canad. Math. Bull. 13 (1970) 475–479; read level: first page and definitions, via Cambridge Core, read 2026-10-26).
   - If the seed's property *is* Cohn's, then "we introduce" is false: it is a known concept under its standard name.
   - If it is a *different* property, the seed reuses a standard name for it, and any referee will object to the collision.
2. **For stable (weak) finiteness, the group-ring results are heavily occupied:**
   - **Characteristic 0, all groups:** Kaplansky (1969, *Fields and Rings*), via the trace on the group von Neumann algebra. Montgomery, *Left and right inverses in group algebras*, Bull. AMS 75 (1969) 539–540, gives a C*-algebra proof for matrices over C[G] (read level: AMS listing and abstract summary, read 2026-10-26).
   - **Residually amenable groups, any division ring:** Ara, O'Meara and Perera, *Stable finiteness of group rings in arbitrary characteristic*, Adv. Math. 170 (2002) 224–238 (read level: citation and secondary descriptions only; whether the result is stated as direct or stable finiteness was not confirmed from the primary source).
   - **Sofic groups, any field:** Elek and Szabó, *Sofic groups and direct finiteness*, J. Algebra 280 (2004), arXiv math/0305440, v1 dated 2003-05-30 (read level: abstract, read 2026-10-26). Secondary sources say it covers stable finiteness, through an affiliated-algebra construction.
   - **Equivalence of direct and stable finiteness:** Dykema, Heister and Juschenko, *Finitely presented groups related to Kaplansky's Direct Finiteness Conjecture*, arXiv:1112.1790, v1 dated 2011-12-08 and v4 2012-08-28 (read level: abstract, read 2026-10-26). They show that direct finiteness of K[G×H] for all finite H implies stable finiteness of K[G]. So the "comparison with direct finiteness" is already settled at the level of the conjectures.
   - **Residually finite-by-sofic groups, finitely generated:** Berlai, *Groups satisfying Kaplansky's stable finiteness conjecture*, arXiv:1501.02893, v1 dated 2015-01-13 (read level: abstract, read 2026-10-26). This gives new finitely presented non-LEA examples that satisfy both conjectures.
3. **Consequence.** No non-sofic group was known on 2017-03-07. So a theorem of the form "if G satisfies conditions C, then K[G] is weakly or stably finite" is new only if the classes it covers are *not already known to be sofic* (or residually-finite-by-sofic, in the Berlai sense). If the classes are amenable, residually finite, residually amenable, LEF, LEA or linear, the result is KNOWN, as a corollary of Elek–Szabó.
4. **If "weak finiteness" is a genuinely new, strictly weaker property than direct finiteness**, the risk changes: the result may be **trivial**. A weakening of the direct finiteness conjecture is easier to prove, and its value depends on whether it says anything about the open positive-characteristic, non-sofic case. The seed does not say.

**What was searched:** direct, stable, weak and strong finiteness of group rings; Cohn's terminology; Kaplansky's conjecture in characteristic 0 and characteristic p; sofic, residually amenable and ULIE groups. Primary statements were checked at abstract level only. No full texts were read.

**Verdict:** The name and the framing are KNOWN. The theorem content is UNCLEAR, because it is unstated. It can be NOVEL only if (i) the property differs from Cohn's weak finiteness, or (ii) the group classes reach beyond those known to be sofic or residually-finite-by-sofic by 2017-03-07.

### Applied Verdict: not evaluated
This is pure algebra, and Type 7 is not claimed.

### Contribution Type Verdicts (mode=full only):

**Type 1 (new theorem): UNCLEAR, at risk of FAIL.**
- Bar: not known, not folklore, not a trivial consequence, with a non-routine proof.
- No theorem is stated, so the bar cannot be checked. The surrounding region is densely owned: Kaplansky and Montgomery (char 0), Ara–O'Meara–Perera (residually amenable), Elek–Szabó (sofic), Dykema–Heister–Juschenko (equivalence of direct and stable finiteness), Berlai (residually finite-by-sofic).
- To pass, the seed must name a group class not covered by these, or a property not equivalent to stable finiteness that has a non-trivial consequence.

**Type 4 (vocabulary): FAIL.**
- Bar: three statements that can be stated cleanly in the new vocabulary but not in standard vocabulary, plus one non-trivial result.
- The term "weak finiteness" is Cohn's standard 1966 term. Under that reading the seed renames a known concept, which is failure mode #2.
- Under the reading that it is a new property, the seed offers no three statements, and the name collision itself counts against it.
- The comparison with direct finiteness is already organised in the literature, through the Dykema–Heister–Juschenko reduction.

### Cross-reference
The two verdicts hang together:
- Type 4 fails regardless.
- Type 1 is the only route left, and it depends entirely on the specific group classes (or the specific new property), which the seed does not give.
- Known components plus an unstated assembly cannot pass the gate.

### Recommendation
**Needs deeper audit / not ready.** Return the seed for the following:
1. A precise definition of "weak finiteness", with a proof or disproof that it equals Cohn's weak (stable) finiteness.
2. Explicit group conditions, checked against soficity, the Ara–O'Meara–Perera class and Berlai's class.
3. Rewording, if the property is Cohn's: "we introduce" becomes "we study".

If the classes turn out to be sofic, **park**. Types evaluated: 1 (UNCLEAR, region owned) and 4 (FAIL, renaming and name collision).

Bearing on the programme's why: none directly. This is a local-to-global finiteness question in ring theory, with no tie to the local-views question.

### Referee estimate: BORDERLINE
Venue class: research journal (algebra or group theory, e.g. J. Algebra, J. Group Theory, Comm. Algebra)
Value carried by: factor 1 (a new theorem), but only if the group classes go beyond those known to be sofic or residually-finite-by-sofic, or if the property is new and non-trivial.
Main risk a referee would raise: "weakly finite" is Cohn's standard term (equal to stable finiteness, which Dykema–Heister–Juschenko show is equivalent to Kaplansky's direct finiteness conjecture). So "introducing" it is a misattribution, and the group classes may already be covered by Elek–Szabó (sofic) or Berlai.

---
Sources (all predate 2017-03-07; read 2026-10-26):
- Cohn 1966, Topology 5 (cited via secondary sources; not read)
- Losey 1970, Canad. Math. Bull. 13: https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/are-onesided-inverses-twosided-inverses-in-a-matrix-ring-over-a-group-ring/9D2CC0E02BC24798C52DB5B1BC54234F (first page)
- Montgomery 1969, Bull. AMS 75: https://www.ams.org/bull/1969-75-03/S0002-9904-1969-12234-2/ (listing)
- Ara–O'Meara–Perera 2002, Adv. Math. 170 (citation only)
- Elek–Szabó 2003/04: https://arxiv.org/abs/math/0305440 (abstract)
- Dykema–Heister–Juschenko 2011: https://arxiv.org/abs/1112.1790 (abstract)
- Berlai 2015: https://arxiv.org/abs/1501.02893 (abstract)
- Wikipedia, "Stably finite ring" (terminology only)
