# Dilation question: scoping verdict

*Scoping round completed 2026-08-03. Hand proofs only; no Lean changes.*

**Verdict labels.** Phase 0: **PARTIALLY ANSWERED; GENERAL CASE OPEN**.
Boolean engine: **VERIFIED, WITH A METRIZABILITY QUALIFICATION AND AN
ADDITIONAL OMP EXTENSION GATE**. Compact-\(P\)-space claim: **REFUTED AS
STATED**. Quarantine comparison: **SAME BOOLEAN PREMEASURE ENGINE; NOT AN
OMP DILATION THEOREM**. Programme disposition: **ADJACENT — DO NOT COMMIT
MONTHS ON THE PRESENT EVIDENCE**.

## The question and the quantifiers

For an OMP \(P\), write \(D(P)\) for the assertion that for every finitely
additive state \(m\) on \(P\) there are an OMP embedding
\(\phi:P\hookrightarrow Q\), a sigma-orthocomplete OMP \(Q\), and a
sigma-additive state \(s\) on \(Q\) such that

\[
  m=s\circ\phi.
\]

The embedding is not required to preserve countable joins. This is essential:
by Lemma R in
[regularity_sigma_additivity_pullback.md](regularity_sigma_additivity_pullback.md),
the mass lost by a countable join in \(P\) is exactly the \(s\)-mass of the
ambient gap.

## Phase 0 — literature gate

### Finding

**D is partially answered, but the general assertion is open.** No theorem
answering the displayed state-preserving sigma-complete dilation question was
located in the specified monographs or in the state-extension and completion
literature, and no general counterexample was located. More positively, the
two halves immediately adjacent to D are known, and their mismatch locates the
open step precisely.

