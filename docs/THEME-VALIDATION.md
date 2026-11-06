# Everyday boutique theme — actual validation

Date: 2026-11-02 (Asia/Shanghai).

## Scope

Original editorial boutique interface for the UK, Ireland and Nordic planning markets. Eight fictional product concepts, five collection routes, nine information routes, refreshed original guide and 404. The existing browser-only admin is retained separately. All old product routes and the three original cart SKUs remain supported.

## Checks completed locally

| Check | Actual result |
| --- | --- |
| Static verification | 26 HTML pages: local links, noindex, viewport, inline and external JS syntax passed |
| Cart unit tests | Corrupted storage, known IDs, bounded integers, blocked storage and persistence passed |
| Catalogue tests | Variant uniqueness, distinct apparel sizes, legacy SKUs, rendered routes/assets, demo-only controls, build exclusion and encoded subcategory URLs passed |
| Build | Allowlisted `dist/`; no source instructions, docs, CI, local preview configuration or QA harness in the final build |
| Desktop visual review | Home and product experience inspected in cloud Chromium; original hero image loads |
| Responsive layout | Home, collection, product, shipping and guide × EN/AR × 4 widths = 40 cases. Actual document client widths 360, 375, 753 and 1425 px (iframe outer widths 375/390/768/1440 minus 15 px scrollbar). No horizontal overflow; correct language and direction |
| Mobile visual review | Home inspected in a 390 px outer iframe (375 px document area); not a physical device test |
| Mobile navigation | Open menu, expand Accessories, follow subcategory link tested. An ampersand query-encoding bug was found and fixed; corrected URL selects only the bag charm |
| Search | `jumper` returns the matching product and navigates to its detail route |
| Product & bag | Size M × 2 adds at £108; increment to 3 updates £162; reload retains 3; another route retains same variant; Sweden price preview updates subtotal; remove restores empty bag |
| Collection | Encoded subcategory preset and low-to-high sorting tested |
| Localisation | English → Arabic changes visible controls, copy, direction and currency format; English restored |
| Privacy control | Clear preview data button confirms removal; includes the exact legacy editor storage key |
| Checkout | Disabled; no address/payment form or customer submission endpoint added |

The temporary local QA pages were never source deliverables and were removed by the final clean build. The managed preview needed a restart to see newly added QA files; this was a preview snapshot refresh, not a production failure.

## Not claimed as verified

- This document is not a certification of accessibility or legal compliance. Physical devices, assistive technology, every keyboard interaction and every product-gallery interaction have not been exhaustively tested.
- Preview has no real catalogue, inventory, orders, refunds, payment processor, CMS, shipping carrier, tax calculator or newsletter backend. Regional prices are synthetic display examples.
- The preview server does not apply Cloudflare `_headers`; deployed response headers, actual preview/production URLs, Cloudflare build status and rollback must be checked on the hosting service.
- GitHub CI status and any generated Cloudflare preview are reported separately in the PR; local success does not imply deployment success.
- No change is merged into `main` in this task: the repository collaboration instructions call for another contributor’s acceptance before merge.

See [UK/Nordic launch task brief](UK-NORDIC-LAUNCH.md) for researched official references and the remaining merchant inputs.
