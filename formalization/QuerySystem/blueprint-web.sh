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
LOG="$HERE/blueprint/render.log"
plastex -c plastex.cfg web.tex 2>&1 | tee "$LOG"

# plasTeX reports an undeclared environment as a WARNING and still exits 0, and
# the damage is silent and severe: it attaches that environment's \label to the
# PRECEDING theorem, so the theorem loses its own id and drops out of the
# dependency graph entirely. This is what hid thm:aj-tower
# (AndersenJessen.X_thick, the main Andersen-Jessen result) -- `remark` was used
# five times in content.tex but never declared in macros/common.tex. A warning
# that quietly deletes a theorem from the graph has to be a hard error.
if grep -qiE "unrecognized command/environment" "$LOG"; then
  echo >&2
  echo "ERROR: plasTeX does not recognize an environment used in the blueprint:" >&2
  grep -iE "unrecognized command/environment" "$LOG" | sort -u | sed 's/^/  /' >&2
  echo "  Declare it in blueprint/src/macros/common.tex --" >&2
  echo "  e.g. \newtheorem{remark}[theorem]{Remark} -- then re-render." >&2
  echo "  Until then any theorem preceding one of these is missing from the graph." >&2
  exit 1
fi

echo
echo "Blueprint written to: formalization/QuerySystem/blueprint/web/index.html"
echo "Dependency graph:     formalization/QuerySystem/blueprint/web/dep_graph_document.html"
