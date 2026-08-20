#!/usr/bin/env python3
"""Scan vault for remaining external Notion links and list missing ones for batch 3."""

import re
from collections import Counter
from pathlib import Path

VAULT = Path(__file__).parent / "out" / "vault"
OUT_LIST = Path(__file__).parent / "out" / "vault" / "_batch3_downloads.md"

# Index all local notion-ids
local_notes: dict[str, Path] = {}
for f in VAULT.rglob("*.md"):
    c = f.read_text(encoding="utf-8")
    m = re.search(r"^notion-id:\s*([a-f0-9]+)", c, re.MULTILINE)
    if m:
        local_notes[m.group(1)] = f

print(f"Local notes indexed: {len(local_notes)}")

# Scan all files for Notion page URLs (excluding images/icons)
missing_links: dict[str, tuple[str, str, list[Path]]] = {}
# key: uuid -> (url, page_name_suggestion, [source_files])
total_links = 0
matched = 0
skipped_images = 0

for f in sorted(VAULT.rglob("*.md")):
    c = f.read_text(encoding="utf-8")
    urls = re.findall(r"https://app\.notion\.com/p/[^\s)\"'`>]+", c)
    for url in sorted(set(urls)):
        total_links += 1

        # Skip image/icon URLs
        if "/image/" in url or "/icons/" in url:
            skipped_images += 1
            continue

        uid_m = re.search(r"([a-f0-9]{32})", url)
        if not uid_m:
            continue
        uid = uid_m.group(1)

        if uid in local_notes:
            matched += 1
        else:
            # Derive a page name from the URL
            clean_url = url.split("?")[0].split("#")[0].rstrip("/")
            seg = clean_url.split("/")[-1]
            page_name = re.sub(r"-([a-f0-9]{32}).*$", "", seg).strip("-")
            if not page_name or page_name == uid:
                page_name = uid[:12]

            if uid not in missing_links:
                missing_links[uid] = (clean_url, page_name, [])
            missing_links[uid][2].append(f.relative_to(VAULT))

print(f"Total Notion page URLs scanned: {total_links}")
print(f"Already linked locally: {matched}")
print(f"Image/icon URLs skipped: {skipped_images}")
print(f"Missing pages (no local copy): {len(missing_links)}")
print(f"\n=== Missing pages ===")
for i, (uid, (url, name, sources)) in enumerate(
    sorted(missing_links.items(), key=lambda x: x[1][1].lower()), 1
):
    print(f"{i:>4}. {name} — {url[:90]}")
    for s in sources[:3]:
        print(f"       referenced by: {s}")
    if len(sources) > 3:
        print(f"       ... and {len(sources)-3} more files")

# Write the missing pages list
lines = [
    "# Missing Notion Page Downloads - Batch 3\n",
    f"\nOut of unresolved Notion links in the vault, **{len(missing_links)}** pages need download.\n",
    "\n## Missing Pages\n",
    "\n| # | Page Name | URL | Referenced From |\n",
    "|---|-----------|-----|-----------------|\n",
]
for i, (uid, (url, name, sources)) in enumerate(
    sorted(missing_links.items(), key=lambda x: x[1][1].lower()), 1
):
    refs = ", ".join(str(s) for s in sources[:5])
    if len(sources) > 5:
        refs += f" (+{len(sources)-5} more)"
    lines.append(f"| {i} | {name} | `{url}` | {refs} |\n")

OUT_LIST.write_text("".join(lines), encoding="utf-8")
print(f"\n\nWritten to: {OUT_LIST}")
