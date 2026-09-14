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
