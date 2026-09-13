# Status

Updated: 2026-09-13 (FX — register FX seat and HogHunter)

## 2026-09-13 FX — FX seat + HogHunter in fleet-apps.json

`fleet-apps.json` now lists seat FX (`fx/`, `~/apps/<prefix>-fx`) and app HogHunter (`HH`, local-only).  KIMI is marked retired.  Agent Seat table and Available (normal) list include FX in both AGENT-SYNC copies.  Board `22164b50`.  Branch `fx/registry-fx-hoghunter`.  Rollout: `docs/rollouts/2026-09-13-fx-seat-and-hoghunter.md`.

Updated: 2026-09-04 (GROK — MiniMax Slack tag MM; DeepSeek Harness DSH)

## 2026-09-04 GROK — seat acronyms MM and DSH

Owner: MiniMax acronym is `MM` anywhere acronyms are used (Slack `[MM]`).  DeepSeek
Harness is `DSH` (Slack `[DSH]`).  Former tags `MINIMAX` and `DEEPSEEK` (harness) are
retired.  A DeepSeek *model* inside Cursor stays `[CURSOR]`.  Branch prefixes stay
`minimax/` and `deepseek/`.  Board `f9df420d`.  Branch `grok/mm-dsh-acronyms`.
Rollout: `docs/rollouts/2026-09-04-mm-dsh-seat-acronyms.md`.

Updated: 2026-09-04 (GROK — Sentry max-features fleet matrix)

## 2026-09-04 GROK — Sentry max features

Inventory + remaining SDK signals across apps that have a Sentry project.
Designer rulings UPDATE: Personal-Site / CTS / fleet-ops omit Sentry
(approved); ST/CT web Replay error 100% / session 10%; Seer Autofix
ENABLE BotFleet only; Android ENABLE on DD/AR/CL.  Canonical matrix:
`docs/rollouts/2026-09-04-sentry-max-features.md`.  Board `af1ab6e9`.
Branch `grok/sentry-max-features-fleet`.  App PRs on
`grok/sentry-max-features` (ST follow-up `grok/sentry-max-replay-10`).
No Coolify / merge / extra-ship.

Updated: 2026-09-03 (GROK — iOS version manifest home)

## 2026-09-03 GROK — iOS versions.json lives here, not ios-app-versions

Owner is deleting `jaywedgeworth22/ios-app-versions`.  Personal-Site does not
link it.  Canonical public file is `site/ios-versions.json`.  iOS clients fetch
https://raw.githubusercontent.com/jaywedgeworth22/ai-fleet-coordinator/main/site/ios-versions.json
Board `ca104839`.  Branch `grok/ios-versions-home`.  Rollout:
`docs/rollouts/2026-09-03-ios-versions-home.md`.

Updated: 2026-09-03 (BF-DIRECTOR — copy: Title Case chrome; never display &nbsp; in cloud text)

## 2026-09-03 BF-DIRECTOR — owner copy strengthening

Owner: Title Case for buttons/headings/titles everywhere (including Bot settings and routine settings).  Sentence case for body; lowercase when not a full sentence.  Two spaces between sentences.  Never display the six characters `&nbsp;` in cloud/owner-visible text; backend may insert U+00A0.  Board `09e01a3c`.  Branch `grok/copy-cloud-nbsp`.  ContactLogo.com punch list `62acf520` routed to Designer.  No TestFlight.

Updated: 2026-09-02 (GROK — RAG adoption: search at start, contribute at closeout)

## 2026-09-02 GROK — RAG adoption all platforms

session-start 2b + closeout contribute wired; skills installed to Claude/Cursor/Codex/Grok/AG/FX/DeepSeek/Monet homes.  Cloud hop already lists `/recall/*`.  Product AGENTS.md still missing the stanza (`docs/AGENTS-RECALL-SNIPPET.md`).  Board `03ee6d8b`.  Branch `grok/rag-adopt`.

Updated: 2026-09-02 (GROK — RAG write path: contribute lessons, not chat dumps)

## 2026-09-02 GROK — RAG memory policy

Owner: `recall_contribute` is the highest-yield write; chat mining is a rare infra/policy scan.
`ingest --all` skips `chat-log`.  Branch `grok/rag-memory-policy`.  Do not ingest the ~50k
staged session JSONL dumps.  Rollout: `docs/rollouts/2026-09-02-rag-contribute-not-chat-dump.md`.

Updated: 2026-09-02 (GROK — idle unload 12h)

## 2026-09-02 GROK — idle MCP unload 36h → 12h

Same `session/close` path as #171.  Default 12 hours.  Transcripts stay; `/resume` reloads tools.  `GROK_IDLE_UNLOAD_HOURS` in the LaunchAgent for shorter trials.  Board `09102247`.  Branch `grok/idle-unload-12h`.

