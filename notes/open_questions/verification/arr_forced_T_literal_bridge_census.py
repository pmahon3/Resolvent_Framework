#!/usr/bin/env python3
"""Exact literal bridge census after adjoining the forced interval top ``T``.

The universal one-copy shadows are used only as a sound prefilter for old
cylinders disjoint from T or T^c.  Every retained candidate is then lifted to
one canonical seven-coordinate MDD for the *actual* adjacent carrier.  Thus
event equality, containment, cardinality, and cylindricity below are physical
event statements, not observational-shadow classifications.

No old lower/upper kernel is recomputed for a bridge.  The census closes no
family and makes no claim about later bridge rounds.
"""
import argparse
import functools
import hashlib
import json
import math
import struct
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "arr_forced_interval_top_audit.py"
SOURCE_RECEIPT = HERE / "arr_forced_interval_top_audit.json"
SELECTOR_RECEIPT = HERE / "arr_k8a_deterministic_selector_cut_audit.json"
RECEIPT = HERE / "arr_forced_T_literal_bridge_census.json"


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


class MDD:
    """Reduced ordered MDD over seven 224-valued state coordinates."""

    def __init__(self, domains):
        self.domains = tuple(tuple(x) for x in domains)
        self.nodes = [None, None]
        self.intern = {}
        self.acache = {}
        self.ncache = {0: 1, 1: 0}

    def node(self, variable, children):
        children = tuple(children)
        if all(child == children[0] for child in children):
            return children[0]
        key = (variable, children)
        answer = self.intern.get(key)
        if answer is None:
            answer = len(self.nodes)
            self.intern[key] = answer
            self.nodes.append(key)
        return answer

    def varset(self, variable, values):
        values = set(values)
        return self.node(variable, [int(x in values)
                                    for x in self.domains[variable]])

    def neg(self, root):
        answer = self.ncache.get(root)
        if answer is not None:
            return answer
        variable, children = self.nodes[root]
        answer = self.node(variable, [self.neg(x) for x in children])
        self.ncache[root] = answer
        return answer

    def app(self, kind, left, right):
        # kind 0 = intersection, kind 1 = union.
        if kind == 0:
            if not left or not right:
                return 0
            if left == 1:
                return right
            if right == 1:
                return left
        else:
            if left == 1 or right == 1:
                return 1
            if not left:
                return right
            if not right:
                return left
        if left == right:
            return left
        key = (kind, min(left, right), max(left, right))
        answer = self.acache.get(key)
        if answer is not None:
            return answer
        vl = self.nodes[left][0]
        vr = self.nodes[right][0]
        variable = min(vl, vr)
        lc = (self.nodes[left][1] if vl == variable else
              (left,) * len(self.domains[variable]))
        rc = (self.nodes[right][1] if vr == variable else
              (right,) * len(self.domains[variable]))
        answer = self.node(variable, [self.app(kind, x, y)
                                      for x, y in zip(lc, rc)])
        self.acache[key] = answer
        return answer


def recover():
    """Run the authoritative forced-interval producer and expose its bank."""
    source = SOURCE.read_text()
    needle = "    out = {"
    assert source.count(needle) == 1
    expose = (
        "    globals()['_BRIDGE_BANK'] = {"
        "'d':d,'events':events,'roots':roots,'macros':macros,'engines':engines,"
        "'op':op,'neg':neg,'subset':subset,'t_univ_left':t_univ_left,"
        "'t_exist_left':t_exist_left,'t_univ_right':t_univ_right,"
        "'t_exist_right':t_exist_right}\n"
    )
    source = source.replace(needle, expose + needle)
    namespace = {"__file__": str(SOURCE), "__name__": "_arr_bridge_source"}
    exec(compile(source, str(SOURCE), "exec"), namespace)
    namespace["payload"]()
    return namespace["_BRIDGE_BANK"]


