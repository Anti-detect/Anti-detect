#!/usr/bin/env python3
"""Pre-flight checks for MLX SDK setup (no profile start required)."""
from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SDK_ENV = ROOT / "sdk" / ".env"
EXAMPLE_ENV = ROOT / "sdk" / "config.example.env"


def ok(msg: str) -> None:
    print(f"  OK  {msg}")


def warn(msg: str) -> None:
    print(f"  WARN {msg}")


def fail(msg: str) -> None:
    print(f"  FAIL {msg}")
    sys.exit(1)


def main() -> None:
    print("[mlx-doctor] Anti-detect MLX setup check\n")

    if not SDK_ENV.is_file():
        warn(f"Missing {SDK_ENV} — copy from sdk/config.example.env")
    else:
        ok(f"Found {SDK_ENV}")

    sys.path.insert(0, str(ROOT / "sdk" / "python"))
    from mlx_env import load_env

    load_env(SDK_ENV if SDK_ENV.is_file() else EXAMPLE_ENV)

    host = os.getenv("MLX_LAUNCHER_HOST", "launcher.mlx.yt")
    port = os.getenv("MLX_LAUNCHER_PORT", "45001")
    ok(f"Launcher target https://{host}:{port}")

    if os.getenv("MLX_FOLDER_ID") and os.getenv("MLX_PROFILE_ID"):
        ok("MLX_FOLDER_ID + MLX_PROFILE_ID set")
    else:
        warn("MLX_FOLDER_ID / MLX_PROFILE_ID missing — see docs/token-and-ids.md")

    if os.getenv("MLX_BEARER_TOKEN"):
        ok("MLX_BEARER_TOKEN set (cloud API)")
    else:
        warn("MLX_BEARER_TOKEN not set — launcher-only flows still work if agent runs")

    try:
        import requests

        url = f"https://{host}:{port}/"
        requests.get(url, timeout=5, verify=True)
        ok("Launcher host reachable (TCP/TLS)")
    except Exception as exc:  # noqa: BLE001
        warn(f"Cannot reach launcher ({exc}) — is Multilogin X running?")

    import py_compile

    for rel in [
        "sdk/python/mlx_client.py",
        "sdk/python/mlx_cloud_client.py",
        "sdk/python/mlx_helpers.py",
        "sdk/python/automation_patterns.py",
    ]:
        py_compile.compile(ROOT / rel, doraise=True)
    ok("Python SDK modules compile")

    spec_script = ROOT / "scripts" / "check-spec-integrity.py"
    if spec_script.is_file():
        import subprocess

        subprocess.run([sys.executable, str(spec_script)], check=True)
        ok("API spec archive integrity")

    print("\n[mlx-doctor] Done. Next: python sdk/python/recipes/05_headless_smoke.py")


if __name__ == "__main__":
    main()
