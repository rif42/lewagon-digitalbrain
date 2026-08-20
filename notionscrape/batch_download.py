#!/usr/bin/env python3
"""Batch download missing Notion pages via cua-driver CLI + Brave automation."""

import json
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).parent
OUT_VAULT = ROOT / "out" / "vault"
REPORT = OUT_VAULT / "_report.md"
MISSING_DOWNLOADS = OUT_VAULT / "_missing_downloads.md"

# ---------------------------------------------------------------------------
# Extract name-based URLs from the conversion report or missing-downloads table
# ---------------------------------------------------------------------------

def get_urls(source: str = "report") -> list[tuple[str, str, str]]:
    """Return list of (url, uuid, page_name) for name-based pages needing download.

    Args:
        source: "report" for _report.md (unresolved links section),
                "missing" for _missing_downloads.md (table of failed downloads).
    """
    if source == "missing":
        return _get_urls_from_missing()

    # Default: read from _report.md
    return _get_urls_from_report()


def _get_urls_from_report() -> list[tuple[str, str, str]]:
    """Extract name-based URLs from the report's Unresolved Internal Links section."""
    text = REPORT.read_text(encoding="utf-8")
    section = text.split("## Unresolved Internal Links")[1].split("##")[0]
    all_urls = re.findall(r"https://app\.notion\.com/p/[^\s`]+", section)

    results = []
    seen = set()
    for url in sorted(set(all_urls)):
        base = url.split("?")[0].split("#")[0].rstrip("/")
        seg = base.split("/")[-1]

        # Skip DB views (lewagon/ prefix = database view URLs)
        if seg.startswith("lewagon/") and "?v=" in url:
            continue
        # Skip pure UUID pages (just hex)
        if re.match(r"^[a-f0-9]{32}$", seg.lower()):
            continue

        uid_match = re.search(r"([a-f0-9]{32})", seg.lower())
        uid = uid_match.group(1) if uid_match else "unknown"
        page_name = re.sub(r"-([a-f0-9]{32}).*$", "", seg).strip("-")

        clean_url = url.split("?")[0]  # strip query params
        if uid not in seen:
            seen.add(uid)
            results.append((clean_url, uid, page_name))

    return results


def _get_urls_from_missing() -> list[tuple[str, str, str]]:
    """Extract name-based URLs from _missing_downloads.md table.

    The table has three columns: #, Page Name, URL.
    URLs are all name-based (the table only lists pages that failed download).
    """
    text = MISSING_DOWNLOADS.read_text(encoding="utf-8")
    all_urls = re.findall(r"https://app\.notion\.com/p/[^\s`|]+", text)

    results = []
    seen = set()
    for url in sorted(set(all_urls)):
        clean_url = url.split("?")[0].split("#")[0].rstrip("/")
        seg = clean_url.split("/")[-1]

        uid_match = re.search(r"([a-f0-9]{32})", seg.lower())
        uid = uid_match.group(1) if uid_match else "unknown"
        page_name = re.sub(r"-([a-f0-9]{32}).*$", "", seg).strip("-")
        if not page_name:
            page_name = uid[:8]

        if uid not in seen:
            seen.add(uid)
            results.append((clean_url, uid, page_name))

    return results


# ---------------------------------------------------------------------------
# cua-driver CLI helpers
# ---------------------------------------------------------------------------

def cua_call(tool: str, args: dict) -> dict:
    """Call a cua-driver tool with JSON args via stdin."""
    result = subprocess.run(
        ["cua-driver", "call", tool],
        input=json.dumps(args),
        capture_output=True,
        text=True,
        errors="replace",
        timeout=30,
    )
    out = result.stdout.strip()
    err = result.stderr.strip()
    if result.returncode != 0:
        return {"error": result.returncode, "stderr": err, "stdout": out}
    try:
        return json.loads(out) if out else {}
    except json.JSONDecodeError:
        return {"raw": out, "stderr": err}


def get_brave_pid() -> int | None:
    """Find Brave browser PID via list_apps."""
    data = cua_call("list_apps", {})
    for app in data.get("apps", []):
        if app.get("name") == "Brave" and app.get("running"):
            return app["pid"]
    return None


def get_brave_window_id(pid: int) -> int | None:
    """Find Brave's main window HWND by PID via list_windows."""
    data = cua_call("list_windows", {})
    for w in data.get("_legacy_windows", []):
        if w.get("pid") == pid and w.get("is_on_screen"):
            return w["window_id"]
    return None


# Error text patterns that indicate a Notion page is not accessible.
_NOTION_ERROR_PATTERNS = [
    "page not found",
    "don't have permission",
    "not found",
    "this page has been deleted",
    "page not available",
    "you don't have access",
    "no permission",
]


