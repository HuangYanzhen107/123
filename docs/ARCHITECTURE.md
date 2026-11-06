# Prototype architecture

| Area | Current implementation | Future extension |
| --- | --- | --- |
| `/` | Original storefront, demo catalog, filters, EN/AR, cart drawer | Catalog components and independent language URLs |
| `/collections/massage-devices/` | Bilingual category hub | Data-driven categories, verified filters |
| `/products/pulse-massage-gun/` | Bilingual sample detail and shared cart | Verified SKU/variants, product media |
| `/guides/choose-a-massager/` | Bilingual illustrative guide | Reviewed localized editorial content |
| `/#bag` | Demo quantities per known product, browser storage, blocked checkout | Server-validated pricing and eligible hosted checkout later |
| `/admin-demo/` | EN/AR editor UI, English sample content, local draft and JSON export | Authenticated roles, shared database, audit and publishing |
| `assets/cart.js` | Bounded demo cart schema shared across routes | Real cart API after transactional requirements are met |
| `assets/locales.js` + `localization.js` | Inner-page text/attribute localization and RTL | Component-owned translation keys and reviewer-approved Arabic |
| `.github/` | CI workflow and PR template | Plan-supported enforced reviews/checks after setup |
| `scripts/build.mjs` | Explicit public-asset allowlist to `dist/` | Framework build if later needed |

Only three fictional demo products exist. No real massage-device data, customers, accounts, order processing, shipping, analytics or payment APIs are connected. The admin edits do not modify the storefront and do not sync across devices. Sample product content in the editor remains English intentionally; translating the editor UI does not rewrite a merchant's draft.

The current language switch is a development feature, not completed multilingual SEO. Pages remain noindex. Future backend services, database bindings, factory integrations and secret storage are planning items only.
