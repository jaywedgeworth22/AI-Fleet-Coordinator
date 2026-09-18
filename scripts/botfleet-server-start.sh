#!/bin/bash
# Launchd entry for com.jay.botfleet-server.
# Start the detached checkout harness, or exit 0 when 127.0.0.1:8799 is
# already healthy (usually /Applications/BotFleet.app).  KeepAlive uses
# SuccessfulExit=false so a clean "already up" does not restart-storm.
set -euo pipefail

ROOT="${BOTFLEET_SERVER_ROOT:-$HOME/apps/botfleet-server}"
PORT="${BOTFLEET_PORT:-8799}"
NODE="${BOTFLEET_NODE:-/opt/homebrew/bin/node}"
PREFIX="[botfleet-server-start]"

# BotFleet's only health route is /api/health (server/index.ts).  /health
# answers 404 "no route", which `curl -f` treats as unhealthy, so probing it made
# this "already up" branch dead and let a wrapper run while the packaged app held
# the port fall through to the node_modules check and exit 1 in a restart loop.
health() {
  /usr/bin/curl -sf -m 2 "http://127.0.0.1:${PORT}/api/health" >/dev/null 2>&1
}

if health; then
  echo "$PREFIX :${PORT} already healthy; not starting a second harness"
  exit 0
fi

if [ ! -d "$ROOT/node_modules" ]; then
  echo "$PREFIX missing $ROOT/node_modules" >&2
  echo "$PREFIX restore with: pnpm install --frozen-lockfile  (cwd $ROOT)" >&2
  exit 1
fi

if [ ! -f "$ROOT/server/index.ts" ]; then
  echo "$PREFIX missing $ROOT/server/index.ts" >&2
  exit 1
fi

if [ ! -x "$NODE" ]; then
  echo "$PREFIX missing node at $NODE" >&2
  exit 1
fi

cd "$ROOT"
exec "$NODE" --experimental-strip-types server/index.ts
