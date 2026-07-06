---
type: domain
title: MVP Scoping
description: Как да дефинираш точно какво да построиш — и какво НЕ.
tags: [product, scope, mvp, planning]
timestamp: 2026-06-23T00:00:00Z

vucp:
  stage_triggers: [solution-design, mvp-scope]
  load_policy: required
  confidence: high
  owner: "Zahari Vitanov"
  last_reviewed: 2026-06-23
---

# MVP Scoping

## The MVP Definition
Minimum Viable Product = **Minimum** set of features to **validate** core hypothesis with **real users**.

Not: "Everything we want to build eventually"
Not: "Everything competitors have"
Yes: "The smallest thing that proves people will pay"

## Scoping Framework

### 1. Core Job-to-be-Done
What is the ONE thing users hire this product to do?
- Not: "Manage projects" (too broad)
- Yes: "Know what to work on next without asking"

### 2. Must-Have vs. Nice-to-Have

| Must-Have | Nice-to-Have |
|---|---|
| User can sign up | Social login |
| Core feature works | Advanced settings |
| User can pay | Annual billing |
| Basic support | Live chat |
| Data export | API access |

Rule: If you can launch without it, it's nice-to-have.

### 3. The "Week 2" Test
"If we launch without X, will users still get value in week 2?"
- Yes → X is nice-to-have
- No → X is must-have

### 4. Time Boxing
- MVP should be buildable in **2-4 weeks** by 1-2 people
- If longer → scope is too big
- If shorter → might be too small to validate

### 5. Success Criteria
Before building, define:
- "We will consider MVP successful if:"
  - 10 people sign up
  - 3 people pay
  - 1 person uses it 3x/week

## Anti-Patterns

### Kitchen Sink MVP
"Let's add analytics, team features, API, mobile app..."
→ Never launches, never validates.

### Perfectionist MVP
"It's not ready, the button color isn't right..."
→ Launches too late, misses market timing.

### Fake MVP
"Landing page with email capture"
→ Validates interest, not willingness to pay.

## Tech Stack for MVP

### Criteria
1. Fast to build (days, not weeks)
2. Easy to change (you WILL change it)
3. Cheap to run (you're not making money yet)
4. Easy to hire for (if you need help)

### Recommended Stacks

**Full-stack frameworks:**
- Next.js + Vercel + Prisma + PostgreSQL
- Rails + Heroku + PostgreSQL
- Laravel + Forge + MySQL

**No-code/Low-code (for non-devs):**
- Bubble (complex apps)
- Webflow (marketing sites + CMS)
- Airtable + Softr (internal tools)

**Backend-as-a-Service:**
- Supabase (open-source Firebase)
- Firebase (Google ecosystem)

### What NOT to use for MVP
- Microservices (overkill)
- Kubernetes (overkill)
- Custom auth (use Auth0, Clerk, or Supabase Auth)
- Custom payments (use Stripe Checkout)
- Self-hosted email (use Resend, SendGrid)
