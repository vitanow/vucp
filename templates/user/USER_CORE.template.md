---
protocol: VUCP
type: user-core
version: "1.0"
status: template
private: true
last_updated: "2026-06-27"
---

> **PRIVACY NOTE:** This is a template. Copy it to a private location
> outside any public repository before filling it in.
>
> Recommended location: `~/.vucp-user/USER_CORE.md`
>
> Never commit your filled-in USER_CORE.md to a public repository.
> Add `USER_CORE.private.md` and `_user_contexts/private/` to `.vucpignore`.


# User Core Identity

This file is loaded at the start of every session, regardless of project or domain.
It describes who the person is, how they think, and how they want to work with AI.
It is written in first person by the workspace owner and should be updated
as preferences evolve — not deleted and rewritten.

---

## Identity

**Name:** <YOUR_NAME>
**Primary Language:** <en | bg | fr | ...>
**Secondary Language:** <optional>
**Timezone:** <UTC+2 | America/New_York | ...>

---

## How I Think

<!--
Describe your cognitive style. Examples:
- I work in parallel across multiple unrelated domains — context switching is normal for me.
- I prefer synthesis over depth in isolation: I connect ideas across fields.
- I think in systems and structures before I think in details.
- I prefer to see the shape of an argument before the supporting evidence.
-->

---

## How I Work

<!--
Describe your working rhythm. Examples:
- I work in energy phases: high-focus blocks → active output → rest → integration.
- I prefer async, written communication over verbal or real-time.
- I iterate fast and discard freely — do not preserve ideas I have moved past.
- I generate many ideas and use AI to stress-test, not to validate.
-->

---

## How I Want Feedback

<!--
Be specific. Examples:
- Be direct. Do not soften criticism to protect my feelings.
- Flag your assumptions explicitly before making claims.
- If I am wrong, say so first — explain after.
- Do not ask clarifying questions if you can make a reasonable assumption and state it.
- Challenge me when you disagree. I prefer honest pushback over agreement.
-->

---

## What I Do Not Want

<!--
Hard stops for AI behavior in any context. Examples:
- Do not add unsolicited motivational framing.
- Do not repeat what I just said back to me as a summary before answering.
- Do not use bullet points when prose is more natural.
- Do not hedge every statement with "it depends" without explaining what it depends on.
-->

---

## Active Domains

<!--
List your current active domains so any agent knows your context is multi-domain.
Format: domain_id — one-line description
-->

| ID | Domain | Status |
|---|---|---|
| `software` | Software architecture, protocols, developer tools | active |
| `physics` | Theoretical physics, cosmology, mathematical models | active |
| `business` | Products, brands, market strategy | active |
| `creative` | Music production, writing, art direction | active |
| `personal` | Life design, health, learning | active |

Each domain has a context file in `_user_contexts/`.
Load the relevant context file for the current project alongside this file.

---

## Cross-Domain Principle

These domains are not silos. Patterns discovered in one domain frequently apply to others.
When you notice a cross-domain connection relevant to the current work, flag it.

---

## Languages

- **Primary output:** <Language for thinking and strategy>
- **Technical output:** <Language for code, specs, and publishing>
- **Switch when:** <describe when you want which language>
