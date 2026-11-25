/* Shared by the five design directions. Loads /data/grants.json, holds the filter state, and calls the page's render(list, data).
   No third-party scripts, no storage, no tracking. */
(function(){
 var S={country:'',stage:'',sector:'',q:''},data=null;
 window.G={
  el:function(t,c,x){var e=document.createElement(t);if(c)e.className=c;if(x!=null)e.textContent=x;return e},
  $:function(i){return document.getElementById(i)},
  label:function(kind,k){return (data.vocabularies[kind]||{})[k]||k},
  val:function(v){return v||'Not stated on the official page'},
  state:S,
  filtered:function(){var q=S.q.toLowerCase();return data.programmes.filter(function(p){
   if(S.country&&p.countries.indexOf(S.country)<0)return false;
   if(S.stage&&p.stages.indexOf(S.stage)<0)return false;
   if(S.sector&&p.sectors.indexOf(S.sector)<0&&p.sectors.indexOf('any')<0)return false;
   if(q&&(p.name+' '+p.organisation+' '+p.eligibility_notes).toLowerCase().indexOf(q)<0)return false;return true})},
  start:function(render){
   fetch('/data/grants.json').then(function(r){return r.json()}).then(function(d){data=d;
    var used={countries:new Set(),stages:new Set(),sectors:new Set()};
    d.programmes.forEach(function(p){p.countries.forEach(function(x){used.countries.add(x)});p.stages.forEach(function(x){used.stages.add(x)});p.sectors.forEach(function(x){used.sectors.add(x)})});
    [['f-country','countries','country'],['f-stage','stages','stage'],['f-sector','sectors','sector']].forEach(function(a){
     var sel=G.$(a[0]);if(!sel)return;Object.keys(d.vocabularies[a[1]]).filter(function(k){return used[a[1]].has(k)}).forEach(function(k){var o=document.createElement('option');o.value=k;o.textContent=d.vocabularies[a[1]][k];sel.appendChild(o)});
     sel.addEventListener('change',function(){S[a[2]]=sel.value;go()})});
    var q=G.$('f-q');if(q)q.addEventListener('input',function(){S.q=q.value;go()});
    var r=G.$('f-reset');if(r)r.addEventListener('click',function(){S.country=S.stage=S.sector=S.q='';['f-country','f-stage','f-sector','f-q'].forEach(function(i){var e=G.$(i);if(e)e.value=''});go()});
    function go(){var l=G.filtered();G.$('count').textContent=l.length+' of '+d.programmes.length+' programmes shown';render(l,d)}
    var gaps=G.$('gaps');if(gaps)d.not_yet_read.forEach(function(g){gaps.appendChild(G.el('li',null,g.name+': '+g.reason))});
    go()}).catch(function(){G.$('count').textContent='The data could not be loaded. See /data/grants.json.'})}
 };
})();
