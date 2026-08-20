#!/usr/bin/env python3
"""Merge new pages into vault: categorize, deduplicate, and add wikilinks."""

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
VAULT = ROOT / "out" / "vault"
PAGES = ROOT / "out" / "pages"

# ---------------------------------------------------------------------------
# Keyword-based folder mapping (first match wins)
# ---------------------------------------------------------------------------
FOLDER_RULES: list[tuple[list[str], str]] = [
    # People profiles
    (["anne dumas", "baptiste deren", "diana baleya", "elena bonhomme",
      "francesca chong", "jérôme schorgen", "orlane lagogu", "rebecca christophersen",
      "maría jesús torres"], "Operations/"),

    # Career Services
    (["career services", "career event", "career workshop", "career form",
      "career support", "careers guide", "getting started with career",
      "huntr guide for coaches", "live workshop plan"], "Career Services/"),

    # Marketing
    (["marketing recap", "marketing ai", "marketing content", "marketing initiative",
      "marketing support", "marketing note", "global editorial strategy",
      "content engine", "social post", "cold email",
      "brand platform", "brand video", "brand tone", "campus branding",
      "bank of pictures", "photos & photoshoot", "printing guidelines",
      "detailed persona", "glossary and editorial",
      "product marketing wiki", "landing pages library",
      "grid email variables", "design guidelines",
      "meta ads", "google ads", "paid ad templates",
      "ui kit", "templates & creative assets"], "Marketing/"),

    # AI & Technology
    (["ai & crm", "- ft ds", "ai chatbot", "ai product builder",
      "ai powered content", "data science & ai", "data science - daily",
      "web ft - daily", "data analytics", "wott ai", "wott improvement",
      "anthropic coupons", "full_time", "part_time"], "AI & Technology/"),

    # CRM & Tools
    (["crm campaign", "crm ops - ongoing", "crm & ops squad",
      "crm & ops fram", "crm & revops", "crm acquisition",
      "crm & ops sales & admission", "all crm & ops visual",
      "hubspot key", "hubspot module", "internal crm tutorial",
      "internal bitly", "calendly - setup", "calendly events",
      "import", "official documentation hub - crm"], "CRM & Tools/"),

    # Sales & Admissions
    (["admissions process", "lead scoring", "qualification",
      "how to assess candidates", "how to onboard a candidate",
      "how to process affiliation", "referral program old",
      "setting up a partnership", "deposit amount variable",
      "slack channel sales", "sales ops dashboard",
      "email templates (sales", "email translation", "emailing"], "Sales & Admissions/"),

    # Kitt Features / Learn Platform
    (["kitt offboarding", "add a button reopen", "deactivate teacher profiles",
      "expose challenge completion", "search students by name",
      "notify online lectures", "notify disability",
      "how to offboard a students from kitt",
      "how to add a new syllabus", "previewing a syllabus on kitt",
      "learn - terms of use", "find my course",
      "how to preview content changes on kitt",
      "how to create events on eventbrite", "how to link your eventbrite",
      "how to create an exam session", "how to run a session",
      "redeem claude code max coupons"], "Kitt Features/"),

    # Student Management
    (["additional student flag", "at-risk student tracking",
      "display students birthdays", "enhance student tickets",
      "export certification eligible", "extend student flags display",
      "students onboarding documentation",
      "notifications for students flags",
      "vérification ponctualité", "automatic prep-work reminders"], "Student Management/"),

    # Teacher Management
    (["lead teacher job", "lead teacher onboarding", "teacher selection (data)",
      "teacher feedback", "how to schedule tas", "le wagon's teaching test",
      "required teaching contracts", "onboarding new teachers"], "Teacher Management/"),

    # Operations / Batch Management
    (["new batch managers staffing", "new notion for bootcamp operations",
      "remote bootcamp operations", "sa ops handover",
      "s&a pm handover", "batch handover database template",
      "onboarding", "ops community survey", "tech framing session",
      "training sessions", "popup plan", "targets 2027"], "Operations/"),

    # Batch Reports
    (["h2 - ", "h2 202", "h2 20", "q4 - ", "q4 20", "q1 ", "q2 ",
      "batch reports", "batch handover"], "Batch Reports/"),

    # Product & Content
    (["content engine", "vertical page process", "syllabus & lp",
      "what is the data analytics bootcamp",
      "welcome guide full-time web development",
      "main tools and use cases", "le wagon description",
      "forms - the basics", "events - the basics", "events hub",
      "faq", "faq careers"], "Product & Content/"),

    # Franchises & Partners
    (["partnering with le wagon", "contact - global partners",
      "global partners", "initiatives - global partners",
      "city yellow flags", "@malt x le wagon",
      "referral program old"], "Franchises & Partners (old)/"),

    # Learn Platform
    (["learn - terms", "learn playbook"], "Learn Platform/"),

    # Fallback: Operations
    ([""], "Operations/"),
]


def categorize(title: str) -> str:
    """Return vault subfolder for a given page title."""
    title_lower = title.lower()
    for keywords, folder in FOLDER_RULES:
        if not keywords:
            continue
        for kw in keywords:
            if kw in title_lower:
                # Check it's not a false positive
                return folder
    return "Operations/"  # fallback


