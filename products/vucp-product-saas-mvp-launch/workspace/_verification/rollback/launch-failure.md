# Rollback Plan: Launch Failure

## Trigger Conditions
- Site down > 1 hour
- Payment failures > 10%
- Critical security issue
- Data loss
- Negative viral feedback

## Immediate Actions (0-15 min)
1. **Assess severity**
   - Is it down completely? Partial? Data issue?

2. **Communicate**
   - Status page update
   - Twitter/post: "We're aware and investigating"
   - Email to active users (if applicable)

3. **Stop the bleeding**
   - If payment issue: pause new charges
   - If security: restrict access
   - If data: stop writes, preserve state

## Rollback Steps (15-60 min)
1. **Identify last known good**
   - Check deploy history
   - Check database backups

2. **Execute rollback**
   - Git revert to last good commit
   - OR restore last database backup
   - OR switch to staging environment

3. **Verify rollback**
   - Core feature works
   - Payments work
   - No data corruption

4. **Communicate resolution**
   - "We're back. Here's what happened."
   - Be honest, not defensive

## Post-Incident (1-24 hours)
1. **Document in `/_delta/ERRORS.md`**
2. **Post-mortem**
   - What happened?
   - Why did it happen?
   - How did we detect it?
   - How did we fix it?
   - How do we prevent it?
3. **Update safeguards**
4. **Follow up with affected users**

## Contacts
- Hosting provider: [ ]
- Payment processor: [ ]
- Domain registrar: [ ]
- Team members: [ ]
