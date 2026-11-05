# Carriers with no Omega: owned map

reviewed: false. 2026-11-05.

Scope: families of local Boolean algebras glued along shared questions, no ambient Omega (pBAs, OMPs/OMLs, test spaces, context categories, spectral presheaf). Method: read `glued_carriers_taxonomy.json` (`owned_regions`, `conj.abstract_carriers`), `stone_role_prior_art.md`, repo grep for names; about 14 US web searches; full text of two papers (vdBH, HLHN). Read levels: [abs] abstract, [snip] search snippet, [skim], [meth] theorem statements/proof read, [full]. Most items below are [abs]/[snip]: this is a map, not a verdict. Hostile default: assume the nearest owner kills each seam until a primary read says otherwise.

## 1. Owned-region table

| Region | Owner(s) | Read | Recorded? |
|---|---|---|---|
| pBA embeds in a Boolean algebra iff two-valued homs separate (pBA Thm 0) | Kochen-Specker 1967 (p.66 Thm 0, via secondary) | [snip] | partly (KS named in task; not as owned_region) |
| OML/OMP has Boolean block-embedding iff full set of two-valued states | Zierler-Schlessinger, Duke 1965; Godowski (as relayed) | [snip] | names present in sigma_essential files, NOT in glued_carriers owned_regions |
| OMP = pasting of Boolean algebras; 3-cycle containment criterion | Greechie 1971; Dichtl; Rogalewicz CMUC 29 (1988); Navara-Rogalewicz Math. Nachr. 154 (1991) | [snip] | Greechie loop recorded (`own.greechie_loop`); Dichtl in stone_role; Rogalewicz in Czech-school notes |
| Colimit theorem: every pBA = colimit of its (f.g.) Boolean subalgebras; BA reflective in pBA, left adjoint L(A) = colimit in BA; K(A) = lim over contexts of Stone spectra; PBoolean complete + cocomplete; also partial complete BAs (Thm 7) | van den Berg-Heunen, Appl. Cat. Struct. 20 (2012), arXiv:1003.3618 Thm 4, Prop 8, Thm 9, Cor 10 | [meth] | yes in `own.stone_space_of_logic` (R3 row); the L(A) corollary is not spelled out there |
| KS property of a pBA <=> no morphism to 2 <=> colimit in BA trivial | vdBH 2012 Sec 5 (KS defined as L(A)=1); restated in Dawar-Shah arXiv:2602.24164 | [meth] vdBH, [abs] D-S | no |
| Recovering an orthoalgebra from its poset of Boolean subalgebras (directions, orthodomains, hypergraphs extending Greechie diagrams) | Harding-Heunen-Lindenhovius-Navara, Order 36 (2019), arXiv:1711.03748 | [abs]+intro | no (Lindenhovius is on the shelf, this paper is not) |
| Domains of commutative C*-subalgebras; C(A) determines A in type I AW* case | Heunen-Lindenhovius, MSCS 29 (2019), arXiv:1504.02730 | [snip] | partly (shelf) |
| Spectral presheaf, KS = no global section / no points; valuations = global sections | Isham-Butterfield; Doring-Isham; Doring-Frembs arXiv:1910.09591; de Silva-Barbosa arXiv:1806.02840 | [snip] | no (Doring only via Cannon-Doring) |
| Global section of empirical model iff hidden variable; sheaf contextuality; ABKLM vertices | Abramsky-Brandenburger 2011; ABKLM 2016 | read | yes |
| Acyclic gluing / cycles as the only obstruction | Vorob'ev 1962; BFMY 1983; Atserias-Kolaitis | read | yes |
| Infinite marginal problem (given marginals on index set, Omega a product) | Kellerer 1964; Shortt 1983 | [snip] | named in taxonomy, not as a region |
| Test spaces, manuals, orthocoherence, operational logic, state space convex but not a simplex | Foulis-Randall 1970s-80s; Foulis-Piron-Randall 1983; Wilce survey (SEP "Quantum Logic and Probability Theory") | [skim] SEP only | stance recorded (`conj.abstract_carriers`), content unread |
| Perfect-graph criterion STAB = QSTAB for exclusivity (orthogonality) graphs | Cabello-Severini-Winter (PRL 2014 / E-principle) | not searched here | `own.exclusivity_principle` recorded at [search] level |
| Convergent KS property: satisfiability for pBAs of projectors is NP-complete / ETR-complete | Dawar-Shah arXiv:2602.24164 | [abs] | no |

## 2. Questions 1-5: known and residue

**Q1. Embedding in ONE Boolean algebra.** Known: KS Thm 0 and Zierler-Schlessinger (embedding iff full set of two-valued states); vdBH make this functorial (the unit A -> L(A) is an embedding iff A is a sub-pBA of a Boolean algebra; L is the free Boolean cover). Overlap-pattern invariants: Greechie loop lemma (no loops of order < 5 does not give states; it gives OMP/OML structure facts), Rogalewicz 3-cycle criterion for being an OMP at all; for probability-consistent families, Vorob'ev/BFMY/Atserias-Kolaitis (acyclicity, induced cycles). Residue: no source seen that states the embedding question for the context POSET alone as a hypergraph invariant (what shape of overlap guarantees A -> L(A) injective, at all sizes). Not searched with a hostile eye in the Czech combinatorial literature (Pulmannova, Tkadlec, Navara 2000 survey); likely partly owned.

**Q2. Two-valued states.** Owned: Greechie 1971 (OMLs with no states), KS sets, Tkadlec, Pták-Pulmannova (unread hardcopy, pinned). Finitely vs sigma-additive: Gudder 1969/84, Navara-Ptak 1983, Dravecky-Sipos 1980 (all recorded). Residue: the pointless direction needs infinity (recorded in repo); no Omega-free formulation seen.

