#!/usr/bin/env python3
"""ACP stdio client of the shared Grok leader.

Lists, loads, peeks, and prompts local chats (the same store the TUI uses).
Does not print secrets.  Requires a process holding ~/.grok/leader.sock
(pm2 grok-leader, or a TUI that spawned the leader).

  python3 /Users/jay/apps/grok-acp-runtime/leader-client.py list
  python3 /Users/jay/apps/grok-acp-runtime/leader-client.py peek --session-id ID --cwd DIR
  python3 /Users/jay/apps/grok-acp-runtime/leader-client.py prompt --session-id ID --cwd DIR --prompt "..."
"""
from __future__ import annotations

import argparse
import json
import os
import select
import subprocess
import sys
import time
from pathlib import Path

GROK = "/Users/jay/.grok/bin/grok"
CMD = [GROK, "agent", "--always-approve", "--leader", "stdio"]
SESSIONS_ROOT = Path.home() / ".grok" / "sessions"


class LeaderStdio:
    def __init__(self):
        self.p = subprocess.Popen(
            CMD,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        self._id = 0
        self._buf = b""

    def close(self):
        if self.p.poll() is None:
            self.p.terminate()
            try:
                self.p.wait(timeout=2)
            except Exception:
                self.p.kill()

    def _next(self):
        self._id += 1
        return self._id

    def _read_msg(self, deadline):
        while time.time() < deadline:
            if self.p.poll() is not None:
                err = self.p.stderr.read().decode(errors="replace")[:800]
                raise RuntimeError("leader stdio exited %s: %s" % (self.p.returncode, err))
            r, _, _ = select.select([self.p.stdout], [], [], 0.2)
            if not r:
                continue
            chunk = os.read(self.p.stdout.fileno(), 8192)
            if not chunk:
                continue
            self._buf += chunk
            while b"\n" in self._buf:
                raw, self._buf = self._buf.split(b"\n", 1)
                if not raw.strip():
                    continue
                try:
                    return json.loads(raw)
                except json.JSONDecodeError:
                    continue
        return None

    def request(self, method, params, timeout=30.0, collect_text=False):
        req_id = self._next()
        line = json.dumps({"jsonrpc": "2.0", "id": req_id, "method": method, "params": params}) + "\n"
        self.p.stdin.write(line.encode())
        self.p.stdin.flush()
        deadline = time.time() + timeout
        chunks = []
        while time.time() < deadline:
            msg = self._read_msg(deadline)
            if msg is None:
                break
            if collect_text:
                text = extract_agent_text(msg)
                if text:
                    chunks.append(text)
            if msg.get("id") != req_id:
                continue
            if "error" in msg:
                raise RuntimeError(json.dumps(msg["error"]))
            result = msg.get("result") or {}
            if collect_text:
                return result, "".join(chunks)
            return result
        raise TimeoutError("no ACP result for %s" % method)


def extract_agent_text(msg):
    """Pull assistant text out of a session/update notification."""
    if not isinstance(msg, dict):
        return ""
    if msg.get("method") not in {"session/update", "x.ai/session/update"}:
        return ""
    params = msg.get("params") or {}
    upd = params.get("update") if isinstance(params.get("update"), dict) else params
    kind = upd.get("sessionUpdate") or upd.get("session_update") or ""
    if kind != "agent_message_chunk":
        return ""
    content = upd.get("content") or {}
    if isinstance(content, dict):
        return content.get("text") or ""
    if isinstance(content, str):
        return content
    return ""


def slim_session(s):
    return {
        "sessionId": s.get("sessionId"),
        "cwd": s.get("cwd"),
        "title": s.get("title"),
        "updatedAt": s.get("updatedAt"),
    }


def _initialize(client, timeout=25.0):
    return client.request(
        "initialize",
        {
            "protocolVersion": 1,
            "clientInfo": {"name": "grok-leader-client", "version": "1.1"},
            "clientCapabilities": {
                "fs": {"readTextFile": True, "writeTextFile": True},
                "terminal": True,
            },
        },
        timeout=timeout,
    )


def find_session_dir(session_id: str):
    if not SESSIONS_ROOT.is_dir() or "/" in session_id or "\\" in session_id:
        return None
    matches = list(SESSIONS_ROOT.glob("*/" + session_id))
    dirs = [p for p in matches if p.is_dir()]
    return dirs[0] if dirs else None


def peek_from_disk(session_id: str) -> dict:
    """Read summary.json.  Does not session/load a live TUI (that hangs ~45s)."""
    path = find_session_dir(session_id)
    if path is None:
        return {"ok": False, "error": "session dir not found", "sessionId": session_id}
    summary_path = path / "summary.json"
    if not summary_path.is_file():
        return {"ok": False, "error": "summary.json missing", "sessionId": session_id, "dir": str(path)}
    try:
        data = json.loads(summary_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {"ok": False, "error": "summary.json parse failed: %s" % exc, "sessionId": session_id}
    info = data.get("info") if isinstance(data.get("info"), dict) else {}
    return {
        "ok": True,
        "sessionId": session_id,
        "cwd": info.get("cwd"),
        "title": data.get("generated_title") or data.get("session_summary"),
        "text": data.get("last_turn_summary") or "",
        "recap": data.get("last_recap") or "",
        "updatedAt": data.get("updated_at") or data.get("last_active_at"),
        "source": "disk",
    }


def _resume(client, session_id, cwd, timeout=20.0):
    """Attach to a session the TUI already has open.  session/load hangs on live chats."""
    return client.request(
        "session/resume",
        {"sessionId": session_id, "cwd": cwd},
        timeout=timeout,
    )


def main():
    p = argparse.ArgumentParser(description="List/load/prompt local Grok chats via the shared leader")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("handshake")
    ls = sub.add_parser("list")
    ls.add_argument("--cwd", default="")
    ld = sub.add_parser("load")
    ld.add_argument("--session-id", required=True)
    ld.add_argument("--cwd", default="/Users/jay")
    pk = sub.add_parser("peek", help="session/load and return any streamed text, no prompt")
    pk.add_argument("--session-id", required=True)
    pk.add_argument("--cwd", default="/Users/jay")
    pr = sub.add_parser("prompt", help="session/load then session/prompt on a live TUI chat")
    pr.add_argument("--session-id", required=True)
    pr.add_argument("--prompt", required=True)
    pr.add_argument("--cwd", default="/Users/jay")
    pr.add_argument("--timeout", type=float, default=180.0)
    args = p.parse_args()

    if args.cmd == "peek":
        print(json.dumps(peek_from_disk(args.session_id), indent=2))
        return

    client = LeaderStdio()
    try:
        init = _initialize(client)
        if args.cmd == "handshake":
            caps = init.get("agentCapabilities") or {}
            print(json.dumps({
                "ok": True,
                "protocolVersion": init.get("protocolVersion"),
                "sessionCapabilities": caps.get("sessionCapabilities"),
                "loadSession": caps.get("loadSession"),
            }, indent=2))
            return
        if args.cmd == "list":
            params = {}
            if args.cwd:
                params["cwd"] = args.cwd
            listed = client.request("session/list", params, timeout=20.0)
            sessions = [slim_session(s) for s in (listed.get("sessions") or [])]
            print(json.dumps({"ok": True, "count": len(sessions), "sessions": sessions}, indent=2))
            return
        if args.cmd == "load":
            # Idle / disk sessions only.  Live TUI chats hang on session/load — use prompt.
            loaded, text = client.request(
                "session/load",
                {
                    "sessionId": args.session_id,
                    "cwd": args.cwd,
                    "mcpServers": [],
                },
                timeout=45.0,
                collect_text=True,
            )
            print(json.dumps({
                "ok": True,
                "sessionId": args.session_id,
                "cwd": args.cwd,
                "keys": sorted(loaded.keys()),
                "text": text,
            }, indent=2))
            return
        if args.cmd == "prompt":
            _resume(client, args.session_id, args.cwd)
            result, text = client.request(
                "session/prompt",
                {
                    "sessionId": args.session_id,
                    "prompt": [{"type": "text", "text": args.prompt}],
                },
                timeout=float(args.timeout),
                collect_text=True,
            )
            print(json.dumps({
                "ok": True,
                "sessionId": args.session_id,
                "cwd": args.cwd,
                "text": text,
                "result": result,
            }, indent=2))
            return
    finally:
        client.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(json.dumps({"ok": False, "error": str(e)}), file=sys.stderr)
        sys.exit(1)
