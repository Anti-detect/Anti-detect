"""
Recipe 11 — Import cookies JSON into MLX profile session (Playwright).

Real use: restore exported cookies, migrate session, or seed cold profiles.
Pair with Recipe 09 export.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from automation_patterns import import_cookies_playwright, playwright_page_from_cdp
from mlx_client import MlxLauncherClient
from mlx_env import load_env
from mlx_helpers import extract_cdp_url


def main() -> None:
    load_env(Path(__file__).resolve().parents[2] / ".env")
    cookies_path = Path(os.getenv("MLX_COOKIES_IN", "cookies_export.json"))
    target = os.getenv("MLX_SMOKE_URL", "https://example.com")

    if not cookies_path.is_file():
        print(f"Missing {cookies_path} — export first with recipes/09_cookie_warm_export.py")
        sys.exit(1)

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("pip install playwright")
        sys.exit(1)

    client = MlxLauncherClient()
    folder_id = os.environ["MLX_FOLDER_ID"]
    profile_id = os.environ["MLX_PROFILE_ID"]

    with client.profile_session(folder_id, profile_id, automation_type="puppeteer") as session:
        cdp_url = extract_cdp_url(session)
        with sync_playwright() as playwright:
            browser, page = playwright_page_from_cdp(playwright, cdp_url)
            count = import_cookies_playwright(page.context, cookies_path)
            page.goto(target, wait_until="domcontentloaded")
            print(f"Imported {count} cookies from {cookies_path}")
            print(f"Land URL: {page.url} — title: {page.title()}")

    print("Profile stopped.")


if __name__ == "__main__":
    main()
