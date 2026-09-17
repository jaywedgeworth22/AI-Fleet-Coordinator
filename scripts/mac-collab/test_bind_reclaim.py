"""Automated coverage for mac-collab port-bind/reclaim.

The 2026-08-20 outage: pid 4783 was reparented to launchd, kept :8792
LISTENing, and served nothing.  Every pm2 replacement died on EADDRINUSE
(~24000 restarts, board down two hours).  A second outage was the same
shape (orphans on 8792).  These tests pin the reclaim path that must
SIGTERM a stale board server, SIGKILL if it does not drop the port, and
refuse to kill anything that is not a stale board server.
"""
import errno
import importlib.util
import io
import os
import signal
import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "mac_collab_server", HERE / "mac-collab-server.py"
)
server = importlib.util.module_from_spec(spec)
spec.loader.exec_module(server)


class TestBindReclaim(unittest.TestCase):
    def setUp(self):
        self.held_stdout = sys.stdout
        self.held_stderr = sys.stderr
        sys.stdout = io.StringIO()
        sys.stderr = io.StringIO()

    def tearDown(self):
        sys.stdout = self.held_stdout
        sys.stderr = self.held_stderr

    @patch("subprocess.run")
    def test_port_holder_pids(self, mock_run):
        mock_result = MagicMock()
        mock_result.stdout = "123\n456\n"
        mock_run.return_value = mock_result
        with patch("os.getpid", return_value=999):
            pids = server._port_holder_pids()
            self.assertEqual(pids, [123, 456])

    @patch("subprocess.run")
    def test_all_board_server_pids(self, mock_run):
        mock_result = MagicMock()
        mock_result.stdout = " 123 python mac-collab-server.py\n 456 bash\n"
        mock_run.return_value = mock_result
        with patch("os.getpid", return_value=999):
            pids = server._all_board_server_pids()
            self.assertEqual(pids, [123])

    @patch("subprocess.run")
    def test_is_board_server(self, mock_run):
        mock_result = MagicMock()
        mock_result.stdout = "/path/to/python mac-collab-server.py\n"
        mock_run.return_value = mock_result
        self.assertTrue(server._is_board_server(123))
        mock_result.stdout = "/path/to/python other.py\n"
        self.assertFalse(server._is_board_server(456))

    @patch("urllib.request.urlopen")
    def test_port_answers_health(self, mock_urlopen):
        mock_resp = MagicMock()
        mock_urlopen.return_value.__enter__.return_value = mock_resp
        self.assertTrue(server._port_answers_health())
        mock_urlopen.side_effect = Exception("failed")
        self.assertFalse(server._port_answers_health())

    @patch.object(server, "_is_board_server")
    @patch.object(server, "_port_answers_health")
    def test_is_stale_board_server(self, mock_health, mock_is_server):
        mock_is_server.return_value = True
        mock_health.return_value = False
        self.assertTrue(server._is_stale_board_server(123))
        mock_health.return_value = True
        self.assertFalse(server._is_stale_board_server(123))
        mock_is_server.return_value = False
        mock_health.return_value = False
        self.assertFalse(server._is_stale_board_server(123))

    @patch.object(server, "ThreadingHTTPServer")
    @patch.object(server, "_port_holder_pids")
    @patch.object(server, "_is_stale_board_server")
    @patch.object(server, "_is_board_server")
    @patch("os.kill")
    @patch("time.sleep")
    @patch("time.time")
    def test_bind_or_reclaim_success_first_try(
        self, mock_time, mock_sleep, mock_kill, mock_is_board, mock_is_stale, mock_pids, mock_server
    ):
        mock_server.return_value = "server_instance"
        inst = server._bind_or_reclaim()
        self.assertEqual(inst, "server_instance")
        mock_pids.assert_not_called()

    @patch.object(server, "ThreadingHTTPServer")
    @patch.object(server, "_port_holder_pids")
    @patch.object(server, "_is_stale_board_server")
    @patch.object(server, "_is_board_server")
    @patch("os.kill")
    @patch("time.sleep")
    @patch("time.time")
    def test_bind_or_reclaim_stale_found(
        self, mock_time, mock_sleep, mock_kill, mock_is_board, mock_is_stale, mock_pids, mock_server
    ):
        err_in_use = OSError(errno.EADDRINUSE, "In use")
        mock_server.side_effect = [err_in_use, "server_instance"]
        mock_pids.return_value = [123]
        mock_is_stale.return_value = True
        mock_time.side_effect = [100, 101]
        inst = server._bind_or_reclaim()
        self.assertEqual(inst, "server_instance")
        mock_kill.assert_called_with(123, signal.SIGTERM)

    @patch.object(server, "ThreadingHTTPServer")
    @patch.object(server, "_port_holder_pids")
    @patch.object(server, "_is_stale_board_server")
    @patch.object(server, "_is_board_server")
    @patch("os.kill")
    @patch("time.sleep")
    @patch("time.time")
    def test_bind_or_reclaim_stale_sigkill(
        self, mock_time, mock_sleep, mock_kill, mock_is_board, mock_is_stale, mock_pids, mock_server
    ):
        err_in_use = OSError(errno.EADDRINUSE, "In use")
        mock_server.side_effect = [err_in_use, "server_instance"]
        mock_pids.return_value = [123]
        mock_is_stale.return_value = True
        mock_time.side_effect = [100, 116]
        inst = server._bind_or_reclaim()
        self.assertEqual(inst, "server_instance")
        mock_kill.assert_any_call(123, signal.SIGTERM)
        mock_kill.assert_any_call(123, signal.SIGKILL)

    @patch.object(server, "ThreadingHTTPServer")
    @patch.object(server, "_port_holder_pids")
    @patch.object(server, "_is_stale_board_server")
    @patch.object(server, "_is_board_server")
    @patch("os.kill")
    @patch("time.sleep")
    @patch("time.time")
    def test_bind_or_reclaim_not_stale(
        self, mock_time, mock_sleep, mock_kill, mock_is_board, mock_is_stale, mock_pids, mock_server
    ):
        err_in_use = OSError(errno.EADDRINUSE, "In use")
        mock_server.side_effect = err_in_use
        mock_pids.return_value = [123]
        mock_is_stale.return_value = False
        mock_is_board.return_value = True
        with self.assertRaises(SystemExit) as cm:
            server._bind_or_reclaim()
        self.assertEqual(cm.exception.code, 3)
        mock_kill.assert_not_called()

    @patch.object(server, "ThreadingHTTPServer")
    @patch.object(server, "_all_board_server_pids")
    @patch.object(server, "_port_holder_pids")
    @patch.object(server, "_is_stale_board_server")
    @patch("os.kill")
    @patch("time.sleep")
    @patch("time.time")
    def test_bind_or_reclaim_lsof_none_falls_back_to_ps(
        self, mock_time, mock_sleep, mock_kill, mock_is_stale, mock_pids, mock_ps, mock_server
    ):
        err_in_use = OSError(errno.EADDRINUSE, "In use")
        mock_server.side_effect = [err_in_use, "server_instance"]
        mock_pids.return_value = None
        mock_ps.return_value = [321]
        mock_is_stale.return_value = True
        mock_time.side_effect = [100, 101]
        inst = server._bind_or_reclaim()
        self.assertEqual(inst, "server_instance")
        mock_ps.assert_called_once()
        mock_kill.assert_called_with(321, signal.SIGTERM)

    @patch.object(server, "ThreadingHTTPServer")
    @patch.object(server, "_port_holder_pids")
    @patch.object(server, "_is_stale_board_server")
    @patch.object(server, "_is_board_server")
    @patch("os.kill")
    def test_bind_or_reclaim_unrelated_process_refuses(
        self, mock_kill, mock_is_board, mock_is_stale, mock_pids, mock_server
    ):
        err_in_use = OSError(errno.EADDRINUSE, "In use")
        mock_server.side_effect = err_in_use
        mock_pids.return_value = [555]
        mock_is_stale.return_value = False
        mock_is_board.return_value = False
        with self.assertRaises(SystemExit) as cm:
            server._bind_or_reclaim()
        self.assertEqual(cm.exception.code, 3)
        mock_kill.assert_not_called()


if __name__ == "__main__":
    unittest.main()
