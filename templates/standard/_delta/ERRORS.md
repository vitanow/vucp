# Documented Workspace Failures & Resolutions

Catalog errors here to prevent recurrence across future runs.
Each entry includes a confidence score that increases with repeated occurrence.

## Scoring Guide

| Field | Meaning |
|---|---|
| `confidence` | 0.0–1.0. Increases with each recurrence. Above 0.8 = treat as a rule. |
| `occurrence_count` | How many times this error has been observed. |
| `status` | `open` = not yet resolved. `resolved` = fix confirmed in production. |

---

## Error Template

```markdown
## Error: <Short descriptive name>

**Discovered:** YYYY-MM-DD
**Last seen:** YYYY-MM-DD
**Occurrence count:** 1
**Confidence:** 0.40
**Status:** open

**Symptom:**
What went wrong — describe from the observable output, not the assumed cause.

**Root cause:**
What actually caused it, once understood.

**Resolution:**
What prevents recurrence. Be specific.

**Claude instruction:**
The exact behavioral rule Claude must follow to avoid this error.
Write it as a direct instruction: "Before doing X, always check Y."
```

---

<!-- Add real errors below this line as they are discovered. -->
