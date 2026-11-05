# CERT/CC — Basic Vulnerability Advisory Document

Source: [CERT/CC Basic Vulnerability Advisory Document](https://certcc.github.io/CERT-Guide-to-CVD/reference/simple_advisory/)

## Advisory structure

### Overview

- Brief vulnerability description (1–2 sentences).

### Vulnerability ID

- CVE ID.
- Any other IDs: vendor tracking ID, bug tracker ID, CERT ID, etc.

### Description

- Software/product(s) containing the vulnerability.
- Version number of vulnerable software/product.
- Product vendor.
- Type of vulnerability (CWE).
- Vulnerability description.
- How an attacker may exploit it (proof of concept).

### Impact

- What the attacker gains that they did not have before.

### CVSS Score

- Full CVSS vector, not only the score.
- Include temporal and environmental metrics if possible.

### Resolution

- Version containing the fix.
- URL or contact to obtain the fix.
- Workarounds/mitigations if no fix exists.

### Reporter

- Who reported/discovered the vulnerability.

### Author and/or Contact Info

- Name, organisation, email, PGP public key.

### Disclosure Timeline

- Date of first vendor contact attempt.
- Date of vendor response.
- Date of patch release.
- Disclosure date.

### References

- Vendor advisory, other disclosures, mitigation advice.

## Why I use it

CERT/CC's structure is vendor-neutral and close to the OASIS CSAF format, making it easy to migrate to machine-readable advisories later.
