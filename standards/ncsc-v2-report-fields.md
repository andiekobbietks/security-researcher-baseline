# NCSC Vulnerability Disclosure Toolkit v2 — Report Fields

Source: `NCSC-Vulnerability-disclosure-Toolkit-v2.pdf` in [`references/`](../references/)

## Report field table

| Report Section | Description | Mandatory |
|----------------|-------------|-----------|
| **Title** | Concise summary categorising the vulnerability and the site/application where it can be found. Example: "Reflected XSS on the XYZ website". | No |
| **Asset** | Web address, IP address, product, service name, etc. | Yes |
| **Weakness** | Such as a CWE. | No |
| **Severity** | Such as low, medium, high, critical, and calculated via CVSS. | No |
| **Description of the Vulnerability** | A summary of the vulnerability; supporting files (screenshot or video); any mitigations or recommendations. | Yes |
| **Steps to Reproduce** | Clear and descriptive steps to reproduce the vulnerability; proof-of-concept code if available. | Yes |
| **Impact** | The effects of successfully exploiting the vulnerability. | No |
| **Contact Details** | Name, email address. Optional to enable anonymous reporting. | No |

`(M)` denotes mandatory field.

## Report lifecycle

NCSC describes a typical report state lifecycle:

- **Open: New** — not yet validated/triaged; may need additional info from finder.
- **Open: Triaged** — valid vulnerability; assigned for remediation.
- **Resolved** — fix verified and report closed.

A unique reference number per report is recommended.

## Why I use it

It is the UK official guidance and gives a minimal, complete field set that works for both vendors and independent finders.
