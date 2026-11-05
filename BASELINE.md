# Pre-Submission Baseline Checklist

I use this checklist before filing any vulnerability report, bug bounty submission, or coordinated disclosure.

## 1. Scope and policy check

- [ ] I have read the project's `SECURITY.md` or disclosure policy.
- [ ] The finding is in scope.
- [ ] I have not accessed data or systems beyond what is necessary to demonstrate the issue.
- [ ] I have not publicly disclosed the issue before the vendor has had a reasonable chance to respond.

## 2. Verification

- [ ] I reproduced the issue myself in a clean environment.
- [ ] I verified the affected version is still present on the latest branch/release.
- [ ] I opened every advisory URL and reference link I include.
- [ ] I removed any reference I could not verify.

## 3. Report structure

My report contains, at minimum:

- [ ] **Executive summary** — one paragraph stating what, where, severity, and fix.
- [ ] **Asset** — exact repository, path, file, line, or endpoint.
- [ ] **Title** — one-line summary naming product and flaw class.
- [ ] **Weakness / CWE** — mapped to a CWE where applicable.
- [ ] **Severity / CVSS** — severity band and, where possible, a CVSS vector.
- [ ] **Description** — in my own words, with supporting evidence.
- [ ] **Affected versions** — exact version numbers.
- [ ] **Steps to reproduce** — numbered, explicit, minimal.
- [ ] **Impact assessment** — C/I/A and business impact, with preconditions.
- [ ] **Suggested fix / mitigation** — concrete, testable.
- [ ] **References** — only sources I have verified.
- [ ] **Contact details** — or explicit anonymous reporting.
- [ ] **Disclosure timeline** — dates of contact, response, fix, disclosure.

## 4. Anti-patterns I avoid

- [ ] No copy-pasted automated-tool output.
- [ ] No Wikipedia or low-credibility references.
- [ ] No invented dates, versions, or impact claims.
- [ ] No AI scaffolding comments left in the submitted document.

## 5. Final human edit

- [ ] I rewrote every paragraph in my own words.
- [ ] I deleted all AI-generated comments and notes.
- [ ] I re-read the report as if I were the triager.
- [ ] The report reflects my own verification and understanding.