Updated: 2026-09-01 (GROK — idle Grok MCP unload + Hetzner swap)

## 2026-09-01 GROK — unload Grok MCP on chats idle >36h; 16GiB Hetzner swap

Live TUI chats each held a full MCP set (~2.6 GB for 10 live).  Hourly `com.jay.grok-idle-unload` calls ACP `session/close` on live idle chats older than 36h.  Transcripts stay on disk; `/resume` reloads tools.  Skips working / needs-input / this TUI.  Hetzner `/swapfile.extra` brings swap 4GiB → 16GiB for container RAM caps 40–50% above the 30GiB box; `vm.swappiness=20` so swap is overflow, not cache steal.  Board `8247aa02`.  Branch `grok/idle-chat-unload`.

Updated: 2026-09-01 (GROK — mine chat logs + extra markdown into fleet-agents)

## 2026-09-01 GROK — mine chats + extra markdown (fleet-agents)

Team of Grok agents mined Claude/Grok/Cursor/Codex/Gemini/Kimi/BotFleet chats and extra markdown into scrubbed JSONL at `~/apps/fleet-rag/mined/` (75k lines, not git).  Code: `chat-log` source + expanded `doc` walker on `grok/rag-mine-chats-docs`, AFC #170.  Board `ef4df7cb`.  Do not start a second ingest while pid 81666 holds the lock.  Rollout: `docs/rollouts/2026-09-01-rag-mine-chats-docs.md`.

Updated: 2026-09-01 (GROK — Sentry org extras)

## 2026-09-01 GROK — Sentry org extras (sponsored account)

Live org config: detector-scoped PagerDuty `3930764`, Slack `3930668` + Seer
triggers, cron Slack `3932162`, remaining uptime, Fleet production dashboard
`9917821`, metric spikes `9700541`–`9700546`, CT PDF inbound filter, labeled
PD test page #86 resolved.  Rollout:
`docs/rollouts/2026-09-01-sentry-org-rollout.md`.  Board `31bd2e3a`.  Branch
`grok/sentry-org-rollout`.  SDK leftovers (UM sentry-ci-report, CT iOS Cocoa,
DSN hygiene, dSYM) stay other lanes.

Updated: 2026-09-01 (GROK pickup — fleet RAG operational, `claude/fleet-rag-operational`)

## 2026-09-01 GROK pickup — fleet RAG operational (Claude cap)

Adopted Claude's uncommitted recall CLI + ingest + MCP + seat-mcp tools + `fleet-recall` skill pack on `claude/fleet-rag-operational` (worktree `~/apps/fleet-claude-rag`).  Boards `c799b564` / `9c75471c` / `0f9a13b1`.  Installer registers MCP configs and puts `recall` on PATH like `board`.  First full ingest and Oracle routines are operational follow-through after the code lands.  Do **not** restart `qdrant-st` during RTH.  Slack `#agent-sync` skipped (`account_inactive`).  Co-authored with Claude.

Updated: 2026-09-01 (GROK — Sentry fleet adoption standing split)

## 2026-09-01 GROK — Sentry fleet adoption (standing split)

