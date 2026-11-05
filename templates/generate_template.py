from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.opc.part import Part
from docx.opc.packuri import PackURI
from lxml import etree
import os
import datetime

output_path = r'C:\Users\Admin\AppData\Local\Temp\opencode\opencode_security_report_improved.docx'
author = 'AI Draft'
# Use UTC now in ISO format
now = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

doc = Document()

# ---------------------------------------------------------------------------
# Word comment machinery
# ---------------------------------------------------------------------------

def ensure_comments_part(doc):
    """Create /word/comments.xml and wire it into the package."""
    pkg = doc.part._package
    # Check if comments part already exists on the main document part
    for rel in doc.part.rels.values():
        if rel.reltype == RT.COMMENTS:
            return rel.target_part
    # Content type and path
    content_type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml'
    partname = PackURI('/word/comments.xml')
    # Build minimal comments.xml root
    comments_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<w:comments xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
        'xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" '
        'xmlns:w15="http://schemas.microsoft.com/office/word/2012/wordml">\n'
        '</w:comments>'
    )
    part = Part(partname, content_type, comments_xml.encode('utf-8'), pkg)
    doc.part.rels.get_or_add(RT.COMMENTS, part)
    return part


def add_comment_to_run(paragraph, run, text, comment_id, author=author, date=now):
    """Attach a Word comment to a single run."""
    comments_part = ensure_comments_part(doc)
    comments_root = etree.fromstring(comments_part._blob)

    # Namespace map for w:
    nsmap = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

    # Build the comment element
    comment_el = etree.SubElement(
        comments_root,
        '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}comment',
        nsmap=nsmap,
        attrib={
            '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}id': str(comment_id),
            '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}author': author,
            '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}date': date,
            '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}initials': ''.join([w[0].upper() for w in author.split() if w]),
        }
    )
    para_el = etree.SubElement(
        comment_el,
        '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p',
        nsmap=nsmap
    )
    run_el = etree.SubElement(
        para_el,
        '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r',
        nsmap=nsmap
    )
    text_el = etree.SubElement(
        run_el,
        '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t',
        nsmap=nsmap
    )
    text_el.text = text

    comments_part._blob = etree.tostring(comments_root, xml_declaration=True, encoding='UTF-8', standalone=True)

    # Insert commentRangeStart before the run and commentRangeEnd + commentReference after
    p = paragraph._element
    r = run._r

    range_start = OxmlElement('w:commentRangeStart')
    range_start.set(qn('w:id'), str(comment_id))

    range_end = OxmlElement('w:commentRangeEnd')
    range_end.set(qn('w:id'), str(comment_id))

    ref_run = OxmlElement('w:r')
    ref = OxmlElement('w:commentReference')
    ref.set(qn('w:id'), str(comment_id))
    ref_run.append(ref)

    p.insert(p.index(r), range_start)
    p.insert(p.index(r) + 1, range_end)
    p.insert(p.index(range_end) + 1, ref_run)


# ---------------------------------------------------------------------------
# Document helpers
# ---------------------------------------------------------------------------

comment_counter = [0]

def add_section(heading, body_text, comment_text):
    """Add a heading + body paragraph and attach a Word comment."""
    h = doc.add_heading(heading, level=2)
    p = doc.add_paragraph(body_text)
    cid = comment_counter[0]
    comment_counter[0] += 1
    # Attach comment to the heading run (first run of the heading)
    if h.runs:
        add_comment_to_run(h, h.runs[0], comment_text, cid)
    return h, p


def add_fill_field(label, comment_text):
    """Add a label line and a blank placeholder line, with comment."""
    p_label = doc.add_paragraph()
    run_label = p_label.add_run(label)
    run_label.bold = True
    p_blank = doc.add_paragraph('________________________________________')
    cid = comment_counter[0]
    comment_counter[0] += 1
    add_comment_to_run(p_label, run_label, comment_text, cid)
    return p_label, p_blank


# ---------------------------------------------------------------------------
# Title / warning
# ---------------------------------------------------------------------------

