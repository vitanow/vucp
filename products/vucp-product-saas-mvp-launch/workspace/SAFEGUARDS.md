# Safeguards

## Core Rule
Този продукт е за MVP launch, не за production scale. Винаги мисли: "Може ли да се обърне?"

## Never Change Without Explicit Approval
- Domain names (след като са купени)
- Payment processor settings (Stripe, etc.)
- Live database schema
- Email sender reputation (SPF, DKIM)
- Customer data (GDPR/CCPA)
- Pricing след първи customers

## Always Include Before Risky Changes
- Risk assessment (1-5)
- What changes
- Verification steps
- Rollback plan
- Files changed
- Commands to run manually

## Stage-Specific Safeguards

### Build & Launch (high risk)
- Pre-launch checklist MUST be completed
- Rollback plan MUST exist in `_verification/rollback/`
- Database backup before schema changes
- Staging environment test before production
- Email deliverability test before blast

### MVP Scope (high risk)
- Feature list MUST have "will not build" section
- Timeline MUST include buffer (20%)
- Tech stack MUST have migration path
- Cost estimate MUST include hosting for 6 months

### Waitlist Setup (medium risk)
- Email compliance (GDPR opt-in, unsubscribe)
- Data storage location (EU vs US)
- Third-party tool terms (Mailchimp, etc.)

## Human Approval Required
- Any payment processing setup
- Any customer data collection
- Any public launch (Hacker News, Product Hunt, etc.)
- Any pricing change
- Any database migration
- Any third-party integration with data access

## Rollback Triggers
- Launch site down > 1 hour
- Email bounce rate > 5%
- Payment failures > 10%
- Negative feedback from > 3 beta users
- Security concern of any kind
