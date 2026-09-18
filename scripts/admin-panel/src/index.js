/**
 * Fleet admin panel — https://admin.jays.services
 *
 * A single Cloudflare Worker that fans out to every fleet control plane and
 * returns one status document.  Every integration degrades on its own: a
 * missing secret reports "Not configured", a failing call reports its error
 * text, and neither stops the other cards from rendering.
 *
 * Routes:
 *   GET /api/status              every integration, cached in memory for 30 s
 *   GET /api/recall/search?q=    proxy for the fleet RAG search
 *   *                            static assets from ./public
 */

const UA = 'admin-jays-services/1.0';
const CACHE_TTL_MS = 30_000;
const PROBE_TIMEOUT_MS = 8_000;
const API_TIMEOUT_MS = 12_000;

// Public surfaces to probe.  Anything behind Cloudflare Access answers with a
// redirect to cloudflareaccess.com, which still counts as up.
const ENDPOINTS = [
  { name: 'Socratic Trade', url: 'https://socratictrade.com' },
  { name: 'Congress.Trade', url: 'https://congress.trade' },
  { name: 'Usage Monitor', url: 'https://usage.jays.services' },
  { name: 'DealDex', url: 'https://dealdex.net' },
  { name: 'Personal Site', url: 'https://jays.services' },
  { name: 'BotFleet', url: 'https://botfleet.app' },
  { name: 'Autorotate', url: 'https://autorotate.codes' },
  { name: 'ContactLogo', url: 'https://contactlogo.com' },
  { name: 'Start Page', url: 'https://start.jays.services' },
  { name: 'The Board', url: 'https://mac.jays.services/board' },
  { name: 'Coolify', url: 'https://host.jays.services' },
  { name: 'Agents Gateway', url: 'https://agents.jays.services/health' },
  { name: 'Scout', url: 'https://scout.jays.services/health' },
  { name: 'Xcode Bridge', url: 'https://xcode.jays.services/health' },
  { name: 'Agent Sync', url: 'https://agent-sync.jays.services/health' },
  { name: 'Fleet Recall', url: 'https://recall.jays.services/health' },
];

// Mirrors fleet-apps.json at the repo root (apps[].repo / .displayName / .kind).
// The Worker has no filesystem, so the registry is inlined here.  Keep in sync
// when an app is onboarded.
const APPS = [
  { repo: 'Socratic.Trade', name: 'Socratic Trade', kind: 'product' },
  { repo: 'Congress.Trade', name: 'Congress.Trade', kind: 'product' },
  { repo: 'Usage-Monitor', name: 'Usage Monitor', kind: 'product' },
  { repo: 'congress-trading-shared', name: 'congress-trading-shared', kind: 'library' },
  { repo: 'DealDex', name: 'DealDex.net', kind: 'product' },
  { repo: 'ai-fleet-coordinator', name: 'AI Fleet Coordinator', kind: 'infra' },
  { repo: 'Personal-Site', name: 'Personal Site', kind: 'product' },
  { repo: 'Autorotate', name: 'Autorotate.Codes', kind: 'product' },
  { repo: 'ContactLogo', name: 'ContactLogo', kind: 'product' },
  { repo: 'BotFleet', name: 'BotFleet.app', kind: 'product' },
  { repo: 'HogHunter', name: 'Hog Hunter', kind: 'product' },
  { repo: 'fleet-ops', name: 'Fleet Ops', kind: 'infra' },
];

/* ------------------------------------------------------------------ utils */

function errText(err) {
  const name = err && err.name;
  if (name === 'TimeoutError' || name === 'AbortError') return 'Timed out';
  const msg = (err && err.message) || String(err);
  // workerd reports a connection failure as "internal error; reference = …",
  // which is noise on a status page.
  if (/^internal error/i.test(msg)) return 'Unreachable';
  return msg.length > 200 ? `${msg.slice(0, 200)}…` : msg;
}

function bodySnippet(text) {
  if (!text) return '';
  const flat = text.replace(/\s+/g, ' ').trim();
  if (!flat) return '';
  return ` — ${flat.length > 140 ? `${flat.slice(0, 140)}…` : flat}`;
}

