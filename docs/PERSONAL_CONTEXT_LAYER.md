# Personal Context Layer

Status: optional v0.5 extension.

The Personal Context Layer adapts the agent to the human without polluting project memory.

## Structure

Recommended private location:

```text
~/.vucp-user/
  USER_CORE.md
  _user_contexts/
    software.md
    physics.md
    business.md
    creative.md
    personal.md
```

## Workspace Reference

In `WORKSPACE.md`:

```yaml
user_profile: "~/.vucp-user/USER_CORE.md"
user_context: "software"
```

## Memory Boundaries

```text
USER_CORE.md          → who the user is and how they generally work
_user_contexts/       → domain-specific working style
WORKSPACE.md          → project identity and boundaries
CURRENT.md            → current operational truth
_delta/ERRORS.md      → project-specific mistakes and resolutions
_delta/LEARNINGS.md   → project-specific repeated patterns
_knowledge/           → stable project/domain knowledge
```

## Safety

Do not commit filled personal context files to public repositories.

Use `templates/user/` only as a template source.

## Cross-Project Pattern Layer

The Personal Context Layer may include:

```text
~/.vucp-user/_cross_project_patterns/
```

This folder stores distilled reusable patterns, not project dumps.

Cross-project patterns help agents reuse lessons across domains while preserving project isolation.

They should be loaded selectively and only when relevant.
