# Blind decode prompt (no key, no originals). usage: python decodeprompt.py <dir> name=file
import sys,os,re
d=sys.argv[1];os.makedirs(f'{d}/dispatch',exist_ok=True)
for a in sys.argv[2:]:
    n,f=a.split('=');t=open(f'{d}/{f}').read().strip()
    you=[m for m in re.findall(r'(?m)^§(\d+) you\b',t)]
    H=('The TEXT below is written in a compact notation. Decode every section back into complete, natural English prose. '
       f'Sections marked "you" ({", ".join("§"+x for x in you)}) are instructions to an assistant: write them as the full original instructions to that assistant. '
       'Keep every fact, number, name, quoted string, condition, permission, prohibition, actor and deadline word exactly; do not add anything that is not in the TEXT. Output: for each section, a line "§N" then its prose.')
    open(f'{d}/dispatch/decode_{n}.txt','w').write(f"{H}\n\nTEXT:\n{t}\n");print('wrote decode',n)
