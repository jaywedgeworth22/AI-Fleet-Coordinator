# Fleet admin panel

One page at **https://admin.jays.services** that shows the state of every fleet app,
platform, and service, and lets you search the fleet RAG corpus.  It is a single
Cloudflare Worker with no build step, no npm dependencies, and no TypeScript.

The Worker holds every fleet API token, so the browser never sees a credential and
never talks to a fleet API directly.  That also means **the hostname must stay behind
Cloudflare Access** — the Worker proxies authenticated fleet APIs, so anyone who can
open the page can read The Board, the RAG corpus, Coolify, Sentry, and PagerDuty.
Access is the only thing standing in front of it.

## What each card shows

| Card | Source | What a row means |
|---|---|---|
| **Public Endpoints** | Direct HTTPS probe of 16 fleet surfaces, 8 s timeout, run in parallel | HTTP status and latency.  2xx and 3xx are up; a redirect to `cloudflareaccess.com` reads "Up, behind Access". |
| **Fleet Recall** | `GET /health`, `GET /recall/stats`, and a canary `POST /recall/search` for `fleet mode` on `recall.jays.services` | Point count, collection name and status, embedder and reranker health, per-source breakdown, and the canary hits.  The search box at the top of the card queries the live corpus. |
| **The Board** | `GET /findings/stats` and `GET /findings?status=open,in_progress` on `mac.jays.services` | Open and in-progress counts by severity, plus the P0 and P1 rows that need attention. |
| **Coolify Applications** | `GET /api/v1/applications` and `/api/v1/servers` on `host.jays.services` | Container status (`running:healthy`, `exited:unhealthy`, …) per application, then server reachability. |
| **GitHub Repositories** | Search API for open PRs and the Actions API for the latest run on `main`, per repo in `fleet-apps.json` | Open PR count and the conclusion of the most recent `main` run.  The row links to that run. |
| **Vercel Projects** | `GET /v9/projects?limit=50`, retried per team when the personal scope is empty | `latestDeployments[0].readyState` — READY, ERROR, BUILDING. |
| **Sentry Issues** | `GET /organizations/jays-services/issues/?query=is:unresolved&statsPeriod=24h` | Unresolved issue count grouped by project slug, with the newest title. |
| **PagerDuty Incidents** | `GET /incidents?statuses[]=triggered&statuses[]=acknowledged` | Open incident titles and their service. |
| **Datadog Monitors** | `GET /api/v1/monitor?page_size=100` on the `us5` site | Monitor counts by `overall_state`, then the alerting and warning monitors by name. |

Every integration runs in parallel with its own timeout and its own error handling.
A missing secret makes that one card read "Not configured"; a failing call puts the
error text on that one card.  Neither stops the rest of the page from rendering.

## Routes

| Route | Behaviour |
|---|---|
| `GET /` | The page, served from `public/` through the `ASSETS` binding. |
| `GET /api/status` | Runs every integration and returns one JSON object keyed by section.  Cached in the isolate for 30 seconds so refreshes and extra viewers do not hammer the APIs. |
| `GET /api/recall/search?q=…&limit=…` | Proxies the fleet RAG search and returns the hits.  `limit` is capped at 25. |

Every API response sets `Cache-Control: no-store`.  The page loads `/api/status` on
open, again every 60 seconds, and when the tab becomes visible.

## Secrets

Set these from this directory before the first real check.  Every one of them is
optional in the sense that the page still renders without it — the matching card
just reads "Not configured".

```bash
wrangler secret put RECALL_API_TOKEN
wrangler secret put CF_ACCESS_CLIENT_ID
wrangler secret put CF_ACCESS_CLIENT_SECRET
wrangler secret put COOLIFY_TOKEN
wrangler secret put GITHUB_TOKEN
wrangler secret put VERCEL_TOKEN
wrangler secret put SENTRY_AUTH_TOKEN
wrangler secret put PAGERDUTY_API_KEY
wrangler secret put DD_API_KEY
wrangler secret put DD_APP_KEY
wrangler secret put MAC_COLLAB_TOKEN
```

Values in `~/.secrets/global-api-keys` are quote-wrapped.  Strip the quotes before
pasting, or the service answers 401 as if the token were revoked.

The Fleet Recall card needs three of these together: `RECALL_API_TOKEN` for the
service bearer, and `CF_ACCESS_CLIENT_ID` plus `CF_ACCESS_CLIENT_SECRET` for the
Cloudflare Access service token in front of the host.  `GET /health` is public and
is checked even when the other two are missing.

Non-secret configuration lives in `wrangler.jsonc` under `vars`: `GITHUB_OWNER`,
`SENTRY_ORG`, `DD_SITE`, and the `RECALL_BASE` / `BOARD_BASE` / `COOLIFY_BASE`
hostnames.

## Deploy

```bash
cd scripts/admin-panel
wrangler deploy
```

The Worker is `admin-jays-services` on the **Usage.Jays.Services** Cloudflare
account, zone `jays.services`, bound to `admin.jays.services` as a custom domain.

`compatibility_date` is pinned to `2026-08-27` because that is the newest date the
workerd binary shipped with wrangler 4.125.0 accepts locally.  Raise it once the
local binary catches up.

## Local development

```bash
cd scripts/admin-panel
wrangler dev --port 8790
curl -s localhost:8790/api/status | head -c 600
```

Local mode needs no Cloudflare login.  Without secrets, the Endpoints card returns
real probe results and every secret-backed card reports "Not configured", which is
the intended degraded state.

## Keeping it in sync

`APPS` in `src/index.js` mirrors `apps[]` from `fleet-apps.json` at the repo root.
The Worker has no filesystem, so the registry is inlined.  Add a row there when an
app is onboarded, and add its public URL to `ENDPOINTS` in the same file.
