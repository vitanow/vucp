# User Context Templates

These are **templates only**. Do not fill them in here.

## Setup Instructions

1. Copy this folder to a private location outside any public repository:

```bash
mkdir -p ~/.vucp-user/_user_contexts
cp templates/user/USER_CORE.md ~/.vucp-user/USER_CORE.md
cp templates/user/_user_contexts/*.md ~/.vucp-user/_user_contexts/
```

2. Fill in `~/.vucp-user/USER_CORE.md` with your actual identity and preferences.

3. Fill in the relevant domain context files in `~/.vucp-user/_user_contexts/`.

4. In each project's `WORKSPACE.md`, declare:

```yaml
user_context: "software"   # or physics, business, creative, personal
```

5. At the start of each session, load:
   - `~/.vucp-user/USER_CORE.md`
   - `~/.vucp-user/_user_contexts/<domain>.md`
   - Project `CURRENT.md`

## Why Private?

USER_CORE.md contains personal working preferences, communication style,
and domain context. This is private information that should not be committed
to a public repository.

## The Four Layers

```
USER_CORE.md              → who you are and how you work (always loaded)
_user_contexts/<domain>   → how you work in this specific domain (per project)
WORKSPACE.md              → what this project is (per project)
CURRENT.md                → what is happening right now (per session)
```

Each layer answers a different question. Together they eliminate
the need to re-explain context at the start of every AI session.

## Cross-Project Patterns

For reusable lessons across projects, copy:

```text
templates/user/_cross_project_patterns/
```

to:

```text
~/.vucp-user/_cross_project_patterns/
```

Then reference it from a workspace:

```yaml
cross_project_patterns: "~/.vucp-user/_cross_project_patterns/index.md"
cross_project_pattern_policy: "selective"
max_cross_project_patterns: 5
```

Do not point agents at entire old projects by default. Promote only distilled patterns through Dream Pass.
