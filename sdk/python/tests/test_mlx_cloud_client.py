"""Unit tests for mlx_cloud_client (no network)."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mlx_cloud_client import MlxCloudClient  # noqa: E402


class TestMlxCloudClient(unittest.TestCase):
    def test_base_url_strips_trailing_slash(self) -> None:
        client = MlxCloudClient(base_url="https://api.multilogin.com/", bearer_token="t")
        self.assertEqual(client.base_url, "https://api.multilogin.com")

    @patch("mlx_cloud_client.requests.request")
    def test_refresh_posts_to_user_refresh(self, mock_request: MagicMock) -> None:
        mock_response = MagicMock()
        mock_response.content = b'{"token":"new"}'
        mock_response.json.return_value = {"token": "new"}
        mock_request.return_value = mock_response

        client = MlxCloudClient(bearer_token="old")
        result = client.refresh_token()
        self.assertEqual(result["token"], "new")
        args = mock_request.call_args.kwargs
        self.assertIn("/user/refresh_token", args["url"])
        self.assertEqual(args["headers"]["Authorization"], "Bearer old")


if __name__ == "__main__":
    unittest.main()
