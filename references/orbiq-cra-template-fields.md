---
title: "CRA Vulnerability Advisory Template (Free DOCX & PDF)"
description: "Free CRA vulnerability advisory template with CVE/EUVD fields, CVSS v4.0 scoring, subscriber notification email, and a filled sample advisory. Ungated."
canonical: https://www.orbiqhq.com/templates/cra-vulnerability-advisory-template
html: https://www.orbiqhq.com/templates/cra-vulnerability-advisory-template
publisher: Orbiq GmbH
language: en
---
# CRA Vulnerability Advisory Template (Free DOCX & PDF)

Free CRA vulnerability advisory template with CVE/EUVD fields, CVSS v4.0 scoring, subscriber notification email, and a filled sample advisory. Ungated.


A **CRA vulnerability advisory template** gives your security team a repeatable structure for the public disclosures the Cyber Resilience Act requires once you fix a vulnerability. From **11 September 2026**, manufacturers of products with digital elements face binding reporting duties under [Regulation (EU) 2024/2847](https://eur-lex.europa.eu/eli/reg/2024/2847/oj) — and from full application in December 2027, publishing information about fixed vulnerabilities stops being good practice and becomes a market-access condition. This free security advisory template ships as DOCX, PDF, and an agent-readable Markdown file, with every field a compliant advisory needs plus a fully filled sample.

**A CRA-compliant vulnerability advisory must describe the fixed vulnerability, identify the affected product and versions, and tell users what action to take (Annex I Part II, points 4 and 8 of Regulation (EU) 2024/2847). A complete advisory adds a CVE or EUVD identifier, a CVSS v4.0 score and vector, fixed versions, mitigations or workarounds, exploitation status, a disclosure timeline, an update log, and a security contact. If the vulnerability is actively exploited, a separate regulatory clock runs in parallel: early warning to ENISA and your coordinating CSIRT within 24 hours, notification within 72 hours, and a final report within 14 days after a corrective measure is available (Article 14).**

## Key Takeaways

- The CRA's vulnerability-handling requirements sit in **Annex I Part II**; Article 13 makes compliance with them a core manufacturer obligation, and Article 14 adds regulatory reporting for actively exploited vulnerabilities.
- **Two different clocks:** the public advisory is due once a security update is available; Article 14 reporting (24h / 72h / 14 days via ENISA's single reporting platform) triggers only for actively exploited vulnerabilities.
- Advisories should carry both a **CVE ID** and an **EUVD ID** — ENISA's [European Union Vulnerability Database](https://euvd.enisa.europa.eu) is now the EU-native reference for both customers and CSIRTs.
- Article 14(8) requires you to inform impacted users, "where appropriate in a structured, machine-readable format" — this template's fields map onto **CSAF 2.0**, the OASIS machine-readable advisory standard.
- Fines for breaching Articles 13/14 or Annex I reach **EUR 15 million or 2.5% of worldwide annual turnover**, whichever is higher.

## What's Inside the Template

The template mirrors the field set used by mature product-security teams and covers everything Annex I Part II expects, in the order your readers need it:

| Field | What it captures | Why it matters |
|---|---|---|
| Advisory ID | Your internal identifier (e.g. `ACME-SA-2026-001`) | Stable reference across updates, emails, and CSAF documents |
| Title | One-line summary naming product and flaw class | First thing customers and aggregators index |
| CVE / EUVD ID | `CVE-YYYY-NNNNN` and `EUVD-YYYY-NNNNN` | Cross-references NVD and ENISA's EUVD |
| CVSS v4.0 score + vector | Numeric score, severity band, full vector string | Objective severity; drives customer patch SLAs |
| Affected products & versions | Product names, version ranges, deployment models | Annex I Part II requires users to be able to identify affected products |
| Fixed versions | First patched release per affected line | The action target of the whole advisory |
| Mitigations & workarounds | Interim measures where patching is delayed | Required "potential action to be taken" (Annex I Part II, point 8) |
| Impact | What an attacker can achieve, preconditions | Lets customers do their own risk assessment |
| Exploitation status | None known / PoC published / exploited in the wild | Determines whether Article 14 reporting triggered |
| Timeline | Report received → triage → fix → disclosure dates | Evidence of handling "without delay"; builds researcher trust |
| Update log | Dated revision history of the advisory | Shows the advisory is maintained, not fire-and-forget |
| Contact & PGP key | Security contact address and encryption key | Annex I Part II requires a contact address for vulnerability reports |

The Markdown variant additionally includes field definitions, a severity scale, an exploitation-status enum, advisory lifecycle states, a subscriber-notification email variant, and a fully filled fictional sample — so both your team and your AI tooling can draft a complete advisory from one file.

## How to Use the Template

1. **Triage the report.** Log the intake date, confirm the vulnerability, and assign your internal advisory ID. Request a CVE ID (via your CNA or MITRE) and note the EUVD ID once assigned.
2. **Score it.** Calculate the CVSS v4.0 base score and record the full vector string, then set the exploitation-status field honestly — it drives everything downstream.
3. **Check the regulatory trigger.** If the vulnerability is **actively exploited**, Article 14 duties start now: early warning within 24 hours via the single reporting platform, notification within 72 hours, final report within 14 days after a corrective measure is available. The public advisory is a separate deliverable on a separate clock.
4. **Fix, then draft.** Prepare the advisory while the fix is in progress, but publish only once the security update is available — that is the disclosure point Annex I Part II anchors to. Coordinate the embargo with the reporter under your coordinated vulnerability disclosure (CVD) policy.
5. **Notify subscribers, then publish.** Send the subscriber-notification email (included in the template) to security contacts and Trust Center subscribers at or just before publication, then post the advisory publicly. Article 14(8) separately requires informing impacted users about actively exploited vulnerabilities and mitigation measures — the CSIRT can do it for you, publicly, if you fail to.
6. **Maintain the update log.** Every material change — new affected versions, exploitation observed, revised mitigations — gets a dated entry. Close the advisory only when all supported lines are fixed.

### Reporting duty vs. public advisory — the distinction that trips teams up

Most vulnerabilities you fix will never touch ENISA's platform. Article 14 covers **actively exploited vulnerabilities** (and severe incidents); Annex I Part II covers **every fixed vulnerability**. Build your workflow so the advisory template is the default path, with the Article 14 escalation bolted on when exploitation evidence appears — not the other way round.

## Legal Basis

- **[Regulation (EU) 2024/2847](https://eur-lex.europa.eu/eli/reg/2024/2847/oj) (Cyber Resilience Act), Article 13** — manufacturers must handle vulnerabilities "in accordance with the vulnerability handling requirements set out in Part II of Annex I" throughout the support period, and must operate a coordinated vulnerability disclosure policy.
- **Annex I Part II** — the vulnerability-handling requirements: identify and document vulnerabilities (including an SBOM covering at least top-level dependencies, point 1); once a security update is available, share and publicly disclose information about fixed vulnerabilities, including a description and information allowing users to identify the affected product (point 4); enforce a CVD policy (point 5); provide a contact address for vulnerability reports; and disseminate free security updates without delay, accompanied by advisory messages with relevant information and potential action to be taken (point 8).
- **Article 14** — reporting of actively exploited vulnerabilities to the CSIRT designated as coordinator and ENISA via the **single reporting platform** established under Article 16: early warning within 24 hours, notification within 72 hours, final report no later than 14 days after a corrective measure is available. Article 14(8) requires informing impacted users, where appropriate in a structured, machine-readable format. These obligations apply from **11 September 2026**; the main CRA obligations apply from **11 December 2027**.
- **Machine-readable advisories** — the CRA names no format, but **CSAF 2.0** (Common Security Advisory Framework, an [OASIS standard](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html)) is the established standard for structured advisories, used by CISA and major vendors. This template's fields correspond to CSAF document properties, keeping a later CSAF migration mechanical.
- **Penalties** — non-compliance with Annex I essential requirements or Articles 13/14 carries fines up to EUR 15 million or 2.5% of total worldwide annual turnover (Article 64).

For the full manufacturer-obligation picture, see our guides to the [Cyber Resilience Act](/eu-regulations/cyber-resilience-act) and [CRA Articles 13 and 14](/eu-regulations/cyber-resilience-act-article-13-14) — and to check where your product stands across classification, conformity route and the full Annex I requirement set, use the companion [CRA Conformity Self-Assessment workbook](/templates/cra-conformity-self-assessment).

## United Kingdom and Norway/EEA

**UK:** The Product Security and Telecommunications Infrastructure (PSTI) Act 2022 regime, in force since **29 April 2024**, requires manufacturers of consumer connectable products sold in the UK to publish a vulnerability disclosure policy with a reporting contact — this template's contact, timeline, and update-log fields do double duty there, though PSTI also demands the policy document and a declared security-update period. **Norway/EEA:** the CRA is marked as EEA-relevant and is expected to be incorporated into the EEA Agreement; Norwegian, Icelandic, and Liechtenstein manufacturers selling into the EU single market are in scope for practical purposes regardless, since the CRA attaches to products placed on the EU market.

## Publish Advisories Where Your Customers Already Look

An advisory nobody sees fails its purpose. [Orbiq Trust Updates](/platform/trust-updates) publishes your security advisories and incident notices directly to your Trust Center, notifies subscribed customers automatically, and keeps the dated update log the CRA expects — turning a compliance duty into a visible trust signal. Related: [what a Trust Center is](/trust-center/what-is-a-trust-center) and how the [NIS2 incident-reporting duties](/eu-regulations/incident-reporting-supply-chain-nis2-articles-21-23) interact with customer notification.

---

## Sources & References

1. [Regulation (EU) 2024/2847 (Cyber Resilience Act) — full text](https://eur-lex.europa.eu/eli/reg/2024/2847/oj) — Official Journal of the European Union.
2. [European Commission — CRA reporting obligations](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting) — the single reporting platform and Article 14 deadlines.
3. [European Commission — Cyber Resilience Act policy page](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act) — entry into force and application dates.
4. [ENISA — European Union Vulnerability Database (EUVD)](https://euvd.enisa.europa.eu) — EU vulnerability records and EUVD identifiers.
5. [Directive (EU) 2022/2555 (NIS2), Article 12](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) — legal basis for the European vulnerability database.
6. [OASIS — Common Security Advisory Framework (CSAF) v2.0](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html) — machine-readable security advisory standard.
7. [FIRST — CVSS v4.0 specification](https://www.first.org/cvss/v4.0/) — scoring and severity bands.
8. [UK Product Security and Telecommunications Infrastructure Act 2022](https://www.legislation.gov.uk/ukpga/2022/46/contents) — UK product security regime.
9. [ENISA — Cyber Resilience Act Requirements Standards Mapping](https://www.enisa.europa.eu/publications/cyber-resilience-act-requirements-standards-mapping) — mapping CRA requirements to existing standards.