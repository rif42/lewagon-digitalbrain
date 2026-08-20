#!/usr/bin/env python3
"""Scan vault for unresolved references — both wikilinks and raw Notion URLs."""
import re
from collections import defaultdict
from pathlib import Path

VAULT = Path("out/vault")

# --- 1. Existing files ---
existing_notes = set()
notion_id_to_file = {}  # notion-id -> vault-relative Path
for f in VAULT.rglob("*.md"):
    if f.name.startswith("_"):
        continue
    existing_notes.add(f.stem.lower())
    # Read notion-id from frontmatter
    text = f.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^notion-id:\s*(\S+)", text, re.MULTILINE)
    if m:
        notion_id_to_file[m.group(1)] = f.relative_to(VAULT)

def filename_exists(link: str) -> bool:
    """Check if a wikilink target exists as a file stem."""
    return link.lower() in existing_notes

# --- 2. Scan all files ---
total_files = 0
broken_wikilinks = defaultdict(list)
raw_notion_urls = defaultdict(list)

for f in sorted(VAULT.rglob("*.md")):
    if f.name.startswith("_"):
        continue
    total_files += 1
    text = f.read_text(encoding="utf-8", errors="replace")
    rel = f.relative_to(VAULT)

    # [[wikilinks]]
    for m in re.finditer(r"\[\[([^\]]+?)\]\]", text):
        link = m.group(1).strip()
        if "|" in link:
            link = link.split("|")[0].strip()
        if link.lower() == "link":
            continue  # false positive: external link anchor text
        if not filename_exists(link):
            broken_wikilinks[link].append(str(rel))

    # Raw notion URLs
    for m in re.finditer(r"https://app\.notion\.com/p/(?:lewagon/)?([a-f0-9]{32})", text):
        uid = m.group(1)
        url = m.group(0)
        # Check if this UUID maps to a known note
        if uid not in notion_id_to_file:
            raw_notion_urls[url].append(str(rel))

# --- 3. Report ---
lines = []
lines.append("# Unresolved References Report\n")
lines.append(f"Scanned **{total_files}** files.\n")

lines.append("## [[Wikilinks]]\n")
lines.append(f"- Total wikilinks scanned: scanned above\n")
if broken_wikilinks:
    lines.append(f"- **{len(broken_wikilinks)} broken wikilinks** pointing to non-existent notes:\n")
    lines.append("| Missing Note | Referenced In |")
    lines.append("|-------------|---------------|")
    for link, sources in sorted(broken_wikilinks.items()):
        refs = ", ".join(sorted(set(sources)))
        lines.append(f"| `{link}` | {refs} |")
else:
    lines.append("- ✅ **0 broken wikilinks.** All `[[wikilinks]]` resolve to existing notes.\n")

lines.append("\n## Raw Notion URLs\n")
lines.append("These are `app.notion.com/p/...` URLs still embedded in the markdown body ")
lines.append("that could not be converted to `[[wikilinks]]` because the target page ")
lines.append("UUID does not match any note in the vault.\n")
lines.append(f"- **{len(raw_notion_urls)} unresolved Notion URLs**\n")

if raw_notion_urls:
    lines.append("| # | Notion URL | Referenced In |")
    lines.append("|---|-----------|---------------|")
    for i, (url, sources) in enumerate(sorted(raw_notion_urls.items()), 1):
        refs = ", ".join(sorted(set(sources)))
        short = url if len(url) <= 90 else url[:87] + "..."
        lines.append(f"| {i} | `{short}` | {refs} |")

with open("out/vault/_link_report.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Report written: out/vault/_link_report.md")
print(f"Files scanned: {total_files}")
print(f"Broken wikilinks: {len(broken_wikilinks)}")
print(f"Unresolved Notion URLs: {len(raw_notion_urls)}")
