---
type: playbook
title: MVP Build Checklist
description: Технически checklist за изграждане на MVP.
tags: [process, technical, mvp, development]
timestamp: 2026-06-23T00:00:00Z

vucp:
  stage_triggers: [build-launch]
  load_policy: required
  confidence: high
  owner: "Zahari Vitanov"
  last_reviewed: 2026-06-23
---

# MVP Build Checklist

## Week 1: Foundation

### Day 1-2: Setup
- [ ] Git repo created
- [ ] Development environment documented
- [ ] Database schema (minimal)
- [ ] Authentication (use service, don't build)
- [ ] Basic routing/pages

### Day 3-4: Core Feature
- [ ] The ONE thing works end-to-end
- [ ] User can complete core job
- [ ] Basic error handling
- [ ] Data persists

### Day 5: Polish
- [ ] Mobile responsive
- [ ] Basic loading states
- [ ] Error messages (human-readable)
- [ ] "It works" test with 1 user

## Week 2: Launch Ready

### Day 6-7: Payments
- [ ] Stripe integration
- [ ] Pricing page
- [ ] Subscription management
- [ ] Invoice/receipt

### Day 8-9: Onboarding
- [ ] Welcome email
- [ ] First-use tutorial (if needed)
- [ ] Empty states (what to do first)
- [ ] Help/docs (minimal)

### Day 10: Analytics
- [ ] Google Analytics or Plausible
- [ ] Key events tracked (signup, payment, core action)
- [ ] Dashboard for you to monitor

### Day 11-12: Launch Prep
- [ ] Domain configured
- [ ] SSL certificate
- [ ] Environment variables secure
- [ ] Database backups
- [ ] Rollback plan documented

### Day 13-14: Soft Launch
- [ ] 5 beta users invited
- [ ] Feedback collected
- [ ] Critical bugs fixed
- [ ] Ready for public

## Technical Decisions

### Auth: Don't Build
- **Clerk** — best developer experience
- **Auth0** — enterprise-ready
- **Supabase Auth** — open-source, free tier
- **NextAuth.js** — if you use Next.js

### Payments: Don't Build
- **Stripe Checkout** — simplest
- **Stripe Billing** — subscriptions
- **Paddle** — handles tax globally
- **LemonSqueezy** — simpler than Stripe

### Email: Don't Build
- **Resend** — beautiful, developer-friendly
- **SendGrid** — reliable, scalable
- **Mailgun** — transactional focus
- **Postmark** — best deliverability

### Hosting
- **Vercel** — Next.js, fastest deploy
- **Railway** — simple, scalable
- **Render** — good free tier
- **Fly.io** — global, Docker-based

### Database
- **Supabase PostgreSQL** — open-source Firebase
- **PlanetScale** — MySQL, serverless
- **Neon** — PostgreSQL, serverless
- **Turso** — SQLite at edge

## Security Basics
- [ ] HTTPS only
- [ ] Environment variables not in repo
- [ ] SQL injection prevention (use ORM)
- [ ] XSS prevention (framework handles most)
- [ ] Rate limiting on auth endpoints
- [ ] Basic GDPR compliance (privacy policy, data deletion)

## Performance Basics
- [ ] Page load < 3 seconds
- [ ] Core Web Vitals passing
- [ ] Images optimized
- [ ] No console errors

## Rollback Plan
```
IF critical bug in production:
  1. Identify last known good commit
  2. `git revert` or rollback deploy
  3. Notify users (status page, Twitter, email)
  4. Fix in staging
  5. Redeploy
  6. Post-mortem in _delta/ERRORS.md
```
