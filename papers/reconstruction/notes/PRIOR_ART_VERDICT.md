# Prior-art findings (durable)

## VERDICT-CHANGING (verified personally)

### Wainwright-Jordan (R1 framework + 2a)
- LOCAL(G) = locally consistent pseudomarginals (pairwise/edge consistency + normalization) = the paper's C (coherence/EA polytope).
- MARG(G) = globally realizable marginals = the paper's R (realisability polytope, hull of global configs).
- THEOREM: MARG(G) ⊆ LOCAL(G) always; LOCAL(G) = MARG(G) IFF G is a tree (LP relaxation tight exactly for trees). Cycles => strict outer bound.
- => R1's "C = R" IS WJ's local=marginal; commensurability = tightness of the LP relaxation. 2a (acyclic => commensurable) = WJ tree-exactness (+ junction-tree/RIP for hypertrees).
- Cite: Wainwright & Jordan 2008, "Graphical Models, Exponential Families, and Variational Inference", FnT ML 1(1-2). Also Wainwright-Jaakkola-Willsky MAP-on-trees (arXiv cs/0508070).
- VERDICT: R1 = KNOWN framework (translation); 2a = KNOWN (WJ tree-exactness + Vorobev/BFMY).

### Prusa-Werner (kills 2c independently, DIRECT hit)
- "Universality of the Local Marginal Polytope", CVPR 2013 + IEEE TPAMI 37(4) 2015.
- THEOREM: ANY polytope is linear-time representable by a local marginal polytope; any LP reduces in linear time to linear optimization over a local marginal polytope.
- => the exact object (local marginal polytope of a graphical model) is UNIVERSAL. This is 2c for the SAME object, not an analogue. NP-hardness + no finite facet taxonomy follow.
- MUST-CITE, and NOT on the paper's declared shelf. More on-point than De Loera-Onn.

### De Loera-Onn 2004 (2c)
- "All Rational Polytopes Are Transportation Polytopes and All Polytopal Integer Sets Are Contingency Tables", IPCO 2004.
- Every rational polytope = a face of a slim (r,c,3) 3-way axial transportation polytope, poly-time. d-way integer table w/ prescribed marginals NP-complete.
- => 2c (variety-typed >=3 contexts UNIVERSAL) = direct corollary. KNOWN.

## Scout 2 DONE: AB/CSW/KCBS (R1 framing + Family-II)
- AB 2011 (NJP 13 113036, arXiv:1102.0264) OWNS definitional core: presheaf compatibility = EA (agree on overlaps); global section = PR; contextuality = EA\PR = obstruction to global section. Thm 8.1: PR <=> factorizable HV model. Their Sec 5: no-signalling = extendable by SIGNED measure => C\R gap IS the AB positive-vs-signed global-section gap. MUST-CITE load-bearing.
- CSW 2014 (PRL 112 040401) OWNS polytope-bound half: S <= alpha (stable-set, classical) <= theta (Lovasz, quantum) <= alpha* (fractional packing, no-disturbance) on exclusivity graph; Result 3: classical=quantum iff perfect graph (SPGT); gap on odd holes/antiholes. E1 polytope = clique inequalities. MUST-CITE.
- KCBS 2008 (PRL 101 020403) OWNS minimal witness: pentagon C5, alpha=2, theta=sqrt5, alpha*=5/2. MUST-CITE.
- Extra must-cite for explicit C=R polytope phrasing: Fine 1982 (PRL 48 291); Pitowsky correlation polytopes.
- Residual crack: literal set-equality "C=R as marginal polytope" not stated verbatim by CSW (they do functional bounds) nor as explicit H-polytope by AB (cohomological). Thin. Dynamical framing genuinely outside all three (= framing not theorem).

## Extra (verified personally): Pitowsky + AIIS
- Pitowsky 1991 "Correlation polytopes: their geometry and complexity" Math. Prog. 50:395-414: membership NP-complete, facets prob not in NP. = the complexity floor. Boole "conditions of possible experience" lineage.
- Avis-Imai-Ito-Sasaki (quant-ph/0505060, J.Phys.A 38 2005): two-party Bell polytope <-> CUT POLYTOPE via triangular elimination / covariance map. Mixed-weight facets expected. On paper's shelf; confirmed.