async function apiJson(url, { headers = {}, method = 'GET', body, timeoutMs = API_TIMEOUT_MS } = {}) {
  const res = await fetch(url, {
    method,
    body,
    headers: { 'User-Agent': UA, Accept: 'application/json', ...headers },
    signal: AbortSignal.timeout(timeoutMs),
  });
  const text = await res.text();
  if (!res.ok) throw new Error(`HTTP ${res.status}${bodySnippet(text)}`);
  try {
    return JSON.parse(text);
  } catch {
    throw new Error(`HTTP ${res.status} but the response was not JSON`);
  }
}

// Wraps a section so one failure can never take the page down.
async function section(fn) {
  const started = Date.now();
  try {
    const out = await fn();
    return { ms: Date.now() - started, ...out };
  } catch (err) {
    return { ok: false, state: 'down', summary: 'Check failed', error: errText(err), items: [], ms: Date.now() - started };
  }
}

function notConfigured(...names) {
  return {
    ok: false,
    state: 'off',
    summary: 'Not configured',
    error: `Set ${names.join(' and ')} with wrangler secret put.`,
    items: [],
  };
}

function missing(env, ...names) {
  return names.filter((n) => !env[n]);
}

function accessHeaders(env) {
  return {
    'CF-Access-Client-Id': env.CF_ACCESS_CLIENT_ID,
    'CF-Access-Client-Secret': env.CF_ACCESS_CLIENT_SECRET,
  };
}

/* -------------------------------------------------------------- endpoints */

async function probe(ep) {
  const started = Date.now();
  try {
    const res = await fetch(ep.url, {
      redirect: 'manual',
      headers: { 'User-Agent': UA, Accept: 'text/html,application/json;q=0.9,*/*;q=0.8' },
      signal: AbortSignal.timeout(PROBE_TIMEOUT_MS),
    });
    const ms = Date.now() - started;
    const status = res.status;
    const location = res.headers.get('location') || '';
    if (status >= 200 && status < 300) {
      return { name: ep.name, url: ep.url, state: 'up', status, ms, detail: 'Up' };
    }
    if (status >= 300 && status < 400) {
      const behindAccess = location.includes('cloudflareaccess.com');
      return {
        name: ep.name,
        url: ep.url,
        state: 'up',
        status,
        ms,
        detail: behindAccess ? 'Up, behind Access' : 'Up, redirects',
      };
    }
    return { name: ep.name, url: ep.url, state: 'down', status, ms, detail: `HTTP ${status}` };
  } catch (err) {
    return {
      name: ep.name,
      url: ep.url,
      state: 'down',
      status: 0,
      ms: Date.now() - started,
      detail: errText(err),
    };
  }
}

async function checkEndpoints() {
  const items = await Promise.all(ENDPOINTS.map(probe));
  const down = items.filter((i) => i.state === 'down');
  return {
    ok: down.length === 0,
    state: down.length === 0 ? 'up' : 'down',
    summary: down.length === 0
      ? `${items.length} of ${items.length} up`
      : `${items.length - down.length} of ${items.length} up, ${down.length} down`,
    items,
  };
}

/* ------------------------------------------------------------ fleet recall */

// Contract lives in scripts/fleet-recall-service/server.py and
// scripts/fleet_rag/recall_api.py:
//   GET  /health         public, no auth
//   GET  /recall/stats   bearer
//   POST /recall/search  bearer, body { query, limit, ... }
// The whole host also sits behind Cloudflare Access, so service-token headers
// ride along on every call including /health.

function recallBase(env) {
  return env.RECALL_BASE || 'https://recall.jays.services';
}

function recallHeaders(env) {
  return {
    ...accessHeaders(env),
    Authorization: `Bearer ${env.RECALL_API_TOKEN}`,
    'Content-Type': 'application/json',
  };
}

// /health is exempt from the bearer check but still behind Access, so send the
// service-token headers when we have them.
function recallPublicHeaders(env) {
  return env.CF_ACCESS_CLIENT_ID && env.CF_ACCESS_CLIENT_SECRET ? accessHeaders(env) : {};
}