def check_page_for_errors(pid: int) -> str | None:
    """Inspect Brave's current page via UIA tree for Notion error indicators.

    Returns:
        "not_found" if the page shows 'Page not found' or similar.
        "no_permission" if the page shows 'no permission'.
        None if the page appears valid (no error text detected).
    """
    window_id = get_brave_window_id(pid)
    if window_id is None:
        return None  # Can't determine; assume valid

    data = cua_call("get_window_state", {
        "pid": pid,
        "window_id": window_id,
        "max_elements": 200,
        "max_depth": 10,
    })

    if "error" in data:
        return None  # Can't inspect; assume valid

    # Check text elements in the tree markdown
    tree_text = data.get("tree_markdown", "").lower()

    if "page not found" in tree_text or "this page has been deleted" in tree_text:
        return "not_found"
    if "don't have permission" in tree_text or "no permission" in tree_text or "you don't have access" in tree_text:
        return "no_permission"

    # Also check structured elements
    elements = data.get("structuredContent", {}).get("elements", [])
    for elem in elements:
        label = (elem.get("label") or "").lower()
        if any(p in label for p in _NOTION_ERROR_PATTERNS):
            if "not found" in label or "deleted" in label:
                return "not_found"
            return "no_permission"

    return None  # Page seems valid


def hotkey(pid: int, keys: list[str]) -> bool:
    """Send a hotkey combination to Brave."""
    result = cua_call("hotkey", {"pid": pid, "keys": keys, "delivery_mode": "foreground"})
    return "error" not in result


def press_key(pid: int, key: str) -> bool:
    """Send a single key press."""
    result = cua_call("press_key", {"pid": pid, "key": key, "delivery_mode": "foreground"})
    return "error" not in result


def click(pid: int, x: int, y: int) -> bool:
    """Click at screen coordinates."""
    result = cua_call("click", {"pid": pid, "x": x, "y": y, "delivery_mode": "foreground"})
    return "error" not in result


# ---------------------------------------------------------------------------
# Save a single page
# ---------------------------------------------------------------------------

def get_save_dialog_pid() -> int | None:
    """Find the Save As dialog PID (separate process from Brave)."""
    data = cua_call("list_windows", {})
    for w in data.get("_legacy_windows", []):
        if w.get("title") == "Save As":
            return w["pid"]
    return None


def save_notion_page(pid: int, url: str, first_page: bool = False) -> str:
    """Navigate to a Notion URL in Brave and save as .mhtml.

    On first page opens a new tab; subsequent pages reuse the current tab.
    Returns a status string:
        "ok"                — page saved successfully
        "skip_not_found"    — Notion returned "Page not found"
        "skip_no_permission" — Notion returned "no permission" / access denied
        "fail"              — cua-driver / navigation / save dialog error
    """
    if first_page:
        # Open new tab on first run
        if not hotkey(pid, ["Ctrl", "T"]):
            return "fail"
    # else: current tab already has a Notion page, navigate fresh

    # Focus address bar, paste URL, navigate
    subprocess.run(["clip"], input=url, text=True)  # copy URL to clipboard
    hotkey(pid, ["Ctrl", "L"])     # focus address bar
    hotkey(pid, ["Ctrl", "V"])     # paste URL
    hotkey(pid, ["Enter"])         # navigate

    # Wait for page to start loading
    time.sleep(5)

    # --- Check for error pages before attempting save ---
    error_type = check_page_for_errors(pid)
    if error_type == "not_found":
        return "skip_not_found"
    if error_type == "no_permission":
        return "skip_no_permission"

    # Page seems valid — proceed with save dialog
    time.sleep(2)

    # Open Save As dialog via menu (Alt+F -> S -> Right -> Down x3 -> Enter)
    hotkey(pid, ["Alt", "F"])
    time.sleep(0.5)
    press_key(pid, "S")
    time.sleep(0.3)
    hotkey(pid, ["Right"])
    time.sleep(0.3)
    for _ in range(3):
        hotkey(pid, ["Down"])
        time.sleep(0.2)
    hotkey(pid, ["Enter"])
    time.sleep(2)

    # Confirm save: find the Save As dialog PID (separate process) and send Alt+S
    dialog_pid = get_save_dialog_pid()
    if dialog_pid:
        subprocess.run(
            ["cua-driver", "call", "hotkey"],
            input=json.dumps({"pid": dialog_pid, "keys": ["Alt", "S"], "delivery_mode": "foreground"}),
            capture_output=True, text=True, errors="replace", timeout=15,
        )
    else:
        # Fallback: send to Brave PID without foreground
        subprocess.run(
            ["cua-driver", "call", "hotkey"],
            input=json.dumps({"pid": pid, "keys": ["Alt", "S"]}),
            capture_output=True, text=True, errors="replace", timeout=15,
        )
    time.sleep(2)

    # Dismiss "Confirm Save As" overwrite dialog if it appeared
    _dismiss_overwrite_dialog(pid)

    return "ok"


