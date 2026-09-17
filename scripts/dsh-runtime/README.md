# dsh-runtime helpers (tracked)

Copy into `~/apps/dsh-runtime/` after merge:

- `start-web.sh` — pm2 `dsh-web`, binds `127.0.0.1:3080`
- `serve-tailscale.sh` — Tailscale Serve HTTPS 3080 → loopback 3080
- `open-harness.sh` — activate the Dock app
- `ensure-web.sh` — start pm2 `dsh-web` if :3080 is down
- `HarnessWindow.swift` — WKWebView shell (Dock running-dot, second click focuses)
- `install-dock-app.sh` — build `~/Applications/Harness.app` + pin Dock
  (display name "Harness"; on-disk name is `Harness.app`; bundle id stays
  `com.jays.dsh-harness-web` so existing Dock pins and saved frames survive;
  upstream is still `@deepseek-ai/dsh` — `Harness` is our local label)
- `assets/harness-icon-1024.png` — full-bleed 1:1 square, sharp 90° corners

Idle cost of always-on `dsh-web`: ~12 MB RSS, 0% CPU.  Keep it running.

Live ACP bridge stays `../dsh-acp.py` + `../dsh-acp.sh`.  Do not `npx`.
