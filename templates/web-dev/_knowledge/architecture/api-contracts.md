---
type: api
title: API Contracts
description: API routes, expected inputs/outputs, and auth requirements.
tags: [api, routes, contracts, endpoints]
vucp:
  stage_triggers: [plan, implement]
  load_policy: required
  confidence: medium
  last_reviewed: 2026-06-27
---

# API Contracts

## Conventions

```yaml
base_url: /api
auth_header: "Authorization: Bearer <token>"
error_format:
  code: string      # machine-readable error code
  message: string   # human-readable message
  details: object   # optional field-level errors
content_type: application/json
```

## Routes

<!-- Document your API routes here. Update as you add endpoints. -->

<!--
### POST /api/auth/login
Auth: none
Body: { email: string, password: string }
Response 200: { user: User, accessToken: string }
Response 401: { code: "INVALID_CREDENTIALS", message: string }

### POST /api/auth/refresh
Auth: refreshToken (httpOnly cookie)
Body: none
Response 200: { accessToken: string }
Response 401: { code: "REFRESH_EXPIRED", message: string }

### GET /api/projects
Auth: required
Query: { page?: number, limit?: number }
Response 200: { data: Project[], total: number, page: number }
-->

## Server Actions (if using Next.js)

<!-- List important Server Actions and their contracts -->
<!--
### createProject(formData: FormData)
Auth: session required (redirects to /login if missing)
Input: name (string, min 3, max 50), description (string, optional)
Output: { project: Project } or throws ActionError
-->
