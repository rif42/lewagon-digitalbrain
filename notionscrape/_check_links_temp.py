#!/usr/bin/env python3
"""Check which Notion URLs in Bank of pictures.md have local copies."""
import re
from pathlib import Path

vault = Path(__file__).parent / "out" / "vault"

# Index all notion-ids
local = {}
for f in vault.rglob("*.md"):
    c = f.read_text(encoding="utf-8")
    m = re.search(r"^notion-id:\s*([a-f0-9]+)", c, re.MULTILINE)
    if m:
        local[m.group(1)] = f.relative_to(vault)

# Check each Notion URL in Bank of pictures
bp = vault / "Marketing" / "Bank of pictures.md"
content = bp.read_text(encoding="utf-8")
urls = re.findall(r"https://app\.notion\.com/p/[^\s)\"`>]+", content)

print(f"Checking {len(urls)} Notion URLs in Bank of pictures.md\n")
for url in sorted(set(urls)):
    uid_m = re.search(r"([a-f0-9]{32})", url)
    if uid_m:
        uid = uid_m.group(1)
        if uid in local:
            print(f"[LOCAL] -> {local[uid]}")
            print(f"         {url[:100]}")
        else:
            print(f"[MISS]  {url[:100]}")
        print()
