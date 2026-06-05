"""
Recipe 09 — Cookie warming + export on a saved MLX profile.

Real use: cold profiles, MMO account prep, backup cookies after manual login.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from automation_patterns import (
    export_context_cookies,
    load_warm_urls,
    playwright_page_from_cdp,
    warm_urls_playwright,
)
from mlx_client import MlxLauncherClient
from mlx_env import load_env
from mlx_helpers import extract_cdp_url


def main() -> None:
    load_env(Path(__file__).resolve().parents[2] / ".env")
    urls = load_warm_urls()
    out = Path(os.getenv("MLX_COOKIES_OUT", "cookies_export.json"))

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("pip install playwright && playwright install chromium")
        sys.exit(1)

    client = MlxLauncherClient()
    folder_id = os.environ["MLX_FOLDER_ID"]
    profile_id = os.environ["MLX_PROFILE_ID"]

    with client.profile_session(folder_id, profile_id, automation_type="puppeteer") as session:
        cdp_url = extract_cdp_url(session)
        with sync_playwright() as playwright:
            browser, page = playwright_page_from_cdp(playwright, cdp_url)
            context = page.context
            print(f"Warming {len(urls)} URL(s)...")
            warm_urls_playwright(page, urls)
            count = export_context_cookies(context, out)
            print(f"Exported {count} cookies -> {out.resolve()}")

    print("Profile stopped.")


if __name__ == "__main__":
    main()
