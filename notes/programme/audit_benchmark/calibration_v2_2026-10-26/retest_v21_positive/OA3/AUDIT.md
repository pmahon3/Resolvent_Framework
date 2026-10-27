## Audit: seed.md, the exclusivity-graph approach to Bell and noncontextuality scores (mode: full)

**Audit date (AS_OF.md): 2014-01-27.** Only sources dated on or before that date count. The seed's own
text, under any version or title, is the submission. So arXiv:1010.2163 (all versions), its QIP 2011
abstract and arXiv:1401.7081 / PRL 112, 040401 are all **excluded**. 1401.7081 has v1 dated 28 Jan
2014, after the cutoff, and it is the seed itself. Post-2014 hits that turned up in searches
(1511.05415, 2004.07673, 2007.10746, 2102.13036, 2105.08561, etc.) were ignored.
Web reads were done 2026-10-27.
**Scope disclosure:** web-sourced PDFs (Knuth, CLMW, KCBS, Avis–Imai–Ito, Svozil) were downloaded
to /tmp/oa3dl and to the harness tool-results cache so they could be text-extracted. Those paths
lie outside OA3. Only web-sourced content was read there, and no other local file was read.

### Declared contribution type(s): Type 3 (unifying framework), Type 4 (vocabulary)
The seed declares types but **no per-type bars** (the framework requires "the per-type bars I commit
to clearing"). This is a readiness defect. It is noted, not fatal.

### Sources consulted (read level, source date)
| Source | Date | Read level | Bearing |
|---|---|---|---|
| Knuth, "The sandwich theorem", Electron. J. Combin. 1 (1994) #A1, arXiv:math/9312214 | 1993-12 / 1994 | **full text** (grepped and passages read) | Defines STAB, TH, QSTAB (§1). Sandwich STAB ⊆ TH ⊆ QSTAB (Lemma 1). ϑ, α, κ = max w·x over TH, STAB, QSTAB (§§4–5). **Thm 14: TH(G) = {x : x_v = c(b_v), b an orthogonal labeling of Ḡ}**, i.e. squared overlaps of a unit "handle" vector with unit vectors (the bar on Ḡ is lost in the text extraction; Knuth's labelings put orthogonality on non-edges). QSTAB attributed to Shannon. Perfect graphs §31; C5 §36. |
| Lovász, IEEE Trans. IT 25 (1979); Grötschel–Lovász–Schrijver, JCTB 40 (1986) and *Geometric Algorithms and Combinatorial Optimization* (1988) | 1979–1988 | **not read directly**; content verified through Knuth's full-text exposition, which reproduces GLS | Primary owners of ϑ, TH(G) and the STAB = TH ⟺ perfect characterisation |
| Klyachko–Can–Binicioğlu–Shumovsky, PRL 101, 020403 (2008), arXiv:0706.0126v4 | 2008-07 | **full text** (grepped) | Pentagram inequality: classical bound 2, quantum √5. **No** mention of Lovász, ϑ, graphs or independence number. It is the C5 instance with no graph invariant identified. |
| Cubitt–Leung–Matthews–Winter, arXiv:1003.3195v2 (IEEE Trans. IT 2011) | 2010-03 / 2010-10 | **full text** (relevant sections read) | **Owns the α / ϑ / α\* hierarchy pattern in zero-error information theory.** Unassisted one-shot capacity is the independence number. Entanglement-assisted capacity is ≤ ϑ (via DSW/Beigi). Non-signalling-assisted capacity is ⌊α\*⌋, the fractional packing number (Thm 7). Uses Kochen–Specker basis sets (Def. 12, Thm 13). Shares an author (Winter) but is a separate work, so it counts. |
| Beigi, PRA 82, 010303(R), arXiv:1002.2488 | 2010-02 | abstract | Entanglement-assisted zero-error capacity ≤ ϑ |
| Duan–Severini–Winter, arXiv:1002.2514 | 2010-02 | abstract | Quantum ϑ for non-commutative graphs. No contextuality or Bell content in the abstract. |
| Avis–Imai–Ito, arXiv:quant-ph/0605148 | 2006-05 | **full text** (grepped) | Bell and Tsirelson bodies ↔ cut polytope and elliptope. **No** Lovász, ϑ or TH. It is the nearest pre-2010 physics–combinatorial-optimisation bridge, but it covers a different body. |
| Acín–Fritz–Leverrier–Sainz, arXiv:1212.4084 | 2012-12 | abstract | **Downstream, not an owner.** It builds on and credits the seed's preprint ("a similar recent approach by Cabello, Severini and Winter"). The same holds for other 2012–13 exclusivity and local-orthogonality papers. |
| Wright, "The state of the pentagon. A nonclassical example", in Marlow (ed.), *Mathematical Foundations of Quantum Theory*, Academic Press 1978, pp. 255–274 | 1978 | **not read.** Existence and citation verified via Svozil, arXiv:quant-ph/9902042v2 (2005), bibliography [47] (full-text grep). Content known only from a search-snippet description in a post-cutoff secondary source (arXiv:1509.03480, used solely as a pointer to the 1978 content): the all-½ pentagon state is realisable neither classically nor quantumly. | **Suspected partial owner of the C5 instance of the general-theory leg** (α\* = 5/2 exceeds both the classical and the quantum value). It does not bear on the general-graph ϑ identification. |
| Yan, PRL 110, 260406 (2013), arXiv:1303.4357 | 2013-03 | abstract plus secondary description | Downstream of the seed's preprint. Shows that the exclusivity principle applied to G *and* its complement (Lovász 1979 Lemma) recovers ϑ for some graphs. Bears on S3 below. |
| Kochen–Specker, J. Math. Mech. 17 (1967); Peres 1991 | 1967/1991 | **not read** (recalled) | Orthogonality graphs of KS vector sets. These are the precursor of the "exclusivity graph". |

### Pure Verdict: KNOWN (mathematics), with a residual physical identification that is not owned
Stripped of vocabulary, the seed's statements and their owners are as follows.

1. **The classical maximum is α(G, w).** Deterministic noncontextual assignments correspond to stable
   sets of the exclusivity graph, and their convex hull is STAB(G). So the classical maximum is
   max w·x over STAB, which is α by definition (Knuth §5). This is a trivial consequence of the
   definitions.
2. **The quantum maximum is ϑ(G, w).** ⟦HAND⟧ The upper bound takes three lines. Let ρ = |ψ⟩⟨ψ| and
   let P_i be projectors with P_iP_j = 0 on edges. Put v_i = P_iψ/‖P_iψ‖. Then v_i ⊥ v_j on edges,
   and ⟨ψ|P_i|ψ⟩ = |⟨ψ|v_i⟩|². By Knuth Thm 14 the behaviour lies in TH(G), so its score is ≤ ϑ.
   Mixed states follow by purification or convexity. Attainment: an optimal orthonormal
   representation together with its handle realises ϑ, taking rank-1 projectors as two-outcome
   tests. **This is a direct reading of Lovász 1979 / GLS 1986 / Knuth Thm 14.**
3. **"Quantum behaviours of some experiment form the theta body."** This is Knuth Thm 14 (GLS) read
   as the Born rule. The only physical content is that each x ∈ TH(G) is realised by rank-1
   projectors with exclusive events orthogonal (and hence commuting and jointly measurable).
4. **The GPT maximum is the fractional packing number.** This is max w·x over QSTAB (Shannon; Knuth
   §5). If "general theories" are defined as obeying only clique-wise exclusivity, it holds by
   definition.
5. **The hierarchy α / ϑ / α\*, read as classical / quantum / general.** The *pattern* is in print in
   a neighbouring field: CLMW 2010 (unassisted / entanglement-assisted / non-signalling-assisted
   zero-error capacity, read in full). The contextuality statement itself is not there.

**Residual that no owner covers (in pre-cutoff works not derived from the seed):**
- the *identification* of Bell and noncontextuality test scores with weighted graph invariants via a
  theory-independent exclusivity graph of events;
- the recognition that KCBS is the C5 case (α = 2, ϑ = √5). KCBS's pentagram is Lovász's umbrella,
  but KCBS does not say so (checked in full text).

Also searched: the quantum-logic / test-space literature. Wright 1978 is a suspected (unread) owner
of the C5 general-theory instance, as noted above. It would add to the KNOWN components. It does not
own the general-graph ϑ identification.
Searched, with no pre-2010 owner of the **general-graph** identification found: the KCBS full text, the Avis–Imai–Ito
full text, the CLMW full text, the DSW and Beigi abstracts, and two web searches on Lovász ϑ ×
Kochen–Specker, Bell and Tsirelson. Every hit dated ≥ 2010 traced back to the seed or to works that
cite it.

Hostile conclusion: under the programme's rule ("trivial consequence of standard techniques: KNOWN"),
the theorems are KNOWN. Each is a few lines from GLS and Knuth once the exclusivity graph is
defined. What survives is a **conceptual identification (a bridge)**, not a new theorem. The
`owned_by` regions are:
- (a) GLS 1986 / Knuth 1994 own the convex-geometry statements, verified in Knuth's full text;
- (b) CLMW 2010 owns the α/ϑ/α\* resource hierarchy for zero-error communication, verified in full
  text.

The entry is **PARTLY OWNED**. The residual is the physical identification, together with its
realisability in all graphs.

### Applied Verdict: not the right lens. FAIL as Type 7 (not claimed)
Decision test: the seed does change practice. It gives a polynomial-time SDP (ϑ) for the quantum
maximum of any noncontextuality test, and an α computation for the classical bound. The seed does
not claim Type 7, though, and offers no computational comparison with standard methods (for
example the NPA hierarchy for Bell tests). Not evaluated further.

### Contribution Type Verdicts (mode=full):

**Type 3 (unifying framework): PASS (conditional on stating the transfers).**
Bar: method transfer, not analogy. The framework does carry concrete combinatorial-optimisation
methods into contextuality. The seed's abstract states only the identifications; **the audit supplied
all three transfers below, inferred from those identifications**, so the PASS rests on audit-inferred
transfers:
- (i) Lovász's SDP computes quantum maxima of noncontextuality scores exactly;
- (ii) the NP-hardness of α, and its weighted-LP relaxation, carry over to the classical and GPT
  bounds;
- (iii) by GLS, STAB = TH ⟺ G is perfect. So **a test admits a quantum–classical gap only if its
  exclusivity graph is imperfect**, i.e. by SPGT (Chudnovsky–Robertson–Seymour–Thomas, Ann. Math. 2006; recalled, not
  read) it contains an odd hole (C5, C7, …) or an odd antihole. This gives a structural criterion for where contextuality can live.

This is transfer, not pattern-coincidence. The condition: the write-up must state (iii) and similar
transfers explicitly. As given, the abstract only says it "links graph invariants to physically
observable quantities", which on its own reads as analogy.

**Type 4 (vocabulary): UNCLEAR, leaning PASS.**
Three-statements test. Candidate statements in the new vocabulary (exclusivity graph of a test):
- (S1) a test has a quantum–classical gap only if its exclusivity graph is imperfect;
- (S2) the set of quantum behaviours for the graph is exactly TH(G), realised by an experiment;
- (S3) restricted to clique-wise exclusivity on a *single* graph, the general-theory bound κ(G, w)
  exceeds the quantum bound ϑ(G, w) whenever TH ≠ QSTAB. This must stay restricted: Yan 2013 (pre-cutoff,
  downstream) shows that exclusivity applied to G together with its complement recovers ϑ in some
  cases.

A non-trivial result: S2, using Knuth Thm 14 together with a realisability argument (non-trivial
only modestly).

The risk: "exclusivity graph" may be the Kochen–Specker / Peres **orthogonality graph** of vectors
lifted to events. If so, the vocabulary partly renames a 1967 notion. Its genuine extension is
theory-independence: events rather than vectors, which is what lets S3 be stated. KS 1967 was not
read, so the verdict is UNCLEAR rather than PASS.

### Cross-reference
The components are known: the convex geometry is GLS/Knuth, and the resource hierarchy pattern is
CLMW 2010. The **assembly as a bridge is not owned**, and it carries real method transfer (Type 3).
The Type 1 theorem bar is not cleared, since each statement is a short consequence of known
mathematics. Type 4 depends on how far "exclusivity graph" goes beyond the KS orthogonality graph.

**Scope flag (referee risk, not fatal).** ⟦HAND⟧ The seed says the quantum maximum *is* ϑ for "Bell
and noncontextuality tests". That holds as the maximum over *all* quantum realisations of the graph,
attained by some experiment. For a *fixed* Bell scenario (tensor-product structure, fixed local
measurement sets) the argument above gives only ≤ ϑ, and equality is not automatic. The statement
should read "upper bound, attained for some experiment realising G". I did not verify a pre-cutoff
counterexample; this concern rests on reasoning only.

### Recommendation
For the programme: **proceed, scoped to Type 3**, with the following conditions:
- the seed must state its per-type bars;
- it must state the transfers explicitly (SDP; perfect-graph criterion);
- it must fix the Bell-scope wording;
- it must credit GLS/Knuth Thm 14 for the theta-body statement and CLMW 2010 for the α/ϑ/α\*
  hierarchy pattern.

Type 1 is not claimed, and would fail. Type 4 needs a KS 1967 / Peres read to settle the renaming
question.

### Referee estimate: ACCEPT-LIKELY
Venue class: short-note or letters (PRL-type physics letters)
Value carried by: factor 3. It is a framework that organises known inequalities (KCBS, CHSH, KS-type)
and yields new statements and tools: the SDP bound, the perfect-graph criterion for a gap, quantum
set = TH, and the general-theory bound α\*. Factor 1 is not relied on.
Main risk a referee would raise: "maximum is ϑ" is overstated for fixed Bell scenarios (where it is
only an upper bound); the mathematics is GLS/Knuth Thm 14 and must be credited as such; the CLMW
α/ϑ/α\* parallel should be cited.

**Caps check.**
- Cap 1 (pure UNCLEAR → ≤ BORDERLINE): **not engaged**. The pure verdict is KNOWN for the
  mathematics with the residual identified. The component owners (Knuth/GLS, CLMW) and the nearest
  neighbours (KCBS, Avis–Imai–Ito) were verified in full text. No owner of the main claim (the
  general-graph identification) is suspected but unread. The unread items (KS 1967, Wright 1978, the
  Beigi and DSW abstracts) bear on Type 4, on the C5 sub-instance, or are adjacent results.
- Cap 2 (ACCEPT on factor 1/2 needs the nearest prior work read): **not engaged**. Value rests on
  factor 3. The nearest prior work was read beyond abstract in any case.
- Cap 3 (owner in print, not credited → REJECT): **not engaged, via the exception.** The submission is
  abstract-only, so I cannot tell whether GLS Thm 14 / Knuth, CLMW or Wright are credited. Even if
  they are not, a clearly substantial residual remains: the general-graph identification of test
  scores with α, ϑ and α\*, realisability for every G, and the transfers (SDP, perfect-graph
  criterion). No pre-cutoff work owns that residual.

### Bearing on the programme's question (one line)
Local exclusivity constraints, each consistent pairwise, add up to a global bound (α, ϑ or α\*) that
depends on the theory. The gap between ϑ and α lives exactly in imperfect graphs (odd holes or antiholes), so
this is a "loop" answer to when local views fail to make one world.