export async function recallSearch(env, query, limit = 8) {
  const data = await apiJson(`${recallBase(env)}/recall/search`, {
    method: 'POST',
    headers: recallHeaders(env),
    body: JSON.stringify({ query, limit }),
  });
  return { hits: (data.hits || []).map(normaliseHit), mode: data.mode || '' };
}

// Hit fields come from _hit() in scripts/fleet_rag/recall_api.py: score, text,
// source, app, category, seat, doc_id, chunk_index, heading, title, url, path,
// created_at (epoch ms).
function normaliseHit(h) {
  const created = typeof h.created_at === 'number' && h.created_at > 0 ? h.created_at : '';
  return {
    title: h.title || h.heading || h.doc_id || 'Untitled',
    score: typeof h.score === 'number' ? h.score : null,
    seat: h.seat || '',
    date: created,
    category: h.category || '',
    app: h.app || '',
    source: h.source || '',
    url: h.url || '',
    path: h.path || '',
    text: h.text || '',
  };
}

async function checkRecall(env) {
  const health = await section(async () => {
    const data = await apiJson(`${recallBase(env)}/health`, {
      headers: recallPublicHeaders(env),
      timeoutMs: PROBE_TIMEOUT_MS,
    });
    const up = data.ok === true && data.backend_ok !== false;
    return {
      ok: up,
      state: up ? 'up' : 'warn',
      summary: up ? 'Healthy' : (data.error ? String(data.error) : 'Backend is not answering'),
      points: typeof data.points === 'number' ? data.points : null,
      collection: data.collection || '',
      version: data.version || '',
    };
  });

  const gaps = missing(env, 'RECALL_API_TOKEN', 'CF_ACCESS_CLIENT_ID', 'CF_ACCESS_CLIENT_SECRET');
  if (gaps.length) {
    return {
      ...notConfigured(...gaps),
      health,
      points: health.points ?? null,
      collection: health.collection || '',
      state: health.ok ? 'warn' : 'off',
      summary: health.ok ? 'Healthy, but search is not configured' : 'Not configured',
    };
  }

  const [stats, canary] = await Promise.all([
    section(async () => {
      const data = await apiJson(`${recallBase(env)}/recall/stats`, { headers: recallHeaders(env) });
      return {
        ok: true,
        state: data.embedder_healthy === false ? 'warn' : 'up',
        summary: data.embedder_healthy === false ? 'Embedder is unhealthy' : 'Stats read',
        points: typeof data.points === 'number' ? data.points : null,
        collection: data.collection || '',
        collectionStatus: data.status || '',
        embedder: data.embedder_healthy,
        reranker: data.rerank_healthy,
        bySource: data.by_source || {},
        byApp: data.by_app || {},
      };
    }),
    section(async () => {
      const { hits, mode } = await recallSearch(env, 'fleet mode', 5);
      const ok = hits.length > 0;
      return {
        ok,
        state: ok ? 'up' : 'warn',
        summary: ok ? `${hits.length} hits, mode ${mode || 'unknown'}` : 'No hits for the canary query',
        items: hits,
      };
    }),
  ]);

  const points = stats.points ?? health.points ?? null;
  const parts = [];
  if (points !== null) parts.push(`${points.toLocaleString('en-US')} points`);
  parts.push(health.ok ? 'healthy' : 'health check failed');
  parts.push(canary.ok ? 'canary passed' : 'canary failed');
  if (stats.reranker === false) parts.push('reranker unhealthy');

  const state = health.ok && canary.ok && stats.ok
    ? (stats.state === 'warn' ? 'warn' : 'up')
    : (health.ok ? 'warn' : 'down');

  // Top sources by point count, so the card says something about the corpus.
  const breakdown = Object.entries(stats.bySource || {})
    .filter(([, n]) => Number(n) > 0)
    .sort((a, b) => b[1] - a[1])
    .map(([name, count]) => ({ name, count, state: 'up' }));

  return {
    ok: state === 'up',
    state,
    summary: parts.join(', '),
    health,
    stats,
    canary,
    points,
    collection: stats.collection || health.collection || '',
    collectionStatus: stats.collectionStatus || '',
    breakdown,
    items: canary.items || [],
    error: [health.error, stats.error, canary.error].filter(Boolean).join(' · ') || undefined,
  };
}

