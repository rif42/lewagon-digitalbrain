#!/usr/bin/env python3
"""Classify and integrate new pages into the vault with wikilinks."""

import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent
NEW = ROOT / "out" / "new_pages"
VAULT = ROOT / "out" / "vault"

# -----------------------------------------------------------------------
# Classification: title keywords -> target folder
# -----------------------------------------------------------------------

CLASSIFICATION = [
    (["Career Services"], [
        "career", "outcomes", "employer", "job status", "embedding careers",
    ]),
    (["Teacher Management"], [
        "teacher", "ta onboarding", "lead teacher", "teacher flag",
        "teacher lifecycle", "teacher mentoring", "teacher management",
        "teachers contract", "deactivate teachers", "increased rates",
    ]),
    (["Marketing"], [
        "marketing", "campaigns", "brand ", "branding",
        "deck template", "email template", "paid ads", "affiliate program",
        "hubspot", "revenue weekly", "battlecard", "battle card",
        "targets & dashboards", "targets and dashboards", "events",
        "global strategy",
    ]),
    (["Sales & Admissions"], [
        "sales", "admissions", "pipeline review", "ats ", "certification",
        "edusign", "exam session", "batch card", "adding forms",
        "admin how to grant", "assess platform", "no go reasons",
        "rqth", "handover hub",
    ]),
    (["Student Management"], [
        "student flag", "student attendance", "attendance tracking",
        "absence tracking", "check-in", "emotional situation",
        "disruptive student", "mid-batch survey", "nps ",
        "student performance", "student faq", "feedback form",
        "mid batch survey", "optimize mid", "student ticket",
    ]),
    (["Kitt Features"], [
        "kitt", "rsvp to events", "slack dm", "slack message after demo",
        "flashcard completion", "display event details",
        "nps response rate", "add the nps", "add reactions", "add a search bar",
        "automated slack", "automate birthday",
        "automate go notification", "automate the sending",
        "edit course hours", "daily ticket",
        "improve visibility on student ticket",
    ]),
    (["Learn Platform"], [
        "learn ", "learn.", "syllabus", "versions", "add a new program",
        "modify an existing syllabus", "learn remote", "improve diploma",
    ]),
    (["Experiments & Projects"], [
        "experiment", "pilot", "growth through", "project pipeline",
        "project management workshop", "project weeks",
        "check out the product",
    ]),
    (["Product & Content"], [
        "best products", "delivery lifecycle", "brainstorming",
        "how we work together", "running a workshop", "simultaneous livecode",
        "morning livecode", "update code", "content",
        "reboot on rails", "web dev insights",
    ]),
    (["AI & Technology"], [
        "ai ", "ai-", "data science", "data engineering", "data analytics",
        "wott", "anthropic", "overview - ai", "overview - data",
        "competitors - ai", "personas - ai", "syllabus - ai",
        "students analysis - ai",
    ]),
    (["CRM & Tools"], [
        "crm", "revops", "directory", "legal doc", "notion training",
        "notion tutorial", "office app", "odoo", "chrome extension",
        "laptop requirements", "email signature", "email and tools",
        "mini jobber", "hubspot x", "accessing s3",
    ]),
    (["Batch Reports"], [
        "h1 ", "h2 ", "q1 ", "q2 ", "q4 ",
        "amsterdam", "montreal", "bali", "barcelona",
        "cdmx", "cologne", "nantes", "rennes",
        "bordeaux", "melbourne", "porto",
        "santiago", "toulouse", "paris",
        "online - de",
    ]),
    (["Operations"], [
        "pre-during-post", "bootcamp opening", "bootcamp operation",
        "batch manager", "freelance batch", "full time batch",
        "sourcing", "get help with", "global updates",
        "program playbook", "team & ", "how to use ",
        "scheduled grid", "create an online course to onboard",
        "create students group", "explain how to read",
        "the most frequently", "monthly ops newsletter",
        "at kick-off", "community survey",
        "daily tasks - ", "data request", "archive",
    ]),
]


def classify_page(title: str) -> str:
    """Return the target folder name for a page title."""
    title_lower = title.lower()
    for folder, keywords in CLASSIFICATION:
        if any(kw in title_lower for kw in keywords):
            return folder[0]
    return "_Uncategorized"


# -----------------------------------------------------------------------
# Read all new pages
# -----------------------------------------------------------------------

