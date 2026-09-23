#!/bin/bash
# Contract: janitor must not treat "kimi" as a substring.  ST #3044
# (cursor/kimi-audit-def) is a Cursor salvage PR the owner kept.  Active
# nested worktrees must still go through the idle check (tested here via
# the classifier only — force_stale is gone).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
JANITOR="${ROOT}/disk-janitor.sh"

fail() { echo "FAIL $*" >&2; exit 1; }

[ -f "$JANITOR" ] || fail "missing $JANITOR"

# The dangerous #90 matcher must stay gone.
if grep -nE 'force_stale=\s*yes' "$JANITOR"; then
  fail "force_stale must not skip the idle check"
fi
if grep -nE '\*kimi\*' "$JANITOR"; then
  fail "substring *kimi* reaps cursor/kimi-audit-def"
fi

# shellcheck disable=SC1090
JANITOR_LIB_ONLY=1
# shellcheck source=disk-janitor.sh
source "$JANITOR"

assert_yes() {
  local wt="$1" br="$2"
  if ! janitor_is_retired_kimi_or_scratch "$wt" "$br"; then
    fail "expected scratch/kimi-seat: wt=$wt br=$br"
  fi
}

assert_no() {
  local wt="$1" br="$2"
  if janitor_is_retired_kimi_or_scratch "$wt" "$br"; then
    fail "expected keep (not kimi-seat/scratch): wt=$wt br=$br"
  fi
}

# ST #3044 — owner-kept salvage on a living Cursor lane.
assert_no "/Users/jay/apps/trading-cursor-kimi-audit" "cursor/kimi-audit-def"
assert_no "/Users/jay/apps/trading-cursor-kimi-audit-def" "refs/heads/cursor/kimi-audit-def"
assert_no "/Users/jay/apps/socratic-cursor-kimi-audit" "refs/heads/cursor/kimi-audit-def"

# Living-seat feature lanes that merely mention kimi in the slug.
assert_no "/Users/jay/apps/trading-grok-kimi-notes" "grok/kimi-retired-notice"
assert_no "/Users/jay/apps/fleet-claude-kimi-docs" "claude/kimi-docs"
assert_no "/Users/jay/apps/trading-grok-litestream-cascade" "grok/litestream-cascade-rag"
assert_no "/Users/jay/Code/Socratic.Trade" "main"
assert_no "/Users/jay/apps/trading-claude" "claude/feature"

# KEEP_RE must keep the always-on BotFleet harness checkout (reaping
# node_modules there crash-loops com.jay.botfleet-server).
if ! grep -q 'botfleet-server' "$JANITOR"; then
  fail "disk-janitor KEEP_RE must mention botfleet-server"
fi

# Retired KIMI seat (unsuffixed and per-lane).
assert_yes "/Users/jay/apps/trading-kimi" "kimi/leftover"
assert_yes "/Users/jay/apps/trading-kimi-onboard" "kimi/autorotate-onboard"
assert_yes "/Users/jay/apps/dealdex-kimi" "refs/heads/kimi/x"
assert_yes "/Users/jay/apps/fleet-kimi-halfdone" "KIMI/old"

# Nested agent scratch + tmp (idle check still applies in the janitor body).
assert_yes "/Users/jay/Code/Socratic.Trade/.claude/worktrees/abc" "agent/foo"
assert_yes "/Users/jay/Code/Socratic.Trade/.grok/worktrees/abc" "grok/foo"
assert_yes "/private/tmp/scratch-wt" "tmp/foo"
assert_yes "/tmp/scratch-wt" "tmp/foo"

# janitor_github_repo: squash-safe origin URL parsing (no network).
origin_repo_tmp=$(mktemp -d)
trap 'rm -rf "$origin_repo_tmp"' EXIT
git -C "$origin_repo_tmp" init -q
assert_origin() {
  local remote="$1" want="$2"
  git -C "$origin_repo_tmp" remote remove origin >/dev/null 2>&1 || true
  git -C "$origin_repo_tmp" remote add origin "$remote"
  local got
  got=$(janitor_github_repo "$origin_repo_tmp")
  [ "$got" = "$want" ] || fail "origin $remote -> '$got' want '$want'"
}
assert_origin "git@github.com:jaywedgeworth22/Socratic.Trade.git" "jaywedgeworth22/Socratic.Trade"
assert_origin "https://github.com/jaywedgeworth22/AI-Fleet-Coordinator.git" "jaywedgeworth22/AI-Fleet-Coordinator"
assert_origin "ssh://git@github.com/jaywedgeworth22/BotFleet.git" "jaywedgeworth22/BotFleet"

echo OK
