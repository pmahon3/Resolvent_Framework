## Audit: seed.md (constructive general Lovász Local Lemma via resampling) (mode: full)

Audit date per AS_OF.md: **2009-03-02**. Only sources on or before that date are counted as prior art. The submission's own text, under any title, is not prior art. I used web search results only to identify and date pre-2009 works, and ignored everything they said about later developments.

### Declared contribution type(s): Type 2 (new proof), Type 3 (unifying framework)
The seed declares types, but it does not state the specific per-type bars it commits to. Its main content is an algorithmic theorem (Type 1), which it does not declare. See the cross-reference section.

### Sources consulted (read level, date)
- Lovász Local Lemma: Erdős–Lovász 1975; general/asymmetric form in Spencer 1977 and Alon–Spencer, *The Probabilistic Method* (2nd ed. 2000, Ch. 5). Read level: known from memory (textbook). Predates.
- J. Beck, "An algorithmic approach to the Lovász Local Lemma", *Random Struct. Alg.* 2 (1991). Read level: secondary (cited in search abstracts and in standard knowledge). Predates.
- N. Alon, "A parallel algorithmic version of the Local Lemma", *Random Struct. Alg.* 2 (1991). Read level: secondary. Predates.
- M. Molloy, B. Reed, "Further algorithmic aspects of the Local Lemma", STOC 1998. Read level: secondary (abstract fragment via the Srinivasan record). Predates.
- A. Czumaj, C. Scheideler, "Coloring nonuniform hypergraphs: a new algorithmic approach to the general Lovász local lemma", *Random Struct. Alg.* 17 (2000), 213–237, plus the SODA 2000 version. Read level: abstract/bibliographic record. Predates. This is the main prior algorithmic work on the **general (asymmetric)** lemma, under restricted conditions.
- A. Srinivasan, "Improved algorithmic versions of the Lovász Local Lemma", SODA 2008. Read level: bibliographic record plus abstract fragment. Predates.
- R. A. Moser, "Derandomizing the Lovász Local Lemma more effectively", arXiv:0807.2120 (July 2008). Read level: secondary (citation in the 0810.4812 text). Predates. Neighbourhood bound about 2^{k/2} for k-SAT.
- R. A. Moser, "A constructive proof of the Lovász Local Lemma", arXiv:0810.4812 (October 2008; the STOC 2009 version had not yet appeared on the audit date). Read level: abstract and introduction (ar5iv), checked 2026-10-26. Predates. It gives resampling for bounded-degree k-SAT under a near-optimal **symmetric** condition (neighbourhood about 2^{k-5}; the versions I saw disagree on the constant), with a counting/"log" analysis. **This is the nearest prior art.** It is a separate, earlier paper, so I treat it as prior art and not as the submission.
- arXiv:0903.0544 ("A constructive proof of the general Lovász Local Lemma") appeared in search results. It is the submission itself and is dated after the audit date, so I **ignored** it as prior art and did not use its content.
- Date uncertainty: the exact posting date of the versions of 0810.4812 (v1 versus v2 bound constants) is unclear. Either version predates 2009-03-02, so the uncertainty does not change any verdict.

### Pure Verdict: NOVEL (as an algorithmic theorem, in the variable setting)
With the vocabulary stripped, the claim is this. Events are determined by independent random variables, and the dependency graph joins events that share variables. Suppose there are x_A ∈ (0,1) with P(A) ≤ x_A ∏_{B∈Γ(A)} (1 − x_B), which is the asymmetric LLL condition. Then the algorithm "while some bad event holds, pick one and resample its variables" halts after at most Σ_A x_A/(1 − x_A) expected resamplings in total. Existence of a good assignment follows as a corollary, which gives a new proof of the LLL in this setting.

