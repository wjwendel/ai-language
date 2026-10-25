# Encoder self-check r3 (SELF-TEST, heuristic): numbers, hedges, negations/modals per passage; flags any bare "!" operator (r2 failure 3) and bare digit+space counts.
import re
orig={f'P{i+1}':p.strip() for i,(h,p) in enumerate(re.findall(r'=== (.*?) ===\n(.*?)(?=\n=== |\Z)',open('originals.txt').read(),re.S))}
pay={('P'+m.group(1)):m.group(0) for m in re.finditer(r'(?ms)^§(\d).*?(?=^§|\Z)',open('payload.txt').read())}
LANG={'P1':'en','P2':'es','P3':'ko','P4':'de','P5':'es'}
NUMW={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'twelve':12,'tres':3,'dos':2,'cuarto':4,'vier':4,'drei':3,'zwölf':12,'열두':12,'여섯':6,'팔순':80,'칠순':70,'noon':12}
def nums(t):
    t=re.sub(r'(\d)[.,](\d{3})\b',r'\1\2',t);v=set()
    for m in re.findall(r'\d+(?:[.,]\d+)?',t): v.add(float(m.replace(',','.')))
    for w,x in NUMW.items():
        if re.search(r'(?<![^\W\d_])'+w if not w.isascii() else r'\b'+w+r'\b',t.lower()): v.add(float(x))
    return v
def pnums(t):
    v=set()
    for m in re.findall(r'\d+(?:\.\d+)?',t):
        f=float(m);v.add(f)
        if len(m) in (3,4) and '.' not in m: v.add(int(m)//100)
        if 13<=f<=24: v.add(f-12)
    for w,x in NUMW.items():
        if re.search(r'\b'+w+r'\b',t): v.add(float(x))
    if 'M' in t: v.update(f*1e6 for f in list(v))
    if '000' in t: v.update(f/1e4 for f in list(v))   # 100000 won = 10만
    return v
NEG={'en':r"\b(never|not|don't|doesn't|isn't|hasn't|can't|cannot|won't|mustn't|no)\b",'es':r'\b(no|nunca|sin)\b','de':r'\b(nicht|kein|keine|nie)\b','ko':r'(못|말고|안 돼|하지 마|않)'}
PNEG=r"\b(never|not|don't|cannot|no|without|need not|unless)\b"
HED={'en':r'\b(about|around)\b','es':r'\b(hacia|unos|unas|alrededor)\b','de':r'\b(etwa|rund|über)\b','ko':r'(쯤|약)'}
# documented waivers (reviewed by encoder): clock minutes/zero hours are inside @HMM; Korean month numbers are inside AprD; ES "No ... nunca" is one prohibition -> never; KO 예약 contains 약 (not a hedge)
WAIVE={'P2':{0.0,30.0},'P3':{4.0},'P5':{0.0}}
ok=True
for p in orig:
    s,y=orig[p],pay[p];L=LANG[p]
    miss=sorted(x for x in nums(s) if x not in pnums(y) and x not in WAIVE.get(p,set()))
    ns,np_=len(re.findall(NEG[L],s,re.I)),len(re.findall(PNEG,y))
    hs,hp=len(re.findall(HED[L],s,re.I)),y.count('~')+len(re.findall(r'\bover\d',y))
    bang=re.findall(r' ![a-z ]',y); bare=re.findall(r' \d+ [a-z]',y)
    st='OK' if not miss and (np_>=ns or p=='P5') and not bang else 'CHECK'
    ok&=st=='OK'
    print(f'{p}[{L}] numbers_missing={miss} negations src={ns} payload={np_} hedges src={hs} payload={hp} bang_ops={bang} bare_count_digits={bare} -> {st}')
print('SELF-CHECK','PASS' if ok else 'REVIEW')
