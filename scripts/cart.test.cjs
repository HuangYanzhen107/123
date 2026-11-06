const {test}=require('node:test'),assert=require('node:assert/strict');
const {migrate,normalizeLanguage,sanitize,EPOCH}=require('../assets/cart.js');
test('jewellery migration clears retired SKUs and drafts while preserving language and market',()=>{
 const data=new Map([['novawell_lang','zh'],['novawell_market','IE'],['novawell_demo_cart','{"a1-s":2,"p1":1,"ref-01":3}'],['novawell_admin_demo','old draft'],['novawell_recently_viewed','old items']]);
 const storage={getItem:k=>data.get(k)??null,setItem:(k,v)=>data.set(k,v),removeItem:k=>data.delete(k)};
 assert.equal(migrate(storage),true);assert.equal(data.get('novawell_lang'),'zh');assert.equal(data.get('novawell_market'),'IE');
 for(const key of ['novawell_demo_cart','novawell_admin_demo','novawell_recently_viewed'])assert.equal(data.has(key),false);
 assert.equal(data.get('novawell_catalog_epoch'),EPOCH);assert.equal(migrate(storage),true);
});
test('blocked storage and unsupported language values do not break the empty catalogue',()=>{
 assert.equal(migrate({getItem(){throw Error('blocked')}}),false);assert.equal(migrate(null),false);
 assert.equal(normalizeLanguage('zh'),'zh');for(const v of ['ar','en','unknown',null])assert.equal(normalizeLanguage(v),'en');
 for(const v of [{p1:1,'a1-s':2},null,[],{sku:10}])assert.deepEqual(sanitize(v),{});
});
