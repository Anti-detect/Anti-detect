"""Unit tests for mlx_cloud_client.search_profiles (no network)."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mlx_cloud_client import MlxCloudClient  # noqa: E402


class TestMlxCloudSearch(unittest.TestCase):
    @patch("mlx_cloud_client.requests.request")
    def test_search_posts_profile_search(self, mock_request: MagicMock) -> None:
        mock_response = MagicMock()
        mock_response.content = b'{"data":{"profiles":[]}}'
        mock_response.json.return_value = {"data": {"profiles": []}}
        mock_request.return_value = mock_response

        client = MlxCloudClient(bearer_token="tok")
        client.search_profiles(limit=10, search_text="shop", folder_id="f-1")
        args = mock_request.call_args.kwargs
        self.assertIn("/profile/search", args["url"])
        self.assertEqual(args["json"]["limit"], 10)
        self.assertEqual(args["json"]["search_text"], "shop")
        self.assertEqual(args["json"]["folder_id"], "f-1")


if __name__ == "__main__":
    unittest.main()
