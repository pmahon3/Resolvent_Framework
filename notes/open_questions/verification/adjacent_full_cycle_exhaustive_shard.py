#!/usr/bin/env python3
"""Execute one canonical rank-mod-32 exhaustive first-round shard."""
import argparse,hashlib,json,os,signal,time
HERE=os.path.dirname(os.path.abspath(__file__))
ENGINE=os.path.join(HERE,'adjacent_full_cycle_join_rich_per_a.py')
MANIFEST=os.path.join(HERE,'adjacent_full_cycle_exhaustive_manifest.json')
SCHEMA='adjacent-full-cycle-exhaustive-first-round-shard-v2';N=32
SLICE_OLD="return tuple(x[3] for x in ranked[:SAMPLE]),ranked"
SLICE_NEW=("expected=MANIFEST_LEFT if fams is left_us else MANIFEST_RIGHT\n"
 "  assert [x[3] for x in ranked]==MANIFEST_FULL_LEFT if fams is left_us else [x[3] for x in ranked]==MANIFEST_FULL_RIGHT\n"
 "  return tuple(expected),ranked")
INIT_OLD="digest=hashlib.sha256();records=[];global_raw=global_lookups=global_distinct=global_bad=0"
INIT_NEW=INIT_OLD+";failure_certs=[]"
FAIL_OLD="if Q&~us[ui]:failures+=1"
FAIL_NEW=("if Q&~us[ui]:\n"
 "       failures+=1\n"
 "       opp=next(i for i,(EO,UO) in enumerate(op_classes) if UO==us[ui] and not classes[A][0]&EO)\n"
 "       assert not bad(P)&~us[ui] and not ba&~us[ui] and not (principal[a]>>P&1) and J==upmap[principal[P]&principal[a]]\n"
 "       failure_certs.append({'orientation':name,'retained_event_index':A,'retained_existential_mask_hex':hex(classes[A][0]),'opposite_witness_event_index':opp,'opposite_existential_mask_hex':hex(op_classes[opp][0]),'universal_mask_hex':hex(us[ui]),'prior_accumulator_event_index':P,'prior_bad_mask_hex':hex(bad(P)),'new_atom_event_index':a,'atom_bad_mask_hex':hex(ba),'escaping_join_event_index':J,'escaping_bad_mask_hex':hex(Q),'escaping_outside_U_hex':hex(Q&~us[ui])})")
