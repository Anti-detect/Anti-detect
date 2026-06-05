"""
Recipe 05 — Headless smoke test before scaling a fleet.

Real use: CI or pre-flight check that launcher + profile + CDP path still works.
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

    def smoke() -> None:
        with client.profile_session(
            folder_id,
            profile_id,
            automation_type="puppeteer",
            headless_mode=True,
        ) as session:
            cdp_url = extract_cdp_url(session)
            print(f"SMOKE OK — headless CDP at {cdp_url}")

    retry(smoke, attempts=3, on_retry=lambda n, e: print(f"Smoke retry {n}: {e}"))


if __name__ == "__main__":
    main()
