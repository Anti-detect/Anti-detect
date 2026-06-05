# MMO & multi-account automation guide

Patterns for **MMO account management** and **multi-account browser** workflows on **Multilogin X** — using recipes in this repo.

> Comply with each platform's terms of service.

## Why anti-detect browsers for MMO

| Risk | Mitigation |
|------|------------|
| Linked fingerprints | One MLX profile per account |
| Shared cookies | Isolated profile storage |
| IP/geo mismatch | Proxy per profile + timezone alignment |
| Bot detection | Playwright attach + human-like delays |

## Recommended stack (this repo)

1. **Onboarding** — [getting-started.md](getting-started.md)
2. **Profile UUIDs** — [token-and-ids.md](token-and-ids.md)
3. **Rotation** — [Recipe 04](../sdk/python/recipes/04_batch_rotation.py) + [cookbook/04](multilogin-api/cookbook/04-multi-account-rotation.md)
4. **Login flows** — [Recipe 07](../sdk/python/recipes/07_login_flow.py)
5. **Pre-flight** — [fingerprint-checklist.md](fingerprint-checklist.md)

## Operational rules

- Never share one profile across unrelated accounts.
- Rotate proxies deliberately; avoid mid-session IP jumps.
- Pilot on 2–3 profiles before fleet scale.
- Redact tokens in logs.

## Pricing

**SAAS50** / **MIN50** on [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — [urls.md](urls.md).

## Related

- [browser-landscape.md](browser-landscape.md)
- [faq.md](faq.md)
