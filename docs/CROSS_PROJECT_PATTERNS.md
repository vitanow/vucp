# Cross-Project Pattern Layer

Status: optional v0.5 extension.

The Cross-Project Pattern Layer lets VUCP reuse distilled lessons across projects without loading entire old projects into context.

## Principle

Do not share whole projects by default.

Share confirmed, reusable patterns.

```text
Project experience
→ candidate pattern
→ Dream Pass
→ confirmed cross-project pattern
→ selective reuse
```

## Why

Architecture, safeguards, CLI conventions, onboarding patterns, and failure modes discovered in one project are often useful in another.

But loading all prior project context creates:

- context pollution;
- false analogies;
- privacy risk;
- token waste;
- overconfident agents.

The solution is a curated pattern library with metadata, confidence scoring, scope, and anti-scope.

## Recommended Private Location

```text
~/.vucp-user/
  USER_CORE.md
  _user_contexts/
  _cross_project_patterns/
    index.md
    architecture/
    errors/
    product/
    operations/
    creative/
```

## Workspace Reference

In `WORKSPACE.md`:

```yaml
cross_project_patterns: "~/.vucp-user/_cross_project_patterns/index.md"
cross_project_pattern_policy: "selective"
max_cross_project_patterns: 5
```

## Loading Rule

Agents must not load all patterns.

For Full Startup:

1. Read `USER_CORE.md`, if available.
2. Read matching `_user_contexts/<domain>.md`, if available.
3. Read `WORKSPACE.md`.
4. Read `CURRENT.md`.
5. Read `_delta/ERRORS.md`.
6. Read current stage `CONTEXT.md`.
7. Read `SAFEGUARDS.md` if risk is medium/high/critical.
8. Read `_cross_project_patterns/index.md`, if available.
9. Select maximum 3–5 confirmed patterns with matching tags, domain, or risk profile.
10. If no confident match exists, do not load cross-project patterns.

## Pattern Status

```text
candidate   → observed, not yet trusted
confirmed   → repeated and reusable
deprecated  → no longer generally valid
rejected    → false or too context-specific
```

## Confidence Rule

```text
confidence < 0.5    → weak signal
confidence 0.5–0.79 → candidate
confidence >= 0.8   → confirmed only if evidence_count >= 2
```

## Safety Rule

Cross-project patterns are advisory.

They must not override:

1. `SAFEGUARDS.md`;
2. current stage `CONTEXT.md`;
3. current `WORKSPACE.md`;
4. explicit human instruction;
5. legal/security/privacy constraints.

## Do Not

- Do not load entire previous projects by default.
- Do not copy project-specific secrets or client data.
- Do not promote a pattern without evidence.
- Do not treat old preferences as permanent laws.
- Do not apply a pattern if `does_not_apply_to` matches the current task.

## CLI tag matching

`vucp patterns <path> --tags a,b,c`:

- Multiple tags use OR: a pattern is selected if it matches any tag.
- Tags are matched against the pattern's `tags`, `applies_to`, and `source_projects`.
- Matching is case-insensitive and whitespace-trimmed; empty entries are ignored.
- `does_not_apply_to` overrides positive matches: if any given tag appears in a pattern's `does_not_apply_to`, the pattern is excluded. Example: a pattern with `tags: [deployment]` and `does_not_apply_to: [production]` is excluded for `--tags deployment,production`.
- Frontmatter block lists (`- item`) are read only for list fields: `tags`, `applies_to`, `does_not_apply_to`, `source_projects`, `semantic_aliases`, `cross_references`.
- Results are ranked by number of matched tags, then by confirmed status and confidence.
- If nothing matches, 0 patterns are returned (exit code 0).
- `--tags ""` means no tag filter; omitting `--tags` uses `user_context` from `WORKSPACE.md`.
