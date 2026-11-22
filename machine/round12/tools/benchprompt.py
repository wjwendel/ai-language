# Frontier bench-v1 prompt: all 15 frozen passages in one prompt, IDs carry the bench id (r3P1.en1). Same INS wording as fixed bench prompt.
import json,re,sys
B=json.load(open('bench/bench.json'))
INS='Answer using only the TEXT. Reply with one JSON object only, mapping each question ID to a short answer string. Answer questions whose ID contains ".es" in Spanish and the rest in English. If the TEXT does not say, answer "not stated".'
def secs(path):
    t=open(path).read();return {m.group(1):m.group(0).rstrip('\n') for m in re.finditer(r'(?ms)^§(r\dP\d)\b.*?(?=^§r|\Z)',t)}
def build(method,path=None):
    ext=secs(path) if path else None;texts=[];qs=[]
    for it in B['items']:
        bid=it['bid']
        txt=ext[bid] if ext else re.sub(r'^§\d',f'§{bid}',it['texts']['original'])
        texts.append(txt)
        for i,x in enumerate(it['questions'],1): qs.append(f'{bid}.en{i}: {x["q"]}')
        if 'es' in it['questions'][0]:
            for i,x in enumerate(it['questions'],1): qs.append(f'{bid}.es{i}: {x["es"]}')
    return 'TEXT:\n'+'\n\n'.join(texts)+'\n\nQUESTIONS (each is about the section named in its ID, e.g. r3P1.en1 is about §r3P1):\n'+'\n'.join(qs)+'\n\n'+INS
for m,p in [('original',None),('mnc16','bench/versions/mnc16.txt'),('mnc16x','bench/versions/mnc16x.txt'),('mnc14','bench/versions/mnc14.txt')]:
    open(f'round12/bench_frontier/prompt_{m}.txt','w').write(build(m,p))
