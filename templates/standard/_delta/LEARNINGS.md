# Accumulated Workspace Learnings

Reusable patterns and insights discovered across runs.
Entries gain confidence as they are validated across multiple sessions.

## Scoring Guide

| Field | Meaning |
|---|---|
| `confidence` | 0.0–1.0. Above 0.8 = treat as stable rule. |
| `validation_count` | Independent runs that confirmed this pattern. |
| `status` | `candidate` → `confirmed` → `deprecated` |

## Dream Pass

Once per week or after 5+ runs:

1. Promote `candidate` entries with `validation_count >= 3` to `confirmed`
2. Mark `confirmed` entries as `deprecated` if recent runs contradict them
3. Merge overlapping entries into a single cleaner rule
4. Delete noise: one-off observations that have not recurred
5. If a pattern applies across ALL projects in a domain → propose move
   to `~/.vucp-user/_user_contexts/<domain>.md`

---

## Learning Template

```markdown
## Learning: <Short descriptive name>

**Discovered:** YYYY-MM-DD
**Last validated:** YYYY-MM-DD
**Validation count:** 1
**Confidence:** 0.40
**Status:** candidate

**Pattern:**
What was observed — the repeatable behavior or result.

**Rule:**
The actionable principle. Written as a direct instruction Claude can apply.

**Applies to:**
Which stages, domains, or project types.

**Counter-examples:**
Situations where this rule does NOT apply.

**Cross-references:**
- `_delta/ERRORS.md#<error-name>` — related failure this pattern prevents
- `_knowledge/<path>` — knowledge file that explains the underlying reason
- `_user_contexts/<domain>.md` — if this graduates to cross-project level
```

---

<!-- Add real learnings below this line. -->
