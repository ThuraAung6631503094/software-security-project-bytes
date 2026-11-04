# STRIDE analysis

Shared file — each owner fills the rows for their area; Person 1 assembles the full table and
the top-5 ranking for REPORT.md §3. STRIDE = Spoofing, Tampering, Repudiation, Information
disclosure, Denial of service, Elevation of privilege.

## Elements / data flows

### Person 2 — access control & input handling (notes, search, admin, note API)

| Element / data flow | Threat (STRIDE) | How it applies here | Finding(s) | Mitigation |
|---|---|---|---|---|
| Browser → `/register` | **E**levation of privilege | Client supplies `role=admin`; duplicate usernames inherit a privileged row | AC-01, AC-02 | Server fixes role to `user`; `UNIQUE` username |
| Browser → `/api/notes/<id>` | **I**nformation disclosure | Authenticated user reads another user's note by ID (no ownership check) | AC-03 | Filter by note ID **and** owner |
| Browser → `/search` | **I**nformation disclosure / **E**levation | SQL injection crosses the owner filter; SSTI evaluates stored expressions server-side | INJ-01, INJ-03 | Parameterized query; render rows as template **data**, not a built template string |
| Browser → `/notes` (create) | **T**ampering / **E**levation | Stored note content is rendered unescaped, executing as script in the viewer's browser | INJ-02 | Contextual output escaping; no `\|safe` |
| Flask → SQLite (notes) | **I**nformation disclosure / **T**ampering | Injected SQL reads or alters rows outside the user's scope | INJ-01, AC-03 | Parameterized queries, least-privilege data access |
| Browser → `/admin` | **R**epudiation | Admin reads of all users are not logged | (hardening) | Add server-side audit logging of admin actions |

### Person 1 — authentication, sessions & crypto
<!-- Person 1: add rows for login, registration auth, session token, cookies (AUTH-01..05, INFO-01). -->
| Element / data flow | Threat (STRIDE) | How it applies here | Finding(s) | Mitigation |
|---|---|---|---|---|
| _TODO_ | | | | |

### Person 3 — platform, CI & supply chain
<!-- Person 3: add rows for export/shell, container, dependencies, CI, releases (INJ-04, CFG-01/02, SC-01, SEC-01). -->
| Element / data flow | Threat (STRIDE) | How it applies here | Finding(s) | Mitigation |
|---|---|---|---|---|
| _TODO_ | | | | |

## Top-5 risk ranking (likelihood × impact)
<!-- Person 1 assembles this once all rows are in. -->

| Rank | Risk | Likelihood | Impact | Rating | Why |
|---|---|---|---|---|---|
| _TODO_ | | | | | |
