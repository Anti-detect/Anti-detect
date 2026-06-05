"""
Recipe 10 — Scrape a page snapshot via MLX + Playwright.

Real use: price checks, listing monitors, QA on logged-in pages.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from automation_patterns import playwright_page_from_cdp, scrape_page_snapshot
from mlx_client import MlxLauncherClient
from mlx_env import load_env
from mlx_helpers import extract_cdp_url


def main() -> None:
    load_env(Path(__file__).resolve().parents[2] / ".env")
    target = os.getenv("MLX_SCRAPE_URL", os.getenv("MLX_SMOKE_URL", "https://example.com"))
    selector = os.getenv("MLX_SCRAPE_SELECTOR", "body")
    out = Path(os.getenv("MLX_SCRAPE_OUT", "scrape_snapshot.json"))

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
            _, page = playwright_page_from_cdp(playwright, cdp_url)
            page.goto(target, wait_until="domcontentloaded")
            snapshot = scrape_page_snapshot(page, selector)
            out.write_text(json.dumps(snapshot, indent=2), encoding="utf-8")
            print(json.dumps(snapshot, indent=2)[:500])
            print(f"\nSaved -> {out.resolve()}")

    print("Profile stopped.")


if __name__ == "__main__":
    main()
