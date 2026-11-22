# token counts vs originals.txt. usage: python tok.py <dir> file1 file2 ...
import tiktoken,json,sys,re
d=sys.argv[1];E={n:tiktoken.get_encoding(n) for n in ['o200k_base','cl100k_base']}
def secs(t): return {m.group(1):m.group(0) for m in re.finditer(r'(?ms)^§(\d+)\b.*?(?=^§\d|\Z)',t)}
base=open(f'{d}/originals.txt').read();b={n:len(e.encode(base)) for n,e in E.items()}
out={}
for f in ['originals.txt']+sys.argv[2:]:
    t=open(f'{d}/{f}').read();out[f]={n:[len(e.encode(t)),round(100*(1-len(e.encode(t))/b[n]),1)] for n,e in E.items()}
    out[f]['per_sec_o200k']={k:len(E['o200k_base'].encode(v)) for k,v in secs(t).items()}
    print(f,{n:out[f][n] for n in E},out[f]['per_sec_o200k'])
json.dump(out,open(f'{d}/tokens.json','w'),indent=1)
