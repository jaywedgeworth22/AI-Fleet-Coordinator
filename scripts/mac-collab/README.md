# mac-collab (tracked copy)

Live process: `~/apps/mac-collab/` under pm2 `mac-collab` (HTTP), `mac-collab-sync`
(files+issues → board), and `mac-collab-writeback` (board writes → live effort logs
+ GitHub Issues).  This directory is the git copy.  Edit live, then copy here
before landing.

Do not serve `global-api-keys`. Names-only: `GET /files/key-names`.

THE BOARD (`/board`) sets an HttpOnly `mac_collab_session` cookie after a successful
Basic (or returning cookie) login so the owner is not asked for `MAC_COLLAB_TOKEN`
on every load.  Cookie max-age is 30 days.  JS `fetch` uses `credentials: include`
and only shows the in-page token bar on 401.  Agents still use Bearer.
`board show` / `board status` accept unique 8-char id prefixes.
`mac-collab-sync` snapshots `findings.db` under `~/apps/mac-collab/backups/` (14-day keep).
Writeback: `write_back.py --loop`.  Protocol: `docs/BOARD-WRITEBACK-PROTOCOL.md`.

## Tests

```bash
python3 scripts/mac-collab/test_bind_reclaim.py
python3 scripts/mac-collab/test_token_staleness.py
python3 scripts/mac-collab/test_write_back.py
```

`test_bind_reclaim.py` covers the 2026-08-20 EADDRINUSE outage path (stale
board server SIGTERM, SIGKILL fallback, refuse to kill a healthy sibling or
an unrelated process, lsof-timeout -> ps fallback).  Board `cd895d6f`.

## Token rotation (board `029f6346`)

`~/.secrets/mac-collab.env` is canonical.  `load_tokens()` re-reads it on
every request so a file rotation takes effect without a server restart.
Process-env `MAC_COLLAB_TOKEN*` is ignored when the file is present (cloud
seats with no file still use env).  Authenticated `GET /health` includes
`token_source`, `token_count`, `secrets_mtime`, `secrets_newer_than_process`,
`pid`, and `restart_hint` — never the token value.  A 401 body carries the
same restart hint.  `board` CLI prefers the file and prints that hint on 401.

After rotating the file, long-running processes that exported the old token
at start still need a new shell.  `pm2 restart mac-collab --update-env` if
the server process env itself still holds a stale token (file-canonical
auth does not need that restart).
