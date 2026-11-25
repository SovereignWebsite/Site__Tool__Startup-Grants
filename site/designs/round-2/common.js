/* Round 2, shared by the five directions. Loads /data/grants.json, holds the filter state, calls the page's render.
   No third-party scripts, no storage, no tracking. */
(function(){
 var S={country:'',stage:'',sector:'',q:''},data=null,renderFn=null;
 var el=function(t,c,x){var e=document.createElement(t);if(c)e.className=c;if(x!=null)e.textContent=x;return e};
 var G=window.G={el:el,state:S,
  $:function(i){return document.getElementById(i)},
  today:function(){return new Date().toISOString().slice(0,10)},
  days:function(d){return Math.round((Date.parse(d+'T00:00:00Z')-Date.parse(G.today()+'T00:00:00Z'))/86400000)},
  daysText:function(d){var n=G.days(d);return n<0?'passed '+(-n)+' day'+(n===-1?'':'s')+' ago':n===0?'today':n===1?'tomorrow':'in '+n+' days'},
  label:function(kind,k){return (data.vocabularies[kind]||{})[k]||k},
  val:function(v){return v||'Not stated on the official page'},
  link:function(text,href){var a=el('a',null,text);a.href=href;return a},
  filtered:function(){var q=S.q.toLowerCase();return data.programmes.filter(function(p){
   if(S.country&&p.countries.indexOf(S.country)<0)return false;
   if(S.stage&&p.stages.indexOf(S.stage)<0)return false;
   if(S.sector&&p.sectors.indexOf(S.sector)<0&&p.sectors.indexOf('any')<0)return false;
   if(q&&(p.name+' '+p.organisation+' '+p.eligibility_notes).toLowerCase().indexOf(q)<0)return false;return true})},
  /* Competitions carry no stage or sector tags, so they show only when those filters are clear. */
  competitions:function(){var oc=data.open_competitions;if(!oc||S.stage||S.sector||(S.country&&S.country!=='GB'))return [];var q=S.q.toLowerCase();
   return oc.items.filter(function(i){return !q||(i.title+' '+i.funder).toLowerCase().indexOf(q)>=0}).sort(function(a,b){return a.closes<b.closes?-1:1})},
  compNote:function(){var oc=data.open_competitions;return (S.stage||S.sector)?'Open UK competitions are not tagged by stage or sector, so they are hidden while those filters are set.':oc.note+' Source: Innovation Funding Service, checked '+oc.date_checked+'.'},
  refresh:function(){var l=G.filtered(),oc=data.open_competitions,nc=G.competitions().length;G.$('count').textContent=l.length+' of '+data.programmes.length+' programmes and '+nc+' of '+(oc?oc.items.length:0)+' open UK competitions shown'+(nc===0&&oc&&(S.stage||S.sector)?' (competitions are hidden while stage or sector is set)':'');
   var n=(S.country?1:0)+(S.stage?1:0)+(S.sector?1:0),s=G.$('fsum');if(s)s.textContent=n?'Filters ('+n+' set)':'Filters';renderFn(l,data)},
  start:function(render){renderFn=render;
   fetch('/data/grants.json').then(function(r){return r.json()}).then(function(d){data=d;G.data=d;
    var used={countries:new Set(),stages:new Set(),sectors:new Set()};
    d.programmes.forEach(function(p){p.countries.forEach(function(x){used.countries.add(x)});p.stages.forEach(function(x){used.stages.add(x)});p.sectors.forEach(function(x){used.sectors.add(x)})});
    [['f-country','countries','country'],['f-stage','stages','stage'],['f-sector','sectors','sector']].forEach(function(a){
     var sel=G.$(a[0]);if(!sel)return;Object.keys(d.vocabularies[a[1]]).filter(function(k){return used[a[1]].has(k)}).forEach(function(k){var o=document.createElement('option');o.value=k;o.textContent=d.vocabularies[a[1]][k];sel.appendChild(o)});
     sel.addEventListener('change',function(){S[a[2]]=sel.value;G.refresh()})});
    var q=G.$('f-q');if(q)q.addEventListener('input',function(){S.q=q.value;G.refresh()});
    var r=G.$('f-reset');if(r)r.addEventListener('click',function(){S.country=S.stage=S.sector=S.q='';['f-country','f-stage','f-sector','f-q'].forEach(function(i){var e=G.$(i);if(e)e.value=''});if(G.onReset)G.onReset();G.refresh()});
    var fb=G.$('fbox');if(fb&&window.matchMedia){var mq=window.matchMedia('(min-width:48rem)');var set=function(){fb.open=mq.matches};set();mq.addEventListener&&mq.addEventListener('change',set)}
    var gaps=G.$('gaps');if(gaps)d.not_yet_read.forEach(function(g){gaps.appendChild(el('li',null,g.name+': '+g.reason))});
    G.refresh()}).catch(function(){G.$('count').textContent='The data could not be loaded. See /data/grants.json.'})},
  /* The same compact list of open competitions, used by the designs that keep them apart. */
  renderComps:function(box){box.textContent='';var l=G.competitions();var h=G.$('comp-h');if(h)h.hidden=false;
   box.appendChild(el('p','muted',G.compNote()));
   if(!l.length&&!(S.stage||S.sector))box.appendChild(el('p','muted','No competitions match.'));
   var ul=el('ul','comps');l.forEach(function(i){var li=el('li');var b=el('strong',null,i.title);li.appendChild(b);
    li.appendChild(el('span','muted',' closes '+i.closes+' ('+G.daysText(i.closes)+')'+(i.award_text?'; '+i.award_text:'')+(i.funder?'; '+i.funder:'')));ul.appendChild(li)});
   if(l.length)box.appendChild(ul)}
 };
})();
/* Compact card: the facts a founder needs first are visible, the rest sits under "More details". */
(function(){var G=window.G,el=G.el;
 G.card=function(p,extra,level){var li=el('li','card'),h=el(level||'h2');h.appendChild(G.link(p.name,p.official_url));li.appendChild(h);
  li.appendChild(el('p','org',p.organisation));
  var t=el('div','tags');p.countries.forEach(function(x){t.appendChild(el('span',null,G.label('countries',x)))});p.stages.forEach(function(x){t.appendChild(el('span',null,G.label('stages',x)))});
  if(p.kind!=='programme')t.appendChild(el('span',null,p.kind==='tax-relief'?'Investor tax relief':'Submission route'));li.appendChild(t);
  if(extra)li.appendChild(extra);
  var dl=el('dl');[['Funding',p.funding_amount_text],['Deadline',p.deadline_text]].forEach(function(r){dl.appendChild(el('dt',null,r[0]));dl.appendChild(el('dd',r[1]?'clamp':'empty',G.val(r[1])))});li.appendChild(dl);
  var d=el('details','more'),s=el('summary',null,'More details');d.appendChild(s);var dl2=el('dl');
  [['Funding, in full',p.funding_amount_text],['Deadline, in full',p.deadline_text],['Share of costs',p.funding_rate_text],['How to apply',p.how_to_apply],['Who can apply',p.eligibility_notes],['Note',p.notes]].forEach(function(r){if(!r[1]&&(r[0]==='Note'||/in full/.test(r[0])))return;dl2.appendChild(el('dt',null,r[0]));dl2.appendChild(el('dd',r[1]?null:'empty',G.val(r[1])))});
  d.appendChild(dl2);var a=el('p','muted','Checked '+p.date_checked+' on ');a.appendChild(G.link('the official page',p.official_url));d.appendChild(a);li.appendChild(d);return li};
})();
