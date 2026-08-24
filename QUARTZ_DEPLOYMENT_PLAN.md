# Notes + Repo + Deployment Hybrid — Quartz on GitHub Pages

> Vault: `E:\work\lewagon-digitalbrain` · Source: `notes/` · Site builder: `quartz/` (isolated subfolder, hidden from Obsidian) · Deploy: GitHub Actions → GitHub Pages

## Assumptions (from your answers)

- **Visibility:** public repo, everything in `notes/` is publishable — fastest path, no filtering needed for v1.
- **Hosting:** GitHub Pages (free, native Quartz path, URL `https://<username>.github.io/<repo>/`).
- **Quartz isolation:** Quartz lives in `quartz/` subfolder hidden from Obsidian via `Settings → Files and links → Excluded files → quartz/**` so you never see build files in the app.

---

1. Prepare hybrid repo structure and hide Quartz from Obsidian
   - Init git at `E:\work\lewagon-digitalbrain`, create `.gitignore` ignoring `.obsidian/workspace.json`, `.obsidian/hotkeys.json`, OS files (`Thumbs.db`, `.DS_Store`), and `quartz/.quartz-cache` + `quartz/public`
   - Keep `notes/` fully tracked; add root `README.md` + `AGENTS.md` explaining `notes/` is vault source, `quartz/` is site builder
   - Configure Obsidian exclusion: `Settings → Files and links → Excluded files → quartz/**` (persists to `.obsidian/app.json` `userIgnoreFilters`) — verify Quartz disappears from Obsidian explorer but stays on disk
   - Decide content mapping: source of truth remains `notes/` at vault root; Quartz reads from `quartz/content/` (not directly from `notes/`) to avoid duplicate-file confusion in Obsidian

2. Install Quartz in isolated `quartz/` subfolder and wire vault content
   - Verify toolchain: `node -v` / `npm -v` / `npx` (you have 24.12 / 11.6.2)
   - Run `npm create quartz@latest` targeting `./quartz` (or `npx quartz create` inside `quartz/`) — choose **Empty Quartz** template, keep it self-contained in `quartz/`
   - Configure `quartz/quartz.config.ts`: set `pageTitle`, `baseUrl = "<username>.github.io/<repo>"`, `ignorePatterns` if needed, `enableSPA: true`
   - Create sync script at repo root `scripts/sync-content.sh` (and `scripts/sync-content.bat` for Windows): `rm -rf quartz/content/* && cp -r notes/* quartz/content/` + copy `notes/index.md` → `quartz/content/index.md`; add `npm run sync` wrapper in root `package.json`
   - Test locally: `npm run sync && npx quartz build --serve` inside `quartz/` → verify `http://localhost:8080` renders all notes, fix broken wikilinks/assets before pushing

3. Push to GitHub and enable GitHub Pages auto-deploy via Actions
   - Create public repo: `gh repo create lewagon-digitalbrain --public --source=. --push` (or manual `git remote add origin <url>` + `git push -u origin main`)
   - Add workflow at repo root `.github/workflows/deploy.yml` (not inside `quartz/`): checkout → setup Node 22 → `npm ci` in `quartz/` → run `../scripts/sync-content.sh` → `npx quartz build` → `actions/upload-pages-artifact` with `quartz/public` → `actions/deploy-pages`
   - Repo settings: `Settings → Pages → Build and deployment → Source: GitHub Actions`; `Settings → Actions → General → Workflow permissions: Read and write`
   - Workflow triggers: `on: push: branches: [main]` + `workflow_dispatch`; confirm `quartz.config.ts` `baseUrl` matches actual repo name before first push

4. Verify end-to-end and polish
   - Push initial commit to `main`, watch Actions run, confirm deployed URL `https://<username>.github.io/<repo>/` loads content from `notes/`
   - Test live edit loop: edit note in Obsidian → `git add/commit/push` → Action rebuilds → site updates in ~1–2 min; add deploy status badge to `README.md`
   - Optional follow-ups (post-MVP): custom domain via `quartz.config.ts` + `CNAME` + Pages custom domain setting; exclude drafts via `draft` frontmatter; add `quartz sync` pre-commit hook to catch broken links locally

---

## Repo layout after setup

```
lewagon-digitalbrain/          # git root + Obsidian vault root
├── .obsidian/                 # vault config (with quartz/** excluded)
├── .github/workflows/deploy.yml
├── notes/                     # ← edit here in Obsidian (source of truth)
│   ├── index.md
│   ├── knowledge_bank/
│   ├── project/
│   ├── socmed/
│   └── trip/
├── quartz/                    # ← Quartz site builder (hidden from Obsidian)
│   ├── quartz.config.ts
│   ├── content/               # ← populated by sync script, not edited directly
│   └── public/                # ← build output, gitignored, deployed as artifact
├── scripts/sync-content.sh
├── scripts/sync-content.bat
├── .gitignore
└── QUARTZ_DEPLOYMENT_PLAN.md  # this file
```

## Quick commands

```bash
# first-time local preview
npm run sync
cd quartz && npx quartz build --serve

# publish
git add -A && git commit -m "update notes" && git push
# → GitHub Action builds + deploys automatically
```
