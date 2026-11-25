# Builds the pages that read grants.json: /fit/, /provenance/, /plan/ and /graph/, from the layout of /start/.
# python3 tools/build-pages.py   (run tools/build-data.py first)
import json,re,html,os
import subprocess
R=subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip()+'/site/'
G=json.load(open(R+'data/grants.json'))
tpl=open(R+'start/index.html').read()
U='https://startup-grants.tool.sovereignweb.site'
esc=lambda s:html.escape(str(s if s is not None else ''),quote=True)
def make(path,title,desc,main,css='',script='',nav_current=''):
    t=tpl
    main=main.replace('@@NPROG@@',str(len(G['programmes']))).replace('@@NGAP@@',str(len(G['not_yet_read']))).replace('@@NSRC@@',str(len(G['sources'])))
    pass
    t=t.replace('Start here: Startup grants in Europe and the UK',esc(title))
    t=t.replace("Where to start, for the owner of this site: connecting GitHub, the first change, and asking for more.",esc(desc))
    t=t.replace(U+'/start/',U+path)
    t=re.sub(r'<main id="main">.*?(?=<footer>)','<main id="main" class="wide">\n'+main+'\n',t,flags=re.S)
    t=t.replace('</style>','''.wide{max-width:70rem}
:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.tblwrap{overflow-x:auto;border:1px solid var(--line);border-radius:6px}.tbl{border-collapse:collapse;width:100%;min-width:52rem;font-size:.9rem}.tbl th,.tbl td{border-bottom:1px solid var(--line);padding:.5rem .6rem;text-align:left;vertical-align:top;overflow-wrap:anywhere}.tbl thead th{border-bottom:2px solid var(--fg)}
.pill{display:inline-block;border:1px solid var(--line);border-radius:99px;padding:0 .5rem;font-size:.78rem}.ok{border-color:var(--accent);color:var(--accent)}
h2{margin-top:2.2rem}ul.plain li,ol li{color:var(--fg)}
'''+css+'</style>',1)
    t=t.replace('<a href="/start/">Start here</a>\n    <a href="/agents/">Use with your AI</a>\n  </nav>','<a href="/">Find grants</a>\n    <a href="/fit/">Check my fit</a>\n    <a href="/graph/">Graph</a>\n    <a href="/provenance/">Provenance</a>\n  </nav>',1)
    t=t.replace('<a href="/start/">Start here</a>\n  <a href="/agents/">Use with your AI</a>\n  <a href="/admin/">How this site was made</a>','<a href="/fit/">Check my fit</a>\n  <a href="/graph/">Graph</a>\n  <a href="/provenance/">Provenance</a>\n  <a href="/plan/">Plan</a>\n  <a href="/start/">Start here</a>\n  <a href="/agents/">Use with your AI</a>\n  <a href="/admin/">How this site was made</a>',1)
    if script: t=t.replace('</body>','<script>'+script+'</script>\n</body>')
    os.makedirs(R+path.strip('/'),exist_ok=True); open(R+path.strip('/')+'/index.html','w').write(t)
progs=G['programmes'];V=G['vocabularies']
# ---------- provenance (static HTML) ----------
def li(u,t=None): return f'<a href="{esc(u)}">{esc(t or u)}</a>'
rows=''
for p in progs:
    pv=p['provenance']
    rows+=f'''<tr><th scope="row">{li(p['official_url'],p['name'])}</th><td>{esc(pv['read_on'])}</td><td>{esc(pv['how_read'].split('. Amounts')[0].replace('page text fetched and summarised by ','Fetched and summarised by '))}{(' '+esc(pv['how_read'].split('Also: ')[1]) if 'Also: ' in pv['how_read'] else '')}</td><td>{esc(pv['source_license']['licence'])}</td><td>{esc(pv['cross_check'] or 'None')}</td></tr>\n'''
