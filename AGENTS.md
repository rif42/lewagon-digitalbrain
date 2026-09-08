# lewagon-digitalbrain — repo + vault conventions

Hybrid repo: Obsidian vault at the git root; static site via Quartz in `quartz/` (hidden from Obsidian).

## Layout

- `notes/` — source of truth, edited in Obsidian. Only notes with `publish: true` frontmatter reach the public site (`ExplicitPublish` filter); everything else is dropped at build. Contains `index.md`, `knowledge_bank/`, `project/`, `socmed/`, `trip/`, and `AGENTS.md` (the operator skill doc inside `notes/`).
- `quartz/` — Quartz v5 site builder. Do **not** edit `quartz/content/` directly; it is wiped and refilled from `notes/` on every build/preview. Configuration is `quartz/quartz.config.yaml` (derived from the `obsidian` template, `baseUrl: rif42.github.io/lewagon-digitalbrain`, `enableSPA: true`).
- `.obsidian/app.json` — has `userIgnoreFilters: ["quartz/**"]` so Quartz files never appear in Obsidian.
- `.gitignore` — ignores `.obsidian/workspace.json`, `.obsidian/hotkeys.json`, `Thumbs.db`, `.DS_Store`, plus `quartz/.quartz-cache` and `quartz/public`.
- `scripts/sync-content.*` — mirrors `notes/` → `quartz/content/` (with `notes/index.md` → `quartz/content/index.md` fallback).
- Root `package.json` exposes `npm run sync` which invokes the sync script; use **npm** for Quartz (root and `quartz/` both use `npm ci` + `npx quartz ...`).

## Quartz deployment

- GitHub Pages (public repo) via `.github/workflows/deploy.yml` (Actions → Pages). Workflow runs on `push` to `main` + `workflow_dispatch`; inside `quartz/` it does `npm ci` → sync script → `npx quartz build` → upload `quartz/public`.
- Repo Pages source is `Build and deployment → Source: GitHub Actions`.
- Public allowlist: `quartz/quartz.config.yaml` has `explicit-publish: enabled: true`, so only `publish: true` notes emit (currently `notes/index.md` shell + `notes/knowledge_bank/Bali Events List.md`). Explorer/search/graph are disabled on public. Private attachments never reach `quartz/public/`: `ignorePatterns` covers `socmed`, `trip`, `project`, `notionscrape`, `knowledge_bank/instagram_raw`, plus `**/*.mhtml` and `**/*.pdf` — filters only gate markdown, so new attachment dirs must be added here.

## Bali Events List — calendar (`notes/knowledge_bank/Bali Events List.md`)

Single file is the source of truth — calendar is inline HTML/JS + FullCalendar 6.1.15 via jsDelivr CDN, no `quartz/` edits, no extra npm deps. The note survives `notes/` → `quartz/content/` sync verbatim.

### Data sources (favolist + frontmatter `sources:`)

