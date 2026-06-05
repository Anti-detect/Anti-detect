#!/usr/bin/env python3
"""
Multilogin X CLI — start, stop, smoke, cloud refresh, doctor.

Usage (from repo root or sdk/python):
  python mlx_cli.py start
  python mlx_cli.py stop
  python mlx_cli.py smoke
  python mlx_cli.py refresh
  python mlx_cli.py doctor
  python mlx_cli.py profiles list
  python mlx_cli.py profiles export -o profiles.json
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SDK_ENV = ROOT / "sdk" / ".env"

sys.path.insert(0, str(Path(__file__).resolve().parent))

from mlx_client import MlxLauncherClient  # noqa: E402
from mlx_cloud_client import MlxCloudClient  # noqa: E402
from mlx_env import load_env  # noqa: E402
from mlx_helpers import extract_cdp_url  # noqa: E402
from profile_catalog import profiles_from_search_response  # noqa: E402


def _load_env() -> None:
    load_env(SDK_ENV if SDK_ENV.is_file() else ROOT / "sdk" / "config.example.env")


def cmd_start(args: argparse.Namespace) -> None:
    client = MlxLauncherClient()
    folder = os.environ["MLX_FOLDER_ID"]
    profile = os.environ["MLX_PROFILE_ID"]
    result = client.start_profile(
        folder,
        profile,
        automation_type=args.automation,
        headless_mode=args.headless,
    )
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        try:
            cdp = extract_cdp_url(result)
            print(f"Started {profile}")
            print(f"CDP: {cdp}")
        except ValueError:
            print(json.dumps(result, indent=2))
    if not args.no_stop_hint:
        print("Stop with: python mlx_cli.py stop")


def cmd_stop(args: argparse.Namespace) -> None:
    client = MlxLauncherClient()
    profile = os.environ["MLX_PROFILE_ID"]
    result = client.stop_profile(profile)
    print(json.dumps(result, indent=2) if args.json else f"Stopped {profile}")


def cmd_smoke(_: argparse.Namespace) -> None:
    script = ROOT / "sdk" / "python" / "recipes" / "05_headless_smoke.py"
    subprocess.run([sys.executable, str(script)], check=True)


def cmd_refresh(args: argparse.Namespace) -> None:
    client = MlxCloudClient()
    if not client.bearer_token:
        raise SystemExit("Set MLX_BEARER_TOKEN in sdk/.env")
    result = client.refresh_token()
    print(json.dumps(result, indent=2) if args.json else result)


def cmd_doctor(_: argparse.Namespace) -> None:
    script = ROOT / "scripts" / "mlx-doctor.py"
    subprocess.run([sys.executable, str(script)], check=True)


def _cloud_client_or_exit() -> MlxCloudClient:
    client = MlxCloudClient()
    if not client.bearer_token:
        raise SystemExit("Set MLX_BEARER_TOKEN in sdk/.env")
    return client


def cmd_profiles_list(args: argparse.Namespace) -> None:
    client = _cloud_client_or_exit()
    result = client.search_profiles(
        limit=args.limit,
        offset=args.offset,
        search_text=args.search_text,
        folder_id=args.folder_id,
    )
    profiles = profiles_from_search_response(result)
    if args.json:
        print(json.dumps({"profiles": profiles}, indent=2))
        return
    if not profiles:
        print("No profiles matched.")
        return
    for row in profiles:
        print(f"{row['label']}\t{row['folder_id']}\t{row['profile_id']}")


def cmd_profiles_export(args: argparse.Namespace) -> None:
    client = _cloud_client_or_exit()
    result = client.search_profiles(
        limit=args.limit,
        offset=args.offset,
        search_text=args.search_text,
        folder_id=args.folder_id,
    )
    profiles = profiles_from_search_response(result)
    if not profiles:
        raise SystemExit("No profiles parsed from cloud search — check token and filters.")
    out = Path(args.output)
    out.write_text(json.dumps({"profiles": profiles}, indent=2), encoding="utf-8")
    print(f"Wrote {len(profiles)} profile(s) → {out}")


def main() -> None:
    _load_env()
    parser = argparse.ArgumentParser(description="Multilogin X Launcher CLI")
    parser.add_argument("--json", action="store_true", help="Print raw JSON responses")
    sub = parser.add_subparsers(dest="command", required=True)

    start_p = sub.add_parser("start", help="Start saved profile")
    start_p.add_argument("--automation", default=os.getenv("MLX_AUTOMATION_TYPE", "puppeteer"))
    start_p.add_argument("--headless", action="store_true")
    start_p.add_argument("--no-stop-hint", action="store_true")
    start_p.set_defaults(func=cmd_start)

    stop_p = sub.add_parser("stop", help="Stop saved profile")
    stop_p.set_defaults(func=cmd_stop)

    smoke_p = sub.add_parser("smoke", help="Run headless smoke recipe")
    smoke_p.set_defaults(func=cmd_smoke)

    refresh_p = sub.add_parser("refresh", help="Refresh cloud bearer token")
    refresh_p.set_defaults(func=cmd_refresh)

    doctor_p = sub.add_parser("doctor", help="Run mlx-doctor setup checks")
    doctor_p.set_defaults(func=cmd_doctor)

    profiles_p = sub.add_parser("profiles", help="Cloud profile search")
    profiles_sub = profiles_p.add_subparsers(dest="profiles_cmd", required=True)

    def _add_search_flags(p: argparse.ArgumentParser) -> None:
        p.add_argument("--limit", type=int, default=int(os.getenv("MLX_SEARCH_LIMIT", "100")))
        p.add_argument("--offset", type=int, default=int(os.getenv("MLX_SEARCH_OFFSET", "0")))
        p.add_argument("--search-text", default=os.getenv("MLX_SEARCH_TEXT", ""))
        p.add_argument(
            "--folder-id",
            default=os.getenv("MLX_FOLDER_ID") if os.getenv("MLX_SEARCH_FOLDER") else None,
        )

    list_p = profiles_sub.add_parser("list", help="Print profiles (TSV)")
    _add_search_flags(list_p)
    list_p.set_defaults(func=cmd_profiles_list)

    export_p = profiles_sub.add_parser("export", help="Write profiles.json for rotation")
    _add_search_flags(export_p)
    export_p.add_argument(
        "-o",
        "--output",
        default=os.getenv("MLX_PROFILES_JSON", "profiles.json"),
    )
    export_p.set_defaults(func=cmd_profiles_export)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
