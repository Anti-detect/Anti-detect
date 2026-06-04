# Getting started

Onboarding for **anti-detect browser automation** and **Multilogin X** — with links to real repositories under [@multilogin-automation](https://github.com/multilogin-automation).

## Path A — New to Multilogin X

1. Open [multilogin-x-getting-started](https://github.com/multilogin-automation/multilogin-x-getting-started) and follow install + first profile launch.
2. Use [multilogin-x-id-token-retrieval-tools](https://github.com/multilogin-automation/multilogin-x-id-token-retrieval-tools) to obtain tokens, profile IDs, and workspace IDs.
3. Clone [multilogin-automation](https://github.com/multilogin-automation/multilogin-automation) and copy from [`templates/`](https://github.com/multilogin-automation/multilogin-automation/tree/main/templates).

## Path B — Python API automation

1. Start with [`templates/mlx_config_template.py`](https://github.com/multilogin-automation/multilogin-automation/blob/main/templates/mlx_config_template.py).
2. Store credentials in environment variables (never commit `.env` with secrets).
3. Confirm Local API / MLX endpoint (commonly port **35000** — verify in your environment docs).
4. Pilot one profile before scaling fleet size.

## Path C — Playwright / Selenium UI automation

1. Launch a profile via MLX API (Path A or B).
2. Integrate [`templates/playwright_stealth.py`](https://github.com/multilogin-automation/multilogin-automation/blob/main/templates/playwright_stealth.py) for stealth hooks.
3. Attach Playwright or Selenium to the browser debugger endpoint returned by the launcher.
4. Run against a staging URL first; watch for Cloudflare/Akamai challenge patterns.

## Path D — Cookie warming

1. [multilogin_x_auto_cookie_collector](https://github.com/multilogin-automation/multilogin_x_auto_cookie_collector) — visit configured sites per profile.
2. [mlx_cookie_robot](https://github.com/multilogin-automation/mlx_cookie_robot) — MLX-focused cookie robot.

## Fingerprint pre-flight

Before scaling profiles, run through [fingerprint-checklist.md](fingerprint-checklist.md) (timezone, WebRTC, Canvas/WebGL, proxy alignment).

## Environment checklist

- [ ] Python 3.10+ or Node LTS (per target repo README)
- [ ] API token / MLX credentials in env vars only
- [ ] Proxy + timezone aligned with profile fingerprint
- [ ] Firewall allows API and browser debug ports
- [ ] One profile per account/tenant where isolation matters

## Multilogin X plans

Commercial **anti-detect browser** capacity: [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — codes **`SAAS50`** / **`MIN50`** ([details](../README.md#multilogin-pricing-reference)).

## Troubleshooting

| Symptom | Check |
|---------|--------|
| 401 / invalid token | Re-run id-token tools; rotate credentials |
| Profile won't start | Proxy health, disk space, MLX agent logs |
| Instant bot block | Fingerprint mismatch (Canvas/WebGL), IP reputation, rate limits |
| Playwright can't connect | Correct CDP/WebSocket URL from launcher |

More: [FAQ](faq.md) · [Glossary](glossary.md) · [Architecture](architecture.md)

## Next steps

- [Open-source catalog](open-source-catalog.md) — full repo list
- [Comparison: anti-detect vs Chrome](comparison-anti-detect-vs-chrome.md)
- [Main README](../README.md)
