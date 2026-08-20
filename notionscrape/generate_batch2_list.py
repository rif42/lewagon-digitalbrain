#!/usr/bin/env python3
"""Generate a download list in the format batch_download.py expects."""
import re
from pathlib import Path
from collections import defaultdict

VAULT = Path("out/vault")

# Build notion-id map
notion_id_map = {}
for f in VAULT.rglob("*.md"):
    if f.name.startswith("_"):
        continue
    text = f.read_text(encoding="utf-8", errors="replace")
    nm = re.search(r"^notion-id:\s*(\S+)", text, re.MULTILINE)
    if nm:
        notion_id_map[nm.group(1)] = f.relative_to(VAULT)

# Find all raw Notion URLs whose UUID doesn't match any note
unresolved = {}
seen_uuids = set()

for f in VAULT.rglob("*.md"):
    if f.name.startswith("_"):
        continue
    text = f.read_text(encoding="utf-8", errors="replace")
    for m in re.finditer(r"(https://app\.notion\.com/p/(?:lewagon/)?[^\s)<>\"]+)", text):
        full_url = m.group(1)
        clean = full_url.split("#")[0].split("?")[0].rstrip("/")
        uid_m = re.search(r"([a-f0-9]{32})", clean)
        if uid_m:
            uid = uid_m.group(1)
            if uid not in notion_id_map and uid not in seen_uuids:
                seen_uuids.add(uid)
                # Derive page name from URL segment
                seg = clean.split("/")[-1]
                page_name = re.sub(r"[-]([a-f0-9]{32})$", "", seg).strip("-")
                if not page_name:
                    page_name = uid[:8]
                unresolved[uid] = (full_url.split("?")[0], page_name)

# Write in _missing_downloads.md format
OUT = Path("out/vault/_missing_downloads_batch2.md")
lines = []
lines.append("# Missing Notion Page Downloads - Batch 2\n")
lines.append(f"Out of unresolved Notion links in the vault, **{len(unresolved)}** pages need download.\n")
lines.append("## Missing Pages\n")
lines.append("| # | Page Name | URL |")
lines.append("|---|-----------|-----|")
for i, (uid, (url, name)) in enumerate(sorted(unresolved.items()), 1):
    lines.append(f"| {i} | {name} | `{url}` |")

OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"Written: {OUT}")
print(f"Total pages: {len(unresolved)}")
