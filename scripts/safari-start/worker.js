// start.jays.services Worker: serve the static Safari start page and proxy search
// autocomplete at /suggest.  The upstream (Google Suggest) sends no CORS headers, so
// the browser cannot call it directly; this proxy adds permissive CORS so the page
// works from the deployed site, the file:// Mac install, and the jays.services/start/
// copy alike.  Everything else falls through to the static assets.

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, OPTIONS",
  "Access-Control-Allow-Headers": "*",
};

function json(obj) {
  return new Response(JSON.stringify(obj), {
    headers: { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "public, max-age=300", ...CORS },
  });
}

async function suggest(url) {
  const q = (url.searchParams.get("q") || "").slice(0, 200).trim();
  if (!q) return json({ q: "", suggestions: [] });
  const upstream = "https://suggestqueries.google.com/complete/search?client=firefox&hl=en&q=" + encodeURIComponent(q);
  try {
    const r = await fetch(upstream, {
      headers: { "User-Agent": "Mozilla/5.0", "Accept": "application/json, text/javascript, */*" },
      cf: { cacheTtl: 300, cacheEverything: true },
    });
    if (!r.ok) return json({ q, suggestions: [] });
    // Google returns ["query", ["s1", "s2", ...], ...] as text/javascript.
    const data = JSON.parse(await r.text());
    const suggestions = Array.isArray(data) && Array.isArray(data[1])
      ? data[1].filter(x => typeof x === "string").slice(0, 10)
      : [];
    return json({ q, suggestions });
  } catch (e) {
    return json({ q, suggestions: [] });
  }
}

export default {
  async fetch(request, env) {
    if (request.method === "OPTIONS") return new Response(null, { headers: CORS });
    const url = new URL(request.url);
    if (url.pathname === "/suggest") return suggest(url);
    return env.ASSETS.fetch(request);
  },
};
