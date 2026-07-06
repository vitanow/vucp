# Current Operational State

## Status

active

## Active Feature

<!-- What are you building right now? -->
<!-- Example: User authentication — JWT login + refresh token rotation -->

## Where I Left Off

<!-- The most important sentence for Claude at the start of a new session. -->
<!-- Example: Middleware written, but refresh endpoint returns 401 on valid token. -->
<!-- Suspected cause: token expiry check uses UTC but DB stores local time. -->

## Files Changed Last Session

<!-- List the files touched. Claude will focus here first. -->
<!--
- src/middleware/auth.ts
- src/app/api/auth/refresh/route.ts
- prisma/schema.prisma (added refreshToken model)
-->

## Open Blockers

<!-- What is stopping progress? -->
<!-- Example: Need to decide: store refresh tokens in DB or Redis? -->

## Do Not Touch

<!-- Hard constraints for Claude this session -->
<!-- Example:
- Do not run prisma migrate — schema changes need review first
- Do not change the auth provider — Clerk is locked in
- Do not refactor the component structure — scope creep risk
-->

## Next Action

<!-- The single most important thing to do next -->
<!-- Example: Debug the 401 — add logging to refresh route and trace token validation -->

## Last Updated

2026-06-27
