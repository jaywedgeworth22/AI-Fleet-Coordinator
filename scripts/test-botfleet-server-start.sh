#!/bin/bash
# Contract: start wrapper exits 0 when :8799 is healthy, 1 when deps missing.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
WRAP="${ROOT}/botfleet-server-start.sh"
[ -f "$WRAP" ] || { echo "missing $WRAP" >&2; exit 1; }

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

python3 - "$WRAP" "$tmp" <<'PY'
import pathlib, sys
src = pathlib.Path(sys.argv[1]).read_text()
root = pathlib.Path(sys.argv[2])
src = src.replace("/usr/bin/curl", str(root / "curl"))
(root / "wrap.sh").write_text(src)
PY
chmod +x "${tmp}/wrap.sh"

# healthy port -> exit 0 even with no checkout
cat >"${tmp}/curl" <<'EOS'
#!/bin/bash
exit 0
EOS
chmod +x "${tmp}/curl"
if ! BOTFLEET_SERVER_ROOT="${tmp}/no-such" bash "${tmp}/wrap.sh" >"${tmp}/out" 2>"${tmp}/err"; then
  echo "FAIL expected exit 0 on healthy harness" >&2
  cat "${tmp}/err" >&2
  exit 1
fi
grep -q "already healthy" "${tmp}/out" || { echo "FAIL missing already-healthy log" >&2; exit 1; }

# The probe must hit /api/health: BotFleet has no /health route (it 404s), so a
# stub that only succeeds for /api/health proves the wrapper asks the real one.
cat >"${tmp}/curl" <<'EOS'
#!/bin/bash
case "$*" in
  *"/api/health"*) exit 0 ;;
  *) exit 22 ;;
esac
EOS
chmod +x "${tmp}/curl"
if ! BOTFLEET_SERVER_ROOT="${tmp}/no-such" bash "${tmp}/wrap.sh" >"${tmp}/out3" 2>"${tmp}/err3"; then
  echo "FAIL wrapper must probe /api/health, not /health" >&2
  cat "${tmp}/err3" >&2
  exit 1
fi
grep -q "already healthy" "${tmp}/out3" || { echo "FAIL /api/health probe: missing already-healthy log" >&2; exit 1; }

# unhealthy + missing node_modules -> exit 1
cat >"${tmp}/curl" <<'EOS'
#!/bin/bash
exit 22
EOS
chmod +x "${tmp}/curl"
if BOTFLEET_SERVER_ROOT="${tmp}/empty-root" bash "${tmp}/wrap.sh" >"${tmp}/out2" 2>"${tmp}/err2"; then
  echo "FAIL expected exit 1 when node_modules missing" >&2
  exit 1
fi
grep -q "missing" "${tmp}/err2" || { echo "FAIL missing node_modules message" >&2; cat "${tmp}/err2" >&2; exit 1; }

echo OK
