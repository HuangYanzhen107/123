(function(){
 'use strict';
 const all=window.NovaCatalogue||[],root=document.querySelector('.catalogue'),select=document.querySelector('[data-variant-select]');
 const lang=()=>document.documentElement.lang==='zh-CN'?'zh':'en',tr=(en,zh)=>lang()==='zh'?zh:en;
 const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 if(select)select.addEventListener('change',()=>{document.querySelectorAll('[data-variant-panel]').forEach(p=>p.hidden=p.dataset.variantPanel!==select.value)});
 if(!root)return;
 const grid=root.querySelector('.product-grid'),count=root.querySelector('.catalogue-count'),empty=root.querySelector('.catalogue-empty'),pagination=root.querySelector('.catalogue-pagination'),label=root.querySelector('.pagination-label'),prev=root.querySelector('[data-catalogue-prev]'),next=root.querySelector('[data-catalogue-next]');
 let page=1,items=[];
 function render(){
  const url=new URL(location.href),query=root.dataset.category==='search'?(url.searchParams.get('q')||'').trim().toLowerCase():'';
  items=all.filter(p=>(['jewellery','search'].includes(root.dataset.category)||p.category===root.dataset.category)&&(!query||query.split(/\s+/).every(word=>p.searchText.includes(word))));
  const pages=Math.max(1,Math.ceil(items.length/24));page=Math.max(1,Math.min(pages,Number.parseInt(url.searchParams.get('page')||'1',10)||1));
  grid.innerHTML=items.slice((page-1)*24,page*24).map(p=>`<article class="product-card"><a href="${esc(p.url)}"><div class="product-image"><img src="${esc(p.image.src)}" width="${p.image.width}" height="${p.image.height}" alt="${esc(tr(p.nameEn,p.nameZh)+' '+p.id)}" loading="lazy" decoding="async"></div><div class="product-card-copy"><p class="product-kind">${esc(tr(p.nameEn,p.nameZh))}</p><h2>${esc(p.id)}</h2><p class="product-material">${esc(tr(p.materialEn,p.materialZh))}</p><p class="product-price">${tr('Price to be confirmed','价格待确认')}</p></div></a></article>`).join('');
  count.textContent=tr(`${items.length} models`,`${items.length} 个型号`);empty.hidden=!!items.length;pagination.hidden=pages<2;label.textContent=tr(`Page ${page} of ${pages}`,`第 ${page} / ${pages} 页`);prev.disabled=page<=1;next.disabled=page>=pages;
 }
 function go(n){const url=new URL(location.href);if(n>1)url.searchParams.set('page',n);else url.searchParams.delete('page');history.pushState(null,'',url);render();root.scrollIntoView({block:'start',behavior:'instant'});count.setAttribute('tabindex','-1');count.focus({preventScroll:true})}
 prev.addEventListener('click',()=>go(page-1));next.addEventListener('click',()=>go(page+1));
 document.addEventListener('nw:languagechange',render);window.addEventListener('popstate',render);document.addEventListener('nw:search',render);render();
})();
