# Terminology citation check

reviewed: false. Date: 2026-11-07. Scope: the `[unverified]` tags from the "Applied 2026-11-06" section of `TERMINOLOGY_CROSSWALK.md`.

Method: shelf index and `*_taxonomy.json` greps (none of these except KIO 2024 and Evans 2012 is on the shelf), then web search or fetch of publisher, journal, arXiv or library pages. Where a source was seen only through search snippets or secondary pages, the row says so. No full texts were read, so every "claim" column is verified at the level of abstract, catalogue or survey, not proof.

## Priority: Harary and the sign convention

- **Balance (Harary 1953).** F. Harary, "On the notion of balance of a signed graph", Michigan Math. J. 2(2) (1953) 143-146, doi:10.1307/mmj/1028989917. A signed graph is balanced iff every cycle has positive sign product (equivalently, it switches to all-positive). Confirmed from Wikipedia, MaRDI and arXiv surveys, not from the paper text.
- **"Frustration" is not Harary's 1953 word.** Harary calls a negative cycle "unbalanced". "Frustrated" comes from spin glasses (Toulouse, Commun. Phys. 2 (1977) 115-119: a plaquette with an odd number of negative bonds is frustrated). In signed graphs, Zaslavsky's "frustration index" renames Harary's "line index of balance" (Harary, Behavioral Science 4 (1959) 316-323): the minimum number of edges whose deletion or sign flip gives balance.
- **Repo error, now fixed.** The repo wrote "Harary's frustrated (product -1)". The convention is right (frustrated cycle = product -1); the attribution is wrong. Fixed to "Toulouse 1977; Zaslavsky; Harary 1953 says unbalanced".
- **Antibalanced.** F. Harary, "Structural duality", Behavioral Science 2 (1957) 255-265. Antibalanced iff the negation -Sigma is balanced; equivalently every even cycle is positive and every odd cycle is negative, i.e. sign product (-1)^length; equivalently switches to all-negative. Sources: 2022 arXiv survey attributing it to Harary, and several arXiv papers by Zaslavsky and others. The 1957 paper itself was not seen. **The repo's "antibalanced" (signs of -R balanced; product (-1)^length) matches the standard meaning.** Check on the all-negative triangle: product -1 = (-1)^3, so antibalanced. Balance and antibalance are not complementary (a positive triangle is neither).
- **Repo's "not antibalanced"** = frustration of -R. It is not frustration of R, and it reads the other way from the signed-graph "frustrated" on odd cycles. The corrected gloss says so.

## Table

