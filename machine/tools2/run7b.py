# SECONDARY weak reader: local Qwen2.5-7B Q4_K_M, temp 0, fresh call per prompt. usage: python run7b.py <dir> name ... (reads dispatch/qa_<name>.txt -> answers_7b/<name>_r1.json)
import sys,os,json;sys.path.insert(0,'/workspace/jordan-context/ailang/machine/bench/tools');import llm;from llm import chat
llm.WALL=2400
d=sys.argv[1];os.makedirs(f'{d}/answers_7b',exist_ok=True)
for n in sys.argv[2:]:
    out=f'{d}/answers_7b/{n}_r1.json'
    if os.path.exists(out): continue
    t,dt,u=chat(open(f'{d}/dispatch/qa_{n}.txt').read(),max_tokens=3500)
    open(out,'w').write(t);print(n,dt,u,flush=True)
