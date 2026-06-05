#!/usr/bin/env python3
"""Validate docs/multilogin-api/spec consistency."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "docs" / "multilogin-api" / "spec"
META_PATH = SPEC / "postman-collection-meta.json"
LAUNCHER_PATH = SPEC / "launcher-endpoints.json"
SAMPLES_ROOT = SPEC / "code-samples"


def fail(message: str) -> int:
    print(f"[spec-integrity] ERROR: {message}")
    return 1


def main() -> int:
    if not META_PATH.is_file():
        return fail(f"Missing {META_PATH}")
    if not LAUNCHER_PATH.is_file():
        return fail(f"Missing {LAUNCHER_PATH}")

    meta = json.loads(META_PATH.read_text(encoding="utf-8"))
    launcher = json.loads(LAUNCHER_PATH.read_text(encoding="utf-8"))
    meta_endpoints = meta.get("endpoints", [])
    meta_by_id = {ep.get("id"): ep for ep in meta_endpoints}
    launcher_ids = set()

    for ep in launcher:
        ep_id = ep.get("id")
        if not ep_id:
            return fail("launcher-endpoints.json contains endpoint without id")
        launcher_ids.add(ep_id)
        if ep_id not in meta_by_id:
            return fail(f"launcher endpoint id '{ep_id}' missing from postman-collection-meta.json")
        meta_ep = meta_by_id[ep_id]
        for field in ("method", "path", "name"):
            if ep.get(field) != meta_ep.get(field):
                return fail(
                    f"Mismatch for endpoint '{ep_id}' field '{field}': "
                    f"launcher={ep.get(field)!r} meta={meta_ep.get(field)!r}"
                )

    launcher_meta_ids = {ep.get("id") for ep in meta_endpoints if ep.get("surface") == "launcher"}
    if launcher_ids != launcher_meta_ids:
        missing = sorted(launcher_meta_ids - launcher_ids)
        extra = sorted(launcher_ids - launcher_meta_ids)
        return fail(f"launcher endpoint sets differ (missing={missing}, extra={extra})")

    exports = meta.get("exports", [])
    if not exports:
        return fail("postman-collection-meta.json has no exports")

    for export in exports:
        language = export.get("language")
        variant = str(export.get("variant", "")).replace(".", "_")
        export_label = f"{language}/{variant}"
        if not language or not variant:
            return fail(f"Invalid export entry: {export}")
        sample_dir = SAMPLES_ROOT / language / variant
        if not sample_dir.is_dir():
            return fail(f"Missing sample folder for {export_label}: {sample_dir}")

        listed_files = {sample.get("file") for sample in export.get("samples", [])}
        if not listed_files:
            return fail(f"No sample files listed in metadata for {export_label}")

        existing_files = {p.name for p in sample_dir.glob("block_*")}
        missing_files = sorted(listed_files - existing_files)
        extra_files = sorted(existing_files - listed_files)
        if missing_files:
            return fail(f"{export_label} missing files from disk: {missing_files}")
        if extra_files:
            return fail(f"{export_label} has untracked files on disk: {extra_files}")

        index_path = sample_dir / "index.json"
        if not index_path.is_file():
            return fail(f"Missing index.json for {export_label}")

    print("[spec-integrity] OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
