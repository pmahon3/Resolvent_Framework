#!/bin/bash
# The build tree and the source tree must name the same modules.
#
# Why this exists: no other gate looks at `.lake/build`. checkdecls, axiomcheck
# and the sorry ratchet all read the Lean ENVIRONMENT, and the environment is
# whatever `import QuerySystem` reaches. An olean with no source is outside it,
# so every one of those gates is blind to one.
#
# Both directions have already bitten this repo, and they bite in different
# places:
#
#   ORPHAN OLEAN (no source). On 2026-08-31 a bare `import QuerySystem` failed
#   on a duplicate `TwoValuedState.toFinAdd` coming from a 2026-07-06
#   SigmaEssentialAmended.olean whose source had been renamed months earlier;
#   `lakefile.toml`'s `QuerySystem.+` glob picks up orphan oleans. That one
#   announced itself as a hard error only because it collided. The three found
#   on 2026-09-01 did not collide and so were silent -- among them
#   ZZTestKS.olean, which declared `ZZTestKS.ks_inconsistent : False` resting on
#   KochenSpecker_witness, the false axiom deleted from the sources. A live,
#   importable proof of `False` sat in the build tree while all five gates
#   reported green. The axiom census could not see it: the census enumerates
#   what `import QuerySystem` reaches, and nothing imports an orphan.
#
#   UNBUILT SOURCE (no olean). Until 2026-08-21 `lakefile.toml` declared the
#   library with no `globs`, `lake build` compiled only the root module, and 46
#   of 47 files went unchecked behind a green build -- PredictiveState.lean sat
#   broken for months. `globs` is set now, but nothing verifies that it still
#   covers every file. This direction is the one that can fail in CI.
#
# Run after `lake build`. A missing build tree is a FAILURE, not a pass: a
# check that reports OK when it did not run is worse than no check.
set -euo pipefail
# `comm` requires its inputs sorted in the collation it compares with, and this
# gate runs on both Windows (Git Bash) and ubuntu-latest. Pin both.
export LC_ALL=C

HERE="$(cd "$(dirname "$0")" && pwd)"
PKG="$(dirname "$HERE")"
SRC="$PKG/QuerySystem"
LIB="$PKG/.lake/build/lib/lean"
BUILD="$LIB/QuerySystem"
# Shown in the removal hint: absolute paths here are unreadably long.
REL=".lake/build/lib/lean/QuerySystem"

if [ ! -d "$SRC" ]; then
  echo "BUILDTREE FAIL: no $SRC -- the check did not run." >&2
  exit 1
fi
if [ ! -d "$BUILD" ]; then
  echo "BUILDTREE FAIL: no $BUILD -- run 'lake build' first; the check did not run." >&2
  exit 1
fi

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

# Module names relative to the QuerySystem/ namespace, plus the root module,
# which lives beside the namespace directory rather than inside it.
( cd "$SRC" && find . -name '*.lean' | sed 's|^\./||; s|\.lean$||' ) > "$tmp/src"
[ -f "$PKG/QuerySystem.lean" ] && echo "<root>" >> "$tmp/src"
sort -o "$tmp/src" "$tmp/src"

( cd "$BUILD" && find . -name '*.olean' | sed 's|^\./||; s|\.olean$||' ) > "$tmp/obj"
[ -f "$LIB/QuerySystem.olean" ] && echo "<root>" >> "$tmp/obj"
sort -o "$tmp/obj" "$tmp/obj"

comm -13 "$tmp/src" "$tmp/obj" > "$tmp/orphans"
comm -23 "$tmp/src" "$tmp/obj" > "$tmp/unbuilt"

nsrc=$(wc -l < "$tmp/src" | tr -d ' ')
nobj=$(wc -l < "$tmp/obj" | tr -d ' ')
norph=$(grep -c . "$tmp/orphans" || true)
nunb=$(grep -c . "$tmp/unbuilt" || true)

echo "build tree: $nobj oleans against $nsrc sources"

rc=0
if [ "$norph" -gt 0 ]; then
  echo "BUILDTREE FAIL -- $norph olean(s) with no source file." >&2
  echo "  These are invisible to every other gate. From $PKG, remove them:" >&2
  while IFS= read -r m; do
    [ -z "$m" ] && continue
    echo "    QuerySystem.$m" >&2
    echo "      rm -f $REL/$m.{olean,ilean,trace,olean.hash,ilean.hash}" >&2
  done < "$tmp/orphans"
  rc=1
fi
if [ "$nunb" -gt 0 ]; then
  echo "BUILDTREE FAIL -- $nunb source file(s) with no olean." >&2
  echo "  Either the build is stale, or lakefile.toml's globs no longer cover" >&2
  echo "  them -- the shape of the pre-2026-08-21 bug where 46 of 47 files went" >&2
  echo "  unchecked behind a green build. Run 'lake build' and re-check." >&2
  sed 's/^/    QuerySystem./' "$tmp/unbuilt" >&2
  rc=1
fi
[ "$rc" -ne 0 ] && exit 1

echo "BUILDTREE OK -- every olean has a source and every source has an olean."
