#!/usr/bin/env python3
"""Batch runner: convert all Notion .mhtml snapshots into an Obsidian vault.

Usage:
    py batch_parse.py

Outputs:
    out/vault/              markdown vault with hierarchy, wikilinks, _index.md, _report.md
    out/pages/              per-page .json metadata + _hierarchy_merged.json
"""
from __future__ import annotations

import email
import json
import re
import shutil
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup, Tag

from parse_mhtml import (
    block_type,
    decode_mhtml,
    extract_uuid,
    find_direct_blocks,
    render_block,
    render_children,
    resolve_link,
    sanitize_filename,
)

ROOT = Path(__file__).parent


# ---------------------------------------------------------------------------
# Hierarchy extraction (fixed: supports aria-owns + nested role=group wrappers)
# ---------------------------------------------------------------------------

def extract_sidebar_title(a: Tag, soup: BeautifulSoup) -> str:
    """Best-effort title extraction for a sidebar treeitem."""
    nt = a.find(class_=re.compile(r"\bnotranslate\b"))
    if nt:
        return nt.get_text(strip=True)
    lab = a.get("aria-labelledby")
    if lab:
        target = soup.find(id=lab)
        if target:
            return target.get_text(strip=True)
    return a.get_text(strip=True)


def build_hierarchy(soup: BeautifulSoup) -> list[dict[str, Any]]:
    """Extract the sidebar tree from a Notion page snapshot.

    Returns a list of root nodes: {id, title, children: [...]}.
    """
    sidebars = soup.find_all(class_=re.compile(r"\bnotion-outliner-shared\b"))
    if not sidebars:
        return []
    # Prefer the outliner that actually contains the treeitems.
    sidebar = max(sidebars, key=lambda s: len(s.find_all(attrs={"role": "treeitem"})))

    node_by_id: dict[str, dict[str, Any]] = {}
    item_group: dict[str, str | None] = {}
    owner_of_group: dict[str, str] = {}

    for a in sidebar.find_all(attrs={"role": "treeitem"}):
        href = a.get("href", "")
        uid = extract_uuid(href)
        if not uid:
            continue
        title = extract_sidebar_title(a, soup)
        node_by_id[uid] = {"id": uid, "title": title, "children": []}

        owns = a.get("aria-owns")
        if owns:
            owner_of_group[owns] = uid

        # Find the nearest ancestor role=group that has an id. The DOM sometimes
        # wraps the real group in an anonymous wrapper, so walk up until we hit
        # an id.
        group_id: str | None = None
        for g in a.find_parents(attrs={"role": "group"}):
            gid = g.get("id")
            if gid:
                group_id = gid
                break
        item_group[uid] = group_id

    # Determine parent of each item from its containing group owner.
    children_map: dict[str, list[str]] = defaultdict(list)
    roots: list[str] = []
    for uid, gid in item_group.items():
        parent = owner_of_group.get(gid) if gid else None
        if parent:
            children_map[parent].append(uid)
        else:
            roots.append(uid)

    # Sort children by DOM order to keep the original sidebar order.
    def dom_order_key(uid: str) -> int:
        # uid is unique in a file; we can rely on the order of node_by_id
        # insertion which matches find_all order.
        return list(node_by_id.keys()).index(uid)

    for parent in children_map:
        children_map[parent].sort(key=dom_order_key)

    def build(uid: str) -> dict[str, Any]:
        node = node_by_id[uid]
        for cid in children_map.get(uid, []):
            node["children"].append(build(cid))
        return node

    return [build(r) for r in roots]


