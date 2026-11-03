# Term Project Report — Secure Build

> Fill in every section and keep the headings. Each section names its owner in an HTML
> comment; the owner drafts it, a teammate reviews it. Remove the comments before submission.

## Cover

| Field | Value |
|---|---|
| Team name | Bytes |
| Members (name + ID) | |
| Target application | NoteVault (course starter app) |
| Repository URL | https://github.com/ThuraAung6631503094/software-security-project-bytes |
| Baseline | tag `vulnerable-baseline` |
| Date | |

## AI-tool usage disclosure
<!-- Owner: everyone. Each member lists the tools they used and how. "None" is valid. -->

| Tool | Who | How it was used |
|---|---|---|
| | | |

---

## 1. Executive Summary
<!-- Owner: Person 1. Half a page: what the app is, findings by severity, risk before vs. after. Write last. -->

---

## 2. System Scope & Function
<!-- Owner: Person 2. What the app does, in-scope components and endpoints, DFD image from docs/threat-model/. -->

---

## 3. Threat Model — STRIDE  *(20 pts)*
<!-- Owner: Person 1 assembles; rows from all three (see docs/threat-model/README.md). -->

| Element / data flow | S | T | R | I | D | E | Top threat & mitigation |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

**Top 5 risks (likelihood × impact)**

| Rank | Risk | Likelihood | Impact | Rating | Why |
|---|---|---|---|---|---|
| 1 | | | | | |

---

## 4. Vulnerability Findings  *(25 pts)*
<!-- Each owner fills their own blocks. Severity from a CVSS vector; OWASP Top 10:2025 numbering. -->

### Person 1 — authentication, sessions & crypto

#### AUTH-01 — Session token forgeable and never expires

| Field | Value |
|---|---|
| CWE | |
| OWASP 2025 | |
| Severity | |
| CVSS vector | |
| Location | |
| Reproduction | |
| Impact | |
| Evidence | `evidence/AUTH-01/exploit.txt`, `evidence/AUTH-01/exploit.png` |

**Root cause:**

#### AUTH-02 — SQL injection in login

| Field | Value |
|---|---|
| CWE | |
| OWASP 2025 | |
| Severity | |
| CVSS vector | |
| Location | |
| Reproduction | |
| Impact | |
| Evidence | `evidence/AUTH-02/exploit.txt`, `evidence/AUTH-02/exploit.png` |

**Root cause:**

#### AUTH-03 — Passwords stored as unsalted MD5

| Field | Value |
|---|---|
| CWE | |
| OWASP 2025 | |
| Severity | |
| CVSS vector | |
| Location | |
| Reproduction | |
| Impact | |
| Evidence | `evidence/AUTH-03/exploit.txt`, `evidence/AUTH-03/exploit.png` |

**Root cause:**

#### AUTH-04 — Session cookie missing security attributes

| Field | Value |
|---|---|
| CWE | |
| OWASP 2025 | |
| Severity | |
| CVSS vector | |
| Location | |
| Reproduction | |
| Impact | |
| Evidence | `evidence/AUTH-04/exploit.txt`, `evidence/AUTH-04/exploit.png` |

**Root cause:**

#### AUTH-05 — No CSRF protection

| Field | Value |
|---|---|
| CWE | |
| OWASP 2025 | |
| Severity | |
| CVSS vector | |
| Location | |
| Reproduction | |
| Impact | |
| Evidence | `evidence/AUTH-05/exploit.txt`, `evidence/AUTH-05/exploit.png` |

**Root cause:**

#### INFO-01 — Admin endpoint discloses password hashes

| Field | Value |
|---|---|
| CWE | |
| OWASP 2025 | |
| Severity | |
| CVSS vector | |
| Location | |
| Reproduction | |
| Impact | |
| Evidence | `evidence/INFO-01/exploit.txt`, `evidence/INFO-01/exploit.png` |

**Root cause:**

### Person 2 — access control & input handling

#### AC-01 — Client-chosen role at registration

| Field | Value |
|---|---|
| CWE | |
| OWASP 2025 | |
| Severity | |
| CVSS vector | |
| Location | |
| Reproduction | |
| Impact | |
| Evidence | `evidence/AC-01/exploit.txt`, `evidence/AC-01/exploit.png` |

**Root cause:**

#### AC-02 — Account takeover through duplicate usernames

| Field | Value |
|---|---|
| CWE | |
| OWASP 2025 | |
| Severity | |
| CVSS vector | |
| Location | |
| Reproduction | |
| Impact | |
| Evidence | `evidence/AC-02/exploit.txt`, `evidence/AC-02/exploit.png` |

**Root cause:**

#### AC-03 — Insecure direct object reference on notes API

| Field | Value |
|---|---|
| CWE | |
| OWASP 2025 | |
| Severity | |
| CVSS vector | |
| Location | |
| Reproduction | |
| Impact | |
| Evidence | `evidence/AC-03/exploit.txt`, `evidence/AC-03/exploit.png` |