pages = []
for f in sorted(NEW.glob("*.md")):
    if f.name.startswith("_"):
        continue
    text = f.read_text(encoding="utf-8")
    title_m = re.search(r"^# (.+)$", text, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else f.stem
    pages.append((f, title, text))

# -----------------------------------------------------------------------
# Classify and report
# -----------------------------------------------------------------------

folder_pages = defaultdict(list)
for src, title, text in pages:
    folder = classify_page(title)
    folder_pages[folder].append((src, title, text))

print("=== Classification ===")
for folder in sorted(folder_pages):
    print(f"\n{folder}/ ({len(folder_pages[folder])} pages)")
    for _, title, _ in sorted(folder_pages[folder], key=lambda x: x[1]):
        print(f"  - {title}")

# -----------------------------------------------------------------------
# Copy files into vault folders
# -----------------------------------------------------------------------

title_to_file = {}
folder_dirs = {}

for folder, items in folder_pages.items():
    folder_path = VAULT / folder
    folder_path.mkdir(parents=True, exist_ok=True)
    folder_dirs[folder] = folder_path

    for src, title, text in items:
        safe_name = re.sub(r'[\[\]#\^|/\\:*?"<>]', "", title)
        safe_name = re.sub(r"\s+", " ", safe_name).strip().rstrip(". ")
        dst = folder_path / f"{safe_name}.md"
        dst.write_text(text, encoding="utf-8")
        title_to_file[title] = Path(folder) / f"{safe_name}.md"

print(f"\n=== Copied {len(pages)} pages into vault ===")
print(f"Folders: {sorted(folder_dirs.keys())}")

# -----------------------------------------------------------------------
# Add wikilink "Related" sections to each page
# -----------------------------------------------------------------------

def find_related(title: str, all_titles: list[str]) -> list[str]:
    stop_words = {"the", "a", "an", "in", "on", "at", "to", "for", "of",
                  "and", "or", "is", "are", "was", "be", "by", "from",
                  "with", "as", "it", "its", "this", "that", "not", "no",
                  "new", "all", "how", "via", "up", "out"}
    words = set(re.findall(r'[a-z]+', title.lower())) - stop_words
    scored = []
    for t in all_titles:
        if t == title:
            continue
        twords = set(re.findall(r'[a-z]+', t.lower())) - stop_words
        common = words & twords
        if len(common) >= 2:
            score = len(common) / max(len(words | twords), 1)
            if score > 0.2:
                scored.append((score, t))
    scored.sort(reverse=True)
    return [t for _, t in scored[:5]]

all_titles = [t for _, t, _ in pages]

for folder, items in folder_pages.items():
    for src, title, text in items:
        related = find_related(title, all_titles)
        if related:
            related_lines = ["", "---", "## Related", ""]
            for rt in related:
                rt_file = title_to_file.get(rt)
                if rt_file:
                    link_name = rt_file.stem
                    related_lines.append(f"- [[{link_name}]]")
            if len(related_lines) > 3:
                text += "\n".join(related_lines) + "\n"
                safe_name = re.sub(r'[\[\]#\^|/\\:*?"<>]', "", title)
                safe_name = re.sub(r"\s+", " ", safe_name).strip().rstrip(". ")
                dst = folder_dirs[folder] / f"{safe_name}.md"
                dst.write_text(text, encoding="utf-8")

print("Wikilink 'Related' sections added.")

# -----------------------------------------------------------------------
# Build _index.md combining existing vault + new pages
# -----------------------------------------------------------------------

def find_existing_vault_files():
    result = {}
    for f in VAULT.rglob("*.md"):
        if f.name.startswith("_"):
            continue
        text = f.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"^# (.+)$", text, re.MULTILINE)
        title = m.group(1).strip() if m else f.stem
        result[title] = f.relative_to(VAULT)
    return result

existing = find_existing_vault_files()

folder_contents = defaultdict(list)
for title, rel_path in existing.items():
    folder = str(rel_path.parent)
    if folder == ".":
        folder = "_Root"
    folder_contents[folder].append((title, rel_path))

index_lines = ["# Vault Index\n"]
for folder in sorted(folder_contents, key=lambda f: (f != "_Root", f)):
    if folder != "_Root":
        index_lines.append(f"## {folder}\n")
    for title, rel_path in sorted(folder_contents[folder], key=lambda x: x[0].lower()):
        link_name = rel_path.stem
        index_lines.append(f"- [[{link_name}]]\n")
    index_lines.append("")

(VAULT / "_index.md").write_text("".join(index_lines), encoding="utf-8")

print(f"_index.md written with {sum(len(v) for v in folder_contents.values())} entries.")

# -----------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------
uncat = folder_pages.get("_Uncategorized", [])
if uncat:
    print(f"\nWARNING: {len(uncat)} uncategorized pages:")
    for _, title, _ in uncat:
        print(f"  - {title}")
else:
    print("\nAll pages classified successfully!")
