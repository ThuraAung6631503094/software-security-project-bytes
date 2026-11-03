# Threat model

Working area for the threat model. The final version goes into `REPORT.md` §2 and §3.

| File | Owner | Content |
|---|---|---|
| `dfd.png` (+ editable source, e.g. `dfd.drawio`) | Person 2 | Data-flow diagram: external entities, processes, data stores, data flows, trust boundaries |
| `stride.md` | Person 1 assembles, all contribute | STRIDE table, one row per element / data flow, plus the top-5 risk ranking |

## What the DFD must show

- External entities: the user's browser; the developer pushing to GitHub.
- Processes: the Flask app (`app.py`); the shell spawned by `/export`; the CI runner.
- Data stores: the SQLite database (`/tmp/notevault.db`); the Docker image; the Git repository.
- Every trust boundary a request or artifact crosses, labelled.

## STRIDE row owners

| Area | Owner |
|---|---|
| Login, registration, session token, cookies | Person 1 |
| Notes, search, admin, note API | Person 2 |
| Export / shell, container, CI pipeline, dependencies, releases | Person 3 |
