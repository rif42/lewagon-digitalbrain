# lewagon-digitalbrain

Hybrid Obsidian vault + Quartz site — powered by [Quartz v5](https://quartz.jzhao.xyz).

- **`notes/`** — Obsidian vault (source of truth). Edit all content here.
- **`quartz/`** — Quartz static-site builder, isolated in a subfolder and hidden from Obsidian via `quartz/**` (`Settings → Files and links → Excluded files`). Do not edit `quartz/content/` directly.
- **`quartz/content/`** — build-time mirror of `notes/`, populated by the sync script.
- **`scripts/`** — `sync-content.sh` / `sync-content.bat` helpers.

## Quick commands (npm)

```bash
# sync vault → quartz/content + build locally
npm run sync
npx --prefix quartz quartz build --serve
# → http://localhost:8080

# publish (auto-deploy via GitHub Actions)
git add -A && git commit -m "update notes" && git push
# → Actions builds quartz/public → deploys to GitHub Pages
```

## Site

- GitHub Pages: `https://rif42.github.io/lewagon-digitalbrain/` (Source: GitHub Actions)
- Quartz config: `quartz/quartz.config.yaml` (`baseUrl: rif42.github.io/lewagon-digitalbrain`, `enableSPA: true`)
- Ignore patterns in `quartz/.gitignore` and repo `.gitignore`: `quartz/.quartz-cache`, `quartz/public`, `.obsidian/workspace.json`, `.obsidian/hotkeys.json`

## Tooling

- Node 22+ / npm 10.9.2+ (`node -v` / `npm -v` — you have 24.12 / 11.6.2)
- Use **npm** (not bun) for Quartz: `npm ci` inside `quartz/`, `npx quartz ...` for CLI.

## Repo layout

```
lewagon-digitalbrain/          # git root + Obsidian vault root
├── .obsidian/                 # vault config (with quartz/** excluded via app.json)
├── .github/workflows/deploy.yml
├── notes/                     # ← edit here in Obsidian (source of truth)
│   ├── index.md
│   ├── knowledge_bank/
│   ├── project/
│   ├── socmed/
│   └── trip/
├── quartz/                    # ← Quartz site builder (hidden from Obsidian)
│   ├── quartz.config.yaml     # ← derived from obsidian template, baseUrl set
│   ├── content/               # ← populated by sync script, not edited directly
│   └── public/                # ← build output, gitignored, deployed as artifact
├── scripts/sync-content.sh
├── scripts/sync-content.bat
├── .gitignore
├── package.json               # root: npm run sync
└── QUARTZ_DEPLOYMENT_PLAN.md
```
