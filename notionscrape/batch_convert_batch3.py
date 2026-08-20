#!/usr/bin/env python3
"""
Convert batch 3 .mhtml files to Markdown, categorize into vault, and relink.

Phases:
  1. Parse all .mhtml -> Markdown files in out/pages_batch_3/
  2. Categorize and move into out/vault/ using existing folder rules
  3. Relink Notion URLs -> [[wikilinks]] across the vault
"""

import email
import io
import json
import os
import re
import shutil
import sys
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag

# ─── Paths ───────────────────────────────────────────────────────────────────

ROOT = Path(__file__).parent
MHTML_DIR = ROOT / "notion_pages_batch3"
OUT_PAGES = ROOT / "out" / "pages_batch_3"
OUT_VAULT = ROOT / "out" / "vault"
LOG_PATH = ROOT / "parse_batch3_log.txt"

# ─── Existing vault index (pre-built, for speed) ─────────────────────────────

# FOLDER_RULES from merge_to_vault.py — first-match-wins keyword mapping
FOLDER_RULES: list[tuple[list[str], str]] = [
    (["anne dumas", "baptiste deren", "diana baleya", "elena bonhomme",
      "francesca chong", "jérôme schorgen", "orlane lagogu", "rebecca christophersen",
      "maría jesús torres"], "Operations/"),
    (["career services", "career event", "career workshop", "career form",
      "career support", "careers guide", "getting started with career",
      "huntr guide for coaches", "live workshop plan"], "Career Services/"),
    (["marketing recap", "marketing ai", "marketing content", "marketing initiative",
      "marketing support", "marketing note", "global editorial strategy",
      "content engine", "social post", "cold email",
      "brand platform", "brand video", "brand tone", "campus branding",
      "bank of pictures", "photos & photoshoot", "printing guidelines",
      "detailed persona", "glossary and editorial",
      "product marketing wiki", "landing pages library",
      "grid email variables", "design guidelines",
      "meta ads", "google ads", "paid ad templates",
      "ui kit", "templates & creative assets",
      "booth", "stickers", "business card", "flyer",
      "event template", "financing one-pager"], "Marketing/"),
    (["ai & crm", "- ft ds", "ai chatbot", "ai product builder",
      "ai powered content", "data science & ai", "data science - daily",
      "web ft - daily", "data analytics", "wott ai", "wott improvement",
      "anthropic coupons", "full_time", "part_time",
      "ai software bootcamp", "ai tuto", "ai workshop", "ai for wagoners",
      "content library - data & ai", "competitors - data analytics",
      "competitors - data science", "competitors - data engineering",
      "data analytics warm up", "data analytics - students analysis",
      "data eng students", "data science students", "data science curriculum",
      "#1 - api", "#2 - data with python", "#3 - intro to ml"], "AI & Technology/"),
    (["crm campaign", "crm ops - ongoing", "crm & ops squad",
      "crm & ops fram", "crm & revops", "crm acquisition",
      "crm & ops sales & admission", "all crm & ops visual",
      "hubspot key", "hubspot module", "internal crm tutorial",
      "internal bitly", "calendly - setup", "calendly events",
      "import", "official documentation hub - crm",
      "crm - internal doc", "crm onboarding", "crm ops handbook",
      "crm plan", "crm revamp", "crm roadmap", "crm training",
      "crm architecture", "crm 2026 strategy",
      "automated emails", "tools database"], "CRM & Tools/"),
    (["admissions process", "lead scoring", "qualification",
      "how to assess candidates", "how to onboard a candidate",
      "how to process affiliation", "referral program",
      "setting up a partnership", "deposit amount variable",
      "slack channel sales", "sales ops dashboard",
      "email templates (sales", "email translation", "emailing"], "Sales & Admissions/"),
    (["kitt offboarding", "add a button reopen", "deactivate teacher profiles",
      "expose challenge completion", "search students by name",
      "notify online lectures", "notify disability",
      "how to offboard a students from kitt",
      "how to add a new syllabus", "previewing a syllabus on kitt",
      "learn - terms of use", "find my course",
      "how to preview content changes on kitt",
      "how to create events on eventbrite", "how to link your eventbrite",
      "how to create an exam session", "how to run a session",
      "redeem claude code max coupons",
      "certification session xml"], "Kitt Features/"),
    (["additional student flag", "at-risk student tracking",
      "display students birthdays", "enhance student tickets",
      "export certification eligible", "extend student flags display",
      "students onboarding documentation",
      "notifications for students flags",
      "vérification ponctualité", "automatic prep-work reminders",
      "create a full lead journey"], "Student Management/"),
    (["lead teacher job", "lead teacher onboarding", "teacher selection (data)",
      "teacher feedback", "how to schedule tas", "le wagon's teaching test",
      "required teaching contracts", "onboarding new teachers",
      "teacher feedback process"], "Teacher Management/"),
    (["new batch managers staffing", "new notion for bootcamp operations",
      "remote bootcamp operations", "sa ops handover",
      "s&a pm handover", "batch handover database template",
      "onboarding", "ops community survey", "tech framing session",
      "training sessions", "popup plan", "targets 2027",
      "bootcamp promo action tracker", "bootcamp syllabi",
      "bootcamp comparison tab",
      "checklist_ post-production", "checklist_ publication",
      "checklist_ video planning", "checklist_ video production",
      "audio best practices", "best practices for filming",
      "content planning", "content inspiration",
      "distribution review", "export video settings",
      "finding subjects", "equipment phone",
      "preparing your script", "posting on instagram",
      "repurposing your videos", "selfie mode",
      "diy video editing", "where to find stock images",
      "visual language guidelines",
      "build data golden moment",
      "companies recruiting alumni"], "Operations/"),
    (["content engine", "vertical page process", "syllabus & lp",
      "what is the data analytics bootcamp",
      "welcome guide full-time web development",
      "main tools and use cases", "le wagon description",
      "forms - the basics", "events - the basics", "events hub",
      "faq", "faq careers",
      "content library - admissions", "content library - alumni",
      "content library - awareness", "content library - career services",
      "content library - consideration", "content library - conversion",
      "content library - downloadable", "content library - financing",
      "content library - learning", "content library - methodology",
      "content library - podcasts", "content library - product",
      "content library - some", "content library - used in email",
      "content library - videos", "content library - web",
      "content library - women in tech", "content library - written",
      "apprenez à générer", "au delà de chatgpt",
      "café au wagon", "café gourmand",
      "apply with source", "speakers sourcing", "replays cleaning",
      "workshop feedback", "archive"], "Product & Content/"),
    (["partnering with le wagon", "contact - global partners",
      "global partners", "initiatives - global partners",
      "city yellow flags", "@malt x le wagon",
      "referral program old"], "Franchises & Partners (old)/"),
    (["learn - terms", "learn playbook"], "Learn Platform/"),
    (["es - bcn", "es - malt", "fr - compliance",
      "event series", "action plan q1 2025",
      "2025 crm roadmap", "2025 crm roadmap",
      "q2 2024", "q2 2022", "q2 2023", "q1 2022",
      "q1 2023", "q3 2022", "q3 2023",
      "crm 2026", "crm roadmap 2024",
      "apr-june", "jan-march", "july-sep", "oct-dec",
      "le wagon knowledge graph"], "Marketing/"),
    ([
      "content & quotes", "content", "competitor database",
      "competitor knowledge hub", "competitors - data analytics",
      "competitors - data science", "competitors - data engineering",
      "core syllabi", "components", "brand tone of voice",
      "branded merch examples"
    ], "Marketing/"),
    ([
      "baptiste deren", "diana baleya"
    ], "Operations/"),
    ([""], "Operations/"),
]


