---
type: reference
title: Environment Variables
description: All environment variables used in the project — purpose and where to set them.
tags: [env, config, secrets, environment]
vucp:
  stage_triggers: [context-load]
  load_policy: required
  confidence: high
  last_reviewed: 2026-06-27
---

# Environment Variables

**Never commit actual values. This file documents purpose only.**

## Required (All Environments)

```bash
# Database
DATABASE_URL="postgresql://..."        # Prisma connection string

# Auth
NEXTAUTH_SECRET="..."                  # Random 32+ char string
NEXTAUTH_URL="http://localhost:3000"   # Full URL of the app
```

## Required (Production Only)

```bash
# Set in Vercel / hosting dashboard
DATABASE_URL="..."                     # Production DB connection
NEXTAUTH_URL="https://app.example.com"
```

## Optional Services

```bash
# Stripe (if payments enabled)
STRIPE_SECRET_KEY="sk_..."
STRIPE_WEBHOOK_SECRET="whsec_..."
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY="pk_..."

# Resend (if email enabled)
RESEND_API_KEY="re_..."
EMAIL_FROM="noreply@example.com"

# Storage (if file upload enabled)
S3_BUCKET_NAME="..."
S3_REGION="..."
S3_ACCESS_KEY_ID="..."
S3_SECRET_ACCESS_KEY="..."
```

## Claude Rules for Env Vars

- Never suggest hardcoding values that belong in env vars
- Never suggest committing `.env.production`
- When adding a new service, always update this file first
- Use `NEXT_PUBLIC_` prefix only for values safe to expose to the browser
