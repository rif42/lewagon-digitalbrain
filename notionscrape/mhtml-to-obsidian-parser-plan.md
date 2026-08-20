# MHTML → Obsidian Markdown Parser Plan

Goal: convert the 100 Notion `.mhtml` snapshots in `notionscrape/` into a clean Obsidian vault with markdown-only notes and proper `[[wikilinks]]`.

> **Prototype scope:** Phases 1–3 are first run on **one** `.mhtml` file (recommend `A Guide to Pedagogical margin _ Notion.mhtml`) to validate extraction quality before any batch work. Phases 4–6 are for the full 100-file run.

---

## Recon Findings

- 100 files, ~279 MB total (largest 11 MB).
- Quoted-printable encoded; attributes split by soft line breaks (`=\r\n`). Must decode before HTML parsing.
- Main content lives inside `div.layout-content > div.notion-page-content`.
- Sidebar lives inside `.notion-outliner-shared`; every file contains the same shared tree, so hierarchy can be extracted once and merged across files.
- Block classes identified across corpus:

| Count | Type | Markdown mapping |
|---|---|---|
| 9884 | `page` | `[[Title]]` |
| 1025 | `text` | paragraph |
| 1000/85 | `numbered` / `numbered_list` | `1.` list |
| 941 | `collection_view_page` | `[[Title]]` (if page exists) or DB stub |
| 568 | `collection_view` | inline database → note + table rows |
| 400 | `gist` | fenced code block (gist embed) |
| 398 | `bulleted_list` | `-` list |
| 213 | `to_do` | `- [ ]` / `- [x]` |
| 169 | `image` | `![alt](url)` or `![[attachment]]` |
| 146 | `divider` | `---` |
| 143 / 127 / 58 | `sub_header` / `sub_sub_header` / `header` | `##` / `###` / `#` |
| 114 | `alias` | `[[Title]]` resolve |
| 106 | `code` | fenced code block |
| 100 / 45 | `column` / `column_list` | flatten sequentially with `---` separator |
| 95 | `toggle` | `<details>` / section header |
| 85 | `callout` | `> [!note]` callout |
| 58 | `header` | `#` |
| 22 | `table` | markdown table |
| 19 | `quote` | `>` blockquote |
| 12 | `button` | keep as link/text |
| 10 | `video` | link to video |
| 8 | `transclusion` / `transclusion_container` | resolve to wikilink |
| 5 | `table_of_contents` | skip (Obsidian has outline) |
| 5 | `bookmark` | bare URL |
| 3 | `unknown` | log + text fallback |
| 2 | `external_object_instance` | log + URL |
| 1 | `embed` | log + URL |

---

## Phase 1 — MHTML Decoding (prototype on 1 file)

