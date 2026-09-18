#!/usr/bin/env bash
# Always-on DeepSeek Harness web UI.  Loopback only; Tailscale Serve
# publishes https://macbook.boa-roygbiv.ts.net:3080
# Tracked copy: ai-fleet-coordinator/scripts/dsh-runtime/start-web.sh
# Live install: ~/apps/dsh-runtime/start-web.sh
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
export DSH_HOME="${DSH_HOME:-$HOME/.dsh}"
HOST="${DSH_WEB_HOST:-127.0.0.1}"
PORT="${DSH_WEB_PORT:-3080}"

reclaim_dsh_port() {
  local holder cmd
  holder="$(/usr/sbin/lsof -nP -iTCP:"$PORT" -sTCP:LISTEN -t 2>/dev/null | head -1 || true)"
  [[ -n "$holder" ]] || return 0
  cmd="$(ps -o command= -p "$holder" 2>/dev/null || true)"
  case "$cmd" in
    *dsh*|*dsh-runtime*)
      if curl -sf -o /dev/null --max-time 8 "http://${HOST}:${PORT}/"; then
        echo "dsh-web: :$PORT already healthy (pid $holder), skip reclaim" >&2
        exit 0
      fi
      echo "dsh-web: reclaiming pid $holder on :$PORT" >&2
      kill -TERM "$holder" 2>/dev/null || true
      for _ in 1 2 3 4 5 6 7 8; do
        /usr/sbin/lsof -nP -iTCP:"$PORT" -sTCP:LISTEN >/dev/null 2>&1 || return 0
        sleep 0.5
      done
      kill -KILL "$holder" 2>/dev/null || true
      sleep 0.5
      ;;
    *)
      echo "dsh-web: :$PORT held by pid $holder ($cmd) — not dsh, exit 3" >&2
      exit 3
      ;;
  esac
}

reclaim_dsh_port

# Re-assert Tailscale Serve before exec so a reset serve config comes back
# when pm2 restarts this job.  Failure is non-fatal (web still binds loopback).
if [[ -x "$ROOT/serve-tailscale.sh" ]]; then
  "$ROOT/serve-tailscale.sh" || true
fi

exec "$ROOT/dsh.sh" web --no-open --host "$HOST" --port "$PORT" \
  --trusted-host "127.0.0.1" \
  --trusted-host "127.0.0.1:${PORT}" \
  --trusted-host "localhost" \
  --trusted-host "localhost:${PORT}" \
  --trusted-host "macbook.boa-roygbiv.ts.net" \
  --trusted-host "macbook.boa-roygbiv.ts.net:${PORT}" \
  --trusted-host "100.113.106.39" \
  --trusted-host "100.113.106.39:${PORT}"
