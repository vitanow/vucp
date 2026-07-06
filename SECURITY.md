# Security Policy

## Supported versions

VUCP is currently in alpha. Security fixes target the latest published alpha unless a specific maintenance branch is announced.

## Reporting a vulnerability

Please do not open a public issue for sensitive reports.

Report security concerns privately to the maintainer:

```text
GitHub: @vitanow
```

Include:

- affected VUCP version or commit;
- impacted file, command, or template;
- steps to reproduce;
- potential impact;
- suggested mitigation, if known.

## Scope

Security-sensitive areas include:

- accidental inclusion of private user context;
- unsafe handling of `.env`, keys, tokens, credentials, or private project data;
- CLI behavior that may overwrite or expose files unexpectedly;
- generated adapter files that encourage unsafe agent behavior.

VUCP templates should remain conservative around destructive actions, production changes, credentials, payment systems, live databases, and trusted memory.
