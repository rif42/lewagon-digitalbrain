#!/usr/bin/env python3
"""Batch convert all .mhtml files in new_notion_pages_batch2/ to markdown in out/pages/.

Handles both regular pages (via parse_mhtml.py) and database-view snapshots.
"""

import email
import json
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).parent
MHTML_DIR = ROOT / "new_notion_pages_batch2"
OUT_PAGES = ROOT / "out" / "pages"
OUT_VAULT = ROOT / "out" / "vault"
LOG = ROOT / "parse_log.txt"
PARSE_SCRIPT = ROOT / "parse_mhtml.py"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def decode_mhtml(path: Path) -> tuple[bytes | None, str, str]:
    """Return (html_bytes, snapshot_url, subject)."""
    with open(path, "rb") as fh:
        msg = email.message_from_binary_file(fh)
    snapshot = msg.get("Snapshot-Content-Location", "")
    subject = msg.get("Subject", "").replace(" | Notion", "").strip()
    html = None
    for part in msg.walk():
        if part.get_content_type().startswith("text/html"):
            html = part.get_payload(decode=True)
            if html is None:
                payload = part.get_payload(decode=False)
                html = payload.encode("utf-8") if isinstance(payload, str) else payload
            break
    return html, snapshot, subject


def extract_uuid(url: str) -> str:
    if not url:
        return ""
    path = url.split("?")[0].split("#")[0].rstrip("/")
    segment = path.split("/")[-1]
    m = re.search(r"(?:^|-)([a-f0-9]{32})$", segment.lower())
    return m.group(1) if m else ""


def sanitize_filename(name: str) -> str:
    name = re.sub(r'[\[\]#\^|/\\:*?"<>]', "", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name


def collect_all_text(soup: BeautifulSoup) -> str:
    """Extract visible text from any notion block-like elements."""
    parts = []
    for el in soup.find_all(class_=lambda c: c and "notion-" in c):
        txt = el.get_text(strip=True)
        if txt and len(txt) > 2:
            parts.append(txt)
    return "\n".join(dict.fromkeys(parts))  # dedup preserving order


def extract_database_content(soup: BeautifulSoup) -> str:
    """Extract a readable summary from a collection-view page."""
    lines = []

    # Collection header text
    for h in soup.find_all(["h1", "h2", "h3"]):
        t = h.get_text(strip=True)
        if t:
            lines.append(f"## {t}")

    # View type (Table / Board / Gallery / List / Calendar)
    view_type_el = soup.find(class_=re.compile(r"notion-collection-view"))
    if view_type_el:
        view_type = view_type_el.get_text(strip=True)[:50]
        lines.append(f"\n*Database view: {view_type}*\n")

    # Property / column names
    props = soup.find_all(class_=re.compile(r"notion-collection-header"))
    if props:
        col_names = [p.get_text(strip=True) for p in props if p.get_text(strip=True)]
        if col_names:
            lines.append("**Columns:** " + ", ".join(col_names))

    # Collection items (rows)
    items = soup.find_all(class_=re.compile(r"notion-collection-item"))
    for item in items:
        a = item.find("a", href=re.compile(r"app\.notion\.com/p/"))
        if a:
            href = a.get("href", "")
            uid = extract_uuid(href)
            title = a.get_text(strip=True) or uid[:8]
            lines.append(f"- {title}")
        else:
            txt = item.get_text(strip=True)[:120]
            if txt:
                lines.append(f"- {txt}")

    return "\n".join(lines) if lines else collect_all_text(soup)


def convert_via_parse_script(mhtml_path: Path) -> bool:
    """Run parse_mhtml.py. Returns True if successful."""
    result = subprocess.run(
        [sys.executable, str(PARSE_SCRIPT), str(mhtml_path)],
        capture_output=True, text=True, errors="replace", timeout=60,
    )
    return result.returncode == 0


def write_minimal_md(title: str, body: str, snapshot: str, uid: str) -> str:
    """Write a minimal markdown file and return its filename."""
    frontmatter = (
        f"---\ntype: notion-import\nnotion-id: {uid}\n"
        f"source-url: {snapshot}\nimported: {datetime.now().strftime('%Y-%m-%d')}\n"
        f"note: partial-import (database view)\n---\n\n"
    )
    md = frontmatter + f"# {title}\n\n{body}\n"
    out_name = sanitize_filename(title) + ".md"
    out_path = OUT_PAGES / out_name
    out_path.write_text(md, encoding="utf-8")
    return out_name


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    OUT_PAGES.mkdir(parents=True, exist_ok=True)
    OUT_VAULT.mkdir(parents=True, exist_ok=True)

    mhtml_files = sorted(MHTML_DIR.glob("*.mhtml"))
    print(f"Found {len(mhtml_files)} .mhtml files")

    # Read already-done log
    done_names = set()
    if LOG.exists():
        for line in LOG.read_text(encoding="utf-8").splitlines():
            parts = line.split("\t")
            if len(parts) >= 1 and parts[1]:
                done_names.add(parts[1])

    todo = [f for f in mhtml_files if f.name not in done_names]
    print(f"Already in log: {len(done_names)}")
    print(f"Remaining to convert: {len(todo)}")
    print()

    if not todo:
        print("All files already converted!")
        return

    success = 0
    fail = 0
    db_view_count = 0

    for i, mhtml_path in enumerate(todo, 1):
        name = mhtml_path.name
        print(f"[{i}/{len(todo)}] {name} ... ", end="", flush=True)

        html, snapshot, subject = decode_mhtml(mhtml_path)
        uid = extract_uuid(snapshot)
        title = subject or mhtml_path.stem

        if html is None:
            print("[FAIL] no HTML part")
            fail += 1
            with open(LOG, "a") as f:
                f.write(f"FAIL\t{name}\tno HTML part\n")
            continue

        soup = BeautifulSoup(html, "lxml")
        has_page_content = bool(soup.find_all(class_=re.compile(r"notion-page-content")))

        if has_page_content:
            # Use the existing converter
            ok = convert_via_parse_script(mhtml_path)
            if ok:
                # Move the generated .md from out/vault/ to out/pages/
                vault_mds = list(OUT_VAULT.glob("*.md"))
                if vault_mds:
                    # Find the one just created (newest)
                    latest = max(vault_mds, key=lambda p: p.stat().st_mtime)
                    dest = OUT_PAGES / latest.name
                    latest.replace(dest)
                    print(f"[OK] {dest.name}")
                    success += 1
                else:
                    print("[OK] (no md file)")
                    success += 1
                log_status = "OK"
            else:
                print("[FAIL] parse script error")
                fail += 1
                log_status = "FAIL"
        else:
            # Database view / collection page — extract what we can
            body = extract_database_content(soup)
            out_name = write_minimal_md(title, body, snapshot, uid)
            db_view_count += 1
            success += 1
            print(f"[OK] {out_name} (database view)")
            log_status = "OK_DB"

        # Log progress
        with open(LOG, "a") as f:
            f.write(f"{log_status}\t{name}\t{uid or 'unknown'}\n")

        if i < len(todo):
            time.sleep(0.3)

    print()
    print("=" * 50)
    print(f"Done! Success: {success}, Failed: {fail} (database views: {db_view_count})")
    print(f"Log saved to: {LOG}")
    print(f"Markdown files in: {OUT_PAGES}")


if __name__ == "__main__":
    main()
