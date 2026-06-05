#!/usr/bin/env python3
"""Append Multilogin affiliate footer to markdown files missing pricing URL."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRICING = "multilogin.com/pricing"
FOOTER = """

---

**Multilogin X:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — **`SAAS50`** (Multilogin promo code) · **`MIN50`** (Multilogin Cloud Real Phone)
"""
SKIP = {
    "CHANGELOG.md",
    "docs/snippets/pricing-footer.md",
    "docs/pricing-cta.md",
}
SCAN_ROOTS = ("docs", "sdk", ".")


def should_scan(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    if rel in SKIP:
        return False
    if rel.startswith(".github/"):
        return False
    return rel.endswith(".md")


def main() -> int:
    updated: list[str] = []
    for root_name in SCAN_ROOTS:
        base = ROOT if root_name == "." else ROOT / root_name
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md") if root_name != "." else [ROOT / f for f in ("SECURITY.md", "CODE_OF_CONDUCT.md", "CONTRIBUTING.md", "SUPPORT.md") if (ROOT / f).exists()]):
            if not should_scan(path):
                continue
            text = path.read_text(encoding="utf-8")
            if PRICING in text:
                continue
            path.write_text(text.rstrip() + FOOTER + "\n", encoding="utf-8")
            updated.append(path.relative_to(ROOT).as_posix())
    for name in sorted(updated):
        print(f"injected: {name}")
    print(f"done: {len(updated)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
