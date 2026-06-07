# Cookbook Post-Migration Runbook

This runbook covers the operational steps after migrating from Render Postgres to Vercel Neon Postgres.

## Scope

- Rotate credentials and reduce blast radius.
- Keep rollback possible during a short safety window.
- Retire the old Render database after stability is confirmed.

## Preconditions

- Production is live and healthy on Neon.
- Render web service DATABASE_URL points to Neon unpooled URL.
- Functional smoke tests have passed in production.

## Phase 1: Immediate Actions (same day)

1. Confirm live service health
- Check Render deploy is green and app routes load without 500 errors.
- Verify critical flows: login, create recipe, edit/delete, share, and popular page.

2. Freeze old Render database usage
- Confirm no services still reference old Render DB URL.
- Keep old DB read-only in practice: do not run writes or migrations against it.

3. Export safety snapshots
- Create a fresh backup from Neon.
- Keep the final pre-cutover Render backup and the first post-cutover Neon backup together.

4. Document final connection source of truth
- Production DB source: Neon unpooled URL in Render environment variables.
- Avoid pooled URL for Django runtime unless search_path behavior is explicitly validated.

## Phase 2: Credential Rotation (within 24 hours)

1. Rotate Neon credentials
- Generate a new Neon password or connection secret.
- Update Render DATABASE_URL with the rotated Neon credential.
- Trigger deploy and validate app health.
- Revoke old Neon credential.

2. Rotate Render service secrets that touched migration tooling
- Rotate any temporary or copied connection strings used during dump and restore.
- Remove migration-only local env values from developer machines if no longer needed.

3. Validate after each rotation
- Open homepage and auth flow.
- Create and delete a test recipe.
- Verify one read-heavy page (popular list).

## Phase 3: Old Render DB Retirement (after 3 to 7 days stable)

1. Keep rollback window
- Minimum suggested window: 72 hours with no production incidents.
- If traffic or risk is high, extend to 7 days.

2. Final pre-retirement checks
- Confirm no active connections or jobs use old Render DB.
- Confirm latest Neon backups are restorable.
- Confirm incident logs show no DB-related errors.

3. Decommission old Render DB
- Take one last Render DB snapshot.
- Delete old Render Postgres instance from Render dashboard.
- Record deletion date and operator in team notes.

## Rollback Plan

Use this only if production issues are clearly DB-related and cannot be fixed quickly.

1. Restore previous known-good DATABASE_URL in Render.
2. Redeploy immediately.
3. Verify app health and core write/read flows.
4. Capture incident timeline and compare schema/data drift before another cutover.

## Completion Checklist

- Neon credential rotated and old credential revoked.
- Render migration-time secrets cleaned up.
- No services reference old Render DB.
- Old Render DB snapshot archived.
- Old Render DB deleted after stability window.
- Runbook completion recorded in project notes.
