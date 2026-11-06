# Accessories fill — validation record

Date: 2026-11-03 (Asia/Shanghai).

## Scope

- 24 selected source-attributed products, 45 locally hosted WebP photos, 7 populated accessory subcollection routes.
- Existing 8 concept product routes and legacy cart IDs retained; 2 legacy concept accessories removed from visible lists/search.
- Clean category navigation, category filter/reset, alphabetical sorting, 12-item pagination, source detail pages, thumbnails/zoom and source links.
- New products remain unpriced, unavailable for orders and excluded from the demo cart. Existing concept cart is unchanged.

## Actual checks

| Check | Result |
| --- | --- |
| Static verification | 57 HTML files: local links, noindex, viewport and JS syntax passed |
| Node regression tests | 11 passed, including existing cart behaviour, reference products excluded from cart, seven category pages, 45 image hashes, pagination boundaries, pending prices and source attribution |
| Build | Allowlisted dist generated; source data, docs, scripts and local preview configuration excluded |
| Pagination | Page 2 shows items 13–24, 12 cards, with new first item; reset returns to 1–12 |
| Category filter | Jewellery selects exactly 6 products; filter reset restores 24-product catalogue |
| Sorting | Name A–Z begins Ari, Ashbury, Black Gingham, Bookstack as expected |
| Search | cherries returns the imported cherry keychain with local image and pending price, then opens its detail page |
| Gallery | Cherry detail changes from source photo 1 to photo 2; zoom opens the same selected image and closes correctly |
| Localisation/layout | Accessory root, Jewellery subcollection and cherry detail × EN/AR × actual document widths 375/768/1440 px = 18 cases; no horizontal overflow; correct lang and direction |
| Mobile navigation | Mobile menu → Accessories → Jewellery opens populated 6-product page |
| Existing demo cart | Pulse massager × 1 = £79 persists when navigating into accessories |

Widths were measured inside iframes with outer sizes 390/783/1455 px and 15 px scrollbars. These are browser CSS checks, not physical-device or certified accessibility tests. A later mobile-only CSS density adjustment hides the decorative intro image/long marketing copy while retaining title, category controls and all products; final 375 px layout was rechecked after this adjustment: all category controls remain visible, the first product row appears in the initial view, and document width/scroll width both equal 375 px.

The provided Taxicab product link remains 404; no Taxicab item has been fabricated. The source shop's stock, USD retail prices and marketing claims were not promoted into NOVA WELL offers. Supplier identity, sellable specifications, rights, commercial prices, stock, payments, shipping and returns still require operator confirmation.

The local preview server does not apply Cloudflare response headers. Remote CI and Cloudflare preview deployment outcomes are reported in the PR, separately from these local checks. No merge into main is performed in this task.
