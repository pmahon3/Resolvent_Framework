#!/usr/bin/env python3
"""Bounded third-round phantom-bridge classifier.

This instruments the deterministic second-round coordinate-child producer
without changing its sample or depth.  For every failing disjoint-union child
it tests each bridge atom independently over the base old join, records every
single-atom escape and its landing, and forms the physical atom saturation
`e0` from all old atoms contained in the target.

The result concerns only the bounded coordinate-target family of the source
receipt.  It does not inspect or depend on exhaustive shard artifacts.
"""
import argparse,hashlib,json,os

HERE=os.path.dirname(os.path.abspath(__file__))
SOURCE=os.path.join(HERE,'adjacent_full_cycle_second_round_coordinate_children.py')
SCHEMA='adjacent-full-cycle-third-round-phantom-bridge-v1'

def payload():
 src=open(SOURCE).read()
 needle="records=[];first_failure=None;shadow_bridges=collections.defaultdict(dict)"
 assert src.count(needle)==1
 src=src.replace(needle,needle+";third_round_failures=[]")
 needle2="fullk,_,good=kernel(union);ok=good and j==fullk and subset(roots[events[j]],union)"
 assert src.count(needle2)==1
 inject="""fullk,eligible_all,good=kernel(union);ok=good and j==fullk and subset(roots[events[j]],union)
    if not ok:
     singles=[]
     for aa in bridges:
      landing=old_join(basej,aa);esc=not subset(roots[events[landing]],union)
      singles.append({'atom':old_record(aa),'full17_phantom':events[aa][1]==0,
       'landing':old_record(landing),'landing_is_top':landing==comp[zero],
       'single_atom_escapes':esc})
     e0=tuple(0 for _ in macros)
     for aa in eligible_all:e0=op(1,e0,roots[events[aa]])
     third_round_failures.append({'orientation':name,'left':rhash(x['root']),
      'right':rhash(y['root']),'target':rhash(union),'base_join':old_record(basej),
      'bridge_atoms':list(bridge_records),'single_atom_tests':singles,
      'single_atom_escape_count':sum(z['single_atom_escapes'] for z in singles),
      'all_single_escapes_land_top':all((not z['single_atom_escapes']) or z['landing_is_top'] for z in singles),
      'all_escaping_atoms_full17_phantom':all((not z['single_atom_escapes']) or z['full17_phantom'] for z in singles),
      'atom_saturation_e0_sha256':rhash(e0),'e0_subset_target':subset(e0,union),
      'e0_strictly_below_target':subset(e0,union) and e0!=union,
      'e0_old_fold':old_record(fullk),'e0_old_fold_inside_target':good})"""
 src=src.replace(needle2,inject)
 needle3="out={'schema':SCHEMA,'schema_version':'1.0',"
 assert src.count(needle3)==1
 src=src.replace(needle3,"out={'third_round_internal':third_round_failures,'schema':SCHEMA,'schema_version':'1.0',")
 ns={'__file__':SOURCE,'__name__':'_third_round_instrumented'}
 exec(compile(src,SOURCE,'exec'),ns)
 base,_=ns['payload']();failures=base.pop('third_round_internal')
 source_receipt=json.load(open(os.path.join(HERE,
  'adjacent_full_cycle_second_round_coordinate_children.json')))
 assert len(failures)==12,len(failures)
 allsing=[z for f in failures for z in f['single_atom_tests'] if z['single_atom_escapes']]
 out={'schema':SCHEMA,'schema_version':'1.0',
  'source_second_round_payload_sha256':source_receipt['payload_sha256'],
  'source_second_round_producer_sha256':source_receipt['producer_sha256'],
  'bounded_strict_union_failures':len(failures),
  'orientation_failure_counts':{o:sum(f['orientation']==o for f in failures)
    for o in sorted({f['orientation'] for f in failures})},
  'failure_records':failures,
  'single_bridge_atom_tests':sum(len(f['single_atom_tests']) for f in failures),
  'single_atom_escapes':len(allsing),
  'all_single_escapes_land_top':all(z['landing_is_top'] for z in allsing),
  'all_escaping_atoms_full17_phantom':all(z['full17_phantom'] for z in allsing),
  'all_failure_atom_saturations_strictly_below_target':
    all(f['e0_strictly_below_target'] for f in failures),
  'all_failure_atom_saturations_kernel_bad':
    all(not f['e0_old_fold_inside_target'] for f in failures),
  'H1':('Each bridge atom of every bounded failure is joined singly to the fixed base join; '
    'the canonical first failure is included among these records.'),
  'H2':('All 12 strict failures in the bounded source census are classified independently '
    'of bridge order by their single-atom landing and full17 phantom status.'),
  'H3':('For each failed target, e0 is the physical union of all contained old atoms; '
    'strict containment and escape of their old-lattice fold are checked separately.'),
  'scope':('Exact bounded replay of the coordinate-target child family from the source '
    'second-round producer only. No exhaustive first-round, full mixed-event closure, '
    'lattice, OML, direct-limit, MBRC, ODBC, or Phi claim.'),
  'verification_independence':('Single instrumented producer sharing the source MDD grammar '
    'and sample. Canonical whole-payload replay is required under seeds 0 and 12345.'),
  'evidence_classes':['Executable verified bounded evidence'],
  'command':'PYTHONHASHSEED=0 python3 notes/open_questions/verification/adjacent_full_cycle_third_round_phantom_bridge.py --verify'}
 out['producer_sha256']=hashlib.sha256(open(__file__,'rb').read()).hexdigest()
 out['payload_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 return out

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--emit',action='store_true');ap.add_argument('--verify',action='store_true');a=ap.parse_args()
 out=payload();path=os.path.join(HERE,'adjacent_full_cycle_third_round_phantom_bridge.json')
 if a.emit:
  with open(path,'w') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
 else:assert json.load(open(path))==json.loads(json.dumps(out,sort_keys=True))
 print(json.dumps({'status':'PASS','payload_sha256':out['payload_sha256'],
  'failures':out['bounded_strict_union_failures'],'single_escapes':out['single_atom_escapes']},sort_keys=True))