## Dynamical-framing novelty check (verified personally): NO PRIOR ART
- Searches for temporal/cyclic contextuality x symbolic dynamics / periodic orbits / golden-mean shift / stable-set polytope: nothing links contextuality-marginal-polytope machinery to subshift periodic-orbit recurrence in the observation-window sense. Supports novelty concentrated in dynamical layer.

## Scout 1 DONE: 2a
- Vorobev 1962 (Theory Probab Appl 7(2):147) OWNS exact iff: "regularity" of complex = N&S for extendability of EVERY consistent family; regularity == alpha-acyclicity. Necessity included.
- BFMY 1983 (JACM 30(3):479) database mirror iff: alpha-acyclic <=> pairwise-consistent => globally-consistent; RIP/GYO/lossless-join equiv.
- Kellerer 1964 EXCLUDED: sufficiency only (decomposable => extends) + broader Frechet/duality.
- Cross-field id (Vorobev-regularity == db-acyclicity): Barbosa via Abramsky 2012/2013 (arXiv:1208.6416, "Relational Databases and Bell's Theorem"). 2a = KNOWN.

## Scout 3 DONE: tamings/parity/dichotomy
- Hoffman-Gale APPENDIX to Heller-Tompkins 1956 owns 2-nonzeros-per-col signing => TU (NOT the HT main text - citation-hygiene flag). Hoffman-Kruskal 1956 = TU iff integral for all b.
- Nemhauser-Trotter 1974 = FSTAB=STAB iff bipartite + half-integrality of vertices. Chvatal 1975 = odd-cycle facet Sum <= (|C|-1)/2, t-perfect. Ghouila-Houri 1962 = TU equitable-bicoloring. Konig 1931.
- SPGT (CRST 2006) + recognition O(n^9) CCLSV 2005; STAB=clique-ineqs iff perfect (Fulkerson/Lovasz/Chvatal).
- DISCRIMINATOR CONFIRMED: projection-equality (LOC=M, realisability) sits strictly ABOVE satisfiability-width (LOC=empty iff M=empty, Barto-Kozik 2014). BUT realisability has its OWN owners paper must clear: Thapper-Zivny 2012/2016 (BLP tight iff fractional symmetric polymorphism) + Prusa-Werner 2013 (local marginal polytope universality) + Weller 2016 (tightness via forbidden signed minors). R5 differentiation from CSP-SAT is correct but INSUFFICIENT.

## LG + covers (verified personally)
- Leggett-Garg 1985 = canonical temporal contextuality/macrorealism; NSIT (Kofler-Brukner; Halliwell arXiv:1704.01485) = no-signalling-in-time refinement; Fine's thm applies (augmented LG N&S). MUST place/cite. But none does cyclic-time marginal-polytope over subshift periodic orbits.
- Voltage-graph/cover x stable-set integrality: found Gerards t-perfect (no bad-K4 subdivision) but NOTHING linking cyclic covers to marginal-realisability integrality. Winding/primitive-orbit criterion survives NOVEL.

## FINAL VERDICTS
R1 KNOWN-translation (WJ local/marginal polytope + AB compatible-family/global-section). Type 6.
2a KNOWN (Vorobev + BFMY + Barbosa/Abramsky).
2b KNOWN-folklore (product measure; independence).
2c KNOWN (De Loera-Onn 2004 + Prusa-Werner 2013; Pitowsky NP-complete floor).
R3 parity NOVEL-REFINEMENT (polytope mechanism classical: Nemhauser-Trotter/Chvatal/Hoffman-Kruskal; refinement = golden-mean/recurrence dressing only).
R4 tamings: individual facts KNOWN/renamed; catalogue-as-structure is the only contribution vehicle.
R5 Circuit Localization NOVEL (assembly + winding/primitive-orbit criterion) IF differentiated from Thapper-Zivny + Prusa-Werner, not just Barto-Kozik.
Genuine survivor: dynamical/observational EA-PR framing + recurrence-as-cyclic-time + winding criterion + assembly. Type 3 clears ONLY if parity/winding are unobtainable without the framework; else Type 6.
