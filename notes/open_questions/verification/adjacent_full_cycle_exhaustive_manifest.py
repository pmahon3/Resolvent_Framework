#!/usr/bin/env python3
"""Canonical manifest for the exhaustive adjacent first-round kernel scan."""
import argparse,collections,hashlib,json,os,sys,time
HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import full_cycle_adjacent_rectangle_intersection as inter
SCHEMA='adjacent-full-cycle-exhaustive-first-round-manifest-v1';SHARDS=32
def payload():
 base,b=inter.capture_grammar();events=b['all_events'];macros=b['macros'];engines=b['engines']
 states=b['states'];roots={ev:r for r,ev in b['root_to_event'].items()};principal=b['principal']
 n=len(events);N=len(states);assert (n,N)==(18676,224)
 upmap={u:i for i,u in enumerate(principal)};allold=(1<<n)-1;zero=upmap[allold];nonatomic=0
 for d,u in enumerate(principal):
  if d!=zero:nonatomic|=u&~(1<<d)
 bits=allold&~nonatomic&~(1<<zero);atoms=[]
 while bits:z=bits&-bits;atoms.append(z.bit_length()-1);bits-=z
 assert len(atoms)==91
 occ=[[[] for _ in range(N)] for _ in range(4)]
 for m,(_,ds) in enumerate(macros):
  for pos in range(4):
   for i,s in enumerate(ds[pos]):occ[pos][s].append((m,i))
 cache={}
 def status(m,r,pos,i):
  k=(m,r,pos,i)
  if k in cache:return cache[k]
  if r<=1:z=r
  else:
   v,ch=engines[m].nodes[r]
   if v==pos:z=status(m,ch[i],pos,i)
   else:q={status(m,x,pos,i) for x in ch};z=q.pop() if len(q)==1 else 2
  cache[k]=z;return z
 def classify(pos):
  out=[]
  for ev in events:
   E=U=0;rr=roots[ev]
   for s,os in enumerate(occ[pos]):
    vals=[status(m,rr[m],pos,i) for m,i in os]
    if any(vals):E|=1<<s
    if all(x==1 for x in vals):U|=1<<s
   out.append((E,U))
  return out
 left=classify(3);right=classify(0)
 def minima(cs):
  g=collections.defaultdict(list)
  for i,(E,U) in enumerate(cs):g[U].append((E,i))
  out={}
  for U,xs in g.items():
   keep=[]
   for E,i in sorted(xs,key=lambda x:(x[0].bit_count(),x[0],x[1])):
    if not any(not K&~E for K,_ in keep):keep.append((E,i))
   out[U]=tuple(keep)
  return out
 def admissible(cs,op):
  return [tuple(sorted((U for U,xs in op.items() if any(not EA&E for E,_ in xs)),
   key=lambda u:(u.bit_count(),u))) for EA,_ in cs]
 lu=admissible(left,minima(right));ru=admissible(right,minima(left))
 assert (sum(map(len,lu)),sum(map(len,ru)))==(28023,27699)
 jt={}
 def joins(A):
  if A not in jt:jt[A]=len({upmap[principal[A]&principal[a]] for a in atoms if not (principal[a]>>A&1)})
  return jt[A]
 def ranked(fams):
  xs=[]
  for A,us0 in enumerate(fams):
   us=[u for u in us0 if u]
   if us:
    j=joins(A);xs.append((-(len(us)*j),-j,-len(us),A,len(us)))
  xs.sort();return xs
 orientations=[]
 for name,fams in (('left_retained_position11',lu),('right_retained_position00',ru)):
  xs=ranked(fams);assert len(xs)==4719
  full=[x[3] for x in xs];shards=[]
  for sh in range(SHARDS):
   selected=[x for rank,x in enumerate(xs) if rank%SHARDS==sh]
   evs=[x[3] for x in selected]
   shards.append({'shard_index':sh,'rank_residue_mod_32':sh,'retained_event_indices':evs,
    'retained_event_count':len(evs),'nonempty_kernel_count':sum(x[4] for x in selected),
    'event_list_sha256':hashlib.sha256(','.join(map(str,evs)).encode()).hexdigest()})
  assert len({e for s in shards for e in s['retained_event_indices']})==4719
  orientations.append({'orientation':name,'ranked_retained_event_count':4719,
   'nonempty_kernel_count':sum(x[4] for x in xs),
   'complete_ranked_event_indices':full,
   'complete_ranking_sha256':hashlib.sha256(','.join(map(str,full)).encode()).hexdigest(),
   'shards':shards})
 assert sum(x['nonempty_kernel_count'] for x in orientations)==18370
 out={'schema':SCHEMA,'schema_version':'1.0','shard_count':SHARDS,
  'base_full_cycle_payload_sha256':base['payload_sha256'],'completed_events_each':n,
  'audited_engine_source_sha256':hashlib.sha256(open(os.path.join(HERE,'adjacent_full_cycle_join_rich_per_a.py'),'rb').read()).hexdigest(),
  'shard_transformation_contract':'Replace only the top-SAMPLE selection return by exact manifest lists; add exhaustive failure-certificate accumulation and export. Shard runner records original and transformed source hashes.',
  'old_atom_count':len(atoms),'complete_kernel_counts':{'all':55722,'u_empty_tautological':37352,'nonempty':18370},
  'selection_rule':'Canonical join-rich ranking, partitioned by zero-based rank modulo 32.',
  'orientation_nonempty_kernel_totals':{'left':9347,'right':9023},
  'orientations':orientations,
  'coverage_proof':'Each orientation has exactly 4719 ranked retained events with nonempty U; rank residues modulo 32 are disjoint and exhaustive; manifest kernel totals sum to 18370.',
  'command':'python3 notes/open_questions/verification/adjacent_full_cycle_exhaustive_manifest.py --verify',
  'evidence_classes':['Hand proved','Executable verified']}
 out['producer_sha256']=hashlib.sha256(open(__file__,'rb').read()).hexdigest()
 out['payload_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 return out
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--emit',action='store_true');ap.add_argument('--verify',action='store_true');a=ap.parse_args()
 out=payload();path=os.path.join(HERE,'adjacent_full_cycle_exhaustive_manifest.json')
 if a.emit:
  with open(path,'w') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
 else:assert json.load(open(path))==out
 print(json.dumps({'status':'PASS','payload_sha256':out['payload_sha256'],'nonempty_kernels':18370},sort_keys=True))
