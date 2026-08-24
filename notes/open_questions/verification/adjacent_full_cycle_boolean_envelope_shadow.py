#!/usr/bin/env python3
"""Boolean-envelope and coarse mixed-shadow checkpoint for adjacent full cycles.

The shadow retained here is only the three-valued empty/partial/full
classification over each shared state.  It forgets the section inside every
partial fibre and therefore cannot certify an actual local lower/upper shadow.
"""
import argparse,collections,hashlib,json,math,os,sys
HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import full_cycle_adjacent_rectangle_intersection as inter
SCHEMA='adjacent-full-cycle-boolean-envelope-shadow-v1'

def payload():
 base,b=inter.capture_grammar();events=b['all_events'];macros=b['macros'];engines=b['engines'];states=b['states']
 roots={ev:r for r,ev in b['root_to_event'].items()};N=len(states);ALL=(1<<N)-1
 # Exact envelope atoms: embedded cell events separate each of the four local
 # state coordinates, hence every carrier tuple is one Boolean-envelope atom.
 counts=[[0]*N for _ in range(4)]
 for _,ds in macros:
  sizes=list(map(len,ds));w=math.prod(sizes)
  for pos,d in enumerate(ds):
   z=w//sizes[pos]
   for s in d:counts[pos][s]+=z
 p,q=counts[3],counts[0]
 # Restrict one MDD root to a value of coordinate pos. Return 0 empty, 1 full,
 # 2 partial; cache makes the 18k x 842 scan a root-type computation.
 caches=[{} for _ in range(4)]
 def cls(m,root,pos,i):
  key=(m,root,pos,i);c=caches[pos]
  if key in c:return c[key]
  if root<=1:z=root
  else:
   v,ch=engines[m].nodes[root]
   if v==pos:z=cls(m,ch[i],pos,i)
   else:
    vals={cls(m,x,pos,i) for x in ch};z=vals.pop() if len(vals)==1 else 2
  c[key]=z;return z
 def shadows(pos):
  out={};prov={}
  for idx,e in enumerate(events):
   possible=[False]*N;universal=[True]*N;seen=[False]*N
   for m,(_,ds) in enumerate(macros):
    root=roots[e][m]
    for i,s in enumerate(ds[pos]):
     z=cls(m,root,pos,i);seen[s]=True;possible[s]|=z!=0;universal[s]&=z==1
   assert all(seen)
   E=sum(1<<s for s,v in enumerate(possible) if v);U=sum(1<<s for s,v in enumerate(universal) if v)
   out[(E,U)]=out.get((E,U),0)+1;prov.setdefault((E,U),idx)
  return out,prov
 L,LP=shadows(3);R,RP=shadows(0)
 # Complement coarse shadows must be present locally.  On the full fibre
 # product EA & EB == 0 is equivalent to physical disjointness of the two
 # pulled cylinders, not merely a sufficient test.
 complement_closed_L=all((ALL^U,ALL^E) in L for E,U in L);complement_closed_R=all((ALL^U,ALL^E) in R for E,U in R)
 missing=[];tested=0
 for A in L:
  EA,UA=A
  for B in R:
   EB,UB=B
   if EA&EB:continue
   tested+=1;shadow=(EA|EB,UA|UB)
   if shadow not in L and shadow not in R:
    missing.append((A,B,shadow));break
  if missing:break
 def h(x):return hashlib.sha256(x.to_bytes(28,'little')).hexdigest()
 witness=None
 if missing:
  A,B,C=missing[0];witness={'left_E_sha256':h(A[0]),'left_U_sha256':h(A[1]),'right_E_sha256':h(B[0]),'right_U_sha256':h(B[1]),
   'union_E_sha256':h(C[0]),'union_U_sha256':h(C[1]),'union_E_points':C[0].bit_count(),'union_U_points':C[1].bit_count()}
 out={'schema':SCHEMA,'schema_version':'1.0','base_full_cycle_payload_sha256':base['payload_sha256'],
 'shared_states':N,'left_envelope_atoms_by_state':p,'right_envelope_atoms_by_state':q,
 'sum_min_envelope_atoms':sum(min(x,y) for x,y in zip(p,q)),'sum_atom_grid_cells':sum(x*y for x,y in zip(p,q)),
 'atom_grid_equals_adjacent_carrier':sum(x*y for x,y in zip(p,q))==211897540016,
 'envelope_atom_theorem':'Every four-cell tuple is an envelope atom because the included 56-event cell algebra separates each of its four local state coordinates.',
 'left_shadow_types':len(L),'right_shadow_types':len(R),'left_complement_shadows_realized':complement_closed_L,'right_complement_shadows_realized':complement_closed_R,
 'mixed_disjoint_shadow_type_pairs_tested_before_stop':tested,'all_mixed_disjoint_union_shadows_locally_realized':not missing,
 'first_missing_mixed_union_shadow':witness,
 'interpretation':('Every first-round disjoint cross-copy union has a coarse empty/partial/full shared-state classification attained by an actual local descriptor in at least one copy.' if not missing else 'A first-round disjoint cross-copy union has a coarse empty/partial/full classification attained by no local descriptor.'),
 'scope':'Exact Boolean-envelope counts and coarse three-valued shadow-type obstruction only. Partial fibre sections are discarded: this does not realize the mixed union, an exact greatest-old-lower or least-old-upper shadow, or imply mixed closure, preservation of extrema, or latticehood.',
 'evidence_class':'executable verified symbolic MDD restriction census',
 'command':'python3 notes/open_questions/verification/adjacent_full_cycle_boolean_envelope_shadow.py --verify'}
 out['producer_sha256']=hashlib.sha256(open(__file__,'rb').read()).hexdigest();out['payload_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest();return out

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--emit',action='store_true');ap.add_argument('--verify',action='store_true');a=ap.parse_args();out=payload();path=os.path.join(HERE,'adjacent_full_cycle_boolean_envelope_shadow.json')
 if a.emit:
  with open(path,'w') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
 else:assert json.load(open(path))==out
 print(json.dumps(out,sort_keys=True,indent=2))
