## What this changes

<!-- One finding per PR. Example: "INJ-01: parameterize the /search query". -->

- Finding ID(s):
- Type: evidence / fix / CI / docs / chore

## For fixes

- **Root cause:**
- **Why this fix (and not an alternative):**
- **Exploit evidence (before):** `evidence/<ID>/exploit.*`
- **Blocked evidence (after):** `evidence/<ID>/fixed.*`

## Checklist

- [ ] Exploit evidence for this finding was already captured against `vulnerable-baseline`
- [ ] The original attack was re-run on this branch and is now blocked
- [ ] Normal behaviour still works (login, add note, search)
- [ ] No secrets, private keys or unredacted tokens committed
- [ ] `REPORT.md` section updated (or a follow-up PR is noted)
