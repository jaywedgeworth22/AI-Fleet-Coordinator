---
name: session-start
description: >-
  Start every Grok session on this Mac — poll Slack, read THE BOARD, pin AGENT_SEAT=GROK, pick the seat worktree, then triple-claim before editing. Use at session start, after a resume, when switching apps, or whenever you are about to begin substantial work. Grok (not another seat) — never skip this for "just a small fix."
---

# Session start (GROK)

> **This install is for `GROK`.** Slack `[GROK]`.  Notes `Grok`.  Branches `grok/`.  Worktrees `~/apps/<app>-grok`.  Do not inherit another seat's tag from a shared template.

> **Runtime fork (Grok).** Mac Grok TUI / CLI is `[GROK]`.  If this session is **Grok Build**, pin `AGENT_SEAT=GROK-BUILD`, tag `[GROK-BUILD]`, branches `grok-build/`, worktrees `~/apps/<app>-grok-build`.  Grok Bot (Cursor cloud) uses `[GB-<NAME>]` role tags, not this pack and not `[GROK-BOT]`.  Never `[MONET]`.


This pack is for the **GROK** Mac TUI / CLI seat.  Tag `[GROK]`.  Notes name `Grok`.  Branches `grok/<slug>` only.  Worktrees `~/apps/<prefix>-grok`.  Never sign as Monet or Grok Bot.  Pin `AGENT_SEAT=GROK`.

## 1. Identity

```bash
export AGENT_SEAT=GROK
export AGENT_TAG=GROK
```

Never open or push another seat's prefix from a Grok session.  Only `grok/`.

## 2. Read live coordination

```bash
AGENT_TAG=GROK /usr/bin/python3 /Users/jay/apps/agent-sync-poll.py
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

| App | Slack `repo:` | Acronym | Grok worktree | Live board |
|-----|---------------|---------|----------------|------------|
| Socratic.Trade | `Socratic.Trade` | ST | `~/apps/trading-grok` | `~/apps/TRADING-EFFORT-LOG.md` |
| Congress.Trade | `Congress.Trade` | CT | `~/apps/congress-grok` | `~/apps/CONGRESS-TRADE-EFFORT-LOG.md` |
| Usage Monitor | `API-usage-monitor` | UM | `~/apps/usage-grok` | `~/apps/API-USAGE-MONITOR-EFFORT-LOG.md` |
| congress-trading-shared | `congress-trading-shared` | CTS | `~/apps/cts-grok` | `~/apps/CONGRESS-SHARED-EFFORT-LOG.md` |
| DealDex | `DealDex` | DD | `~/apps/dealdex-grok` | `~/apps/DEALDEX-EFFORT-LOG.md` |
| Personal-Site | `Personal-Site` | PS | `~/apps/personal-grok` | `~/apps/PERSONAL-SITE-EFFORT-LOG.md` |
| AI-Fleet-Coordinator / machine infra | `AI-Fleet-Coordinator` or `fleet-infra` | AFC | `~/apps/fleet-grok` (or a `~/apps/fleet-grok-<lane>` worktree) | `~/apps/FLEET-INFRA-EFFORT-LOG.md` |

As of 2026-08-20 only `~/apps/trading-grok` is guaranteed to exist.  Create a missing standing lane before editing:

```bash
git -C /Users/jay/Code/<Repo> worktree add -b grok/<slug> ~/apps/<prefix>-grok
```

Per-lane isolation is also fine: `~/apps/<prefix>-grok-<lane>`.  Inventory is `~/Code/AI-Fleet-Coordinator/fleet-apps.json`.  `scripts/setup-agent-lanes.sh` uses a different naming scheme (`Socratic.Trade-monet` / `agent/monet`) — do not run it for this seat.

Then read that app's `AGENTS.md`, `STATUS.md`, latest `docs/rollouts/`, and `docs/EFFORT-LOG.md`.  Personal-Site `AGENTS.md` can lag `README.md` (the live source is `site/`); believe README + current tree over a stale "static snapshot" paragraph.

## 4. Triple-claim before substantial edits

1. **THE BOARD** — `board list --app <app>` then `board claim <id> --by GROK --env Mac --where "~/apps/<lane> @ grok/<slug>"`.  If nothing exists: `board file --title "..." --app <app> --severity P1 --by GROK --env Mac --where "..." --desc "..."`.
2. **Effort board** — In Progress on the live file **and** `docs/EFFORT-LOG.md` (fleet-infra has no repo mirror).  Never delete another seat's row.
3. **Slack** — then GitHub issue if you are executing a numbered one.

Post (prefer this over Slack MCP):

```bash
AGENT_TAG=GROK /Users/jay/apps/agent-sync-websocket.py --post "[GROK] sync-1
repo: <project>
claim: grok/<slug>
state: WIP
cadence: per-turn-poll
work: <one line>"
```

Fallback: `SLACK_AGENT_NAME=GROK bash scripts/slack-sync.sh post "..."` from the app checkout, or `/Users/jay/apps/slack-sync.sh`.  Do not open a second Slack Socket Mode connection.

`FLEET` as recipient only when every listening seat on every platform must spend time.  This coordinator signs as `AFC`.

## 5. Prior messages stay in scope

A new owner message **adds** work unless they explicitly cancel or replace the objective.  Keep unfinished items on a todo list.

## 6. Do not

- Kill `com.jay.claude-remote-control` because `ps` shows `claude` with no TTY.  Monet, Renoir, and Claude Code all look like `claude`.  That job is KeepAlive phone / claude.ai steering.
- Self-filter Slack on `[GROK` when you run parallel Grok lanes — sibling posts are for you too.
- Start in `~/Code/Personal-Site` or any other integration tree.
- Skip THE BOARD.  It is the write surface; `mac-collab-writeback` copies status to live effort logs and GitHub Issues.  Still land `docs/EFFORT-LOG.md` in the app PR when you touch that repo.

## Canon

- `/Users/jay/apps/AGENT-SYNC.md` — identity, THE BOARD, Slack, prior-messages, always-commit
- `/Users/jay/apps/EFFORT-LOG-PROTOCOL.md`
- `/Users/jay/Code/AI-Fleet-Coordinator/docs/ONBOARDING-NEW-AGENT.md`
- `/Users/jay/Code/AI-Fleet-Coordinator/fleet-apps.json`
- Skills in this pack: `board-ops`, `closeout`, `secret-handoff`, `land-lane`