**Root cause:**

#### INJ-01 — SQL injection in search

| Field | Value |
|---|---|
| CWE | |
| OWASP 2025 | |
| Severity | |
| CVSS vector | |
| Location | |
| Reproduction | |
| Impact | |
| Evidence | `evidence/INJ-01/exploit.txt`, `evidence/INJ-01/exploit.png` |

**Root cause:**

#### INJ-02 — Stored cross-site scripting

| Field | Value |
|---|---|
| CWE | |
| OWASP 2025 | |
| Severity | |
| CVSS vector | |
| Location | |
| Reproduction | |
| Impact | |
| Evidence | `evidence/INJ-02/exploit.txt`, `evidence/INJ-02/exploit.png` |

**Root cause:**

#### INJ-03 — Server-side template injection in search

| Field | Value |
|---|---|
| CWE | |
| OWASP 2025 | |
| Severity | |
| CVSS vector | |
| Location | |
| Reproduction | |
| Impact | |
| Evidence | `evidence/INJ-03/exploit.txt`, `evidence/INJ-03/exploit.png` |

**Root cause:**

### Person 3 — platform & supply chain

#### INJ-04 — OS command injection in export

| Field | Value |
|---|---|
| CWE | |
| OWASP 2025 | |
| Severity | |
| CVSS vector | |
| Location | |
| Reproduction | |
| Impact | |
| Evidence | `evidence/INJ-04/exploit.txt`, `evidence/INJ-04/exploit.png` |

**Root cause:**

#### CFG-01 — Debug mode and network exposure

| Field | Value |
|---|---|
| CWE | |
| OWASP 2025 | |
| Severity | |
| CVSS vector | |
| Location | |
| Reproduction | |
| Impact | |
| Evidence | `evidence/CFG-01/exploit.txt`, `evidence/CFG-01/exploit.png` |

**Root cause:**

#### CFG-02 — Insecure container image

| Field | Value |
|---|---|
| CWE | |
| OWASP 2025 | |
| Severity | |
| CVSS vector | |
| Location | |
| Reproduction | |
| Impact | |
| Evidence | `evidence/CFG-02/exploit.txt`, `evidence/CFG-02/exploit.png` |

**Root cause:**

#### SC-01 — Vulnerable and unused dependencies

| Field | Value |
|---|---|
| CWE | |
| OWASP 2025 | |
| Severity | |
| CVSS vector | |
| Location | |
| Reproduction | |
| Impact | |
| Evidence | `evidence/SC-01/exploit.txt`, `evidence/SC-01/exploit.png` |

**Root cause:**

#### SEC-01 — Password hashes committed to the repository

| Field | Value |
|---|---|
| CWE | |
| OWASP 2025 | |
| Severity | |
| CVSS vector | |
| Location | |
| Reproduction | |
| Impact | |
| Evidence | `evidence/SEC-01/exploit.txt`, `evidence/SEC-01/exploit.png` |

**Root cause:**

---

## 5. Remediation  *(25 pts)*
<!-- Each owner fills their own blocks: before/after code, reasoning, commit, proof. -->

### Person 1 — authentication, sessions & crypto

#### Fix for AUTH-01

```diff
- 
+ 
```
- **Why this fixes it:**
- **Why this approach (and not an alternative):**
- **Commit / PR:**
- **Proof the exploit now fails:** `evidence/AUTH-01/fixed.txt`, `evidence/AUTH-01/fixed.png`

#### Fix for AUTH-02

```diff
- 
+ 
```
- **Why this fixes it:**
- **Why this approach (and not an alternative):**
- **Commit / PR:**
- **Proof the exploit now fails:** `evidence/AUTH-02/fixed.txt`, `evidence/AUTH-02/fixed.png`

#### Fix for AUTH-03

```diff
- 
+ 
```
- **Why this fixes it:**
- **Why this approach (and not an alternative):**
- **Commit / PR:**
- **Proof the exploit now fails:** `evidence/AUTH-03/fixed.txt`, `evidence/AUTH-03/fixed.png`

#### Fix for AUTH-04

```diff
- 
+ 
```
- **Why this fixes it:**
- **Why this approach (and not an alternative):**
- **Commit / PR:**
- **Proof the exploit now fails:** `evidence/AUTH-04/fixed.txt`, `evidence/AUTH-04/fixed.png`

#### Fix for AUTH-05

```diff
- 
+ 
```
- **Why this fixes it:**
- **Why this approach (and not an alternative):**
- **Commit / PR:**
- **Proof the exploit now fails:** `evidence/AUTH-05/fixed.txt`, `evidence/AUTH-05/fixed.png`

#### Fix for INFO-01

```diff
- 
+ 
```
- **Why this fixes it:**
- **Why this approach (and not an alternative):**
- **Commit / PR:**
- **Proof the exploit now fails:** `evidence/INFO-01/fixed.txt`, `evidence/INFO-01/fixed.png`

