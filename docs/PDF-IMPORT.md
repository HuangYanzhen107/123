# PDF product import — 2026-11-04

This step adds supplied product information to the accepted jewellery theme; no new design scope or commerce activation.

| Category | PDF pages | Models | Catalogue entries |
| --- | ---: | ---: | ---: |
| Bracelets | 41 | 181 | 201 |
| Rings | 28 | 106 | 145 |
| Earrings | 66 | 182 | 357 |
| Total | 135 | 469 | 703 |

703 original embedded photographs extracted, including complete images split across PDF page boundaries. 469 model detail routes preserve the supplier's identifiers. Multiple entries under one model keep each photograph and parameter record separate; these are catalogue entries, not confirmed stock SKUs. ES134/26Letters and JZ063-1 labels are preserved exactly. No unsupported jewellery marketing names are fabricated.

Categories follow navigation order; model numbers sort numerically. 24 model cards per page. Search accepts model/category/material in English or Chinese, includes all entries in each model and supports pagination. Detail selector displays the matching catalogue entry image, material, colour, supplier dimensions, weight, supply unit and source pages. Unknown values, reference-picture colours and ambiguous ring numbering are marked pending rather than inferred. The existing cart remains empty and sales disabled.

Wholesale EXW USD quotations, minimum order quantities and supplier email are retained only in private source audit, excluded from public pages, JSON/JS projections and dist. No wholesale quotation is relabelled as retail price. Copper, alloy, pearls and the supplier's Titanium Steel wording are retained without claiming all items are stainless steel or pure titanium. Colour does not establish gold content. No stock, durability, allergy or waterproof claims are added.

Original PDFs are not committed or deployed. data/import-summary.json records filenames, SHA256 and totals. Run scripts/import-pdf-catalogue.py with a local directory containing these three PDFs to regenerate imports (PyMuPDF/Pillow required only for manual extraction). The renderer/build use standard Python/Node and run without PDF dependencies.

The earlier JEWELLERY-HANDOFF document describes the previous empty-catalogue stage; this import supersedes that part only. Shipping, returns, pricing and trading integrations remain pending. This step is complete at catalogue preview delivery; wait for the user's next optimisation instructions.
