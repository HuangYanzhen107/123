#!/usr/bin/env python3
"""Extract supplier catalogue rows and original embedded photographs. Run manually with PDF directory."""
import fitz,json,re,sys,hashlib,io,collections
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parent.parent
source=Path(sys.argv[1]);models={};audit=[];photo_cache={};counts={}
labels={'Material','Color','Length','Width','Width/Length','Size','Weight','MOQ','MOQ(pcs)','Quantity','EXW USD Unit Price'}
pattern=r'(ES|JZ|SL)\d+(?:-\d+)?(?:/26Letters)?'
for f in sorted(source.glob('*.pdf')):
 doc=fitz.open(f);rows=[];cur=None;images=[]
 for pn,page in enumerate(doc):
  for b in page.get_text('dict')['blocks']:
   if b['type']!=0:continue
   for line in b['lines']:
    tx=''.join(s['text'] for s in line['spans']).strip()
    if re.fullmatch(pattern,tx):
     cur={'model':tx,'page':pn+1,'endPage':pn+1,'y':line['bbox'][1],'raw':[],'images':[]};rows.append(cur)
    elif cur:cur['raw'].append(tx);cur['endPage']=pn+1
  for im in page.get_image_info(xrefs=True):
   if im['width']>=30 and im['height']>=30:images.append((pn+1,(im['bbox'][1]+im['bbox'][3])/2,im['xref']))
 for pn,y,xref in images:
  prev=[r for r in rows if (r['page'],r['y'])<=(pn,y)]
  assert prev,(f.name,pn,'orphan image')
  if xref not in prev[-1]['images']:prev[-1]['images'].append(xref)
 for row in rows:
  fields={};key=None
  for tx in row.pop('raw'):
   if tx in ('Picture','Model No'):continue
   if tx in labels:key=tx;fields.setdefault(key,[])
   elif key:fields[key].append(tx)
  fields={k:' '.join(v).strip() for k,v in fields.items()}
  assert fields.get('Material') and row['images'],(f.name,row)
  photographs=[]
  for xref in row.pop('images'):
   cachekey=(f.name,xref)
   if cachekey not in photo_cache:
    embedded=doc.extract_image(xref);img=Image.open(io.BytesIO(embedded['image'])).convert('RGB');img.thumbnail((1000,1000))
    buf=io.BytesIO();img.save(buf,format='WEBP',quality=86,method=6);data=buf.getvalue();name=hashlib.sha256(data).hexdigest()[:20]+'.webp'
    path=ROOT/'assets/products'/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)
    photo_cache[cachekey]={'src':'/assets/products/'+name,'width':img.width,'height':img.height}
   photographs.append(photo_cache[cachekey])
  code=row['model'];category={'SL':'bracelets','JZ':'rings','ES':'earrings'}[code[:2]]
  slug=re.sub('[^a-z0-9-]+','-',code.lower()).strip('-')
  product=models.setdefault(code,{'id':code,'slug':slug,'category':category,'sourceFile':f.name,'variants':[]})
  publicFields={k:v for k,v in fields.items() if k not in ['MOQ','MOQ(pcs)','Quantity','EXW USD Unit Price']}
  unit=fields.get('Quantity',fields.get('MOQ',fields.get('MOQ(pcs)',''))).lower()
  publicFields['Unit']='Set' if 'set' in unit else 'Pair' if 'pair' in unit else 'Piece' if 'pc' in unit or unit.isdigit() else 'Not specified'
  variant={'number':len(product['variants'])+1,'sourcePage':row['page'],'sourceEndPage':row['endPage'],'fields':publicFields,'images':photographs}
  product['variants'].append(variant)
  audit.append({'model':code,'file':f.name,'page':row['page'],'endPage':row['endPage'],'fields':fields,'images':photographs})
 counts[category]={'pages':len(doc),'rows':len(rows),'models':len(set(r['model'] for r in rows))}
order={'bracelets':0,'rings':1,'earrings':2}
products=sorted(models.values(),key=lambda p:(order[p['category']],int(re.search(r'\d+',p['id'])[0]),p['id']))
(ROOT/'data/products.json').write_text(json.dumps(products,ensure_ascii=False,indent=2)+'\n')
(ROOT/'data/supplier-import-audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
summary={'categories':counts,'models':len(products),'rows':len(audit),'photographs':len(list((ROOT/'assets/products').glob('*.webp'))),'sourceHashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in source.glob('*.pdf')}}
(ROOT/'data/import-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n');print(json.dumps(summary,ensure_ascii=False,indent=2))
