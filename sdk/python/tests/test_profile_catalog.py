"""Unit tests for profile_catalog (no network)."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from profile_catalog import profiles_from_search_response, shard_profiles  # noqa: E402


class TestProfileCatalog(unittest.TestCase):
    def test_profiles_from_data_profiles(self) -> None:
        resp = {
            "data": {
                "profiles": [
                    {"id": "p1", "folder_id": "f1", "name": "Shop A"},
                    {"profile_id": "p2", "folderId": "f2", "label": "Shop B"},
                ]
            }
        }
        rows = profiles_from_search_response(resp)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["profile_id"], "p1")
        self.assertEqual(rows[0]["label"], "Shop A")

    def test_shard_even_split(self) -> None:
        profiles = [{"profile_id": str(i)} for i in range(4)]
        w0 = shard_profiles(profiles, 0, 2)
        w1 = shard_profiles(profiles, 1, 2)
        self.assertEqual([p["profile_id"] for p in w0], ["0", "2"])
        self.assertEqual([p["profile_id"] for p in w1], ["1", "3"])

    def test_shard_single_worker(self) -> None:
        profiles = [{"profile_id": "a"}, {"profile_id": "b"}]
        self.assertEqual(shard_profiles(profiles, 0, 1), profiles)


if __name__ == "__main__":
    unittest.main()
