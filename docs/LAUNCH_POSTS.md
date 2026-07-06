# VUCP Launch Posts

## Main launch post

I’m **Zahari Vitanov**, and I built **VUCP — Vitanow Unified Context Protocol**.

It is a portable AI workspace format for people building with Codex, Claude Code, Cursor, Windsurf, Gemini CLI, and other AI agents.

The problem:

AI agents are powerful, but project memory is fragile.

Context gets lost in chats.  
Agents repeat the same mistakes.  
Rules files grow messy.  
Decisions disappear.  
Review and rollback are often invisible.

VUCP turns a normal project folder into an inspectable AI workspace:

```text
CURRENT.md        → what is happening now
WORKSPACE.md      → what this project is
AGENTS.md         → how agents should behave
_delta/           → errors, learnings, decisions
_runs/            → traceable execution records
stages/           → structured workflow
```

It is not another agent.  
It is not another memory database.  
It is not a replacement for MCP.

VUCP is the project-side layer that makes human-AI work visible, repeatable, portable, and safer.

Created by **Zahari Georgiev Vitanov / Vitanow OPS**.

GitHub: https://github.com/vitanow/vucp

## Short post

I built VUCP — a portable AI workspace format for inspectable human-AI work.

It helps Codex, Claude Code, Cursor, Windsurf, and other agents work from visible project state instead of fragile chat memory.

Created by **Zahari Vitanov / Vitanow OPS**.

GitHub: https://github.com/vitanow/vucp

## Technical post

VUCP is not trying to replace MCP, AGENTS.md, Claude memory, Cursor rules, or agent frameworks.

It sits one layer below the agent experience:

```text
project folder → structured workspace → agent-specific exports
```

The goal is simple:

Make AI-assisted project work inspectable, repeatable, portable, and safer.

Created by **Zahari Georgiev Vitanov / Vitanow OPS**.

## Bulgarian post

Аз съм **Захари Витанов** и създадох **VUCP — Vitanow Unified Context Protocol**.

Това е portable AI workspace format — структура за проектна папка, която прави работата с AI агенти по-видима, проследима, повторяема и безопасна.

VUCP е за хора, които работят с Codex, Claude Code, Cursor, Windsurf, Gemini CLI и други AI инструменти, но не искат всеки път да обясняват проекта отначало.

Проблемът:

- контекстът се губи;
- агентите повтарят грешки;
- правилата стават хаотични;
- решенията остават скрити в чатове;
- няма ясна следа кой какво е направил и защо.

VUCP превръща нормална проектна папка в AI workspace с:

```text
CURRENT.md
WORKSPACE.md
AGENTS.md
_delta/
_runs/
stages/
```

Не е нов агент.  
Не е база данни за памет.  
Не заменя MCP.

VUCP е проектният слой, който прави AI работата видима и проверима.

Създадено от **Захари Георгиев Витанов / Vitanow OPS**.

GitHub: https://github.com/vitanow/vucp

## Assisted Autopilot launch angle

VUCP now includes Assisted Autopilot: human attention only when it matters.

```text
AUTOPILOT.md
_attention/ATTENTION.md
_delta/AUTOPILOT_LOG.md
```

The recommended default is `SURFACE`: AI performs safe routine checks and then surfaces a short attention list with recommended next steps.

Created by **Zahari Georgiev Vitanov / Vitanow OPS**.
