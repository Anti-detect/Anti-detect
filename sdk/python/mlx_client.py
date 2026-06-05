"""
Thin Multilogin X Local Launcher client (requests).
Derived from Postman spec archive — Launcher folder.
"""
from __future__ import annotations

import json
import os
from contextlib import contextmanager
from typing import Any, Iterator
from urllib.parse import urlencode

import requests

DEFAULT_HOST = "launcher.mlx.yt"
DEFAULT_PORT = 45001


class MlxLauncherClient:
    """HTTP client for MLX Local Launcher API."""

    def __init__(
        self,
        host: str | None = None,
        port: int | str | None = None,
        bearer_token: str | None = None,
        timeout: int = 120,
    ) -> None:
        self.host = host or os.getenv("MLX_LAUNCHER_HOST", DEFAULT_HOST)
        self.port = int(port or os.getenv("MLX_LAUNCHER_PORT", DEFAULT_PORT))
        self.bearer_token = bearer_token or os.getenv("MLX_BEARER_TOKEN")
        self.timeout = timeout
        self._base = f"https://{self.host}:{self.port}"

    def _headers(self, json_body: bool = False) -> dict[str, str]:
        headers = {"Accept": "application/json"}
        if json_body:
            headers["Content-Type"] = "application/json"
        if self.bearer_token:
            headers["Authorization"] = f"Bearer {self.bearer_token}"
        return headers

    def _request(self, method: str, path: str, body: Any | None = None) -> dict[str, Any]:
        url = f"{self._base}{path}"
        kwargs: dict[str, Any] = {
            "method": method,
            "url": url,
            "headers": self._headers(json_body=body is not None),
            "timeout": self.timeout,
        }
        if body is not None:
            kwargs["data"] = json.dumps(body)
        response = requests.request(**kwargs)
        response.raise_for_status()
        return response.json()

    def start_profile(
        self,
        folder_id: str,
        profile_id: str,
        automation_type: str = "puppeteer",
        headless_mode: bool = False,
    ) -> dict[str, Any]:
        qs = urlencode(
            {
                "automation_type": automation_type,
                "headless_mode": str(headless_mode).lower(),
            }
        )
        path = f"/api/v2/profile/f/{folder_id}/p/{profile_id}/start?{qs}"
        return self._request("GET", path)

    def stop_profile(self, profile_id: str) -> dict[str, Any]:
        return self._request("GET", f"/api/v1/profile/stop/p/{profile_id}")

    def quick_profile_v2(self, payload: dict[str, Any]) -> dict[str, Any]:
        return self._request("POST", "/api/v2/profile/quick", payload)

    def quick_profile_v3(self, payload: dict[str, Any]) -> dict[str, Any]:
        return self._request("POST", "/api/v3/profile/quick", payload)

    @contextmanager
    def profile_session(
        self,
        folder_id: str,
        profile_id: str,
        automation_type: str = "puppeteer",
        headless_mode: bool = False,
    ) -> Iterator[dict[str, Any]]:
        """Start a saved profile and always stop it on exit (success or error)."""
        result = self.start_profile(
            folder_id,
            profile_id,
            automation_type=automation_type,
            headless_mode=headless_mode,
        )
        try:
            yield result
        finally:
            self.stop_profile(profile_id)


if __name__ == "__main__":
    from mlx_env import load_env

    load_env()
    client = MlxLauncherClient()
    folder = os.environ["MLX_FOLDER_ID"]
    profile = os.environ["MLX_PROFILE_ID"]
    print(client.start_profile(folder, profile))
