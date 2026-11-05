# Report-Structure Comparison Matrix

This matrix shows where each source places emphasis and how I combine them into my baseline.

| Element | NCSC v2 | Cobalt.io | CERT/CC | My baseline |
|---------|---------|-----------|---------|-------------|
| Executive summary | No | No | No | Yes (from PurpleSec style) |
| Title | Yes | Yes | Yes | Yes |
| Asset | Yes (M) | Implied | Yes | Yes (M) |
| CWE / Weakness | Yes | Yes | Yes | Yes |
| Severity / CVSS | Yes | Criticality | Yes | Yes |
| Description | Yes (M) | Yes | Yes | Yes (M) |
| Affected versions | No | Yes | Yes | Yes |
| Steps to reproduce | Yes (M) | Yes (PoC) | Yes | Yes (M) |
| Impact | Yes | C/I/A + business | Yes | Yes |
| Evidence / attachments | Implied | Yes | Implied | Yes |
| Tools used | No | Yes | No | Yes |
| Suggested fix | Yes | Yes | Yes | Yes |
| References | No | Yes | Yes | Yes |
| Reporter / contact | Yes (optional) | No | Yes | Yes |
| Disclosure timeline | Lifecycle | No | Yes | Yes |

## My composite baseline order

1. Executive Summary
2. Asset (mandatory)
3. Title
4. Weakness / CWE
5. Severity / CVSS
6. Description of the Vulnerability (mandatory)
7. Affected Product & Versions
8. Fixed Versions / Suggested Fix
9. Steps to Reproduce (mandatory)
10. Impact / Criticality Assessment
11. Evidence & Attachments
12. Tools Used
13. Advisory References
14. Reporter / Contact Details
15. Disclosure Timeline

This order front-loads what triagers need to route the report, then gives the evidence and mechanics, then closes with disclosure hygiene.
