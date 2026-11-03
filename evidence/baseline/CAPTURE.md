# Baseline capture — normal behaviour

Shows the app working normally on the unmodified starter (tag `vulnerable-baseline`), so the
findings are read against a known-good baseline. Capture these **before** any fix is merged.

Run the app first (PowerShell, from `project/starter-app`):

```powershell
$env:TEAM_ID="TEAM_BYTES"; docker compose up --build
```

Then open <http://localhost:8080> and take these screenshots. Save each PNG in this folder
with the exact name in the table.

| # | Filename | What to show |
|---|---|---|
| 1 | `01-login-page.png` | The home page while logged out (login + register forms) |
| 2 | `02-alice-logged-in.png` | Signed in as `alice` / `alicepw`, showing her notes |
| 3 | `03-add-note.png` | After adding a note as alice (a normal note like "test / hello") |
| 4 | `04-search.png` | Searching alice's notes for `milk` and getting the groceries note |
| 5 | `05-admin-panel.png` | Signed in as `admin` / `admin123`, the `/admin` JSON page |

Record the baseline commit once, so every finding can reference it:

```powershell
git rev-parse vulnerable-baseline   # paste the hash into each evidence log's "Commit:" line
```
