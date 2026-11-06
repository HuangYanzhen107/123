# Project instructions

## Current user-approved direction

NOVA WELL is now a jewellery-only brand site. Modern sans-serif wordmark, warm white/stone grey/charcoal, restrained motion and clear navigation. Categories: necklaces, bracelets, rings, earrings, pendants. English/Simplified Chinese. Planned markets: UK, Ireland and the Nordics.

The user explicitly requested that every old product and non-jewellery category be removed. The user has now supplied three PDFs and explicitly requested import. The catalogue contains 469 supplier models / 703 entries, for information preview only; retain exact supplied materials including copper and alloy. Do not restore old accessory photos, concept products or retired cart SKUs. No fabricated product names, sizes, prices, stock or selectable variants. The hero is an original AI brand concept and must remain labelled as not a product listing.

## Code and workflow

- Plain static HTML/CSS/JS. Run `python3 scripts/render-store.py` to generate the bilingual shell, 469 product routes and public catalogue.
- Views: renderer and `scripts/home_cover.py`; style: `assets/jewellery.css` and homepage-only `assets/home-cover.css`; interactions: `assets/jewellery.js` and `assets/home-cover.js`; retired-cart migration: `assets/cart.js`.
- Keep image files inside the project; never reintroduce external image hotlinks or copy reference-brand marketing material.
- Validate with `python3 scripts/verify_site.py`, `node --test scripts/cart.test.cjs`, `node scripts/build.mjs`, `node --test scripts/catalog.test.cjs`.
- Publish only the allowlisted `dist/` through GitHub → Cloudflare Pages. Source docs and future PDF files stay private.
- Use feature branches and PR previews. User acceptance precedes merging and updating the formal website. Do not merge main automatically.

## Commerce and content rules

- The user reports an existing entity, payment channel and support email. Registration region, provider and delivery/returns details remain unconfirmed for implementation.
- No live payment, customer forms, subscriptions, addresses, email capture or fake order success in this preparation stage. Keep noindex.
- Future scope: custom backend, approximately100 products with Excel import, guest checkout, secure order lookup and email updates. This is not yet operational.
- Product fields must be supported by user PDFs: material/steel grade, plating, colour, ring size, chain length, single/pair, pendant chain inclusion, dimensions, weight and care. Capture source file/page, mark missing fields as pending. This import is authorised for preview; retail sale remains disabled pending verified prices, availability and missing specifications.
- Do not claim hypoallergenic, waterproof, precious-metal content, certification or product performance without verified data.
- Never ask for passwords, bank details, API tokens or secrets in chat. Configure credentials only through provider-controlled flows and server settings.
- Follow semantic markup, keyboard/focus behaviour, labelled controls, reduced motion and responsive layouts. Preserve English/Chinese preferences across pages. Old cart/editor records must not be reused.

See `docs/JEWELLERY-HANDOFF.md` for the current design and PDF handoff. Earlier private project documents describe historical directions and do not override this file or the latest user instructions.

## Homepage campaign (2026-11-05)

The user authorised implementing a model-video cover with earrings and rings. The current home uses supplied AI model footage, a separate mobile crop, supplied gold/silver ring films and supplied reference stills. All public derivatives are in `assets/campaign/`; no reference-brand media is used. The model is fictional; keep the visible AI concept disclosure. `scripts/prepare-cover-video.py` creates cosine-eased forward/reverse loops from original frames without morphing or optical-flow interpolation. This is a deliberately bidirectional edit, not continuous forward action. See `docs/HOME-COVER-HANDOFF.md` for files, playback behaviour and QA. The normal site renderer does not require ffmpeg/numpy.