/* -------------------------------------------------------------- the board */

// scripts/mac-collab/mac-collab-server.py:
//   GET /health         public
//   GET /findings/stats bearer -> { total, open, p0p1_open, done, by_kind, apps }
//   GET /findings       bearer -> { findings: [...], count, total_matching }
// The stats route has no per-severity or per-status breakdown, so the open
// rows are listed once and counted here.
async function checkBoard(env) {
  if (!env.MAC_COLLAB_TOKEN) return notConfigured('MAC_COLLAB_TOKEN');
  const base = env.BOARD_BASE || 'https://mac.jays.services';
  const headers = { Authorization: `Bearer ${env.MAC_COLLAB_TOKEN}` };

  const [stats, rows] = await Promise.all([
    apiJson(`${base}/findings/stats`, { headers }),
    apiJson(`${base}/findings?status=open,in_progress&limit=2000`, { headers })
      .catch((err) => ({ __error: errText(err) })),
  ]);

  const findings = (rows && rows.findings) || [];
  const bySeverity = { P0: 0, P1: 0, P2: 0, P3: 0, P4: 0 };
  let open = 0;
  let inProgress = 0;
  for (const f of findings) {
    if (bySeverity[f.severity] !== undefined) bySeverity[f.severity] += 1;
    if (f.status === 'open') open += 1;
    else if (f.status === 'in_progress') inProgress += 1;
  }

  const items = Object.entries(bySeverity)
    .filter(([key, n]) => n > 0 || key === 'P0' || key === 'P1')
    .map(([name, count]) => ({
      name,
      count,
      state: count === 0 ? 'up' : (name === 'P0' ? 'down' : (name === 'P1' ? 'warn' : 'up')),
    }));

  const urgent = findings
    .filter((f) => f.severity === 'P0' || f.severity === 'P1')
    .slice(0, 6)
    .map((f) => ({
      name: f.title || `Finding ${f.id}`,
      sub: [f.app, f.addressed_by || 'unclaimed'].filter(Boolean).join(' · '),
      status: `${f.severity} ${String(f.status || '').replace('_', ' ')}`,
      state: f.severity === 'P0' ? 'down' : 'warn',
      url: `${base}/board`,
    }));

  const openTotal = Number(stats.open ?? (open + inProgress));
  const p0p1 = Number(stats.p0p1_open ?? (bySeverity.P0 + bySeverity.P1));
  const state = bySeverity.P0 > 0 ? 'down' : (p0p1 > 0 ? 'warn' : 'up');

  return {
    ok: state === 'up',
    state,
    summary: `${open} open, ${inProgress} in progress, ${p0p1} at P0 or P1`,
    items,
    urgent,
    counts: { total: Number(stats.total || 0), open: openTotal, done: Number(stats.done || 0), p0p1 },
    byKind: stats.by_kind || {},
    apps: stats.apps || [],
    error: rows && rows.__error ? `Findings list: ${rows.__error}` : undefined,
  };
}

/* ---------------------------------------------------------------- coolify */

async function checkCoolify(env) {
  if (!env.COOLIFY_TOKEN) return notConfigured('COOLIFY_TOKEN');
  const base = env.COOLIFY_BASE || 'https://host.jays.services';
  const headers = { Authorization: `Bearer ${env.COOLIFY_TOKEN}` };

  const [apps, servers] = await Promise.all([
    apiJson(`${base}/api/v1/applications`, { headers }),
    apiJson(`${base}/api/v1/servers`, { headers }).catch((err) => ({ __error: errText(err) })),
  ]);

  const list = Array.isArray(apps) ? apps : (apps.data || []);
  const items = list.map((a) => {
    const status = String(a.status || 'unknown');
    return {
      name: a.name || a.uuid || 'unnamed',
      status,
      state: coolifyState(status),
      url: a.fqdn ? String(a.fqdn).split(',')[0].trim() : '',
      uuid: a.uuid || '',
    };
  }).sort((x, y) => x.name.localeCompare(y.name));

  const serverList = Array.isArray(servers) ? servers : (servers.data || []);
  const serverItems = serverList.map((s) => ({
    name: s.name || 'server',
    state: s.is_reachable && s.is_usable ? 'up' : (s.is_reachable ? 'warn' : 'down'),
    status: s.is_reachable ? (s.is_usable ? 'reachable and usable' : 'reachable, not usable') : 'unreachable',
  }));

  const bad = items.filter((i) => i.state === 'down').length;
  const warn = items.filter((i) => i.state === 'warn').length;
  return {
    ok: bad === 0,
    state: bad > 0 ? 'down' : (warn > 0 ? 'warn' : 'up'),
    summary: `${items.length - bad - warn} of ${items.length} running`,
    items,
    servers: serverItems,
    error: servers && servers.__error ? `Servers: ${servers.__error}` : undefined,
  };
}