def sanitize_filename(name: str) -> str:
    """Sanitize for filesystem."""
    name = re.sub(r'[\[\]#\^|/\\:*?"<>]', "", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name


def read_frontmatter_field(text: str, field: str) -> str:
    """Extract a YAML frontmatter field value."""
    m = re.search(rf"^{field}:\s*(.+)$", text, re.MULTILINE)
    if m:
        return m.group(1).strip().strip('"').strip("'")
    return ""


def find_linked_notes(content: str, all_titles: set[str]) -> list[str]:
    """Find potential wikilink targets in content."""
    found = set()
    # Match [[Title]] or [[Title|alias]]
    for m in re.finditer(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", content):
        found.add(m.group(1).strip())
    # Also look for exact title mentions that could be linked
    lower_content = content.lower()
    for title in all_titles:
        if len(title) > 4 and title.lower() in lower_content:
            found.add(title)
    return sorted(found)


def main():
    # ------------------------------------------------------------------
    # 1. Index existing vault
    # ------------------------------------------------------------------
    vault_by_stem: dict[str, Path] = {}
    vault_by_title: dict[str, Path] = {}
    vault_all_titles: set[str] = set()

    for f in VAULT.rglob("*.md"):
        stem = f.stem.lower()
        vault_by_stem[stem] = f
        vault_all_titles.add(f.stem)

    print(f"Vault: {len(vault_by_stem)} files")

    # ------------------------------------------------------------------
    # 2. Process each new page
    # ------------------------------------------------------------------
    new_files = sorted(PAGES.glob("*.md"))
    skip_count = 0
    move_count = 0

    for pf in new_files:
        title = pf.stem
        stem_lower = title.lower()

        # Check for duplicate by stem
        if stem_lower in vault_by_stem:
            existing = vault_by_stem[stem_lower]
            # Compare size — identical means skip
            if pf.stat().st_size == existing.stat().st_size:
                print(f"  SKIP (identical): {title}")
            else:
                print(f"  SKIP (exists, diff size): {title}")
                print(f"    vault={existing.relative_to(VAULT)} ({existing.stat().st_size}b) pages=({pf.stat().st_size}b)")
            skip_count += 1
            continue

        # Categorize
        content = pf.read_text(encoding="utf-8")
        folder_name = categorize(title)
        target_dir = VAULT / folder_name
        target_dir.mkdir(parents=True, exist_ok=True)
        target_path = target_dir / pf.name

        # If target already exists, skip
        if target_path.exists():
            print(f"  SKIP (target exists): {title} -> {folder_name}")
            skip_count += 1
            continue

        # Move file
        shutil.move(str(pf), str(target_path))
        move_count += 1
        print(f"  MOVE: {title} -> {folder_name}")

        # ------------------------------------------------------------------
        # 3. Add wikilinks to related notes
        # ------------------------------------------------------------------
        vault_by_stem[stem_lower] = target_path
        vault_by_title[title] = target_path

    print(f"\nMoved: {move_count}, Skipped: {skip_count}")

    # ------------------------------------------------------------------
    # 4. Second pass: add related wikilinks at the bottom of each new page
    # ------------------------------------------------------------------
    print("\n--- Adding wikilinks ---")

    # Build a title index of everything in the vault
    all_titles: set[str] = set()
    for f in VAULT.rglob("*.md"):
        all_titles.add(f.stem)

    link_count = 0
    for f in VAULT.rglob("*.md"):
        # Only process files we just moved (check modification time recency)
        # Actually, process all files and add "Related" sections where links are missing
        content = f.read_text(encoding="utf-8")

        # Skip files that already have a "Related:" section
        if re.search(r"^##?\s*Related", content, re.MULTILINE):
            continue

        # Find potential links
        lower_content = content.lower()
        related = []
        for t in sorted(all_titles):
            if t.lower() == f.stem.lower():
                continue  # skip self
            # Check if the title appears in the content (but isn't already linked)
            if len(t) > 4 and t.lower() in lower_content:
                # Check not already a wikilink
                if f"[[{t}" not in content:
                    related.append(t)

        # Check frontmatter for notion-id links to other pages
        notion_id = read_frontmatter_field(content, "notion-id")
        if notion_id:
            # Find pages that reference this notion-id
            for other in VAULT.rglob("*.md"):
                if other == f:
                    continue
                other_content = other.read_text(encoding="utf-8")
                if notion_id in other_content and f"[[{f.stem}" not in other_content:
                    # Add a backlink to the other file
                    pass  # We'll handle backlinks separately

        if related:
            # Add a "Related" section
            links = "\n".join(f"- [[{t}]]" for t in related[:20])  # limit to 20
            new_content = content.rstrip() + f"\n\n## Related\n{links}\n"
            f.write_text(new_content, encoding="utf-8")
            link_count += len(related)
            print(f"  {f.relative_to(VAULT)}: +{len(related)} links")

    print(f"\nTotal wikilinks added: {link_count}")


if __name__ == "__main__":
    main()
