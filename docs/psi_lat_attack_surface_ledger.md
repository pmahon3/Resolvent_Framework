# Claim-status ledger: `Psi_lat` attack surface

*Opened 2026-08-06; entries current through 2026-08-09. Full proofs, source
links, and definition anchors are in
[`psi_lat_attack_surface.md`](psi_lat_attack_surface.md). Falsifiers are stated
at the scope of the corresponding claim. No finite exhaustive search and no
Lean work were performed.*

## Entry PLA-EXCL-1 — exclusion lemma

**Claim under test.** Inside a concrete sigma-orthocomplete OML:

1. latticehood excludes the missing-limit mechanism and thereby excludes the
   product-Ulam kill mechanism;
2. concreteness excludes sharp/stateless holonomy; and
3. non-segregation forces the nontrivial-overlap block nerve to be connected.

**Falsifiers named before the audit.**

- A sigma-orthocomplete OML with a missing countable monotone supremum or
  infimum.
- A concrete logic with no sigma-additive two-valued state.
- A non-segregated concrete carrier with disconnected nontrivial-overlap block
  nerve.
- For the claimed product-Ulam derivation specifically: a proof that the
  banked s11 obstruction uses unresolved points below an incompatible binary
  overlap rather than a missing countable monotone limit.

**Outcome.**

- **COUNTABLE-LIMIT CLAUSE — VERIFIED.** Holland's theorem, and the elementary
  orthogonal-difference proof reproduced in the attack memo, give all
  countable joins and meets.
- **PRODUCT-ULAM DERIVATION — REFUTED AS STATED; CORRECT MECHANISM VERIFIED.**
  The actual witness's missing object is the binary meet of `A_1,A_2`; its
  countable lower bounds have no countable cofinal family. The s11 reason is T1
  singleton quarantine: fine singleton structure below a set intersection
  forces the lattice meet to equal that intersection and makes the pair
  compatible.
- **ABSOLUTE STATELESSNESS CLAUSE — VERIFIED.** Every carrier point supplies a
  global sigma-additive Dirac. The conclusion does not extend to failure of a
  specified finite trace to match any Dirac or sigma-state.
- **CONNECTED-NERVE CLAUSE — REFUTED.** Segregation is an operational
  blockwise rescue condition, not a nerve condition. A horizontal-sum
  attachment preserves an existing bad family in one component while adding
  an isolated nerve component.

**Status.** **PARTIALLY VERIFIED, WITH TWO REQUIRED CORRECTIONS. THE
EXCLUSION ACCOUNTING DOES NOT CLOSE `Psi_lat`.**

**Evidence grade.** **PRIMARY LITERATURE + REPO-VERIFIED THEOREMS + ELEMENTARY
HAND PROOFS.** The direct source is Holland 1970; the repo mechanisms are
`cor:incompat`, T1 in `oml_lattice_regularity_attack.md` section 9c,
`rem:quotient`, and `rem:segregated`.

**Surviving mechanism.** A coherent global finitely additive two-valued state
whose finite value-one cluster uses at least three incompatible blocks, but
whose blockwise sigma-replacements admit no common-boundary-compatible
selection. This is exactly GSD/distributed boundary descent. It is proved as a
normal form; identifying it with a carrier-cell polytope gap is not proved.

**Disposition.** Use “probabilistic holonomy” only as a synonym for the exact
common-`mu` GSD obstruction. Do not cite countable completeness as the s11
product-Ulam kill, and do not infer nerve connectedness from non-segregation.

## Entry PLA-CHORD-1 — meet-as-chord conditional

**Claim under test.** For a finite trace `F`, augmenting by lattice meets gives
a constraint hypergraph to which Vorob'ev--Kellerer applies; if that hypergraph
is decomposable, then every `L`-visible trace is cell-realizable.

**Falsifier named before any configuration hunt.** An infinite concrete
sigma-complete OML containing a finite `F` such that its full
complement-and-meet augmentation remains non-acyclic and an actual global
finitely additive zero--one state has an `F`-trace outside the realized cell
polytope. To falsify the corresponding `Psi_lat` hope rather than only the
Dirac claim, additionally require `L in Adm` and that no global sigma-additive
two-valued state matches the trace.

**Gate checks that fired before the hunt.**

1. **HYPERGRAPH TYPE ERROR.** Vorob'ev vertices are variables/measurements and
   hyperedges are joint marginal contexts. The proposed vertices are carrier
   cells/points and the hyperedges are events whose probabilities are vertex
   sums.
2. **TARGET TYPE ERROR.** Cell weightings are mixtures of Diracs. `Phi` permits
   non-Dirac sigma-additive two-valued states. The finite horizontal
   `Omega_7` lattice has a global sigma-state with trace `111` and no realizing
   point.