Search, across the names constructive LLL, algorithmic LLL, general/asymmetric LLL algorithm, resampling, and Beck's method:
- Beck, Alon, Molloy–Reed, Czumaj–Scheideler and Srinivasan all reach only **weakened** conditions: polynomially or exponentially lossy relative to the LLL, or restricted structure (bounded event size, bounded degree). None reaches the exact general condition.
- Moser (0810.4812) reaches a near-optimal condition, but only for the **symmetric** k-SAT case, with a constant-factor loss and a counting argument specific to that setting. The seed has **no** constant loss, works for arbitrary events in the variable model, and covers the **asymmetric** condition. The witness-structure charging argument (a "witness tree" in the referee's words) is not in any pre-2009 source I found.
- Could an expert call it "obvious" or a "trivial consequence of Moser 2008"? No. Extending Moser's analysis to the exact asymmetric condition requires a new accounting device: each resampling is charged to a structure whose probability is bounded by a product of P(A)s, and that product is summed against a Galton–Watson-type branching weight. Moser's counting does not give this.

**Correctness and scope flag.** The seed says it works "under the conditions of the general lemma". Stated that way, this overreaches. The analysis needs the **variable setting**: events determined by independent variables, with the dependency graph induced by shared variables. The abstract LLL allows any dependency graph for which each event is mutually independent of its non-neighbours. That includes settings such as random permutations, Hamiltonian cycles, and the lopsided LLL, which a variable-resampling algorithm does not cover directly. So "a new proof of the lemma" is a proof of the variable-model LLL, not of the fully general lemma. The claim of "constructive versions of nearly all known uses" carries the same caveat. The central claim is correct within its proper scope. I verified this by reconstructing the argument from the seed's description and standard knowledge; I did not formalise it. The scope sentence must be fixed.

### Applied Verdict: CONDITIONAL
- Decision test: the result does change practice. Any LLL application in the variable model becomes a randomized polynomial-time algorithm with no case-specific engineering, replacing Beck-style multi-phase constructions.
- Practitioner test, "I already use Beck/Molloy–Reed/Srinivasan": those methods lose in the exponent or the constants and need per-application work. This one needs only the LLL hypothesis itself and is a three-line algorithm.
- Computational comparison: none is offered. For a theoretical algorithms result, the "experiment" is the proven running-time bound, which the seed states. Regime boundaries are sharp: exactly the asymmetric LLL condition, in the variable model. Reproducibility is trivial.
- Conditional on (i) the variable-model scope being stated, and (ii) the expected-running-time bound being made explicit, including the cost of finding a violated event when there are exponentially many events.

### Contribution Type Verdicts (mode=full):

Type 2 (New proof of known result): **PASS**
The bar needs at least one of three things: (a) a technique applicable elsewhere, (b) an unexpected connection, (c) a substantial simplification.
- (c) holds. The proof of the variable-model LLL is short, and it is **constructive** where the classical proof is not.
- (a) holds. The witness-structure charging of a resampling process is a general technique for analysing local-search and resampling algorithms, and it can be reused for other "fix a violated constraint" dynamics.

The gain is methodological as well as conceptual, so this is not "merely an alternative route". Caveat: the new proof covers the variable-model LLL only, not the full abstract lemma.

Type 3 (Unifying framework): **FAIL** (as declared)
The bar is method transfer: a technique from domain A becomes usable in domain B through the framework.
- What the seed offers is one general theorem, with constructive versions of applications as corollaries. These applications were already unified by the LLL itself; the seed makes the shared tool algorithmic.
- That is a strengthening of a single tool within one field (probabilistic combinatorics and algorithms). It is not a framework showing that previously unrelated results are instances of one phenomenon, and it does not transfer a technique between domains.
- The "applications" are instantiations of a new theorem, not transfers. The value is real, but it belongs to Type 1/2, not Type 3.

Undeclared Type 1 (New theorem): **would PASS.** The constructive asymmetric LLL with the explicit Σ x_A/(1 − x_A) bound is not in the pre-2009 literature found (see Pure Verdict). The seed should redeclare it.

### Cross-reference
The components are partly known:
- resampling for symmetric k-SAT: Moser 2008;
- algorithmic LLL under lossy conditions: Beck 1991 → Srinivasan 2008;
- the general LLL as an existence result.

The step to the **exact general (asymmetric) condition**, with a charging argument that also gives the existence statement, is new. The pure novelty and Type 2 hold together, because the same argument does both jobs. Type 3 fails only because the seed classified itself wrongly. Its honest types are 1 + 2.

### Recommendation
**Proceed to Phase 3**, scoped to Type 1 (redeclare it) and Type 2. Drop Type 3. Before drafting:
1. Restate the scope as "the variable-model (general/asymmetric) LLL", and qualify "nearly all known uses".
2. Credit Moser arXiv:0810.4812 explicitly as the symmetric k-SAT precursor, and differentiate from it: asymmetric condition, no constant loss, arbitrary events, the witness-structure analysis.
3. Credit Czumaj–Scheideler 2000 as the prior algorithmic attack on the general (asymmetric) lemma.

Bearing on the why: this result is about local repair with no centre. Each violated constraint is fixed locally, and a global consistent state emerges. It is a lens on "order from local relations", and the gap to any applied ecology claim is large.

### Referee estimate: ACCEPT-LIKELY
Venue class: research journal (top-tier theory: STOC/FOCS, then J. ACM-class)
Value carried by: factor 1 (new theorem: exact constructive general LLL) and factor 2 (constructive, markedly simpler proof of the variable-model LLL)
Main risk a referee would raise: novelty over Moser's own arXiv:0810.4812 must be stated precisely, and "conditions of the general lemma" must be restricted to the variable model (permutation/lopsided settings are not covered).
