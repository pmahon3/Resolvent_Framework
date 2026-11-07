# Known issues: reconstruction paper (created 2026-11-06)

reviewed: false. Terminology fixes from `notes/programme/TERMINOLOGY_CROSSWALK.md` (Batch 6, approved by the user 2026-11-06). The paper text (`reconstruction.tex`, `reconstruction_skeleton.tex`) is not edited. Apply these at the next revision.

- **"commensurable / commensurability"** clashes with quantum usage, where *commensurable observables* means jointly measurable, a property of a pair of observables. Here it is a property of a scenario: the coherence polytope C equals the realisability polytope R. Gloss at first use as "contextuality-free scenario (C = R)" (crosswalk C11). Owners of the region: Vorob'ev 1962; Beeri–Fagin–Maier–Yannakakis 1983 (`glued_carriers_taxonomy.json` own.vorobev_acyclic); Kharoof–Ipek–Okay 2024.
- **"window"** here is a sliding length-L block (a cylinder) on a symbolic orbit, not the two-coordinate context of the glued-carriers notes (crosswalk C9). Say so at first use (skeleton §1, l.20).
- **Winding criterion** = Kharoof–Ipek–Okay 2024 Thm 4.4 (`own.cycle_vertices_fixed_L`). The skeleton cites it at §boundary (l.122); check that every earlier use (abstract, intro) carries the citation too, as CLAUDE.md requires.
- **Safe(ρ)** ↔ Abramsky–Barbosa–Kishida–Lal–Mansfield 2016 Prop 6.3 (`own.abklm_vertex_form`): unsafe iff a strongly contextual support exists. Cited at skeleton l.125; check the abstract-level use (l.38).
- **EA / PR vocabulary** (empirical adequacy / probabilistic realism) belongs to Paper II, which is PARKED after its 2026-10-27 reversal (`../paper_ii/PAPER_II_REVERSAL_CHECK.md`). Remove it or mark it as parked framing. The crosswalk counts about 15 EA/PR/VDR hits in the skeleton and 7 in the main file.
- **"reach"** (`lem:reach`) keeps its name: digraph reachability, the paper's open core. The synchrony notes' "reach of a centre" was renamed "cause arity" to free the word (crosswalk C3).
