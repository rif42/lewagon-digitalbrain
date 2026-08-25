# Instagram Scraper (instaloader) — Bali Events

Free, local-only scraper for Canggu venue Instagrams. No paid service required — runs with `instaloader 4.14.2` on the global `pythoncore-3.11-64` (Python 3.11).

> **One-liners via npm:**
> ```bash
> npm run instagram:fixture   # offline PoC (no IG login)
> npm run instagram           # live scrape (add -- --login USER to pass args: npm run instagram -- --login USER --limit 12)
> npm run instagram:merge:dry # preview merge into Bali Events List.md
> npm run instagram:merge     # merge (needs_review)
> ```

## Quick start

```bash
# 1. Install deps (once)
pip install -r scripts/instagram/requirements.txt

# 2. Login with throwaway account (see Auth below)
python scripts/instagram/scrape.py --login YOUR_THROWAWAY --handles finnsbeachclub potatoheadbali --limit 12

# 3. Inspect output
cat notes/knowledge_bank/instagram_raw/finnsbeachclub.json | head -n 80
cat notes/knowledge_bank/instagram_raw/potatoheadbali.json | head -n 80

# 4. Merge Instagram candidates into Bali Events List (needs_review)
python scripts/instagram/merge.py --dry-run   # preview
python scripts/instagram/merge.py             # write
```

## Files

- `scripts/instagram/scrape.py` — fetch posts per handle (PoC: 1-2 handles)
- `scripts/instagram/merge.py` — dedupe + merge into `notes/knowledge_bank/Bali Events List.md`
- `scripts/instagram/requirements.txt` — pinned `instaloader==4.14.2`
- `notes/knowledge_bank/instagram_raw/<handle>.json` — raw post dumps (git-tracked sample fixtures only)
- `scripts/instagram/session-*` — **local session files, never committed** (see `.gitignore`)
- `scripts/instagram/out/` — optional staging dir (also ignored)

## Auth

Instagram rate-limits anonymous scrapes heavily. Use a **throwaway account** (create a new IG account you don't care about; avoid phone 2FA if possible, or handle the 2FA prompt).

Login once — session is saved to `scripts/instagram/session-<username>`:

```bash
instaloader --login YOUR_THROWAWAY
# or via the script flag which does the same:
python scripts/instagram/scrape.py --login YOUR_THROWAWAY --handles finnsbeachclub --limit 12
```

If you see `LoginRequiredException` or `429`, re-login or wait. The script sleeps 2–5 s between requests and backs off on 429.

**Never commit** `session-*`, `*.session`, `cookies.txt`, or credentials.

## Scheduling

Weekly is enough for Bali events. Options:

- Manual: `python scripts/instagram/scrape.py ... && python scripts/instagram/merge.py`
- Windows Task Scheduler → run weekly `pip install -r ... && python scrape.py ...`
- GitHub Actions: `workflow_dispatch` only, with `IG_USERNAME`/`IG_PASSWORD` as repo secrets (not committed)

## Troubleshooting

- `Profile isn't available` → wrong handle or removed
- Empty output / login wall → re-login with `--login`
- `429 Too Many Requests` → wait 10–30 min, reduce `--limit`, increase `--sleep`
