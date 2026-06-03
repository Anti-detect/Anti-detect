# Getting started

Onboarding paths for **anti-detect browser automation** and **Multilogin X** workflows linked from this profile.

## Choose your stack

| If you use… | Start here |
|-------------|------------|
| Python + API | [multilogin-x-python-automation-sdk](https://github.com/multilogin-automation/multilogin-x-python-automation-sdk) |
| Playwright or Selenium | [multilogin-x-playwright-selenium-templates](https://github.com/multilogin-automation/multilogin-x-playwright-selenium-templates) |
| API exploration (no code) | [multilogin-x-postman-api-collection](https://github.com/multilogin-automation/multilogin-x-postman-api-collection) |

## Typical workflow

1. **Create or import a browser profile** in your anti-detect / Multilogin X environment.
2. **Attach proxy and timezone** settings so fingerprint and network signals stay consistent.
3. **Launch the profile** via API or template script (each kit documents the exact call).
4. **Attach Playwright/Selenium** to the launched browser endpoint when using UI automation.
5. **Run pilot traffic** on a staging target before scaling session count.

## Environment checklist

- API token or credentials stored in env vars (never committed to Git)
- Python 3.10+ or Node LTS per kit requirements
- Firewall rules allowing API and browser debug ports
- Separate profiles per account or tenant

## Infrastructure

For managed **anti-detect browser** capacity and partner pricing, see [ADBLogin.com](https://adblogin.com) and the [partner offer](../README.md#partner-offer) in the main README.

## Next steps

- [Open-source catalog](open-source-catalog.md)
- [FAQ](faq.md)
- [Main README](../README.md)