### Person 2 — access control & input handling

#### Fix for AC-01

```diff
- 
+ 
```
- **Why this fixes it:**
- **Why this approach (and not an alternative):**
- **Commit / PR:**
- **Proof the exploit now fails:** `evidence/AC-01/fixed.txt`, `evidence/AC-01/fixed.png`

#### Fix for AC-02

```diff
- 
+ 
```
- **Why this fixes it:**
- **Why this approach (and not an alternative):**
- **Commit / PR:**
- **Proof the exploit now fails:** `evidence/AC-02/fixed.txt`, `evidence/AC-02/fixed.png`

#### Fix for AC-03

```diff
- 
+ 
```
- **Why this fixes it:**
- **Why this approach (and not an alternative):**
- **Commit / PR:**
- **Proof the exploit now fails:** `evidence/AC-03/fixed.txt`, `evidence/AC-03/fixed.png`

#### Fix for INJ-01

```diff
- 
+ 
```
- **Why this fixes it:**
- **Why this approach (and not an alternative):**
- **Commit / PR:**
- **Proof the exploit now fails:** `evidence/INJ-01/fixed.txt`, `evidence/INJ-01/fixed.png`

#### Fix for INJ-02

```diff
- 
+ 
```
- **Why this fixes it:**
- **Why this approach (and not an alternative):**
- **Commit / PR:**
- **Proof the exploit now fails:** `evidence/INJ-02/fixed.txt`, `evidence/INJ-02/fixed.png`

#### Fix for INJ-03

```diff
- 
+ 
```
- **Why this fixes it:**
- **Why this approach (and not an alternative):**
- **Commit / PR:**
- **Proof the exploit now fails:** `evidence/INJ-03/fixed.txt`, `evidence/INJ-03/fixed.png`

### Person 3 — platform & supply chain

#### Fix for INJ-04

```diff
- 
+ 
```
- **Why this fixes it:**
- **Why this approach (and not an alternative):**
- **Commit / PR:**
- **Proof the exploit now fails:** `evidence/INJ-04/fixed.txt`, `evidence/INJ-04/fixed.png`

#### Fix for CFG-01

```diff
- 
+ 
```
- **Why this fixes it:**
- **Why this approach (and not an alternative):**
- **Commit / PR:**
- **Proof the exploit now fails:** `evidence/CFG-01/fixed.txt`, `evidence/CFG-01/fixed.png`

#### Fix for CFG-02

```diff
- 
+ 
```
- **Why this fixes it:**
- **Why this approach (and not an alternative):**
- **Commit / PR:**
- **Proof the exploit now fails:** `evidence/CFG-02/fixed.txt`, `evidence/CFG-02/fixed.png`

#### Fix for SC-01

```diff
- 
+ 
```
- **Why this fixes it:**
- **Why this approach (and not an alternative):**
- **Commit / PR:**
- **Proof the exploit now fails:** `evidence/SC-01/fixed.txt`, `evidence/SC-01/fixed.png`

#### Fix for SEC-01

```diff
- 
+ 
```
- **Why this fixes it:**
- **Why this approach (and not an alternative):**
- **Commit / PR:**
- **Proof the exploit now fails:** `evidence/SEC-01/fixed.txt`, `evidence/SEC-01/fixed.png`

---

## 6. Supply-Chain Hardening  *(15 pts)*
<!-- Owner: Person 3. -->
- **SBOM (CycloneDX):** `evidence/supply-chain/sbom.json`, component count:
- **Artifact signed & verified with Cosign:** paste the `cosign verify` output
- **SLSA self-assessment:**

---

## 7. Security CI Pipeline  *(10 pts)*
<!-- Owner: Person 3. -->
- **Workflow:** `.github/workflows/security-ci.yml`
- **Failing run on the baseline:** link + `evidence/ci/` screenshot
- **Passing run after fixes:** link + `evidence/ci/` screenshot
- **Gate configuration (what fails the build):**

---

## 8. Conclusion & Reflection  *(5 pts — clarity)*
<!-- Owner: everyone. Residual risks, what we'd harden next, lessons learned. -->

---

## Appendix
<!-- Tools, references (OWASP/CWE links), task split written in the past tense. -->

---

## Grading rubric (100)

| Criterion | Pts |
|---|---|
| Threat model quality & completeness (§3) | 20 |
| Vulnerability findings — correctness, CWE/OWASP mapping, depth (§4) | 25 |
| Remediation quality — correct, minimal, well-explained (§5) | 25 |
| Supply-chain hardening — SBOM + signing + provenance (§6) | 15 |
| CI pipeline — works, fails build appropriately (§7) | 10 |
| Presentation & report clarity (§1, §8) | 5 |

*All work stays within the course ethics policy: local sandbox only.*
