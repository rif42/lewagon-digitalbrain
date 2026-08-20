#!/usr/bin/env python3
"""Prototype: convert one Notion .mhtml snapshot to Obsidian markdown."""
import email
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote

from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = Path(__file__).parent
DEFAULT_MHTML = ROOT / "A Guide to Pedagogical margin _ Notion.mhtml"
MHTML = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_MHTML
OUT = ROOT / "out"
OUT_PAGES = OUT / "pages"
OUT_VAULT = OUT / "vault"


def decode_mhtml(path: Path):
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

    if html is None:
        raise RuntimeError("No text/html part found")

    return html, snapshot, subject


def extract_uuid(url: str) -> str:
    """Extract the last 32-hex UUID from a Notion page URL path."""
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


# --- hierarchy ---

def build_hierarchy(soup: BeautifulSoup):
    """Extract sidebar shared tree. Returns list of root nodes."""
    sidebars = soup.find_all(class_=re.compile(r"\bnotion-outliner-shared\b"))
    if not sidebars:
        return []
    sidebar = sidebars[0]

    # map group id -> list of treeitem links
    group_map = {}
    for g in sidebar.find_all(attrs={"role": "group"}):
        gid = g.get("id")
        if gid:
            group_map[gid] = []

    # build treeitem nodes and link to group
    node_by_id = {}
    for a in sidebar.find_all(attrs={"role": "treeitem"}):
        href = a.get("href", "")
        uid = extract_uuid(href)
        title_el = a.find(class_=re.compile(r"\bnotranslate\b")) or a
        lab = a.get("aria-labelledby")
        if lab:
            target = soup.find(id=lab)
            title = target.get_text(strip=True) if target else title_el.get_text(strip=True)
        else:
            title = title_el.get_text(strip=True)
        if not uid:
            continue
        node = {"id": uid, "title": title, "children": []}
        node_by_id[uid] = node
        # parent group
        parent = a.find_parent(attrs={"role": "group"})
        if parent:
            gid = parent.get("id")
            group_map.setdefault(gid, []).append(node)
        # children group
        owns = a.get("aria-owns")
        if owns:
            group_map.setdefault(owns, [])  # ensure exists

    # attach children using aria-owns
    for uid, node in node_by_id.items():
        # find the treeitem a again? We need its aria-owns.
        # Easier: iterate all a and attach node_by_id[uid] children.
        pass

    # Better: iterate treeitems again and set children
    for a in sidebar.find_all(attrs={"role": "treeitem"}):
        href = a.get("href", "")
        uid = extract_uuid(href)
        if not uid:
            continue
        owns = a.get("aria-owns")
        if owns and owns in group_map:
            node_by_id[uid]["children"] = group_map[owns]

    # root = groups not referenced by any aria-owns
    owned_groups = set()
    for a in sidebar.find_all(attrs={"role": "treeitem"}):
        owns = a.get("aria-owns")
        if owns:
            owned_groups.add(owns)

    roots = []
    for gid, items in group_map.items():
        if gid is None or gid not in owned_groups:
            roots.extend(items)

    return roots


# --- content rendering ---

def block_type(block: Tag) -> str | None:
    classes = block.get("class", [])
    if not classes:
        return None
    for c in classes:
        if isinstance(c, str) and c.startswith("notion-") and c.endswith("-block"):
            return c[len("notion-") : -len("-block")]
    return None


def find_direct_blocks(parent: Tag) -> list[Tag]:
    """Collect descendant blocks that are direct children of parent in the block tree."""
    results = []
    for child in parent.children:
        if not isinstance(child, Tag):
            continue
        if block_type(child):
            results.append(child)
        else:
            results.extend(find_direct_blocks(child))
    return results


def content_leaf(block: Tag) -> Tag | None:
    """Find the content-editable leaf containing text for a block."""
    leaf = block.find(attrs={"data-content-editable-leaf": "true"})
    if leaf:
        return leaf
    # fallback for RTL or older Notion
    leaf = block.find(class_=re.compile(r"content-editable-leaf"))
    return leaf


