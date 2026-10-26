## Audit: seed.md (sheaf-like unification of non-locality and contextuality) (mode: full)

**Audit date (as-of): 2011-01-31.** Only sources dated on or before 2011-01-31 are counted. The
seed's own text is the submission. Abramsky, "Relational hidden variables and non-locality"
(arXiv:1007.2754) is a **distinct earlier paper** by an author who may overlap with the
submission. It is not a version of the seed, so it is treated as prior art. Only **v4 (31 Dec
2010)** is used. v5 (18 Oct 2011) is ignored.

### Declared contribution type(s): Type 3 (unifying framework), Type 4 (vocabulary)

The seed names these types but **commits to no per-type bars**. It does not say which method is
transferred, and it does not name three new statements. The skill flags this as not fully ready
for Phase 2. The statements tested under Type 4 below were constructed by the auditor, not
offered by the seed.

### Sources consulted (read level, date)

| # | Source | Date | Read level |
|---|--------|------|-----------|
| S1 | Abramsky, *Relational hidden variables and non-locality*, arXiv:1007.2754v4 | 31 Dec 2010 | **full text** (pdftotext; intro, Props 4.3–4.4, 6.1–6.4, 8.1–8.3, §11 grepped/read) |
| S2 | Isham & Butterfield, *A topos perspective on the Kochen–Specker theorem I*, quant-ph/9803055; IJTP 37 (1998) 2669 | Mar 1998 | snippet (search summary) |
| S3 | Vorob'ev, *Consistent families of measures and their extensions*, Theory Probab. Appl. 7 (1962) 147–163 | 1962 | snippet (Math-Net.ru record) |
| S4 | Cereceda, *Local hidden-variable models and negative-probability measures*, quant-ph/0010091v4; Found. Phys. Lett. 13 (2000) 427 | 13 Dec 2000 | **full text** of intro/abstract (pdftotext); body grepped |
| S5 | Han, Hwang & Koh, Phys. Lett. A 221 (1996) 283 | 1996 | snippet (KAIST record + Cereceda's citation) |
| S6 | Brandenburger & Yanofsky, *A classification of hidden-variable properties*, J. Phys. A 41 (2008) 425302, arXiv:0711.4650 | Nov 2007 / 2008 | abstract |
| S7 | Mermin, *Simple unified form for the major no-hidden-variables theorems*, PRL 65 (1990) 3373 | 1990 | snippet (abstract via secondary record) |
| S8 | Fine, *Hidden variables, joint probability, and the Bell inequalities*, PRL 48 (1982) 291 | 1982 | reference-list only (cited as [12] in S1); content known to the auditor, not re-read |
| S9 | Pitowsky, *Quantum Probability – Quantum Logic*, LNP 321 (Springer) | 1989 | reference-list only (cited as [29] in S1); textbook, correlation polytopes |
| S10 | Liang, Spekkens & Wiseman, *Specker's parable of the over-protective seer*, arXiv:1010.1273 **v1** | 6 Oct 2010 | abstract (v1 only; the erratum in the title is later and is ignored) |
| S11 | Cabello, Severini & Winter, *(Non-)contextuality of physical theories as an axiom*, arXiv:1010.2163 | 11 Oct 2010 | snippet/abstract |
| S12 | Spekkens, *Negativity and contextuality are equivalent notions of nonclassicality*, PRL 101 (2008) 020401, arXiv:0710.5549 | Oct 2007 / 2008 | abstract (search summary) |
| S13 | Cabello, *"All versus nothing" inseparability for two observers*, PRL 87 (2001), quant-ph/0101108 | 2001 | snippet |
| T1 | Peres, *Quantum Theory: Concepts and Methods* (Kluwer 1993), Ch. 6 (Bell), Ch. 7 (KS) | 1993 | not re-read (textbook; auditor's knowledge) |

**Dates not determined:**
- Fritz, "Possibilistic Physics" (2009 essay, S1 ref [13]). The essay was not located, so its content is unverified. It is the obvious candidate owner of the possibilistic tier.
- Brandenburger & Keisler (S1 ref [4]). Not checked.

### Pure Verdict: KNOWN (components) / UNCLEAR (assembly: strong tier and general signed-measure theorem)

With the vocabulary stripped, the seed makes the following claims.

1. **Empirical model = compatible family of distributions over a cover of measurement contexts.
   Nonlocality/contextuality = non-existence of a global distribution (section) restricting to
   it.**
   - The probabilistic statement is **Vorob'ev's extension problem (S3, 1962)**: a consistent family of measures over a complex, and when it is extendable.
   - In the Bell case it is **Fine's theorem (S8, 1982)**: LHV ⇔ a joint distribution exists.
   - For quantum KS, "no global section of a presheaf over contexts" is **Isham–Butterfield (S2, 1998)**: KS ⇔ the spectral presheaf has no global elements.
   - The new part is restricted to the following. The presheaf is taken over *empirical* data for an *arbitrary* cover, rather than over the quantum spectral presheaf. Bell scenarios are then a special cover, so KS and Bell sit in one functorial picture.
   - Verdict: **KNOWN as content; the sheaf packaging is a translation.**
2. **Linear-algebraic method for computing the obstruction.**
   - Deciding whether a global distribution exists is LP feasibility over the deterministic global assignments. This is the standard correlation-polytope method (**Pitowsky S9, 1989**), which follows directly from S3/S8.
   - S1 already notes membership of LHV is in NP.
   - Verdict: **KNOWN (standard technique).**
3. **Ranking Bell, Hardy and GHZ by strength.**
   - Already known:
     - S1 (Dec 2010) proves Hardy and GHZ no-gos *purely relationally* (Props 6.2, 6.3), in what it calls "purely logical terms". It notes that Bell/CHSH needs probabilities.
     - Cabello (S13, 2001) calls GHZ-type proofs "all-versus-nothing" and contrasts them with Hardy.
     - The informal ordering is folklore.
   - S1's "strict hierarchy" is a *different* chain (LHV ⊊ QM ⊊ NS, Props 11.1–11.2).
   - Not found before 2011-01-31: a *formal* three-tier hierarchy on arbitrary covers (probabilistic ⊋ possibilistic ⊋ "strong" = no global section consistent with the support at all), with strictness witnessed by CHSH/Hardy/GHZ.
   - Verdict: **UNCLEAR, leaning novel as a formal theorem.** The gap is that Fritz 2009 was unread.
4. **Signed-measure LHV ↔ no-signalling.**
   - Cereceda (S4, Dec 2000) proves the following in the (2,2,2) CHSH scenario: *any* "consistent" set of probabilities (normalisation plus the "causal communication constraint", i.e. no-signalling) is reproduced by an LHV model with a signed measure. He gives the general solution.
   - This builds on Han–Hwang–Koh (S5, 1996) and Mückenheim (1982).
   - Not found: the converse (signed LHV ⇒ NS) stated as a characterisation, and the version for arbitrary n-party / arbitrary-cover scenarios.
   - Verdict: **KNOWN for CHSH; general-scenario characterisation not found** (it is plausibly a routine linear-algebra generalisation).
5. **"One framework" for nonlocality and contextuality.** Owned in spirit by four sources:
   - Mermin (S7, 1990): a unified form for KS and Bell.
   - Brandenburger–Yanofsky (S6, 2008): one classification covering EPR, Bell and KS.
   - Liang–Spekkens–Wiseman (S10 v1, Oct 2010): joint-measurability/marginal framing that ties contextuality, nonlocality and complementarity together.
   - Cabello–Severini–Winter (S11, Oct 2010): one graph-theoretic framework for Bell and KS inequalities, with classical bound = independence number.

   Verdict: **KNOWN as a programme. The specific sheaf form is not found.**

**Would an expert say "obvious"?**
- Claims 1, 2 and 4 (CHSH case): mostly yes, to anyone who knows Vorob'ev, Fine or Pitowsky.
- Claim 3 as a formal hierarchy: no.

### Applied Verdict: not evaluated (Type 7 not claimed)

Practitioner test, for the record: "I already decide locality by the Fine/Pitowsky LP." The seed's
answer is that the same LP decides contextuality for any cover, and that the support-level tiers
are decidable combinatorially. The second half of that answer is the only part a practitioner does
not already have.

### Contribution Type Verdicts (mode=full):

**Type 3 (Unifying framework): UNCLEAR, leaning FAIL as written.**
- Bar: a technique from domain A demonstrably becomes applicable in domain B.
- Candidate transfers:
  - (a) The LP / global-section test moves from Bell scenarios to arbitrary contextuality scenarios. This is **owned**: Vorob'ev (S3) already poses the extension problem for arbitrary complexes, and Pitowsky (S9) and CSW (S11) apply LP- or graph-bound methods across Bell and KS.
  - (b) Hardy-type *possibilistic* arguments move from bipartite nonlocality to KS-type contextuality, and the GHZ/KS kinship is made precise as "strong contextuality". This would be a genuine transfer. Mermin (S7) already linked GHZ and KS, and S1 Prop 6.4 already treats KS in the same relational format as GHZ/Hardy.
  - (c) Sheaf-theoretic or cohomological tools move from topology to quantum foundations. This is **not demonstrated** in the seed. "Obstruction to global sections" is named but no sheaf technique is used to compute anything.
- The seed *asserts* a method and does not demonstrate any transfer.
- PASS would require at least one of the following, worked out:
  - a cohomological or sheaf-theoretic criterion that detects contextuality where LP is not the natural tool;
  - a Hardy-style possibilistic contextuality argument for a non-Bell cover, obtained *via* the framework.

**Type 4 (Vocabulary / conceptual infrastructure): CONDITIONAL PASS (contingent on proofs of strictness).**

Three-statements test, applied to statements the auditor constructed:
1. *"Model e is strongly contextual": no global assignment is consistent with the support
   presheaf.* This is stateable for arbitrary covers. Standard vocabulary has
   "all-versus-nothing" (S13) only as an informal label for particular proofs. S1's relational LHV
   realisability is the *possibilistic* tier and does not isolate this one. **New.**
2. *"Contextuality comes in three strictly nested tiers on every cover (probabilistic ⊋
   possibilistic ⊋ strong), and the Bell/CHSH, Hardy and GHZ models are witnesses separating
   them."* This is not stateable without (1) and without a uniform notion of a possibilistic
   section over an arbitrary cover. **New statement; a non-trivial result if proved** (strictness
   needs explicit models, and needs the possibilistic collapse of a CHSH-violating model to be
   shown to be possibilistically extendable).
3. *"Possibilistic (Hardy-type) non-extendability is a property of the support presheaf alone, so
   it is decidable without probabilities, uniformly for nonlocality and contextuality."* This is
   partly anticipated by S1 (relational no-gos, possibilistic collapse, Props 8.1–8.3), but only
   for Bell-type product measurement sets. **Partly new** (the generalisation to arbitrary covers).

Not counted:
- "Contextuality = non-extendability of a compatible family over a cover". It is cleanly stateable in Vorob'ev's vocabulary (consistent family / extendable; S3), so it fails "not stateable in standard vocabulary".
- "No-signalling ⇔ signed-measure LHV". This is stateable in standard vocabulary, and the CHSH case is in S4.

Result: statement 2 is the non-trivial result. Statements 1–3 give about 2.5 new statements, which
clears the bar narrowly once the hierarchy theorem is actually proved. The risk is Fritz 2009
(unread), which may own the possibilistic tier.

### Cross-reference

- The components are known:
  - Vorob'ev 1962 and Fine 1982: global extension;
  - Isham–Butterfield 1998: KS as no global section;
  - Pitowsky 1989: LP;
  - Cereceda 2000: signed measures ⇔ consistent data in CHSH;
  - Abramsky Dec 2010: relational Bell/GHZ/Hardy/KS no-gos.
- The surviving novelty is **vocabulary-level**: the strong-contextuality tier and the formal three-tier hierarchy on arbitrary covers.
- Type 4 can pass where Type 1 and Type 3 do not, because the known parts are organised into a hierarchy that standard vocabulary cannot state.
- Type 3 fails as written because "one framework" is asserted, not shown to carry a method across.

### Recommendation

**Proceed to Phase 3, scoped to Type 4.** Type 3 is parked unless a concrete transfer is
demonstrated. Conditions:
1. Prove the strict three-tier hierarchy on arbitrary covers with explicit witnesses. This is the non-trivial result.
2. Read Fritz 2009 "Possibilistic Physics" before claiming the possibilistic tier.
3. Mandatory citations, with the differences stated:
   - Vorob'ev 1962 (extension problem; acyclicity of the complex);
   - Fine 1982;
   - Pitowsky 1989;
   - Isham–Butterfield 1998 (global-section form of KS);
   - Mermin 1990;
   - Brandenburger–Yanofsky 2008;
   - Cereceda 2000 and Han–Hwang–Koh 1996 (the negative-probability ↔ no-signalling link is **not new** in the CHSH case; claim only the general-scenario characterisation and its converse);
   - Abramsky arXiv:1007.2754v4 (relational GHZ/Hardy/KS);
   - Liang–Spekkens–Wiseman 2010;
   - Cabello–Severini–Winter 2010.
4. Drop "linear-algebraic method" as a contribution. It is the standard LP, so cite it as such.

**Most damaging prior source:** Abramsky, arXiv:1007.2754v4 (31 Dec 2010):
- Props 6.2–6.4: GHZ, Hardy and KS no-gos in one relational framework;
- §8: possibilistic collapse;
- Props 4.3–4.4: no-signalling characterisation.

The runner-up for the negative-probability claim is Cereceda (Dec 2000), which gives the general
signed LHV solution for any consistent (no-signalling) set of CHSH probabilities.

**Bearing on the programme's question (one line):** this is the clearest pre-existing statement of
"local views, each correct, that do not glue into one world", seen as a sheaf obstruction. Its
tiers (probabilistic, possibilistic, strong) are the graded answer to "what do they say when they
don't".
