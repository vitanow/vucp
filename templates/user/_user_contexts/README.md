# User Context Files

Each file in this folder describes how the workspace owner works
within a specific domain. These files complement `USER_CORE.md`:

- `USER_CORE.md` — who you are, always loaded
- `_user_contexts/<domain>.md` — how you work in that domain, loaded per project

## How to Link a Context to a Project

In the project's `WORKSPACE.md` frontmatter, add:

```yaml
user_context: "software"
```

The agent loads `_user_contexts/software.md` alongside `USER_CORE.md`
at the start of every session for that project.

## Available Contexts

| File | Domain |
|---|---|
| `software.md` | Software development and architecture |
| `physics.md` | Theoretical physics and mathematics |
| `business.md` | Products, brands, market strategy |
| `creative.md` | Music, writing, visual art |
| `personal.md` | Health, learning, life design |

## Adding a New Context

Copy any existing file, change the `domain:` field and content.
There is no required schema beyond the frontmatter fields shown.
