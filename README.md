# NoteVault — Secure Build (Team Bytes)

Term project for the Software Security course: assess the **NoteVault** starter app like an
attacker, fix it like a defender, and harden its build and release pipeline.

> ⚠️ **Sandbox only.** NoteVault is intentionally vulnerable. Run it on your own machine
> (`localhost`) and never deploy it or test anything outside the local sandbox.

## Team

| Role | Member | Area |
|---|---|---|
| Person 1 | _name + student ID_ | Repo lead · authentication, sessions & crypto |
| Person 2 | _name + student ID_ | Access control & input handling |
| Person 3 | _name + student ID_ | Platform, CI & supply chain |

Who does what: [docs/TASKS.md](docs/TASKS.md) · How we work: [CONTRIBUTING.md](CONTRIBUTING.md)

## Repository layout

```
.
├── starter-app/            NoteVault source (app.py, Dockerfile, compose, requirements)
├── evidence/               Exploit and fix evidence, one folder per finding ID
│   ├── baseline/           Normal behaviour of the unmodified app
│   ├── ci/                 CI run screenshots (failing baseline, passing final)
│   └── supply-chain/       SBOM, image digest, Cosign verify output
├── docs/
│   ├── TASKS.md            Task split and finding register
│   ├── threat-model/       DFD image and STRIDE working notes
│   └── course/             Original project instructions and report template
├── REPORT.md               Final report (fill in section by section)
└── CONTRIBUTING.md         Branches, commits, pull requests, evidence rules
```

## Baseline

The unmodified starter app is tagged **`vulnerable-baseline`**. All exploit evidence is
captured against that tag. To look at the original code at any time:

```bash
git checkout vulnerable-baseline      # read-only look; return with: git checkout main
git diff vulnerable-baseline main -- starter-app/
```

## Run it locally

All three members must use the **same** `TEAM_ID` so every screenshot carries the same marker.

PowerShell:

```powershell
cd starter-app
$env:TEAM_ID="<team-id>"; docker compose up --build
```

Git Bash:

```bash
cd starter-app
export TEAM_ID=<team-id> && docker compose up --build
```

Open <http://localhost:8080>. Seeded sandbox accounts: `alice` / `alicepw`, `admin` / `admin123`.

## Deliverables

| Deliverable | Where |
|---|---|
| Threat model (DFD + STRIDE) | `docs/threat-model/`, `REPORT.md` §2–3 |
| Vulnerability findings | `evidence/<ID>/`, `REPORT.md` §4 |
| Remediated code | `starter-app/`, one PR per finding |
| SBOM + Cosign signature | `evidence/supply-chain/`, `REPORT.md` §6 |
| Security CI pipeline | `.github/workflows/`, `REPORT.md` §7 |
| Demo | Week 16 WIP studio, Week 19 recorded video + live Q&A |

Course brief: [docs/course/PROJECT-INSTRUCTIONS.md](docs/course/PROJECT-INSTRUCTIONS.md)
