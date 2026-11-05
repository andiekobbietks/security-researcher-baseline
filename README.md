# Security Researcher Baseline

[![GitHub](https://img.shields.io/badge/GitHub-andiekobbietks%2Fsecurity--researcher--baseline-blue?logo=github)](https://github.com/andiekobbietks/security-researcher-baseline)

This repo documents the baseline I follow when reporting security findings, filing bug bounty reports, and doing coordinated vulnerability disclosure (CVD).

It exists so maintainers, triagers, and program owners can see the standard behind my reports — and so I stay consistent across different platforms. It is pinned to my GitHub profile as my working reference.

## What this repo contains

| Directory | Purpose |
|-----------|---------|
| [`standards/`](./standards/) | Side-by-side summary of the report structures I follow |
| [`references/`](./references/) | Original source files I downloaded for reference |
| [`templates/`](./templates/) | My working Word template and the script that generates it |
| [`BASELINE.md`](./BASELINE.md) | The single-page checklist I use before submitting any report |

## Why this standard?

I picked a composite baseline built from:

1. **NCSC Vulnerability Disclosure Toolkit v2** (UK official) — mandatory report fields and lifecycle.
2. **Cobalt.io** — practical advice for triager-friendly reports and evidence.
3. **CERT/CC Basic Vulnerability Advisory Document** — structured advisory format with CVSS and timeline.
4. **PurpleSec sample report** — example of executive summary, methodology, and risk assessment layout.

## My reports are human-verified

I use AI tooling to draft and scaffold, but every report I submit is:

- Reproduced manually in my own environment.
- Rewritten in my own words.
- Verified against the original advisory and the affected code/dependency.
- Stripped of scaffolding comments before submission.

See [`BASELINE.md`](./BASELINE.md) for the pre-submission checklist.

## License

My own text and templates in this repo are released under [CC0 1.0 Universal](./LICENSE). Third-party reference documents remain the property of their original publishers and are stored here only for personal reference.
