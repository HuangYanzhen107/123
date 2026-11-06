"""PDF-backed catalogue views; no retail price, stock or sales claims."""
import json,re
from html import escape as e
from pathlib import Path
LABELS={'Material':('Material','材质'),'Color':('Colour','颜色'),'Length':('Length / size (supplier)','长度／尺码（供应商标注）'),'Width':('Width','宽度'),'Width/Length':('Width / length','宽度／长度'),'Size':('Size (supplier notation)','尺码（供应商标注）'),'Weight':('Weight (supplier)','重量（供应商标注）'),'Unit':('Catalogue unit','目录计量单位')}
CAT={'bracelets':('Bracelet','手链'),'rings':('Ring','戒指'),'earrings':('Earrings','耳环')}
def translated(value):
 if not value or value.strip().lower() in ['/','please contact me','not specified']:return ('Not specified · To be confirmed','未提供，待确认')
 v=value.strip();zh=v
 translations=[('316 Stainless steel','316不锈钢'),('Titanium Steel','钛钢（供应商称谓）'),('Stainless steel','不锈钢'),('rose gold','玫瑰金色'),('reference picture','见图，具体选项待确认'),('Adjustable','可调节'),('Copper','铜'),('Alloy','合金'),('Zircon','锆石'),('pearl','珍珠（类型未注明）'),('acrylic','亚克力'),('Gold','金色'),('Silver','银色'),('Black','黑色'),('White','白色'),('colorful','多色'),('width','宽'),('Pair','一对'),('Piece','一件'),('Set','一套')]
 for a,b in translations:zh=re.sub(re.escape(a),b,zh,flags=re.I)
 return v,zh

