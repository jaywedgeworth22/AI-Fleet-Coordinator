/**
 * Fleet Mac always-on jobs.  Source of truth for `pm2 start` / `pm2 save`.
 *
 *   pm2 start /Users/jay/apps/pm2-ecosystem.config.cjs --only <name>
 * grok-leader must stay up for Shellular Grok / new TUI session sharing.
 *   pm2 save
 *   bash ~/apps/mac-status.sh
 *
 * Do not start vendor jobs here (GitHub runners, Homebrew moshi-hook,
 * system cloudflared).  Do not start scheduled fire-and-exit jobs here
 * (watchdog, janitor, collector) — those stay launchd StartInterval.
 *
 * Deprecated / removed from this ecosystem (do not resurrect): scout,
 * residential-proxy, senate-relay, senate-tunnel.  Senate/residential stay
 * off this Mac; Coolify/Texas paths own them.
 */
const home = "/Users/jay";
const logs = `${home}/.pm2/logs`;
const path =
  "/Users/jay/.grok/bin:/opt/homebrew/bin:/usr/local/bin:/Users/jay/.local/bin:/usr/sbin:/sbin:/usr/bin:/bin";

function app(partial) {
  return {
    autorestart: true,
    max_restarts: 30,
    min_uptime: "10s",
    watch: false,
    merge_logs: true,
    time: true,
    env: {
      PATH: path,
      HOME: home,
      DD_AGENT_HOST: "127.0.0.1",
      DD_TRACE_AGENT_PORT: "8126",
      DD_ENV: "prod",
      DD_SITE: "us5.datadoghq.com",
      ...(partial.env || {})
    },
    ...partial,
  };
}

module.exports = {
  apps: [
    app({
      name: "shellular",
      script: `${home}/apps/shellular-runtime/node_modules/shellular/dist/main.js`,
      args: "__daemon --server https://server.shellular.dev --dir /Users/jay --unknown-clients always-allow",
      cwd: home,
      interpreter: "node",
      out_file: `${logs}/shellular-out.log`,
      error_file: `${logs}/shellular-error.log`,
    }),
    app({
      name: "agent-sync-push",
      script: `${home}/apps/agent-sync-push/start.sh`,
      interpreter: "bash",
      cwd: `${home}/Code/Congress.Trade`,
      out_file: `${logs}/agent-sync-push-out.log`,
      error_file: `${logs}/agent-sync-push-error.log`,
    }),
    app({
      name: "code-main-keeper",
      script: `${home}/apps/code-main-keeper-daemon.sh`,
      interpreter: "bash",
      cwd: `${home}/apps`,
      out_file: `${home}/apps/logs/code-main-keeper.pm2.out.log`,
      error_file: `${home}/apps/logs/code-main-keeper.pm2.err.log`,
    }),
    app({
      name: "vision-worker",
      script: `${home}/vision-worker/run-vision-worker.sh`,
      interpreter: "bash",
      cwd: `${home}/vision-worker`,
      out_file: `${logs}/vision-worker-out.log`,
      error_file: `${logs}/vision-worker-error.log`,
    }),
    app({
      name: "xcode-health",
      script: `${home}/apps/xcode-health/xcode-health-server.py`,
      interpreter: "/usr/bin/python3",
      cwd: `${home}/apps/xcode-health`,
      out_file: `${logs}/xcode-health-out.log`,
      error_file: `${logs}/xcode-health-error.log`,
    }),
    app({
      name: "mac-collab",
      script: `${home}/apps/mac-collab/mac-collab-server.py`,
      interpreter: "/usr/bin/python3",
      cwd: `${home}/apps/mac-collab`,
      out_file: `${logs}/mac-collab-out.log`,
      error_file: `${logs}/mac-collab-error.log`,
    }),
    app({
      name: "mac-collab-sync",
      script: `${home}/apps/mac-collab/sync_board.py`,
      args: "--loop",
      interpreter: "/usr/bin/python3",
      interpreter_args: "-u",
      cwd: `${home}/apps/mac-collab`,
      out_file: `${logs}/mac-collab-sync-out.log`,
      error_file: `${logs}/mac-collab-sync-error.log`,
    }),
    app({
      name: "mac-collab-writeback",
      script: `${home}/apps/mac-collab/write_back.py`,
      args: "--loop",
      interpreter: "/usr/bin/python3",
      interpreter_args: "-u",
      cwd: `${home}/apps/mac-collab`,
      out_file: `${logs}/mac-collab-writeback-out.log`,
      error_file: `${logs}/mac-collab-writeback-error.log`,
    }),
    app({
      name: "cursor-slack-sync",
      script: `${home}/apps/cursor-slack-ws-sync.py`,
      interpreter: "/opt/homebrew/bin/python3",
      cwd: `${home}/apps`,
      out_file: `${logs}/cursor-slack-sync-out.log`,
      error_file: `${logs}/cursor-slack-sync-error.log`,
    }),
    app({
      name: "agy-acp",
      script: `${home}/apps/agy-acp-runtime/start.sh`,
      interpreter: "bash",
      cwd: `${home}/apps/agy-acp-runtime`,
      env: { AGY_ACP_BIND: "127.0.0.1", AGY_ACP_PORT: "8765" },
      out_file: `${logs}/agy-acp-out.log`,
      error_file: `${logs}/agy-acp-error.log`,
    }),
    app({
      name: "grok-leader",
      script: `${home}/apps/grok-acp-runtime/leader.sh`,
      interpreter: "bash",
      cwd: `${home}/apps/grok-acp-runtime`,
      // 75 = lock already held (leader.sh).  Stop instead of restart-storm.
      stop_exit_codes: [75],
      exp_backoff_restart_delay: 4000,
      max_restarts: 8,
      out_file: `${logs}/grok-leader-out.log`,
      error_file: `${logs}/grok-leader-error.log`,
    }),
    app({
      name: "grok-acp",
      script: `${home}/apps/grok-acp-runtime/start.sh`,
      interpreter: "bash",
      cwd: `${home}/apps/grok-acp-runtime`,
      out_file: `${logs}/grok-acp-out.log`,
      error_file: `${logs}/grok-acp-error.log`,
    }),
    app({
      name: "dsh-web",
      script: `${home}/apps/dsh-runtime/start-web.sh`,
      interpreter: "bash",
      cwd: `${home}/apps/dsh-runtime`,
      // 3 = :3080 held by a non-dsh process (start-web.sh).  Do not storm.
      stop_exit_codes: [3],
      env: { DSH_HOME: `${home}/.dsh`, DSH_WEB_HOST: "127.0.0.1", DSH_WEB_PORT: "3080" },
      out_file: `${logs}/dsh-web-out.log`,
      error_file: `${logs}/dsh-web-error.log`,
    }),
    app({
      name: "seat-mcp",
      script: `${home}/apps/seat-mcp/start.sh`,
      interpreter: "bash",
      cwd: `${home}/apps/seat-mcp`,
      out_file: `${logs}/seat-mcp-out.log`,
      error_file: `${logs}/seat-mcp-error.log`,
    }),
    app({
      name: "mac-collab-litestream",
      script: `${home}/apps/mac-collab/start_litestream.sh`,
      interpreter: "bash",
      cwd: `${home}/apps/mac-collab`,
      out_file: `${logs}/mac-collab-litestream-out.log`,
      error_file: `${logs}/mac-collab-litestream-error.log`,
    }),
  ],
};