srows=''
for s in G['sources']:
    dead=('404' in s['note'])
    srows+=f'''<tr><td>{(esc(s['url']) if dead else '<a href="%s">%s</a>'%(esc(s['url']),esc(s['host'] or s['id']))) if s['url'] else esc(s['id'])}</td><td><span class="pill {'ok' if s['outcome']=='read' else ''}">{esc(s['outcome'])}</span></td><td>{esc(s['method'])}</td><td>{esc(s['read_on'])}</td><td>{esc(s['note'])}</td></tr>\n'''
nread=sum(1 for s in G['sources'] if s['outcome']=='read')
nfail=sum(1 for s in G['sources'] if s['outcome'] in('not read','refused'))
CAPS=json.load(open(R+'assets/provenance/captions.json'))['screenshots']
shots=''.join(f'<figure><a href="/assets/provenance/{esc(c["file"])}"><img src="/assets/provenance/{esc(c["file"])}" width="{c["width"]}" height="{c["height"]}" loading="lazy" alt="{esc(c["title"])}"></a><figcaption><strong>{esc(c["title"])}</strong><br>{esc(c["detail"])}</figcaption></figure>' for c in CAPS)
main=f'''<div class="mark">Provenance</div>
<h1>How we know</h1>
<p>Every entry on this site comes from the programme's own official page. This page shows the whole chain, who read what and when, what failed, and what we did not trust. {len(progs)} programmes, {len(G['sources'])} source records ({nread} read, {nfail} not read or refused).</p>
<h2>The chain, for every entry</h2>
<ol>
<li><strong>Starting list.</strong> The public Notion database <em>{esc(G['credits']['starting_list']['name'])}</em> gave names and official links only. No text was copied. {li(G['credits']['starting_list']['url'],'Open it')}.</li>
<li><strong>Official page.</strong> A web-fetch sub-agent started by the keeper fetched the page and summarised it. The keeper did not read the page itself, so amounts, rates and dates are kept as short quotes.</li>
<li><strong>Entry.</strong> The keeper, <code>startup-grants.a@SovereignWebsite.dinis</code> (Claude Sonnet 5.5, per the commit trailer), wrote the entry in its own words into {li('https://github.com/SovereignWebsite/Site__Tool__Startup-Grants/blob/dev/site/data/grants.json','site/data/grants.json')}. Fields the page does not state stay empty.</li>
<li><strong>Commit.</strong> Each change is a signed commit with an <code>Agent:</code> and a <code>Claude-Session:</code> trailer; the repository's signer check verifies it against the keeper's published key in <code>site/keys/</code>.</li>
<li><strong>Site and vault.</strong> The pages are built from that file. A read-only vault (<code>{G['vault']['host']}</code>, id <code>{G['vault']['vault_id']}</code>) holds the same data and screenshots of these pages, so the evidence lives outside the site too. Its address is not linked here yet: the site's leak scan blocks read keys, so publishing it is the owner's decision.</li>
</ol>
<h2>What we did not trust</h2>
<ul class="plain">
<li>A ChatGPT research brief supplied for this work: used for ideas only. It said the Notion list was private; it is public and was read. Its citations were not checked.</li>
<li>Aggregators and news articles: none used. When the only page found was a news item, the entry was left out.</li>
<li>Where an official page refused or was gone, the programme is listed as not read, with the reason, and nothing was filled in from memory or from the Notion text.</li>
</ul>
<h2>Cross-check with PrompTugal News</h2>
<p>PrompTugal News holds its own research on EU programmes (<a href="https://github.com/PrompTugal/PrompTugal__News__Startups/blob/dev/data/research/eu.json">data/research/eu.json</a>, read 21 November 2026 by a different agent). Where both give an amount or date they agree: EIC Accelerator, EIC Transition and Women TechEU. EIC Pathfinder is listed there with no amount.</p>
<h2>Screenshots, kept in the vault</h2>
<p>These pictures are stored in the vault as well as here. The first and last show the vault's own page as read back from the vault; the others are this site's pages as live at the time.</p>
<div class="shots">{shots}</div>
<h2>Entries</h2>
<div class="tblwrap" tabindex="0" role="region" aria-label="Entries and how each was read"><table class="tbl"><thead><tr><th scope="col">Programme (official page)</th><th scope="col">Read on</th><th scope="col">How it was read</th><th scope="col">Page licence</th><th scope="col">Cross-check</th></tr></thead><tbody>
{rows}</tbody></table></div>
<p>Licences: only the EIC site's CC BY 4.0 is on record, from PrompTugal's own licence research. For every other host the terms page has not been checked yet; the entry says so.</p>
<h2>Every address tried</h2>
<div class="tblwrap" tabindex="0" role="region" aria-label="Every address tried"><table class="tbl"><thead><tr><th scope="col">Address</th><th scope="col">Outcome</th><th scope="col">How</th><th scope="col">Date</th><th scope="col">Note</th></tr></thead><tbody>
{srows}</tbody></table></div>
<p>The same records are in <a href="/data/sources.json">sources.json</a>. The data files: <a href="/data/grants.json">grants.json</a>, <a href="/data/graph.json">graph.json</a>, <a href="/data/grants.jsonld">grants.jsonld</a>, described in <a href="/data/SCHEMA.md">the schema</a>.</p>
'''
make('/provenance/','How we know: Startup grants in Europe and the UK','The chain from official page to entry, who read what and when, and every address tried, including those that failed.',main,'.shots{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(18rem,100%),1fr));gap:1rem}.shots figure{margin:0;border:1px solid var(--line);border-radius:8px;padding:.6rem}.shots img{width:100%;height:auto;display:block;border-radius:4px}.shots figcaption{font-size:.85rem;color:var(--muted);margin-top:.4rem}.shots figcaption strong{color:var(--fg)}')
# ---------- plan ----------
main='''<div class="mark">Plan</div>
<h1>The map: sources, provenance, refresh and the fit check</h1>
<p>This page maps what exists, what is next, and what needs a decision. It is a plan, not a promise: each step says who does it and what it needs.</p>
<h2>What exists now</h2>
<ul class="plain">
<li><strong>Data:</strong> @@NPROG@@ programmes and 25 open UK competitions from official pages, @@NGAP@@ starting-list items and other addresses not yet read, with reasons (<a href="/data/grants.json">grants.json</a>).</li>
<li><strong>Provenance:</strong> a record for every entry and every address tried (<a href="/provenance/">Provenance</a>, <a href="/data/sources.json">sources.json</a>), in the same shape PrompTugal News uses for its own facts.</li>
<li><strong>Semantic graph:</strong> funders, programmes, countries, stages, sectors, official pages and readers as nodes and edges (<a href="/graph/">Graph</a>, <a href="/data/graph.json">graph.json</a>, <a href="/data/grants.jsonld">grants.jsonld</a>).</li>
<li><strong>Fit check:</strong> a form that compares a startup's answers with the criteria the official pages state (<a href="/fit/">Check my fit</a>).</li>
<li><strong>Vault:</strong> the data, the provenance and screenshots of these pages, kept in a read-only vault outside the site. It exists and renders; its address is not linked here until the owner decides how to publish a read key, because the site's leak scan blocks read keys.</li>
</ul>
<h2>Overlap with PrompTugal News</h2>
<p>PrompTugal News Startups has 577 facts about Portuguese startups, incubators, investors and rounds, 17 of them EU programmes. Ours is programme-first and Europe-wide. They agree where they overlap. Proposed: PrompTugal reads <code>grants.json</code> for programmes; this site reads PrompTugal's place pages for local incubators, which are out of scope here.</p>
<h2>Data model (from the research brief, checked against what we hold)</h2>
<table class="tbl" style="min-width:0"><thead><tr><th scope="col">Entity</th><th scope="col">Today</th><th scope="col">Next</th></tr></thead><tbody>
<tr><th scope="row">Funder</th><td>A text field on each programme</td><td>Its own record, so one funder links many programmes</td></tr>
<tr><th scope="row">Programme</th><td>@@NPROG@@ entries</td><td>More, from the 19 gaps and the EU portal</td></tr>
<tr><th scope="row">Call</th><td>25 UK competitions, kept separate</td><td>Link each call to its programme; add EU calls</td></tr>
<tr><th scope="row">Eligibility</th><td>Structured criteria for @@NPROG@@ programmes, only what pages state</td><td>More criteria as pages are read in full</td></tr>
<tr><th scope="row">Source</th><td>@@NSRC@@ records, with outcome and reader</td><td>A hash of each page's text, to see when it changes</td></tr>
<tr><th scope="row">Instrument type</th><td>Programme, route or tax relief</td><td>Grant, loan, equity, prize, cascade, accelerator, as the brief suggests</td></tr>
</tbody></table>
<h2>Refresh: how the site keeps itself current</h2>
<p>Facts are never changed by a script. A refresh only finds out what may have changed and asks an agent or a person to check.</p>
<ol>
<li><strong>Fetch:</strong> a scheduled job reads every address in <code>sources.json</code> and stores a hash of the page text and the date.</li>
<li><strong>Compare:</strong> a different hash, a passed deadline, or an address that now fails raises a flag.</li>
<li><strong>Report:</strong> flags go into a short report, one line per programme, with the old and new text side by side.</li>
<li><strong>Re-read:</strong> the keeper (or a person) re-reads the flagged pages and updates the entry and its <code>date_checked</code>, in a signed commit.</li>
<li><strong>Publish:</strong> the site rebuilds; the vault gets a new snapshot, so every version stays on record.</li>
</ol>
<p>Needs a decision: where the job runs. It cannot be on this static site. Options are a scheduled GitHub Actions job in this repository, or the keeper's own scheduled session. Either needs the permission to read the blocked pages in a browser to be settled first.</p>
<h2>Where it is not enough</h2>
<ul class="plain">
<li>@@NGAP@@ pages refused automated reading, have moved or are hubs; they stay gaps until read.</li>
<li>The fit check can only use criteria the pages state in numbers or places. Everything else is shown as text for the reader to judge.</li>
<li>Nothing here is advice, and only the funder decides who is eligible.</li>
</ul>
'''
make('/plan/','Plan: Startup grants in Europe and the UK','What exists, what overlaps with PrompTugal News, the data model, how a refresh would work and what needs a decision.',main)
# ---------- fit ----------
cs=''.join(f'<option value="{k}">{esc(v)}</option>' for k,v in V['countries'].items() if k!='EU')
ss=''.join(f'<option value="{k}">{esc(v)}</option>' for k,v in V['stages'].items())
se=''.join(f'<option value="{k}">{esc(v)}</option>' for k,v in V['sectors'].items() if k!='any')
css='''.fitform{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(15rem,100%),1fr));gap:1rem;margin:1rem 0}.fitform label,.fitform fieldset{display:flex;flex-direction:column;gap:.25rem;font-size:.9rem;color:var(--muted);min-width:0;border:0;padding:0;margin:0}
.fitform input,.fitform select{font:inherit;font-size:1rem;padding:.45rem .6rem;border:1px solid var(--muted);border-radius:6px;background:var(--bg);color:var(--fg);min-height:44px;width:100%;min-width:0}
.fitform .chk{flex-direction:row;align-items:center;gap:.5rem;min-height:44px;color:var(--fg)}.fitform .chk input{width:22px;min-height:0;height:22px}
.res{list-style:none;padding:0;display:grid;gap:.8rem}.res li{border:1px solid var(--line);border-radius:8px;padding:.8rem 1rem}.res h3{margin:0;font-size:1.05rem}.res ul{padding-left:1.1rem;margin:.4rem 0;color:var(--fg)}.res li li{margin:.2rem 0}.sym{display:inline-block;min-width:4.2rem;font-weight:700}
.btn{font:inherit;min-height:44px;padding:.4rem 1rem;border:1px solid var(--accent);background:transparent;color:var(--accent);border-radius:6px;cursor:pointer}'''
main=f'''<div class="mark">Check my fit</div>
<h1>Which of these might apply to my startup?</h1>
<p>Answer what you can; leave the rest blank. The page compares your answers with the criteria each programme's official page states, and tells you what fits, what does not, and what it cannot tell yet. It is not advice and not a decision: only the funder decides. Nothing you type leaves your browser.</p>
<form class="fitform" id="fit" onsubmit="return false" aria-label="About your startup">
<label>Where is the company registered, or where will the project be?<select id="q-country"><option value="">Not sure or skip</option>{cs}<option value="OTHER">Somewhere else</option></select></label>
<fieldset><legend>Is the company incorporated yet?</legend><label class="chk"><input type="checkbox" id="q-pre"> Not yet incorporated</label></fieldset>
<label>How old is the company, in years? (0.5 is six months)<input id="q-age" type="number" min="0" step="0.5" inputmode="decimal"></label>
<label>Full-time equivalent staff<input id="q-fte" type="number" min="0" step="1" inputmode="numeric"></label>
<label>Stage<select id="q-stage"><option value="">Skip</option>{ss}</select></label>
<label>Sector<select id="q-sector"><option value="">Skip</option>{se}<option value="other">Something else</option></select></label>
<label>Technology readiness level<select id="q-trl"><option value="">Not sure or skip</option>{''.join(f'<option value="{i}">TRL {i}</option>' for i in range(1,10))}</select></label>
<label>Equity raised so far, in euros<input id="q-eq" type="number" min="0" step="1000" inputmode="numeric"></label>
<label>Gross assets, in pounds (UK companies)<input id="q-ga" type="number" min="0" step="1000" inputmode="numeric"></label>
<label>Founded or co-founded by a woman in a top management role?<select id="q-w"><option value="">Skip</option><option value="yes">Yes</option><option value="no">No</option></select></label>
<div><button type="button" class="btn" id="q-reset">Clear answers</button></div>
</form>
<p id="q-sum" role="status" aria-live="polite">Loading the programmes</p>
<div id="q-out"></div>
<p><a href="/provenance/">How we know</a> · <a href="/data/grants.json">grants.json</a> holds every criterion with its source.</p>'''
script=r'''(function(){
var $=function(i){return document.getElementById(i)},el=function(t,c,x){var e=document.createElement(t);if(c)e.className=c;if(x!=null)e.textContent=x;return e};
var D=null;
function ans(){var n=function(i){var v=$(i).value;return v===''?null:Number(v)};
 var pre=$('q-pre').checked;return{country:$('q-country').value,pre:pre,age:pre?0:n('q-age'),fte:n('q-fte'),stage:$('q-stage').value,sector:$('q-sector').value,trl:n('q-trl'),eq:n('q-eq'),ga:n('q-ga'),w:$('q-w').value}}
// returns 'pass' | 'fail' | 'unknown'
function test(c,a,p){switch(c.type){
 case 'country_in':return !a.country?'unknown':((c.values.indexOf(a.country)>=0||(a.country==='GB-NIR'&&c.values.indexOf('GB')>=0))?'pass':'fail');
 case 'country_eu_or_associated':{if(!a.country)return 'unknown';if(a.country==='OTHER')return 'unknown';var cc=a.country==='GB-NIR'?'GB':a.country,V=D.vocabularies;return (V.eu_member_states.indexOf(cc)>=0||V.horizon_europe_associated.indexOf(cc)>=0)?'pass':'unknown'}
 case 'age_years_max':return a.age==null?'unknown':(a.age<=c.value?'pass':'fail');
 case 'age_months_max':return a.age==null?'unknown':(a.pre?(c.allow_pre_incorporation?'pass':'fail'):(a.age*12<=c.value?'pass':'fail'));
 case 'age_months_between':return a.pre?'fail':(a.age==null?'unknown':(a.age*12>=c.min&&a.age*12<=c.max?'pass':'fail'));
 case 'fte_lt':return a.fte==null?'unknown':(a.fte<c.value?'pass':'fail');
 case 'gross_assets_le_gbp':return a.ga==null?'unknown':(a.ga<=c.value?'pass':'fail');
 case 'trl_between':return a.trl==null?'unknown':(a.trl>=c.min&&a.trl<=c.max?'pass':'fail');
 case 'equity_raised_lt_eur':return a.eq==null?'unknown':(a.eq<c.value?'pass':'fail');
 case 'women_led':return !a.w?'unknown':(a.w==='yes'?'pass':'fail');
 case 'sector_in':return !a.sector?'unknown':(c.values.indexOf(a.sector)>=0?'pass':'fail');
 case 'sector_not':return !a.sector?'unknown':(c.values.indexOf(a.sector)>=0?'fail':'pass');
 default:return 'unknown'}}
function evalP(p,a){var rs=p.criteria.map(function(c){return{c:c,s:test(c,a,p),machine:c.type!=='text_only'}});
 // softer, keeper-classified fields: stage and sector tags
 var soft=[];if(a.stage&&p.stages.indexOf(a.stage)<0)soft.push('Aimed at a different stage: '+p.stages.map(function(x){return D.vocabularies.stages[x]}).join(', ')+' (the keeper\'s reading of the page).');
 if(a.sector&&a.sector!=='other'&&p.sectors.indexOf('any')<0&&p.sectors.indexOf(a.sector)<0)soft.push('Covers different sectors: '+p.sectors.map(function(x){return D.vocabularies.sectors[x]}).join(', ')+'.');
 var fail=rs.filter(function(r){return r.s==='fail'}),unk=rs.filter(function(r){return r.machine&&r.s==='unknown'}),pass=rs.filter(function(r){return r.machine&&r.s==='pass'});
 var g=fail.length||soft.length?'no':(pass.length&&!unk.length?'yes':'maybe');return{p:p,rs:rs,soft:soft,g:g}}
var SYM={pass:['Fits','sym'],fail:['Does not fit','sym'],unknown:['Cannot tell','sym']};
function card(r){var li=el('li'),h=el('h3'),a=el('a',null,r.p.name);a.href=r.p.official_url;h.appendChild(a);li.appendChild(h);
 li.appendChild(el('p','muted',r.p.organisation+'. Checked '+r.p.date_checked+'.'));
 var ul=el('ul');r.rs.forEach(function(x){var i=el('li');i.appendChild(el('span','sym',x.c.type==='text_only'?'Read this':SYM[x.s][0]));i.appendChild(document.createTextNode(' '+x.c.text));ul.appendChild(i)});
 r.soft.forEach(function(t){var i=el('li');i.appendChild(el('span','sym','Does not fit'));i.appendChild(document.createTextNode(' '+t));ul.appendChild(i)});li.appendChild(ul);
 var m=el('p','muted','Funding: '+(r.p.funding_amount_text||'not stated on the page')+' Deadline: '+(r.p.deadline_text||'not stated on the page'));li.appendChild(m);return li}
function render(){var a=ans(),rs=D.programmes.map(function(p){return evalP(p,a)});
 var groups=[['yes','Passes every check we can make','Every number and place on the page that we can check fits your answers. Read the other criteria too.'],['maybe','Cannot tell yet','Some checks need an answer you have not given, or the page has only text criteria. Fill in more, or read the criteria.'],['no','Does not fit','At least one stated criterion does not match your answers.']];
 var out=$('q-out');out.textContent='';var any=ans();
 var cnt={yes:0,maybe:0,no:0};rs.forEach(function(r){cnt[r.g]++});
 $('q-sum').textContent=cnt.yes+' pass every check we can make, '+cnt.maybe+' cannot be told yet, '+cnt.no+' do not fit.';
 groups.forEach(function(g){var l=rs.filter(function(r){return r.g===g[0]});if(!l.length)return;var s=el('section'),h=el('h2',null,g[1]+' ('+l.length+')');s.appendChild(h);s.appendChild(el('p','muted',g[2]));var ul=el('ul','res');l.forEach(function(r){ul.appendChild(card(r))});s.appendChild(ul);out.appendChild(s)})}
fetch('/data/grants.json').then(function(r){return r.json()}).then(function(d){D=d;
 ['q-country','q-pre','q-age','q-fte','q-stage','q-sector','q-trl','q-eq','q-ga','q-w'].forEach(function(i){$(i).addEventListener('input',render);$(i).addEventListener('change',render)});
 $('q-pre').addEventListener('change',function(){$('q-age').disabled=$('q-pre').checked});
 $('q-reset').addEventListener('click',function(){$('fit').reset();$('q-age').disabled=false;render()});render()}).catch(function(){$('q-sum').textContent='The data could not be loaded. See grants.json.'});
})();'''
make('/fit/','Check my fit: Startup grants in Europe and the UK','Answer a few questions and see which programmes fit the criteria their official pages state, which do not, and which cannot be told yet.',main,css,script)
# ---------- graph ----------
css='''.gwrap{position:relative;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.4fr);gap:3rem;margin:1rem 0}@media (max-width:40rem){.gwrap{grid-template-columns:minmax(0,1fr);gap:1.5rem}#gsvg{display:none}}
#gsvg{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}.gcol{display:flex;flex-direction:column;gap:.35rem;position:relative;z-index:1}.gcol h2{margin:.8rem 0 .2rem;font-size:.9rem;color:var(--muted)}
.node{font:inherit;text-align:left;min-height:44px;padding:.3rem .7rem;border:1px solid var(--line);border-radius:6px;background:var(--bg);color:var(--fg);cursor:pointer}.node[aria-pressed="true"]{border-color:var(--accent);outline:2px solid var(--accent)}.node.link{border-color:var(--accent);color:var(--accent)}.node.dim{color:var(--muted);border-style:dashed}
#gdetail{border:1px solid var(--line);border-radius:8px;padding:.8rem 1rem;min-height:5rem}#gdetail dt{font-weight:600;margin-top:.4rem}#gdetail dd{margin:0;color:var(--muted)}'''
main='''<div class="mark">Graph</div>
<h1>How the grants connect</h1>
<p>Pick a country, stage, sector or funder on the left to see the programmes it connects to. Pick a programme on the right to see everything it connects to, including the official page it was written from. The same nodes and edges are in <a href="/data/graph.json">graph.json</a> and, as linked data, <a href="/data/grants.jsonld">grants.jsonld</a>.</p>
<p id="gcount" role="status" aria-live="polite">Loading the graph</p>
<div class="gwrap" id="gwrap"><svg id="gsvg" aria-hidden="true"></svg><div class="gcol" id="gleft"></div><div class="gcol" id="gright"></div></div>
<h2>Selected</h2>
<div id="gdetail" role="status" aria-live="polite"><p class="muted">Nothing selected yet.</p></div>
<p><a href="/provenance/">How we know</a></p>'''
script=r'''(function(){
var $=function(i){return document.getElementById(i)},el=function(t,c,x){var e=document.createElement(t);if(c)e.className=c;if(x!=null)e.textContent=x;return e};
var G,sel=null,btn={};
fetch('/data/graph.json').then(function(r){return r.json()}).then(function(g){G=g;
 var byId={};g.nodes.forEach(function(n){byId[n.id]=n});
 var left=$('gleft'),right=$('gright'),kinds=[['country','Countries'],['stage','Stages'],['sector','Sectors'],['funder','Funders']];
 var nb={};g.edges.forEach(function(e){(nb[e.source]=nb[e.source]||[]).push(e.target);(nb[e.target]=nb[e.target]||[]).push(e.source)});
 function mk(n,col){var b=el('button','node',n.label);b.type='button';b.setAttribute('aria-pressed','false');b.dataset.id=n.id;b.addEventListener('click',function(){pick(n.id)});btn[n.id]=b;col.appendChild(b)}
 kinds.forEach(function(k){var ns=g.nodes.filter(function(n){return n.type===k[0]});if(!ns.length)return;left.appendChild(el('h2',null,k[1]));ns.forEach(function(n){mk(n,left)})});
 right.appendChild(el('h2',null,'Programmes'));g.nodes.filter(function(n){return n.type==='programme'}).forEach(function(n){mk(n,right)});
 $('gcount').textContent=g.nodes.filter(function(n){return n.type==='programme'}).length+' programmes, '+g.nodes.length+' nodes and '+g.edges.length+' edges.';
 function draw(ids){var s=$('gsvg');s.textContent='';var w=$('gwrap').getBoundingClientRect();if(!ids)return;
  ids.forEach(function(p){var a=btn[sel.id],b=btn[p];if(!a||!b)return;var ra=a.getBoundingClientRect(),rb=b.getBoundingClientRect();
   var left=ra.left<rb.left,x1=(left?ra.right:ra.left)-w.left,y1=ra.top+ra.height/2-w.top,x2=(left?rb.left:rb.right)-w.left,y2=rb.top+rb.height/2-w.top;
   var l=document.createElementNS('http://www.w3.org/2000/svg','line');l.setAttribute('x1',x1);l.setAttribute('y1',y1);l.setAttribute('x2',x2);l.setAttribute('y2',y2);l.setAttribute('stroke','currentColor');l.setAttribute('stroke-width','2');l.style.color=getComputedStyle(document.documentElement).getPropertyValue('--accent');s.appendChild(l)})}
 function pick(id){sel=sel&&sel.id===id?null:byId[id];var ids=sel?(nb[id]||[]):null;
  Object.keys(btn).forEach(function(k){var on=sel&&k===sel.id,lk=ids&&ids.indexOf(k)>=0;btn[k].setAttribute('aria-pressed',on?'true':'false');btn[k].classList.toggle('link',!!lk);btn[k].classList.toggle('dim',!!sel&&!on&&!lk)});
  var dt=$('gdetail');dt.textContent='';if(!sel){dt.appendChild(el('p','muted','Nothing selected yet.'));draw(null);return}
  var h=el('p');h.appendChild(el('strong',null,sel.label));h.appendChild(document.createTextNode(' ('+sel.type.replace('_',' ')+')'));dt.appendChild(h);
  var dl=el('dl'),groups={};(nb[id]||[]).forEach(function(o){var n=byId[o];(groups[n.type]=groups[n.type]||[]).push(n)});
  Object.keys(groups).forEach(function(t){dl.appendChild(el('dt',null,t.replace('_',' ')+(groups[t].length>1?'s':'')));var dd=el('dd');groups[t].forEach(function(n,i){if(i)dd.appendChild(document.createTextNode(', '));if(n.url){var a=el('a',null,n.label);a.href=n.url;dd.appendChild(a)}else dd.appendChild(document.createTextNode(n.label))});dl.appendChild(dd)});dt.appendChild(dl);
  draw((ids||[]).filter(function(o){return btn[o]&&(sel.type==='programme'?byId[o].type!=='programme':byId[o].type==='programme')}))}
 window.addEventListener('resize',function(){if(sel){var id=sel.id;sel=null;pick(id)}});
}).catch(function(){$('gcount').textContent='The graph could not be loaded. See graph.json.'});
})();'''
make('/graph/','Graph: Startup grants in Europe and the UK','Funders, programmes, countries, stages, sectors and official pages as a graph you can explore.',main,css,script)
