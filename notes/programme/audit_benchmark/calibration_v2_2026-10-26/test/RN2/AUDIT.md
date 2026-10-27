## Audit: seed.md, "short alternative proof of Glivenko's theorem in natural deduction via at-most-one RAA" (mode: full)

Audit date per AS_OF.md: **2015-10-19**. Only sources dated on or before that day count as prior art. The seed's own text (in any version, under any title) is the submission and is not cited as prior art.

Read levels: **P** = primary text read; **A** = abstract or publisher preview read; **S** = known only through a secondary description; **M** = from memory, not re-checked this session.

### Declared contribution type(s): Type 2 (new proof of a known result), Type 6 (exposition). The seed names types but not the per-type bars it commits to clearing, so it does not meet the full Phase-1 requirement.

### Pure Verdict: KNOWN

The seed claims no new theorem, so this checks whether the result, the key lemma and the proof route are already known.

1. **Statement.** Glivenko's theorem: ⊢_C A iff ⊢_I ¬¬A, for propositional A. Glivenko (1929), *Bull. Acad. Royale de Belgique* 15. [M, 1929.] It is a textbook theorem, for example Kleene, *Introduction to Metamathematics* (1952), and Troelstra–van Dalen, *Constructivism in Mathematics* Vol. I (1988), Ch. 2. [M; I did not check theorem numbers.] KNOWN.
2. **Key lemma.** "Every derivation can be transformed so that reductio ad absurdum is applied at most once" appears to be Seldin's normalization strategy: J. P. Seldin, "Normalization and excluded middle. I", *Studia Logica* 48(2), 193–217, 1989.
   - Seldin's abstract, from the Springer search snippet [A, 1989]: the usual classical rule is stronger than necessary; a weaker rule, equivalent to excluded middle, is introduced; and logics using these rules are normalized. The abstract does not state the "at most one RAA, last rule" wording.
   - That exact wording (fragment {∧,∨,→,⊥,∃}, at most one application of the classical absurdity rule, which is the last rule) comes to me only from secondary sources dated **after** 2015-10-19.
   - Pereira et al. 2010 (pre-date, below) describes "Seldin's normalization strategy" and draws a Glivenko corollary from it. I could not confirm from the 2010 preview that it gives the single-final-RAA wording.
   - The full texts were paywalled: Springer redirected and PhilArchive returned 403.
   - **Flag:** the attribution of the lemma's exact form to Seldin rests partly on post-cutoff secondary descriptions. Verdict: KNOWN (high confidence, not primary-verified).
3. **Lemma ⇒ Glivenko.** This step is immediate. If the single RAA is the last step, the derivation of A ends with RAA from ¬A ⊢_I ⊥. That gives ⊢_I ¬¬A by →I. The converse is trivial. A Glivenko corollary of Seldin's strategy is in print for the **implicational {→}-fragment with Peirce's rule only**: Pereira, Haeusler, Costa, Sanz, "A New Normalization Strategy for the Implicational Fragment of Classical Propositional Logic", *Studia Logica* 96(1), 95–108, 2010. In the words of that source, "as a corollary of Seldin's normalization strategy we obtain a form of Glivenko's theorem for the classical {→}-fragment". [A, 2010: abstract and reference list from the publisher preview.]
   - I found **no pre-2015 source** that states *full propositional* Glivenko as an explicit corollary of single-final-RAA. One targeted search turned up nothing. Stålmarck (JSL 56, 1991) [S] and Prawitz (1965) [M] give classical normalization but not this corollary, as far as I saw.
   - The step is a one-line consequence of the lemma, so an expert would call it folklore. Its being in print in full generality is UNCONFIRMED.
4. **Related.** Prawitz, *Natural Deduction* (1965), Ch. III: the classical normal form theorem with ⊥_c restricted to atomic conclusions, the standard normalization the seed would rely on. [M, 1965.]

