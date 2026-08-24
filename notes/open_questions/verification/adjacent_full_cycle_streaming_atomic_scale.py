#!/usr/bin/env python3
"""Immutable scale run of the committed streaming atomic-kernel engine.

The underlying transition, regression, mutation, and differential checks are
imported unchanged.  This wrapper selects 500 endpoint-spread retained events
in each orientation (prefix zero), covers all their admissible U masks, and
writes a separate receipt.
"""
import argparse,hashlib,json,os,signal

import adjacent_full_cycle_streaming_atomic_differential as engine

SCHEMA='adjacent-full-cycle-streaming-atomic-scale-v1'
PREFIX=0
SPREAD=500

def payload():
 def timeout(_signum,_frame):raise TimeoutError('scale run exceeded hard process-level 720-second cap')
 prior=signal.getsignal(signal.SIGALRM);signal.signal(signal.SIGALRM,timeout);signal.alarm(720)
 try:out,seconds=engine.payload(PREFIX,SPREAD)
 finally:
  signal.alarm(0);signal.signal(signal.SIGALRM,prior)
 kernel_schema=out['schema'];kernel_source=out.pop('producer_sha256')
 out['schema']=SCHEMA
 out['schema_version']='1.0'
 out['kernel_engine_schema']=kernel_schema
 out['kernel_engine_source_sha256']=kernel_source
 out['scale_run_intent']='500 endpoint-spread retained events per orientation, every admissible U, grouped/scalar differential replay'
 out['hard_timeout_discipline']='Process-level SIGALRM at 720 seconds wraps capture, classification, regressions, grouped scan, and scalar replay; alarm is cancelled and the prior handler restored afterward.'
 out['command']='python3 notes/open_questions/verification/adjacent_full_cycle_streaming_atomic_scale.py --verify'
 out['producer_sha256']=hashlib.sha256(open(__file__,'rb').read()).hexdigest()
 out.pop('payload_sha256',None)
 out['payload_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 return out,seconds

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--emit',action='store_true');ap.add_argument('--verify',action='store_true');a=ap.parse_args()
 out,seconds=payload();path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'adjacent_full_cycle_streaming_atomic_scale.json')
 if a.emit:
  with open(path,'w') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
 else:assert json.load(open(path))==out
 print(json.dumps({'status':'PASS','payload_sha256':out['payload_sha256'],'tested_kernels':out['tested_kernel_count'],'failures':out['failure_count'],'runtime_seconds':round(seconds,3)},sort_keys=True))
