# Taxonomy schema & conventions

*How the per-collection JSON taxonomies are structured, so they stay consistent and
the format is reproducible. Validated against the 6 taxonomies registered in
`taxonomies_index.json` (2026-06-26). A taxonomy is a **zoom-out index** of a problem
collection's attempts — cheap to load, linking down to detailed leaf files.*

---

## The three zoom levels

1. **Registry** — `notes/taxonomies_index.json`: one row per collection. Load first.
2. **Taxonomy** — `<collection>_taxonomy.json`: id + status + one_line per attempt,
   grouped by category. The 50,000-ft shape of one collection.
3. **Leaf** — the `detail` file#anchor each entry points to: full reasoning, proofs,
   verdicts. One leaf md per low-level entry (or a shared archive log).

## File placement & naming

- Name: `<collection>_taxonomy.json`. Place it at the collection's center of gravity
  (its `open_questions/`, `covered_leads/`, paper dir, or `unsorted/` home).
- `detail` pointers are **relative to the taxonomy file's own directory** (use `../`
  to cross directories). The registry's `taxonomy` paths are **relative to repo root**.

## Required top-level structure

```json
{
  "$meta": { ... },           // self-describing header (see below)
  "<category_1>": [ {entry}, {entry}, ... ],
  "<category_2>": [ ... ],
  ...
}
```

Categories are **collection-specific** (the schema does not fix them) — e.g.
σ-essential uses walls/candidate_carriers/strategies/costumes/fenced_reversals/
settled_facts/open_frontier; κ_Q uses ladder_levels/.../kills; Paper II uses
contributions/results/owned/blocking_gaps/kills/polish. Choose categories that match
the collection's actual shape. List them in `$meta.categories`.

### `$meta` fields

| field | required | purpose |
|---|---|---|
| `title` | ✓ | collection name |
| `purpose` | ✓ | "zoom-out index … load first … follow detail pointers" |
| `updated` | ✓ | ISO date |
| `what_is_it` | ✓ | one sentence defining the core object/question |
| `status` | ✓ | overall collection status (OPEN / PARKED / REVISE / ARCHIVE-ONLY / MIXED) |
| `the_shape` | ✓ | 2-4 sentences: the structural punchline (what almost everything bottoms out at) |
| `categories` | ✓ | object mapping each category key → one-line meaning |
| `headline` | ✓ | object of small counts (entries per kind, key totals) |
| `scope_note` / `overlap_note` | when relevant | what's excluded and why (e.g. material owned by another collection — do NOT double-list) |

### Entry fields

| field | required | purpose |
|---|---|---|
| `id` | ✓ | stable kebab/dotted handle, unique within the taxonomy (e.g. `wall.disjointification`, `kill.type4`). Cross-collection references use these. |
| `name` | ✓ | short human label |
| `status` | ✓ | from the collection's status vocabulary (open/killed/settled/parked/dead/superseded/forbidden/live/…) |
| `one_line` | ✓ | the whole point in one line — cheap to scan; this IS the zoom-out content |
| `detail` | ✓ | `file#anchor` (or `file; note`) to the leaf holding full reasoning; "self-contained; cf. …" if the one_line suffices |
| `category` | optional | echoes the group key (useful when entries are flattened) |
| `killed` / `examined` | optional | ISO date of the verdict |
| cross-links | optional | `costume_of`, `same_as`, `kills_or_bounds`, `death_number` — ids/links that make structure machine-visible |

## Cross-linking (what makes the tree modular)

- **Within a taxonomy**: `same_as` / `costume_of` / `kills_or_bounds` reference other
  entries' `id`s, so "everything bottoms out at X" is machine-traceable, not just prose.
- **Across taxonomies**: use `[[file-stem]]` wiki-links in `one_line`/`detail` (e.g.
  `[[paper_iii_taxonomy]]`). Shared concepts get the same `id` shape in both.
- **Re-parenting** (the dynamic-mutation goal): when a sub-problem moves up/down an
  abstraction level or between collections, move its entry to the new taxonomy keeping
  its `id`, update cross-links, and add/adjust the registry row. No prose rewrite.

## The hard rules (verify-before-ship)

1. **Valid JSON.** `python3 -c "import json; json.load(open(f))"`.
2. **Every `detail` file resolves.** Resolve each `detail`'s file (before `#`/`;`/`(`)
   relative to the taxonomy's directory; all must exist. This is non-negotiable — a
   taxonomy pointing at phantom/moved files is worse than none. (4 σ-essential pointers
   and several relative-path slips were caught exactly this way.)
3. **No content invented.** Taxonomies are built from an inventory sweep of the actual
   files (an Explore agent grounded in the ledger/notes), never a tidy reconstruction.
4. **Verify before deleting.** Inventory "pure-index" labels are unreliable — three
   σ-essential "Bucket A" files actually held unique content. Before deleting any file,
   confirm its unique content is captured elsewhere (extract to a leaf if not), repoint
   all references, and re-check that pointers still resolve.

## Validation snippet

```python
import json, os, re
d = json.load(open(TAXONOMY))                      # rule 1
files = set()
def walk(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == "detail" and isinstance(v, str):
                t = re.split(r"[;#(]", v)[0].strip()
                if t.endswith((".md", ".json")): files.add(t)
            else: walk(v)
    elif isinstance(o, list): [walk(x) for x in o]
walk(d)
missing = [f for f in files if not os.path.exists(f)]  # run from taxonomy's dir; rule 2
assert not missing, missing
```

## What does NOT get a taxonomy

Programme-meta that isn't a problem-collection: the authoritative state doc
(`program_overview.md`), genealogy/vision narratives, the contribution-evaluation
framework, and reception docs for withdrawn arcs. Listed under
`taxonomies_index.json#not_yet_taxonomized`. Don't force meta into a problem-taxonomy.