**Expert reaction.** "This is Seldin's postponement of RAA, and Glivenko is the well-known one-line corollary." The lemma is Seldin's (1989). The Glivenko corollary was in print for the {→}-fragment (2010) and is a one-line step in general. The seed as submitted (the abstract only is available) does not credit either source.

**Correctness.** The argument is sound as sketched: the lemma is true (Seldin) and the corollary step is valid. I found **no correctness problem**. The problem is attribution: the seed presents the key lemma as its own.

Date flags:
- Guerrieri–Naibo, arXiv:1710.08854 (2017), and an ecumenical-Glivenko arXiv paper (2025/26) postdate the audit date. **Neither is cited as prior art.** They served only as locators, and they supplied the exact wording of Seldin's lemma (see item 2).
- arXiv:1510.05873, Sánchez Terraf, "Yet Another Proof of Glivenko's Theorem" (October 2015), matches the seed and is taken to be the submission itself. It is **excluded** under AS_OF.
- Stålmarck 1991 and Pereira et al. 2010 predate the audit date.

### Applied Verdict: not evaluated (no applied or methodological claim; Type 7 not declared)

### Contribution Type Verdicts (mode=full only):

**Type 2 (new proof of known result): FAIL.**
Bar: (a) a technique usable elsewhere, (b) an unexpected cross-field connection, or (c) a substantial simplification.
- (a) The technique, postponing RAA to a single final use, is Seldin's (1989). Pereira et al. 2010 already extended it to Peirce's rule. It is not new.
- (b) There is no cross-field connection: everything stays inside the proof theory of natural deduction.
- (c) The route is already published for the {→}-fragment (2010), and it is a direct corollary of Seldin's lemma in general. The result is short only because it relies on a normalization theorem: the hard part moves into the cited lemma. That is no simplification over the standard proofs. The standard inductive proof (Kleene 1952; Troelstra–van Dalen 1988) and the negative-translation proof are each a page or less.
- Verdict: an already-published alternative route, presented without attribution.

**Type 6 (exposition / translation): FAIL.**
- (a) No target audience is named. "Brief self-contained treatment" is not an audience.
- (b) No inaccessible literature is cited. Glivenko's theorem is in standard textbooks (Kleene 1952; Troelstra–van Dalen 1988 Ch. 2; van Dalen, *Logic and Structure*) [M], and Seldin's lemma is in a mainstream journal.
- (c) No non-trivial translation work is shown.
- Verdict: the material is already accessible, which fails the programme bar.

### Cross-reference
Pure KNOWN covers both the theorem and the proof route. Type 2 fails because the route is Seldin's, with the Glivenko corollary already in print. Type 6 fails because the material is accessible and no audience is named. No type clears its bar.

### Recommendation
**Park.**
- Evaluated: Pure; Type 2; Type 6.
- Failed bars: Type 2 (a)/(b)/(c), because the route was published by Seldin (1989) and the corollary by Pereira et al. (2010). Type 6 (a)/(b), because there is no audience and the literature is accessible.
- If the author still wants a note: credit Seldin 1989 and Pereira et al. 2010, and recast the note as a classroom exposition for a named audience (for example, students of a first proof-theory course) at a pedagogical venue.

How the item bears on the programme's why (one line): it does not. It is a single-system logic re-proof with no local-to-global content.

### Referee estimate: BORDERLINE
Venue class: short-note or letters / expository (pedagogical)
Value carried by: factor 2 (a short proof by a different technique), weakly. Most of the work is Seldin's 1989 lemma.
Main risk a referee would raise: the key lemma is Seldin's (Studia Logica 1989), and the seed does not credit it. A {→}-fragment version of the corollary is in Pereira et al. 2010.
Uncertainty: if a pre-2015 source states full propositional Glivenko as this corollary, the note is an uncredited re-proof already in print, and the estimate becomes REJECT-LIKELY. I could not confirm such a source.