# ─── MHTML Parsing (from parse_mhtml.py) ─────────────────────────────────────

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


def build_hierarchy(soup: BeautifulSoup):
    """Extract sidebar shared tree. Returns list of root nodes."""
    sidebars = soup.find_all(class_=re.compile(r"\bnotion-outliner-shared\b"))
    if not sidebars:
        return []
    sidebar = sidebars[0]
    group_map = {}
    for g in sidebar.find_all(attrs={"role": "group"}):
        gid = g.get("id")
        if gid:
            group_map[gid] = []
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
        parent = a.find_parent(attrs={"role": "group"})
        if parent:
            gid = parent.get("id")
            group_map.setdefault(gid, []).append(node)
        owns = a.get("aria-owns")
        if owns:
            group_map.setdefault(owns, [])
    for a in sidebar.find_all(attrs={"role": "treeitem"}):
        href = a.get("href", "")
        uid = extract_uuid(href)
        if not uid:
            continue
        owns = a.get("aria-owns")
        if owns and owns in group_map:
            node_by_id[uid]["children"] = group_map[owns]
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


def block_type(block: Tag) -> str | None:
    classes = block.get("class", [])
    if not classes:
        return None
    for c in classes:
        if isinstance(c, str) and c.startswith("notion-") and c.endswith("-block"):
            return c[len("notion-") : -len("-block")]
    return None


