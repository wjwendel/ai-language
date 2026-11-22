# R4 lint (MNC19 form-aware): every facts.json `must` regex must match its payload section. usage: python lint_facts.py <dir> payload_x.txt
# Normalises for matching only: `never: A; B` -> `never A` lines; `Name (="x"` -> `Name="x"`; decision words -> symbols.
import json,re,sys
def norm(s):
    out=[]
    for ln in s.split('\n'):
        m=re.match(r'^(.*?)\bnever:\s*(.*)$',ln)
        if m: out+= [m.group(1)]+[f'never {x.strip()}' for x in m.group(2).split(';')]
        else: out.append(ln)
    s='\n'.join(out)
    s=s+'\n'+'\n'.join(f'{a}="{c}\n{b}="{c}' for a,b,c in re.findall(r'(\S+)\s+(\S+)\s*\(=\s*"([^"]*)"',s))
    for a,b in [(r'\bless than\s*','<'),(r'\bmore than\s*','>'),(r'\bat least\s*','≥'),(r'\b(at most|up to)\s*','≤'),(r'\bunder\s*(?=\d)','<'),(r'\bfewer than\s*','<'),(r'(\d+\s*\w*) or more',r'≥\1')]: s=s+'\n'+re.sub(a,b,s,flags=re.I) if re.search(a,s,re.I) else s
    return s
d=sys.argv[1];P=open(f'{d}/{sys.argv[2]}').read()
sec={m.group(1):norm(m.group(0)) for m in re.finditer(r'(?ms)^§(\d+)\b.*?(?=^§\d|\Z)',P)}
F=json.load(open(f'{d}/facts.json'))['facts'];bad=0
for f in F:
    s=sec.get(str(f['sec']),'')
    miss=[r for r in f.get('must',[]) if not re.search(r,s,re.I)]
    if miss: bad+=1;print('MISS',f['id'],f['text'][:70],'|',miss)
print(f'{len(F)-bad}/{len(F)} facts pass lint');sys.exit(1 if bad else 0)
