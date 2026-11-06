/* No retired catalogue lines may survive the jewellery-only transition. */
(function(root){
  'use strict';
  const EPOCH='jewellery-only-2026-11';
  function normalizeLanguage(value){return value==='zh'?'zh':'en';}
  function migrate(storage){
    if(!storage)return false;
    try{
      if(storage.getItem('novawell_catalog_epoch')!==EPOCH){
        for(const key of ['novawell_demo_cart','novawell_admin_demo','novawell_recently_viewed'])storage.removeItem(key);
        storage.setItem('novawell_catalog_epoch',EPOCH);
      }
      return true;
    }catch{return false;}
  }
  function sanitize(){return {};}
  const api={EPOCH,normalizeLanguage,migrate,sanitize};root.JewelleryState=api;
  if(typeof module!=='undefined')module.exports=api;
})(typeof window==='undefined'?globalThis:window);
