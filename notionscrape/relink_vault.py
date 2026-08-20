#!/usr/bin/env python3
"""Replace external Notion page URLs with local [[wikilinks]] where a local copy exists."""

import re
from pathlib import Path

VAULT = Path(__file__).parent / "out" / "vault"


def sanitize_wikilink(name: str) -> str:
    return re.sub(r"[\[\]#^|]", "", name).strip()


def extract_uuid(url: str) -> str | None:
    m = re.search(r"([a-f0-9]{32})", url)
    return m.group(1) if m else None


# ---------------------------------------------------------------------------
# 1. Build local index: notion-id -> (title, filepath)
# ---------------------------------------------------------------------------
local_index: dict[str, tuple[str, Path]] = {}
for f in VAULT.rglob("*.md"):
    content = f.read_text(encoding="utf-8")
    m = re.search(r"^notion-id:\s*([a-f0-9]+)", content, re.MULTILINE)
    if m:
        local_index[m.group(1)] = (f.stem, f)

print(f"Local notes indexed: {len(local_index)}")


# ---------------------------------------------------------------------------
# 2. Process each file
# ---------------------------------------------------------------------------
total_replacements = 0
files_changed = 0

all_files = sorted(VAULT.rglob("*.md"))
total_files = len(all_files)

for idx, f in enumerate(all_files, 1):
    original = f.read_text(encoding="utf-8")
    content = original
    file_changed = [False]

    def convert_link(m: re.Match) -> str:
        full = m.group(0)
        text = m.group(1)
        url = m.group(2)
        uid = extract_uuid(url)
        if uid is None or uid not in local_index:
            return full
        local_title, _ = local_index[uid]
        if local_title == f.stem:
            return full
        file_changed[0] = True
        safe_title = sanitize_wikilink(local_title)
        clean_text = sanitize_wikilink(text)
        if clean_text and clean_text != safe_title:
            return f"[[{safe_title}|{clean_text}]]"
        return f"[[{safe_title}]]"

    def convert_bare(m: re.Match) -> str:
        url = m.group(0)
        uid = extract_uuid(url)
        if uid is None or uid not in local_index:
            return url
        local_title, _ = local_index[uid]
        if local_title == f.stem:
            return url
        file_changed[0] = True
        safe_title = sanitize_wikilink(local_title)
        return f"[[{safe_title}]]"

    # Phase A: Markdown links [text](url)
    content = re.sub(r"\[([^\]]*)\]\(([^)]*)\)", convert_link, content)
    # Phase B: Bare Notion URLs
    content = re.sub(
        r"(?<!\]\()https://app\.notion\.com/p/[^\s)\"`>\[\]]*",
        convert_bare,
        content,
    )

    if file_changed[0]:
        f.write_text(content, encoding="utf-8")
        files_changed += 1

        n_before = original.count("[[")
        n_after = content.count("[[")
        n_new = n_after - n_before

        total_replacements += n_new

        # Show sample diffs
        diff_lines = []
        for i, (ol, nl) in enumerate(zip(original.splitlines(), content.splitlines())):
            if ol != nl:
                diff_lines.append(f"  L{i+1}: {nl.strip()[:150]}")
        for d in diff_lines[:4]:
            safe = d.encode('ascii', errors='replace').decode('ascii')
            print(safe)
        if len(diff_lines) > 4:
            print(f"  ... and {len(diff_lines)-4} more changes")
        rel = str(f.relative_to(VAULT)).encode('ascii', errors='replace').decode('ascii')
        print(f"  -> {rel} ({n_new} links)")
        print()

    if idx % 100 == 0:
        print(f"[{idx}/{total_files}] ... ({files_changed} files changed, ~{total_replacements} links)")

print(f"\n{'='*50}")
print(f"Files scanned: {total_files}")
print(f"Files modified: {files_changed}")
print(f"Total replacements (net new [[wikilinks]]): {total_replacements}")