def populate(ctx):
 root=ctx['ROOT'];write=ctx['write'];t=ctx['t'];shell=ctx['shell'];nav=ctx['nav'];icon=ctx['icon'];button=ctx['button'];products=ctx['products']
 public=[]
 def card(p):
  catEn,catZh=CAT[p['category']];im=p['variants'][0]['images'][0];matEn,matZh=translated(p['variants'][0]['fields']['Material'])
  return f'<article class="product-card"><a href="/products/{p["slug"]}/"><div class="product-image"><img src="{im["src"]}" width="{im["width"]}" height="{im["height"]}" alt="{e(catEn+" "+p["id"])}" loading="lazy" decoding="async"></div><div class="product-card-copy"><p class="product-kind">{t(catEn,catZh)}</p><h2>{e(p["id"])}</h2><p class="product-material">{t(matEn,matZh)}</p><p class="product-price">{t("Price to be confirmed","价格待确认")}</p></div></a></article>'
 for p in products:
  en,zh=CAT[p['category']];matEn,matZh=translated(p['variants'][0]['fields']['Material'])
  public.append({'id':p['id'],'category':p['category'],'nameEn':en,'nameZh':zh,'materialEn':matEn,'materialZh':matZh,'image':p['variants'][0]['images'][0],'url':'/products/'+p['slug']+'/','searchText':' '.join([p['id'],en,zh]+[z for v in p['variants'] for raw in v['fields'].values() for z in translated(raw)]).lower()})
 def catalogue(items,category):
  pages=(len(items)+23)//24
  cards=''.join(card(p) for p in items[:24])
  return f'''<div class="catalogue" data-category="{category}"><div class="catalogue-summary"><p class="catalogue-count" aria-live="polite">{t(f'{len(items)} models',f'{len(items)} 个型号')}</p><p>{t('Catalogue order · Model number','目录顺序 · 型号排序')}</p></div><p class="catalogue-disclaimer">{t('Product information preview. Retail prices and availability are being prepared; ordering is not open.','商品资料展示。零售价与供货状态尚待确认，暂未开放下单。')}</p><div class="product-grid" id="productGrid">{cards}</div><p class="catalogue-empty" hidden>{t('No matching jewellery. Try a model number or another category.','暂无匹配商品，请尝试型号或其他分类。')}</p><nav class="catalogue-pagination" aria-label="Catalogue pagination" {"hidden" if pages<2 else ""}><button class="button secondary" data-catalogue-prev>{t('Previous','上一页')}</button><span class="pagination-label" aria-live="polite">{t(f'Page 1 of {pages}',f'第 1 / {pages} 页')}</span><button class="button secondary" data-catalogue-next>{t('Next','下一页')}</button></nav></div>'''
 # Keep the original theme, replacing only the preparation block with actual PDF catalogue cards.
 home=(root/'index.html').read_text();start=home.index('<section class="collection-preview');end=home.index('<section class="perspective',start)
 featured=[next(p for p in products if p['id']==code) for code in ['SL001','SL002','JZ001','JZ002','ES001','ES002']]
 block=f'<section class="catalogue-home wrap"><div class="section-heading"><div><p class="eyebrow">{t("FROM THE CATALOGUE","首饰目录")}</p><h2>{t("Explore the details.","从细节，认识首饰。")}</h2></div><a class="text-link" href="/collections/jewellery/">{t("All jewellery","全部首饰")}{icon("arrow")}</a></div><div class="product-grid">'+''.join(card(p) for p in featured)+f'</div><p class="catalogue-disclaimer">{t("Product catalogue preview · Prices and availability to be confirmed","商品目录预览 · 售价与供货状态待确认")}</p></section>'
 home=home[:start]+block+home[end:];write('index.html',home)
 for slug,en,zh in [('jewellery','Jewellery','首饰')]+ctx['CATEGORIES']:
  items=[p for p in products if slug=='jewellery' or p['category']==slug]
  body=f'<div class="wrap collection-page"><div class="breadcrumbs"><a href="/">{t("Home","首页")}</a><span>/</span>{t(en,zh)}</div><div class="collection-heading"><p class="eyebrow">NOVA WELL / {t("THE COLLECTION","首饰系列")}</p><h1>{t(en,zh)}</h1><p>{t("Explore by category, then by model number.","按分类探索，依型号有序浏览。")}</p></div><nav class="collection-tabs" aria-label="Jewellery categories">{nav(slug)}</nav>'
  if items:body+=catalogue(items,slug)
  else:body+=f'<div class="collection-empty collection-large"><h2>{t("This collection is in preparation.","此系列正在筹备。")}</h2><p>{t("No product information has been supplied for this category yet.","此分类暂未提供商品资料，后续将按实际资料补充。")}</p>{button("/collections/jewellery/","Explore available categories","浏览已有商品分类",True)}</div>'
  write(f'collections/{slug}/index.html',shell(en,zh,body+'</div>','collection',slug))
 search=f'<div class="wrap collection-page"><div class="breadcrumbs"><a href="/">{t("Home","首页")}</a><span>/</span>{t("Search","搜索")}</div><div class="collection-heading"><p class="eyebrow">NOVA WELL / {t("THE CATALOGUE","商品目录")}</p><h1>{t("Find your everyday piece.","寻找你的日常首饰。")}</h1></div><form class="search-form catalogue-search" data-search-form data-search-page><label for="pageSearch">{t("Search by model, category or material","按型号、分类或材质搜索")}</label><div class="search-input-row"><input id="pageSearch" name="q" type="search" maxlength="120" placeholder="SL001, rings, stainless steel…"><button class="icon-button" type="submit" aria-label="Search">{icon("search")}</button></div></form>{catalogue(products,"search")}</div>'
 write('pages/search/index.html',shell('Search jewellery','搜索首饰',search,'search'))
 for p in products:
  en,zh=CAT[p['category']];code=e(p['id']);variants=p['variants'];opts=''.join(f'<option value="{i}" data-en="Entry {i+1} · PDF p. {v["sourcePage"]}" data-zh="条目 {i+1} · PDF 第 {v["sourcePage"]} 页">Entry {i+1} · PDF p. {v["sourcePage"]}</option>' for i,v in enumerate(variants))
  select=f'<label class="variant-label" for="catalogueVariant">{t("Style / catalogue entry","款式／目录条目")}</label><select id="catalogueVariant" data-variant-select>{opts}</select>' if len(variants)>1 else ''
  panels=''
  for i,v in enumerate(variants):
   ims=''.join(f'<img src="{im["src"]}" width="{im["width"]}" height="{im["height"]}" alt="{e(en+" "+p["id"]+" · catalogue entry "+str(i+1))}" loading="{ "eager" if i==0 else "lazy"}" decoding="async">' for im in v['images'])
   fields=''.join('<div><dt>'+t(*LABELS[k])+'</dt><dd>'+t(*translated(value))+'</dd></div>' for k,value in v['fields'].items() if k in LABELS)
   pages=str(v['sourcePage'])+(f'–{v["sourceEndPage"]}' if v['sourceEndPage']!=v['sourcePage'] else '')
   panels+=f'<section class="piece-panel" data-variant-panel="{i}" {"hidden" if i else ""}><div class="piece-gallery">{ims}</div><div class="piece-specification"><h2>{t("Product details","商品参数")}</h2><dl class="piece-fields">{fields}</dl><p class="source-note">{t("Source: supplier "+en.lower()+" catalogue · p. "+pages+" · entry "+str(i+1),"资料来源：供应商"+zh+"目录 · 第 "+pages+" 页 · 条目 "+str(i+1))}</p></div></section>'
  body=f'<div class="piece-page wrap"><div class="breadcrumbs"><a href="/">{t("Home","首页")}</a><span>/</span><a href="/collections/{p["category"]}/">{t(en,zh)}</a><span>/</span>{code}</div><header class="piece-heading"><div><p class="eyebrow">NOVA WELL / {t(en,zh)}</p><h1>{code}</h1><p>{t("Price to be confirmed · Ordering not yet open","价格待确认 · 暂未开放下单")}</p></div><div class="variant-control">{select}<p>{t(f"{len(variants)} catalogue entries for this model. Each entry retains its own image and specifications.",f"此型号含 {len(variants)} 条目录记录，图片与参数逐条对应。")}</p></div></header>{panels}<div class="piece-notes"><h2>{t("Before ordering opens","商品说明")}</h2><p>{t("Images and specifications are taken from the supplied catalogue. A photograph may show several styles or a set; it does not confirm what will be included in a retail order. Missing values and supplier sizing systems remain to be confirmed.","图片与参数来自所提供目录。图片可能包含多个款式或套装，不代表零售订单的实际包含内容。缺失参数及供应商尺码体系仍待确认。")}</p><p>{t("Colour names describe appearance, not precious-metal content. Water resistance, allergy suitability and plating specifications have not been verified.","颜色名称用于描述外观，不代表贵金属含量。防水、过敏适用性及镀层规格尚未核实。")}</p><div class="piece-links"><a class="text-link" href="/pages/size-guide/">{t("Size guide","尺寸指南")}{icon("arrow")}</a><a class="text-link" href="/pages/materials-care/">{t("Materials & care","材质与护理")}{icon("arrow")}</a><a class="text-link" href="/collections/{p["category"]}/">{t("Back to collection","返回此分类")}{icon("arrow")}</a></div></div></div>'
  write(f'products/{p["slug"]}/index.html',shell(p['id']+' '+en,p['id']+' '+zh,body,'product',p['category']))
 write('assets/catalog.json',json.dumps(public,ensure_ascii=False,separators=(',',':'))+'\n')
 write('assets/catalog.js','/* Supplied PDF catalogue projection; no wholesale prices or supplier contacts. */\n(function(root){const products='+json.dumps(public,ensure_ascii=False,separators=(',',':'))+';root.NovaCatalogue=products;if(typeof module!=="undefined")module.exports=products;})(typeof window==="undefined"?globalThis:window);\n')
