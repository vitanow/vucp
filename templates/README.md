# VUCP Templates

Ready-to-use workspace starters. Copy the folder that matches your project type.

## Available Templates

### standard/
Generic starting point. Works for any domain.
Three stages: research → drafting → review.
No domain-specific knowledge files — you fill them in.

### web-dev/
For software architects and web developers working with AI.
Six stages: context-load → plan → implement → test → review → deploy-prep.
Includes pre-filled `_knowledge/` with architecture, patterns, and error-handling guides.
Pre-loaded `_delta/ERRORS.md` with six common AI coding mistakes.
Tech stack-aware `WORKSPACE.md` covering Next.js, TypeScript, Prisma, auth, and infra.

## How to Use

```bash
# Copy your chosen template to a new project folder
cp -r templates/web-dev/ ~/my-project/

# Validate the structure
python cli/vucp_cli_mvp.py lint ~/my-project

# Fill in placeholders
# Start with WORKSPACE.md → then CURRENT.md → then _knowledge/ files
```

## Adding Your User Identity

Place `USER_CORE.md` and `_user_contexts/` in a root folder accessible
across all your projects — not inside a single project workspace.
Each project reads them via the `user_context` field in `WORKSPACE.md`.
