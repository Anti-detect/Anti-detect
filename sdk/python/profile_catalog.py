"""Normalize cloud profile search → rotation JSON."""
from __future__ import annotations

from typing import Any


def profiles_from_search_response(response: dict[str, Any]) -> list[dict[str, str]]:
    """
    Map POST /profile/search JSON to profiles.json rows.

    Handles common MLX shapes: data.profiles, data.items, top-level profiles.
    """
    raw = _extract_profile_list(response)
    out: list[dict[str, str]] = []
    for item in raw:
        if not isinstance(item, dict):
            continue
        profile_id = _first_str(item, "id", "profile_id", "uuid")
        folder_id = _first_str(item, "folder_id", "folderId", "parent_id", "parentId")
        if not profile_id or not folder_id:
            continue
        label = _first_str(item, "name", "label", "title") or profile_id
        out.append(
            {
                "label": label,
                "folder_id": folder_id,
                "profile_id": profile_id,
            }
        )
    return out


def shard_profiles(
    profiles: list[dict[str, Any]],
    worker_id: int,
    worker_count: int,
) -> list[dict[str, Any]]:
    """Split profile list for distributed workers (index % count == worker_id)."""
    if worker_count < 1:
        raise ValueError("worker_count must be >= 1")
    if worker_id < 0 or worker_id >= worker_count:
        raise ValueError(f"worker_id must be 0..{worker_count - 1}")
    if worker_count == 1:
        return list(profiles)
    return [p for i, p in enumerate(profiles) if i % worker_count == worker_id]


def _extract_profile_list(response: dict[str, Any]) -> list[Any]:
    data = response.get("data", response)
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for key in ("profiles", "items", "results", "list"):
            val = data.get(key)
            if isinstance(val, list):
                return val
    for key in ("profiles", "items"):
        val = response.get(key)
        if isinstance(val, list):
            return val
    return []


def _first_str(item: dict[str, Any], *keys: str) -> str | None:
    for key in keys:
        val = item.get(key)
        if val is not None and str(val).strip():
            return str(val).strip()
    return None
