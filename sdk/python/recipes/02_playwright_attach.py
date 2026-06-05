"""
Recipe 02 — Start saved profile and automate with Playwright over CDP.

Real use: stealth UI automation without launching a vanilla Chromium.
Requires: pip install playwright && playwright install chromium
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mlx_client import MlxLauncherClient
from mlx_env import load_env
from mlx_helpers import extract_cdp_url


def automate(page) -> None:
    """Replace with your flow (login, form fill, scrape, etc.)."""
    page.goto("https://example.com", wait_until="domcontentloaded")
    print(f"Title: {page.title()}")


def main() -> None:
    load_env(Path(__file__).resolve().parents[2] / ".env")
    client = MlxLauncherClient()
    folder_id = os.environ["MLX_FOLDER_ID"]
    profile_id = os.environ["MLX_PROFILE_ID"]
    target_url = os.getenv("MLX_SMOKE_URL", "https://example.com")

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Install Playwright first:")
        print("  pip install playwright")
        print("  playwright install chromium")
        sys.exit(1)

    with client.profile_session(folder_id, profile_id, automation_type="puppeteer") as session:
        cdp_url = extract_cdp_url(session)
        print(f"Connecting Playwright to {cdp_url}")

        with sync_playwright() as playwright:
            browser = playwright.chromium.connect_over_cdp(cdp_url)
            context = browser.contexts[0] if browser.contexts else browser.new_context()
            page = context.pages[0] if context.pages else context.new_page()
            page.goto(target_url, wait_until="domcontentloaded")
            automate(page)

    print("Profile stopped cleanly.")


if __name__ == "__main__":
    main()
