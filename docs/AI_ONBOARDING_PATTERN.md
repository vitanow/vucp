# AI Onboarding Pattern

**Status:** recommended product pattern — v0.5

---

## What It Is

A normal README explains a tool to a human.

An AI onboarding guide explains the setup process to an AI assistant,
so the assistant can guide the human step by step — one step at a time,
with verification at each step, and with the human doing as little as possible.

## The Pattern

Create a file named:

```
<PROJECT>_SETUP_GUIDE.ai.md
```

Give this file to your AI (paste it, upload it, or reference it).
The AI reads it and becomes the guide. The human follows.

The file tells the assistant:

- What the tool is, in one sentence
- What questions to ask first
- How to choose the simplest setup path based on answers
- How to give one step at a time and verify before continuing
- How to troubleshoot without guessing
- When to make decisions autonomously vs. ask the human
- How to end: what "success" looks like, and what the human needs to remember

## VUCP Implementation

VUCP includes:

```
VUCP_SETUP_GUIDE.ai.md     ← give this to any AI to onboard a new user
docs/AI_SETUP_GUIDE.md     ← same file, in docs/ for discoverability
```

## Why This Works

The AI has infinite patience and no ego.
It will repeat the same step five times without frustration.
It will explain what a terminal is without condescension.
It will make every decision if the human says "just do it."

This removes the human from the critical path of setup —
they only appear when their specific knowledge is genuinely needed
(project name, what they're building, which AI tool they use).

## Design Rules for AI Onboarding Files

1. **For AI, not humans.** Say so at the top. Humans who read it should
   understand it's instructions for the agent, not a user guide.

2. **One step at a time.** Never give a list of 10 commands. One. Then verify.

3. **Ask before assuming.** OS, skill level, tool preference — ask first.
   Two questions at a time, not all at once.

4. **Autonomous mode.** If the human says "just set it up" — the AI makes
   all decisions and explains what it chose at the end. Does not ask
   for permission mid-process.

5. **Celebrate the win.** End with a clear statement of what was achieved
   and the two or three things the human needs to remember going forward.

## Extending the Pattern

Any VUCP product or template can ship its own `*_SETUP_GUIDE.ai.md`.
This is the recommended distribution format for non-technical users:

```
SaaS MVP Launch Kit → SAAS_MVP_SETUP_GUIDE.ai.md
Web Dev Template   → WEB_DEV_SETUP_GUIDE.ai.md
Research Workspace → RESEARCH_SETUP_GUIDE.ai.md
```

The marketplace product ships the guide. The buyer gives it to their AI.
No documentation to read. No setup videos. The AI handles it.
