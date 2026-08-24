# lewagon-digitalbrain — repo + vault conventions

Hybrid repo: Obsidian vault at the git root; static site via Quartz in `quartz/` (hidden from Obsidian).

## Layout

- `notes/` — source of truth, edited in Obsidian (published as-is — no filtering). Contains `index.md`, `knowledge_bank/`, `project/`, `socmed/`, `trip/`, and `AGENTS.md` (the operator skill doc inside `notes/`).
- `quartz/` — Quartz v5 site builder. Do **not** edit `quartz/content/` directly; it is wiped and refilled from `notes/` on every build/preview. Configuration is `quartz/quartz.config.yaml` (derived from the `obsidian` template, `baseUrl: rif42.github.io/lewagon-digitalbrain`, `enableSPA: true`).
- `.obsidian/app.json` — has `userIgnoreFilters: ["quartz/**"]` so Quartz files never appear in Obsidian.
- `.gitignore` — ignores `.obsidian/workspace.json`, `.obsidian/hotkeys.json`, `Thumbs.db`, `.DS_Store`, plus `quartz/.quartz-cache` and `quartz/public`.
- `scripts/sync-content.*` — mirrors `notes/` → `quartz/content/` (with `notes/index.md` → `quartz/content/index.md` fallback).
- Root `package.json` exposes `npm run sync` which invokes the sync script; use **npm** for Quartz (root and `quartz/` both use `npm ci` + `npx quartz ...`).

## Quartz deployment

- GitHub Pages (public repo) via `.github/workflows/deploy.yml` (Actions → Pages). Workflow runs on `push` to `main` + `workflow_dispatch`; inside `quartz/` it does `npm ci` → sync script → `npx quartz build` → upload `quartz/public`.
- Repo Pages source is `Build and deployment → Source: GitHub Actions`.
