# Proof-writing prompt — reconstruction paper (Phase 4 → 5)

You are writing the complete proofs for the reconstruction structure theory.
The Phase-2 hostile prior-art audit (`reconstruction_audit_full.md`, this directory,
verdict: Type 6 secure, Type 3 conditional-on-winding, Type 5 not-novel) has
fixed what is borrowed and what is ours. Honour that split exactly. The paper's
credibility rests on NOT writing original proofs for classical facts and NOT
letting conjectures harden into theorems.

## The cite-vs-prove contract (do not cross these lines)

CITE ONLY — reduce to the cited result in <=1 paragraph, write no original proof:
- Prop. (commensurability is C=R): local/marginal polytope gap, Wainwright-Jordan.
- Thm (acyclic => tame): Vorob'ev 1962 (regularity <=> alpha-acyclicity) + BFMY 1983
  + Barbosa-via-Abramsky identification. Already disclaimed in the draft — keep it.
- Thm (variety-typed => universal): De Loera-Onn 2004 + Prusa-Werner 2015 +
  Pitowsky 1991 (NP-complete floor) + Avis-Imai-Ito-Sasaki 2005 (covariance map).
  This is a KNOWN impossibility; the proof is a reduction chain, not new work.
- Parity MECHANISM (stable-set integrality, TU): Nemhauser-Trotter, Chvatal,
  Hoffman-Kruskal, Konig. Cite the mechanism; the golden-mean specialization is
  where your writing goes.
- Signability => TU: the Hoffman-GALE APPENDIX to Heller-Tompkins 1956, NOT the
  main text. This attribution is a known landmine — state it precisely.

PROVE ORIGINALLY — these are the contribution; full rigorous proofs owed:
1. The reduction lemmas of the parity theorem: (a) golden-mean homomorphisms
   <=> independent sets, giving C ~= FSTAB(C_L), R ~= STAB(C_L); (b) the
   marginal-determination affine lift (edge distribution affine in endpoint
   vertex-marginals on the variety). The det = 1-(-1)^L parity computation and
   the "unique fractional vertex u = 1/2 on odd rings" claim must be proved, not
   asserted — including that a zero coordinate lands on a forest (TU, integral)
   face.
2. The odd-ring PR-box corollary: contextual fraction = 1 and the
   1/(L-1) relative violation of the odd-cycle inequality. Prove the
   no-noncontextual-part argument (2 sum v_i >= L > L-1) rigorously.
3. Theorem (signable languages tame on bipartite frames): the theta-sweep is
   claimed CONSTRUCTIVE — write the explicit decomposition and prove it
   reproduces any coherent point exactly (this is a proved theorem per the draft,
   so it needs a real construction + verification, not a sketch).
4. Theorem (forest counting): |rho| <= 2|A|-1 => |E(H)| <= |V(H)|-1 => forest =>
   bipartite. Short but must be exact (the marginal-determination bound is the
   crux).
5. Theorem (Circuit Localization, LOOPLESS symmetric case ONLY): the assembly
   proof — forest target => phase-decoupling on bipartite frames (taming 10 ->
   signable, Thm taming7) + acyclicity elsewhere (Thm acyclic) cover the
   gate-passing frames. This is the proved headline. Prove taming (10)
   (bipartite-target phase decoupling) in full — it is load-bearing and only
   sketched.
6. Theorem (winding characterisation) + Lemma (layer-injectivity discriminant):
   THE contribution that carries Type 3. The Lean lemma
   (WindingInjectivity.lean) is done (0 sorry); write the covering-space /
   flow-decomposition proof that fractional vertices of C are exactly the
   normalised simple directed cycles of winding >= 2, under the genericity gate.
   This proof must be self-contained and MUST NOT depend on anything in section
   "open".

FENCE AS CONJECTURE — prove NOTHING here; keep the gap named:
- Conjecture (universal impossibility) and Conjecture (pruning lemma). The k=2
  residual carries a REAL phase gap: the reduction to lockstep exchange drops a
  relative-phase DOF between the two winding strands. Do not close it. Empirical
  no-counterexample-to-length-35 is EVIDENCE, not proof — label it so. The
  audit's Type-5 verdict FAILS as novelty precisely because this is unproved;
  any wording that implies it is proved re-opens the audit.

## Differentiation the proofs must make visible (from the audit)

- Parity: the even/odd split is the golden-mean face of the n-cycle
  noncontextuality polytope of Araujo-Quintino-Budroni-Terra Cunha-Cabello 2013
  (now cited, PRA 88, 022118). Your proof's novelty is the DYNAMICAL route
  (recurrence on the subshift, odd-period orbits), not the polyhedral fact.
  Write it so a referee sees you know this is a special case of a known
  characterization.
- Tamings: signability/TU is close in kind to Weller 2016 (LP tightness by
  forbidding signed minors; now cited). The proof of Thm taming7 should be
  framed so the delta from Weller is explicit — the observational-frame
  bipartition is the new ingredient, the integrality is not.

## Verification discipline (the paper's method note)

- Every "commensurable" verdict = a theorem or an exact rational enumeration.
- Every "contextual" verdict = an EXHIBITED rational witness in C\R.
- Sampling is screening only, never the basis of a commensurable claim.
- Novel results get Lean certification (Phase 5): layer-injectivity is done; the
  queued targets are theta-sweep, phase-mixture, monotone collapse (taming 9),
  empty-intersection. Prove on paper first, then formalize.
- After each proof: independent check (Lean for the formalizable ones, manual
  otherwise). Do not trust an LLM-produced proof without it.

## Order of work (suggested)

Forest counting (4) -> signable/theta-sweep (3) -> Circuit Localization assembly
(5) -> parity reduction lemmas + PR-box (1,2) -> winding characterisation (6).
Leave section "open" exactly as fenced. Re-run `/audit full` (Phase 7) before
declaring complete; the winding proof is the one whose novelty the second audit
will probe hardest.
