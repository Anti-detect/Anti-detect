"""Unit tests for mlx_helpers (no MLX agent required)."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mlx_helpers import (  # noqa: E402
    build_quick_v3_payload,
    extract_cdp_url,
    extract_debug_port,
    extract_selenium_address,
    retry,
)


class TestExtractPort(unittest.TestCase):
    def test_top_level_data_port(self) -> None:
        self.assertEqual(extract_debug_port({"data": {"port": 9222}}), 9222)

    def test_cdp_url(self) -> None:
        self.assertEqual(extract_cdp_url({"data": {"port": 9333}}), "http://127.0.0.1:9333")

    def test_selenium_address(self) -> None:
        self.assertEqual(extract_selenium_address({"data": {"port": 9444}}), "127.0.0.1:9444")


class TestQuickPayload(unittest.TestCase):
    def test_v3_proxy_at_root(self) -> None:
        payload = build_quick_v3_payload(proxy_host="proxy.test", proxy_port=8080)
        self.assertIn("proxy", payload)
        self.assertEqual(payload["proxy"]["host"], "proxy.test")
        self.assertNotIn("proxy", payload["parameters"])


class TestRetry(unittest.TestCase):
    def test_succeeds_after_failure(self) -> None:
        calls = {"n": 0}

        def flaky() -> str:
            calls["n"] += 1
            if calls["n"] < 2:
                raise RuntimeError("busy")
            return "ok"

        self.assertEqual(retry(flaky, attempts=3, delay_seconds=0), "ok")


if __name__ == "__main__":
    unittest.main()
