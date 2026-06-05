"""
Recipe 12a — Export cloud profile search → profiles.json for rotation.

Requires MLX_BEARER_TOKEN. Does not start browsers.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mlx_cloud_client import MlxCloudClient
from mlx_env import load_env
from profile_catalog import profiles_from_search_response


def main() -> None:
    load_env(Path(__file__).resolve().parents[2] / ".env")
    if not os.getenv("MLX_BEARER_TOKEN"):
        raise SystemExit("Set MLX_BEARER_TOKEN in sdk/.env (see docs/token-and-ids.md)")

    client = MlxCloudClient()
    limit = int(os.getenv("MLX_SEARCH_LIMIT", "100"))
    offset = int(os.getenv("MLX_SEARCH_OFFSET", "0"))
    search_text = os.getenv("MLX_SEARCH_TEXT", "")
    folder_id = os.getenv("MLX_FOLDER_ID") if os.getenv("MLX_SEARCH_FOLDER") else None

    result = client.search_profiles(
        limit=limit,
        offset=offset,
        search_text=search_text,
        folder_id=folder_id,
    )
    profiles = profiles_from_search_response(result)
    if not profiles:
        print("No profiles parsed — check token and search filters.")
        print(json.dumps(result, indent=2)[:2000])
        sys.exit(1)

    out = Path(os.getenv("MLX_PROFILES_JSON", Path(__file__).with_name("profiles.json")))
    out.write_text(json.dumps({"profiles": profiles}, indent=2), encoding="utf-8")
    print(f"Wrote {len(profiles)} profile(s) → {out}")


if __name__ == "__main__":
    main()