3. **MISSING SUPPORT BRIDGE.** Indicator-variable gluing produces a measure on
   the full assignment cube. It is supported on actual carrier cells only if
   the realized support is the natural join of its context projections.
4. **MISSING VALUE-TRANSMISSION BRIDGE.** A two-valued sigma-state on a
   concrete OML need not charge `a meet b` when it charges `a` and `b`; `MO_2`
   is the explicit counterexample.

**Product-Ulam calibration.** **PASSED AT DIRAC SCOPE.** The four realized
triple cells are `110,101,011,000`; the actual global finitely additive vote
state has trace `111`. `lem:table`(IV) and `cor:incompat` identify the absent
linking meets. This validates the cell diagnostic for this rigid witness, not
the general theorem.

**Outcome.** **BROKEN — THE STATED CONDITIONAL IS NOT WELL-TYPED.** A corrected
classical conditional is proved in the attack memo: alpha-acyclic joint scopes
plus compatible local marginals, local support, and a lossless-support identity
imply a cell-supported global distribution. Lattice visibility has not been
shown to provide any of those bridge premises.

**Literature status.** **CLASSICAL ENGINE ALREADY KNOWN; OML BRIDGE NOT
LOCATED.** Vorob'ev proves the universal regular-complex `iff`; modern
contextuality explicitly uses the acyclic marginal theorem and credits
Kellerer independently. The bounded orthomodular/concrete-logic search found
no meet-as-chord application to `Phi`.

**Evidence grade.** **PRIMARY-SOURCE LITERATURE VERDICT + EXPLICIT HAND
COUNTEREXAMPLES + CONDITIONAL HAND THEOREM.** No search for the registered
infinite falsifier was needed after the typing gates fired.

**Disposition.** Do not spend pen-and-paper time proving the classical gluing
step. Any renewed chord argument must first define a marginal-scenario
hypergraph, prove lossless carrier support, and prove state-value transmission.

## Entry PLA-FLAT-1 — flat-habitat and sigma-triangulation verdict

**Claim under test.** Sigma-completing an infinite loop/ladder pasting with
flat cross-block meets necessarily adjoins nontrivial chord elements; failing
that, essential irreducibility or non-segregation excludes the retained flat
habitat.

**Falsifiers named before the audit.**

- For generic sigma-triangulation: a sigma-complete or complete OML obtained by
  completing the blocks of a cyclic pasting while retaining the same sites and
  creating no new cross-block bounds.
- For exclusion by essential irreducibility: an infinite concrete
  sigma-complete OML with trivial (hence essentially trivial) centre and flat
  off-block meets.
- For the full habitat verdict: an infinite concrete sigma-complete,
  essentially irreducible, non-segregated carrier with an infinite coarse
  boundary, state-null mixed meets, and a common-`mu` descent obstruction.

**Observations.**

- **GENERIC SIGMA-TRIANGULATION — REFUTED.** The banked five-cycle of
  finite--cofinite blocks remains an OML after each block is completed to its
  powerset. The resulting OML is complete, the sites and cycle remain, and no
  new block-private element changes an old cross-block meet or join.
- **CONCRETE/`Adm` SCOPE — NOT DECIDED BY THAT EXAMPLE.** The completion note
  proves an abstract complete-OML result; it does not certify all concrete
  state and `Adm` gates.
- **ESSENTIAL-IRREDUCIBILITY EXCLUSION — REFUTED.** Concrete `MO_omega` is an
  infinite sigma-complete flat horizontal lattice with trivial centre. It is
  tame because it is segregated/Polish, not because flatness conflicts with
  irreducibility.
- **NON-SEGREGATION EXCLUSION — NOT PROVED AND NOT DEFINITIONAL.** The
  definition imposes blockwise rescue, not mixed-meet geometry.
- **FINITE-SITE HABITAT — EXCLUDED.** `finite_interface_quarantine` forces
  `Phi`; a live carrier needs infinite interfaces.
- **COUNTABLE-IDEAL-VANISHING COARSE FIBRES — EXCLUDED.** The coarse-fibre
  fence shows that purely countable/co-countable distinctions become central
  after quotienting. Countable-type defect also reduces to the closed relay
  mechanism.

**Status.** **GENERIC TRIANGULATION REFUTED; FULL ADMISSIBLE FLAT HABITAT
OPEN, WITH ITS BOUNDARY SCALE AND COARSE RESOURCE LOCATED.**

**Evidence grade.** **REPO-VERIFIED COMPLETION CONSTRUCTION, FORMAL
FINITE-INTERFACE THEOREM, AND HAND DEFINITION AUDIT.** No new construction is
claimed.

**Specific hand target.** Use the banked three-cell conditional-diagonal star
with three distinct nonseparating quotient supports, choose interfaces outside
the countable-type-over-atoms class and surviving the countable quotient, and
attempt the coherence-preserving flat-realisation lemma: the diagram has a
faithful concrete sigma-complete OML realisation in which the designated
three-face trace remains globally finitely coherent and every closure-created
mixed meet is strict and null for that extension.

