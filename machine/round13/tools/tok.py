import tiktoken,json,sys
E={n:tiktoken.get_encoding(n) for n in ['o200k_base','cl100k_base']}
base={n:len(e.encode(open('originals.txt').read())) for n,e in E.items()}
out={}
for f in ['originals.txt']+sys.argv[1:]:
    t=open(f).read();out[f]={n:[len(e.encode(t)),round(100*(1-len(e.encode(t))/base[n]),1)] for n,e in E.items()}
    print(f,out[f])
json.dump(out,open('tokens.json','w'),indent=1)
