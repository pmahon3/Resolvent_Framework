#!/usr/bin/env python3
"""Research decision graph: advisory change-impact for the programme.

Nodes  = entries of every tracked *_taxonomy.json (ids qualified as `collection:id`)
         + nodes in notes/programme/decision_graph.json (layer 0-2 items, papers, decisions).
Edges  = justification: `uses` / `rests_on` (list of ids or {id, kind: statement|proof});
                        `rests_on_any` (list of alternative support groups, TMS OR-groups).
         influence:     `informs` ([{to, date, kind}]) - may loop; reported, never propagated.

Commands (read-only; statuses are NEVER written - "record, not propagate"):
  check            dangling ids, justification cycles (error), layer-direction lint
  impact <id>      transitive dependents (sole support vs alternative remains), sorted
                   least-entrenched first, 1-hop `informs`, and UNDECLARED mentions found by
                   grepping the node's id and `labels` across the repo
Design: docs/research_decision_graph_prior_art.md (sections c-d).
"""
import json, re, subprocess, sys
from pathlib import Path
import networkx as nx

ROOT = Path(__file__).resolve().parent.parent
DG = ROOT / "notes/programme/decision_graph.json"
SEARCH_DIRS = ["notes", "papers", "docs", "formalization/QuerySystem/blueprint/src",
               "formalization/QuerySystem/QuerySystem", "CLAUDE.md", "WHY.md"]   # v1: Lean sources included
GRADE = {"lean": 6, "hand-verified": 5, "hand-unverified": 4, "cited-read": 3,
         "cited-secondary": 2, "llm": 1, None: 0}
LAYER_BY_KEY = {"theorems": 3, "conjectures": 3, "objects": 3, "examples": 4, "probes": 4,
                "owned_regions": 5}


def grade_of(n):
    if n.get("grade") in GRADE:
        return n["grade"]
    s = (n.get("status") or "").lower()
    if "lean" in s:
        return "lean"
    if "hand" in s or "proved" in s:
        return "hand-unverified"
    if "owned" in s or "read" in s:
        return "cited-read"
    return None


def norm_edges(v):
    out = []
    for e in v or []:
        if isinstance(e, str):
            out.append((e, "statement"))
        elif isinstance(e, dict) and "id" in e:
            out.append((e["id"], e.get("kind", "statement")))
    return out


def load():
    nodes = {}
    tax = subprocess.run(["git", "ls-files", "*_taxonomy.json"], cwd=ROOT,
                         capture_output=True, text=True).stdout.split()
    for rel in tax:
        coll = Path(rel).stem.replace("_taxonomy", "")
        try:
            data = json.load(open(ROOT / rel))
        except Exception as ex:
            print(f"WARN cannot parse {rel}: {ex}")
            continue
        for key, val in data.items():
            if not isinstance(val, list):
                continue
            for e in val:
                if isinstance(e, dict) and "id" in e:
                    nid = f"{coll}:{e['id']}"
                    nodes[nid] = dict(e, _file=rel, _coll=coll,
                                      layer=e.get("layer", LAYER_BY_KEY.get(key, 3)))
    if DG.exists():
        for e in json.load(open(DG))["nodes"]:
            nodes[e["id"]] = dict(e, _file=e.get("file", str(DG.relative_to(ROOT))), _coll="")
    return nodes


def resolve(ref, src, nodes):
    if ref in nodes:
        return ref
    coll = nodes[src].get("_coll")
    if coll and f"{coll}:{ref}" in nodes:
        return f"{coll}:{ref}"
    return None


def build(nodes):
    g, inf, dangling = nx.DiGraph(), [], []
    g.add_nodes_from(nodes)
    for nid, n in nodes.items():
        refs = norm_edges(n.get("uses")) + norm_edges(n.get("rests_on"))
        for grp in n.get("rests_on_any") or []:
            refs += [(r, "statement") for r in grp]
        for ref, kind in refs:
            r = resolve(ref, nid, nodes)
            if r is None:
                dangling.append((nid, ref))
            else:
                g.add_edge(nid, r, kind=kind)          # nid rests on r
        for e in n.get("informs") or []:
            inf.append((nid, e.get("to"), e.get("date"), e.get("kind", "suggests")))
    return g, inf, dangling