Implementation of the 2026-09-01 adoption report as fleet docs + CI/ship
hygiene, not another plan.  Canonical plan remains
`docs/plans/2026-09-01-sentry-fleet-integration.md` (AFC #158).  Rollout:
`docs/rollouts/2026-09-01-sentry-fleet-adoption.md`.  Binding: Personal-Site
stays Datadog-only (no Sentry project); CTS and fleet-ops have no project;
Android SDK waits until those tracks ship; Seer only on ST + CT after
contributor billing is Jay's GitHub user only; CI fingerprints `[app,
workflow]` only; Size Analysis TODO on `~/apps/ios-fleet/ship-testflight.sh`
(no new LaunchAgent).  Board `42c563a6`.  Branch `grok/sentry-fleet-adoption`.  Merged AFC #159.

Updated: 2026-09-01 (GROK — Sentry sponsored-account fleet integration plan)

## 2026-09-01 GROK — Sentry fleet integration plan

Plan-only inventory of org `jays-services` vs the sponsored product surface.  Canonical: `docs/plans/2026-09-01-sentry-fleet-integration.md`.  Board `6ac85c0e`.  Branch `grok/sentry-fleet-integration-plan`.  No SDK or alert changes in this unit.  Next: owner GitHub/Slack/PagerDuty integrations; unstick ST #3141/#3146 and CT #2282; first impl lane is UM scheduler cron + sentry-ci-report + one Slack alert.

Updated: 2026-08-30 (GROK — seat-mcp grok sessionId flush)

## 2026-08-30 GROK — seat-mcp grok sessionId flush + one-job queue

Jobs 401c53c0 / 15958b82 timed out 900s with sessionId none and bytesOut 0 because acp-client printed one JSON blob after `session/prompt` returned, `--timeout` was not on argv, and each RPC cancelled the WS pump.  NDJSON `event=session` flushes sessionId immediately.  One pump for the connection.  seat_status exposes sessionId, bytesOut, lastTool, gitMoved.  Second grok ACP job is rejected.  Board `51965c1b`.  Branch `grok/seat-flush`.  Do not extra-ship ST.  Do not start grok-leader.

Updated: 2026-08-30 (GROK — grok-acp auto-approve + ACP terminals)

## 2026-08-30 GROK — grok-acp auto-approve permissions and ACP terminals

Conductor github-only jobs hung after `git status` / `gh pr view`.  `session/request_permission` was unanswered or answered with a hardcoded `allow-always` that was not in the offered options, then `run_terminal_command` called `terminal/create` and the client replied `{}` (`failed to deserialize response`).  `acp-client.py` now picks an offered allow option, implements `terminal/*`, and returns `-32601` for unknown server methods.  acp-home `[ui] permission_mode = always-approve`.  Board `e1dc9024`.  Branch `grok/acp-auto-approve`.  Did not rebase ST #3120.  Did not restart grok-leader.

Updated: 2026-08-27 (GROK — TUI drive follow-ups + cloud hop)

## 2026-08-27 GROK — TUI drive follow-ups + cloud hop

Six leftovers from #137 plus cloud agents → `https://agents.jays.services/mcp` → Mac TUI.  Install-on-merge script, await-next-turn, pendingTool, self-guard, tracked stdio launchers.  Board `56cc91fd`.  Branch `grok/tui-drive-cloudhop`.

Updated: 2026-08-27 (GROK — live TUI prompt returns queued)

## 2026-08-27 GROK — grok-drive prompt returns when queued

Monitor peek worked; prompt inject landed in the TUI (`__drive_retry_no_load__`) but grok-drive waited up to 180s for this turn to finish.  Default prompt now returns `queued: true` after resume+inject.  `--wait` keeps the old wait-for-reply behavior.

Updated: 2026-08-27 (GROK — live TUI drive uses resume, not load)

## 2026-08-27 GROK — live TUI drive: session/resume, not session/load

Grok Bot list worked; peek/prompt died on `session/load` (~45s) for the open TUI.  Prompt now `session/resume` + `session/prompt`.  Peek reads `summary.json`.  Board `d854b8b4` follow-up.  Branch `grok/tui-drive-resume`.

Updated: 2026-08-27 (GROK — Grok Bot drive for live Grok TUI)

## 2026-08-27 GROK — Grok Bot drive for live Grok TUI sessions

Grok Bot attaches to live Mac Grok TUI chats via seat-mcp + the shared leader (`grok_sessions_list` / `grok_session_prompt`, CLI `grok-drive.py`).  New `:12419` sessions stay `seat=grok`.  Board `d854b8b4`.  Branch `grok/tui-drive`.  Owner leftover: Cursor cloud HTTP MCP env headers.

Updated: 2026-08-25 (CURSOR — agy-acp session/list wrapper)

## 2026-08-25 CURSOR — agy-acp session/list wrapper

Thin NDJSON proxy `scripts/agy-acp-runtime/agy-acp-list-wrapper` so Shellular custom `agy` advertises `sessionCapabilities.list` and answers `session/list` from Antigravity CLI files.  Child stays `agy-acp-turbo.sh`.  pm2 `:8765` / `start.sh` unchanged.  Branch `cursor/agy-acp-session-list-2365`.

Updated: 2026-08-25 (CURSOR — agy-acp fail-closed)

## 2026-08-25 CURSOR — harden pm2 agy-acp fail-closed

Tracked `agy-acp-turbo.sh` next to `start.sh`.  pm2 `:8765` now spawns the same turbo policy as Shellular.  Disconnect grace is 300s.  Loopback bind persists via `bind-loopback.cjs` (`node -r`), so `npm i` cannot restore `:::8765`.  Branch `cursor/agy-acp-fail-closed-387d`.

Updated: 2026-08-22 (CURSOR — agent config Google Drive mirror)

## 2026-08-22 CURSOR — mirror fleet agent skills to Google Drive

Google Drive desktop cannot sync `~/.Gemini` / `~/.cursor` / `~/.claude` / `~/.grok`
natively.  Added `scripts/sync-fleet-agent-config-to-gdrive.py` and extended the daily
`com.jay.fleet-gdrive-backup` runner to refresh `My Drive/fleet-agent-config/` and
`My Drive/fleet-skills/`.  Live copy `~/apps/fleet-gdrive-backup/`.  Branch
`cursor/agent-config-gdrive-sync`.

Updated: 2026-08-22 (GROK — owner-facing times are Central Time)

## 2026-08-22 GROK — tell the owner times in Central, never UTC-only

Owner: always say Central Time when telling him a time.  AGENT-SYNC /
FLEET-UI-COPY / owner-copy / onboarding strengthened.  `00:00 UTC` is 7:00 PM
CT the previous calendar day in CDT.  Board `4289393c`.  Branch
`grok/owner-times-ct`.

Updated: 2026-08-22 (GROK — disk prune + Kimi salvage)

## 2026-08-22 GROK — Mac disk prune, Kimi salvage, janitor coverage

Owner: more disk, old worktrees any app, heavy Kimi prune, extract 1–2wk leftovers, Mac+Hetzner health.  Janitor now covers all fleet Code repos.  Salvage in `~/apps/KIMI-SALVAGE-2026-08-22/`.  ST #3044 kept open.  Board `a4417d6f`.  Branch `grok/disk-prune-kimi`.

Updated: 2026-08-22 (GROK — board.jays.services redirect)

## 2026-08-22 GROK — board.jays.services → /board

Cloudflare Single Redirect 302 + proxied `AAAA 100::`.  Canonical URL stays `https://mac.jays.services/board`.  Short link `https://board.jays.services`.  Board `b89c8330`.  Branch `grok/board-redirect`.

Updated: 2026-08-21 (GROK — iOS Debug vs TestFlight)

## 2026-08-21 GROK — iOS Debug vs TestFlight

Owner: do Xcode-console debug autonomously.  Helper `~/apps/ios-fleet/ios-debug.sh`.  Policy in AGENT-SYNC § iOS agent build loop.  Board `cbc1edeb`.  Branch `grok/ios-device-debug`.

Updated: 2026-08-21 (GROK — grok-leader lock-held restart storm)

## 2026-08-21 GROK — grok-leader lock-held restart storm

`ms` grok-leader `errored` 355 restarts: this TUI holds `~/.grok/leader.sock`.
Watch skip used bare `lsof`; launchd PATH omitted `/usr/sbin`.  Stopped the
job.  Watch + plist PATH + `leader.sh` exit 75.  ios-ship-now exit-1 is the
2026-08-13 login leftover.  Board `0095ae36`.  Branch `grok/leader-lock`.

Updated: 2026-08-21 (GROK — Mac + Hetzner recovery)

## 2026-08-21 GROK — Mac + Hetzner recovery

Watch: jlist-timeout dump-safe restore; HTTP /health bounce; Shellular ioreg/Connected.  Host: `fleet-health-recover@socratic-app` and `@usage-monitor` active; verify cron Pushover.  Branch `grok/mac-hetzner-recovery`.  Board `21c68868`.

Updated: 2026-08-21 (GROK — Apple Notes HTML sentence gap)

## 2026-08-21 GROK — Apple Notes HTML sentence gap

Notes.app collapses two ASCII spaces.  `--html` bodies must use `Sentence.&nbsp; Next`.  Helper converts leftover `.  ` / `!  ` / `?  ` (not inside code/pre).  Branch `grok/notes-html-nbsp`.

Updated: 2026-08-21 (GROK — Apple Notes section spacing)

## 2026-08-21 GROK — Apple Notes section spacing

Helper MD converter was dropping blank lines, so Coding notes looked packed.  Now emits `<div><br></div>` between sections and bullets.  Prefer `--html` with explicit spacers.  Live copy `~/apps/apple-notes-coding.sh`.  Branch `grok/notes-section-spacing`.

Live fleet-infra board: `~/apps/FLEET-INFRA-EFFORT-LOG.md`.  Repo mirror: `docs/EFFORT-LOG.md`.

## 2026-08-20 GROK — Monet Desktop fleet-skills pack

Rewrote `~/Desktop/fleet-skills` for the MONET Claude.app library and landed a
git copy at `docs/fleet-skills/`.  Five original skills are fleet-wide (current
Hetzner Coolify UUIDs, THE BOARD, secret grep trap).  Added session-start,
board-ops, closeout, secret-handoff, apple-notes, owner-copy, ios-ship.
Owner still uploads on the MONET login.  Board `f78464cb`.  Rollout:
`docs/rollouts/2026-08-20-monet-fleet-skills.md`.

## 2026-08-20 CURSOR — Cross-app coordination follow-ups (pointer)

Socratic.Trade audit #2802 follow-ups are in ST PR #2941, Congress.Trade #2064, Usage-Monitor #1245.  Pins still CTS v2.5.2.  Pin-check is fail-closed but not a required merge check.  DealDex stays protocol-only / Vercel.
