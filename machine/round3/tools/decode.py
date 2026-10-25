# Blind decode: decoder sees ONLY key text + payload text + target language/section. Usage: decode.py KEY PAYLOAD OUT "1:English" "2:English" "2:Spanish" ...
import sys,re,json;sys.path.insert(0,'.');from llm import chat
key=open(sys.argv[1]).read() if sys.argv[1]!='-' else '';pay=open(sys.argv[2]).read();out=sys.argv[3]
log=[]
with open(out,'w') as f:
    f.write(f'# Blind decode\nDecoder: Qwen2.5-7B-Instruct (Q4_K_M, llama.cpp, temperature 0), one fresh stateless call per section/language. Input per call: key + payload only.\n\n')
for job in sys.argv[4:]:
    sec,lang=job.split(':')
    if key:
        prompt=f"Below is a decoding KEY for a compact code, then a PAYLOAD written in that code. Using only the key and the payload, decode section §{sec} into fluent, natural prose in {lang}. Keep every fact, add nothing. Output only the decoded text.\n\nKEY:\n{key}\n\nPAYLOAD:\n{pay}"
    else:
        prompt=f"Below is a compressed TEXT. Rewrite section §{sec} as fluent, natural, complete prose in {lang}. Keep every fact, add nothing. Output only the rewritten text.\n\nTEXT:\n{pay}"
    txt,dt,u=chat(prompt)
    log.append({'job':job,'seconds':dt,'usage':u})
    with open(out,'a') as f: f.write(f'## §{sec} → {lang}\n\n{txt.strip()}\n\n')
    print(job,dt,flush=True)
json.dump(log,open(out+'.log.json','w'),indent=1)