def walk_hierarchy(nodes: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Flatten a hierarchy tree into a uuid -> node map."""
    out: dict[str, dict[str, Any]] = {}
    for n in nodes:
        out[n["id"]] = n
        out.update(walk_hierarchy(n.get("children", [])))
    return out


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def safe_name(name: str) -> str:
    """Sanitize a name for a file or folder."""
    name = sanitize_filename(name)
    name = name.strip()
    if not name:
        name = "Untitled"
    # Windows reserves trailing dots/spaces; strip them.
    name = name.rstrip(". ")
    return name


def unique_sibling_name(name: str, used: set[str], uid: str) -> str:
    """Deduplicate a name within a folder by appending a short UUID suffix."""
    if name not in used:
        return name
    suffix = uid[:6]
    candidate = f"{name} {suffix}"
    # In case even that collides, keep extending.
    i = 2
    while candidate in used:
        candidate = f"{name} {suffix}-{i}"
        i += 1
    return candidate


def compute_hierarchy_paths(
    roots: list[dict[str, Any]], pages_by_id: dict[str, "PageInfo"]
) -> dict[str, Path]:
    """Return uuid -> vault-relative Path (markdown file) for hierarchy nodes.

    Branch nodes get a folder of their own with a note inside.
    Leaf nodes live directly under their parent folder.
    """
    paths: dict[str, Path] = {}

    # Used names per *parent folder* path string.
    used: dict[str, set[str]] = defaultdict(set)

    def helper(nodes: list[dict[str, Any]], parent_folder: Path):
        for node in nodes:
            uid = node["id"]
            title = node["title"]
            children = node.get("children", [])
            name = safe_name(title)
            name = unique_sibling_name(name, used[str(parent_folder)], uid)
            used[str(parent_folder)].add(name)

            if children:
                folder = parent_folder / name
                paths[uid] = folder / (name + ".md")
                helper(children, folder)
            else:
                paths[uid] = parent_folder / (name + ".md")

    helper(roots, Path("."))
    return paths


def find_largest_content(soup: BeautifulSoup) -> Tag:
    """Return the largest .notion-page-content element, or for database-only
    pages, the largest top-level Notion block (usually a collection_view)."""
    contents = soup.find_all(class_=re.compile(r"\bnotion-page-content\b"))
    if contents:
        return max(contents, key=lambda x: len(x.get_text(strip=True)))
    # Fallback: some pages are full-page databases with no .notion-page-content.
    blocks = soup.find_all(class_=re.compile(r"\bnotion-.*-block\b"))
    if blocks:
        return max(blocks, key=lambda x: len(x.get_text(strip=True)))
    raise RuntimeError("No page content or block found")


def render_database_block(block: Tag, link_map: dict) -> tuple[str, list[str]]:
    """Render a full-page database as a simple list of linked rows."""
    seen: set[str] = set()
    lines: list[str] = []
    for a in block.find_all("a", href=re.compile(r"app\.notion\.com/p/")):
        href = a.get("href", "")
        uid = extract_uuid(href)
        text = a.get_text(strip=True)
        if not text:
            continue
        key = uid or text
        if key in seen:
            continue
        seen.add(key)
        lines.append(f"- {resolve_link(href, text, link_map)}")
    return "\n".join(lines) + "\n\n", []


def count_block_types(content: Tag) -> Counter:
    """Aggregate block-type counts for a page content tree."""
    counts: Counter = Counter()

    def walk(node: Tag):
        if not isinstance(node, Tag):
            return
        bt = block_type(node)
        if bt:
            counts[bt] += 1
            for child in find_direct_blocks(node):
                walk(child)
        else:
            for child in node.children:
                if isinstance(child, Tag):
                    walk(child)

    walk(content)
    return counts


# ---------------------------------------------------------------------------
# Page metadata container
# ---------------------------------------------------------------------------

class PageInfo:
    def __init__(self, path: Path, title: str, uid: str, snapshot: str):
        self.path = path
        self.title = title
        self.uid = uid
        self.snapshot = snapshot
        self.hierarchy_path: Path | None = None
        self.md_text: str = ""
        self.block_counts: Counter = Counter()
        self.unhandled_types: set[str] = set()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Convert Notion .mhtml snapshots to Obsidian markdown")
    parser.add_argument("--input-dir", default=".", help="Directory containing .mhtml files (default: current dir)")
    parser.add_argument("--vault-dir", default="out/vault", help="Output directory for markdown vault (default: out/vault)")
    parser.add_argument("--meta-dir", default="out/pages", help="Output directory for JSON metadata (default: out/pages)")
    args = parser.parse_args()

    MHTML_DIR = ROOT / args.input_dir
    OUT_VAULT = ROOT / args.vault_dir
    OUT_PAGES = ROOT / args.meta_dir

    mhtml_files = sorted(MHTML_DIR.glob("*.mhtml"))
    if not mhtml_files:
        print(f"No .mhtml files found in {MHTML_DIR}")
        return

    # -----------------------------------------------------------------------
    # Pass 1: extract page metadata and hierarchy from every file.
    # -----------------------------------------------------------------------
    pages: list[PageInfo] = []
    pages_by_id: dict[str, PageInfo] = {}

    # Global merged-hierarchy structures.
    # We merge by uuid and by parent->child edges.
    all_titles: dict[str, str] = {}
    all_children: dict[str, set[str]] = defaultdict(set)
    all_parents: dict[str, str | None] = {}

    for file in mhtml_files:
        try:
            html, snapshot, subject = decode_mhtml(file)
        except Exception as e:
            print(f"[SKIP] {file.name}: decode failed: {e}")
            continue

        soup = BeautifulSoup(html, "lxml")
        title = soup.title.string if soup.title else subject
        title = re.sub(r"\s*\|\s*Notion\s*$", "", title).strip()
        title = re.sub(r"\s{2,}", " ", title)
        uid = extract_uuid(snapshot)

        if not uid:
            print(f"[WARN] {file.name}: could not extract UUID, using filename")
            uid = file.stem[:32]

        page = PageInfo(file, title, uid, snapshot)
        pages.append(page)
        pages_by_id[uid] = page

        hierarchy = build_hierarchy(soup)
        # Register all hierarchy nodes and their edges.
        def register_tree(nodes: list[dict[str, Any]], parent: str | None):
            for n in nodes:
                nid = n["id"]
                all_titles[nid] = n["title"]
                all_parents[nid] = parent
                if parent:
                    all_children[parent].add(nid)
                register_tree(n.get("children", []), nid)
        register_tree(hierarchy, None)

    # -----------------------------------------------------------------------
    # Build merged hierarchy tree from parent/child edges.
    # -----------------------------------------------------------------------
    node_ids = set(all_titles) | set(pages_by_id)
    for pid in node_ids:
        if pid not in all_titles:
            # Page that never appeared in any sidebar; treat as orphan node.
            all_titles[pid] = pages_by_id[pid].title
            all_parents[pid] = None

    # Decide which title to use when a sidebar title and a page title differ.
    # Prefer the page title because it is what the page H1 says.
    for pid in pages_by_id:
        all_titles[pid] = pages_by_id[pid].title

    root_ids = {nid for nid in node_ids if all_parents.get(nid) is None}

    def build_merged_tree(ids: set[str]) -> list[dict[str, Any]]:
        tree: list[dict[str, Any]] = []
        # Keep deterministic order: sort by title, but ideally we want sidebar order.
        # Since we don't have a global order, sort by title for stability.
        for nid in sorted(ids, key=lambda x: all_titles[x].lower()):
            tree.append({
                "id": nid,
                "title": all_titles[nid],
                "children": build_merged_tree(all_children.get(nid, set())),
            })
        return tree

    merged_roots = build_merged_tree(root_ids)
    merged_nodes = walk_hierarchy(merged_roots)
    all_titles.update({nid: n["title"] for nid, n in merged_nodes.items()})

    # -----------------------------------------------------------------------
    # Determine vault placement for every page.
    # -----------------------------------------------------------------------
    hierarchy_paths = compute_hierarchy_paths(merged_roots, pages_by_id)

    orphans: list[PageInfo] = []
    for page in pages:
        if page.uid in hierarchy_paths:
            page.hierarchy_path = hierarchy_paths[page.uid]
        else:
            orphans.append(page)

    # Orphans go to _orphans/.
    used_orphan_names: set[str] = set()
    for page in orphans:
        name = unique_sibling_name(safe_name(page.title), used_orphan_names, page.uid)
        used_orphan_names.add(name)
        page.hierarchy_path = Path("_orphans") / (name + ".md")

    # -----------------------------------------------------------------------
    # Build a global title map that points to the sanitized vault filename.
    # This makes wikilinks match the actual markdown files.
    # -----------------------------------------------------------------------
    target_title_map: dict[str, str] = {}
    for uid, path in hierarchy_paths.items():
        target_title_map[uid] = path.stem
    for page in pages:
        if page.uid not in target_title_map:
            target_title_map[page.uid] = safe_name(page.title)
    title_map = target_title_map

    # -----------------------------------------------------------------------
    # Prepare output directories (clear for safe rerun).
    # -----------------------------------------------------------------------
    if OUT_PAGES.exists():
        shutil.rmtree(OUT_PAGES)
    if OUT_VAULT.exists():
        shutil.rmtree(OUT_VAULT)
    OUT_PAGES.mkdir(parents=True, exist_ok=True)
    OUT_VAULT.mkdir(parents=True, exist_ok=True)

    # -----------------------------------------------------------------------
    # Pass 2: render markdown for every page and write outputs.
    # -----------------------------------------------------------------------
    total_block_counts: Counter = Counter()
    total_unhandled: set[str] = set()
    image_urls: set[str] = set()
    skipped_db_views: list[tuple[str, str]] = []  # (page_title, url)
    unresolved_links: dict[str, list[str]] = defaultdict(list)  # url -> page titles

    def collect_links(md: str, page_title: str):
        # Unresolved internal Notion links.
        for m in re.finditer(
            r'https?://app\.notion\.com/p/[^\s)<>\]]+',
            md,
        ):
            unresolved_links[m.group(0)].append(page_title)
        # Skipped database views.
        for m in re.finditer(
            r'>\s*\[!warning\]\s*Database view not exported\s*\n>\s*('
            r'https?://app\.notion\.com/p/[^\s)<>\]]+)',
            md,
            re.IGNORECASE,
        ):
            skipped_db_views.append((page_title, m.group(1)))
        # Image URLs.
        for m in re.finditer(r'!\[.*?\]\((https?://[^\)]+)\)', md):
            image_urls.add(m.group(1))

    successful_pages: list[PageInfo] = []
    skipped_pages: list[PageInfo] = []

    for page in pages:
        try:
            html, snapshot, subject = decode_mhtml(page.path)
            soup = BeautifulSoup(html, "lxml")
            content = find_largest_content(soup)
            # Use render_children for normal page content containers; render a single
            # block directly for full-page databases that have no .notion-page-content.
            classes = set(content.get("class", []))
            if any("notion-page-content" in c for c in classes):
                md, unhandled = render_children(content, title_map)
            elif block_type(content) in ("collection_view", "collection_view_page"):
                md, unhandled = render_database_block(content, title_map)
            else:
                md, unhandled = render_block(content, title_map, 0)

            page.block_counts = count_block_types(content)
            page.unhandled_types = set(unhandled)
            total_block_counts.update(page.block_counts)
            total_unhandled.update(page.unhandled_types)

            # Collect links from the rendered body only, not the frontmatter.
            collect_links(md, page.title)

            frontmatter = (
                "---\n"
                f"type: notion-import\n"
                f"notion-id: {page.uid}\n"
                f"source-url: {page.snapshot}\n"
                f"imported: {datetime.now().strftime('%Y-%m-%d')}\n"
                "---\n\n"
            )
            page.md_text = frontmatter + f"# {page.title}\n\n" + md

            # Write markdown to vault.
            rel_path = page.hierarchy_path
            if rel_path is None:
                rel_path = Path("_orphans") / (safe_name(page.title) + ".md")
            md_path = OUT_VAULT / rel_path
            md_path.parent.mkdir(parents=True, exist_ok=True)
            md_path.write_text(page.md_text, encoding="utf-8")

            # Write JSON metadata.
            json_name = md_path.stem + ".json"
            meta = {
                "title": page.title,
                "notion_id": page.uid,
                "source_url": page.snapshot,
                "block_counts": dict(page.block_counts),
                "unhandled_types": sorted(page.unhandled_types),
            }
            (OUT_PAGES / json_name).write_text(
                json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
            )

            successful_pages.append(page)
            print(f"[OK] {page.path.name} -> {rel_path}")
        except Exception as e:
            skipped_pages.append(page)
            print(f"[SKIP] {page.path.name}: {e}")

    # -----------------------------------------------------------------------
    # Write merged hierarchy JSON.
    # -----------------------------------------------------------------------
    (OUT_PAGES / "_hierarchy_merged.json").write_text(
        json.dumps(merged_roots, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # -----------------------------------------------------------------------
    # Write _index.md at vault root.
    # -----------------------------------------------------------------------
    def render_index(nodes: list[dict[str, Any]], level: int = 0) -> str:
        lines: list[str] = []
        indent = "    " * level
        for n in nodes:
            target = target_title_map.get(n["id"], n["title"])
            lines.append(f"{indent}- [[{target}]]")
            lines.append(render_index(n.get("children", []), level + 1))
        return "\n".join(lines)

    index_md = "# Vault Index\n\n" + render_index(merged_roots)
    (OUT_VAULT / "_index.md").write_text(index_md, encoding="utf-8")

    # -----------------------------------------------------------------------
    # Write _report.md.
    # -----------------------------------------------------------------------
    report_lines: list[str] = []
    report_lines.append("# Batch Conversion Report\n")
    report_lines.append(f"- Total .mhtml files found: **{len(mhtml_files)}**")
    report_lines.append(f"- Pages successfully converted: **{len(successful_pages)}**")
    report_lines.append(f"- Pages skipped due to errors: **{len(skipped_pages)}**")
    report_lines.append(f"- Orphan pages (no hierarchy placement): **{len(orphans)}**")
    report_lines.append(
        f"- Unresolved internal Notion links: **{len(unresolved_links)}**"
    )
    report_lines.append(f"- Skipped database views: **{len(skipped_db_views)}**")
    report_lines.append(f"- Image URLs kept: **{len(image_urls)}**")
    report_lines.append(f"- Hierarchy nodes (merged): **{len(merged_nodes)}**")
    report_lines.append("")

    report_lines.append("## Skipped Pages\n")
    if skipped_pages:
        for page in skipped_pages:
            report_lines.append(f"- {page.title} (`{page.uid}`)")
    else:
        report_lines.append("_No pages were skipped._")
    report_lines.append("")

    report_lines.append("## Orphan Pages\n")
    if orphans:
        for page in orphans:
            report_lines.append(f"- {page.title} (`{page.uid}`) -> `{page.hierarchy_path.as_posix() if page.hierarchy_path else 'N/A'}`")
    else:
        report_lines.append("_No orphan pages._")
    report_lines.append("")

    report_lines.append("## Unresolved Internal Links\n")
    if unresolved_links:
        for url in sorted(unresolved_links):
            titles = sorted(set(unresolved_links[url]))
            report_lines.append(f"- `{url}` (in {len(titles)} page(s))")
    else:
        report_lines.append("_All internal Notion links were resolved._")
    report_lines.append("")

    report_lines.append("## Skipped Database Views\n")
    if skipped_db_views:
        for title, url in skipped_db_views:
            report_lines.append(f"- {title}: `{url}`")
    else:
        report_lines.append("_No database views were skipped._")
    report_lines.append("")

    report_lines.append("## Image URLs (kept for optional download)\n")
    if image_urls:
        for url in sorted(image_urls)[:200]:
            report_lines.append(f"- `{url}`")
        if len(image_urls) > 200:
            report_lines.append(f"- ... and {len(image_urls) - 200} more")
    else:
        report_lines.append("_No image URLs found._")
    report_lines.append("")

    report_lines.append("## Block Type Coverage Summary\n")
    report_lines.append("| Block type | Count |")
    report_lines.append("|---|---|")
    for btype, count in total_block_counts.most_common():
        report_lines.append(f"| {btype} | {count} |")
    report_lines.append("")

    report_lines.append("## Unhandled Block Types\n")
    if total_unhandled:
        for btype in sorted(total_unhandled):
            report_lines.append(f"- `{btype}`")
    else:
        report_lines.append("_No unhandled block types._")
    report_lines.append("")

    (OUT_VAULT / "_report.md").write_text("\n".join(report_lines), encoding="utf-8")

    # -----------------------------------------------------------------------
    # Summary to stdout.
    # -----------------------------------------------------------------------
    print("\n--- Batch parse complete ---")
    print(f"MHTML files: {len(mhtml_files)}")
    print(f"Markdown files created: {len(successful_pages)}")
    print(f"Pages skipped: {len(skipped_pages)}")
    print(f"Hierarchy nodes (merged): {len(merged_nodes)}")
    print(f"Orphan pages: {len(orphans)}")
    print(f"Unresolved internal links: {len(unresolved_links)}")
    print(f"Image URLs: {len(image_urls)}")
    print(f"Skipped database views: {len(skipped_db_views)}")
    print(f"Unhandled block types: {sorted(total_unhandled)}")
    print(f"Vault root: {OUT_VAULT}")
    print(f"Metadata root: {OUT_PAGES}")


if __name__ == "__main__":
    main()
