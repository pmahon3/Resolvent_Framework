# The corrected proof — σ-additivity is not first-order axiomatizable

*Written 2026-06-24, for understanding (not for submission). The standalone note
this belongs to is RETIRED. This file records the **correct** argument, since the
originally-submitted proof was broken. Verified sound by audit + advisor; the one
genuinely checkable piece is Lean-verified.*

---

## The kill — primary-source verified (2026-06-24)

Both the result (in its strongest form) and the proof method are explicitly in
print, so the note clears no contribution bar (Type 1/2 fail; Type 6 fails — the
bridge is not unmade). Three verified quotes:

**1. The STRONGER result ("not axiomatizable by any set of sentences" = not
elementary) — explicitly stated.**
> "…the class of probability algebras **is not elementary in classical first order
> logic**, a fact which restricts considerably what can be done or proved…"
> — Itaï Ben Yaacov, *On Theories of Random Variables*, Israel J. Math. (rev. 2011),
> introduction, p. 1. `http://math.univ-lyon1.fr/~begnac/articles/RandVar.pdf`

"Not elementary in classical first-order logic" = not the model class of any *set*
of first-order sentences. This is precisely the note's strongest claim. Stated as
known background motivating continuous logic; the field exists *because* of it.

**2. The WEAKER single-formula version — in the note's OWN cited reference.**
> "…our axiom system does not imply countable additivity, since **countable
> additivity cannot be expressed by a formula in our language**." (with witness
> p(T)=0 for finite T, p(T)=1 for co-finite T)
> — Fagin, Halpern & Megiddo, *A Logic for Reasoning about Probabilities*,
> Information and Computation **87** (1990), §2.2.
> `http://theory.stanford.edu/~megiddo/pdf/fag-hal.pdf`

**3. The proof ENGINE (saturation ⟹ σ-additive) — folklore, explicit.**
> An internal finitely-additive measure on the internal algebra A (every countable
> cover of an A-set has a finite subcover) is **automatically countably additive**;
> Carathéodory extends it to a σ-additive (Loeb) measure.
> — Peter A. Loeb, *Conversion from Nonstandard to Standard Measure Spaces…*,
> Trans. AMS **211** (1975), 113–122.

**Note on the search history (so the strength of the kill is honest):** FHM owns
only the single-formula version. The note's actual claim is the stronger
sentence-set version, which a 2026-06-24 hostile search initially could NOT find
stated explicitly — at which point "folklore" rested only on "experts could
assemble it from FHM-witness + Loeb/Łoś saturation + Keisler–Shelah." A *hard
targeted* second search then found the explicit statement (Ben Yaacov 2011),
closing the question on primary sources rather than on assembly. The kill is now
overdetermined for **every** strength of the claim.

---

## Setup

Work in the first-order language $\mathcal{L}_{\mathrm{BA},\mu}$ of Boolean
algebras carrying a normalized finitely-additive charge (the charge encoded by the
rational-cut predicates $M_{\le q}, M_{\ge q}$, as in the note). The property at
issue is **countable additivity**, which we state as a single property of
$\mathcal{L}_{\mathrm{BA},\mu}$-structures:

> $P(B,\mu) :\Longleftrightarrow$ for every sequence $(b_k)$ in $B$ with
> $b_k \downarrow 0$, one has $\mu(b_k) \to 0$.

This continuity-at-$0$ form is the **only** form to use. Do **not** phrase $P$ as
"$B$ is $\sigma$-complete and $\mu$ is countably additive": the ultrapower $N$
below has a Boolean algebra that is *not* $\sigma$-complete, so that phrasing makes
$P(N)$ ill-posed — and that exact equivocation is what sank the original proof.
One property, two structures, opposite truth-values.

**Claim.** $P$ is not first-order axiomatizable over $\mathcal{L}_{\mathrm{BA},\mu}$:
there is no set $T$ of $\mathcal{L}_{\mathrm{BA},\mu}$-sentences whose models are
exactly the structures satisfying $P$.

## The proof

Let $\ell$ be the $\{0,1\}$-valued **ultrafilter charge** on $P(\mathbb N)$ for a
fixed nonprincipal ultrafilter $\mathcal U_0$: $\ell(A) = 1$ iff
$A \in \mathcal U_0$. Set $M = (P(\mathbb N), \ell)$, an
$\mathcal{L}_{\mathrm{BA},\mu}$-structure.

