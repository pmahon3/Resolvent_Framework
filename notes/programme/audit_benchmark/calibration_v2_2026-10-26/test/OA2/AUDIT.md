## Audit: seed.md, "a simplified geometrical, measure-theoretic proof of the Kochen–Specker theorem in every dimension ≥ 3" (mode: full)

Audit date (AS_OF.md): **2017-08-03**. Only sources dated on or before that day count as prior art. The seed's own work, in any version and under any title, is not used, and neither are later notices about it.

Search date: 2026-10-26, WebSearch/WebFetch in standard mode.

Read levels used below:
- **[A]** abstract or arXiv metadata read on 2026-10-26.
- **[M]** known from standard background and not re-read here; the citation was checked against search snippets.
- **[S]** secondary description only (search snippet or SEP note).

### Declared contribution type(s): Type 2 (new proof of a known result) and Type 6 (exposition / translation)

The seed declares its types but **does not state its per-type bars**. Under the framework's Phase 1 rule it is not fully ready for Phase 2. The audit goes ahead against the standard bars.

The seed is a five-sentence abstract. There is no proof text, so the *argument* cannot be checked. Every verdict below is limited to what the abstract claims.

### Pure Verdict: KNOWN (the theorem itself; the seed does not claim otherwise)

With the vocabulary removed, the statement is: in a real or complex Hilbert space of dimension n ≥ 3, there is no map v from unit vectors (rays) to {0,1} that gives the value 1 to exactly one member of every orthonormal basis. This is the Kochen–Specker theorem. The seed itself presents it as a fifty-year-old result. The only novelty claim is about the proof (Type 2), so Type 1 does not apply.

**The "any dimension ≥ 3" part is routine.**
1. Pick any orthonormal basis. Exactly one vector gets the value 1; call it b₁.
2. Fix b₄,…,bₙ, which all have value 0.
3. Every orthonormal triad of span(b₁,b₂,b₃), together with b₄,…,bₙ, is a basis. So v restricted to that 3-dimensional subspace is a KS colouring.
4. Hence dimension 3 implies every dimension ≥ 3.

This reduction is folklore. It is noted in Kochen–Specker 1967 [M] and in the standard expositions (Peres 1993 ch. 7 [M]; Held, SEP "The Kochen-Specker Theorem", 2000 onward [S]). It adds nothing as a contribution.

**Prior proofs that are "geometrical" and "short", all predating 2017-08-03:**
- **Bell 1966**, Rev. Mod. Phys. 38, 447 [M]. A continuity argument derived from Gleason: on S², points valued 1 and points valued 0 cannot be arbitrarily close, which contradicts the connectedness of the sphere. This is the original "geometric, minimal machinery" route.
- **Kochen & Specker 1967**, J. Math. Mech. 17, 59 [M]. The finite 117-vector construction. Its first step (nearby points cannot receive different values) goes back to Specker's earlier work and is effectively a consequence of Gleason's theorem (SEP notes, archived 2001–2003 [S]).
- **Cooke, Keane & Moran 1985**, Math. Proc. Camb. Phil. Soc. 98, 117 [M]. An elementary geometric proof of Gleason's theorem, with KS as a corollary. Kalmbach, *Measures and Hilbert Lattices* (1986) [M], gives a similar argument.
- **Gill & Keane 1996**, J. Phys. A 29, L289; arXiv quant-ph/0304013 (2003) [A]. "A short geometric proof of the Kochen-Specker no-go theorem", built on the Cooke–Keane–Moran idea. Larsson's note says the construction contains the KS, Bell, Conway–Kochen, Schütte and possibly Peres constructions.
- **Calude, Hertling & Svozil 1998**, Tatra Mt. Math. Publ. 15(2), 133–142; arXiv 1402.5195 (2014) [A]. "Kochen-Specker Theorem: Two Geometric Proofs".
- **Peres 1991**, J. Phys. A 24, L175 (33 rays in d=3) [M]. **Mermin 1990/1993**, PRL 65 and RMP 65, 803 [M]. **Cabello, Estebaranz & García-Alcaine 1996**, PLA 212, 183 (18 vectors in d=4) [M]. These are the "intricate brute-force" line, already much simplified.
- **Hrushovski & Pitowsky 2003/2004**, arXiv quant-ph/0307139, Stud. Hist. Phil. Mod. Phys. 35 [A]. KS from Gleason plus compactness, a direct finite construction, and the effectiveness of Gleason's theorem.

