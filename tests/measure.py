import tiktoken,re
from passages import EX,P,JM
c=tiktoken.get_encoding("cl100k_base");o=tiktoken.get_encoding("o200k_base")
n=lambda e,s:len(e.encode(s))
for f in ["LEARN-AND-USE.md","../v2.2/LEARN-AND-USE.md","../v2.1/LEARN-AND-USE.md"]:
  s=open(f).read();print(f,"o200k",n(o,s),"cl100k",n(c,s))
def parse(f):
  d={};cur=None
  for line in open(f).read().split("\n"):
    if re.fullmatch(r"[A-Z]",line.strip()): cur=line.strip(); d[cur]=[]
    elif cur: d[cur].append(line)
  return {k:"\n".join(v).strip() for k,v in d.items()}
blind=parse("../v2.2/blindtest/encoded.txt")
def show(D,lab,ref=None):
  T=[0,0,0,0]
  for k,(p,a) in D.items():
    r=(n(o,p),n(o,a),n(c,p),n(c,a));T=[x+y for x,y in zip(T,r)]
    extra=f" | v2.2 blind o200k {n(o,ref[k])}" if ref else ""
    print(k,f"{lab} o200k {r[0]}->{r[1]} (-{100*(1-r[1]/r[0]):.0f}%) | cl100k {r[2]}->{r[3]} (-{100*(1-r[3]/r[2]):.0f}%)"+extra)
  print("TOTAL",T,f"o200k -{100*(1-T[1]/T[0]):.0f}% cl100k -{100*(1-T[3]/T[2]):.0f}%")
show(EX,"plain");show(P,"plain");show(JM,"plain",blind)
for k in JM: print(k, repr(blind[k][:60]))
