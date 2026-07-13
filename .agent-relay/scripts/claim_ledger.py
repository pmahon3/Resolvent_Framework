from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


def _identifier(prefix: str, statement: str) -> str:
    return f"{prefix}-{hashlib.sha256(statement.encode('utf-8')).hexdigest()[:10].upper()}"


def _evidence_class(statement: str) -> str:
    lowered = statement.lower()
    if re.search(r"\blean\b", lowered) or "zero-sorry" in lowered: return "lean"
    if "hand-proof" in lowered or "hand proof" in lowered or "lemma" in lowered: return "hand_proof"
    if "executable" in lowered or "finite" in lowered or "python" in lowered: return "executable_or_finite"
    return "research_state"


def initial_ledger(*, accepted_commit: str) -> dict:
    banked = [
        "The amended orthomodular-poset form has a zero-sorry Lean certificate.",
        "The two-fibre atom-selector class is closed: jointly coherent pairs have disjoint propagation support, rectangular compatibility, and identity monodromy.",
        "Several finite relay and short-loop architectures have been classified or killed; these are finite/executable evidence unless separately hand-proved or formalized.",
        "Hand-proof lemma: in an OML, Boolean blocks containing the same compatible pair e,f generate the same embedded Boolean subalgebra from e,f.",
        "Executable finite result: in the fixed seven-block skeleton, O2 and O3 repeat one intrinsic four-region datum across their two common blocks; the associated duplicate-edge constraints reduce to one pullback.",
        "O2/O3 repeated-common-block candidates do not produce two inequivalent quotient edges merely from multiple blocks containing the same selector pair.",
        "Hand-proof lemma: if common embedded Boolean subalgebras jointly generate each of two Boolean blocks in an OML, then the blocks coincide.",
        "Finite executable result: the four-point P/Q versus P/R control has two inequivalent edge relations whose intersection is the permutation [0,1,3,2], while both overlap families jointly generate their endpoints.",
        "The minimal four-point jointly-generating distinct-event-family transverse square cannot realize two distinct maximal Boolean blocks; its canonical collapse is a wholly central 16-element Boolean algebra.",
    ]
    closed = [
        "Naive product-Ulam and atom-selector routes do not yield the required lattice witness.",
        "Direct finite repeater candidates fail one or more of latticehood, σ-completeness, global state extension, or σ-state order separation.",
    ]
    claims = {}
    for category, items in (("banked_result", banked), ("closed_architecture", closed)):
        for statement in items:
            identifier = _identifier("BANK" if category == "banked_result" else "CLOSED", statement)
            claims[identifier] = {
                "statement": statement, "category": category,
                "status": "accepted", "scope": "As stated; evidence classes remain distinct.",
                "evidence_class": _evidence_class(statement), "evidence": [],
                "supersedes": None, "introduced_by": accepted_commit,
                "last_reviewed_by": None,
            }
    return {
        "schema_version": 1,
        "original_conjecture": "Does a concrete σ-complete orthomodular lattice carry a σ-essential state? The current programme conjectures no; bounded or finite evidence must not be reported as resolving this question.",
        "claims": claims,
        "open_gate": "Resolve a transverse-overlap architecture whose inequivalent overlap families have proper joint Boolean closure in at least one endpoint, with mixed completion, latticehood, σ-completeness, maximal blocks, centre, state extension, and order separation checked independently.",
        "formalization_boundary": "The joint-generation collapse lemma is a hand proof and the four-point controls are finite executable evidence. Existing Lean files still do not certify the open OML conjecture or a general transverse-overlap classification.",
        "next_task": "Construct the smallest proper-joint-closure transverse candidate and audit its full mixed completion and structural gates.",
        "controlling_files": ["CLAUDE.md", "notes/taxonomies_index.json", "notes/programme/program_overview.md", "notes/programme/frontier_map.md", "notes/programme/shovel_plan.md", "notes/open_questions/oml_attack/oml_lattice_taxonomy.json", "notes/open_questions/oml_attack/oml_lattice_regularity_attack.md", "formalization/QuerySystem/"],
        "scope_qualifications": "Finite approximants, Python receipts, hand proofs, executable evidence, and Lean theorems are distinct evidence classes. No bounded census establishes an infinite classification. The centre, σ-completeness, latticehood, and maximal-block behavior remain explicit gates for proposed witnesses.",
        "accepted_commit": accepted_commit,
    }


def load_or_initialize(relay: Path, *, accepted_commit: str) -> dict:
    path = relay / "CLAIMS.json"
    return json.loads(path.read_text()) if path.exists() else initial_ledger(accepted_commit=accepted_commit)


def apply_review_patch(ledger: dict, review: dict, *, mathematical_tip: str, run_id: str) -> dict:
    patch = review["state_patch"]
    for category, prefix, key in (
        ("banked_result", "BANK", "banked_results_add"),
        ("closed_architecture", "CLOSED", "closed_architectures_add"),
    ):
        for statement in patch[key]:
            identifier = _identifier(prefix, statement)
            prior = ledger["claims"].get(identifier)
            ledger["claims"][identifier] = {
                "statement": statement, "category": category, "status": "accepted",
                "scope": "As stated in the accepted reviewer patch.",
                "evidence_class": _evidence_class(statement),
                "evidence": (prior or {}).get("evidence", []),
                "supersedes": (prior or {}).get("supersedes"),
                "introduced_by": (prior or {}).get("introduced_by", mathematical_tip),
                "last_reviewed_by": run_id,
            }
    ledger.update(open_gate=patch["open_gate"], formalization_boundary=patch["formalization_boundary"],
                  next_task=patch["next_task"], accepted_commit=mathematical_tip)
    return ledger


def render(ledger: dict) -> str:
    groups = {"banked_result": [], "closed_architecture": []}
    for identifier, claim in sorted(ledger["claims"].items()):
        if claim.get("status") == "accepted" and claim.get("category") in groups:
            groups[claim["category"]].append((identifier, claim))
    lines = ["# Compact theorem ledger", "", "<!-- Generated from CLAIMS.json; edit the ledger, not this file. -->", "",
             "## Original conjecture", "", ledger["original_conjecture"], "", "## Banked results", ""]
    lines.extend(f"- [{identifier}] {claim['statement']}" for identifier, claim in groups["banked_result"])
    lines += ["", "## Closed architectures", ""]
    lines.extend(f"- [{identifier}] {claim['statement']}" for identifier, claim in groups["closed_architecture"])
    lines += ["", "## Current open gate", "", ledger["open_gate"], "", "## Formalization boundary", "", ledger["formalization_boundary"],
              "", "## Controlling files", ""]
    lines.extend(f"- `{path}`" for path in ledger["controlling_files"])
    lines += ["", "## Most recent accepted mathematical commit", "", ledger["accepted_commit"],
              "", "## Unresolved scope qualifications", "", ledger["scope_qualifications"],
              "", "## Single best next strategic problem", "", ledger["next_task"], ""]
    return "\n".join(lines)
