# Architectural & Strategic Decisions

<!-- Record major technical decisions here as they are made. -->
<!-- Format: Date — Decision — Reason — Impact — Status -->

## 2026-06-27 — Adopted VUCP v0.4.1

**Decision:** Use VUCP filesystem protocol for all Claude AI sessions.

**Reason:** Eliminate context re-loading overhead at the start of every Claude session.
All architectural knowledge, patterns, and session state live as files — readable by
both humans and Claude without re-explanation.

**Impact:** Every new Claude session starts with CURRENT.md + WORKSPACE.md instead of
a paragraph of "here's the project" context. ERRORS.md prevents repeated mistakes.

**Status:** active
