"""Unit tests for fleet_rag.core.http_json's retry/backoff behavior: 408 handling and the
RECALL_HTTP_RETRIES / RECALL_HTTP_BACKOFF_MAX env overrides used by `recall-tunnel env` to
widen the budget for the SSH-tunnel path.

    cd scripts && python3 -m unittest fleet_rag.tests.test_core_http -v

No network: urllib.request.urlopen is mocked in every test, and time.sleep is mocked so no
test actually waits out a backoff.
"""
from __future__ import annotations

import io
import json
import os
import unittest
import urllib.error
from unittest import mock

from fleet_rag import core
from fleet_rag.core import FleetRagError


class FakeResponse:
    """Stands in for the object urllib.request.urlopen() returns, used as a context manager."""

    def __init__(self, payload: dict) -> None:
        self._body = json.dumps(payload).encode()

    def __enter__(self) -> "FakeResponse":
        return self

    def __exit__(self, *exc) -> bool:
        return False

    def read(self) -> bytes:
        return self._body


def http_error(code: int) -> urllib.error.HTTPError:
    # A ResourceWarning about HTTPError's own fp can print here on an interim (retried) attempt
    # whose error is discarded before http_json's final `e.read(400)` -- cosmetic only, unittest
    # does not fail on it.
    return urllib.error.HTTPError(url="https://x.test/path", code=code, msg="err",
                                  hdrs=None, fp=io.BytesIO(b""))


class Http408RetryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.env = mock.patch.dict(os.environ, {}, clear=False)
        self.env.start()
        os.environ.pop(core.RETRIES_ENV, None)
        os.environ.pop(core.BACKOFF_MAX_ENV, None)
        self.sleep = mock.patch.object(core.time, "sleep")
        self.sleep_mock = self.sleep.start()

    def tearDown(self) -> None:
        self.sleep.stop()
        self.env.stop()

    def test_408_is_retried_like_429_and_5xx(self) -> None:
        calls = {"n": 0}

        def fake_urlopen(req, timeout=None):
            calls["n"] += 1
            if calls["n"] < 3:
                raise http_error(408)
            return FakeResponse({"ok": True})

        with mock.patch.object(core.urllib.request, "urlopen", fake_urlopen):
            result = core.http_json("https://x.test/path")
        self.assertEqual(result, {"ok": True})
        self.assertEqual(calls["n"], 3)

    def test_408_exhausts_retries_and_raises_naming_the_code(self) -> None:
        def always_408(req, timeout=None):
            raise http_error(408)

        with mock.patch.object(core.urllib.request, "urlopen", always_408):
            with self.assertRaisesRegex(FleetRagError, "HTTP 408"):
                core.http_json("https://x.test/path", retries=2)

    def test_default_retry_count_is_unchanged_when_env_unset(self) -> None:
        calls = {"n": 0}

        def always_500(req, timeout=None):
            calls["n"] += 1
            raise http_error(500)

        with mock.patch.object(core.urllib.request, "urlopen", always_500):
            with self.assertRaises(FleetRagError):
                core.http_json("https://x.test/path")
        self.assertEqual(calls["n"], core.RETRIES + 1)   # RETRIES retries + the first attempt

    def test_a_4xx_that_is_not_408_or_429_is_never_retried(self) -> None:
        calls = {"n": 0}

        def always_404(req, timeout=None):
            calls["n"] += 1
            raise http_error(404)

        with mock.patch.object(core.urllib.request, "urlopen", always_404):
            with self.assertRaisesRegex(FleetRagError, "HTTP 404"):
                core.http_json("https://x.test/path")
        self.assertEqual(calls["n"], 1)


class RetryEnvOverrideTests(unittest.TestCase):
    def setUp(self) -> None:
        self.env = mock.patch.dict(os.environ, {}, clear=False)
        self.env.start()
        os.environ.pop(core.RETRIES_ENV, None)
        os.environ.pop(core.BACKOFF_MAX_ENV, None)
        self.sleep = mock.patch.object(core.time, "sleep")
        self.sleep_mock = self.sleep.start()

    def tearDown(self) -> None:
        self.sleep.stop()
        self.env.stop()

    def test_recall_http_retries_env_widens_the_budget(self) -> None:
        os.environ[core.RETRIES_ENV] = "6"
        calls = {"n": 0}

        def always_503(req, timeout=None):
            calls["n"] += 1
            raise http_error(503)

        with mock.patch.object(core.urllib.request, "urlopen", always_503):
            with self.assertRaises(FleetRagError):
                core.http_json("https://x.test/path")
        self.assertEqual(calls["n"], 7)   # 6 retries + the first attempt

    def test_recall_http_retries_env_is_read_at_call_time_not_import_time(self) -> None:
        # Two calls in the same process, env changed in between -- proves it is not baked in
        # as a function default evaluated once at import/definition time.
        calls = {"n": 0}

        def always_503(req, timeout=None):
            calls["n"] += 1
            raise http_error(503)

        with mock.patch.object(core.urllib.request, "urlopen", always_503):
            os.environ[core.RETRIES_ENV] = "0"
            with self.assertRaises(FleetRagError):
                core.http_json("https://x.test/path")
            self.assertEqual(calls["n"], 1)

            calls["n"] = 0
            os.environ[core.RETRIES_ENV] = "2"
            with self.assertRaises(FleetRagError):
                core.http_json("https://x.test/path")
            self.assertEqual(calls["n"], 3)

    def test_explicit_retries_argument_overrides_the_env_var(self) -> None:
        os.environ[core.RETRIES_ENV] = "6"
        calls = {"n": 0}

        def always_503(req, timeout=None):
            calls["n"] += 1
            raise http_error(503)

        with mock.patch.object(core.urllib.request, "urlopen", always_503):
            with self.assertRaises(FleetRagError):
                core.http_json("https://x.test/path", retries=1)
        self.assertEqual(calls["n"], 2)   # explicit retries=1 wins over the env var

    def test_recall_http_backoff_max_env_caps_the_sleep(self) -> None:
        os.environ[core.BACKOFF_MAX_ENV] = "3"

        def always_503(req, timeout=None):
            raise http_error(503)

        with mock.patch.object(core.urllib.request, "urlopen", always_503):
            with self.assertRaises(FleetRagError):
                core.http_json("https://x.test/path", retries=5)
        # min(2**attempt, 3) for attempt 0..4 -> 1, 2, 3, 3, 3
        self.sleep_mock.assert_has_calls([mock.call(1), mock.call(2), mock.call(3),
                                          mock.call(3), mock.call(3)])

    def test_default_backoff_cap_is_ten_when_env_unset(self) -> None:
        def always_503(req, timeout=None):
            raise http_error(503)

        with mock.patch.object(core.urllib.request, "urlopen", always_503):
            with self.assertRaises(FleetRagError):
                core.http_json("https://x.test/path", retries=5)
        # min(2**attempt, 10) for attempt 0..4 -> 1, 2, 4, 8, 10
        self.sleep_mock.assert_has_calls([mock.call(1), mock.call(2), mock.call(4),
                                          mock.call(8), mock.call(10)])

    def test_malformed_env_value_falls_back_to_the_default(self) -> None:
        os.environ[core.RETRIES_ENV] = "not-a-number"
        calls = {"n": 0}

        def always_503(req, timeout=None):
            calls["n"] += 1
            raise http_error(503)

        with mock.patch.object(core.urllib.request, "urlopen", always_503):
            with self.assertRaises(FleetRagError):
                core.http_json("https://x.test/path")
        self.assertEqual(calls["n"], core.RETRIES + 1)


if __name__ == "__main__":
    unittest.main()
