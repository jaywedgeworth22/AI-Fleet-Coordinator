"""MAC_COLLAB_TOKEN rotation: file is canonical, health exposes mtime, 401 hints restart.

Never asserts on token values in health/401 bodies -- those must stay secret.
"""
import importlib.util
import os
import tempfile
import unittest
from importlib.machinery import SourceFileLoader
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "mac_collab_server_token", HERE / "mac-collab-server.py"
)
server = importlib.util.module_from_spec(spec)
spec.loader.exec_module(server)

board_cli = SourceFileLoader("board_cli", str(HERE / "board")).load_module()


class TestTokenStaleness(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.secrets = Path(self.tmp.name) / "mac-collab.env"
        self.secrets.write_text('MAC_COLLAB_TOKEN="file-token-aaa"\n', encoding="utf-8")
        self._orig_secrets = server.SECRETS
        server.SECRETS = self.secrets
        server._LOGGED_FILE_WINS = False
        self._env_was = os.environ.get("MAC_COLLAB_TOKEN")
        os.environ.pop("MAC_COLLAB_TOKEN", None)

    def tearDown(self):
        server.SECRETS = self._orig_secrets
        server._LOGGED_FILE_WINS = False
        if self._env_was is None:
            os.environ.pop("MAC_COLLAB_TOKEN", None)
        else:
            os.environ["MAC_COLLAB_TOKEN"] = self._env_was
        self.tmp.cleanup()

    def test_file_wins_over_env(self):
        os.environ["MAC_COLLAB_TOKEN"] = "env-token-bbb"
        tokens = server.load_tokens()
        self.assertIn("file-token-aaa", tokens)
        self.assertNotIn("env-token-bbb", tokens)

    def test_reload_after_file_change(self):
        first = server.load_tokens()
        self.assertIn("file-token-aaa", first)
        self.secrets.write_text('MAC_COLLAB_TOKEN="file-token-ccc"\n', encoding="utf-8")
        second = server.load_tokens()
        self.assertIn("file-token-ccc", second)
        self.assertNotIn("file-token-aaa", second)

    def test_env_only_when_file_missing(self):
        server.SECRETS = Path(self.tmp.name) / "does-not-exist.env"
        os.environ["MAC_COLLAB_TOKEN"] = "env-token-bbb"
        tokens = server.load_tokens()
        self.assertIn("env-token-bbb", tokens)

    def test_auth_meta_has_mtime_not_token(self):
        meta = server.token_auth_meta()
        self.assertEqual(meta["token_source"], "file")
        self.assertEqual(meta["token_count"], 1)
        self.assertIsInstance(meta["secrets_mtime"], int)
        blob = str(meta)
        self.assertNotIn("file-token-aaa", blob)
        self.assertIn("pm2 restart mac-collab --update-env", meta["restart_hint"])

    def test_secrets_newer_than_process(self):
        os.utime(self.secrets, (server.STARTED + 10, server.STARTED + 10))
        meta = server.token_auth_meta()
        self.assertTrue(meta["secrets_newer_than_process"])

    def test_401_hint_omits_token_value(self):
        self.assertIn("rotated", server.AUTH_FAIL_HINT)
        self.assertNotIn("file-token-aaa", server.AUTH_FAIL_HINT)
        self.assertNotIn("env-token", server.AUTH_FAIL_HINT)

    def test_authorized_uses_passed_tokens_snapshot(self):
        from unittest.mock import MagicMock, patch

        handler = MagicMock()
        handler.headers = {"Authorization": "Bearer snap-token"}
        with patch.object(
            server, "load_tokens", side_effect=AssertionError("should not reload")
        ):
            ident = server.authorized(handler, tokens={"snap-token": None})
        self.assertEqual(ident, "OWNER")

    def test_cookie_does_not_survive_empty_tokens(self):
        """HMAC key is derived from live tokens.  An unreadable file does not
        keep old cookies valid; checking the cookie first would still fail.
        """
        from http.server import BaseHTTPRequestHandler
        from unittest.mock import MagicMock

        cookie = server.mint_session_value("OWNER")
        handler = MagicMock(spec=BaseHTTPRequestHandler)
        handler.headers = {"Cookie": f"{server.SESSION_COOKIE}={cookie}"}
        self.assertEqual(server.cookie_authorized(handler), "OWNER")
        self.secrets.write_text("", encoding="utf-8")
        self.assertIsNone(server.cookie_authorized(handler))
        self.assertIsNone(server.authorized(handler))


class TestBoardCliToken(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.secrets = Path(self.tmp.name) / "mac-collab.env"
        self.secrets.write_text('MAC_COLLAB_TOKEN="file-token-aaa"\n', encoding="utf-8")
        self._orig = board_cli.SECRETS
        board_cli.SECRETS = self.secrets
        self._env_was = os.environ.get("MAC_COLLAB_TOKEN")
        os.environ.pop("MAC_COLLAB_TOKEN", None)

    def tearDown(self):
        board_cli.SECRETS = self._orig
        if self._env_was is None:
            os.environ.pop("MAC_COLLAB_TOKEN", None)
        else:
            os.environ["MAC_COLLAB_TOKEN"] = self._env_was
        self.tmp.cleanup()

    def test_board_prefers_file_over_env(self):
        os.environ["MAC_COLLAB_TOKEN"] = "env-token-bbb"
        self.assertEqual(board_cli.token(), "file-token-aaa")

    def test_board_401_hint_omits_token(self):
        hint = board_cli.AUTH_FAIL_HINT
        self.assertIn("rotated", hint)
        self.assertIn("pm2 restart mac-collab --update-env", hint)
        self.assertNotIn("file-token-aaa", hint)


if __name__ == "__main__":
    unittest.main()
