#!/usr/bin/env python3
"""
Parse Postman HTML exports OR refresh spec/parsed-index.json from spec archive.
Prefer docs/multilogin-api/spec/ — API-HTML/ is optional input for re-archive only.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API_DIR = ROOT / "API-HTML"
SPEC = ROOT / "docs" / "multilogin-api" / "spec"
META = SPEC / "postman-collection-meta.json"

METHOD_NAME = re.compile(
    r'<span class="sc-fzoaKM diFeSb">(GET|POST|PUT|DELETE|PATCH)</span>'
    r'<span class="sc-fzomuh[^"]*">([^<]+)</span>'
)
METHOD_NAME_ALT = re.compile(r"documentation-cor[^>]*>([^<]+)</span>")
FOLDERS = re.compile(r'<div class="sc-fzqMAW jYXJBZ">([^<]+)</div></h2>')
PATHS = re.compile(r'"(/api/[^"]+)"')
HOSTS = re.compile(r"(api\.multilogin\.com|launcher\.mlx\.yt)")


def parse_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="ignore")
    endpoints = METHOD_NAME.findall(text)
    names_alt = METHOD_NAME_ALT.findall(text)
    seen = {(m, n.strip()) for m, n in endpoints}
    ep_list = [{"method": m, "name": n} for m, n in seen]
    if not ep_list and names_alt:
        ep_list = [{"method": "?", "name": n.strip()} for n in dict.fromkeys(names_alt)]
    return {
        "file": path.name,
        "endpoints": ep_list,
        "folders": FOLDERS.findall(text),
        "api_paths": sorted({p.replace("&amp;", "&") for p in PATHS.findall(text)}),
        "hosts": sorted(set(HOSTS.findall(text))),
    }


def from_spec() -> list[dict]:
    if not META.is_file():
        return []
    meta = json.loads(META.read_text(encoding="utf-8"))
    out = []
    for exp in meta.get("exports", []):
        out.append(
            {
                "file": exp["html_file"],
                "language": exp["language"],
                "variant": exp["variant"],
                "endpoints": [
                    {"method": e["method"], "name": e["name"]}
                    for e in meta.get("endpoints", [])
                    if e.get("surface") == "launcher"
                ],
                "api_paths": exp.get("api_paths_extracted", []),
                "hosts": list(meta.get("bases", {}).values()),
            }
        )
    return out


def main():
    SPEC.mkdir(parents=True, exist_ok=True)
    out_path = SPEC / "parsed-index.json"

    if API_DIR.is_dir() and list(API_DIR.glob("*.html")):
        results = [parse_file(p) for p in sorted(API_DIR.glob("*.html"))]
        print("Parsed from API-HTML/")
    else:
        results = from_spec()
        print("Loaded from spec/ (no API-HTML/*.html)")

    out_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"Wrote {out_path}")
    for r in results:
        print(f"  {r.get('file', r.get('language'))}: {len(r.get('endpoints', []))} endpoints")


if __name__ == "__main__":
    main()
