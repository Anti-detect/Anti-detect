"""
Recipe 08 — Selenium attach to MLX-launched browser.

Real use: teams already on Selenium/WebDriver who want MLX fingerprints.
Requires: pip install selenium + matching ChromeDriver on PATH (or Selenium 4.6+ manager).
Start profile with automation_type=selenium.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from automation_patterns import connect_selenium_chrome, human_pause
from mlx_client import MlxLauncherClient
from mlx_env import load_env


def automate(driver) -> None:
    target = os.getenv("MLX_SMOKE_URL", "https://example.com")
    driver.get(target)
    human_pause()
    print(f"Title: {driver.title}")


def main() -> None:
    load_env(Path(__file__).resolve().parents[2] / ".env")
    client = MlxLauncherClient()
    folder_id = os.environ["MLX_FOLDER_ID"]
    profile_id = os.environ["MLX_PROFILE_ID"]

    try:
        with client.profile_session(
            folder_id,
            profile_id,
            automation_type="selenium",
            headless_mode=os.getenv("MLX_HEADLESS", "false").lower() in ("1", "true", "yes"),
        ) as session:
            driver = connect_selenium_chrome(session)
            try:
                automate(driver)
            finally:
                driver.quit()
    except ImportError:
        print("pip install selenium")
        sys.exit(1)

    print("Profile stopped.")


if __name__ == "__main__":
    main()
