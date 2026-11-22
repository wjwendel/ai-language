# Round-12 frontier QA prompt (same format as round11/tools/qaprompt.py; languages updated).
import json,sys
Q=json.load(open('directuse/questions.json'))
def qids(p):
    qs=Q[f'P{p}'];out=[(f'§{p}.en{i}',x['q']) for i,x in enumerate(qs,1)];l2=qs[0]['l2']
    out+=[(f'§{p}.{l2}{i}',x['sl']) for i,x in enumerate(qs,1)];return out
INS='Answer using only the TEXT. Reply with one JSON object only, mapping each question ID to a short answer string. Answer each question in the language named in its ID: ".en" English, ".es" Spanish, ".zh" Chinese, ".fr" French, ".pt" Portuguese, ".pl" Polish. If the TEXT does not say, answer "not stated".'
def prompt(text):
    ql='\n'.join(f'{i}: {q}' for p in range(1,6) for (i,q) in qids(p))
    return f"TEXT:\n{text.strip()}\n\nQUESTIONS (each is about the section named in its ID):\n{ql}\n\n{INS}"
if __name__=='__main__':
    for m in sys.argv[1:]:
        src={'original':'originals.txt','mnc16':'payload_mnc16.txt','mnc16xx':'payload_mnc16xx.txt'}.get(m,f'baselines/{m}.txt')
        open(f'frontier/prompt_{m}.txt','w').write(prompt(open(src).read()));print(m)
