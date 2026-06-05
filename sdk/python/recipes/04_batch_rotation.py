"""
Recipe 04 — Rotate through multiple saved profiles sequentially.

Real use: MMO / multi-shop workflows — one account per profile, same script, isolated storage.
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mlx_client import MlxLauncherClient
from mlx_env import load_env
from mlx_helpers import extract_cdp_url, extract_debug_port


def _use_playwright() -> bool:
    return os.getenv("MLX_USE_PLAYWRIGHT", "").lower() in ("1", "true", "yes")


def run_job(label: str, session: dict) -> None:
    """Placeholder sleep, or Playwright smoke when MLX_USE_PLAYWRIGHT=1."""
    if _use_playwright():
        try:
            from playwright.sync_api import sync_playwright
        except ImportError:
            raise SystemExit("pip install playwright (or unset MLX_USE_PLAYWRIGHT)")

        from automation_patterns import playwright_page_from_cdp

        cdp_url = extract_cdp_url(session)
        target = os.getenv("MLX_SMOKE_URL", "https://example.com")
        with sync_playwright() as playwright:
            browser, page = playwright_page_from_cdp(playwright, cdp_url)
            page.goto(target, wait_until="domcontentloaded")
            print(f"  [{label}] {page.title()} @ {page.url}")
        return

    port = extract_debug_port(session)
    print(f"  [{label}] working on debug port {port} ...")
    time.sleep(float(os.getenv("MLX_ROTATION_DELAY_SEC", "3")))


def main() -> None:
    load_env(Path(__file__).resolve().parents[2] / ".env")
    profiles_path = Path(
        os.getenv("MLX_PROFILES_JSON", Path(__file__).with_name("profiles.example.json"))
    )
    data = json.loads(profiles_path.read_text(encoding="utf-8"))
    profiles = data.get("profiles", [])
    if not profiles:
        raise SystemExit(f"No profiles in {profiles_path}")

    client = MlxLauncherClient()
    for entry in profiles:
        label = entry.get("label", entry["profile_id"])
        folder_id = entry["folder_id"]
        profile_id = entry["profile_id"]
        print(f"\n=== {label} ===")

        with client.profile_session(folder_id, profile_id, automation_type="puppeteer") as session:
            run_job(label, session)

    print("\nRotation complete.")


if __name__ == "__main__":
    main()
