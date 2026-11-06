#!/usr/bin/env python3
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import subprocess,re
ROOT=Path(__file__).resolve().parent.parent
class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        for key in ('href','src','data-video-desktop','data-video-mobile'):
            if d.get(key):self.links.append(d[key])
pages=[p for p in ROOT.rglob('*.html') if not set(p.relative_to(ROOT).parts)&{'dist','.openai','.git','.qa'}]
for p in pages:
    doc=p.read_text(encoding='utf-8');assert 'noindex,nofollow' in doc,p
    assert 'name="viewport"' in doc,p
    assert not re.search('[\u0600-\u06ff]',doc),p
    parser=Links();parser.feed(doc)
    for value in parser.links:
        if value.startswith(('#','https:','http:','data:','mailto:')):continue
        path=unquote(urlsplit(value).path)
        if not path:continue
        target=ROOT/path.lstrip('/') if path.startswith('/') else p.parent/path
        if target.is_dir():target=target/'index.html'
        assert target.exists(),f'{p.relative_to(ROOT)} -> {value}'
for p in (ROOT/'assets').glob('*.js'):subprocess.run(['node','--check',str(p)],check=True,capture_output=True)
assert all(p.parent.name.startswith(('sl','es','jz')) for p in (ROOT/'products').rglob('index.html')),'Unexpected product route'
assert not (ROOT/'assets/reference-products').exists(),'Retired photos exist'
print(f'PASS: {len(pages)} HTML pages, local links, noindex, viewport and JS syntax; only PDF-backed product routes published.')