def _dismiss_overwrite_dialog(pid: int) -> None:
    """If a 'Confirm Save As' overwrite dialog is open, press Alt+Y to accept.

    Tries the dialog's own PID first, then falls back to the browser PID.
    """
    for attempt in range(3):
        try:
            data = subprocess.run(
                ["cua-driver", "call", "list_windows"],
                capture_output=True, text=True, errors="replace", timeout=15,
            )
            if data.returncode != 0:
                return
            windows = json.loads(data.stdout).get("_legacy_windows", [])
            found = False
            for w in windows:
                title = w.get("title", "")
                # Common overwrite dialog titles on Windows
                if any(phrase in title for phrase in ["Confirm Save As", "确认另存为", "Save Webpage"]):
                    dialog_pid = w.get("pid")
                    if dialog_pid and dialog_pid != pid:
                        # Send to the dialog's own PID
                        subprocess.run(
                            ["cua-driver", "call", "hotkey"],
                            input=json.dumps({"pid": dialog_pid, "keys": ["Alt", "Y"], "delivery_mode": "foreground"}),
                            capture_output=True, text=True, errors="replace", timeout=15,
                        )
                    else:
                        # Fallback to browser PID
                        subprocess.run(
                            ["cua-driver", "call", "hotkey"],
                            input=json.dumps({"pid": pid, "keys": ["Alt", "Y"]}),
                            capture_output=True, text=True, errors="replace", timeout=15,
                        )
                    time.sleep(1)
                    found = True
                    break
            if not found:
                return  # No overwrite dialog, we're done
        except (json.JSONDecodeError, subprocess.TimeoutExpired, OSError):
            pass
        time.sleep(1)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Batch download missing Notion pages")
    parser.add_argument(
        "--source", choices=["report", "missing"], default="missing",
        help="Source of URLs: 'report' = _report.md unresolved links, 'missing' = _missing_downloads.md table (default)"
    )
    parser.add_argument(
        "--missing-file", default=None,
        help="Override the missing-downloads file path (e.g. '_missing_downloads_batch2.md')"
    )
    args = parser.parse_args()

    if args.missing_file:
        global MISSING_DOWNLOADS
        MISSING_DOWNLOADS = OUT_VAULT / args.missing_file

    urls = get_urls(source=args.source)
    print(f"Source: _{args.source}.md")
    print(f"Found {len(urls)} name-based pages to download")

    # Check download log for already-processed URLs
    downloaded_ids = set()
    log_path = ROOT / "download_log.txt"
    if log_path.exists():
        for line in log_path.read_text().splitlines():
            parts = line.split("\t")
            if len(parts) >= 2:
                downloaded_ids.add(parts[1])  # URL is at index 1

    todo = []
    for url, uid, name in urls:
        if url not in downloaded_ids:
            todo.append((url, uid, name))

    print(f"Already in log: {len(downloaded_ids)}")
    print(f"Already downloaded: {len(urls) - len(todo)}")
    print(f"Remaining to download: {len(todo)}")
    print()

    if not todo:
        print("All pages already downloaded!")
        return

    # Find Brave PID
    pid = get_brave_pid()
    if pid is None:
        print("ERROR: Brave not running. Start Brave first.")
        sys.exit(1)
    print(f"Brave PID: {pid}")
    print()

    # Bring Brave to front
    cua_call("bring_to_front", {"pid": pid})
    time.sleep(0.5)

    # Process each URL
    success = 0
    fail = 0
    skipped_not_found = 0
    skipped_no_permission = 0

    for i, (url, uid, name) in enumerate(todo, 1):
        print(f"[{i}/{len(todo)}] {name} ... ", end="", flush=True)
        status = "FAIL"

        try:
            status = save_notion_page(pid, url, first_page=(i == 1))

            if status == "ok":
                before = {f for f in ROOT.glob("*.mhtml")}
                time.sleep(1)
                after = {f for f in ROOT.glob("*.mhtml")}
                new_files = after - before
                if new_files:
                    print(f"[OK] ({new_files.pop().name})")
                else:
                    print("[OK] (file not detected in folder)")
                success += 1
            elif status == "skip_not_found":
                print("[SKIP] Page not found")
                skipped_not_found += 1
            elif status == "skip_no_permission":
                print("[SKIP] No permission")
                skipped_no_permission += 1
            else:
                print("[FAIL] cua-driver error")
                fail += 1
        except Exception as e:
            print(f"[FAIL] {e}")
            fail += 1

        # Log progress
        with open(log_path, "a") as f:
            f.write(f"{status}\t{url}\t{name}\n")

        # Small delay between pages
        if i < len(todo):
            time.sleep(1)

    print()
    print("=" * 50)
    print(f"Done! Success: {success}, Failed: {fail}, "
          f"Not found: {skipped_not_found}, No permission: {skipped_no_permission}")
    print(f"Log saved to: {log_path}")


if __name__ == "__main__":
    main()
