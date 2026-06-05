# Browser fingerprint checklist (MLX fleets)

Operational checklist before scaling **anti-detect browser** automation on **Multilogin X**. Complements [architecture.md](architecture.md) and [getting-started.md](getting-started.md).

## Per-profile consistency

| Signal | Check |
|--------|--------|
| Timezone | Matches proxy geo and locale |
| Language / Accept-Language | Aligns with profile country |
| User-Agent + Client Hints | Same “device story” as OS/GPU |
| Screen resolution | Not identical across entire fleet unless intentional |
| WebRTC | No leak of real IP when proxy required |
| Canvas / WebGL | Unique or intentionally varied per profile |
| Fonts | Stable per profile; avoid random drift mid-campaign |

## Network

- [ ] Residential or mobile proxy quality matches target platform risk
- [ ] DNS does not expose home ISP when using datacenter proxy
- [ ] Sticky session for login flows; rotate only when planned

## Automation attach

- [ ] Profile launched via MLX API / launcher (not raw Chrome for production)
- [ ] Playwright/Selenium connects to launcher CDP/WebSocket URL
- [ ] Playwright attach via [Recipe 02](multilogin-api/cookbook/02-playwright-attach.md); human delays in [automation_patterns.py](../sdk/python/automation_patterns.py)

## Behavior (anti-bot)

- [ ] Human-like delays between actions
- [ ] Cold profiles warmed with realistic browsing before high-risk flows ([mmo-automation-guide.md](mmo-automation-guide.md))
- [ ] Rate limits respected per platform ToS

## Before go-live

- [ ] One profile pilot on staging URL
- [ ] Logs redact tokens and profile IDs in shared channels
- [ ] Rollback plan if block rate spikes

## Related

- [Comparison: anti-detect vs Chrome](comparison-anti-detect-vs-chrome.md)
- [Glossary](glossary.md)
- [FAQ](faq.md)
