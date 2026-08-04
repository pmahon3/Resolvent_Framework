# Regularity and sigma-additivity under pullback

*Gate check completed 2026-08-03. Hand proof only; no Lean changes.*

**Verdict labels.** Lemma R(a): **VERIFIED**. Lemma R(b): **VERIFIED,
WITH THE SHARPER EXACT IDENTITY**. OMP gate: **SURVIVED**. Novelty:
**FOLKLORE — NOT NOVEL**. The blanket Boolean assertion that the canonical
clopen inclusion is always non-sigma-regular: **REFUTED**. The Boolean lifting
assertion: **ALL FINITELY ADDITIVE STATES**, not merely a subclass.

## Definitions and convention

An embedding \(\phi:P\to Q\) of orthomodular posets is injective, preserves
orthocomplementation, and preserves finite orthogonal joins. In particular it
preserves \(0,1\) and order. It is **regular** when, for every family whose join
or meet exists in \(P\), the corresponding join or meet of the images exists
in \(Q\) and equals the image of the join or meet. It is
**sigma-regular** when the same assertion is required only for countable
families. Regularity and sigma-regularity are not identified below, and neither
is part of the definition of an embedding.

A state \(s:Q\to[0,1]\) has \(s(1)=1\) and is additive on finite orthogonal
joins. It is sigma-additive when

\[
  s\!\left(\bigvee_{n=1}^{\infty}q_n\right)
    =\sum_{n=1}^{\infty}s(q_n)
\]

for every countable orthogonal family for which the displayed join exists.

In the OMP literature, “sigma-complete quantum logic” commonly means
**sigma-orthocomplete**: every countable orthogonal family has a join. That is
the only completeness used here. If “sigma-complete” is instead read as the
stronger existence of joins for all countable subsets, the proof remains
valid, but the hypothesis is stronger than necessary and in particular
already supplies binary joins.

## Phase 0 — prior-art finding

**Finding: FOLKLORE — NOT NOVEL.** No verbatim statement of Lemma R, and no
named “gap element” pullback lemma, was located in the specified books.
Nevertheless, neither part clears a novelty bar. Part (a) is immediate from
the standard definitions of a sigma-homomorphism and a sigma-additive state;
part (b) is the standard OMP orthogonal-difference identity followed by finite
and countable additivity.

The following checks were made.

