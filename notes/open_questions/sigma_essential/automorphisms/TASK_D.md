# Task D: relevance to the paper

**Verdict: NOTHING. This line does not go in the paper.** This is the useful
negative outcome the task asked for, and I want to be precise about why, since
"nothing" could be laziness rather than a finding.

The reason is Theorem A's genericity, which cuts against its own interest.
Theorem A holds for ANY concrete orthoposet containing all singletons. It uses
no Ulam matrix, no cores, no invariant, no rigidity. So it says nothing about
the product Ulam carrier specifically; it is a remark about concrete orthoposets
with singletons, and a routine one (atomistic + order-determined perp => the
automorphisms are the obvious ones). A paper proving a ZFC witness theorem has
no use for it.

Taking the four candidates in turn:

**(a) Automorphism-invariance route to Cor 5.12 (centre).** NO. Two reasons.
First, the S_4 fibre action does not reduce the case analysis: Cor 5.12's proof
uses compatibility of E with each of A_1, A_2, A_3 to force [E_1]=[E_2]=[E_3],
and S_4 acts transitively enough to permute those three compatibility
statements -- so in principle one could say "by symmetry, WLOG" and do one case
instead of three. But the three cases in the existing proof are already one line
each ("Compatibility with A_2 gives [E_1]=[E_3], with A_3 gives [E_2]=[E_3]"),
so the saving is negative once the S_4 action has to be set up and justified.
Second and worse: the symmetry argument needs Theorem A plus B0(a) plus the
observation that the argument is S_4-equivariant -- three imported facts to save
half a sentence. Proof economy fails decisively.

**(b) Robustness statement for non-latticehood (Cor 5.11).** NO. Non-latticehood
is proved via Cor 5.9 (M x {1} not in L), which is a parity fact about E_4 --
odd weight -- and is already manifestly invariant under everything in sight. An
automorphism-theoretic restatement would be strictly weaker (it would say the
failure is not an artefact of labelling, which the parity argument already says
outright and constructively).

**(c) Psi_lat, Question 6.4.** NO. Psi_lat asks whether some ADMISSIBLE LATTICE
carrier fails Phi. Theorem A is about a non-lattice carrier's automorphisms and
transfers nothing: the conjecture in Question 6.4 is that latticehood FORCES Phi,
i.e. it is about the interaction of meet-closure with sigma-additive states, and
Aut is not a lever on that. Nothing in Tasks A-C constrains which lattices are
admissible, and the S_4 action in particular is a property of the fibre
combinatorics that any lattice completion would inherit trivially.

**(d) The "(LR*) three-cell star calculation".** MALFORMED -- this belongs to a
DIFFERENT THREAD. Searched the repo: "three-cell star" occurs in
`notes/programme/frontier_map.md` (l.94) as a Campaign-11 artefact of the
**OML/lattice attack** (`oml_attack/`), not in `papers/sigma_essential/` at all,
and "(LR*)" occurs nowhere in the repo. The task has crossed the sigma-essential
paper with the oml_attack campaign. Whatever the three-cell star controls, it is
not a feature of this paper, so Task A-C cannot bear on it. Flagging rather than
guessing.

**The one thing worth keeping** (and it is small, and it is not a paper item):
the C1/C3 contrast is a decent piece of EXPOSITORY framing for the programme's
recurring question of when order determines orthocomplementation. Concretely:
  - MO_2 / dim-2 projections: order does NOT determine perp (24 vs 8; Uhlhorn
    fails in dim 2) -- the degenerate regime.
  - dim >= 3 projections: Uhlhorn, perp determined, rigid symmetry group.
  - concrete orthoposets with all singletons (incl. the witness): perp
    determined trivially, by atomisticity.
The witness sits in the third, trivial regime. If anything, this CONFIRMS that
the carrier's interest is measure-theoretic (the Ulam/ultrafilter layer), not
symmetry-theoretic, which is worth one sentence in a notes file and zero
sentences in the paper.