- `https://www.nowbali.co.id/all-events/?month=August` + `?month=September` — NOW! Bali Events Calendar (paginated by month, 5 + 2 events in Aug 2026). Detail pages at `https://www.nowbali.co.id/upcoming-events/<slug>/`.
- `https://bali.com/events-calendar/` + `https://bali.com/nightlife/` — perennial guides, no dated events in Aug/Sep window; keep weekly entries `w1`–`w4` (FINNS, Old Man's, Savaya, La Favela) with next occurrence in `schedule`.
- `https://favolist.notion.site/1e969801bbdf80c3843fc98864b663e1` — **Bali Bootcamp Events** Notion DB (public). The canvas URL the user shared (`https://app.notion.com/p/favolist/...?v=1e969801bbdf802dbb48000ceb92a256`) redirects there. Schema: `Event Name` (title) · `Event Type` (select) · `Start Date & Time` (date, `Asia/Singapore`) · `Location` (URL, often `maps.google.com`) · `Description` · `Cost` · `RSVP Needed` · `Event URL` · `Meeting Point`.
  - Collection: `1e969801-bbdf-80e7-8a2c-000b08442ada` (space `0fbdf48d-e926-47c1-968c-e574b09dad21`), calendar view `1e969801-bbdf-80c0-9468-000cff3a1708`, **All Events** table view `1e969801-bbdf-80fd-9479-e632cdf77811` (the view saved in the `.mhtml` snapshot). Query via `POST https://favolist.notion.site/api/v3/queryCollection` (no auth) — see recipe below.
- `notes/knowledge_bank/Bali Bootcamp Events _ All Events _ Notion.mhtml` — **archived snapshot** of the same Notion DB (`All Events` view, saved `Fri 28 Aug 2026 16:54 +08:00` from `https://app.notion.com/p/favolist/1e969801bbdf80c3843fc98864b663e1?v=1e969801bbdf802dbb48000ceb92a256`). Contains 33 rendered table rows (00–32 in `temp_mhtml`). Primary event source URLs inside the snapshot are `g.co`, `maps.app.goo.gl`, `bit.ly`, `meetup.com`, `eventbrite.com`, `itsocialevent.com`, `samadibali.com`, `megatix.com.au`, `nomeo.io`, `chat.whatsapp.com`, `docs.google.com` — see `## Notes & Sources` in the list file for the dated extract. Useful as offline fallback when the live Notion API is unavailable; parse with `email.policy` + `BeautifulSoup` (recipe below).
- `https://nomeo.co` — Cloudflare JS challenge, consistently 301/403 for both `crawl4ai` and plain `requests`/`curl`. Skip unless using Playwright stealth + proxy; fall back to its Instagram mirror.
- Per-event `source` field should point to the crawlable canonical URL (NOW! Bali detail, Bali.com page, or `https://favolist.notion.site/<Slug>-<id>`). For favolist rows, `Event URL` + `Location` columns already carry the per-event source — copy them verbatim.

### How to refresh — search → filter → edit → verify (rolling 2-week window)

1. **Pick window:** `window_start = today in WITA (Asia/Makassar, UTC+8)` at 00:00, `window_end = window_start + 14 days` inclusive. Frontmatter `window_start`/`window_end` and `#bali-calendar` `data-window-start`/`data-window-end` + FullCalendar `validRange`/`initialDate` must all match. Also update header `> **Window: …**` and `crawl_date`/`updated`.
2. **Crawl public sites (fresh):** with `crawl4ai` MCP `crawl_url(url, fresh=True)`:
   ```text
   crawl_url("https://www.nowbali.co.id/all-events/?month=August", fresh=True)
   crawl_url("https://www.nowbali.co.id/all-events/?month=September", fresh=True)
   crawl_url("https://bali.com/events-calendar/", fresh=True)
   crawl_url("https://bali.com/nightlife/", fresh=True)
   # then each detail URL found (SAYA, Michelin Master Series, Stroberi, etc.)
   ```
   Keep `fresh=True` to bypass crawl4ai's file cache; collect dated `start` strings from the list/detail pages.
3. **Query favolist Notion DB** — three options (the DB is JS-rendered, so `crawl_url` alone returns a shell):
   - **A. Live API POST (deterministic, preferred for refreshes):**
     ```json
     POST https://favolist.notion.site/api/v3/queryCollection
     {"collection":{"id":"1e969801-bbdf-80e7-8a2c-000b08442ada","spaceId":"0fbdf48d-e926-47c1-968c-e574b09dad21"},
      "collectionView":{"id":"1e969801-bbdf-80c0-9468-000cff3a1708","spaceId":"0fbdf48d-e926-47c1-968c-e574b09dad21"},
      "loader":{"userTimeZone":"Asia/Singapore","sort":[],"reducers":{"calendar_results":{
        "type":"results",
        "filter":{"operator":"and","filters":[
          {"property":"fja;","filter":{"operator":"date_is_on_or_after","value":{"type":"exact","value":{"type":"date","start_date":"<window_start YYYY-MM-DD>"}}}} ,
          {"property":"fja;","filter":{"operator":"date_is_on_or_before","value":{"type":"exact","value":{"type":"date","start_date":"<window_end YYYY-MM-DD>"}}}}
        ]},"limit":5000}}}}
     ```
     Property id `fja;` = `Start Date & Time`. Map each returned block's `properties` → event: `title[0][0]`, `hP[[` (Event Type), `fja;` (datetime), `~N?o` (Description), `~xjM` (Location URL), `PMXu` (Event URL), `fWMC` (Cost). Any view id from the DB works when you keep the same `collection` — `1e969801-bbdf-80c0-9468-000cff3a1708` (calendar), `1e969801-bbdf-80fd-9479-e632cdf77811` (All Events table) etc. share the same `calendar_results` reducer.
   - **B. Offline `.mhtml` fallback (no network, archived 28 Aug 2026):** the repo ships `notes/knowledge_bank/Bali Bootcamp Events _ All Events _ Notion.mhtml` (the `All Events` view, 33 rows). Parse it locally:
     ```python
     from email import policy; from email.parser import BytesParser; pathlib.Path(mhtml).read_bytes()
     msg = BytesParser(policy=policy.default).parsebytes(data)  # walk to text/html part, decode
     from bs4 import BeautifulSoup
     soup = BeautifulSoup(html, "lxml")
     rows = soup.find_all("div", class_=lambda c: c and "notion-table-view-row" in c)  # 33 rows in Aug 28 snapshot
     # or: soup.find_all("div", class_=lambda c: c and "notion-collection-item" in c)
     for row in rows:
         bid = row.find_parent("div", attrs={"data-block-id": True}).get("data-block-id")
         text = row.get_text(" | ", strip=True)  # "Event Name | Event Type | Start Date & Time | ... | Cost | RSVP | Event URL"
         links = [a["href"] for a in row.find_all("a", href=True)]  # per-event source URLs live here
         # date cell: re.search(r"(Jan|Feb|…)\s+\d{1,2},?\s*\d{4}", text)
     ```
     Text uses ` | ` between columns; dates like `May 9, 2025 13:00 → 15:00` or `NO DATE` for weeklies. Source domains in the snapshot: `g.co`, `maps.app.goo.gl`, `bit.ly`, `meetup.com`, `eventbrite.com`, `itsocialevent.com`, `samadibali.com`, `megatix`, `nomeo.io`, `chat.whatsapp.com`, `docs.google.com`.
   - **C. Playwright capture (exploration):** launch Chromium, `page.goto("https://favolist.notion.site/1e969801bbdf80c3843fc98864b663e1?v=1e969801bbdf80c09468000cff3a1708")`, intercept `api/v3/queryCollection` responses and parse `recordMap.block` + `reducerResults.calendar_results.blockIds`.
4. **Filter to window (WITA):** keep events where `start_date` ∈ `[window_start, window_end]`. Drop past events (e.g. Aug 27 Purnama when window starts Aug 28) and events strictly beyond `window_end` (e.g. Sep 12 Celebrate Wellness when window ends Sep 11). Weekly recurrences (`w*`) stay outside the date filter but update `schedule` to the next occurrence(s) falling in the window.
5. **Edit the file:** (a) frontmatter `window_start`/`window_end`/`updated`/`crawl_date`/`window_note`/`sources`; (b) the two `data-window-*` attrs; (c) the JSON block `<script type="application/json" id="bali-events">` — preserve id ordering and anchor scheme; (d) FullCalendar `initialDate` (≈ first dated event) + `validRange`; (e) `## Notes & Next Steps` + `## Sources` sections with per-source crawl status (✓ / blocked) and what changed (added/dropped).
6. **Validate + deploy:** `npm run sync` → `bash -c 'cd quartz && npx quartz build'` should report `Parsed ~733 Markdown files` / `Emitted ~1001 files` with no error; `quartz/public/knowledge_bank/bali-events-list.html` must contain `bali-calendar` + `FullCalendar` and still contain `Overview`. Push to `main` deploys via `.github/workflows/deploy.yml`.

### Editing rules (shapes, anchors, colors)

- **Edit the JSON block** `<script type="application/json" id="bali-events">` near the top. It is the canonical data; the Overview table + `## 1)…` detail sections below are the `<noscript>`/Obsidian fallback — keep them in sync.
- **Dated event** shape: `{"id","name","location","description","start","finish","category","cost","source","recurring":false,"anchor"}`. `start`/`finish` are WITA ISO 8601 with offset: `YYYY-MM-DDTHH:mm:ss+08:00` (e.g. `2026-08-28T18:00:00+08:00`). `finish` may be `null` for single-moment events. Multi-day events (e.g. #3 `2026-08-28T19:30` → `2026-08-29T22:00` or #10 Sep 5 16:00 → Sep 6 22:00) use one object with `end` spanning both days — FullCalendar renders the bar across them.
- **Weekly/recurring** shape: `{"id":"w1","name","location","description","schedule","category","cost","source","recurring":true}` — shown in `#bali-weekly-strip` below the grid, not as calendar cells. `schedule` should name the next date(s) in the current window (e.g. `Every Wed 19:00–Thu 01:00 (Sep 2/9 — next in window)`).
- **`anchor`** must match the Quartz heading slug for the detail section (Quartz slugifies `## 3) …` → `3-the-michelin-…`; `—` becomes `--`, so `—` in titles → `--` in anchor). Clicking a calendar event opens the modal and "Jump to details" scrolls to `## N)`.
- **Category colors** are mapped in `catColor()` in the inline script: Dining/Culinary/Brunch/Talk → `#284b63`, Fashion → `#7b5ea7`, Music/Concert → `#c17c3a`, Wellness/Sport → `#4a9a7b`, Nightlife/Club/Party/Beach → `#5a6e7f`. Add new categories there if needed.
- **Favolist-specific notes:** Notion dates are in `Asia/Singapore` (UTC+8, same as WITA). If `Location` is only a `maps.google.com/?cid=…` link, use the event name's Notion page (`https://favolist.notion.site/<Slug>-<id>`) as `source` and keep the maps link inside `location`. `Cost`/`RSVP` may be empty.
