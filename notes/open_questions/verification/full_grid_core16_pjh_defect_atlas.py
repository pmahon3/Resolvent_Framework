#!/usr/bin/env python3
"""Extract the finite first-PJH-defect atlas from the exhaustive P(16) DAG.

This is a structural verifier over the already exhaustive core16 receipt.  It
does not replay the 16-point search and makes no assertion that PJH holds in a
full-grid terminal.  It records every internal forcing state at which the
existential hull of the corresponding full-grid join may first fail to be an
event.
"""
import argparse, collections, hashlib, itertools, json, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = "full_grid_2x2_rectangle_core16_exhaustive.json"
SCHEMA = "full-grid-core16-pjh-defect-atlas-v1"
FULL = (1 << 16) - 1

def mask16(pred):
    return sum(1 << j for j in range(16)
               if pred((j >> 3) & 1, (j >> 2) & 1,
                       (j >> 1) & 1, j & 1))

def raw16():
    out = {0, FULL}
    for a in (0, 1):
        for i in (0, 1):
            for bits in range(16):
                out.add(mask16(lambda q0,q1,r0,r1,a=a,i=i,bits=bits:
                    bool(bits & (1 << (2 * (q0,q1)[a] + (r0,r1)[i])))))
    return frozenset(out)

def close16(seed):
    ev = set(seed)
    while True:
        arr = np.fromiter(ev, dtype=np.uint32, count=len(ev))
        cand = set(np.bitwise_xor(np.uint32(FULL), arr).tolist())
        for lo in range(0, len(arr), 4096):
            block = arr[lo:lo+4096]
            unions = block[:,None] | arr[None,:]
            disjoint = (block[:,None] & arr[None,:]) == 0
            cand |= set(unions[disjoint].tolist())
        new = cand - ev
        if not new:
            return frozenset(ev)
        ev |= new

def family_sha(fam):
    return hashlib.sha256(
        ",".join(str(x) for x in sorted(fam)).encode()).hexdigest()

