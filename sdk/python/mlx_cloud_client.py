"""
Multilogin X Cloud API client (Profile Access + refresh).
Launcher start/stop remains in mlx_client.py — use both when needed.
"""
from __future__ import annotations

import json
import os
from typing import Any

import requests

DEFAULT_CLOUD_BASE = "https://api.multilogin.com"


class MlxCloudClient:
    """HTTP client for MLX Cloud API (Bearer auth)."""

    def __init__(
        self,
        base_url: str | None = None,
        bearer_token: str | None = None,
        timeout: int = 60,
    ) -> None:
        self.base_url = (base_url or os.getenv("MLX_CLOUD_BASE", DEFAULT_CLOUD_BASE)).rstrip("/")
        self.bearer_token = bearer_token or os.getenv("MLX_BEARER_TOKEN")
        self.timeout = timeout

    def _headers(self, json_body: bool = False) -> dict[str, str]:
        headers = {"Accept": "application/json"}
        if json_body:
            headers["Content-Type"] = "application/json"
        if self.bearer_token:
            headers["Authorization"] = f"Bearer {self.bearer_token}"
        return headers

    def _request(self, method: str, path: str, body: Any | None = None) -> dict[str, Any]:
        url = f"{self.base_url}{path}"
        kwargs: dict[str, Any] = {
            "method": method,
            "url": url,
            "headers": self._headers(json_body=body is not None),
            "timeout": self.timeout,
        }
        if body is not None:
            kwargs["json"] = body
        response = requests.request(**kwargs)
        response.raise_for_status()
        if not response.content:
            return {}
        return response.json()

    def refresh_token(self, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Refresh bearer token (~30 min lifetime).
        Body shape varies — see live Postman Profile Access Management.
        """
        return self._request("POST", "/user/refresh_token", payload or {})

    def search_profiles(
        self,
        *,
        limit: int = 100,
        offset: int = 0,
        search_text: str = "",
        folder_id: str | None = None,
        is_removed: bool = False,
        extra: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        POST /profile/search — list profiles in workspace (cloud).
        See Postman Profile Management for full body fields.
        """
        body: dict[str, Any] = {
            "is_removed": is_removed,
            "limit": limit,
            "offset": offset,
            "search_text": search_text,
        }
        if folder_id:
            body["folder_id"] = folder_id
        if extra:
            body.update(extra)
        return self._request("POST", "/profile/search", body)

    def get(self, path: str) -> dict[str, Any]:
        return self._request("GET", path)

    def post(self, path: str, body: dict[str, Any]) -> dict[str, Any]:
        return self._request("POST", path, body)


if __name__ == "__main__":
    from mlx_env import load_env

    load_env()
    client = MlxCloudClient()
    if not client.bearer_token:
        raise SystemExit("Set MLX_BEARER_TOKEN in sdk/.env (see docs/token-and-ids.md)")
    print(json.dumps(client.refresh_token(), indent=2))