def payload():
    d = recover()
    events, roots = d["events"], d["roots"]
    macros, old_engines = d["macros"], d["engines"]
    op, neg, subset = d["op"], d["neg"], d["subset"]
    arr = d["d"]["arr"]
    n = len(events)
    assert n == 18676 and (arr["pos"], arr["oppos"]) == (3, 0)

    # Prefilter only.  C is actually disjoint from X iff the cylinder C is
    # contained in X^c's universal shadow on its own side.
    zero_old = tuple(0 for _ in macros)
    universal_shadows = {
        "left": {
            "T": d["t_univ_left"],
            "Tc": neg(d["t_exist_left"]),
        },
        "right": {
            "T": d["t_univ_right"],
            "Tc": neg(d["t_exist_right"]),
        },
    }
    # To be disjoint from X, a cylinder must lie in the universal shadow of
    # X^c (not in X's own universal shadow).
    disjoint_old = {
        side: {
            target: [i for i, event in enumerate(events) if op(
                0, roots[event], family["Tc" if target == "T" else "T"]
            ) == roots[event]]
            for target in ("T", "Tc")
        }
        for side, family in universal_shadows.items()
    }

    states = d["d"]["states"]
    domain = tuple(range(len(states)))
    engine = MDD((domain,) * 7)
    left_map = (0, 1, 2, 3)
    right_map = (3, 4, 5, 6)

    # Translate a local macro root to the common 224-valued coordinates and
    # restrict every skipped variable to that macro's domain.
    def local_piece(macro_index, local_root, mapping):
        old = old_engines[macro_index]
        domains = macros[macro_index][1]
        memo = {}

        def translate(root):
            if root <= 1:
                return root
            if root in memo:
                return memo[root]
            variable, children = old.nodes[root]
            by_state = dict(zip(domains[variable], children))
            answer = engine.node(mapping[variable], [
                translate(by_state[x]) if x in by_state else 0 for x in domain
            ])
            memo[root] = answer
            return answer

        answer = translate(local_root)
        for variable, values in enumerate(domains):
            answer = engine.app(0, answer,
                                engine.varset(mapping[variable], values))
        return answer

    lift_cache = {}

    def lift(index, side):
        key = (side, index)
        if key in lift_cache:
            return lift_cache[key]
        mapping = left_map if side == "left" else right_map
        answer = 0
        local_roots = roots[events[index]]
        for macro_index, local_root in enumerate(local_roots):
            if local_root:
                answer = engine.app(
                    1, answer,
                    local_piece(macro_index, local_root, mapping))
        lift_cache[key] = answer
        return answer

    # The one-copy top imposes all local compatibility constraints.  Gluing
    # coordinate 3 of the left copy to coordinate 0 of the right copy gives
    # the exact adjacent carrier.  Its count is an authoritative sanity gate.
    top = next(i for i, event in enumerate(events)
               if roots[event] == tuple(1 for _ in macros))
    left_carrier, right_carrier = lift(top, "left"), lift(top, "right")
    carrier = engine.app(0, left_carrier, right_carrier)

    def compose_truth(predicate_roots, table):
        memo = {}

        def go(rs):
            if rs in memo:
                return memo[rs]
            if all(root <= 1 for root in rs):
                word = sum((root & 1) << k for k, root in enumerate(rs))
                answer = (table >> word) & 1
            else:
                variable = min(engine.nodes[root][0]
                               for root in rs if root > 1)
                children = []
                for choice in range(len(domain)):
                    children.append(go(tuple(
                        engine.nodes[root][1][choice]
                        if root > 1 and engine.nodes[root][0] == variable
                        else root for root in rs
                    )))
                answer = engine.node(variable, children)
            memo[rs] = answer
            return answer

        return go(tuple(predicate_roots))

    relation_inputs = ([lift(i, "left") for i in arr["retained"]] +
                       [lift(i, "right") for i in arr["opposite"]])
    R = engine.app(0, carrier, compose_truth(relation_inputs, arr["F"]))
    Rc = engine.app(0, carrier, engine.neg(R))
    E = lift(18322, "right")
    T = engine.app(0, R, E)
    Tc = engine.app(0, carrier, engine.neg(T))

    selector = json.loads(SELECTOR_RECEIPT.read_text())
    points = [tuple(row["adjacent_state_tuple"])
              for row in selector["selector_points"]]

    def singleton(point):
        answer = carrier
        for variable, value in enumerate(point):
            answer = engine.app(0, answer, engine.varset(variable, {value}))
        return answer

    S = 0
    for point in points:
        S = engine.app(1, S, singleton(point))
    Sc = engine.app(0, carrier, engine.neg(S))
    specials = {"R": R, "Rc": Rc, "S": S, "Sc": Sc,
                "T": T, "Tc": Tc}

    # A coordinate is on its activated row exactly when its local cell state
    # charges all three shared activation atoms.  Testing all seven coordinates
    # is conservative with respect to either row naming and avoids importing a
    # procedural rectangle-layout convention.
    activated_states = {
        i for i, state in enumerate(states)
        if {"a1", "a2", "a3"}.issubset(state)
    }
    activation_cylinders = [
        engine.app(0, carrier, engine.varset(variable, activated_states))
        for variable in range(7)
    ]

    def le(left, right):
        return engine.app(0, left, engine.neg(right)) == 0

    def disjoint(left, right):
        return engine.app(0, left, right) == 0

    @functools.lru_cache(None)
    def structural_hash(root):
        if root <= 1:
            return hashlib.sha256(bytes((root,))).digest()
        variable, children = engine.nodes[root]
        h = hashlib.sha256(b"M" + struct.pack("<I", variable))
        for child in children:
            h.update(structural_hash(child))
        return h.digest()

    @functools.lru_cache(None)
    def count_from(root, level=0):
        if root <= 1:
            return root * math.prod(len(engine.domains[v])
                                    for v in range(level, 7))
        variable, children = engine.nodes[root]
        skipped = math.prod(len(engine.domains[v])
                            for v in range(level, variable))
        return skipped * sum(count_from(child, variable + 1)
                             for child in children)

    def quantify_exists(root, variables):
        variables = frozenset(variables)
        memo = {}

        def go(node):
            if node <= 1:
                return node
            if node in memo:
                return memo[node]
            variable, children = engine.nodes[node]
            mapped = [go(child) for child in children]
            if variable in variables:
                answer = 0
                for child in mapped:
                    answer = engine.app(1, answer, child)
            else:
                answer = engine.node(variable, mapped)
            memo[node] = answer
            return answer

        return go(root)

    projection_carriers = {
        "left": quantify_exists(carrier, {4, 5, 6}),
        "right": quantify_exists(carrier, {0, 1, 2}),
    }

    def cylindrical(root, side):
        eliminated = {4, 5, 6} if side == "left" else {0, 1, 2}
        existential = quantify_exists(root, eliminated)
        bad = engine.app(0, carrier, engine.neg(root))
        universal = engine.app(
            0, projection_carriers[side],
            engine.neg(quantify_exists(bad, eliminated)))
        return existential == universal

    # Authoritative total carrier and special-event checks guard the global
    # lift and the deterministic selector transport.
    carrier_count = count_from(carrier, 0)
    assert carrier_count == 211897540016
    assert count_from(S, 0) == 3 and le(T, R)

    forced_sources = {
        ("T", "left", 13848),
        ("T", "right", 15250),
        ("T", "right", 16786),
        ("Tc", "left", 1154),
        ("Tc", "right", 109),
    }

    bridge_rows = []
    seen_roots = {}

    def add_bridge(base_name, source_kind, source_name, source_root,
                   side=None, old_index=None):
        base = specials[base_name]
        assert disjoint(base, source_root)
        union = engine.app(1, base, source_root)
        target_name = "Tc" if base_name == "T" else "T"
        difference = engine.app(0, specials[target_name],
                                engine.neg(source_root))
        assert difference == engine.app(0, carrier, engine.neg(union))
        for operation, root in (("disjoint_union", union),
                                ("complementary_difference", difference)):
            exact_hash = structural_hash(root).hex()
            class_id = seen_roots.setdefault(root, len(seen_roots))
            row = {
                "exact_event_class": class_id,
                "exact_mdd_sha256": exact_hash,
                "operation": operation,
                "base": base_name if operation == "disjoint_union" else target_name,
                "source_kind": source_kind,
                "source_name": source_name,
                "source_side": side,
                "source_old_index": old_index,
                "physical_cardinality": count_from(root, 0),
                "singleton_hazard": count_from(root, 0) == 1,
                "activation_supported_coordinates": [
                    variable for variable, activation in
                    enumerate(activation_cylinders) if le(root, activation)
                ],
                "left_cylindrical": cylindrical(root, "left"),
                "right_cylindrical": cylindrical(root, "right"),
                "contained_in_T": le(root, T),
                "contained_in_Tc": le(root, Tc),
                "contained_in_R": le(root, R),
                "contains_T": le(T, root),
                "contains_Tc": le(Tc, root),
                "contains_R": le(R, root),
                "contained_in_source_parent": le(root, source_root),
                "contains_source_parent": le(source_root, root),
                "is_one_of_five_forced_differences": (
                    operation == "complementary_difference" and
                    source_kind == "old_cylinder" and
                    (target_name, side, old_index) in forced_sources),
                "source_in_frozen_five_parent_pool": (
                    source_kind == "old_cylinder" and
                    any(side == s and old_index == i
                        for _, s, i in forced_sources)),
            }
            row["activation_supported"] = bool(
                row["activation_supported_coordinates"])
            bridge_rows.append(row)

    # X is disjoint from the old cylinders listed under X.  Each union and its
    # complement difference are literal closure consequences.
    for side in ("left", "right"):
        for base_name in ("T", "Tc"):
            for index in disjoint_old[side][base_name]:
                root = engine.app(0, carrier, lift(index, side))
                assert disjoint(specials[base_name], root)
                add_bridge(base_name, "old_cylinder",
                           f"cyl_{side}({index})", root, side, index)

    # Special-special bridges are kept separately because S is a genuine
    # three-point physical event, not a cylinder or a shadow signature.
    special_disjoint_pairs = []
    for base_name in ("T", "Tc"):
        for source_name in ("R", "Rc", "S", "Sc"):
            if disjoint(specials[base_name], specials[source_name]):
                special_disjoint_pairs.append([base_name, source_name])
                add_bridge(base_name, "special", source_name,
                           specials[source_name])

    # Behavioural transition types retain exact physical class and provenance.
    descriptor_fields = (
        "operation", "base", "source_kind", "source_side",
        "left_cylindrical", "right_cylindrical", "contained_in_T",
        "contained_in_Tc", "contained_in_R", "contains_T", "contains_Tc",
        "contains_R", "contained_in_source_parent", "contains_source_parent",
        "is_one_of_five_forced_differences",
        "source_in_frozen_five_parent_pool", "singleton_hazard",
        "activation_supported",
    )
    types = {}
    for row in bridge_rows:
        key = tuple(row[field] for field in descriptor_fields)
        types.setdefault(key, []).append(row)
    transition_types = []
    for type_id, (key, rows) in enumerate(sorted(
            types.items(), key=lambda item: repr(item[0]))):
        transition_types.append({
            "transition_type": type_id,
            "descriptor": dict(zip(descriptor_fields, key)),
            "occurrence_count": len(rows),
            "exact_event_class_count": len({r["exact_event_class"] for r in rows}),
            "source_old_indices": sorted({r["source_old_index"] for r in rows
                                          if r["source_old_index"] is not None}),
            "exact_mdd_sha256s": sorted({r["exact_mdd_sha256"] for r in rows}),
        })

    exact_classes = []
    for root, class_id in sorted(seen_roots.items(), key=lambda item: item[1]):
        rows = [row for row in bridge_rows
                if row["exact_event_class"] == class_id]
        special_equalities = [name for name, value in specials.items()
                              if value == root]
        old_rows = [row for row in rows if row["source_kind"] == "old_cylinder"]
        new = not special_equalities
        exact_classes.append({
            "exact_event_class": class_id,
            "exact_mdd_sha256": structural_hash(root).hex(),
            "occurrence_count": len(rows),
            "equals_specials": special_equalities,
            "new_relative_to_specials": new,
            "has_frozen_parent_representation": any(
                row["source_in_frozen_five_parent_pool"] for row in old_rows),
            "requires_outside_frozen_parent_among_literal_representations": (
                new and bool(old_rows) and not any(
                    row["source_in_frozen_five_parent_pool"] for row in old_rows)
            ),
            "source_old_indices": sorted({row["source_old_index"]
                                          for row in old_rows}),
            "activation_supported_coordinates": sorted({
                variable for row in rows
                for variable in row["activation_supported_coordinates"]
            }),
        })

    source = json.loads(SOURCE_RECEIPT.read_text())
    out = {
        "schema": "arr-forced-T-literal-bridge-census-v1",
        "schema_version": "1.0",
        "source_forced_interval_payload_sha256": source["payload_sha256"],
        "actual_adjacent_carrier_points": carrier_count,
        "actual_adjacent_mdd_node_count": len(engine.nodes),
        "old_disjoint_cylinder_counts": {
            side: {target: len(indices) for target, indices in family.items()}
            for side, family in disjoint_old.items()
        },
        "special_disjoint_pairs": special_disjoint_pairs,
        "literal_bridge_occurrence_count": len(bridge_rows),
        "exact_literal_bridge_event_count": len(seen_roots),
        "transition_type_count": len(transition_types),
        "transition_types": transition_types,
        "exact_event_classes": exact_classes,
        "bridges": bridge_rows,
        "five_forced_difference_hits": sum(
            row["is_one_of_five_forced_differences"] for row in bridge_rows),
        "outside_frozen_parent_occurrence_count": sum(
            row["source_kind"] == "old_cylinder" and
            not row["source_in_frozen_five_parent_pool"]
            for row in bridge_rows),
        "new_exact_events_requiring_outside_frozen_parent_count": sum(
            row["requires_outside_frozen_parent_among_literal_representations"]
            for row in exact_classes),
        "singleton_hazard_count": sum(row["singleton_hazard"]
                                      for row in bridge_rows),
        "activation_supported_bridge_count": sum(
            bool(row["activation_supported_coordinates"])
            for row in bridge_rows),
        "scope": (
            "Exact actual-event census of every old cylinder in either full "
            "18,676-event copy disjoint from T or T^c, plus R,R^c,S,S^c when "
            "disjoint. It classifies only the immediate literal disjoint unions "
            "and complementary differences. It computes no bridge old kernel, "
            "does not close the mixed family, and proves no later-round, lattice, "
            "OML, centre, state, sigma, ODBC, MBRC, or Phi claim."
        ),
        "evidence_class": "Executable verified — exhaustive finite scope",
        "verification_independence": (
            "One deterministic physical seven-coordinate MDD implementation, "
            "reusing the authoritative old-event MDD bank and relation truth table."
        ),
        "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "command": (
            "PYTHONHASHSEED=0 python3 notes/open_questions/verification/"
            "arr_forced_T_literal_bridge_census.py --verify"
        ),
    }
    out["payload_sha256"] = digest(out)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit", action="store_true")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    out = payload()
    if args.emit:
        RECEIPT.write_text(json.dumps(out, sort_keys=True, indent=2) + "\n")
    if args.verify or not args.emit:
        assert json.loads(RECEIPT.read_text()) == out
    print(json.dumps({
        "status": "PASS",
        "payload_sha256": out["payload_sha256"],
        "bridges": out["literal_bridge_occurrence_count"],
        "exact_events": out["exact_literal_bridge_event_count"],
        "types": out["transition_type_count"],
        "forced_hits": out["five_forced_difference_hits"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
