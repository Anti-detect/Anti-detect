# Anti-detect browser vs standard Chrome

Quick comparison for teams evaluating **browser fingerprinting** and **profile isolation**.

| Dimension | Standard Chrome profile | Anti-detect / MLX profile |
|-----------|-------------------------|---------------------------|
| Fingerprint surface | Shared OS + GPU signals across profiles | Per-profile Canvas/WebGL/UA/fonts |
| Storage isolation | Partial (profiles help, same machine tells remain) | Dedicated storage per profile |
| Proxy binding | Manual, easy to misconfigure | Usually first-class per profile |
| Fleet scale | Same fingerprint cluster at scale | Designed for many unique identities |
| Automation attach | Direct launch | Launch via API → attach Playwright/Selenium |
| Ops complexity | Low | Higher — tokens, proxies, warming |
| Best fit | Personal browsing, simple QA | Multi-account, stealth automation, MMO |

## When standard Chrome is enough

- Single account, low volume
- Internal tools without bot protection
- Short-lived manual QA

## When anti-detect is justified

- Many accounts that must not link
- Sites with **anti-bot** + fingerprint scoring
- Long-running sessions needing consistent device story
- Multilogin X or equivalent already in budget

## Commercial MLX + this repo

| Approach | Where |
|----------|--------|
| Multilogin X plans | [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — `SAAS50` / `MIN50` |
| API automation | [sdk/](../sdk/) + [cookbook](multilogin-api/cookbook/) |

## Related

- [Architecture](architecture.md)
- [Getting started](getting-started.md)