**Step 1 — $P(M)$ is FALSE (the verified core).**
$P(\mathbb N)$ is a genuine $\sigma$-algebra, so the meet is literal: with
$A_k = \{k, k+1, \dots\}$ one has $A_k \downarrow \varnothing$, yet
$\ell(A_k) = 1$ for every $k$ (each $A_k$ is cofinite, hence in $\mathcal U_0$).
So $\ell(A_k) \not\to 0$ and $P(M)$ fails.
*This is the one genuinely non-obvious, fully checkable step, and it is
Lean-verified:* `ultrafilterCharge_not_sigma_additive` in
`formalization/QuerySystem/QuerySystem/UltrafilterCharge.lean` (0 sorry), together
with `ultrafilterCharge_union_of_disjoint` (finite additivity, so $M$ is a model)
and `ultrafilterCharge_eq_one_iff_dirac`.

**Step 2 — Form the ultrapower.**
Let $\mathcal U$ be a nonprincipal (hence countably incomplete) ultrafilter on
$\mathbb N$ and put $N = M^{\mathbb N}/\mathcal U$. By Łoś's theorem the diagonal
embedding is elementary, $M \preceq N$, so in particular $M \equiv N$.
[classical: Łoś 1955]

**Step 3 — $P(N)$ is TRUE (saturation / the Loeb phenomenon).**
Since $\mathcal U$ is countably incomplete, $N$ is $\aleph_1$-saturated.
Suppose $(b_k)$ in $N$ with $b_k \downarrow 0$ and, for contradiction,
$\mu^*(b_k) \ge \varepsilon > 0$ for all $k$ (where $\mu^*$ is $N$'s charge). Pick
a rational $q \in (0,\varepsilon)$. The 1-type
$p(x) = \{\, x \wedge b_k = x : k \in \mathbb N \,\} \cup \{ M_{\ge q}(x) \}$
over the countable parameter set $\{b_k\}$ is finitely satisfiable: any finite
subset mentions $b_0, \dots, b_m$, and $x = b_m$ realizes it (the $b_k$ decrease,
and $\mu^*(b_m) \ge \varepsilon > q$). By $\aleph_1$-saturation $p$ is realized by
some $x \ne 0$ with $x \le b_k$ for all $k$ and $\mu^*(x) \ge q > 0$; so
$\inf_k b_k \ne 0$, contradicting $b_k \downarrow 0$. Hence $\mu^*(b_k) \to 0$:
$P(N)$ holds. (This is exactly Loeb's 1975 observation that saturation upgrades a
finitely-additive internal charge to a countably-additive one.)
[classical: Loeb 1975; standard $\aleph_1$-saturation of ultrapowers over a
countably-incomplete ultrafilter]

**Step 4 — Conclude.**
$M \equiv N$, $P(M)$ false, $P(N)$ true. So $P$ is not preserved under elementary
equivalence; the class of structures satisfying $P$ is not elementary; hence $P$ is
not axiomatizable by any set of first-order sentences. $\qquad\blacksquare$

## What is verified where

| Step | Status |
|------|--------|
| 1 ($M$ non-σ-additive on the real $P(\mathbb N)$) | **Lean-verified, 0 sorry** — the one non-obvious checkable piece |
| 2 ($M \preceq N$, Łoś) | classical, cite Łoś 1955 |
| 3 (saturation ⟹ $P(N)$) | classical, cite Loeb 1975 + standard saturation |
| 4 (≡ ⟹ not FO-axiomatizable) | immediate |

Per the repo rule "don't formalize known results; `axiom` with citation," steps 2–4
are not formalized: they are textbook model theory / the Loeb construction. Only the
genuinely checkable measure-theoretic core (step 1) is in Lean.

## Why the original proof was wrong (recorded so it is not repeated)

The submitted/withdrawn proof tried to make the **ultraproduct of Diracs** the
non-σ-additive object: $\ell(A) = \lim_{\mathcal U}\delta_n(A)$ on the diagonal copy
of $P(\mathbb N)$ inside $\prod_{\mathcal U}(P(\mathbb N),\delta_n)$, with witness
$A_k \downarrow \varnothing$. That fails: setting $d(n) = A_n$, the element $[d]$
satisfies $[d] \le [\mathrm{const}_{A_k}]$ for all $k$ (since $\{n : A_n \subseteq
A_k\}$ is cofinite) and $\mu^*([d]) = 1$ — so the diagonal images are trapped above
a measure-$1$ element and do **not** decrease to $0$ in the ultraproduct's Boolean
algebra. The witness establishes nothing about the ultraproduct charge; worse, by
Step 3 that charge **is** σ-additive, so no ultraproduct over a nonprincipal
ultrafilter on $\mathbb N$ can witness the result.

**The fix is a reversal of roles:** the saturation phenomenon that *kills* the old
proof (it forces the ultra-object to be σ-additive) is exactly what *powers* the
correct one — put the non-σ-additivity in the **base** $M$ (a real $\sigma$-algebra,
where it is honest and Lean-checked) and let saturation make the **ultrapower** $N$
σ-additive. The contradiction is then just $M \equiv N$.
