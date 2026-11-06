"""NOVA WELL original campaign home; catalogue facts remain in catalogue_views."""
import re
from html import escape


def decorate(ctx):
    root, t, icon = ctx['ROOT'], ctx['t'], ctx['icon']
    page = root / 'index.html'
    html = page.read_text(encoding='utf-8')
    nav = ''.join(f'<a href="/collections/{slug}/">{t(en, zh)}</a>' for slug,en,zh in [('jewellery','All jewellery','全部首饰'),('earrings','Earrings','耳环'),('rings','Rings','戒指'),('bracelets','Bracelets','手链')])
    nav = nav.replace('<a href="/collections/jewellery/">'+t('All jewellery','全部首饰')+'</a>', '<button type="button" class="campaign-collections" data-open="menuDialog" aria-haspopup="dialog" aria-controls="menuDialog">'+t('All jewellery','全部首饰')+' <span aria-hidden="true">⌄</span></button>')
    header = f'''<header class="site-header campaign-header"><div class="campaign-masthead wrap"><button class="icon-button campaign-menu" data-open="menuDialog" aria-label="Open menu">{icon('menu')}</button><a class="wordmark" href="/" aria-label="NOVA WELL home">NOVA WELL</a><nav class="campaign-nav" aria-label="Main navigation">{nav}</nav><div class="header-actions"><button class="icon-button" data-open="searchDialog" aria-label="Search">{icon('search')}</button><button id="language" class="language" aria-label="Change language">中文</button><button class="icon-button bag-button" data-open="bagDialog" aria-label="Open bag">{icon('bag')}<span class="bag-count" aria-hidden="true">0</span></button></div></div></header>'''
    html = re.sub(r'<header class="site-header">.*?</header>', lambda _: header, html, count=1, flags=re.S)
    html = html.replace('</head>', '<link rel="stylesheet" href="/assets/home-cover.css"><link rel="preload" as="image" href="/assets/campaign/model-poster-desktop.webp" media="(min-width: 701px)"><link rel="preload" as="image" href="/assets/campaign/model-poster-mobile.webp" media="(max-width: 700px)"><script src="/assets/home-cover.js" defer></script></head>')
    cards = ''
    for code in ['JZ001', 'ES001', 'JZ002', 'ES002']:
        p = next(x for x in ctx['products'] if x['id'] == code)
        im = p['variants'][0]['images'][0]
        en, zh = ('Ring', '戒指') if p['category'] == 'rings' else ('Earrings', '耳环')
        cards += f'<article class="edit-card"><a href="/products/{p["slug"]}/"><div class="edit-card-image"><img src="{im["src"]}" width="{im["width"]}" height="{im["height"]}" alt="{en} {escape(code)}" loading="lazy" decoding="async">{icon("arrow")}</div><div class="edit-card-label"><span>{t(en,zh)}</span><h3>{code}</h3><span>{t("Price to be confirmed","价格待确认")}</span></div></a></article>'
    body = f'''
<section class="campaign-hero" aria-labelledby="campaignTitle">
  <div class="campaign-media">
    <picture class="campaign-poster"><source media="(max-width: 700px)" srcset="/assets/campaign/model-poster-mobile.webp" width="720" height="960"><img src="/assets/campaign/model-poster-desktop.webp" alt="AI model wearing gold-colour heart earrings and a silver-colour ring; brand concept imagery" data-alt-en="AI model wearing gold-colour heart earrings and a silver-colour ring; brand concept imagery" data-alt-zh="AI模特佩戴金色酒红爱心耳环与银色戒指的品牌概念影像" width="1600" height="900" fetchpriority="high"></picture>
    <video id="campaignVideo" class="campaign-video campaign-film" muted loop playsinline preload="none" aria-hidden="true" data-video-desktop="/assets/campaign/model-loop-desktop.mp4" data-video-mobile="/assets/campaign/model-loop-mobile.mp4"></video>
    <div class="campaign-styling-action"><button type="button" class="styling-trigger" data-open="stylingDialog" aria-haspopup="dialog" aria-controls="stylingDialog">{t('View the styling','查看造型细节')}<span aria-hidden="true">＋</span></button></div>
  </div>
  <div class="campaign-copy"><p class="campaign-eyebrow">{t('THE EVERYDAY EDIT','日常首饰灵感')}</p><h1 id="campaignTitle">{t('A little detail.','一点细节，')}<br>{t('A lot of you.','很像自己。')}</h1><p class="campaign-intro">{t('For the days that are entirely your own.','为每一个属于自己的日常。')}</p><a class="campaign-button" href="/collections/jewellery/">{t('Explore jewellery','探索首饰')}{icon('arrow')}</a><div class="campaign-quicklinks"><a href="/collections/earrings/">{t('Earrings','耳环')}</a><span aria-hidden="true">/</span><a href="/collections/rings/">{t('Rings','戒指')}</a></div></div>
</section>
<div class="campaign-ribbon"><span>{t('YOUR EVERYDAY, IN A NEW LIGHT.','日常，自有光芒。')}</span><a href="#the-edit">{t('Discover the edit','向下探索')}<span aria-hidden="true">↓</span></a></div>
<section class="styling-story" id="the-edit" aria-labelledby="stylingTitle">
  <div class="story-media story-ring">
    <img id="ringPoster" src="/assets/campaign/ring-gold.webp" alt="Gold-colour ring product reference" data-alt-en="Gold-colour ring product reference" data-alt-zh="金色戒指商品参考图" width="977" height="980" loading="lazy">
    <video id="ringVideo" class="ring-film campaign-film" muted loop playsinline preload="none" aria-hidden="true" data-video-desktop="/assets/campaign/ring-gold-loop.mp4"></video>
    <div class="ring-toolbar"><div class="ring-tones" role="group" aria-label="Ring film colour"><button type="button" data-ring-tone="gold" aria-pressed="true"><span class="tone-dot gold" aria-hidden="true"></span>{t('Gold colour','金色')}</button><button type="button" data-ring-tone="silver" aria-pressed="false"><span class="tone-dot silver" aria-hidden="true"></span>{t('Silver colour','银色')}</button></div></div>
  </div>
  <div class="story-copy"><p class="campaign-eyebrow">{t('THE ART OF CONTRAST','搭配的分寸')}</p><h2 id="stylingTitle">{t('Warm meets cool.','金与银，')}<br>{t('You make it yours.','由你定义。')}</h2><p>{t('A touch of colour. A silver-colour line. Explore earrings and rings, then find your own way to wear them.','一点酒红，一道银色线条。从耳环与戒指开始，找到自己的佩戴方式。')}</p><div class="story-links"><a class="campaign-text-link" href="/collections/rings/">{t('Explore rings','探索戒指')}{icon('arrow')}</a><button type="button" class="campaign-text-link" data-open="stylingDialog" data-styling-tab="ring" aria-haspopup="dialog" aria-controls="stylingDialog">{t('See the ring reference','查看戒指参考图')}<span aria-hidden="true">＋</span></button></div></div>
</section>
<section class="earring-story" aria-labelledby="heartTitle">
  <div class="earring-copy"><p class="campaign-eyebrow">{t('A LITTLE COLOUR','一点色彩')}</p><h2 id="heartTitle">{t('Follow your','跟随你的')}<br><em>{t('own heart.','心意。')}</em></h2><p>{t('A heart-shaped detail, in deep wine red. A new starting point for everyday styling.','深酒红色的爱心细节，为日常搭配打开新的灵感。')}</p><a class="campaign-text-link" href="/collections/earrings/">{t('Explore earrings','探索耳环')}{icon('arrow')}</a></div>
  <button type="button" class="earring-visual" data-open="stylingDialog" data-styling-tab="earring" aria-haspopup="dialog" aria-controls="stylingDialog" aria-labelledby="earringVisualLabel">
    <span class="earring-media" aria-hidden="true">
      <img src="/assets/campaign/earring-poster.webp" alt="" width="800" height="800" loading="lazy" decoding="async">
      <video id="earringVideo" class="campaign-film" muted loop playsinline preload="none" aria-hidden="true" data-video-desktop="/assets/campaign/earring-loop.mp4"></video>
    </span>
    <span class="earring-visual-label">{t('A closer look','近看细节',attrs='id="earringVisualLabel"')}<span aria-hidden="true">＋</span></span>
  </button>
</section>
<section class="brand-philosophy" aria-labelledby="philosophyTitle">
  <div class="brand-philosophy-inner wrap">
    <div>
      <p class="campaign-eyebrow">{t('THE NOVA WELL PHILOSOPHY','NOVA WELL 品牌理念')}</p>
      <h2 id="philosophyTitle">{t('Jewellery that feels like you.','戴出自己的样子。')}</h2>
    </div>
    <div class="brand-philosophy-detail">
      <p>{t('Clean lines, thoughtful proportions and a hint of colour. We like jewellery that slips easily into your everyday and leaves room for you to make it yours.','利落的线条，恰到好处的比例，再加一点色彩。我们喜欢能自然融入日常的首饰，也相信每个人都有自己的佩戴方式。')}</p>
      <a class="campaign-text-link" href="/pages/about/">{t('More about NOVA WELL','了解 NOVA WELL')}{icon('arrow')}</a>
    </div>
  </div>
</section>
<section class="campaign-edit wrap" aria-labelledby="editTitle"><div class="edit-heading"><div><p class="campaign-eyebrow">{t('FROM THE CATALOGUE','来自商品目录')}</p><h2 id="editTitle">{t('Find your next detail.','发现下一份心动。')}</h2></div><a class="campaign-text-link" href="/collections/jewellery/">{t('All jewellery','全部首饰')}{icon('arrow')}</a></div><div class="edit-grid">{cards}</div><p class="edit-status">{t('Product information preview · Prices and availability to be confirmed','商品资料预览 · 售价与供货状态待确认')}</p><nav class="campaign-categories" aria-label="Jewellery categories">{ctx['nav']()}</nav></section>
<dialog id="stylingDialog" class="styling-dialog" aria-labelledby="stylingDialogTitle">
  <div class="dialog-head"><h2 id="stylingDialogTitle">{t('The details, up close.','细节，近看。')}</h2><button data-close aria-label="Close styling details">{icon('close')}</button></div>
  <p class="styling-context">{t('AI-assisted campaign imagery shows styling ideas. For product information, see the individual catalogue entries.','造型影像经 AI 辅助创作，用于展示搭配灵感。具体商品信息请查看目录中的各型号资料。')}</p>
  <div class="styling-tabs" role="tablist" aria-label="Styling details"><button type="button" role="tab" id="earringTab" aria-controls="earringPanel" aria-selected="true" data-style-tab="earring">{t('Earrings','耳环')}</button><button type="button" role="tab" id="ringTab" aria-controls="ringPanel" aria-selected="false" data-style-tab="ring" tabindex="-1">{t('Ring','戒指')}</button></div>
  <div id="earringPanel" role="tabpanel" aria-labelledby="earringTab"><img src="/assets/campaign/earrings-reference.webp" alt="Supplied earring product reference" data-alt-en="Supplied earring product reference" data-alt-zh="用户提供的耳环参考图" width="977" height="977" loading="lazy"><p>{t('Gold-colour hoops. Wine-red heart-shaped drops. Product reference; exact specifications are to be confirmed.','金色耳圈，酒红色爱心吊坠。商品参考图，具体商品参数待确认。')}</p><a class="campaign-button" href="/collections/earrings/">{t('Explore earrings','探索耳环')}{icon('arrow')}</a></div>
  <div id="ringPanel" role="tabpanel" aria-labelledby="ringTab" hidden><div class="ring-reference-pair"><img src="/assets/campaign/ring-gold.webp" alt="Supplied gold-colour ring reference" data-alt-en="Supplied gold-colour ring reference" data-alt-zh="用户提供的金色戒指参考图" width="977" height="980" loading="lazy"><img src="/assets/campaign/ring-silver.webp" alt="Supplied silver-colour ring reference" data-alt-en="Supplied silver-colour ring reference" data-alt-zh="用户提供的银色戒指参考图" width="979" height="981" loading="lazy"></div><p>{t('Two colours, the same point of view. Product references; explore the catalogue for product details.','两种颜色，同一份表达。商品参考图，具体信息请查看商品目录。')}</p><a class="campaign-button" href="/collections/rings/">{t('Explore rings','探索戒指')}{icon('arrow')}</a></div>
</dialog>
'''
    html = re.sub(r'<main id="main" tabindex="-1">.*?</main>', lambda _: '<main id="main" tabindex="-1">'+body+'</main>', html, count=1, flags=re.S)
    html = html.replace('A new jewellery collection is taking shape.', 'Jewellery. Everyday expression.').replace('全新首饰系列，正在筹备。', '首饰，融入日常表达。')
    page.write_text(html, encoding='utf-8')
