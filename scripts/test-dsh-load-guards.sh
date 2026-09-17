#!/bin/bash
# Contract: DSH web must not self-exec, must not kill a healthy :3080, and
# the Dock ping must outlast a slow loopback under CPU load.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
DSH="$ROOT/dsh-runtime/dsh.sh"
START="$ROOT/dsh-runtime/start-web.sh"
ENSURE="$ROOT/dsh-runtime/ensure-web.sh"
SWIFT="$ROOT/dsh-runtime/HarnessWindow.swift"

fail() { echo "FAIL $*" >&2; exit 1; }

[ -f "$DSH" ] || fail "missing $DSH"
[ -f "$START" ] || fail "missing $START"
[ -f "$ENSURE" ] || fail "missing $ENSURE"
[ -f "$SWIFT" ] || fail "missing $SWIFT"

if grep -nE 'exec[[:space:]]+.*/dsh-runtime/dsh\.sh' "$DSH"; then
  fail "dsh.sh must not exec itself"
fi
if ! grep -q 'node_modules/.bin/dsh' "$DSH"; then
  fail "dsh.sh must exec node_modules/.bin/dsh"
fi
if ! grep -q 'node_modules/.bin' "$DSH"; then
  fail "dsh.sh must refuse a bin path outside node_modules/.bin"
fi

if ! grep -q 'already healthy' "$START"; then
  fail "start-web.sh must skip reclaim when HTTP is healthy"
fi
if ! grep -q 'skip reclaim' "$START"; then
  fail "start-web.sh must log skip reclaim"
fi

if ! grep -q 'skip restart' "$ENSURE"; then
  fail "ensure-web.sh must skip pm2 restart when :3080 is listening"
fi
if grep -nE 'max-time 2' "$ENSURE"; then
  fail "ensure-web.sh curl timeout must not stay at 2s"
fi
if ! grep -q 'max-time 8' "$ENSURE"; then
  fail "ensure-web.sh curl timeout must be 8s"
fi

if ! grep -q 'timeoutInterval: 8' "$SWIFT"; then
  fail "HarnessWindow pingHarness timeout must be 8s"
fi
if grep -nE 'timeoutInterval: 2[^0-9]' "$SWIFT"; then
  fail "HarnessWindow pingHarness must not stay at 2s"
fi

echo "ok dsh-load-guards"