| Item | Citation | Repo claim | Verdict |
|---|---|---|---|
| Harary 1953 | Michigan Math. J. 2(2) 143-146 | balanced = all cycles positive; "frustrated" = product -1 | CORRECTED: convention right, "frustrated" is Toulouse 1977 / Zaslavsky, not Harary (see above) |
| Harary 1957 | Behavioral Science 2, 255-265 | antibalanced | VERIFIED (definition via secondary sources; paper text not seen) |
| Kolmogorov-Bochner | Bochner, Harmonic Analysis and the Theory of Probability, Univ. California Press 1955 (Thm 5.1.1 per a citing paper) | consistent marginals on a projective system extend to a limit | VERIFIED; extension holds for projective systems of (standard Borel / locally compact) spaces. Repo had no date; note it is 1955, not 1947 |
| Johnstone | Stone Spaces, Cambridge Studies in Adv. Math. 3, CUP 1982; "The point of pointless topology", Bull. AMS 8 (1983) | locale / point-free ancestry | VERIFIED |
| KIO 2024 | Kharoof, Ipek, Okay, arXiv:2406.19961 (shelf) | contextuality read as holonomy | NOT VERIFIABLE for the "holonomy" reading: the abstract says "homotopical methods in simplicial distributions", no "holonomy". Paper itself is on the shelf. Tag kept |
| Fine 1982 | Phys. Rev. Lett. 48 (1982) 291-295, doi:10.1103/PhysRevLett.48.291 | joint distribution exists iff local hidden-variable model; Bell-type inequalities equivalent | VERIFIED (Garg-Mermin PRL 49 (1982) 1220 shows sufficiency fails for 8 variables; scope caveat) |
| Bishop-Fienberg-Holland | Discrete Multivariate Analysis: Theory and Practice, MIT Press 1975 (Springer reprint 2007) | no-three-factor interaction | VERIFIED bibliographically; the section (sec. 2.4, three-dimensional arrays) was inferred from the TOC, not read |
| Varga | R. S. Varga, "On recurring theorems on diagonal dominance", LAA 13 (1976) 1-9 (exists); also Matrix Iterative Analysis (1962) | H-matrix / generalized diagonal dominance margin | NOT VERIFIABLE: could not confirm Varga as the H-matrix source (a later paper cites Ostrowski 1937 and Varga 1976). Verified instead: Boman-Chen-Parekh-Toledo, LAA 405 (2005) 239-248: factor width <= 2 = symmetric H-matrices with nonnegative diagonal. Tag kept on Varga, Boman cited alongside |
| Agler et al. 1988 | Agler, Helton, McCullough, Rodman, LAA 107 (1988) 101-149, doi:10.1016/0024-3795(88)90240-6 | owner of the chordal sparse-PSD cone decomposition | VERIFIED; surveys attribute the clique-sum decomposition to it. Co-owner: Griewank-Toint 1984 (independent), also Kakimura 2010 |
| Vandenberghe-Andersen | Chordal Graphs and Semidefinite Optimization, Found. Trends Optim. 1(4) (2015) 241-433, doi:10.1561/2400000006 | survey of chordal cones | VERIFIED (publisher page) |
| Vietoris-Rips | Vietoris, Math. Ann. 97 (1927) 454-472; popularised by Gromov 1987; name "Vietoris-Rips" due to Hausmann 1995; Rips's work unpublished | H(d) = complex of point sets of diameter <= d | VERIFIED |
| Campbell-Fiske 1959 | Psychol. Bull. 56 (1959) 81-105 | method variance vs trait variance | VERIFIED |
| Leek et al. 2010 | Nat. Rev. Genet. 11(10) (2010) 733-739, doi:10.1038/nrg2825 | batch effects | VERIFIED |
| Ostrom | V. Ostrom, Tiebout, Warren, Amer. Polit. Sci. Rev. 55(4) (1961) 831-842, doi:10.1017/S0003055400125973; E. Ostrom, Amer. Econ. Rev. 100(3) (2010) 641-672 | polycentric governance as the source of the metaphor | VERIFIED (2010 paper itself credits Ostrom-Tiebout for the concept) |
| Reichenbach | The Direction of Time, Univ. California Press 1956 (posthumous; ed. M. Reichenbach) | common cause principle | VERIFIED (SEP) |
| Evans 2016 | "Graphs for margins of Bayesian networks", Scand. J. Stat. 43(3) (2016), arXiv:1408.1809, doi:10.1111/sjos.12194 | mDAGs; hyperedge = latent common cause | VERIFIED for mDAGs / latent-variable margins. Not confirmed: "faces" and inequality constraints (abstract silent; those are in Evans 2012, on shelf). The repo's claim in `theory_shape.md` is only "mDAG hyperedge", which holds |

## Other tags found (not on the assigned list)

- `papers/sigma_essential/KNOWN_ISSUES.md:10`: carrier = support of a measure (Bhaskara Rao, Bourbaki) `[unverified]`. Not checked; left tagged.
- `notes/open_questions/views_across_records/synchrony_dataset_scout.md`, `neuro_critical/prior_art.md`: snippet-level dataset and literature flags, own sense. Left tagged.
- `notes/TAXONOMY_SCHEMA.md:71` describes the tag convention; left.

## Edits made

`[unverified]` removed (full citation added) for VERIFIED items; Harary attribution corrected; remaining tags: KIO holonomy reading and Varga, both in `theory_shape.md` (Varga also in `SYNCHRONY_CAUSALITY_METHOD.md`).