function coolifyState(status) {
  const s = status.toLowerCase();
  if (s.startsWith('running')) return s.includes('unhealthy') ? 'warn' : 'up';
  if (s.startsWith('exited') || s.startsWith('stopped') || s.startsWith('degraded')) return 'down';
  if (s.startsWith('restarting') || s.startsWith('starting')) return 'warn';
  return 'warn';
}

/* ----------------------------------------------------------------- github */

async function checkGitHub(env) {
  if (!env.GITHUB_TOKEN) return notConfigured('GITHUB_TOKEN');
  const owner = env.GITHUB_OWNER || 'jaywedgeworth22';
  const headers = {
    Authorization: `Bearer ${env.GITHUB_TOKEN}`,
    Accept: 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28',
  };

  const items = await Promise.all(APPS.map(async (app) => {
    const row = { name: app.name, repo: app.repo, kind: app.kind, prs: null, run: null, state: 'warn' };

    const [prs, runs] = await Promise.all([
      apiJson(
        `https://api.github.com/search/issues?q=${encodeURIComponent(`repo:${owner}/${app.repo} is:pr is:open`)}`,
        { headers },
      ).catch((err) => ({ __error: errText(err) })),
      apiJson(
        `https://api.github.com/repos/${owner}/${app.repo}/actions/runs?branch=main&per_page=1`,
        { headers },
      ).catch((err) => ({ __error: errText(err) })),
    ]);

    if (prs && prs.__error) row.prError = prs.__error;
    else row.prs = Number(prs.total_count || 0);

    if (runs && runs.__error) {
      row.runError = runs.__error;
    } else {
      const run = (runs.workflow_runs || [])[0];
      if (run) {
        row.run = {
          status: run.status,
          conclusion: run.conclusion,
          url: run.html_url,
          updated: run.updated_at,
          name: run.name,
        };
      }
    }

    row.state = runState(row.run);
    return row;
  }));

  const failing = items.filter((i) => i.state === 'down');
  const openPrs = items.reduce((n, i) => n + (i.prs || 0), 0);
  return {
    ok: failing.length === 0,
    state: failing.length === 0 ? 'up' : 'down',
    summary: `${openPrs} open PRs, ${failing.length === 0 ? 'main green everywhere' : `${failing.length} repos failing on main`}`,
    items,
  };
}

function runState(run) {
  if (!run) return 'warn';
  if (run.status !== 'completed') return 'warn';
  if (run.conclusion === 'success') return 'up';
  if (run.conclusion === 'skipped' || run.conclusion === 'neutral' || run.conclusion === 'cancelled') return 'warn';
  return 'down';
}

/* ----------------------------------------------------------------- vercel */