**Falsifier for that next lemma.** A mixed-cut identity forced in every
faithful realisation whose finite-additivity equations contradict the three
prescribed value-one faces. Its first appearance would identify the exact
triangulation step; a coherence-preserving realisation would locate the flat
carrier architecture for the later `Adm` audit.

**Disposition.** Keep the completion-thread verdicts unchanged. Reuse
“regular/sigma-homomorphic boundary” only for the puncture obstruction, and do
not promote it to generic chord creation.

## Entry PLA-S11-1 — locality of singleton quarantine

**Claim under test.** The banked s11/T1 proof is either a product-Ulam
artifact or a general mechanism by which latticehood forces a live mixed
constraint.

**Falsifier named before proof inspection.** Any use in T1 of an Ulam row or
column, countability, atomicity, sigma-additivity, a block-selection theorem,
or the three-core loop.

**Outcome.** **GENERAL AS A PAIRWISE MEET SQUEEZE; LOCAL AS A STATE-KILL
MECHANISM.** The actual proof uses only the greatest carrier lower bound of
one pair and the hypothesis that carrier lower bounds cover its literal set
intersection. Singletons are one sufficient cover. It does not prove the meet
nonzero or non-null and contains no block or three-cell step. The
product-Ulam-specific input is that this locally resolved fine structure sits
under the charged incompatible core overlap.

**Evidence grade.** **REPO-VERIFIED PROOF INSPECTION.** Anchors: T1 in
`oml_lattice_regularity_attack.md` section 9c and the machine-checked
`compat_of_locally_resolved` / `compat_of_singletons` statements in
`ConcreteOMLBlocks.lean`. Full audit:
[`s11_quarantine_generality.md`](s11_quarantine_generality.md).

## Entry PLA-S11-2 — locally resolved value-one meet lemma

**Candidate.** Let `L` be a concrete sigma-class, `mu` a finitely additive
two-valued state, and `a,b` value-one events whose carrier meet exists. If
every point of `a cap b` lies in a carrier event contained in `a cap b`, then
`a meet b=a cap b` and `mu(a meet b)=1`.

**Falsifier named before the derivation.** A tuple satisfying all displayed
hypotheses with `mu(a meet b)=0`.

**Outcome.** **HAND-PROVED FROM BANKED T1.** T1 makes the pair compatible;
finite additivity on the Boolean algebra of the pair makes the value-one
filter intersection-closed. No sigma-completeness, block, countable-type,
atomicity, or Ulam hypothesis is used.

**Evidence grade.** **REPO-VERIFIED T1 + ELEMENTARY HAND COROLLARY.**

**Deletion boundary / explicit negative result.** **LOCAL RESOLUTION IS
ESSENTIAL.** In the banked concrete `MO_omega`, a Dirac state charges private
events from two distinct blocks while every such mixed meet is `0`; their
nonempty literal intersections contain no nonempty carrier lower bound.
Thus concreteness, sigma-completeness, non-Booleanness, essential
irreducibility, and latticehood do not by themselves force a live mixed meet.

**Relation to `Adm`.** Concreteness and the added lattice hypothesis supply
the setting, but no `Adm` clause supplies local resolution. The global
all-singletons form would make the lattice Boolean and therefore conflicts
with `Adm` at that global scope. Essential irreducibility does not repair the
gap (`MO_omega`); non-segregation is a trace-rescue condition, not a mixed-meet
condition.

## Entry PLA-S11-3 — three-cell star test

**Claim under test.** The locally resolved value-one meet lemma either
shortcuts the banked three-cell conditional-diagonal star or proves that its
interfaces evade s11.

**Decisive falsifiers named before the test.** A proof that every faithful
star realization locally resolves one designated value-one mixed
intersection would falsify flat realization (shortcut). A proof that the
fenced interface conditions force an unresolved point in every designated
mixed intersection would establish evasion.

**Outcome.** **UNDETERMINED — ONE EXACT HYPOTHESIS LOCATED.** The star's
distinct proper nonseparating quotient supports, non-countable-type
interfaces, and nontrivial countable quotient imply neither the local
lower-bound cover nor its negation. “Nonseparating” cannot be replaced by
“locally unresolved.” If the cover is forced, the candidate lemma gives a
value-one mixed meet; if strict/state-null meets are realized, T1 says the
cover fails. Deciding which occurs is exactly the pending mixed-cut hand
calculation.

**Evidence grade.** **REPO-ANCHORED TARGET-SPECIFICATION AUDIT; NO
CONSTRUCTION OR SEARCH.**

**Disposition.** The pen-and-paper target is unchanged. Test the local-cover
condition at the first designated mixed cut; do not infer evasion merely from
the coarse/nonseparating interface labels.
