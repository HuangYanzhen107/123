(function(){
  'use strict';
  const $=(s,r=document)=>r.querySelector(s),all=(s,r=document)=>Array.from(r.querySelectorAll(s));
  const regions={GB:['United Kingdom · GBP','英国 · GBP 英镑'],IE:['Ireland · EUR','爱尔兰 · EUR 欧元'],SE:['Sweden · SEK','瑞典 · SEK 瑞典克朗'],DK:['Denmark · DKK','丹麦 · DKK 丹麦克朗'],NO:['Norway · NOK','挪威 · NOK 挪威克朗'],FI:['Finland · EUR','芬兰 · EUR 欧元'],IS:['Iceland · ISK','冰岛 · ISK 冰岛克朗']};
  let language='en',region='GB',storage=null,toastTimer;
  try{storage=window.localStorage;JewelleryState.migrate(storage);language=JewelleryState.normalizeLanguage(storage.getItem('novawell_lang'));const saved=storage.getItem('novawell_market');if(Object.hasOwn(regions,saved))region=saved;}catch{}
  const tr=(en,zh)=>language==='zh'?zh:en;
  const labels={'Open menu':'打开菜单','NOVA WELL home':'NOVA WELL 首页','Search':'搜索','Change language':'切换语言','Open bag':'打开购物袋','Main navigation':'主导航','Mobile navigation':'手机导航','Jewellery categories':'首饰分类','Close styling details':'关闭造型细节','View earring reference':'查看耳环参考图','Styling details':'造型细节','Ring film colour':'戒指影像颜色','Ring detail film':'戒指细节影像','AI jewellery brand film':'AI首饰品牌影像','Close menu':'关闭菜单','Close search':'关闭搜索','Close bag':'关闭购物袋','Close region selector':'关闭地区选择'};
  function save(key,value){try{storage?.setItem(key,value);return !!storage;}catch{return false;}}
  function applyLanguage(){
    document.documentElement.lang=language==='zh'?'zh-CN':'en-GB';document.documentElement.dir='ltr';
    all('[data-en][data-zh]').forEach(el=>{el.textContent=el.dataset[language]});
    document.title=document.documentElement.dataset[language==='zh'?'titleZh':'titleEn'];
    $('#language').textContent=language==='zh'?'English':'中文';
    all('[aria-label]').forEach(el=>{el.dataset.originalLabel??=el.getAttribute('aria-label');el.setAttribute('aria-label',language==='zh'?(labels[el.dataset.originalLabel]||el.dataset.originalLabel):el.dataset.originalLabel)});
    all('[data-alt-en]').forEach(el=>{el.alt=el.dataset[language==='zh'?'altZh':'altEn']});
    all('input[type=search]').forEach(input=>{input.placeholder=tr('Necklaces, rings, everyday details…','项链、戒指、日常细节…')});
    all('option',$('#regionSelect')).forEach(option=>{option.textContent=regions[option.value][language==='zh'?1:0]});
    $('#regionLabel').textContent=regions[region][language==='zh'?1:0];
    document.dispatchEvent(new Event('nw:languagechange'));
  }
  $('#language').addEventListener('click',()=>{language=language==='en'?'zh':'en';save('novawell_lang',language);applyLanguage()});
  const dialogs=all('dialog');
  function openDialog(id,opener){const dialog=document.getElementById(id);if(!dialog||dialog.open)return;dialog._opener=opener||document.activeElement;if(id==='regionDialog'){$('#regionSelect').value=region;$('#regionStatus').textContent='';}dialog.showModal();document.body.classList.add('modal-open');if(id==='searchDialog')$('#searchInput').focus();}
  function closeDialog(dialog){
    if(!dialog.open||dialog._closing)return;
    if(matchMedia('(prefers-reduced-motion: reduce)').matches){dialog.close();return;}
    dialog._closing=true;
    const a=dialog.animate([{opacity:1,transform:'translateY(0)'},{opacity:0,transform:'translateY(5px)'}],{duration:120,easing:'ease-in'});
    a.finished.catch(()=>{}).then(()=>{dialog._closing=false;dialog.close()});
  }
  all('[data-open]').forEach(button=>button.addEventListener('click',()=>openDialog(button.dataset.open,button)));
  dialogs.forEach(dialog=>{
    all('[data-close]',dialog).forEach(button=>button.addEventListener('click',()=>closeDialog(dialog)));
    dialog.addEventListener('cancel',event=>{event.preventDefault();closeDialog(dialog)});
    dialog.addEventListener('click',event=>{if(event.target!==dialog)return;const box=dialog.getBoundingClientRect();if(event.clientX<box.left||event.clientX>box.right||event.clientY<box.top||event.clientY>box.bottom)closeDialog(dialog)});
    dialog.addEventListener('close',()=>{if(!dialogs.some(d=>d.open))document.body.classList.remove('modal-open');if(dialog._opener?.isConnected)dialog._opener.focus()});
  });
  all('[data-search-form]').forEach(form=>form.addEventListener('submit',event=>{
    event.preventDefault();const input=$('input[name=q]',form),query=input.value.trim().slice(0,120);
    if(form.hasAttribute('data-search-page')){const url=new URL(location.href);if(query)url.searchParams.set('q',query);else url.searchParams.delete('q');url.searchParams.delete('page');history.pushState(null,'',url);document.dispatchEvent(new Event('nw:search'));}
    else location.href='/pages/search/'+(query?'?q='+encodeURIComponent(query):'');
  }));
  if($('#pageSearch'))$('#pageSearch').value=(new URLSearchParams(location.search).get('q')||'').slice(0,120);
  $('#regionSelect').value=region;
  $('#saveRegion').addEventListener('click',()=>{
    const next=$('#regionSelect').value;if(!Object.hasOwn(regions,next))return;region=next;
    const stored=save('novawell_market',region);applyLanguage();
    $('#regionStatus').textContent=stored?tr('Your browsing preference is saved.','浏览偏好已保存。'):tr('Updated for this page. Browser storage is unavailable.','本页已更新，浏览器本地存储不可用。');
  });
  $('#clearPreferences')?.addEventListener('click',()=>{
    let ok=true;for(const key of ['novawell_lang','novawell_market','novawell_demo_cart','novawell_admin_demo','novawell_recently_viewed'])try{storage?.removeItem(key);if(!storage)ok=false;}catch{ok=false;}
    language='en';region='GB';$('#regionSelect').value=region;applyLanguage();
    $('#clearStatus').textContent=ok?'Saved preferences cleared on this device.':'Browser storage is unavailable. Check your site-data settings.';
  });
  applyLanguage();
  if(location.hash==='#bag')openDialog('bagDialog');
})();