async function checkVercel(env) {
  if (!env.VERCEL_TOKEN) return notConfigured('VERCEL_TOKEN');
  const headers = { Authorization: `Bearer ${env.VERCEL_TOKEN}` };

  let projects = await fetchVercelProjects(headers, '');
  const scopes = [];
  if (!projects.length) {
    const teams = await apiJson('https://api.vercel.com/v2/teams', { headers }).catch(() => ({ teams: [] }));
    for (const team of teams.teams || []) {
      const scoped = await fetchVercelProjects(headers, `&teamId=${encodeURIComponent(team.id)}`);
      if (scoped.length) scopes.push(team.slug || team.name || team.id);
      projects = projects.concat(scoped);
    }
  }

  const items = projects.map((p) => {
    const dep = (p.latestDeployments || [])[0] || {};
    const readyState = dep.readyState || dep.state || 'UNKNOWN';
    return {
      name: p.name,
      status: String(readyState).toLowerCase(),
      state: vercelState(readyState),
      url: dep.url ? `https://${dep.url}` : '',
      updated: dep.createdAt ? new Date(dep.createdAt).toISOString() : '',
    };
  }).sort((a, b) => a.name.localeCompare(b.name));

  const bad = items.filter((i) => i.state === 'down').length;
  return {
    ok: bad === 0,
    state: bad > 0 ? 'down' : 'up',
    summary: items.length
      ? `${items.length} projects, ${bad === 0 ? 'no failed deployments' : `${bad} failed`}${scopes.length ? ` (teams: ${scopes.join(', ')})` : ''}`
      : 'No projects visible to this token',
    items,
  };
}

async function fetchVercelProjects(headers, suffix) {
  const data = await apiJson(`https://api.vercel.com/v9/projects?limit=50${suffix}`, { headers });
  return data.projects || [];
}

function vercelState(readyState) {
  const s = String(readyState).toUpperCase();
  if (s === 'READY') return 'up';
  if (s === 'ERROR' || s === 'CANCELED') return 'down';
  if (s === 'BUILDING' || s === 'QUEUED' || s === 'INITIALIZING') return 'warn';
  return 'warn';
}

/* ----------------------------------------------------------------- sentry */

async function checkSentry(env) {
  if (!env.SENTRY_AUTH_TOKEN) return notConfigured('SENTRY_AUTH_TOKEN');
  const org = env.SENTRY_ORG || 'jays-services';
  const issues = await apiJson(
    `https://sentry.io/api/0/organizations/${org}/issues/?query=${encodeURIComponent('is:unresolved')}&statsPeriod=24h&limit=100`,
    { headers: { Authorization: `Bearer ${env.SENTRY_AUTH_TOKEN}` } },
  );

  const byProject = new Map();
  for (const issue of issues) {
    const slug = (issue.project && issue.project.slug) || 'unknown';
    const row = byProject.get(slug) || { name: slug, count: 0, top: '' };
    row.count += 1;
    if (!row.top) row.top = issue.title || issue.culprit || '';
    byProject.set(slug, row);
  }

  const items = [...byProject.values()]
    .map((r) => ({ ...r, state: r.count === 0 ? 'up' : (r.count > 10 ? 'down' : 'warn') }))
    .sort((a, b) => b.count - a.count);

  return {
    ok: issues.length === 0,
    state: issues.length === 0 ? 'up' : (issues.length > 25 ? 'down' : 'warn'),
    summary: issues.length === 0
      ? 'No unresolved issues in the last 24 hours'
      : `${issues.length} unresolved issues across ${items.length} projects`,
    items,
    link: `https://${org}.sentry.io`,
  };
}

/* -------------------------------------------------------------- pagerduty */

async function checkPagerDuty(env) {
  if (!env.PAGERDUTY_API_KEY) return notConfigured('PAGERDUTY_API_KEY');
  const data = await apiJson(
    'https://api.pagerduty.com/incidents?statuses[]=triggered&statuses[]=acknowledged&limit=25',
    {
      headers: {
        Authorization: `Token token=${env.PAGERDUTY_API_KEY}`,
        Accept: 'application/vnd.pagerduty+json;version=2',
      },
    },
  );

  const items = (data.incidents || []).map((i) => ({
    name: i.title || i.summary || 'Incident',
    status: i.status,
    state: i.status === 'triggered' ? 'down' : 'warn',
    url: i.html_url || '',
    service: (i.service && i.service.summary) || '',
    urgency: i.urgency || '',
  }));

  return {
    ok: items.length === 0,
    state: items.some((i) => i.state === 'down') ? 'down' : (items.length ? 'warn' : 'up'),
    summary: items.length === 0 ? 'No open incidents' : `${items.length} open incidents`,
    items,
  };
}

/* ---------------------------------------------------------------- datadog */

