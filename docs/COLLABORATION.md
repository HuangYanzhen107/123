# Collaboration and previews

> Current theme update (2026-11-02): the existing public preview https://nova-well-store.pages.dev/ has been opened successfully. Later edits to this document are historical setup notes. The new boutique theme is delivered through a feature branch and PR, not asserted deployed. See `UK-NORDIC-LAUNCH.md` and `THEME-VALIDATION.md` for current scope and verification.

## Repository setup

Private repository created: https://github.com/xueguangbin380-afk/nova-well-store . The stable branch is `main`; source is uploaded at the root with its subdirectories preserved. Cloudflare integration still requires official sign-in. Do not upload passwords, tokens, customer data or real product materials.

Add actual developers from repository Settings → Collaborators. The owner must select and verify the intended GitHub usernames. No invitations have been sent. Testers only need the eventual public website URL.

## Development flow

1. Branch from `main` using `feature/<short-description>` or `fix/<short-description>`.
2. Change code and run `python3 scripts/verify_site.py`, `node --test scripts/cart.test.cjs`, and `node scripts/build.mjs`.
3. Open a Pull Request into `main`; fill in the included template.
4. After Cloudflare Git integration is connected, inspect its actual preview URL and the GitHub check results.
5. Another developer reviews desktop/mobile, English/Arabic and demo cart behavior. Merge only after acceptance. `main` deploys to production automatically after Cloudflare setup.
6. To undo a bad change, revert the merged commit with a new reviewed PR. Cloudflare production deployment rollback is an additional recovery option; align source afterwards.

The included `Site checks` workflow has read-only repository permissions and uses no deployment secrets. It has not run on GitHub until the repository is created and pushed. Private-repository Actions usage is subject to the account's included allowance; keep paid usage disabled if remaining on a free plan.

## Branch protection limitations

GitHub's current documentation lists enforced private-repository protected branches under Pro/Team/Enterprise. Free private repositories still support the branch/PR collaboration convention, but this file and PR template do **not** technically enforce it. Never make the repository public to obtain this feature. Check the owner's plan before configuring required reviews/checks. No paid upgrade is authorized or needed for this first preview.

## Cloudflare Pages configuration (pending account authorization)

Use **Git integration**, not Direct Upload and not a Workers-only project.

| Setting | Value |
| --- | --- |
| Repository visibility | Private |
| Production branch | `main` |
| Framework | None |
| Build command | `node scripts/build.mjs` |
| Build output directory | `dist` |
| Root directory | Repository root |
| Preview branch deployments | Enable development branches |
| Payment and cloud secrets | None |

The build copies only HTML, CSS, JS, `robots.txt` and `_headers` to `dist`. Handover notes, source instructions, tests and CI files are not published. `_headers` disables indexing, outbound connections and form submission in the hosted demo. This is not authentication: the public demo admin contains only a local product-content editor.

Verify the actual Cloudflare deployment state and displayed `*.pages.dev` URL before sharing. Validate noindex/CSP headers and routes on the deployed host; the local preview server does not apply Cloudflare `_headers`.

## Official references checked on 2026-11-01

- https://developers.cloudflare.com/pages/framework-guides/deploy-anything/
- https://developers.cloudflare.com/pages/get-started/git-integration/
- https://developers.cloudflare.com/pages/configuration/preview-deployments/
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches

