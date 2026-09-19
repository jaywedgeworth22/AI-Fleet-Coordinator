# dsh-runtime helpers (fallback copy)

Canonical scripts now live in `jaywedgeworth22/Harness`
(`~/Code/Harness/scripts/`, live `~/apps/harness-runtime/`).  This
directory is a fallback copy for seats that still have an AFC checkout
and no Harness clone.

pm2 `harness-web` runs `~/apps/harness-runtime/scripts/start-web.sh`.
Do not point new jobs at this folder.  Do not `npx @deepseek-ai/dsh`.

After a Harness change that touches a live-install script, copy it here
only if AFC still needs a tracked fallback; prefer a PR in Harness.