The search turned up no pre-2017 proof that specifically uses measure-theoretic properties of {0,1} assignments on S² in the sense the seed's abstract suggests. The nearest measure-based routes are Gleason-type arguments. The **measurable frame-function case** of Gleason's theorem is classical and easy (Gleason 1957 [M]; Dvurečenskij, *Gleason's Theorem and its Applications*, 1993 [M]). A {0,1}-valued *measurable* frame function is ruled out at once by that case.

**Correctness flag.** This is a structural concern derived from first principles; the seed's argument was not read.
- A KS assignment is an arbitrary function. Nothing in the hypothesis makes {x ∈ S² : v(x) = 1} Lebesgue-measurable.
- The KS theorem holds for *all* assignments, and it is provable in ZF, since it reduces to a finite uncolourable set.
- So a proof that uses measures of value sets on the sphere has two options:
  - (i) **Assume measurability.** It then proves only "no *measurable* noncontextual assignment". That is strictly weaker, and it already follows from the easy measurable case of Gleason.
  - (ii) **Use outer or inner measure.** Additivity then fails, and the standard averaging step breaks. That step integrates the indicator over random orthonormal frames to get μ(S) = 1/3.
- Kent–Meyer–Clifton (1999–2000) [M] show that colourable dense subsets exist, for example the rational directions. Measure-zero sets therefore carry real content. An "almost-everywhere" argument cannot deliver KS unless it handles the uncountably many triads exactly.
- Unless the full text closes this gap explicitly, a referee would treat the central claim as **unverified and probably wrong as stated**. This is the main risk.

### Applied Verdict: not evaluated (no Type 7 claim; nothing applied in the seed)

### Contribution Type Verdicts (mode=full):

**Type 2 (New proof of known result): FAIL**

The bar requires at least one of three things.
- **(a) A technique applicable elsewhere.** None is named. "Measure-theoretic properties of assignments" is the standard Gleason/frame-function toolkit (Gleason 1957; Cooke–Keane–Moran 1985).
- **(b) An unexpected connection between fields.** None. Measure theory on the sphere has been tied to KS since Gleason, Bell and Specker.
- **(c) A substantial simplification.** This is not shown. The bar is set by Bell 1966 (a paragraph-long continuity argument), Gill–Keane 1996 (short and geometric) and Calude–Hertling–Svozil 1998 (two geometric proofs). The seed claims to be "another simplified geometrical proof". No measure of simplicity against these is given, and the seed cites none of them. "Any dimension ≥ 3" is the routine reduction above.

If the argument relies on measurability (see the correctness flag), it is not a proof of KS at all, and Type 2 fails at the root. As described, it is "different but not better or more revealing". **Park condition met.**

**Type 6 (Exposition / translation): FAIL**
- (a) **Audience:** not named. "What the theorem implies about realism" points loosely at philosophers of physics or foundations readers.
- (b) **Literature that audience cannot access:** none identified. KS is very well exposed for that audience: Held, SEP entry (2000 onward); Peres, *Quantum Theory: Concepts and Methods* (1993) ch. 7; Mermin RMP 1993; Redhead, *Incompleteness, Nonlocality and Realism* (1987); Bub, *Interpreting the Quantum World* (1997) [all M].
- (c) **Non-trivial translation work:** none is evident. A further proof plus a discussion of realism is not a translation.

The bar's park clause, "well-explained in [textbook], Chapter N", applies directly: Peres 1993 ch. 7, and the SEP entry.

### Cross-reference

The theorem is fifty years old and the seed says so. The whole value would have to come from the proof, and the proof claim fails Type 2 against at least four short geometric proofs (Bell 1966, Cooke–Keane–Moran 1985, Gill–Keane 1996, Calude–Hertling–Svozil 1998). The seed cites none of them.

The measure-theoretic route is the one place where novelty could live. It is also the place where a correctness gap is structurally likely, because KS assignments need not be measurable. Type 6 cannot rescue the item, since the exposition is already accessible.

**Bearing on WHY.md** (one line, not a bar): KS is the original "local views, each correct, that add up to no world" result. A measure-theoretic proof that quietly assumes measurability would be an example of the *hidden idealisation* question: it smuggles in regularity that the answers themselves do not supply.

### Recommendation

**Park.**
- Types evaluated: 2 and 6.
- Type 2 failed: no technique transfer, no new connection, and no simplification shown over Bell, Gill–Keane or Calude–Hertling–Svozil. Correctness is also unverified, with a structural measurability gap.
- Type 6 failed: the audience is unnamed and the literature is already accessible (Peres ch. 7, SEP).

Re-entry is possible only if the full text proves KS for *arbitrary* (non-measurable) assignments by a genuinely measure-theoretic argument. That would be a real Type 2 (a) or (b) contribution, and it would need an explicit comparison with Gill–Keane 1996.

### Referee estimate: REJECT-LIKELY
Venue class: none. At best it would be a short-note or letters venue (J. Phys. A letters, Found. Phys.), and only if the proof is correct and positioned against the earlier geometric proofs.
Value carried by: none shown. Factor 2 (a different, shorter proof) would carry it only if the measure argument is valid for non-measurable assignments and is clearly shorter than Bell, Gill–Keane or Calude–Hertling–Svozil.
Main risk a referee would raise: the measure-theoretic step needs value sets on S² to be measurable. KS assignments need not be measurable, so either the proof is incomplete or wrong, or it proves only the easy measurable case already covered by Gleason. In addition, the earlier short geometric proofs are not cited.

**Undetermined dates:**
- Gill–Keane: the J. Phys. A 1996 reference is taken from the arXiv comments [A]; the arXiv posting is 2003. Both predate the audit date.
- Calude–Hertling–Svozil: the journal date of 1998 is taken from the arXiv journal-ref [A]. Both 1998 and 2014 predate the audit date.
- Search results dated after 2017-08-03 (arXiv 2402.09186, 2403.05230) were ignored.
