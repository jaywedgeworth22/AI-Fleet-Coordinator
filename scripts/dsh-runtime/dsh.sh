#!/usr/bin/env bash
# Pinned Harness CLI.  Never npx.  Never exec this file.
#
# Tracked copy: AI-Fleet-Coordinator/scripts/dsh-runtime/dsh.sh
# Live install: ~/apps/dsh-runtime/dsh.sh
#
# 2026-09-16: a PATH wrapper that execs this script was copied *into* this
# script.  bash then exec'd itself until the CPU pegged and nothing bound
# :3080 (Harness "Load failed" on every thread).  Refuse that loop.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
BIN="$ROOT/node_modules/.bin/dsh"

if [[ ! -x "$BIN" ]]; then
  echo "dsh-runtime: missing $BIN — run npm ci in $ROOT (never npx)" >&2
  exit 127
fi

bin_dir="$(cd "$(dirname "$BIN")" && pwd)"
case "$bin_dir" in
  */node_modules/.bin) ;;
  *)
    echo "dsh-runtime: $BIN is not under node_modules/.bin — refuse self-exec" >&2
    exit 127
    ;;
esac

exec "$BIN" "$@"