title = doc.add_heading('Responsible Disclosure Report — anomalyco/opencode', level=0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

warning = doc.add_paragraph()
warning_run = warning.add_run('WARNING: ')
warning_run.bold = True
warning_run.font.color.rgb = RGBColor(255, 0, 0)
warning.add_run(
    'anomalyco/opencode explicitly bans AI-generated security reports (see their SECURITY.md). '
    'This document is a template/scaffold only. You must heavily edit it, add your own verification, '
    'rewrite every section in your own words, and remove all Word comments before submitting.'
)

doc.add_paragraph()

# ---------------------------------------------------------------------------
# Main sections
# ---------------------------------------------------------------------------

add_section(
    '1. Executive Summary',
    'One-paragraph summary: what was found, in which component, severity, and the single recommended action.',
    'Write this last, after you have verified everything else. Keep it to 3-5 sentences. This is what the triager reads first.'
)

add_fill_field(
    '2. Asset (mandatory)',
    'NCSC v2 treats Asset as mandatory. Be specific: repository URL, package path, file, line/dependency tree. Example: anomalyco/opencode, packages/console/app/package.json, wrangler@4.50.0.'
)

add_fill_field(
    '3. Title',
    'NCSC example format: "Reflected XSS on the XYZ website". For a dependency issue try: "OS command injection in wrangler@4.50.0 devDependency (packages/console/app)".'
)

add_fill_field(
    '4. Weakness / CWE',
    'Map the finding to a CWE. For wrangler pages deploy OS command injection, verify whether CWE-78 (OS Command Injection) applies. Check MITRE CWE yourself; do not copy my label.'
)

add_fill_field(
    '5. Severity / CVSS',
    'Provide a severity band (low/medium/high/critical) and, if you can calculate it, a CVSS vector + score. CERT/CC asks for the full vector, not just the number.'
)

add_section(
    '6. Description of the Vulnerability (mandatory)',
    'Describe the vulnerability in your own words. State the vulnerable dependency, the affected subcommand, and why it matters in this project.',
    'Do not copy the advisory text verbatim. Read GHSA-36p8-mvp6-cv38 yourself, then explain it as you would to a newcomer. Attach screenshots or lockfile snippets if useful.'
)

add_fill_field(
    '7. Affected Product & Versions',
    'List exact products/versions. Example: anomalyco/opencode @ dev branch, packages/console/app, wrangler "4.50.0". Verify the version is still present on the latest branch.'
)

add_fill_field(
    '8. Fixed Versions / Suggested Fix',
    'State the first patched version and how to apply it. Example: bump wrangler to ^4.110.0 or later, run bun install, commit the lockfile change. Verify the new version is clean in OSV and that the project still builds.'
)

add_section(
    '9. Steps to Reproduce (mandatory)',
    '''1. Clone the repository: git clone https://github.com/anomalyco/opencode.git
2. Check out the latest dev branch
3. Install dependencies: bun install
4. Inspect packages/console/app/package.json for the wrangler version
5. Confirm the same version in bun.lock under the @opencode/console-app dependency tree
6. Cross-check the version against the advisory (GHSA-36p8-mvp6-cv38)''',
    'Run every step yourself. Replace these bullets with the exact commands you ran and their actual output. If a step fails or the version changed, update it.'
)

add_section(
    '10. Impact / Criticality Assessment',
    'Assess impact against Confidentiality, Integrity, and Availability. State preconditions for exploitation (e.g. attacker must control input to wrangler pages deploy). Rate business impact.',
    'Be honest about residual risk. If the project never invokes "wrangler pages deploy", say so and explain why the risk is lower. Do not overstate exploitability.'
)

add_fill_field(
    '11. Evidence & Attachments',
    'Paste terminal output, lockfile excerpts, OSV API responses, screenshots, or video links here. Cobalt.io recommends attaching proof.'
)

add_fill_field(
    '12. Tools Used',
    'List tools and sources: git, grep, bun install, OSV API (https://api.osv.dev), pypdf/lockfile parser, etc.'
)

add_section(
    '13. Advisory References',
    '''GHSA-36p8-mvp6-cv38 — Wrangler affected by OS command injection in "wrangler pages deploy"
OSV entry: https://osv.dev/vulnerability/GHSA-36p8-mvp6-cv38
Vendor/security policy: https://github.com/anomalyco/opencode/blob/main/SECURITY.md''',
    'Open every URL yourself before including it. Remove any reference you cannot verify. Do not cite Wikipedia or low-credibility sources (per Cobalt.io guidance).'
)

add_fill_field(
    '14. Reporter / Contact Details',
    'Your name, email, and optional PGP key. NCSC v2 notes contact details are optional if you prefer to report anonymously.'
)

add_section(
    '15. Disclosure Timeline',
    '''Date of first report: [INSERT]
Expected vendor acknowledgement: within 6 business days (per anomalyco/opencode SECURITY.md)
Date of vendor response: [INSERT]
Date of patch release: [INSERT]
Public disclosure date: [INSERT or N/A]''',
    'Fill in dates as they happen. This section is evidence of coordinated disclosure. Do not invent dates.'
)

# ---------------------------------------------------------------------------
# Closing
# ---------------------------------------------------------------------------

doc.add_paragraph()
closing = doc.add_paragraph()
closing_run = closing.add_run('Before submitting: ')
closing_run.bold = True
closing.add_run(
    'delete every Word comment, rewrite every paragraph in your own words, verify every URL and version number, '
    'and run the reproduction steps yourself.'
)

# Save
doc.save(output_path)
print(f'Saved improved DOCX with Word comments: {output_path}')