SIG_OLD="def orientation(name,pos,classes,fams):"
SIG_NEW="def orientation(name,pos,classes,fams,op_classes):"
CALL_L_OLD="orientation('left_retained_position11',3,left,left_us)"
CALL_L_NEW="orientation('left_retained_position11',3,left,left_us,right)"
CALL_R_OLD="orientation('right_retained_position00',0,right,right_us)"
CALL_R_NEW="orientation('right_retained_position00',0,right,right_us,left)"
OUT_OLD="'sample_failures':sum(r['sample_failures'] for r in records),"
OUT_NEW=OUT_OLD+"'failure_certificates':failure_certs,"
def math_hash(d):
 x=dict(d);x.pop('mathematical_payload_sha256',None);x.pop('operational_measurements',None)
 return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def payload(shard,pilot_limit=None):
 manifest=json.load(open(MANIFEST));assert manifest['shard_count']==N
 om={x['orientation']:x for x in manifest['orientations']}
 L=next(x for x in om['left_retained_position11']['shards'] if x['shard_index']==shard)
 R=next(x for x in om['right_retained_position00']['shards'] if x['shard_index']==shard)
 left_selected=L['retained_event_indices'] if pilot_limit is None else L['retained_event_indices'][:pilot_limit]
 right_selected=R['retained_event_indices'] if pilot_limit is None else R['retained_event_indices'][:pilot_limit]
 src=open(ENGINE).read()
 for old in (SLICE_OLD,INIT_OLD,FAIL_OLD,OUT_OLD,SIG_OLD,CALL_L_OLD,CALL_R_OLD):assert src.count(old)==1
 transformed=(src.replace(SLICE_OLD,SLICE_NEW).replace(INIT_OLD,INIT_NEW)
  .replace(FAIL_OLD,FAIL_NEW).replace(OUT_OLD,OUT_NEW).replace(SIG_OLD,SIG_NEW)
  .replace(CALL_L_OLD,CALL_L_NEW).replace(CALL_R_OLD,CALL_R_NEW))
 ns={'__file__':ENGINE,'__name__':'embedded_exhaustive_engine',
  'MANIFEST_LEFT':left_selected,'MANIFEST_RIGHT':right_selected,
  'MANIFEST_FULL_LEFT':om['left_retained_position11']['complete_ranked_event_indices'],
  'MANIFEST_FULL_RIGHT':om['right_retained_position00']['complete_ranked_event_indices']}
 exec(compile(transformed,ENGINE,'exec'),ns);inner,seconds,peak=ns['payload']()
 if pilot_limit is None:assert inner['sample_nonempty_kernels']==L['nonempty_kernel_count']+R['nonempty_kernel_count']
 out={'schema':SCHEMA,'schema_version':'2.0','shard_index':shard,'shard_count':N,
  'manifest_payload_sha256':manifest['payload_sha256'],
  'manifest_source_sha256':manifest['producer_sha256'],
  'embedded_engine_source_sha256':hashlib.sha256(open(ENGINE,'rb').read()).hexdigest(),
  'transformed_engine_source_sha256':hashlib.sha256(transformed.encode()).hexdigest(),
  'base_full_cycle_payload_sha256':inner['base_full_cycle_payload_sha256'],
  'orientation_records':inner['orientation_records'],
  'expected_orientation_manifest':{'left':L,'right':R},
  'diagnostic_pilot_limit_per_orientation':pilot_limit,
  'nonempty_kernels':inner['sample_nonempty_kernels'],'failures':inner['sample_failures'],
  'failure_certificates':inner['failure_certificates'],
  'bad_event_pair_queries':inner['bad_event_pair_queries'],
  'raw_short_circuit_occurrence_comparisons':inner['raw_short_circuit_occurrence_comparisons'],
  'whole_state_class_pair_lookups':inner['whole_state_class_pair_lookups'],
  'sum_per_a_distinct_class_pairs':inner['sum_per_a_distinct_class_pairs'],
  'bad_mask_digest_sha256':inner['bad_mask_digest_sha256'],
  'mdd_snapshot_before':inner['mdd_snapshot_before'],'mdd_snapshot_after':inner['mdd_snapshot_after'],
  'u_empty_discharge':inner['u_empty_discharge'],
  'coverage_scope':(('Every nonempty admissible U for both complete orientation event lists assigned by this manifest shard.')
   if pilot_limit is None else f'Diagnostic prefix only: first {pilot_limit} manifest-assigned retained events in each orientation; not exhaustive for this shard.'),
  'scope_not_covered':'Other shards; second-round closure, latticehood, OML, sigma closure, MBRC, ODBC, Phi.',
  'verification_independence':inner['verification_independence'],
  'hash_seed_policy':'Mathematical payload excludes operational runtime/RSS and must reproduce under PYTHONHASHSEED=12345 for the pilot and selected audit shards.',
  'evidence_classes':['Hand proved','Executable verified'],
  'command':(f'python3 notes/open_questions/verification/adjacent_full_cycle_exhaustive_shard.py --verify --shard {shard}'
   +('' if pilot_limit is None else f' --pilot-limit {pilot_limit}')),
  'producer_sha256':hashlib.sha256(open(__file__,'rb').read()).hexdigest()}
 out['mathematical_payload_sha256']=math_hash(out)
 return out,seconds,peak
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--emit',action='store_true');ap.add_argument('--verify',action='store_true');ap.add_argument('--shard',type=int,required=True);ap.add_argument('--pilot-limit',type=int);a=ap.parse_args()
 if not 0<=a.shard<N:ap.error('shard must be 0..31')
 def timeout(_s,_f):raise TimeoutError('exhaustive shard exceeded 720 seconds')
 prior=signal.getsignal(signal.SIGALRM);signal.signal(signal.SIGALRM,timeout);signal.alarm(720)
 try:out,seconds,peak=payload(a.shard,a.pilot_limit)
 finally:signal.alarm(0);signal.signal(signal.SIGALRM,prior)
 path=os.path.join(HERE,(f'adjacent_full_cycle_exhaustive_shard_{a.shard:02d}.json' if a.pilot_limit is None else f'adjacent_full_cycle_exhaustive_pilot_{a.shard:02d}_{a.pilot_limit}.json'))
 if a.emit:
  out['operational_measurements']={'runtime_seconds':round(seconds,6),'peak_rss_platform_units':peak,
   'pythonhashseed':os.environ.get('PYTHONHASHSEED','default')}
  with open(path,'w') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
 else:
  stored=json.load(open(path));assert stored['mathematical_payload_sha256']==math_hash(stored)
  x=dict(stored);x.pop('operational_measurements',None);assert x==out
 print(json.dumps({'status':'PASS','shard':a.shard,'kernels':out['nonempty_kernels'],
  'failures':out['failures'],'mathematical_payload_sha256':out['mathematical_payload_sha256'],
  'runtime_seconds':round(seconds,3),'peak_rss_console_only':peak},sort_keys=True))