- Pták and Pulmannová, [*Orthomodular Structures as Quantum
  Logics*](https://books.google.com/books?id=wymaAAAAIAAJ), Chapter 2,
  especially section 2.2, treat states and sigma-homomorphisms. A searchable
  check did not locate the exact pullback-gap formulation.
- Dvurečenskij, [*Gleason's Theorem and Its
  Applications*](https://books.google.com/books?id=Z3zvCAAAQBAJ), pp. 74–75,
  records the standard homomorphism/sigma-homomorphism terminology. A
  searchable check did not locate the exact formulation.
- Hamhalter, [*Quantum Measure
  Theory*](https://link.springer.com/book/10.1007/978-94-017-0119-8), section
  8.1, p. 254, gives the analogous additive and sigma-additive orthomorphism
  terminology in projection structures. It does not supply novelty for the
  elementary composition argument.
- Dvurečenskij, Neubrunn, and Pulmannová, [“Regular States and Countable
  Additivity on Quantum
  Logics”](https://doi.org/10.1090/S0002-9939-1992-1045591-0), pp. 931–932,
  state the OMP orthomodular axiom and the definition of a countably additive
  state used below. Their “regular state” is a different, measure-theoretic
  notion; it is not regularity of an embedding and is not Lemma R.

Thus the exact packaging was not found as a citable named proposition, so a
short derivation is recorded. Its content is still standard and no novelty is
claimed.

Two read-only repository results do not change this assessment.
[`FullCycleAssemblyKernel.lean`](../formalization/QuerySystem/QuerySystem/FullCycleAssemblyKernel.lean)
derives binary join and meet preservation from monotone retractions; it is
finitary and says nothing about states or countable joins.
[`KernelClosureCalculus.lean`](../formalization/QuerySystem/QuerySystem/KernelClosureCalculus.lean)
gives finite/order-theoretic criteria for failure of join preservation; it
can diagnose a particular non-preserving embedding but does not prove the
sigma-additivity identity.

## Phase 1 — OMP proof

Let \((x_n)_{n\geq 1}\) be a countable orthogonal family in \(P\), suppose

\[
  a:=\bigvee_{n=1}^{\infty}x_n
\]

exists in \(P\), and set

\[
  x:=\bigvee_{n=1}^{\infty}\phi(x_n)\quad\text{in }Q,
  \qquad y:=\phi(a).
\]

The requested six checks are as follows.

1. **The images are pairwise orthogonal.** If \(n\ne m\), then
   \(x_n\leq x_m'\). Order and orthocomplement preservation give
   \(\phi(x_n)\leq\phi(x_m')=\phi(x_m)'\), so
   \(\phi(x_n)\perp\phi(x_m)\).

2. **The ambient join exists.** The family in step 1 is countable and
   orthogonal. Sigma-orthocompleteness of \(Q\) therefore supplies \(x\). This
   is the only point at which the global completeness hypothesis on \(Q\) is
   used.

3. **The order relation and the proposed gap are valid.** For every \(n\),
   \(x_n\leq a\), hence \(\phi(x_n)\leq y\). Since \(x\) is their least upper
   bound, \(x\leq y\). Consequently \(y'\leq x'\), and equivalently
   \(x\perp y'\). The orthogonal join \(x\vee y'\) therefore exists, and

   \[
     g:=(x\vee y')'
   \]

   is well defined.

4. **The OMP orthogonal-difference decomposition holds.** Because
   \(x\vee y'\) exists, De Morgan duality identifies

   \[
     g=(x\vee y')'=x'\wedge y.
   \]

   This does not assume that arbitrary meets exist: this particular meet
   exists as the complement of the already-existing orthogonal join. The OMP
   orthomodular law for \(x\leq y\) now gives

   \[
     y=x\vee(y\wedge x')=x\vee g.
   \]

   Since \(g\leq x'\), the join is orthogonal: \(x\perp g\).

5. **Apply the two additivity axioms.** Finite additivity at the decomposition
   in step 4 gives

   \[
     s(y)=s(x)+s(g).
   \]

   Sigma-additivity at the image family gives

   \[
     s(x)=\sum_{n=1}^{\infty}s(\phi(x_n)).
   \]

6. **Exact defect formula.** Combining step 5 yields

   \[
     \boxed{
     s\!\left(\phi\!\left(\bigvee_{n=1}^{\infty}x_n\right)\right)
       =\sum_{n=1}^{\infty}s(\phi(x_n))+s(g).}
   \]

Before countable additivity is considered, \(s\circ\phi\) is already a state
on \(P\): bounds are preserved, and preservation of each finite orthogonal
join followed by finite additivity of \(s\) proves finite additivity of the
pullback.

For Lemma R(a), sigma-regularity gives \(y=x\), so \(g=0\); the boxed formula
proves sigma-additivity of \(s\circ\phi\). For Lemma R(b), no regularity of
\(\phi\) is assumed. Since states are nonnegative, the boxed formula shows
that the pullback equality fails at \((x_n)\) if and only if \(s(g)>0\).

The hypotheses can be sharpened without changing the result. For the single
family in (b), it is enough to assume that \(\bigvee_n\phi(x_n)\) exists in
\(Q\); global sigma-orthocompleteness is only a uniform existence condition.
For (a), preservation of countable **orthogonal** joins is enough. Full
sigma-regularity, including preservation of every existing countable
nonorthogonal join and the dual meets, is strictly more than this proof uses.
Arbitrary regularity is not used. Injectivity is also not used in the
calculation, although it is part of the fixed meaning of “embedding.”

## Phase 2 — Boolean case

Let \(B\) be a Boolean algebra, let \(S=S(B)\) be its Stone space, and write
\(\widehat b\) for the clopen corresponding to \(b\in B\). The Stone map
identifies

\[
  B\cong\operatorname{Clopen}(S)
\]

and the canonical inclusion

\[
  j:\operatorname{Clopen}(S)\hookrightarrow\operatorname{Baire}(S)
\]

is a Boolean, hence OMP, embedding. For a countable family \((b_n)\) whose
join \(b=\bigvee_n b_n\) exists in \(B\), Fremlin's Stone-space formula is

\[
  \widehat b
    =\overline{\bigcup_{n=1}^{\infty}\widehat{b_n}}.
\]

See Fremlin, [*Measure Theory*, Chapter 31, 313C and
313L](https://www1.essex.ac.uk/maths/people/fremlin/chap31.pdf). In the Baire
sigma-algebra, by contrast, the join of the image sets is their union.

The prompt's unqualified assertion that this inclusion **is not**
sigma-regular is false. For example, if \(B\) is finite, every subset of its
finite Stone space is clopen, so
\(\operatorname{Clopen}(S)=\operatorname{Baire}(S)\), and \(j\) is regular.
The correct statement is conditional:

\[
  j\text{ preserves the displayed join}
  \quad\Longleftrightarrow\quad
  \bigcup_n\widehat{b_n}\text{ is closed}
  \quad\Longleftrightarrow\quad
  \widehat b=\bigcup_n\widehat{b_n}.
\]

Thus \(j\) is non-sigma-regular exactly when at least one countable existing
join has a nonempty topological gap (the meet condition reduces to this by
complementation). For an orthogonal family, put

\[
  U_n:=\widehat{b_n},\qquad
  U:=\bigcup_n U_n,\qquad
  G:=\widehat b\setminus U
    =\overline U\setminus U.
\]

The \(U_n\) are pairwise disjoint Baire sets, \(G\) is a Baire set, and this
is exactly the Boolean specialization of \(g=(x\vee y')'\).

### Infinitude does not characterize non-sigma-regularity

The stronger claim that \(j\) is non-sigma-regular if and only if \(B\) is
infinite is also false. Let \(I\) be uncountable and let \(B\) be the
finite–cofinite algebra on \(I\). Its Stone space is the one-point
compactification \(I\cup\{\infty\}\), and \(B\) is infinite. Nevertheless
\(j\) is sigma-regular. For a countable family \((A_n)\subseteq B\), a
cofinite member makes \(\bigcup_nA_n\) a cofinite join; if all members are
finite, their union is either finite and is the join, or is countably infinite
and has no least cofinite upper bound, so no join exists in \(B\). Hence every
existing countable join is its set-theoretic union, and \(j\) preserves it;
the meet case follows by complementation.

The proposed compact-\(P\)-space argument proves a different statement. If
every countable union of clopens of a zero-dimensional space is clopen, the
space is a \(P\)-space; and every compact Hausdorff \(P\)-space is finite.
Indeed, a countably infinite subset would be closed, hence compact, while as a
countable \(P\)-space it would be discrete. The invalid inference was from
sigma-regularity to closure under *all* countable clopen unions:
sigma-regularity tests only families whose join already exists in \(B\).

Now let \(m\) be **any** finitely additive state on \(B\). Fremlin,
[*Measure Theory*, Chapter 41,
416Q](https://www1.essex.ac.uk/maths/people/fremlin/chap41.pdf), proves that
nonnegative additive functionals on a Boolean algebra correspond one-to-one
to Radon measures on its Stone space. Hence there is a unique Radon probability
measure \(\mu\) on \(S\) such that

\[
  m(b)=\mu(\widehat b)\qquad(b\in B).
\]

Restricting \(\mu\) to \(\operatorname{Baire}(S)\) gives a sigma-additive
state with \(m=\mu\circ j\). Countable additivity upstairs and finite
additivity across \(U\sqcup G\) give the exact formula

\[
  \boxed{
  m(b)=\sum_{n=1}^{\infty}m(b_n)+\mu(G).}
\]

Therefore \(m\) fails sigma-additivity at the orthogonal family \((b_n)\) if
and only if \(\mu(G)>0\).

This quantifier statement is exact. Every finitely additive state has such a
lift, but for a fixed gap only the states whose representing measures charge
that gap fail there. Conversely, if \(G\ne\varnothing\), choose \(p\in G\).
The Dirac measure \(\delta_p\) pulls back to the two-valued ultrafilter state
with value \(1\) at \(b\) and value \(0\) at every \(b_n\), so every nonempty
orthogonal gap is detected by at least one state.

A concrete witness is the finite-cofinite algebra on \(\mathbb N\). Its Stone
space is the one-point compactification
\(\mathbb N\cup\{\infty\}\). The singleton atoms have join \(1\) in the
abstract algebra, their clopens have union \(\mathbb N\), and the gap is
\(\{\infty\}\). The state that is zero on finite sets and one on cofinite
sets pulls back from \(\delta_\infty\) and charges precisely that gap.

**Answer to the scope question: the Boolean lifting and defect statement is a
theorem about every finitely additive state on every Boolean algebra, not only
some states.** This says that all states lift, not that all states charge every
gap. What is also not universal is the existence of a nonempty gap: finite
algebras, and any particular countable join that the inclusion preserves,
have none.

## Phase 3 — verdict

**Lemma R holds for OMPs under the stated assumptions:** in (a), a
sigma-additive state pulls back to a sigma-additive state when the embedding
preserves the relevant countable orthogonal joins (the stated sigma-regularity
is sufficient but stronger), and in (b) an arbitrary OMP embedding satisfies
the exact defect identity whenever the image join exists (the stated
sigma-orthocompleteness of \(Q\) guarantees this uniformly). The proof uses no
ambient lattice meets. The result is **folklore, not new**: the exact gap
notation was not located verbatim, but it is an immediate orthomodular
difference/additivity calculation. In the Boolean case the converse
representation covers **all** finitely additive states, while the claim that
the clopen inclusion is always non-sigma-regular is false.

For “the \(S\supset S_\sigma\) gap is generated by non-sigma-regularity” to be
a theorem, one would need a dilation theorem showing that every finitely
additive OMP state is the pullback of a sigma-additive state along an embedding
into a sigma-orthocomplete OMP, with every failure of sigma-additivity detected
by a positive gap of that embedding.