1. **The finitely additive enlargement is known.** Navara, Pták, and
   Rogalewicz, [*Enlargements of quantum
   logics*](https://msp.org/pjm/1988/135-2/pjm-v135-n2-p10-s.pdf), Theorem
   2.2, prove that for every logic \(P\) and every state \(m\in S(P)\) there
   is an embedding \(e:P\hookrightarrow R\) into a rigid logic \(R\) whose
   unique finitely additive state restricts to \(m\). Their theorem is
   state-specific and uses the right ordinary embedding notion, but it does
   not make \(R\) sigma-complete or its state sigma-additive.

2. **The state-free sigma-completion problem is also open.** Harding and Wang,
   [*Logical aspects of quantum
   structures*](https://arxiv.org/abs/2108.09819), Problem 2, ask whether
   every OML/OMP embeds into a sigma-complete OML/OMP. For each state-bearing
   \(P\), a witness to \(D(P)\) would in particular supply such an embedding
   and would add a prescribed-state sigma-additivity requirement. Problem 2
   also ranges over stateless OMPs, for which D is vacuous, so it is adjacent
   rather than literally a weaker assertion. It nevertheless confirms that no
   general sigma-completion machine is currently available. The 1988
   rigid-enlargement theorem does not bridge this gap.

3. **The older sigma-complete enlargement result is conditional.** Pták,
   [*Exotic logics*](http://eudml.org/doc/266236), Appendix, says explicitly
   that the preceding enlargement constructions do not in general produce a
   sigma-complete logic. Theorem 4.1 handles already sigma-complete source
   logics in two special regimes and preserves a two-valued state only when
   that state is already sigma-additive. It does not dilate an arbitrary
   finitely additive state.

4. **Known extension theorems stop at finite additivity or special operator
   structures.** Hamhalter, Navara, and Pták,
   [*States on orthoalgebras*](https://doi.org/10.1007/BF00676255), prove
   finite-additive state-extension admissibility for Boolean and Hilbertian
   orthoalgebras. Hamhalter's [*Quantum Measure
   Theory*](https://doi.org/10.1007/978-94-017-0119-8), Chapter 10, treats
   restrictions and extensions in the projection/operator-algebraic setting.
   Pták–Pulmannová's [*Orthomodular Structures as Quantum
   Logics*](https://link.springer.com/book/9780792312079) and
   Dvurečenskij's [*Gleason's Theorem and Its
   Applications*](https://doi.org/10.1007/978-94-015-8222-3) provide the
   standard OMP and Gleason-side theory, but no general sigma-complete
   state-preserving enlargement theorem was found there.

The literature verdict is therefore not “unmentioned, hence open.” It is
**open after a positive finite-additive theorem and alongside an explicitly
open sigma-completion problem**.

### Positive regimes already on record

- **Boolean algebras:** all states lift, by the compact Stone-space argument
  below (equivalently Fremlin 416Q).
- **Finite OMPs:** every countable orthogonal family has only finitely many
  nonzero members, so every state is sigma-additive and the identity works.
- **States already sigma-additive on sigma-complete OMPs:** take the identity
  embedding.
- **Projection lattices without a type-\(I_2\) summand:** Bunce–Wright's
  [Mackey–Gleason theorem](https://arxiv.org/abs/math/9204228) extends a
  finitely additive probability on projections to a positive functional.
  Its GNS representation, direct-summed with a faithful representation,
  embeds the projection OMP into a complete Hilbert projection lattice; the
  GNS vector state is normal and pulls back to the prescribed state. Hence D
  is affirmative in this operator-algebraic regime.
- **The incomplete-inner-product-space example:** the state \(m_x\) on
  \(E(S)\) in Dvurečenskij–Neubrunn–Pulmannová lifts along
  \(M\mapsto\overline M\) into \(L(\overline S)\) to the corresponding vector
  state; this is already their Example 2.3
  [construction](https://doi.org/10.1090/S0002-9939-1992-1045591-0).

These are genuine partial answers, not evidence for an unrestricted OMP
theorem.

## Phase 1 — what the Boolean lift runs on

### The engine

Let \(B\) be a Boolean algebra, \(X=S(B)\) its Stone space, and
\(b\mapsto\widehat b\) its clopen representation. If
\(C,C_n\in\operatorname{Clopen}(X)\), the \(C_n\) are pairwise disjoint, and

\[
  C=\bigsqcup_{n\in\mathbb N}C_n,
\]

then \((C_n)\) is an open cover of the compact set \(C\). A finite subfamily
covers \(C\), and disjointness forces every remaining \(C_n\) to be empty.
Consequently every finitely additive charge on the clopen algebra is a
premeasure: the only countable disjoint decompositions whose union remains in
the algebra are effectively finite.

Carathéodory therefore extends the charge to
\(\sigma(\operatorname{Clopen}(X))=\operatorname{Baire}(X)\). If \(X\) is
compact metrizable, as in the quarantine theorem, Baire equals Borel. For an
arbitrary Stone space, the elementary Carathéodory conclusion is a Baire
measure; the representing Radon Borel measure uses the additional
Riesz/regularity result recorded in Fremlin,
[*Measure Theory*, 416Q](https://www1.essex.ac.uk/maths/people/fremlin/chap41.pdf).

Thus the proposed correction is right with one qualification:
**compactness is the premeasure engine; Stone duality supplies the compact
zero-dimensional representation on which that engine runs.** It is too strong
to say Stone duality plays no role, but it is not the reason finite additivity
upgrades to countable additivity.

For pairwise disjoint \(b_n\in B\) with \(b=\bigvee_n b_n\) existing in \(B\),
Fremlin [313C](https://www1.essex.ac.uk/maths/people/fremlin/chap31.pdf) gives

\[
  \widehat b=\overline{\bigcup_n\widehat{b_n}}.
\]

Writing \(U_n=\widehat{b_n}\) and
\(G=\widehat b\setminus\bigcup_nU_n\), the extension \(\mu\) satisfies

\[
  m(b)=\sum_n m(b_n)+\mu(G).
\]

This is exactly the Boolean instance of Lemma R's gap identity.

### What the same route would require for an OMP

The finite-disjoint-cover property is the sigma step, but it is **not by
itself an OMP dilation theorem**. A compact/Carathéodory lift for a state
\(m\) on an OMP \(P\) needs all of the following:

1. a faithful concrete embedding of \(P\) as clopen events on a compact base
   \(X\);
2. extension of \(m\) from those OMP events to a finitely additive charge on a
   Boolean algebra (or another Carathéodory premeasure domain) of clopen events
   containing them;
3. the finite-disjoint-cover property on that domain, supplied by compactness;
4. Carathéodory extension to its generated sigma-algebra, which supplies the
   sigma-complete ambient OMP and sigma-additive state.

Step 2 is the missing non-Boolean gate. A state on an OMP is additive only on
its defined orthogonal sums; it need not extend to a charge on the Boolean
algebra generated by a concrete representation. Finite concrete logics already
exhibit failures of such Boolean-envelope state extension (see De Simone,
Navara, and Pták, [*Extending states on finite concrete
logics*](https://arxiv.org/abs/math-ph/0311012)). Those finite logics still
satisfy D by the identity embedding, so Boolean-envelope extension is a
sufficient route, not a necessary reformulation of D.

The precise correction is therefore: a Boolean-style OMP lift needs a compact
representation base **plus state extension to a clopen premeasure domain**.
Merely requiring the images of \(P\) to have the finite-disjoint-cover property
omits the hard extension step.

### The compact-\(P\)-space claim

The claim

\[
  \operatorname{Clopen}(S(B))\hookrightarrow\operatorname{Baire}(S(B))
  \text{ is non-sigma-regular}
  \quad\Longleftrightarrow\quad
  B\text{ is infinite}
\]

is **refuted**.

Let \(I\) be uncountable and let \(B\) be the finite–cofinite algebra on
\(I\). Its Stone space is the one-point compactification
\(X=I\cup\{\infty\}\) of the discrete space \(I\). The algebra \(B\) is
infinite. Nevertheless its clopen inclusion is sigma-regular. Indeed, for a
countable family \((A_n)\subseteq B\):

- if some \(A_n\) is cofinite, then \(\bigcup_nA_n\) is cofinite and is the
  join in \(B\);
- if every \(A_n\) is finite and their union is finite, that union is the join;
- if every \(A_n\) is finite and their union is infinite, the union is
  countable and not cofinite, and there is no least cofinite upper bound, so
  the join does not exist in \(B\).

Thus every countable join that exists in \(B\) is already the set union, and
the inclusion preserves it; meets follow by complementation.

The proposed \(P\)-space fact is true but does not imply the claim. In a
zero-dimensional space, “every countable union of clopens is clopen” implies
the \(P\)-space property. Every compact Hausdorff \(P\)-space is finite: if it
were infinite, choose a countably infinite subset \(A\); \(A\) is closed
because its complement is a countable intersection of open complements of
points, hence \(A\) is compact, while the countable \(P\)-space \(A\) is
discrete, a contradiction. The error is that sigma-regularity constrains only
countable families whose join already exists in \(B\); it does not say every
countable union of clopens is clopen.

## Phase 2 — comparison with the quarantine theorem

### Exact statement from the paper of record

The paper of record is
[papers/spine/spine_body.tex](../papers/spine/spine_body.tex). Theorem
thm:quarantine assumes that \(X\) is compact, zero-dimensional, and
metrizable, and states:

1. every finitely additive two-valued state on a **Boolean subalgebra**
   \(B\subseteq\operatorname{Clo}(X)\) is the restriction of a point
   evaluation;
2. every finitely additive probability charge on
   \(\operatorname{Clo}(X)\) is a premeasure and extends uniquely to a Borel
   probability measure;
3. every charge on a Boolean subalgebra of \(\operatorname{Clo}(X)\) extends,
   first by Horn–Tarski to \(\operatorname{Clo}(X)\), then by part 2 to a
   Borel measure.

Its conclusion is that sigma-essential realization failure is impossible on
these compact clopen Boolean carriers; after a charge exists on the generated
Boolean algebra, there is no further countable-additivity obstruction.

### Proof-mechanism audit

- **Part 1 uses a different compactness mechanism:** extend the value-one
  filter to a clopen ultrafilter, then use the finite-intersection property of
  closed subsets of compact \(X\) to obtain a realizing point.
- **Part 2 uses exactly the Boolean-lift mechanism:** a countable disjoint
  clopen cover of a clopen set has a finite subcover, so a charge is a
  premeasure.
- **Part 3 is Horn–Tarski plus part 2:** finite-additive extension is supplied
  algebraically; compactness then supplies the sigma upgrade.

Therefore the shared compactness hypothesis is not a coincidence. Parts 2–3
are literally the compactness engine identified in Phase 1; part 1 is a second
compactness argument. The roles of the other hypotheses are separate:
zero-dimensionality supplies the clopen Boolean base, while metrizability
makes the sigma-algebra generated by that base the full Borel sigma-algebra.

### Regime actually covered

The corpus already contains D for the following exact regime:

\[
  B\subseteq\operatorname{Clo}(X),\qquad
  X\text{ compact, zero-dimensional, metrizable},
\]

where \(B\) is a Boolean subalgebra and the state is a charge on \(B\). Take
\(Q=\operatorname{Bor}(X)\); Horn–Tarski followed by Carathéodory supplies the
sigma-additive state. More generally, the same conclusion holds for an OMP
state **already known to extend to such a Boolean clopen envelope**.

It does **not** follow for an arbitrary OMP of clopen events. The theorem says
“Boolean subalgebra” and “charge”; its proof uses Boolean intersections,
inclusion–exclusion, and Horn–Tarski. None is available for a general OMP
state. Hence the corpus contains the Boolean-envelope layer of the lift, not
the missing OMP state-extension layer. The thread is **corpus-internal at the
Boolean mechanism and adjacent at D**.

## Phase 3 — scope memo

**Status.** General D remains open. It is settled affirmatively for Boolean
algebras, for finite OMPs, for the operator-algebraic projection regime
without type \(I_2\), for states already sigma-additive on their
sigma-complete carrier, and for individual spatial examples such as
\(E(S)\hookrightarrow L(\overline S)\). The arbitrary OMP case is beyond the
current completion and extension theorems. The concrete-OMP case is not closed
by quarantine: concreteness gives an event representation, but not extension
of every OMP state to its Boolean envelope.

**Corpus coverage.** The quarantine theorem already contains exactly the
compact premeasure step and, by Horn–Tarski, the full dilation for its Boolean
clopen subalgebras. It does not answer D for the corpus's non-Boolean OMP
carriers unless a Boolean-envelope charge extension has separately been
proved.

**Smallest named open checkpoint located.** Finite OMPs are closed by the
identity argument above. The first explicit published infinite non-Boolean
checkpoint located is Navara's \(M=\mathbb N\) sigma-orthocomplete OML
\(\mathcal L_{\mathbb N}\) from
[*Regularity and sigma-additivity of states on quantum
logics*](https://doi.org/10.1090/S0002-9939-1992-1079705-3). Its sublogic
\(\{1\mid C:C\subseteq\mathbb N\}\) of characteristic elements is isomorphic to
\(\mathcal P(\mathbb N)\), and every state on that sublogic extends uniquely
to \(\mathcal L_{\mathbb N}\). Choose the free-ultrafilter state; its unique
extension is not sigma-additive. Whether that prescribed state has a
sigma-additive dilation along some OMP embedding is not answered by the
located results. This is a named checkpoint, not a claim of cardinal
minimality.

**Disposition.** Do not make a months-scale commitment from this thread.
The reusable mechanism is already in the corpus, while the missing step is a
general OMP state-extension/completion problem adjacent to a longstanding open
structural problem. A later targeted test of Navara's
\(\mathcal L_{\mathbb N}\) could be worthwhile, but a general attack on D is
an adjacent paper, not unfinished work on the sigma-essential paper.

**Completion/concreteness flag.** A Stone-type route needs a faithful set
representation, equivalently enough two-valued states. Harding–Wang Remark
3.14 records that concrete OMLs are not closed under MacNeille or canonical
completion. This is an obstruction to the compact-representation strategy:
adjoining the required joins by either standard completion can destroy the
very concreteness on which that strategy depends. It is not an obstruction to
D itself, because D neither requires a concrete ambient nor requires either
standard completion, and its embedding may be deliberately nonregular. Thus
the remark identifies a route-specific obstruction, not a general
counterexample and not a coincidence.
