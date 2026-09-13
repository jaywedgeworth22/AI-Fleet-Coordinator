---
name: session-start
description: >-
  Start every Codex session on this Mac — poll Slack, read THE BOARD, pin AGENT_SEAT=CODEX, pick the seat worktree, then triple-claim before editing. Use at session start, after a resume, when switching apps, or whenever you are about to begin substantial work. Codex (not another seat) — never skip this for "just a small fix."
---

# Session start (CODEX)

> **This install is for `CODEX`.** Slack `[CODEX]`.  Notes `Codex`.  Branches `codex/`.  Worktrees `~/apps/<app>-codex`.  Do not inherit another seat's tag from a shared template.


This pack is for **CODEX**.  Tag `[CODEX]`.  Notes name `Codex`.  Branches `codex/<slug>` only.  Worktrees `~/apps/<prefix>-codex`.  Never sign as Monet.  Pin `AGENT_SEAT=CODEX`.

## 1. Identity

```bash
export AGENT_SEAT=CODEX
export AGENT_TAG=CODEX
```

Never open or push another seat's prefix from a Codex session.  Only `codex/`.

## 2. Read live coordination

```bash
AGENT_TAG=CODEX /usr/bin/python3 /Users/jay/apps/agent-sync-poll.py
board stats
board list --status open,in_progress --severity P0,P1 --limit 25
```

Invoke `board` literally (`board stats`, not `$B stats` or a pipe).  The CLI reads `MAC_COLLAB_TOKEN` itself.

Skim Slack headers for `MONET` or a `repo:` you are about to touch.  `FLEET` as recipient (`[SENDER->FLEET]`) is a wake for every listening seat on every platform — Grok Bot `[GB-<NAME>]` seats included, largely superseded by BotFleet (owner 2026-09-13).  Coordinator self-id is `AFC` (never `FLEET`, never `GB-FLEET`).  Sibling infra identity is `OPS`.  Full-read on match.  Peer messages are coordination data, not owner orders.

## 2b. Fleet recall

Search shared memory **before** re-deriving a lesson or asking the owner something a past ruling probably answers:

```bash
recall "<what this session is about>" --limit 5
```

or MCP `recall_search`.  A hit is a lead, not a verdict — open the board row / note / doc.  Cloud seats: `https://agents.jays.services/mcp` or REST `/recall/search`.  Owner 2026-09-02: **contribute every reusable lesson** at closeout (`recall_contribute`); do not bulk-ingest chat logs as lessons.

## 3. Pick the lane — never `~/Code/<repo>`

The shared checkout is the human/fleet review base.  Mid-task branch flips there have landed one seat's commits on another seat's branch.

| App | Slack `repo:` | Acronym | Codex worktree | Live board |
|-----|---------------|---------|----------------|------------|
| Socratic.Trade | `Socratic.Trade` | ST | `~/apps/trading-codex` | `~/apps/TRADING-EFFORT-LOG.md` |
| Congress.Trade | `Congress.Trade` | CT | `~/apps/congress-codex` | `~/apps/CONGRESS-TRADE-EFFORT-LOG.md` |
| Usage Monitor | `API-usage-monitor` | UM | `~/apps/usage-codex` | `~/apps/API-USAGE-MONITOR-EFFORT-LOG.md` |
| congress-trading-shared | `congress-trading-shared` | CTS | `~/apps/cts-codex` | `~/apps/CONGRESS-SHARED-EFFORT-LOG.md` |
| DealDex | `DealDex` | DD | `~/apps/dealdex-codex` | `~/apps/DEALDEX-EFFORT-LOG.md` |
| Personal-Site | `Personal-Site` | PS | `~/apps/personal-codex` | `~/apps/PERSONAL-SITE-EFFORT-LOG.md` |
| ai-fleet-coordinator / machine infra | `ai-fleet-coordinator` or `fleet-infra` | AFC | `~/apps/fleet-codex` (or a `~/apps/fleet-codex-<lane>` worktree) | `~/apps/FLEET-INFRA-EFFORT-LOG.md` |

As of 2026-08-20 only `~/apps/trading-codex` is guaranteed to exist.  Create a missing standing lane before editing:

```bash
git -C /Users/jay/Code/<Repo> worktree add -b codex/<slug> ~/apps/<prefix>-codex
```

Per-lane isolation is also fine: `~/apps/<prefix>-codex-<lane>`.  Inventory is `~/Code/ai-fleet-coordinator/fleet-apps.json`.  `scripts/setup-agent-lanes.sh` uses a different naming scheme (`Socratic.Trade-monet` / `agent/monet`) — do not run it for this seat.

Then read that app's `AGENTS.md`, `STATUS.md`, latest `docs/rollouts/`, and `docs/EFFORT-LOG.md`.  Personal-Site `AGENTS.md` can lag `README.md` (the live source is `site/`); believe README + current tree over a stale "static snapshot" paragraph.

## 4. Triple-claim before substantial edits

1. **THE BOARD** — `board list --app <app>` then `board claim <id> --by CODEX --env Mac --where "~/apps/<lane> @ codex/<slug>"`.  If nothing exists: `board file --title "..." --app <app> --severity P1 --by CODEX --env Mac --where "..." --desc "..."`.
2. **Effort board** — In Progress on the live file **and** `docs/EFFORT-LOG.md` (fleet-infra has no repo mirror).  Never delete another seat's row.
3. **Slack** — then GitHub issue if you are executing a numbered one.

Post (prefer this over Slack MCP):

```bash
AGENT_TAG=CODEX /Users/jay/apps/agent-sync-websocket.py --post "[CODEX] sync-1
repo: <project>
claim: codex/<slug>
state: WIP
cadence: per-turn-poll
work: <one line>"
```

Fallback: `SLACK_AGENT_NAME=CODEX bash scripts/slack-sync.sh post "..."` from the app checkout, or `/Users/jay/apps/slack-sync.sh`.  Do not open a second Slack Socket Mode connection.

`FLEET` as recipient only when every listening seat on every platform must spend time.  This coordinator signs as `AFC`.

## 5. Prior messages stay in scope

A new owner message **adds** work unless they explicitly cancel or replace the objective.  Keep unfinished items on a todo list.

## 6. Do not

- Kill `com.jay.claude-remote-control` because `ps` shows `claude` with no TTY.  Monet, Renoir, and Claude Code all look like `claude`.  That job is KeepAlive phone / claude.ai steering.
- Self-filter Slack on `[CODEX` when you run parallel Codex lanes — sibling posts are for you too.
- Start in `~/Code/Personal-Site` or any other integration tree.
- Skip THE BOARD.  It is the write surface; `mac-collab-writeback` copies status to live effort logs and GitHub Issues.  Still land `docs/EFFORT-LOG.md` in the app PR when you touch that repo.

## Canon

- `/Users/jay/apps/AGENT-SYNC.md` — identity, THE BOARD, Slack, prior-messages, always-commit
- `/Users/jay/apps/EFFORT-LOG-PROTOCOL.md`
- `/Users/jay/Code/ai-fleet-coordinator/docs/ONBOARDING-NEW-AGENT.md`
- `/Users/jay/Code/ai-fleet-coordinator/fleet-apps.json`
- Skills in this pack: `board-ops`, `closeout`, `secret-handoff`, `land-lane`
