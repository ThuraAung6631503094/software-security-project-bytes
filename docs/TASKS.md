# Task split

Each person owns their findings **end to end**: exploit → evidence → fix → proof the fix works
→ report section → demo. In the Week 19 Q&A you will be asked about *your own* fixes.

| | Person 1 | Person 2 | Person 3 |
|---|---|---|---|
| Area | Repo lead · authentication, sessions & crypto | Access control & input handling | Platform, CI & supply chain |
| Findings | AUTH-01…05, INFO-01 | AC-01…03, INJ-01…03 | INJ-04, CFG-01, CFG-02, SC-01, SEC-01 |
| Threat model | STRIDE rows (auth) + assemble table + top-5 ranking | DFD + STRIDE rows (data access) | STRIDE rows (platform/CI) + CI trust boundaries on DFD |
| Report | §1, §4/§5 for own findings | §2, §4/§5 for own findings, final editor | §6, §7, §4/§5 for own findings |
| Extra | Repo setup, conventions, PR reviews | — | CI pipeline, SBOM, Cosign, demo video edit |

## Finding register

Severity is provisional until each owner scores it (CVSS vector in the report).

| ID | Finding | Location | Owner | Evidence | Fixed |
|---|---|---|---|---|---|
| AUTH-01 | Session token forgeable (hard-coded secret, `none` allowed) and never expires | `app.py` `SECRET`, `current_user()` | P1 | ☐ | ☐ |
| AUTH-02 | SQL injection in `/login` | `login()` | P1 | ☐ | ☐ |
| AUTH-03 | Passwords stored as unsalted MD5 | `seed()`, `register()`, `login()` | P1 | ☐ | ☐ |
| AUTH-04 | Session cookie lacks `HttpOnly` / `Secure` / `SameSite` | `login()` `set_cookie` | P1 | ☐ | ☐ |
| AUTH-05 | No CSRF protection on state-changing POSTs | `PAGE` forms, POST routes | P1 | ☐ | ☐ |
| INFO-01 | `/admin` returns every user's password hash | `admin()` | P1 | ☐ | ☐ |
| AC-01 | Client chooses its own role at registration (mass assignment) | `register()` | P2 | ☐ | ☐ |
| AC-02 | Duplicate usernames allow account takeover (incl. `admin`) | `users` schema, `register()` | P2 | ☐ | ☐ |
| AC-03 | Any user can read any note by ID (IDOR / BOLA) | `api_note()` | P2 | ☐ | ☐ |
| INJ-01 | SQL injection in `/search` | `search()` | P2 | ☐ | ☐ |
| INJ-02 | Stored XSS through `notes_html|safe` | `PAGE`, `home()` | P2 | ☐ | ☐ |
| INJ-03 | Server-side template injection in `/search` → code execution | `search()` `render_template_string` | P2 | ☐ | ☐ |
| INJ-04 | OS command injection in `/export` | `export()` | P3 | ☐ | ☐ |
| CFG-01 | Debug mode on, binds all interfaces, port published to the network, unhandled errors | `app.run`, `docker-compose.yml`, `register()` | P3 | ☐ | ☐ |
| CFG-02 | Container runs as root, unpinned base, `COPY . .`, secret in `ENV` | `Dockerfile` | P3 | ☐ | ☐ |
| SC-01 | Outdated / vulnerable dependencies, unused packages | `requirements.txt` | P3 | ☐ | ☐ |
| SEC-01 | Password hashes committed to the repo and copied into the image | `project_hashes.txt` | P3 | ☐ | ☐ |

Found something else? Add a row with the next free ID in its category and tell the team.

---

## Person 1 — repo lead · authentication, sessions & crypto

**Phase 0 — setup (now)**
- [ ] Repo created, baseline committed and tagged `vulnerable-baseline`
- [ ] Repo skeleton merged (this PR)
- [ ] Invite Person 2 and Person 3 as collaborators
- [ ] Protect `main` (require PR + 1 approval) or agree on the no-direct-push rule
- [ ] Fill in names / IDs in `README.md` and `REPORT.md` cover
- [ ] Agree `TEAM_ID` with the team

**Phase 1 — evidence on the baseline**
- [ ] `evidence/baseline/`: normal login, add note, search, admin page (shared with team)
- [ ] AUTH-01: forge an admin token with the leaked secret; also try `alg: none` and record what PyJWT 1.7.1 actually does
- [ ] AUTH-02: login bypass; note what identity the resulting session has
- [ ] AUTH-03: show the stored MD5 values and how fast they crack
- [ ] AUTH-04: capture the `Set-Cookie` header
- [ ] AUTH-05: cross-origin POST to `/notes` succeeds without a token
- [ ] INFO-01: `/admin` JSON containing password hashes
- [ ] Optional demo chain: AUTH-02 login with a SQL payload as username → INJ-01 search returns every note

**Phase 2 — threat model (Week 7)**
- [ ] STRIDE rows for login, registration, session token, cookies
- [ ] Assemble `docs/threat-model/stride.md` and rank the top 5 risks

