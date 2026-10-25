# Baselines a/b: a fresh stateless model call per passage (same local Qwen2.5-7B, temp 0; it sees only the source passage).
import re,sys;sys.path.insert(0,'tools');from llm import chat
orig=[(h,p.strip()) for h,p in re.findall(r'=== (.*?) ===\n(.*?)(?=\n=== |\Z)',open('originals.txt').read(),re.S)]
P={'a_terse':"Shorten the following text maximally into terse, telegraphic plain English. Keep every fact. Output only the shortened text.\n\n",
   'b_summarize':"Summarize/compress this text.\n\n"}
for k,pr in P.items():
    out=[]
    for i,(h,p) in enumerate(orig):
        t,dt,u=chat(pr+p,max_tokens=800); out.append(f'§{i+1}\n'+t.strip()); print(k,i+1,dt,flush=True)
    open(f'baselines/{k}.txt','w').write('\n'.join(out)+'\n')
