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
# dependency graph. Prefer a real graphviz: the binaries pygraphviz bundles in
# its own bin/ are linked against DLLs it does not ship and die with
# "error while loading shared libraries". So pygraphviz's bin is APPENDED as a
# last resort, never prepended -- prepending it shadows a working tred.
for d in "/c/Program Files/Graphviz/bin" "/usr/local/bin" "/opt/homebrew/bin"; do
  if [ -x "$d/tred" ] || [ -x "$d/tred.exe" ]; then export PATH="$d:$PATH"; fi
done
PGV_BIN="$(python -c 'import pygraphviz, os; print(os.path.join(os.path.dirname(pygraphviz.__file__), "bin"))' 2>/dev/null || true)"
if [ -n "${PGV_BIN:-}" ] && [ -d "$PGV_BIN" ]; then
  export PATH="$PATH:$PGV_BIN"
fi

# Fail loudly rather than silently emitting an unreduced graph: web.tex no
# longer passes `nonreducedgraph`, so a broken tred is a hard error there and
# the message plasTeX surfaces for it is opaque.
if ! printf 'digraph{a->b;b->c;a->c;}' | tred >/dev/null 2>&1; then
  echo "ERROR: no working 'tred' on PATH." >&2
  echo "  Install graphviz (winget install --id Graphviz.Graphviz), or add" >&2
  echo "  'nonreducedgraph' to the blueprint options in blueprint/src/web.tex." >&2
  exit 1
fi

cd "$HERE/blueprint/src"

echo "Rendering blueprint..."
plastex -c plastex.cfg web.tex

echo
echo "Blueprint written to: formalization/QuerySystem/blueprint/web/index.html"
echo "Dependency graph:     formalization/QuerySystem/blueprint/web/dep_graph_document.html"
