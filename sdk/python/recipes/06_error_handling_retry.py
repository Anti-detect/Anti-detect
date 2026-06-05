"""
Recipe 06 — Retry launcher start when profile is warming or busy.

Demonstrates mlx_helpers.retry around start_profile.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mlx_client import MlxLauncherClient
from mlx_env import load_env
from mlx_helpers import extract_cdp_url, retry


def main() -> None:
    load_env(Path(__file__).resolve().parents[2] / ".env")
    client = MlxLauncherClient()
    folder_id = os.environ["MLX_FOLDER_ID"]
    profile_id = os.environ["MLX_PROFILE_ID"]
    attempts = int(os.getenv("MLX_RETRY_ATTEMPTS", "3"))
    delay = float(os.getenv("MLX_RETRY_DELAY_SEC", "2"))

    def start_once() -> dict:
        return client.start_profile(folder_id, profile_id, automation_type="puppeteer")

    result = retry(start_once, attempts=attempts, delay_seconds=delay)
    cdp = extract_cdp_url(result)
    print(f"Started after retries — CDP: {cdp}")

    client.stop_profile(profile_id)
    print("Profile stopped.")


if __name__ == "__main__":
    main()