async function checkDatadog(env) {
  const gaps = missing(env, 'DD_API_KEY', 'DD_APP_KEY');
  if (gaps.length) return notConfigured(...gaps);
  const site = env.DD_SITE || 'us5.datadoghq.com';
  const monitors = await apiJson(`https://api.${site}/api/v1/monitor?page_size=100`, {
    headers: { 'DD-API-KEY': env.DD_API_KEY, 'DD-APPLICATION-KEY': env.DD_APP_KEY },
  });

  const counts = { Alert: 0, Warn: 0, 'No Data': 0, OK: 0, Other: 0 };
  const alerting = [];
  for (const m of monitors) {
    const state = m.overall_state || 'Other';
    if (counts[state] === undefined) counts.Other += 1;
    else counts[state] += 1;
    if (state === 'Alert' || state === 'Warn') {
      alerting.push({
        name: m.name || `Monitor ${m.id}`,
        status: state.toLowerCase(),
        state: state === 'Alert' ? 'down' : 'warn',
        url: `https://app.${site.replace('api.', '')}/monitors/${m.id}`,
      });
    }
  }

  const items = Object.entries(counts)
    .filter(([, n]) => n > 0)
    .map(([name, count]) => ({
      name,
      count,
      state: name === 'Alert' ? 'down' : (name === 'Warn' || name === 'No Data' ? 'warn' : 'up'),
    }));

  return {
    ok: counts.Alert === 0,
    state: counts.Alert > 0 ? 'down' : (counts.Warn > 0 ? 'warn' : 'up'),
    summary: `${monitors.length} monitors, ${counts.Alert} alerting, ${counts.Warn} warning`,
    items,
    alerting,
  };
}

/* ------------------------------------------------------------ orchestration */

let cache = { at: 0, payload: null };

async function buildStatus(env) {
  const names = ['endpoints', 'recall', 'board', 'coolify', 'github', 'vercel', 'sentry', 'pagerduty', 'datadog'];
  const results = await Promise.all([
    section(() => checkEndpoints()),
    section(() => checkRecall(env)),
    section(() => checkBoard(env)),
    section(() => checkCoolify(env)),
    section(() => checkGitHub(env)),
    section(() => checkVercel(env)),
    section(() => checkSentry(env)),
    section(() => checkPagerDuty(env)),
    section(() => checkDatadog(env)),
  ]);

  const sections = {};
  names.forEach((n, i) => { sections[n] = results[i]; });

  const states = Object.values(sections).map((s) => s.state);
  const overall = states.includes('down') ? 'down' : (states.includes('warn') ? 'warn' : 'up');

  return { checkedAt: new Date().toISOString(), overall, sections };
}

function jsonResponse(payload, status = 200) {
  return new Response(JSON.stringify(payload), {
    status,
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Cache-Control': 'no-store',
    },
  });
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    if (url.pathname === '/api/status') {
      const now = Date.now();
      if (cache.payload && now - cache.at < CACHE_TTL_MS) {
        return jsonResponse({ ...cache.payload, cached: true });
      }
      const payload = await buildStatus(env);
      cache = { at: now, payload };
      return jsonResponse({ ...payload, cached: false });
    }

    if (url.pathname === '/api/recall/search') {
      const q = (url.searchParams.get('q') || '').trim();
      if (!q) return jsonResponse({ ok: false, error: 'Add a query.', hits: [] }, 400);
      const gaps = missing(env, 'RECALL_API_TOKEN', 'CF_ACCESS_CLIENT_ID', 'CF_ACCESS_CLIENT_SECRET');
      if (gaps.length) {
        return jsonResponse({ ok: false, error: 'Not configured', hits: [] }, 503);
      }
      const limit = Math.min(Number(url.searchParams.get('limit') || 10) || 10, 25);
      try {
        const hits = await recallSearch(env, q, limit);
        return jsonResponse({ ok: true, query: q, hits });
      } catch (err) {
        return jsonResponse({ ok: false, error: errText(err), hits: [] }, 502);
      }
    }

    if (url.pathname.startsWith('/api/')) {
      return jsonResponse({ ok: false, error: 'No such route.' }, 404);
    }

    return env.ASSETS.fetch(request);
  },
};