def cmd_check(nodes):
    g, inf, dangling = build(nodes)
    err = 0
    for a, b in dangling:
        print(f"DANGLING  {a} -> {b}")
    for comp in nx.strongly_connected_components(g):
        if len(comp) > 1:
            err = 1
            print("CYCLE (justification; circular support):", " -> ".join(sorted(comp)))
    for a, b in g.edges:
        if nodes[a].get("layer", 3) <= 1 and nodes[b].get("layer", 3) >= 4:
            print(f"LINT  aim/stance {a} rests on evidence-level {b}")
    print(f"{len(nodes)} nodes, {g.number_of_edges()} justification edges, "
          f"{len(inf)} informs edges, {len(dangling)} dangling")
    return err


IGNORE = re.compile(r"(^notes/archive/|^archive/|\.py$)")   # v1: no global ignore of reversal records


def grep_mentions(patterns, skip_files=(), lean_only=False):
    """Undeclared mentions. v1: Lean sources searched; per-node `records` files skipped (the
    reversal records OF this node), not all reversal records; returns {file: {(line, label)}} and
    per-label file counts for specificity ranking."""
    hits, per_label = {}, {}
    dirs = ["formalization/QuerySystem/QuerySystem"] if lean_only else SEARCH_DIRS
    for p in patterns:
        if not p:
            continue
        r = subprocess.run(["git", "grep", "-n", "-I", "-F", p, "--"] + dirs, cwd=ROOT,
                           capture_output=True, text=True)
        files = set()
        for line in r.stdout.splitlines():
            f, ln = line.split(":", 2)[:2]
            if IGNORE.search(f) or f in skip_files:
                continue
            hits.setdefault(f, set()).add((int(ln), p))
            files.add(f)
        per_label[p] = len(files)
    return hits, per_label


def cmd_impact(nodes, target, cap=40):
    g, inf, _ = build(nodes)
    target = target if target in nodes else next((k for k in nodes if k.endswith(":" + target)), None)
    if target is None:
        print("unknown id"); return 2
    deps = nx.ancestors(g, target)               # nodes that (transitively) rest on target
    affected = deps | {target}
    rows = []
    for d in deps:
        n = nodes[d]
        groups = n.get("rests_on_any") or []
        alt = any(all(resolve(r, d, nodes) not in affected for r in grp) for grp in groups)
        direct = target in g.successors(d)
        rows.append((GRADE[grade_of(n)], n.get("layer", 3), d,
                     "alternative remains -> re-verify" if alt else "SOLE support -> retract/re-verify",
                     "direct" if direct else "indirect", n["_file"]))
    rows.sort()
    print(f"IMPACT of {target}  ({len(rows)} declared dependents; least entrenched first)")
    for gr, lay, d, verdict, how, f in rows[:cap]:
        print(f"  [L{lay} {grade_of(nodes[d]) or '-'}] {d}  {verdict} ({how})  {f}")
    if len(rows) > cap:
        print(f"  ... {len(rows) - cap} more")
    for a, b, date, kind in inf:
        if b in affected:
            print(f"  INFORMS ({kind}, {date}): {a} was {kind} by an affected node -> re-prioritise")
    declared_files = {nodes[d]["_file"] for d in affected}
    skip = set(nodes[target].get("records") or [])
    pats = [target.split(":")[-1]] + list(nodes[target].get("labels") or [])
    hits, per_label = grep_mentions(pats, skip)
    code_hits, code_per = grep_mentions(list(nodes[target].get("code_labels") or []), skip, lean_only=True)
    for f, v in code_hits.items():
        hits.setdefault(f, set()).update(v)
    per_label.update(code_per)
    und = {f: v for f, v in hits.items() if f not in declared_files}
    # v1 specificity: a file's score = best (smallest) file-count among the labels that hit it;
    # labels matching more than BROAD files are marked broad and listed last.
    BROAD = 25
    def score(f):
        return min(per_label.get(p, 999) for _, p in und[f])
    print(f"UNDECLARED mentions ({len(und)} files; most specific first; add an edge or mark mentions_only):")
    print("  label file-counts: " + ", ".join(f"{p}={n}{' (broad)' if n > BROAD else ''}"
                                             for p, n in sorted(per_label.items(), key=lambda x: x[1])))
    for f in sorted(und, key=lambda f: (score(f), f)):
        lines = sorted(und[f])
        tag = " [broad-only]" if score(f) > BROAD else ""
        print(f"  {f}{tag}: " + ", ".join(f"{ln}[{p}]" for ln, p in lines[:8])
              + (f" (+{len(lines) - 8})" if len(lines) > 8 else ""))
    return 0


def main(argv):
    nodes = load()
    if len(argv) >= 2 and argv[1] == "check":
        return cmd_check(nodes)
    if len(argv) >= 3 and argv[1] == "impact":
        return cmd_impact(nodes, argv[2])
    print(__doc__); return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
