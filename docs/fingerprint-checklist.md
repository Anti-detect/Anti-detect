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
- [ ] [`playwright_stealth.py`](https://github.com/multilogin-automation/multilogin-automation/blob/main/templates/playwright_stealth.py) hooks applied where needed

## Behavior (anti-bot)

- [ ] Human-like delays between actions
- [ ] Cookie warming completed for cold profiles ([cookie tools](open-source-catalog.md#cookie--proxy-utilities))
- [ ] Rate limits respected per platform ToS

## Before go-live

- [ ] One profile pilot on staging URL
- [ ] Logs redact tokens and profile IDs in shared channels
- [ ] Rollback plan if block rate spikes

## Related

- [Comparison: anti-detect vs Chrome](comparison-anti-detect-vs-chrome.md)
- [Glossary](glossary.md)
- [FAQ](faq.md)