**Q3. What replaces points.** Owned: spectral presheaf and global-section talk (Doring-Isham, Frembs, de Silva-Barbosa), vdBH Stone-type duality for pBAs (K(A) as a limit of Stone spaces, reflection to Stone spaces). Key observation from vdBH Prop 8 (my reading, [meth]): Hom_pBA(A, 2) = Hom_BA(L(A), 2) = points of the Stone space of L(A). So in the Omega-free setting "two-valued state" already means "point of the canonical Omega", and pointlessness in the programme's sense has no meaning at the two-valued level here; it needs a second structure (a sigma-class, or a chosen representation). Burešova-Pták 2024 (recorded) says the same for a fixed logic. Residue: vdBH treat partial COMPLETE Boolean algebras (Thm 7, locale side) but I did not find a sigma-complete variant, nor f.a. probability states (only two-valued homs).

**Q4. Answers-first treatments.** Owner: Foulis-Randall test spaces / Wilce (operational logic Pi(X), orthocoherence, "most test spaces do not embed in a classical test space, and even if they do the embedding may not account for all states", SEP [skim]); convex-operational/GPT (Barnum-Wilce, Mackey). Also the sheaf empirical model (states = no-signalling families) is itself state-first. Residue: no content read from FPR 1983 / Randall-Foulis 1983 / Wilce 2000, 2009 (UNREAD, see §4). Cannot yet say whether test-space "regularity" gives a stated theorem on embedding in a Borel/classical test space in terms of loop type.

**Q5. Finite vs infinite; f.a. vs sigma-additive.** Known: finite: Vorob'ev/BFMY/A-K; compactness for coherence (Howson, de Finetti, recorded); infinite: Kellerer 1964 / Shortt 1983 (marginal problem on products, sigma-additive), Barbosa et al. 1905.08267 (continuous-variable sheaf, still with discrete context set; recorded `own.cv_sheaves_sigma`). Residue: I found NO source treating abstract (non-product) infinite pBAs with f.a. versus sigma-additive consistent families, in the cycle setting. A search for it returned only finite Vorob'ev material and a 2016 consistency theorem (arXiv:1611.00214) for multiple f.a. measures on a fixed (Omega, F).

## 3. Candidate seams (hostile; nearest killer named)

**S1. Free Boolean cover with sigma-structure.** Objects: a pBA whose blocks are sigma-algebras (sigma-complete) with sigma-morphisms on overlaps; colimit in sigma-complete BAs, L_sigma(A), versus the f.a. L(A). Question: when is A -> L_sigma(A) injective, and when do sigma-additive consistent families on A extend to L_sigma(A)? vdBH cover total and "complete" variants, finite KS-type facts; nobody seen for sigma. Killers: vdBH Thm 7 proof pattern may give the colimit for free but not additivity of states; Katrinak-Neubrunn / Neubrunn sigma-class compatibility (recorded, `own.sigma_class_compatibility`); Navara-Ptak 1983.

**S2. Probabilistic twist on OMPs (consistent families vs conv of two-valued states).** Gap between the polytope of block-consistent probability families and conv Hom(A,2), over pBAs with orthogonality (not product) blocks. Question: classify the smallest cycle-type context patterns where the gap is nonzero, in terms of Greechie loop order and block sizes (analogue of "compressed" threshold). Nearest killers: the exclusivity-graph approach (STAB vs QSTAB; equal iff graph perfect, so finite cases reduce to perfect-graph theory), Navara-Rogalewicz/Navara 2000 state-space survey, Sullivant 2006 for the product case. High chance of being owned on the finite side; residue only at infinite sizes.

**S3. Does a context-poset invariant decide injectivity A -> L(A) at all sizes?** Combinatorial (not state-based). The KS property is "L(A) trivial"; the opposite extreme "L(A) faithful" would be characterised by a hypergraph-type condition on the overlap pattern (a Greechie/Helly/loop-like condition). Nearest killers: Greechie loop lemma + Rogalewicz pastings (strong for orthomodular case), Dawar-Shah complexity results (finite, projector pBAs), HLHN hypergraph representation (shape determines the algebra). If S3 exists it is a restatement of Q1 with the shelf's loop results; low novelty prior.

## 4. Unread sources that could close a seam

1. Kochen-Specker, J. Math. Mech. 17 (1967) 59-87, Thm 0 proof and the notion of regularity (S3).
2. HLHN 1711.03748, Sections on hypergraph representation and maximal 4-element blocks (S3, Q1): only abstract/intro read.
3. Navara, "State spaces of orthomodular structures", Rend. Circ. Mat. Palermo 2000 survey (S2, Q2): semipasted families <-> OMP preserving states.
4. Cabello-Severini-Winter, "Graph-theoretic approach to quantum correlations" (PRL 2014) (S2).
5. Foulis-Piron-Randall 1983; Wilce, Handbook of Quantum Logic chapter (Q4).
6. Dawar-Shah arXiv:2602.24164 full text (colimit/KS-property statements).
7. Doring-Frembs 1910.09591 and de Silva-Barbosa 1806.02840 (Q3): whether sigma-/f.a. states on the spectral presheaf appear.
8. Kellerer 1964 Satz 2.2 and Shortt 1983 for the index-set condition (Q5).
9. Pták-Pulmannova 1991 (hardcopy, pinned in memory) for Greechie/state existence at infinite size.

Not shown here: any Lean or computation. No sources saved to the shelf; no SHELF_INDEX edits.
