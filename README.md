# NOVA WELL · PDF jewellery catalogue

469 models / 703 catalogue entries imported from three user-supplied PDFs (181 bracelet, 106 ring, 182 earring models). Retail prices, stock and checkout are not enabled. Necklaces and pendants remain empty pending source data.

Run `python3 scripts/render-store.py`, `node scripts/build.mjs`, `python3 scripts/verify_site.py`, `node --test scripts/cart.test.cjs scripts/catalog.test.cjs`.

Data: `data/products.json`; private supplier audit: `data/supplier-import-audit.json`; source import script: `scripts/import-pdf-catalogue.py`. Never publish data/, docs/, scripts/ or original supplier PDFs. Public assets/catalog* contain only the browsing projection. Images are embedded PDF originals encoded to WebP, never AI replacements.

Keep the jewellery brand theme and EN/ZH preferences. Feature preview only; no automatic main merge. See `docs/PDF-IMPORT.md`.