def payload():
    source = json.load(open(os.path.join(HERE, SOURCE)))
    core = source["payload"]
    assert core["search_capped"] is False
    assert core["every_terminal_reconstructs_a_same_side_boundary"] is True
    tree = core["tree"]
    ids = {n["id"] for n in tree}
    assert len(tree) == len(ids)
    internal = [n for n in tree if "children" in n]
    terminal = [n for n in tree if n.get("outcome") == "terminal"]
    assert len(tree) == 48 and len(internal) == 31 and len(terminal) == 17
    assert sum(len(n["children"]) for n in internal) == 64
    assert collections.Counter(len(n["children"]) for n in internal) == {2:30,4:1}
    assert max(n["depth"] for n in tree) == 6

    # Replay each first-seen path, including memo targets, rather than trusting
    # interval metadata alone.
    by_path = {tuple(n["path_choices_hex"]): n for n in tree}
    families = {}
    root = close16(raw16())
    assert len(root) == core["initial_closure_events"] == 82
    families[()] = root
    for n in sorted(tree, key=lambda x:(x["depth"],x["id"])):
        path = tuple(n["path_choices_hex"])
        if path:
            parent = path[:-1]
            assert parent in families
            z = int(path[-1], 16)
            families[path] = close16(families[parent] | {z, FULL ^ z})
        assert len(families[path]) == n["events"]
    family_to_id = {families[tuple(n["path_choices_hex"])]:n["id"] for n in tree}
    assert len(family_to_id) == len(tree)
    terminal_by_sha = {t["family_sha256"]:t for t in core["terminals"]}

    records = []
    for n in internal:
        fam = families[tuple(n["path_choices_hex"])]
        lo = int(n["chosen_lower_hex"], 16)
        hi = int(n["chosen_upper_hex"], 16)
        children = [int(x, 16) for x in n["children"]]
        assert lo & ~hi == 0
        gap = hi & ~lo
        assert gap.bit_count() == n["gap_bits"]
        expected = sorted(lo | s for s in range(1 << 16) if s & ~gap == 0)
        assert sorted(children) == expected
        assert lo in children and hi in children
        upper_bounds = [u for u in fam if lo & ~u == 0]
        actual_hi = FULL
        for u in upper_bounds:
            actual_hi &= u
        assert actual_hi == hi and hi not in fam
        subs = sorted(e for e in fam if e & ~lo == 0)
        witness = next((a,b) for a in subs for b in subs if a <= b and a|b==lo)
        assert witness[0] in fam and witness[1] in fam
        assert witness[0] | witness[1] == lo
        edge_records=[]
        for z in children:
            child = close16(fam | {z, FULL ^ z})
            assert child in family_to_id
            target = family_to_id[child]
            target_node = next(x for x in tree if x["id"] == target)
            outcome = "terminal" if target_node.get("outcome") == "terminal" else "internal"
            edge_records.append({"candidate_hull_hex":hex(z),
                "child_family_sha256":family_sha(child),
                "target_node_id":target,"target_outcome":outcome})
        records.append({
            "node_id": n["id"], "depth": n["depth"],
            "path_choices_hex": n["path_choices_hex"],
            "events_in_profile_family": n["events"],
            "failed_lower_hex": n["chosen_lower_hex"],
            "failed_upper_hex": n["chosen_upper_hex"],
            "gap_bits": n["gap_bits"], "candidate_hulls_hex": n["children"],
            "node_family_sha256":family_sha(fam),
            "witness_pair_hex":[hex(witness[0]),hex(witness[1])],
            "upper_bound_count":len(upper_bounds),
            "upper_is_intersection_of_all_upper_bounds":True,
            "upper_is_absent":True,"edges":edge_records,
        })
    interval_hist = collections.Counter(
        (r["failed_lower_hex"], r["failed_upper_hex"]) for r in records)
    atlas_digest = hashlib.sha256(json.dumps(
        records, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    terminal_checks=[]
    q_atoms=[sum(1<<j for j in range(16) if ((j>>3)&1)==e and ((j>>2)&1)==f)
             for e in (0,1) for f in (0,1)]
    r_atoms=[sum(1<<j for j in range(16) if ((j>>1)&1)==e and (j&1)==f)
             for e in (0,1) for f in (0,1)]
    for n in terminal:
        fam=families[tuple(n["path_choices_hex"])]
        sha=family_sha(fam);assert sha in terminal_by_sha
        cert=terminal_by_sha[sha]
        cls=cert["classification"]
        assert cls["reconstructs_q0q1"] or cls["reconstructs_r0r1"]
        assert cert["lattice"] is True
        q_present=all(a in fam for a in q_atoms);r_present=all(a in fam for a in r_atoms)
        assert q_present==cls["reconstructs_q0q1"]
        assert r_present==cls["reconstructs_r0r1"]
        terminal_checks.append({"node_id":n["id"],"family_sha256":sha,
            "terminal_lattice_certified_by_source_receipt":True,
            "q_side_atom_words_hex":[hex(a) for a in q_atoms] if q_present else [],
            "r_side_atom_words_hex":[hex(a) for a in r_atoms] if r_present else [],
            "reconstructs_q0q1":q_present,"reconstructs_r0r1":r_present})
    out = {
        "schema": SCHEMA, "schema_version": "1.0",
        "source_receipt": SOURCE,
        "source_payload_sha256": source["payload_sha256"],
        "profile_points": core["points"],
        "dag_nodes": len(tree), "internal_forcing_nodes": len(internal),
        "reconstructing_terminal_nodes": len(terminal),
        "distinct_failed_intervals": len(interval_hist),
        "candidate_hull_edges": sum(len(n["children"]) for n in internal),
        "all_interval_endpoints_included":True,
        "branching_histogram": {str(k):v for k,v in sorted(
            collections.Counter(len(n["children"]) for n in internal).items())},
        "maximum_depth": max(n["depth"] for n in tree),
        "all_terminal_nodes_reconstruct_a_side": True,
        "all_edges_resolve_to_replayed_nodes":True,
        "records_sha256": atlas_digest, "records": records,
        "terminal_checks":terminal_checks,
        "source_producer_sha256":hashlib.sha256(open(os.path.join(
            HERE, source["generator"]),"rb").read()).hexdigest(),
        "theorem_scope": (
            "finite first-defect atlas conditional on the hand PJH descent "
            "argument and the banked exhaustive P(16) covering theorem; no "
            "claim that a full-grid terminal realizes or excludes any defect"),
        "command": ("python3 notes/open_questions/verification/"
                    "full_grid_core16_pjh_defect_atlas.py --verify"),
    }
    out["producer_sha256"] = hashlib.sha256(open(__file__, "rb").read()).hexdigest()
    out["payload_sha256"] = hashlib.sha256(json.dumps(
        out, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--emit", action="store_true")
    ap.add_argument("--verify", action="store_true")
    args = ap.parse_args()
    out = payload()
    path = os.path.join(HERE, "full_grid_core16_pjh_defect_atlas.json")
    if args.emit:
        with open(path, "w") as f:
            json.dump(out, f, sort_keys=True, indent=2); f.write("\n")
    elif args.verify or os.path.exists(path):
        assert json.load(open(path)) == out
    print(json.dumps({"status":"PASS", "payload_sha256":out["payload_sha256"],
        "internal_nodes":out["internal_forcing_nodes"],
        "candidate_hull_edges":out["candidate_hull_edges"]},
        sort_keys=True, indent=2))

if __name__ == "__main__":
    main()
