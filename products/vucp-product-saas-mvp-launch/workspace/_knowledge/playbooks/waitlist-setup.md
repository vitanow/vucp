---
type: playbook
title: Waitlist Setup Playbook
description: Как да събереш имейли преди да си готов за launch.
tags: [process, technical, waitlist, email]
timestamp: 2026-06-23T00:00:00Z

vucp:
  stage_triggers: [waitlist-setup]
  load_policy: required
  confidence: high
  owner: "Zahari Vitanov"
  last_reviewed: 2026-06-23
---

# Waitlist Setup Playbook

## Why Waitlist?
- Validate demand before building
- Build audience for launch day
- Create urgency ("First 100 get X")
- Test messaging

## The Waitlist Page

### Structure
```
[Hero: Problem + Promise]
"Tired of [pain]? [Product] solves it. 
Join the waitlist — launch in [date]."

[Email Input]
[CTA: "Get Early Access"]

[Social Proof]
"[Number] people already waiting"

[FAQ]
Q: When do you launch?
A: [Date]. Waitlist gets first access.

Q: Is it free?
A: Free trial, then $X/month.

Q: Can I get a discount?
A: Waitlist members get 50% off first 3 months.
```

## Tools

### Simple (No-Code)
- **Carrd** ($19/year) — waitlist page + form
- **Tally** (free) — form, connects to Notion/Airtable
- **Notion** (free) — database + simple page

### Email Collection
- **Mailchimp** (free up to 500) — basic, reliable
- **ConvertKit** (free up to 1000) — creator-focused
- **Resend** (free up to 3000) — developer-friendly, beautiful emails

### Full Stack
- **Next.js + Supabase** — custom, scalable
- **Webflow + Zapier** — no-code + automation

## Email Sequence (Waitlist → Launch)

### Email 1: Welcome (immediate)
```
Subject: You're in! Here's what happens next.

Hi [Name],

Thanks for joining the waitlist for [Product]!

Here's what to expect:
- Launch date: [Date]
- First 100 get 50% off
- Weekly updates on our progress

Reply with your biggest [problem] challenge — 
I read every email.

[Your name]
```

### Email 2: Progress Update (Week 1)
```
Subject: Week 1 update: [Specific milestone]

Hi [Name],

Quick update on [Product]:

✅ [Milestone 1]
🔄 [Milestone 2 — in progress]
📅 [Milestone 3 — next week]

Behind the scenes: [Personal story/challenge]

Questions? Just reply.

[Your name]
```

### Email 3: Launch Day
```
Subject: 🚀 [Product] is live! (Waitlist discount inside)

Hi [Name],

Today's the day. [Product] is live.

As a waitlist member, you get:
✅ 50% off first 3 months
✅ Priority support
✅ [Bonus feature]

[Get Started — 2 Minute Setup]

This discount expires in 48 hours.

[Your name]
```

### Email 4: Post-Launch (Day 3)
```
Subject: How's your first week with [Product]?

Hi [Name],

Hope you're enjoying [Product]!

Quick questions:
1. What's working well?
2. What's confusing?
3. What should we build next?

Reply directly — I read everything.

[Your name]
```

## Waitlist Metrics
Track weekly:
- Signups
- Open rate (emails)
- Click rate
- Conversion to paid (at launch)
- Referrals (if you have referral program)

## Common Mistakes
- Waitlist without launch date (people forget)
- No email sequence (cold launch)
- No incentive (why should they wait?)
- No updates (they forget you exist)
- Too many emails (unsubscribe spike)
