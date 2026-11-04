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

| Element / data flow | Threat (STRIDE) | How it applies here | Finding(s) | Mitigation |
|---|---|---|---|---|
| Browser → `/export` → shell | **E**levation / **T**ampering | User-controlled `fmt` reaches `subprocess(..., shell=True)` → OS command execution | INJ-04 | Allowlist formats; no shell; argument-list exec |
| Flask app runtime (process/host) | **I**nformation disclosure / **D**enial of service | `debug=True` leaks tracebacks and source; app bound 0.0.0.0 and published on all interfaces | CFG-01 | `debug=False`; bind localhost; error handlers |
| Container image | **E**levation of privilege / **I**nformation disclosure | Runs as root; unpinned base; `COPY . .`; secret baked in `ENV` | CFG-02 | Non-root user; pin base by digest; `.dockerignore`; no baked secret |
| Repository → image (dependencies) | **T**ampering (supply chain) | Outdated, vulnerable, and unused Python packages pulled into the image | SC-01 | Upgrade/trim deps; SCA gate in CI; SBOM |
| Repository / image (secrets) | **I**nformation disclosure | Seed password hashes committed to git and shipped in the image | SEC-01 | Remove file; rotate seed creds; secret scanning in CI |
| CI runner → released image/artifacts | **T**ampering / **R**epudiation | Without scanning/signing, a tampered build or dependency can ship unnoticed | CI, supply chain | SAST+SCA+secret gates failing on HIGH/CRITICAL; Cosign-signed artifact; pinned actions |

## Top-5 risk ranking (likelihood × impact)
<!-- Person 1 assembles this once all rows are in. -->

| Rank | Risk | Likelihood | Impact | Rating | Why |
|---|---|---|---|---|---|
| _TODO_ | | | | | |
