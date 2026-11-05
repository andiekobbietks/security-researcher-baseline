# Report Templates

## `vulnerability-report-template.docx`

My working Word template for responsible-disclosure / bug-bounty reports.

- Built from the composite baseline in [`standards/`](../standards/).
- Contains **Word comments** with AI drafting notes attached to each section.
- The comments appear in Word's Review pane so I know what to verify and rewrite.
- I delete all comments and rewrite the report in my own words before submitting.

## `generate_template.py`

Python script that regenerates the DOCX. Requires `python-docx` and `lxml`.

```bash
python generate_template.py
```

Output path is hardcoded to the current directory; edit the script if you want a different location.

## How I use this template

1. Copy the template for a new report.
2. Replace placeholder lines (`________________________`) with verified facts.
3. Follow the Word comments to verify each section.
4. Delete all comments.
5. Re-read the report as the triager would.
6. Submit.
