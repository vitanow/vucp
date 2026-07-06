# Cross-Project Pattern Index

This index points agents to reusable patterns without loading every prior project.

## Loading Policy

- Load this index during Full Startup only if `cross_project_patterns` is configured in `WORKSPACE.md`.
- Select maximum 3–5 relevant confirmed patterns.
- Do not load full old project folders.
- Do not load candidate patterns unless explicitly requested.

## Pattern Index

| Path | Type | Status | Confidence | Tags | Applies To | Summary |
|---|---|---:|---:|---|---|---|
| `architecture/cli-help-contract.md` | architecture | confirmed | 0.95 | cli, tooling, safety | cli, automation, scripts | Every CLI should support `--help`, `-h`, `help`, and where useful `/?`. |
| `architecture/rollback-first-deployment.md` | architecture | confirmed | 0.88 | rollback, deployment, safety | infrastructure, cli, production | Risky work requires verification and rollback before execution. |
| `errors/context-inflation.md` | error | confirmed | 0.86 | context, agents, tokens | ai-workflows, documentation | Loading too much context reduces quality and increases cost. |
| `product/demo-before-pitch.md` | product | confirmed | 0.84 | product, validation, pitching | startups, templates, SaaS | Demo and validation should precede investor/product expansion. |
