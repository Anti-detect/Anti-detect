"""
Recipe 12b — Distributed rotation via worker sharding.

Each worker runs Recipe 04 logic on its slice of profiles.json.
Run one worker per machine (or terminal) with unique MLX_WORKER_ID.

Example (two machines, same profiles.json):
  Machine A: MLX_WORKER_ID=0 MLX_WORKER_COUNT=2 python 12_parallel_workers.py
  Machine B: MLX_WORKER_ID=1 MLX_WORKER_COUNT=2 python 12_parallel_workers.py
"""
from __future__ import annotations

import importlib.util
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mlx_client import MlxLauncherClient
from mlx_env import load_env
from profile_catalog import shard_profiles

_rotation = Path(__file__).with_name("04_batch_rotation.py")
_spec = importlib.util.spec_from_file_location("batch_rotation", _rotation)
_mod = importlib.util.module_from_spec(_spec)
assert _spec and _spec.loader
_spec.loader.exec_module(_mod)
run_job = _mod.run_job


def main() -> None:
    load_env(Path(__file__).resolve().parents[2] / ".env")
    profiles_path = Path(
        os.getenv("MLX_PROFILES_JSON", Path(__file__).with_name("profiles.example.json"))
    )
    data = json.loads(profiles_path.read_text(encoding="utf-8"))
    all_profiles = data.get("profiles", [])
    if not all_profiles:
        raise SystemExit(f"No profiles in {profiles_path}")

    worker_id = int(os.getenv("MLX_WORKER_ID", "0"))
    worker_count = int(os.getenv("MLX_WORKER_COUNT", "1"))
    profiles = shard_profiles(all_profiles, worker_id, worker_count)
    if not profiles:
        print(f"Worker {worker_id}/{worker_count}: no profiles in shard — exit.")
        return

    print(f"Worker {worker_id}/{worker_count}: {len(profiles)} profile(s) in shard")
    client = MlxLauncherClient()
    for entry in profiles:
        label = entry.get("label", entry["profile_id"])
        folder_id = entry["folder_id"]
        profile_id = entry["profile_id"]
        print(f"\n=== {label} ===")
        with client.profile_session(folder_id, profile_id, automation_type="puppeteer") as session:
            run_job(label, session)

    print(f"\nWorker {worker_id} complete.")


if __name__ == "__main__":
    main()
