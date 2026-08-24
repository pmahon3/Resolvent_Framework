#!/usr/bin/env python3
"""Verify manifest coverage and aggregate 32 exhaustive shard receipts."""
import argparse,hashlib,json,os
HERE=os.path.dirname(os.path.abspath(__file__));N=32
SCHEMA='adjacent-full-cycle-exhaustive-first-round-master-v2'
def shard_math_hash(d):
 x=dict(d);x.pop('mathematical_payload_sha256',None);x.pop('operational_measurements',None)
 return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def payload():
 manifest=json.load(open(os.path.join(HERE,'adjacent_full_cycle_exhaustive_manifest.json')))
 ds=[json.load(open(os.path.join(HERE,f'adjacent_full_cycle_exhaustive_shard_{i:02d}.json'))) for i in range(N)]
 mx=dict(manifest);mh=mx.pop('payload_sha256')
 assert mh==hashlib.sha256(json.dumps(mx,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 assert manifest['producer_sha256']==hashlib.sha256(open(os.path.join(HERE,'adjacent_full_cycle_exhaustive_manifest.py'),'rb').read()).hexdigest()
 assert all(d['mathematical_payload_sha256']==shard_math_hash(d) for d in ds)
 assert [d['shard_index'] for d in ds]==list(range(N))
 assert all(d['shard_count']==N and d['manifest_payload_sha256']==manifest['payload_sha256'] for d in ds)
 assert len({d['embedded_engine_source_sha256'] for d in ds})==1
 assert len({d['transformed_engine_source_sha256'] for d in ds})==1
 assert len({d['base_full_cycle_payload_sha256'] for d in ds})==1
 assert len({d['producer_sha256'] for d in ds})==1
 assert next(iter({d['producer_sha256'] for d in ds}))==hashlib.sha256(open(os.path.join(HERE,'adjacent_full_cycle_exhaustive_shard.py'),'rb').read()).hexdigest()
 assert next(iter({d['embedded_engine_source_sha256'] for d in ds}))==manifest['audited_engine_source_sha256']
 orient={}
 for mo in manifest['orientations']:
  name=mo['orientation'];seen=[];kernels=0
  for sh,d in enumerate(ds):
   r=next(x for x in d['orientation_records'] if x['orientation']==name)
   expected=mo['shards'][sh];assert r['selected_event_indices']==expected['retained_event_indices']
   assert r['selected_event_indices_sha256']==expected['event_list_sha256']
   assert r['sample_nonempty_admissible_kernels']==expected['nonempty_kernel_count']
   seen.extend(r['selected_event_indices']);kernels+=r['sample_nonempty_admissible_kernels']
  assert len(seen)==len(set(seen))==4719 and set(seen)==set(mo['complete_ranked_event_indices'])
  assert kernels==mo['nonempty_kernel_count']
  orient[name]={'retained_events':4719,'nonempty_kernels':kernels,
   'coverage_event_set_sha256':hashlib.sha256(','.join(map(str,sorted(seen))).encode()).hexdigest()}
 assert sum(x['nonempty_kernels'] for x in orient.values())==18370
 assert orient['left_retained_position11']['nonempty_kernels']==9347
 assert orient['right_retained_position00']['nonempty_kernels']==9023
 failures=sum(d['failures'] for d in ds);certs=[c for d in ds for c in d['failure_certificates']]
 assert len(certs)==failures
 out={'schema':SCHEMA,'schema_version':'2.0','manifest_payload_sha256':manifest['payload_sha256'],
  'shard_count':N,'orientation_coverage':orient,'u_empty_tautological_kernels':37352,
  'exhaustive_nonempty_kernels':18370,'total_first_round_kernels':55722,
  'failures':failures,'failure_certificates':certs,
  'shard_mathematical_payload_sha256':[d['mathematical_payload_sha256'] for d in ds],
  'chained_bad_mask_digest_sha256':hashlib.sha256(''.join(d['bad_mask_digest_sha256'] for d in ds).encode()).hexdigest(),
  'aggregate_counters':{k:sum(d[k] for d in ds) for k in (
   'bad_event_pair_queries','raw_short_circuit_occurrence_comparisons',
   'whole_state_class_pair_lookups','sum_per_a_distinct_class_pairs')},
  'coverage_proof':'The canonical 4719-event ranking in each orientation is partitioned by rank modulo 32; receipts exactly equal each manifest list, are disjoint, and cover both complete rankings. Kernel totals equal 18370 nonempty plus 37352 empty-U.',
  'conclusion':('All exact first-round kernels possess greatest old lowers.' if not failures else 'Exact first-round escapes exist; see certificates.'),
  'scope_not_covered':'Second-round mixed closure, latticehood, OML, sigma closure, MBRC, ODBC, Phi.',
  'evidence_classes':['Hand proved','Executable verified'],
  'command':'python3 notes/open_questions/verification/aggregate_adjacent_full_cycle_exhaustive_shards.py --verify',
  'producer_sha256':hashlib.sha256(open(__file__,'rb').read()).hexdigest()}
 out['payload_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 return out
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--emit',action='store_true');ap.add_argument('--verify',action='store_true');a=ap.parse_args()
 out=payload();path=os.path.join(HERE,'adjacent_full_cycle_exhaustive_first_round_master.json')
 if a.emit:
  with open(path,'w') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
 else:assert json.load(open(path))==out
 print(json.dumps({'status':'PASS','kernels':18370,'failures':out['failures'],'payload_sha256':out['payload_sha256']},sort_keys=True))
