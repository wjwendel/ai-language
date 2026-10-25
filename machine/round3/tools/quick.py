import tiktoken,re,sys;o=tiktoken.get_encoding('o200k_base');c=tiktoken.get_encoding('cl100k_base')
n=lambda s:(len(o.encode(s)),len(c.encode(s)))
orig=[p.strip() for h,p in re.findall(r'=== (.*?) ===\n(.*?)(?=\n=== |\Z)',open('originals.txt').read(),re.S)]
pay=[m.group(0).rstrip('\n') for m in re.finditer(r'(?ms)^§(\d).*?(?=^§|\Z)',open(sys.argv[1] if len(sys.argv)>1 else 'payload.txt').read())]
T=[0,0,0,0]
for i,(a,b) in enumerate(zip(orig,pay)):
    x,y=n(a),n(b);T=[T[0]+x[0],T[1]+x[1],T[2]+y[0],T[3]+y[1]];print(f'P{i+1}',x,y,f'{100*(1-y[0]/x[0]):.1f}% {100*(1-y[1]/x[1]):.1f}%')
print('all',T,f'{100*(1-T[2]/T[0]):.1f}% {100*(1-T[3]/T[1]):.1f}%')
if '-w' in sys.argv:
  for l in open(sys.argv[1]).read().split('\n'):
    for w in re.findall(r' \S+',l):
      if n(w)[0]>1: print(repr(w),n(w))
