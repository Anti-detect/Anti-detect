"""
Recipe 07 — Configurable login flow on a saved MLX profile (Playwright).

Real use: daily re-login checks, account warm-up, or post-cookie session validation.
Set credentials via env — never commit secrets.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from automation_patterns import (
    load_login_config,
    playwright_page_from_cdp,
    run_login_playwright,
)
from mlx_client import MlxLauncherClient
from mlx_env import load_env
from mlx_helpers import extract_cdp_url


def main() -> None:
    load_env(Path(__file__).resolve().parents[2] / ".env")
    username = os.getenv("MLX_LOGIN_USER")
    password = os.getenv("MLX_LOGIN_PASS")
    if not username or not password:
        print("Set MLX_LOGIN_USER and MLX_LOGIN_PASS in sdk/.env")
        print("Optional: MLX_LOGIN_CONFIG=recipes/login.example.json")
        sys.exit(1)

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("pip install playwright && playwright install chromium")
        sys.exit(1)

    config = load_login_config()
    client = MlxLauncherClient()
    folder_id = os.environ["MLX_FOLDER_ID"]
    profile_id = os.environ["MLX_PROFILE_ID"]

    with client.profile_session(folder_id, profile_id, automation_type="puppeteer") as session:
        cdp_url = extract_cdp_url(session)
        with sync_playwright() as playwright:
            _, page = playwright_page_from_cdp(playwright, cdp_url)
            run_login_playwright(page, config, username, password)
            print(f"Login flow finished — current URL: {page.url}")

    print("Profile stopped.")


if __name__ == "__main__":
    main()
