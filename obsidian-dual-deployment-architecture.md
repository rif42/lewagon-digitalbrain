# Obsidian Dual-Deployment Architecture (Public & Internal)

## 1. Overview & Architecture

A zero-maintenance, $0/month architecture for hosting a single Obsidian vault with split access:
- **Public Audience**: Strictly filtered subset of notes (`publish: true`).
- **Internal Team (3 users)**: Full vault access gated behind Cloudflare Zero Trust (Access).

```
                      [ Private GitHub Repository ]
                        (Single Source of Truth)
                                   │
                  Push to main / Scheduled Workflow
                                   │
            ┌──────────────────────┴──────────────────────┐
            ▼                                             ▼
   [ Pipeline A: Public ]                       [ Pipeline B: Internal ]
   - Strip non-published notes                  - Build full vault
   - Quartz: `ExplicitPublish()`               - Quartz: Default build
   - Deploy: GitHub Pages / CF Pages            - Deploy: Cloudflare Pages
   - Access: Public                             - Access: Cloudflare Zero Trust
                                                          (Email OTP / SSO)
```

---

## 2. Directory & Frontmatter Conventions

### 2.1 Frontmatter Rules
Notes are private by default. Only notes containing explicit public frontmatter are emitted to the public target.

```yaml
---
title: Public API Reference
publish: true
---
```

### 2.2 Asset Security Caution
Quartz emits attachments (images, PDFs) found in `content/` by default. Do not store sensitive private attachments in the same media folder if using naive builds. Keep private attachments isolated or sanitize the build directory during CI.

---

## 3. Quartz Configuration

### `quartz.config.ts` (Public Target)
Activate `ExplicitPublish` to block any markdown file lacking `publish: true`:

```typescript
// quartz.config.ts
plugins: {
  transformers: [
    // ... standard transformers
  ],
  filters: [
    Plugin.ExplicitPublish(), // Drops files without `publish: true`
  ],
  emitters: [
    Plugin.ContentPage(),
    Plugin.FolderPage(),
    Plugin.TagPage(),
    Plugin.ContentIndex(),
    Plugin.Assets(),
    // ...
  ],
}
```

### `quartz.layout.ts` (Public UI Hardening)
Remove search, explorer, and graph if you only expose isolated pages to prevent structural probing:

```typescript
// quartz.layout.ts
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.Breadcrumbs(),
    Component.ArticleTitle(),
    Component.ContentMeta(),
  ],
  left: [
    Component.PageTitle(),
    // Component.Search(),   // Disabled to prevent indexing leaks
    // Component.Explorer(), // Disabled to prevent directory inspection
  ],
  right: [
    // Component.Graph(),    // Disabled
    Component.DesktopOnly(Component.TableOfContents()),
  ],
}
```

---

## 4. CI/CD Deployment Pipeline (`.github/workflows/deploy.yml`)

Using GitHub Actions to build both targets avoids hitting Cloudflare Pages' 500 build/month free tier limit via direct upload (`wrangler`).

```yaml
name: Deploy Dual Quartz Sites

on:
  push:
    branches: [ main ]

jobs:
  deploy-public:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Vault
        uses: actions/checkout@v4

      - name: Setup Node & Bun
        uses: oven-sh/setup-bun@v1

      - name: Install & Build Public
        run: |
          bun install
          # Build using ExplicitPublish config
          npx quartz build --bundleInfo

      - name: Deploy Public to Cloudflare Pages
        uses: cloudflare/wrangler-action@v3
        with:
          apiToken: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          accountId: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}
          command: pages deploy public --project-name=my-public-docs

  deploy-internal:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Vault
        uses: actions/checkout@v4

      - name: Setup Node & Bun
        uses: oven-sh/setup-bun@v1

      - name: Configure Internal Quartz
        run: |
          # Swap filter to RemoveDrafts (or disable filter) to include all notes
          sed -i 's/Plugin.ExplicitPublish()/Plugin.RemoveDrafts()/' quartz.config.ts
          bun install
          npx quartz build --bundleInfo

      - name: Deploy Internal to Cloudflare Pages
        uses: cloudflare/wrangler-action@v3
        with:
          apiToken: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          accountId: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}
          command: pages deploy public --project-name=my-internal-docs
```

---

## 5. Cloudflare Zero Trust (Access Setup)

Protect the internal deployment (`my-internal-docs.pages.dev`) via Cloudflare Access:

1. **Navigate**: Cloudflare Dashboard → Zero Trust → Access → Applications.
2. **Add Application**: Select **Self-hosted**.
3. **Application Configuration**:
   - **Application Name**: `Internal Knowledge Base`
   - **Application Domain**: `internal-docs.yourdomain.com` (or `*.pages.dev` subdomain).
4. **Define Policy**:
   - **Action**: `Allow`
   - **Rule Type**: `Include`
   - **Selector**: `Emails` or `Emails Ending in` (e.g., specific user emails or `@yourteam.com`).
5. **Authentication Method**:
   - One-Time PIN (OTP sent to user email) or Google OAuth / GitHub SSO.

---

## 6. Cost & Limits Audit (3-Person Team)

| Metric | Cloudflare Free Limit | Actual Usage (Est.) | Headroom |
|---|---|---|---|
| **Bandwidth** | Unlimited | < 5 GB / month | Infinite |
| **Auth Seats (Zero Trust)** | 50 seats free | 3 seats | 47 seats left |
| **Build Limits (Direct Upload)** | Unlimited via `wrangler` | ~20–50 builds / day | Infinite |
| **Git-Integrated Builds** | 500 / month | 0 (offloaded to GHA) | 500 / month |
| **Asset Size Limit** | 25 MB per file | < 5 MB typical | Safe |
| **Total Monthly Cost** | **$0.00** | **$0.00** | **Free forever** |

---

## 7. Security Hardening Checklist

- [ ] **Repository Privacy**: Private repository; never make the source repo public.
- [ ] **Search Index Verification**: Check `public/static/contentIndex.json` in the public output to verify internal slugs/titles are not present.
- [ ] **Orphaned Media Check**: Ensure private attachments (images, PDFs) referenced only by private notes are not copied into the public `public/` directory.
- [ ] **Access Session Duration**: Set Cloudflare Access session timeout to 7–30 days to avoid constant OTP prompts for internal members.
