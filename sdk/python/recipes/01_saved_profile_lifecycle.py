"""
Recipe 01 — Saved profile lifecycle (start → inspect → stop).

Real use: daily automation on a persistent MLX profile (cookies, logins kept).
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mlx_client import MlxLauncherClient
from mlx_env import load_env
from mlx_helpers import extract_cdp_url, extract_debug_port, retry


def main() -> None:
    load_env(Path(__file__).resolve().parents[2] / ".env")
    client = MlxLauncherClient()
    folder_id = os.environ["MLX_FOLDER_ID"]
    profile_id = os.environ["MLX_PROFILE_ID"]

    def start() -> dict:
        with client.profile_session(folder_id, profile_id, automation_type="puppeteer") as session:
            port = extract_debug_port(session)
            cdp = extract_cdp_url(session)
            print(f"Profile {profile_id} running")
            print(f"  debug port: {port}")
            print(f"  CDP URL:    {cdp}")
            print("  → attach Playwright/Selenium here, or run recipe 02")
            return session

    retry(start, attempts=3, on_retry=lambda n, e: print(f"Retry {n}: {e}"))


if __name__ == "__main__":
    main()
