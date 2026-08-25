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

## Bali Events List — calendar (`notes/knowledge_bank/Bali Events List.md`)

Single file is the source of truth — calendar is inline HTML/JS + FullCalendar 6.1.15 via jsDelivr CDN, no `quartz/` edits, no extra npm deps. The note survives `notes/` → `quartz/content/` sync verbatim.

- **Edit the JSON block** `<script type="application/json" id="bali-events">` near the top of the file. It is the canonical data; the Overview table + `## 1)…8)` detail sections below are the `<noscript>`/Obsidian fallback — keep them in sync.
- **Dated event** shape: `{"id","name","location","description","start","finish","category","cost","source","recurring":false,"anchor"}`. `start`/`finish` are WITA ISO 8601 with offset: `YYYY-MM-DDTHH:mm:ss+08:00` (e.g. `2026-08-27T20:00:00+08:00`). `finish` may be `null` for single-moment events. Multi-day events (e.g. #3 `2026-08-28T19:30` → `2026-08-29T22:00`) use one object with `end` spanning both days — FullCalendar renders the bar across them.
- **Weekly/recurring** shape: `{"id":"w1","name","location","description","schedule","category","cost","source","recurring":true}` — shown in `#bali-weekly-strip` below the grid, not as calendar cells.
- **`anchor`** must match the Quartz heading slug for the detail section (Quartz slugifies `## 3) …` → `3-the-michelin-…`; `—` becomes `--`, so `—` in titles → `--` in anchor). Clicking a calendar event opens the modal and "Jump to details" scrolls to `## N)`.
- **Category colors** are mapped in `catColor()` in the inline script: Dining/Culinary/Brunch/Talk → `#284b63`, Fashion → `#7b5ea7`, Music/Concert → `#c17c3a`, Wellness/Sport → `#4a9a7b`, Nightlife/Club/Party/Beach → `#5a6e7f`. Add new categories there if needed.
- **Verify locally:** `npm run sync` → `bash -c 'cd quartz && npx quartz build'` should report `Parsed 733 Markdown files` / `Emitted 1001 files` with no error; `quartz/public/knowledge_bank/bali-events-list.html` should contain `bali-calendar` + `FullCalendar` and still contain `Overview`. Push to `main` deploys via the workflow.