**Phase 3 — fixes (by Week 14, after SC-01 and INJ-02/03 are merged)**
- [ ] AUTH-01: secret from environment, `algorithms=["HS256"]` only, add `exp`
- [ ] AUTH-02: parameterized lookup by username, password checked in Python
- [ ] AUTH-03: adaptive password hashing (Werkzeug scrypt/pbkdf2 or Argon2)
- [ ] AUTH-04: `HttpOnly`, `SameSite`, `Secure` behind a config flag
- [ ] AUTH-05: Flask-WTF `CSRFProtect` + tokens in forms (keep the auth cookie name separate from Flask's session cookie)
- [ ] INFO-01: `/admin` selects only `id, username, role`
- [ ] `evidence/<ID>/fixed.*` for each

**Phase 4 — report & demo**
- [ ] §1 Executive summary, §4/§5 for own findings
- [ ] Demo segment: one attack → root cause → fix

## Person 2 — access control & input handling

**Phase 1 — evidence on the baseline**
- [ ] AC-01: register with `role=admin`, access `/admin`
- [ ] AC-02: register a second `admin` (or `alice`) with your own password, log in, show admin access / their notes
- [ ] AC-03: as Alice, read another user's note via `/api/notes/<id>`
- [ ] INJ-01: search payload that returns other users' notes; try a UNION that dumps the `users` table (sqlmap output welcome)
- [ ] INJ-02: stored script in a note executes on the home page
- [ ] INJ-03: note containing `{{7*7}}` renders as `49` in search; then a harmless proof of code execution (e.g. read `id`)

**Phase 2 — threat model (Week 7)**
- [ ] DFD in `docs/threat-model/` (image + editable source)
- [ ] STRIDE rows for notes, search, admin, note API

**Phase 3 — fixes (by Week 14, after SC-01 is merged)**
- [ ] AC-01: registration always assigns `user`
- [ ] AC-02: `UNIQUE` on `username`, return 409 on duplicates
- [ ] AC-03: query filters by note ID **and** owner
- [ ] INJ-01: parameterized search
- [ ] INJ-02 + INJ-03: pass rows to Jinja templates as data, no `|safe`, no string-built templates (merge **before** Person 1's CSRF form changes)
- [ ] `evidence/<ID>/fixed.*` for each

**Phase 4 — report & demo**
- [ ] §2 System scope + DFD, §4/§5 for own findings
- [ ] Final editor: consistent formatting, every evidence path in the report exists
- [ ] Demo segment: INJ-03 (SSTI) is the strongest one

## Person 3 — platform, CI & supply chain

**Phase 1 — evidence on the baseline**
- [ ] INJ-04: `/export?fmt=...` runs an extra harmless command (e.g. `id`)
- [ ] CFG-01: debug traceback (e.g. register with no password); app reachable on non-localhost interface
- [ ] CFG-02: `docker compose run --rm notevault id` shows root; `APP_SECRET` and `project_hashes.txt` present inside the image
- [ ] SC-01: Trivy (and/or pip-audit) report on `requirements.txt`
- [ ] SEC-01: Gitleaks / manual proof the committed hashes crack to the seed passwords
- [ ] **CI:** `.github/workflows/security-ci.yml` (Semgrep SAST, Trivy SCA + image, Gitleaks), fails on HIGH/CRITICAL; screenshot the **failing** run on the baseline → `evidence/ci/`

**Phase 2 — threat model (Week 7)**
- [ ] STRIDE rows for export/shell, container, dependencies, CI, releases
- [ ] Add repo → CI → image trust boundaries to the DFD

**Phase 3 — fixes & hardening (by Week 14)**
- [ ] SC-01 **first**: upgrade dependencies, drop unused `requests`/`urllib3` (tell the team when merged — PyJWT 2.x changes `jwt.encode`)
- [ ] INJ-04: allowlist formats, no shell
- [ ] CFG-01: `debug=False`, host/port from env, compose binds `127.0.0.1`, error handlers
- [ ] CFG-02: base pinned by digest, non-root user, `.dockerignore`, no `ENV` secret, minimal `COPY`
- [ ] SEC-01: delete `project_hashes.txt`; explain it remains in history and why the seed passwords change
- [ ] SBOM (CycloneDX) → `evidence/supply-chain/sbom.json`
- [ ] Sign the release with Cosign, verify, save output (private key never committed)
- [ ] CI green on `main`; screenshot → `evidence/ci/`

**Phase 4 — report & demo**
- [ ] §6 Supply chain (incl. SLSA self-assessment), §7 CI, §4/§5 for own findings
- [ ] Edit the final demo video from everyone's segments

## Everyone

- [ ] §3 STRIDE rows for your area
- [ ] §8 Conclusion & reflection, AI-tool disclosure, appendix task split (written together, past tense)
- [ ] Review at least one teammate PR per week
- [ ] Week 16: live WIP demo · Week 19: recorded video + 3-minute live Q&A
- [ ] Private peer-contribution rating at submission

## Milestones

| Milestone | Due |
|---|---|
| Team + target chosen, repo set up | Week 4 |
| All baseline evidence captured, CI failing on baseline | Before any fix merges |
| Threat model | Week 7 |
| Vulnerability report draft | Week 11 |
| Remediation + SBOM + signed artifact | Week 14 |
| WIP demo & peer review | Week 16 |
| Final report + recorded demo + Q&A | Week 19 |
