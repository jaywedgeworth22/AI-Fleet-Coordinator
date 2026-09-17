# 2026-09-17 — Onboarding prompt for INSTINCT, the iMessage interface seat

PR #251.  Branch `claude/instinct-imessage-onboarding-n6u9oh` (Claude Code cloud, seat CLAUDE).

## Context

The owner asked what instructions to give a new iMessage-based interface agent called Instinct so it
knows how to interact with the team.  The fleet already has a paste-ready prompt pattern
(`docs/FX-ONBOARDING-PROMPT.md`, `docs/CODEX-FLEET-RAG-PROMPT.md`) and a standing seat procedure
(`docs/ONBOARDING-NEW-AGENT.md`), so the answer is a third prompt doc on that pattern rather than a
one-off join.

## What changed

- `docs/INSTINCT-ONBOARDING-PROMPT.md` (new).  Owner-facing preamble (assumed defaults, what Instinct
  needs before its first session), the prompt itself, the Agent Seat row text, a "how to tell it
  took" list, and the existing iMessage jobs the prompt builds on.
- `STATUS.md` and `docs/EFFORT-LOG.md` rows for this unit.
- Follow-up section for a browser-only runtime (added the same day after Instinct reported a form-only vault and no MCP client): board by browser session and by GitHub issue, no Slack write until a Mac-side bridge exists, no recall or seat-mcp, revised first unit.  Facts checked in `scripts/mac-collab/mac-collab-server.py`, `scripts/mac-collab/sync_board.py`, and `scripts/agent-sync-push/daemon.js`.

## Decisions

- Instinct is an **interface seat**: it files, wakes, drives (seat-mcp), and reports; it owns no
  coding lane unless the owner assigns one.  So no `fleet-apps.json` entry yet (that file drives
  worktrees, branch prefixes, and the digest legend).
- Tag `INSTINCT` by default; `BF-INSTINCT` if it runs as a BotFleet bot.  Everything else holds.
- Transport is bound by `AGENT-SYNC.md` § Process 10: send only from the `agents` macOS account
  through the one authorized listener and sender; never a second `chat.db` reader or a sender
  under `jay` (the 2026-09-02 echo loop is the precedent).  The prompt tells Instinct to file a
  board item and stop if it needs more; only the owner amends Process 10.
- New Slack body field `owner-relay:` for verbatim owner quotes with a Central Time stamp, so peers
  can tell relayed owner words from Instinct's own inference.  Documented in the seat row.
- The owner's phone gets watcher noise discipline: forward Slack only on a tag / app / `->FLEET` /
  HALT match.

## Verification

- Sentence-gap check on the new doc: no single-space sentence boundaries.
- `python3 scripts/check-fleet-registry.py` (no registry file changed).

## Not done here

- Board item and Slack claim: this sandbox has no `MAC_COLLAB_TOKEN` and its `SLACK_BOT_TOKEN`
  returns `invalid_auth`.  A Mac seat files the board item when the owner confirms the tag.
- Seat row not landed in `AGENT-SYNC.md` (either copy) until the owner confirms the tag; the row
  text is in the doc.
