# Prediction ledger: Conjecture C

*Registered by the investigation prompt before the Phase 2 computation;
adjudicated 2026-08-02.*

## Entry C-SR-1

**Claim under test.** If every site in a Boolean-block pasting is regular in
each incident block, then pasting the block MacNeille completions over the same
diagram yields a completion and preserves OMP/OML status.

**Pre-registered prediction.** In the Amemiya-Araki OML $L$ of finite and
orthogonally cofinite subspaces of an incomplete inner-product space, at least
one intersection of maximal Boolean blocks is non-regular.

**Proposed falsifier named in advance.** If every site of $L$ is regular,
Conjecture C is false immediately, because the MacNeille completion of $L$ is
not an OML.

**Falsifier validity audit.** **CONDITIONALLY VALID; SCOPE GAP.** Harding-Wang
Remark 3.4 says that $L$ nevertheless embeds into a complete OML. Definition
3.7 and Theorem 3.8 show why the bad MacNeille completion rules out a
*regular* completion: every regular completion factors through the MacNeille
completion. The proposed falsifier is therefore decisive for a strengthened
claim whose completed paste is a regular completion, or is the global
MacNeille completion of $L$. Literal Conjecture C says only "yields a
completion." No implication from regular site legs to a globally regular
embedding was established. The falsifier cannot adjudicate the literal claim
without that missing implication, and the claim is not reformulated here.

**Discriminating observation.** For

\[
 V=c_{00}(\mathbb N;\mathbb C)\oplus c_{00}(\mathbb Z;\mathbb C),
\]

the two basis blocks constructed in
`docs/site_regularity_orthomodular_completions.md` have site

\[
 S=\{G_D:D\subseteq\mathbb N\text{ finite}\}
   \cup\{G_D^\perp:D\subseteq\mathbb N\text{ finite}\}.
\]

The family of shared atoms

\[
 \{\operatorname{span}(g_n):n\in\mathbb N\}
\]

has join $V$ in $S$, but has no join in either containing block. Hence both
site legs are non-regular.

**Prompt-dichotomy correction.** The registered prompt offered only unequal
ambient joins or regularity of all sites. The observation is a third case:
the site join exists and the ambient joins do not. For these two blocks,
different computed joins are impossible; whenever an ambient join exists, it
is the same join in both blocks and in the site.

**Outcome.** **OBSERVATION MATCHED; LITERAL CLAIM NOT ADJUDICATED.** The
explicit site is non-regular. This rejects the vacuity threat and exhibits the
proposed mechanism, but it is not a verdict-grade prediction hit because the
prediction was not shown to follow from literal Conjecture C. The proposed
falsifier did not fire.

**Conjecture status.** **OPEN - NOT ADJUDICATED.** This entry confirms that the
proposed obstruction occurs in the decisive known MacNeille example. It does
not prove that the obstruction is necessary, that regularity is sufficient,
that the completed pasting is an OMP/OML, or that all completion obstructions
are site-local.

**Evidence grade.** Explicit hand proof, primary-source-backed ambient example;
no Lean formalization.
