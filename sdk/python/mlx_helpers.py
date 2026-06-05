"""Helpers for real-world MLX Launcher workflows."""
from __future__ import annotations

import time
from typing import Any, Callable, TypeVar

T = TypeVar("T")


def extract_debug_port(response: dict[str, Any]) -> int | None:
    """Read local CDP/debug port from a start-profile or quick-profile response."""
    data = response.get("data", response)
    if not isinstance(data, dict):
        return None
    for key in ("port", "debug_port", "cdp_port"):
        if key in data and data[key] is not None:
            return int(data[key])
    return None


def extract_cdp_url(response: dict[str, Any], host: str = "127.0.0.1") -> str:
    """Build a Playwright/Selenium CDP URL from launcher response JSON."""
    port = extract_debug_port(response)
    if port is None:
        raise ValueError(f"No debug port in launcher response: {response}")
    return f"http://{host}:{port}"


def build_quick_v3_payload(
    *,
    browser_type: str = "mimic",
    core_version: int = 124,
    os_type: str = "linux",
    automation: str = "puppeteer",
    headless: bool = False,
    proxy_host: str | None = None,
    proxy_port: int | None = None,
    proxy_type: str = "http",
    proxy_user: str = "",
    proxy_pass: str = "",
    start_urls: list[str] | None = None,
) -> dict[str, Any]:
    """
    Minimal Quick Profile v3 body for one-off runs.
    v3 places `proxy` at the root — not only under `parameters`.
    """
    payload: dict[str, Any] = {
        "browser_type": browser_type,
        "core_version": core_version,
        "os_type": os_type,
        "automation": automation,
        "is_headless": headless,
        "parameters": {
            "flags": {
                "audio_masking": "mask",
                "fonts_masking": "mask",
                "geolocation_masking": "mask",
                "graphics_masking": "mask",
                "navigator_masking": "mask",
                "proxy_masking": "custom" if proxy_host else "mask",
                "timezone_masking": "mask",
                "webrtc_masking": "mask",
            }
        },
    }
    if proxy_host and proxy_port:
        payload["proxy"] = {
            "host": proxy_host,
            "type": proxy_type,
            "port": proxy_port,
            "username": proxy_user,
            "password": proxy_pass,
        }
    if start_urls:
        payload["parameters"]["custom_start_urls"] = start_urls
    return payload


def retry(
    fn: Callable[[], T],
    *,
    attempts: int = 3,
    delay_seconds: float = 2.0,
    on_retry: Callable[[int, Exception], None] | None = None,
) -> T:
    """Retry transient launcher errors (agent warming up, profile busy)."""
    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        try:
            return fn()
        except Exception as exc:  # noqa: BLE001 — recipe-level resilience
            last_error = exc
            if attempt >= attempts:
                break
            if on_retry:
                on_retry(attempt, exc)
            time.sleep(delay_seconds)
    assert last_error is not None
    raise last_error
