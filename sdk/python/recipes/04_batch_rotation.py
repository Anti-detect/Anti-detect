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
from mlx_helpers import extract_debug_port


def run_job(label: str, debug_port: int | None) -> None:
    """Replace with Playwright attach or Selenium — placeholder shows rotation timing."""
    print(f"  [{label}] working on debug port {debug_port} ...")
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
            port = extract_debug_port(session)
            run_job(label, port)

    print("\nRotation complete.")


if __name__ == "__main__":
    main()
