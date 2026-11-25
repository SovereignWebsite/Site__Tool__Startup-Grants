# Puts the "Choose a design" picker after the header of every page in site/, and its stylesheet link in the head.
# Every local stylesheet link also gets ?v=<content hash>, so a browser never serves an old copy at the same address.
# Idempotent: it replaces what it put before. Run while designs are open for a pick; run with --remove once Dinis has picked.
#   python3 tools/add-picker.py [--remove]
import re,sys,subprocess,glob,os
root=subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip()+'/site/'
D=[(1,'Cards, compact','Key facts first, the rest under More details',False),
   (2,'Dense table','Compare many programmes at once',False),
   (3,'Guided sentence','Fill in where, what stage, what sector',False),
   (4,'Faceted panel','Tick-box filters with counts',False),
   (5,'Deadline timeline with cards','Grouped by month, days left beside each date',True)]
def block(path):
    lis=''
    for n,name,desc,rec in D:
        cur=f' aria-current="page"' if path==f'/designs/round-2/d{n}/' else ''
        lis+=f'<li><a href="/designs/round-2/d{n}/"{cur}><img src="/assets/designs/round2-d{n}.jpg" width="160" height="100" alt="" loading="lazy"><span class="n">{n}. {name}</span><span class="muted">{desc}</span>{"<br><span class=\"t\">Recommended</span>" if rec else ""}</a></li>'
    live='The live pages use the cards layout (design 1) until Dinis picks.'
    return f'<!--picker--><aside class="dp" aria-label="Choose a design"><div class="dp-in"><h2>Choose a design</h2><p>Five directions are open for a pick. {live} Tell the keeper the number, or open <a href="/designs/round-2/">the round 2 page</a> for the full list.</p><ul>{lis}</ul></div></aside><!--/picker-->'
import hashlib
def hashed(m):
    p=root+m.group(1).lstrip('/')
    h=hashlib.sha1(open(p,'rb').read()).hexdigest()[:10] if os.path.exists(p) else None
    return f'href="{m.group(1)}?v={h}"' if h else m.group(0)
n=0
for f in glob.glob(root+'**/*.html',recursive=True):
    t=open(f).read()
    path='/'+os.path.relpath(f,root).replace('index.html','').replace('\\','/')
    t=re.sub(r'<!--picker-->.*?<!--/picker-->','',t,flags=re.S)
    t=t.replace('<link rel="stylesheet" href="/assets/picker.css">\n','')
    if '--remove' not in sys.argv:
        if '</header>' in t:
            t=t.replace('</header>','</header>\n'+block(path),1)
        elif '<main id="main">' in t:
            t=t.replace('<main id="main">',block(path)+'\n<main id="main">',1)
        else:
            continue
        t=t.replace('</head>','<link rel="stylesheet" href="/assets/picker.css">\n</head>',1)
        n+=1
    t=re.sub(r'href="(/[^"?#]+\.css)(?:\?v=[0-9a-f]+)?"',hashed,t)
    open(f,'w').write(t)
print('picker on',n,'pages')