def _wikilink_safe(text: str) -> str:
    """Strip characters that break Obsidian wikilink syntax."""
    if not text:
        return text
    text = re.sub(r"[\[\]#^|]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def resolve_link(href: str, text: str, link_map: dict) -> str:
    if not href:
        return text
    uid = extract_uuid(href)
    if uid and uid in link_map:
        title = _wikilink_safe(link_map[uid])
        text = _wikilink_safe(text)
        if title and text and title != text:
            return f"[[{title}|{text}]]"
        return f"[[{title}]]"
    # external
    if text and text != href:
        return f"[{text}]({href})"
    return f"<{href}>"


def extract_inline(node: Tag, link_map: dict) -> str:
    """Convert inline rich text inside a content leaf to markdown."""
    parts = []
    for child in node.children:
        if isinstance(child, NavigableString):
            parts.append(str(child))
        elif child.name == "strong" or child.name == "b":
            parts.append(f"**{extract_inline(child, link_map)}**")
        elif child.name == "em" or child.name == "i":
            parts.append(f"*{extract_inline(child, link_map)}*")
        elif child.name == "code":
            parts.append(f"`{extract_inline(child, link_map)}`")
        elif child.name in ("s", "del", "strike"):
            parts.append(f"~~{extract_inline(child, link_map)}~~")
        elif child.name == "a":
            href = child.get("href", "")
            text = extract_inline(child, link_map)
            parts.append(resolve_link(href, text, link_map))
        elif child.name == "br":
            parts.append("\n")
        elif child.name == "span":
            style = child.get("style", "")
            text = extract_inline(child, link_map)
            # Notion uses inline styles for bold/italic
            if "font-weight:600" in style or "font-weight: 600" in style:
                text = f"**{text}**"
            if "font-style:italic" in style or "font-style: italic" in style:
                text = f"*{text}*"
            parts.append(text)
        elif child.name == "img":
            alt = child.get("alt", "")
            src = child.get("src", "")
            # Notion renders emoji icons as transparent gifs with the emoji in alt
            if src.startswith("data:image/gif;base64") or not src:
                parts.append(alt)
            else:
                parts.append(f"![{alt}]({src})")
        else:
            parts.append(extract_inline(child, link_map))
    return "".join(parts)


def get_text(block: Tag, link_map: dict) -> str:
    leaf = content_leaf(block)
    if not leaf:
        return block.get_text(strip=True)
    text = extract_inline(leaf, link_map)
    # replace non-breaking spaces and collapse
    text = text.replace("\xa0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = text.replace(" \n", "\n").replace("\n ", "\n")
    return text.strip()


def indent_lines(text: str, level: int) -> str:
    prefix = "    " * level
    return "\n".join(prefix + line if line else line for line in text.splitlines())


def render_block(block: Tag, link_map: dict, level: int = 0) -> tuple[str, list[str]]:
    """Return (markdown, unhandled_types)."""
    btype = block_type(block) or "unknown"
    unhandled = []
    md = ""

    if btype in ("header", "sub_header", "sub_sub_header"):
        prefix = {"header": "#", "sub_header": "##", "sub_sub_header": "###"}[btype]
        text = get_text(block, link_map)
        md = f"{prefix} {text}\n\n"

    elif btype == "text":
        text = get_text(block, link_map)
        if text:
            md = f"{text}\n\n"

    elif btype == "bulleted_list":
        text = get_text(block, link_map)
        children_md, child_un = render_children(block, link_map, level + 1)
        unhandled.extend(child_un)
        line = f"- {text}"
        if children_md:
            md = f"{indent_lines(line, level)}\n{indent_lines(children_md.rstrip(), level + 1)}\n\n"
        else:
            md = f"{indent_lines(line, level)}\n\n"

    elif btype == "numbered_list":
        text = get_text(block, link_map)
        children_md, child_un = render_children(block, link_map, level + 1)
        unhandled.extend(child_un)
        line = f"1. {text}"
        if children_md:
            md = f"{indent_lines(line, level)}\n{indent_lines(children_md.rstrip(), level + 1)}\n\n"
        else:
            md = f"{indent_lines(line, level)}\n\n"

    elif btype == "to_do":
        text = get_text(block, link_map)
        checked = False
        cb = block.find(attrs={"role": "checkbox"})
        if cb:
            checked = cb.get("aria-checked", "false").lower() == "true"
        else:
            # look for a check svg
            if block.find("svg") and re.search(r"M\s*\d+.*\d+.*\d+", block.get_text(" ", strip=True)):
                checked = True
        mark = "x" if checked else " "
        md = f"{indent_lines(f'- [{mark}] {text}', level)}\n\n"

    elif btype == "toggle":
        summary = get_text(block, link_map)
        children_md, child_un = render_children(block, link_map, level + 1)
        unhandled.extend(child_un)
        md = f"<details><summary>{summary}</summary>\n\n{children_md}</details>\n\n"

    elif btype == "code":
        # try to find language
        lang = ""
        for el in block.find_all():
            cls = " ".join(el.get("class", []))
            if "language-" in cls:
                m = re.search(r"language-(\w+)", cls)
                if m:
                    lang = m.group(1)
                    break
        pre = block.find("pre")
        if pre:
            code = pre.get_text()
        else:
            code = block.get_text(strip=True)
        md = f"```{lang}\n{code}\n```\n\n"

    elif btype == "quote":
        text = get_text(block, link_map)
        md = "\n".join(f"> {line}" for line in text.splitlines() if line or True) + "\n\n"

    elif btype == "callout":
        icon = block.find(class_=re.compile(r"\bnotion-record-icon\b"))
        icon_text = icon.get_text(strip=True) if icon else ""
        text = get_text(block, link_map)
        # remove icon text if it's already at the start
        if text.startswith(icon_text):
            text = text[len(icon_text):].strip()
        md = f"> [!note] {icon_text}\n> {text}\n\n"

    elif btype == "divider":
        md = "---\n\n"

    elif btype == "image":
        img = block.find("img")
        src = img.get("src", "") if img else ""
        alt = img.get("alt", "") if img else ""
        md = f"![{alt}]({src})\n\n"

    elif btype == "page":
        a = block.find("a")
        href = a.get("href", "") if a else ""
        text = get_text(block, link_map)
        md = f"{indent_lines(resolve_link(href, text, link_map), level)}\n\n"

    elif btype == "collection_view_page":
        a = block.find("a")
        href = a.get("href", "") if a else ""
        text = get_text(block, link_map)
        md = f"{indent_lines(resolve_link(href, text, link_map), level)}\n\n"

    elif btype == "alias":
        a = block.find("a")
        href = a.get("href", "") if a else ""
        text = get_text(block, link_map)
        md = f"{indent_lines(resolve_link(href, text, link_map), level)}\n\n"

    elif btype == "button":
        text = get_text(block, link_map)
        if text:
            md = f"{indent_lines(f'**{text}**', level)}\n\n"
        else:
            md = ""

    elif btype == "table":
        rows = []
        for row in block.find_all(attrs={"role": "row"}):
            cells = [c.get_text(strip=True) for c in row.find_all(attrs={"role": "cell"})]
            if cells:
                rows.append(cells)
        if rows:
            widths = [max(len(c) for c in col) for col in zip(*rows)]
            md_rows = []
            for i, row in enumerate(rows):
                md_rows.append("| " + " | ".join(c.ljust(widths[j]) for j, c in enumerate(row)) + " |")
                if i == 0:
                    md_rows.append("| " + " | ".join("-" * w for w in widths) + " |")
            md = "\n".join(md_rows) + "\n\n"
        else:
            md = f"\n{block.get_text(strip=True)}\n\n"

    elif btype == "column_list":
        cols = []
        for col in find_direct_blocks(block):
            if block_type(col) == "column":
                cols.append(col)
        rendered = []
        for col in cols:
            rendered.append(render_children(col, link_map, level)[0].strip())
        md = "\n\n---\n\n".join(rendered) + "\n\n"

    elif btype == "column":
        md, child_un = render_children(block, link_map, level)
        unhandled.extend(child_un)

    elif btype == "collection_view":
        header_a = block.find("a", href=re.compile(r"app\.notion\.com/p/"))
        header_href = header_a.get("href", "") if header_a else ""
        header_title = get_text(header_a, link_map) if header_a else ""
        items = []
        for item in block.find_all(class_=re.compile(r"\bnotion-collection-item\b")):
            a = item.find("a", href=re.compile(r"app\.notion\.com/p/"))
            href = a.get("href", "") if a else ""
            text = get_text(item, link_map)
            title_line = text.splitlines()[0] if text else ""
            items.append(resolve_link(href, title_line, link_map))
        if items:
            md = f"### {header_title}\n\n" + "\n".join(f"- {it}" for it in items) + "\n\n"
        else:
            md = f"> [!warning] Database view not exported\n> {header_href}\n\n"

    elif btype == "bookmark":
        a = block.find("a")
        href = a.get("href", "") if a else ""
        text = get_text(block, link_map)
        md = f"[{text}]({href})\n\n"

    elif btype == "video":
        a = block.find("a")
        href = a.get("href", "") if a else ""
        md = f"> [!video] {href}\n\n"

    elif btype == "embed":
        src = block.get("src", "") or block.find("iframe", src=True)
        if isinstance(src, Tag):
            src = src.get("src", "")
        md = f"> [!embed] {src}\n\n"

    elif btype == "table_of_contents":
        md = ""

    elif btype == "transclusion_container":
        md, child_un = render_children(block, link_map, level)
        unhandled.extend(child_un)

    elif btype == "transclusion":
        a = block.find("a")
        href = a.get("href", "") if a else ""
        text = get_text(block, link_map)
        md = f"{indent_lines(resolve_link(href, text, link_map), level)}\n\n"

    elif btype == "gist":
        a = block.find("a")
        href = a.get("href", "") if a else ""
        md = f"> [!gist] {href}\n\n"

    elif btype == "external_object_instance":
        a = block.find("a")
        href = a.get("href", "") if a else ""
        md = f"> [!object] {href}\n\n"

    elif btype == "unknown":
        text = get_text(block, link_map)
        if text:
            md = f"<!-- unhandled: {btype} -->\n{text}\n\n"
            unhandled.append(btype)
        else:
            md = ""

    else:
        text = get_text(block, link_map)
        md = f"<!-- unhandled: {btype} -->\n{text}\n\n"
        unhandled.append(btype)

    return md, unhandled


def render_children(parent: Tag, link_map: dict, level: int = 0):
    md = ""
    unhandled = []
    for child in find_direct_blocks(parent):
        child_md, child_un = render_block(child, link_map, level)
        md += child_md
        unhandled.extend(child_un)
    return md, unhandled


# --- main ---

def main():
    OUT_PAGES.mkdir(parents=True, exist_ok=True)
    OUT_VAULT.mkdir(parents=True, exist_ok=True)

    html, snapshot, subject = decode_mhtml(MHTML)
    soup = BeautifulSoup(html, "lxml")
    title = soup.title.string if soup.title else subject
    title = re.sub(r"\s*\|\s*Notion\s*$", "", title).strip()
    title = re.sub(r"\s{2,}", " ", title)
    uid = extract_uuid(snapshot)

    hierarchy = build_hierarchy(soup)
    (OUT_PAGES / "_hierarchy.json").write_text(
        json.dumps(hierarchy, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # link map from hierarchy
    link_map = {}

    def walk(nodes):
        for n in nodes:
            link_map[n["id"]] = n["title"]
            walk(n["children"])

    walk(hierarchy)

    contents = soup.find_all(class_=re.compile(r"\bnotion-page-content\b"))
    if not contents:
        print("ERROR: no .notion-page-content found")
        sys.exit(1)
    content = max(contents, key=lambda x: len(x.get_text(strip=True)))

    md, unhandled = render_children(content, link_map)

    frontmatter = f"---\ntype: notion-import\nnotion-id: {uid}\nsource-url: {snapshot}\nimported: {datetime.now().strftime('%Y-%m-%d')}\n---\n\n"
    md = frontmatter + f"# {title}\n\n" + md

    out_name = sanitize_filename(title) + ".md"
    md_path = OUT_VAULT / out_name
    md_path.write_text(md, encoding="utf-8")

    # debug tree
    block_counts = {}

    def count_types(node: Tag):
        btype = block_type(node)
        if btype:
            block_counts[btype] = block_counts.get(btype, 0) + 1
        for c in find_direct_blocks(node):
            count_types(c)

    count_types(content)

    tree = {
        "title": title,
        "notion_id": uid,
        "source_url": snapshot,
        "block_counts": block_counts,
        "unhandled_types": sorted(set(unhandled)),
    }
    (OUT_PAGES / (sanitize_filename(title) + ".json")).write_text(
        json.dumps(tree, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"Page: {title}")
    print(f"UUID: {uid}")
    print(f"Markdown: {md_path}")
    print(f"  size: {md_path.stat().st_size} bytes")
    print(f"Hierarchy: {OUT_PAGES / '_hierarchy.json'}")
    print(f"Block counts: {block_counts}")
    print(f"Unhandled types: {sorted(set(unhandled))}")


if __name__ == "__main__":
    main()