1. Read `.mhtml` as bytes.
2. Parse the `Content-Type: multipart/related; boundary=...` header to get the MIME boundary.
3. Extract the part with `Content-Type: text/html`.
4. Decode `quoted-printable` using `quopri.decodestring()` (handles soft line breaks automatically).
5. Parse with `lxml` (tolerant of Notion's messy nesting).
6. Extract `Snapshot-Content-Location` → canonical page URL → UUID.
7. Extract `Subject` → fallback page title.
8. Verify that exactly one `.notion-page-content` exists.

Output: `BeautifulSoup` tree + page UUID + title.

---

## Phase 2 — Sidebar Hierarchy (extract once, merge across files)

1. Find `.notion-outliner-shared` containers.
2. Recursively walk `div[role=group]` + `a[role=treeitem]`.
3. For each treeitem, read:
   - `href` → extract 32-hex UUID from `app.notion.com/p/lewagon/<id>`.
   - title text from inner `.notranslate` div.
   - nesting depth from parent group nesting.
4. Build tree: `{id, title, children: [...]}`.
5. In the prototype run, extract the tree from the single sample file. For the full run, merge trees from all 100 files by UUID to recover collapsed subtrees.
6. Persist `out/pages/_hierarchy.json`.

---

## Phase 3 — Block Extraction & Markdown Render (prototype on 1 file)

Walk `.notion-page-content` children depth-first, dispatch on `notion-*-block` class.

### Per-block mapping

- **`page` / `collection_view_page`**: emit `[[title]]`; register child page in hierarchy.
- **`header` / `sub_header` / `sub_sub_header`**: `#` / `##` / `###` from inline text.
- **`text`**: paragraph. Preserve inline formatting: `strong` → `**`, `em` → `*`, `code` → `` ` ``, `s` → `~~`, `a[href]` → resolved link.
- **`bulleted_list`**: `-` item, indented by nesting depth.
- **`numbered_list`**: `1.` item, indented by nesting depth (sequential within sibling group).
- **`to_do`**: `- [ ]` or `- [x]` from checkbox state.
- **`toggle`**: `<details><summary>...</summary>` + rendered body. Or flatten to a `##` section if markdown/HTML details cause issues.
- **`code`**: fenced code block. Language from `data-lang` or class if available.
- **`callout`**: `> [!note]` (or `> [!warning]`, etc.) with nested body.
- **`quote`**: prefix each line with `>`.
- **`image`**: `![alt](src)`.
  - Most images are remote `app.notion.com/image/...` URLs that are likely auth-gated.
  - Decision: keep the URL in markdown, add URL to a report for optional later download.
- **`table`**: convert `.notion-table` div rows/columns to GitHub markdown table.
- **`column_list` / `column`**: render columns sequentially with `---` separator.
- **`collection_view`**: extract visible rows if rendered in DOM; otherwise emit `> [!warning] Database view not exported` plus the original URL.
- **`divider`**: `---`.
- **`alias` / `transclusion`**: resolve to wikilink.
- **`bookmark` / `video` / `embed`**: bare URL + note.
- **`table_of_contents`**: skip.
- **`unknown`** or unhandled block: log to `report.jsonl`, emit a raw text fallback. Never drop content silently.

### Rich text inline handling

Preserve all text spans, with these conversions:

- `a[href]` → external link, or `[[title]]` if href points to a known Notion page UUID.
- `strong` → `**text**`
- `em` → `*text*`
- `code` → `` `text` ``
- `s` → `~~text~~`
- nested formatting handled left-to-right.

Output: one markdown file for the sample page, plus intermediate JSON dump of the block tree for debugging.

---

## Phase 4 — Link Resolution & Wikilinks (full run)

1. Build global map `UUID → {title, vault_path}` from all 100 mhtml files plus the merged sidebar hierarchy.
2. Resolve all `app.notion.com/p/lewagon/<id>` hrefs:
   - Known UUID → `[[Title]]` (or `[[Title|display text]]` if anchor text differs).
   - Unknown UUID but in sidebar map → `[[Title]]`.
   - Unknown UUID not in sidebar → keep original URL + flag in report.
3. Filename sanitize: remove `[]#^|/\:*?"<>`, collapse whitespace.
4. Dedup collisions by appending a short UUID suffix.
5. Vault path scheme: mirror sidebar hierarchy as `vault/<Top Section>/<Page>.md`.
6. Pages not in the hierarchy go to `vault/_orphans/`.

---

## Phase 5 — Vault Assembly (full run)

1. Emit one `.md` per page with OKF-style frontmatter:

```yaml
---
type: notion-import
notion-id: <uuid>
source-url: <canonical>
imported: 2026-07-21
---
```

2. Create `_index.md` per folder: indented wikilink list of the sidebar tree.
3. Create `_report.md` containing:
   - orphan pages
   - unresolved links
   - skipped database views
   - image URLs for optional download
   - block-type coverage stats

---

## Phase 6 — Verification

### Prototype verification (1 file)

- Eyeball the sample markdown against the original `.mhtml` rendered in browser.
- Check: headings, lists, toggles, links, tables, callouts, images render reasonably.
- Adjust block mapping before moving to batch.

### Full-run verification (100 files)

- Count: every input page produced an output file (expect 100).
- No unhandled block types unless explicitly whitelisted.
- Broken link scan: every `[[...]]` target should exist as a file.
- Text coverage: output char count ≥ ~60% of extracted plain text (catches silent drops).
- Spot-check 3–5 diverse pages in Obsidian: graph view, backlinks, outline.

---

## Risks & Open Questions

1. **Remote images are auth-gated.** Keep URLs in markdown; download later if needed.
2. **Collection views** are partially rendered in DOM. Need sample inspection before promising row extraction.
3. **Collapsed sidebar nodes** may hide children. Merging across all files recovers most, but some subtrees may never have been expanded. `_orphans/` is the safety net.
4. **Per-file runtime:** ~11 MB HTML + lxml ≈ seconds each. Full run is minutes, no LLM cost.
5. **Optional LLM pass:** only after the parser run, for pages flagged as garbled (e.g. dense tables). Not part of the core pipeline.

---

## Estimated Effort

- Core parser (Phase 1–3) prototype: ~half a day.
- Block-type edge cases + full run: ~half a day.
- Verification + fixes: ~half a day.

**Next step:** build the Phase 1–3 prototype on one file and review the markdown output.
