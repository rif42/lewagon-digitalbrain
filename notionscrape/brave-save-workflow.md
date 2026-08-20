# Brave Save Page Workflow (via cua-driver CLI)

Save a Notion page from Brave as `.mhtml` using keyboard automation via `cua-driver` CLI.

## Prerequisites

- Brave browser running (PID known)
- cua-driver CLI installed and running
- URL copied to clipboard before step 3

## Sequence

| Step | Action | Description |
|------|--------|-------------|
| 1 | `bring_to_front` | Bring Brave window to foreground |
| 2 | `Ctrl+T` | Open a new tab |
| 3 | `Ctrl+L` → `Ctrl+V` → `Enter` | Focus address bar, paste URL, navigate |
| 4 | Sleep **6s** | Wait for Notion page to fully load |
| 5 | `Ctrl+S` | Open Save As dialog directly (native Brave shortcut) |
| 6 | Sleep **1.5s** | Wait for dialog to appear |
| 7 | `Alt+S` | Confirm save (Windows Save button accelerator) |

## CLI Commands

```bash
# 1. Bring Brave to front
echo '{"pid":<PID>}' | cua-driver call bring_to_front

# 2. Navigate to URL (copy URL to clipboard first)
echo -n "<URL>" | clip
echo '{"pid":<PID>,"keys":["Ctrl","L"],"delivery_mode":"foreground"}' | cua-driver call hotkey
echo '{"pid":<PID>,"keys":["Ctrl","V"],"delivery_mode":"foreground"}' | cua-driver call hotkey
echo '{"pid":<PID>,"keys":["Enter"],"delivery_mode":"foreground"}' | cua-driver call hotkey

# 3. Wait for page load
sleep 6

# 4. Open Save As dialog (Ctrl+S)
echo '{"pid":<PID>,"keys":["Ctrl","S"],"delivery_mode":"foreground"}' | cua-driver call hotkey

# 5. Wait for dialog
sleep 1.5

# 6. Confirm save (Alt+S)
echo '{"pid":<PID>,"keys":["Alt","S"],"delivery_mode":"foreground"}' | cua-driver call hotkey
```

## Notes

- `Ctrl+S` opens the Save As dialog directly (native Chromium shortcut) — no need for the Alt+F menu navigation.
- `Alt+S` is the Windows Save button accelerator; plain `Enter` does **not** confirm the dialog.
- The save target directory is Brave's default download location (usually `~/Downloads`) unless previously changed.
- Replace `<PID>` with Brave's process ID (find via `cua-driver call --tool list_apps`).
- For batch processing, reuse the same tab: just repeat the navigation + save steps.
