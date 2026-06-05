"""Reusable automation patterns for MLX recipes (Playwright + Selenium)."""
from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from mlx_helpers import extract_cdp_url, extract_debug_port, extract_selenium_address


@dataclass
class LoginConfig:
    login_url: str
    username_selector: str
    password_selector: str
    submit_selector: str
    success_url_contains: str = ""
    post_login_wait_ms: int = 2000

    @classmethod
    def from_json(cls, path: Path) -> LoginConfig:
        data = json.loads(path.read_text(encoding="utf-8"))
        selectors = data.get("selectors", {})
        success = data.get("success_indicator", {})
        return cls(
            login_url=data["login_url"],
            username_selector=selectors["username"],
            password_selector=selectors["password"],
            submit_selector=selectors["submit"],
            success_url_contains=success.get("url_contains", ""),
            post_login_wait_ms=int(data.get("post_login_wait_ms", 2000)),
        )

    @classmethod
    def from_env(cls) -> LoginConfig:
        return cls(
            login_url=os.environ["MLX_LOGIN_URL"],
            username_selector=os.getenv("MLX_LOGIN_USER_SELECTOR", "#username"),
            password_selector=os.getenv("MLX_LOGIN_PASS_SELECTOR", "#password"),
            submit_selector=os.getenv("MLX_LOGIN_SUBMIT_SELECTOR", "button[type='submit']"),
            success_url_contains=os.getenv("MLX_LOGIN_SUCCESS_URL_CONTAINS", ""),
            post_login_wait_ms=int(os.getenv("MLX_LOGIN_WAIT_MS", "2000")),
        )


def human_pause(min_ms: int = 400, max_ms: int = 1200) -> None:
    """Small random delay between UI actions (reduces bot-like timing)."""
    import random

    time.sleep(random.uniform(min_ms, max_ms) / 1000.0)


def wait_for_debug_port(
    response: dict[str, Any],
    *,
    timeout_seconds: float = 30.0,
    poll_seconds: float = 1.0,
) -> int:
    """Poll until launcher response exposes a debug port (agent still starting)."""
    deadline = time.monotonic() + timeout_seconds
    while time.monotonic() < deadline:
        port = extract_debug_port(response)
        if port is not None:
            return port
        time.sleep(poll_seconds)
    raise TimeoutError(f"No debug port within {timeout_seconds}s: {response}")


def playwright_page_from_cdp(playwright, cdp_url: str):
    """Return (browser, page) attached to MLX browser over CDP."""
    browser = playwright.chromium.connect_over_cdp(cdp_url)
    context = browser.contexts[0] if browser.contexts else browser.new_context()
    page = context.pages[0] if context.pages else context.new_page()
    return browser, page


def run_login_playwright(page, config: LoginConfig, username: str, password: str) -> None:
    """Generic login flow — replace selectors in login.example.json for your app."""
    page.goto(config.login_url, wait_until="domcontentloaded")
    human_pause()
    page.fill(config.username_selector, username)
    human_pause()
    page.fill(config.password_selector, password)
    human_pause()
    page.click(config.submit_selector)
    page.wait_for_timeout(config.post_login_wait_ms)
    if config.success_url_contains and config.success_url_contains not in page.url:
        raise RuntimeError(
            f"Login may have failed — expected URL to contain {config.success_url_contains!r}, got {page.url}"
        )


def connect_selenium_chrome(session: dict[str, Any]):
    """Attach Selenium to MLX browser via debuggerAddress."""
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
    except ImportError as exc:
        raise ImportError("pip install selenium") from exc

    address = extract_selenium_address(session)
    options = Options()
    options.add_experimental_option("debuggerAddress", address)
    return webdriver.Chrome(options=options)


def load_login_config() -> LoginConfig:
    config_path = os.getenv("MLX_LOGIN_CONFIG")
    if config_path:
        return LoginConfig.from_json(Path(config_path))
    return LoginConfig.from_env()


def load_warm_urls() -> list[str]:
    """URLs to visit for cookie warming (comma env or warm-urls.json)."""
    config = os.getenv("MLX_WARM_URLS_JSON")
    if config:
        data = json.loads(Path(config).read_text(encoding="utf-8"))
        return list(data.get("urls", []))
    raw = os.getenv("MLX_WARM_URLS", "https://example.com")
    return [u.strip() for u in raw.split(",") if u.strip()]


def warm_urls_playwright(page, urls: list[str]) -> None:
    for url in urls:
        page.goto(url, wait_until="domcontentloaded")
        human_pause(800, 2000)
        print(f"  warmed: {url}")


def export_context_cookies(context, out_path: Path) -> int:
    cookies = context.cookies()
    out_path.write_text(json.dumps(cookies, indent=2), encoding="utf-8")
    return len(cookies)


def scrape_page_snapshot(page, selector: str = "body") -> dict[str, str]:
    return {
        "url": page.url,
        "title": page.title(),
        "text": page.inner_text(selector)[:4000],
    }


def import_cookies_playwright(context, cookies_path: Path) -> int:
    """Load cookies JSON (Playwright export format) into browser context."""
    cookies = json.loads(cookies_path.read_text(encoding="utf-8"))
    if isinstance(cookies, dict) and "cookies" in cookies:
        cookies = cookies["cookies"]
    if not isinstance(cookies, list):
        raise ValueError("Expected list of cookie objects or {cookies: [...]}")
    context.add_cookies(cookies)
    return len(cookies)
