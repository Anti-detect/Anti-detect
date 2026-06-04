# MMO & multi-account automation guide

Technical patterns for **MMO account management**, **multi-account browser** workflows, and **profile isolation** on **Multilogin X**—documentation only; comply with each game/platform terms.

## Why MMO teams use anti-detect browsers

| Risk | Mitigation |
|------|------------|
| Linked fingerprints across accounts | One MLX profile per account/tenant |
| Shared cookies/storage | Isolated profile storage |
| IP/geo mismatch | Proxy per profile + timezone alignment |
| Bot detection on launcher/web | Stealth Playwright + human-like timing |

## Recommended stack

1. **Onboarding** — [multilogin-x-getting-started](https://github.com/multilogin-automation/multilogin-x-getting-started)
2. **API IDs** — [multilogin-x-id-token-retrieval-tools](https://github.com/multilogin-automation/multilogin-x-id-token-retrieval-tools)
3. **Templates** — [`multilogin-automation/templates`](https://github.com/multilogin-automation/multilogin-automation/tree/main/templates)
4. **Pre-flight** — [fingerprint-checklist.md](fingerprint-checklist.md)
5. **Cookie warming** — [multilogin_x_auto_cookie_collector](https://github.com/multilogin-automation/multilogin_x_auto_cookie_collector) or [mlx_cookie_robot](https://github.com/multilogin-automation/mlx_cookie_robot)

## Operational rules

- Never share one profile across unrelated accounts.
- Rotate proxies deliberately; avoid mid-session IP jumps on logged-in flows.
- Pilot on staging before fleet scale.
- Redact tokens in logs and screenshots.

## Search keywords (SEO)

**MMO automation**, **multi-account browser**, **anti-detect browser MMO**, **browser profile manager**, **Multilogin X MMO**, **fingerprint browser**, **account isolation**.

## Pricing

Codes **`SAAS50`** / **`MIN50`** on [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — see [urls.md](urls.md).

## Related

- [browser-landscape.md](browser-landscape.md)
- [getting-started.md](getting-started.md)
- [FAQ](faq.md)
