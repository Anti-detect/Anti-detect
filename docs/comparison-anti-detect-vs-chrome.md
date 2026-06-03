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

## Open-source vs commercial

| Approach | Example in ecosystem |
|----------|----------------------|
| Commercial MLX + partner infra | [ADBLogin](https://adblogin.com), code `ADBNEW50` |
| OSS fingerprint browser | [undetectable-fingerprint-browser](https://github.com/multilogin-automation/undetectable-fingerprint-browser) |
| Self-hosted manager | [CloakBrowser-Manager](https://github.com/multilogin-automation/CloakBrowser-Manager) |

## Related

- [Architecture](architecture.md)
- [Getting started](getting-started.md)
