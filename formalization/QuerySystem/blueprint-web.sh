#!/bin/bash
# Render the Lean blueprint to blueprint/web/.
#
# NOTE: we call plasTeX directly rather than `leanblueprint web`. The
# leanblueprint CLI resolves the project root with
# `Repo(".", search_parent_directories=True).working_dir`, i.e. the GIT root,
# and assumes the lakefile sits there. In this repo the Lean package is a
# subdirectory (formalization/QuerySystem), so the CLI cannot find the
# lakefile. `leanblueprint web` is only `plastex -c plastex.cfg web.tex` run in
# blueprint/src, which is what this does.
#
# Requires: pip install leanblueprint  (pulls plasTeX, plastexdepgraph,
# plastexshowmore; pygraphviz ships a working `dot`, so no system graphviz).
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"

# plasTeX shells out to kpsewhich to resolve \input targets. On Windows a
# missing kpsewhich fails silently (shell=True), so plasTeX never reaches its
# own fallback search. blueprint/bin holds a shim; harmless if a real TeX
# distribution is installed, since that one is found first only if it precedes
# us on PATH -- prepend ours to keep the render hermetic.
export PATH="$HERE/blueprint/bin:$PATH"

# Declaration names contain non-ASCII (pre-mu, sigmaQ, ...). plasTeX writes
# blueprint/lean_decls with Path.write_text(), which on Windows defaults to
# cp1252 and dies. UTF-8 mode makes that default UTF-8 everywhere.
export PYTHONUTF8=1

# plastexdepgraph shells out to `tred` (transitive reduction) for the
# dependency graph. pygraphviz ships the graphviz binaries in its own bin/ but
# does not put them on PATH.
PGV_BIN="$(python -c 'import pygraphviz, os; print(os.path.join(os.path.dirname(pygraphviz.__file__), "bin"))' 2>/dev/null || true)"
if [ -n "${PGV_BIN:-}" ] && [ -d "$PGV_BIN" ]; then
  export PATH="$PGV_BIN:$PATH"
fi

cd "$HERE/blueprint/src"

echo "Rendering blueprint..."
plastex -c plastex.cfg web.tex

echo
echo "Blueprint written to: formalization/QuerySystem/blueprint/web/index.html"
echo "Dependency graph:     formalization/QuerySystem/blueprint/web/dep_graph_document.html"
