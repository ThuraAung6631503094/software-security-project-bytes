# How we work

## Golden rules

1. **Evidence first, fixes second.** Every exploit is captured against `vulnerable-baseline`
   before any fix for it is merged. Once a fix lands, the attack no longer works.
2. **Never push straight to `main`.** Everything goes through a pull request reviewed by
   another member.
3. **One finding per branch, per pull request.** Commit as yourself; your history is part of
   how individual contribution is checked.
4. **Do not copy** text, tables, payloads or evidence from other teams or reference reports.
5. **No secrets in Git.** No real tokens, private keys (`cosign.key`) or `.env` files. Redact
   session tokens in evidence logs.

## Branch names

| Kind | Pattern | Example |
|---|---|---|
| Evidence capture | `evidence/<ID>` or `evidence/<name>` | `evidence/inj-01` |
| Fix | `fix/<id>-<short-name>` | `fix/ac-03-note-ownership` |
| CI / build | `ci/<short-name>` | `ci/security-pipeline` |
| Docs / report | `docs/<short-name>` | `docs/threat-model` |
| Housekeeping | `chore/<short-name>` | `chore/repo-skeleton` |

## Commit messages

Start with the finding ID (or the area), then say what changed in the imperative:

```
INJ-01: parameterize search query
AUTH-04: set HttpOnly, Secure and SameSite on the session cookie
docs: add STRIDE rows for access-control flows
```

## Daily workflow

```bash
git checkout main
git pull
git checkout -b fix/inj-01-search-sqli
# ...change, test, re-run the exploit...
git add starter-app/app.py evidence/INJ-01/
git commit -m "INJ-01: parameterize search query"
git push -u origin fix/inj-01-search-sqli
# open a pull request on GitHub, ask a teammate to review, then merge
```

Keep your branch current while it is open: `git pull origin main` (merge) or
`git rebase origin/main`.

## Merge order for fixes

`app.py` is shared, so merge small pull requests often and follow this order:

1. **Person 3** — dependency upgrade (SC-01). Everyone else builds fixes on the new versions.
2. **Person 2** — template rendering fixes (INJ-02, INJ-03).
3. **Person 1** — CSRF, cookies, password hashing (AUTH-03…05).
4. Everything else in any order.

## Evidence rules

See [evidence/README.md](evidence/README.md). In short: one folder per finding ID, a `.txt`
request/response log plus a `.png` screenshot for both the exploit and the blocked retry, and
the commit hash the evidence was captured against.