def find_direct_blocks(parent: Tag) -> list[Tag]:
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
    leaf = block.find(attrs={"data-content-editable-leaf": "true"})
    if leaf:
        return leaf
    leaf = block.find(class_=re.compile(r"content-editable-leaf"))
    return leaf


def _wikilink_safe(text: str) -> str:
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
    if text and text != href:
        return f"[{text}]({href})"
    return f"<{href}>"


def extract_inline(node: Tag, link_map: dict) -> str:
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
            if "font-weight:600" in style or "font-weight: 600" in style:
                text = f"**{text}**"
            if "font-style:italic" in style or "font-style: italic" in style:
                text = f"*{text}*"
            parts.append(text)
        elif child.name == "img":
            alt = child.get("alt", "")
            src = child.get("src", "")
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
    text = text.replace("\xa0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = text.replace(" \n", "\n").replace("\n ", "\n")
    return text.strip()


def indent_lines(text: str, level: int) -> str:
    prefix = "    " * level
    return "\n".join(prefix + line if line else line for line in text.splitlines())


def render_block(block: Tag, link_map: dict, level: int = 0) -> tuple[str, list[str]]:
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


def extract_database_content(soup: BeautifulSoup) -> str:
    """Extract a readable summary from a collection-view page."""
    lines = []
    for h in soup.find_all(["h1", "h2", "h3"]):
        t = h.get_text(strip=True)
        if t:
            lines.append(f"## {t}")
    view_type_el = soup.find(class_=re.compile(r"notion-collection-view"))
    if view_type_el:
        view_type = view_type_el.get_text(strip=True)[:50]
        lines.append(f"\n*Database view: {view_type}*\n")
    props = soup.find_all(class_=re.compile(r"notion-collection-header"))
    if props:
        col_names = [p.get_text(strip=True) for p in props if p.get_text(strip=True)]
        if col_names:
            lines.append("**Columns:** " + ", ".join(col_names))
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
    return "\n".join(lines) if lines else ""


def collect_all_text(soup: BeautifulSoup) -> str:
    """Extract visible text from any notion block-like elements."""
    parts = []
    for el in soup.find_all(class_=lambda c: c and "notion-" in c):
        txt = el.get_text(strip=True)
        if txt and len(txt) > 2:
            parts.append(txt)
    return "\n".join(dict.fromkeys(parts))


# ─── Phase 1: Convert all .mhtml to Markdown ─────────────────────────────────

def convert_mhtml_to_md(mhtml_path: Path, out_dir: Path) -> dict | None:
    """Convert a single .mhtml file to Markdown. Returns info dict or None on fail."""
    try:
        html, snapshot, subject = decode_mhtml(mhtml_path)
        uid = extract_uuid(snapshot)
        title = subject or mhtml_path.stem.replace(" | Notion", "").strip()
        if html is None:
            return None

        soup = BeautifulSoup(html, "lxml")
        has_page_content = bool(soup.find_all(class_=re.compile(r"notion-page-content")))

        if has_page_content:
            # Build hierarchy for link_map
            hierarchy = build_hierarchy(soup)
            link_map = {}
            def walk(nodes):
                for n in nodes:
                    link_map[n["id"]] = n["title"]
                    walk(n["children"])
            walk(hierarchy)

            contents = soup.find_all(class_=re.compile(r"\bnotion-page-content\b"))
            if not contents:
                return None
            content = max(contents, key=lambda x: len(x.get_text(strip=True)))
            md_body, unhandled = render_children(content, link_map)
        else:
            # Database view
            body = extract_database_content(soup)
            if not body:
                body = collect_all_text(soup)
            md_body = f"\n{body}\n"
            unhandled = ["database_view"]

        frontmatter = (
            f"---\ntype: notion-import\nnotion-id: {uid}\n"
            f"source-url: {snapshot}\n"
            f"imported: {datetime.now().strftime('%Y-%m-%d')}\n---\n\n"
        )
        full_md = frontmatter + f"# {title}\n\n" + md_body

        out_name = sanitize_filename(title) + ".md"
        out_path = out_dir / out_name
        out_path.write_text(full_md, encoding="utf-8")

        return {
            "title": title,
            "uid": uid,
            "source": str(mhtml_path.name),
            "out": out_name,
            "unhandled": sorted(set(unhandled)),
            "size": out_path.stat().st_size,
            "is_db": not has_page_content,
        }
    except Exception as e:
        print(f"    [ERROR] {e}")
        return None


def phase1_convert_all():
    """Convert all .mhtml files to Markdown in out/pages_batch_3/."""
    OUT_PAGES.mkdir(parents=True, exist_ok=True)
    mhtml_files = sorted(MHTML_DIR.glob("*.mhtml"))
    print(f"Phase 1: Converting {len(mhtml_files)} .mhtml files...\n")

    results = []
    success = 0
    fail = 0
    db_count = 0

    for i, mhtml_path in enumerate(mhtml_files, 1):
        name = mhtml_path.name
        print(f"  [{i}/{len(mhtml_files)}] {name}", end="", flush=True)

        result = convert_mhtml_to_md(mhtml_path, OUT_PAGES)
        if result:
            results.append(result)
            success += 1
            if result["is_db"]:
                db_count += 1
            print(f" → {result['out']} ({result['size']}b)")
        else:
            fail += 1
            print(" → FAILED")

        if i < len(mhtml_files) and i % 20 == 0:
            # Brief pause every 20 files for system stability
            time.sleep(0.2)

    # Write summary
    summary = {
        "total": len(mhtml_files),
        "success": success,
        "fail": fail,
        "database_views": db_count,
        "files": results,
    }
    (OUT_PAGES / "_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # Log
    with open(LOG_PATH, "a") as f:
        f.write(f"\n=== Phase 1: {datetime.now()} ===\n")
        f.write(f"Total: {len(mhtml_files)}, Success: {success}, Fail: {fail}, DB: {db_count}\n")

    print(f"\n  Done! {success} converted, {fail} failed, {db_count} database views")
    return results


# ─── Phase 2: Categorize and move into vault ─────────────────────────────────

def categorize(title: str) -> str:
    """Return vault subfolder for a given page title."""
    title_lower = title.lower()
    for keywords, folder in FOLDER_RULES:
        if not keywords:
            continue
        for kw in keywords:
            if kw in title_lower:
                return folder
    return "Operations/"  # fallback


def phase2_categorize_and_move():
    """Move markdown files from pages_batch_3/ into categorized vault folders."""
    print(f"\nPhase 2: Categorizing and moving into vault...\n")

    # Index existing vault files
    vault_stems: set[str] = set()
    for f in OUT_VAULT.rglob("*.md"):
        vault_stems.add(f.stem.lower())

    new_files = sorted(OUT_PAGES.glob("*.md"))
    # Exclude summary files
    new_files = [f for f in new_files if not f.name.startswith("_")]
    print(f"  New files to categorize: {len(new_files)}")

    skipped = 0
    moved = 0
    folder_counts = defaultdict(int)
    moved_files = []

    for pf in new_files:
        title = pf.stem
        stem_lower = title.lower()

        # Skip if already exists in vault
        if stem_lower in vault_stems:
            print(f"  SKIP (exists in vault): {title}")
            skipped += 1
            continue

        # Read content to categorize
        content = pf.read_text(encoding="utf-8")
        folder_name = categorize(title)
        target_dir = OUT_VAULT / folder_name
        target_dir.mkdir(parents=True, exist_ok=True)
        target_path = target_dir / pf.name

        if target_path.exists():
            print(f"  SKIP (target exists): {title} -> {folder_name}")
            skipped += 1
            continue

        # Move file
        shutil.move(str(pf), str(target_path))
        moved += 1
        folder_counts[folder_name] += 1
        moved_files.append(target_path)
        vault_stems.add(stem_lower)
        print(f"  MOVE: {title} -> {folder_name}")

    print(f"\n  Moved: {moved}, Skipped: {skipped}")
    if folder_counts:
        print("  Per folder:")
        for folder, count in sorted(folder_counts.items()):
            print(f"    {folder}: {count}")

    return moved_files


# ─── Phase 3: Relink Notion URLs to wikilinks ───────────────────────────────

def sanitize_wikilink(name: str) -> str:
    return re.sub(r"[\[\]#^|]", "", name).strip()


def phase3_relink_vault():
    """Replace external Notion page URLs with local [[wikilinks]]."""
    print(f"\nPhase 3: Relinking Notion URLs to wikilinks...\n")

    # Build local index: notion-id -> (title, filepath)
    local_index: dict[str, tuple[str, Path]] = {}
    for f in OUT_VAULT.rglob("*.md"):
        content = f.read_text(encoding="utf-8")
        m = re.search(r"^notion-id:\s*([a-f0-9]+)", content, re.MULTILINE)
        if m:
            local_index[m.group(1)] = (f.stem, f)

    print(f"  Local notes indexed: {len(local_index)}")

    total_replacements = 0
    files_changed = 0
    all_files = sorted(OUT_VAULT.rglob("*.md"))

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

        if idx % 100 == 0:
            print(f"  [{idx}/{len(all_files)}] ... ({files_changed} files changed, ~{total_replacements} links)")

    print(f"\n  Files scanned: {len(all_files)}")
    print(f"  Files modified: {files_changed}")
    print(f"  Total new [[wikilinks]]: {total_replacements}")

    return files_changed, total_replacements


# ─── Phase 4: Add Related sections ──────────────────────────────────────────

def phase4_add_related_sections():
    """Add 'Related' sections to newly imported pages based on title similarity."""
    print(f"\nPhase 4: Adding Related sections...\n")

    # Build title index
    all_stems: dict[str, Path] = {}
    for f in OUT_VAULT.rglob("*.md"):
        all_stems[f.stem.lower()] = f

    # Find files that were just imported today and don't have a Related section
    today = datetime.now().strftime("%Y-%m-%d")
    processed = 0
    link_count = 0

    for f in sorted(OUT_VAULT.rglob("*.md")):
        content = f.read_text(encoding="utf-8")

        # Only process recently imported files
        if "imported: " + today not in content:
            continue
        if re.search(r"^##?\s*Related", content, re.MULTILINE):
            continue

        lower_content = content.lower()
        related = []
        for t_stem, t_path in sorted(all_stems.items()):
            if t_stem == f.stem.lower():
                continue
            if len(t_stem) > 4 and t_stem in lower_content:
                if f"[[{t_path.stem}" not in content:
                    related.append(t_path.stem)

        if related:
            links = "\n".join(f"- [[{t}]]" for t in related[:20])
            new_content = content.rstrip() + f"\n\n## Related\n{links}\n"
            f.write_text(new_content, encoding="utf-8")
            processed += 1
            link_count += len(related)

    print(f"  Files with new Related sections: {processed}")
    print(f"  Total wikilinks added: {link_count}")


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("Batch 3: Convert .mhtml -> Markdown -> Vault -> Relink")
    print("=" * 60)

    # Phase 1: Convert all .mhtml to markdown in pages_batch_3
    phase1_convert_all()

    # Phase 2: Categorize and move into vault
    moved_files = phase2_categorize_and_move()

    # Phase 3: Relink Notion URLs to wikilinks across the whole vault
    files_changed, total_links = phase3_relink_vault()

    # Phase 4: Add Related sections to new pages
    phase4_add_related_sections()

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Phase 1: .mhtml files converted to Markdown in out/pages_batch_3/")
    print(f"  Phase 2: New files moved into vault with categorization")
    print(f"  Phase 3: {files_changed} files relinked ({total_links} new wikilinks)")
    print(f"  Phase 4: Related sections added to imported pages")

    # Count vault
    total_vault = len(list(OUT_VAULT.rglob("*.md")))
    print(f"\n  Vault now contains ~{total_vault} files")

    print("\nDone!")


if __name__ == "__main__":
    main()
