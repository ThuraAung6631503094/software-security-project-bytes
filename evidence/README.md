# Evidence

Everything here must come from **our own** local runs, using our team's `TEAM_ID`.

## Layout

```
evidence/
├── baseline/              Normal behaviour of the unmodified app (login, notes, search, admin)
├── <ID>/                  One folder per finding, created by its owner, e.g. evidence/INJ-01/
│   ├── exploit.txt        Request(s) and response(s) proving the issue on vulnerable-baseline
│   ├── exploit.png        Screenshot of the same
│   ├── fixed.txt          The same attack re-run after the fix, showing it is blocked
│   └── fixed.png          Screenshot of the same
├── ci/                    CI screenshots: failing run on the baseline, passing run after fixes
└── supply-chain/          sbom.json, image digest, cosign verify output, cosign.pub
```

Extra files are fine (e.g. `control.txt` for a normal request, `sqlmap.txt`, a Burp export).

## What every `.txt` log starts with

```
Finding:   <ID> — <title>
Captured:  <date and time>
Commit:    <git rev-parse HEAD>
Target:    <method and URL>
```

Then: the **control** (a normal request and its result), the **attack** (exact payload and
result), and a one-line conclusion.

## Rules

- Redact real session tokens and secrets (`eyJ…<redacted>`). Never commit `cosign.key`.
- Capture exploits against the `vulnerable-baseline` tag, not a branch with fixes.
- Do not commit large binaries (image `.tar` exports); record the digest instead.
