/-
# QuerySystem -- library root

This module is an INDEX: it imports every module of the library and declares
nothing itself.

## Why it is an index and not a source file

Until 2026-08-21 this file was a 26K source file that defined `Query`,
`Refine`, `QuerySystem`, `QuerySystem.Omega` and ~20 more declarations -- all
of which `QuerySystem/QuerySystem.lean` (82K) ALSO defines. Both were created
in `8c55137` (2026-03-18); the submodule then received nine commits of
development while this file's content was last changed in that same first
commit. Every other module imports `QuerySystem.QuerySystem`; nothing imported
the root.

Two modules defining the same names is not merely untidy: importing both is a
hard error ("environment already contains ..."), which is how this was found --
the blueprint declaration check could not name an import set that resolved.

The old file is preserved at `archive/QuerySystemRootLegacy.lean`. It is not
built (only `QuerySystem.+` is globbed). It is the superseded LOWER-directed
generation of the theory: its one declaration absent from the submodule is
`finCyl_eq_cyl_of_lowerBound`, whose successor is
`finCyl_eq_cyl_of_upperBound`. That lemma had no users.

Because `lakefile.toml` globs `QuerySystem.+` -- the root module AND its
submodules -- building this index builds the library.
-/

import QuerySystem.AJNoExtension
import QuerySystem.AndersenJessen
import QuerySystem.BandClosure
import QuerySystem.BoundaryDescent
import QuerySystem.Commensurability
import QuerySystem.ConcreteOMLBlocks
import QuerySystem.ConcreteOMLPatterns
import QuerySystem.DelayEmbedding
import QuerySystem.DescentWitnessClosure
import QuerySystem.DescentWitnessConsistency
import QuerySystem.DescentWitnessFinite
import QuerySystem.DescentWitnessInfinite
import QuerySystem.Diagonal
import QuerySystem.DiscriminabilityFoundations
import QuerySystem.EncodingDefectCheck
import QuerySystem.ExtensionObstruction
import QuerySystem.FibreProductReflection
import QuerySystem.FiniteAtomFoldKernel
import QuerySystem.FullCycleAssemblyKernel
import QuerySystem.InnerRegularity
import QuerySystem.KernelClosureCalculus
import QuerySystem.MarczewskiTransport
import QuerySystem.ODBCRegimes
import QuerySystem.ODBCSections
import QuerySystem.Omega7Counterexample
import QuerySystem.OrthomodularMO2
import QuerySystem.PruningTheorem
import QuerySystem.QuerySystem
import QuerySystem.ReconstructionTheorem
import QuerySystem.RelationalDelay
import QuerySystem.SigmaEssentialAmended
import QuerySystem.SigmaEssentialBareForm
import QuerySystem.SigmaEssentialConjectures
import QuerySystem.SigmaEssentialLocalization
import QuerySystem.SigmaEssentialOpenCore
import QuerySystem.StoneDualityExtension
import QuerySystem.TheoremB
import QuerySystem.ThickTrace
import QuerySystem.UlamWitnessCore
import QuerySystem.UlamWitnessFidelity
import QuerySystem.UlamWitnessInvariant
import QuerySystem.UlamWitnessLatticeGap
import QuerySystem.UlamWitnessMain
import QuerySystem.UlamWitnessOmega1
import QuerySystem.UlamWitnessReceipts
import QuerySystem.UlamWitnessState
import QuerySystem.UltrafilterCharge
import QuerySystem.WindingDichotomy
import QuerySystem.WindingInjectivity
