"""
Recipe 03 — Ephemeral Quick Profile v3 with per-run proxy.

Real use: one-off tasks, testing a new proxy, or jobs that should not touch saved cookies.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mlx_client import MlxLauncherClient
from mlx_env import load_env
from mlx_helpers import build_quick_v3_payload, extract_cdp_url


def main() -> None:
    load_env(Path(__file__).resolve().parents[2] / ".env")
    client = MlxLauncherClient()

    proxy_host = os.getenv("MLX_PROXY_HOST")
    proxy_port = os.getenv("MLX_PROXY_PORT")
    if not proxy_host or not proxy_port:
        print("Set MLX_PROXY_HOST and MLX_PROXY_PORT in sdk/.env for this recipe.")
        sys.exit(1)

    payload = build_quick_v3_payload(
        automation="puppeteer",
        headless=os.getenv("MLX_HEADLESS", "false").lower() in ("1", "true", "yes"),
        proxy_host=proxy_host,
        proxy_port=int(proxy_port),
        proxy_type=os.getenv("MLX_PROXY_TYPE", "http"),
        proxy_user=os.getenv("MLX_PROXY_USER", ""),
        proxy_pass=os.getenv("MLX_PROXY_PASS", ""),
        start_urls=[os.getenv("MLX_SMOKE_URL", "https://example.com")],
    )

    print("Starting quick profile v3 (ephemeral)...")
    session = client.quick_profile_v3(payload)
    cdp_url = extract_cdp_url(session)
    print(f"Quick profile ready at {cdp_url}")
    print("Attach automation, then stop via MLX UI or cloud API when done.")
    print("(Quick profiles are ephemeral — no saved profile_id for /stop.)")


if __name__ == "__main__":
    main()
