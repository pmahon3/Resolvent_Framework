#!/usr/bin/env python3
"""Patch oml_lattice_taxonomy.json with s33 results. Idempotent-ish:
removes any prior s33 entries by id before adding. Run with the 2-port
verdict string as argv[1] (e.g. 'no-go within design class (0 survivors)').
"""
import json
import sys

P = '/Users/pmahon/Research/Mathematics/Resolvent_Framework/notes/open_questions/oml_attack/oml_lattice_taxonomy.json'
twoport = sys.argv[1] if len(sys.argv) > 1 else 'PENDING'

d = json.load(open(P))
cc = d['counterexample_construction']

new_ids = {'oml.construct.k3plus_two_cell', 'oml.construct.three_cell_relay',
           'oml.construct.removable_face'}
cc = [e for e in cc if e['id'] not in new_ids]

detail = 'oml_lattice_regularity_attack.md#27-next-finite-classes-k3-two-cell-exit-b-one-port-three-cell-unconditional-no-go-and-a-richer-removable-face-found-2026-07-11-session-33'

cc.append({
    'id': 'oml.construct.k3plus_two_cell',
    'name': 'Two-cell k>=3 identifications',
    'status': 'exit-b-screen-passed-witness-fails',
    'one_line': ('Two-cell route complete. k>=6 has no girth-valid map; '
                 'k=4,5 die at the screen (empty sigma-live set); k=3 gives '
                 'four screen-survivors with the ideal ten-state live set '
                 '(liveness lasso-confirmed) but all four die downstream: '
                 'two at global (periodic) girth, two at master-cycle girth.'),
    'detail': detail,
})
cc.append({
    'id': 'oml.construct.three_cell_relay',
    'name': 'Three-pentagon period-3 relays',
    'status': 'exit-b-one-port-unconditional',
    'one_line': ('One-port period-3 relays: unconditional no-go (full 10^6 '
                 'product, zero survivors at every phase). Two-port (10^9 '
                 'infeasible whole): ' + twoport + '. Two-port outside the '
                 's_*-preserving design class is not claimed closed.'),
    'detail': detail,
})
cc.append({
    'id': 'oml.construct.removable_face',
    'name': 'Richer removable face (Exit C precondition)',
    'status': 'precondition-established-operative-open',
    'one_line': ('The pentagon is the degenerate zero-slack case (only one '
                 'removable state, no |F|>=2 face). Larger girth-5 Greechie '
                 'OMLs have removable faces abundantly (6-loop 18, 7-loop '
                 '154, two-pentagons-sharing-one-atom 4825, |F| up to 10), '
                 'complement order-determining, each face state individually '
                 'dispensable. This is the LOCAL precondition only; whether a '
                 'richer face avoids the dynamic liveness/separation tradeoff '
                 'is open (relay unbuilt for these OMLs).'),
    'detail': detail,
})

d['counterexample_construction'] = cc

# meta updates
d['$meta']['updated'] = '2026-07-11'
d['$meta']['headline']['entries'] = 47 + 3
d['$meta']['headline']['current_next_step'] = (
    'Execute HANDOFF_2026-07-11_s33.md. s33 closed two-cell route (EXIT B, '
    'complete: k>=6 empty, k=4/5 die at screen, k=3 survivors die at '
    'girth/master geometry) and one-port three-cell relays (unconditional). '
    'Two-port three-cell scoped to design class. Priority: run the '
    'three-condition screen on a RICHER REMOVABLE FACE (found in the 7-loop / '
    'two-pentagons-sharing-one-atom) by generalizing the relay automaton to '
    'that OML and putting the whole face in s_*\'s role -- this is the live '
    'test of whether a richer face escapes the pentagon liveness/separation '
    'tradeoff. Complete the two-port three-cell design-class census.')

json.dump(d, open(P, 'w'), indent=1, ensure_ascii=False)
print('patched taxonomy; entries now', d['$meta']['headline']['entries'])
print('cc entries:', len(cc))

# also bump the registry row
R = '/Users/pmahon/Research/Mathematics/Resolvent_Framework/notes/taxonomies_index.json'
reg = json.load(open(R))
for coll in reg.get('collections', reg if isinstance(reg, list) else []):
    pass


def walk(o):
    if isinstance(o, dict):
        if o.get('id') == 'oml_lattice':
            o['entries'] = 50
            o['status'] = (o['status'].split(' Machine-checked')[0]
                           + ' s33 (2026-07-11): two-cell relay route COMPLETE '
                           '(EXIT B — k>=6 empty, k=4/5 die at screen, four k=3 '
                           'screen-survivors die at girth/master geometry) and '
                           'one-port three-cell relays UNCONDITIONAL no-go; a '
                           'richer removable FACE exists (7-loop / '
                           'two-pentagons-sharing-one-atom, |F|>=2, '
                           'order-determining complement) but its operative '
                           'liveness/separation test is unrun. Machine-checked '
                           '2026-07-11 s17–s18, ALL AXIOM-FREE:'
                           + o['status'].split('ALL AXIOM-FREE:')[1]
                           if 'ALL AXIOM-FREE:' in o['status'] else o['status'])
        for v in o.values():
            walk(v)
    elif isinstance(o, list):
        for v in o:
            walk(v)


walk(reg)
json.dump(reg, open(R, 'w'), indent=1, ensure_ascii=False)
print('bumped registry oml_lattice row to 50 entries + s33 status')
