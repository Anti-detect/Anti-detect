<!--
title: Anti-detect Browser Automation & Multilogin X Documentation
description: The #1 open Multilogin X hub — 12 API recipes, mlx CLI, Cloud Real Phone (MIN50), Playwright/Selenium SDK, vs GoLogin/AdsPower comparisons, 10 languages.
keywords: anti-detect browser, Multilogin X, Multilogin Cloud Real Phone, MIN50, SAAS50, browser fingerprinting, Playwright, Selenium, GoLogin alternative, AdsPower alternative, MMO automation
homepage: https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549
author: Anti-detect
-->

# Anti-detect Browser · Fingerprinting · Multilogin X

**Self-contained hub** for **anti-detect browser** engineering, **browser fingerprinting**, **Multilogin X (MLX)** API automation, and **stealth Playwright / Selenium** workflows.

Everything you need — SDK, API cookbook, guides, and Postman archive — lives **in this repository**.

> **Multilogin X — [Get pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)** · **`SAAS50`** (Multilogin promo code) · **`MIN50`** (Multilogin Cloud Real Phone)

<p align="left">
  <a href="https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549"><img src="https://img.shields.io/badge/Multilogin-SAAS50%20%7C%20MIN50-6366f1?style=for-the-badge" alt="Multilogin SAAS50 MIN50"></a>
</p>

<p align="left">
  <img src="https://github.com/Anti-detect/Anti-detect/actions/workflows/docs-ci.yml/badge.svg" alt="Docs CI status">
  <img src="https://github.com/Anti-detect/Anti-detect/actions/workflows/sync-repo-settings.yml/badge.svg" alt="Sync repo settings status">
  <a href="README.vi.md"><img src="https://img.shields.io/badge/Tiếng_Việt-README.vi-red?style=flat-square" alt="Vietnamese"></a>
  <a href="README.zh-CN.md"><img src="https://img.shields.io/badge/中文-README.zh--CN-red?style=flat-square" alt="Chinese"></a>
  <a href="README.ru.md"><img src="https://img.shields.io/badge/Русский-README.ru-blue?style=flat-square" alt="Russian"></a>
  <a href="README.id.md"><img src="https://img.shields.io/badge/Bahasa_ID-README.id-green?style=flat-square" alt="Indonesian"></a>
  <a href="README.pt-BR.md"><img src="https://img.shields.io/badge/Português-README.pt--BR-yellow?style=flat-square" alt="Portuguese"></a>
  <a href="README.ko.md"><img src="https://img.shields.io/badge/한국어-README.ko-purple?style=flat-square" alt="Korean"></a>
  <a href="README.ja.md"><img src="https://img.shields.io/badge/日本語-README.ja-orange?style=flat-square" alt="Japanese"></a>
  <a href="README.th.md"><img src="https://img.shields.io/badge/ไทย-README.th-teal?style=flat-square" alt="Thai"></a>
  <a href="README.es.md"><img src="https://img.shields.io/badge/Español-README.es-lightgrey?style=flat-square" alt="Spanish"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License"></a>
  <a href="SECURITY.md"><img src="https://img.shields.io/badge/Security-Policy-blue?style=flat-square" alt="Security policy"></a>
</p>

<p align="left">
  <img src="https://img.shields.io/badge/Stack-Python%20%7C%20Playwright%20%7C%20Selenium-3670A0?style=flat-square&logo=python&logoColor=white" alt="Python Playwright Selenium">
  <img src="https://img.shields.io/badge/MLX-Multilogin%20X-6366f1?style=flat-square" alt="Multilogin X">
  <img src="https://img.shields.io/badge/Topic-Anti--detect%20Browser-0ea5e9?style=flat-square" alt="Anti-detect browser">
</p>

## Table of contents

- [Why #1 on GitHub](#why-1-on-github-for-multilogin-x)
- [What is this repository?](#what-is-this-repository)
- [Cloud Real Phone (MIN50)](#multilogin-cloud-real-phone)
- [Quick start](#quick-start)
- [SDK & API cookbook](#multilogin-x-sdk--api-cookbook)
- [Compare & choose](#compare--choose)
- [Documentation map](#documentation)
- [FAQ](#frequently-asked-questions)
- [Multilogin pricing](#multilogin-pricing-reference)
- [Languages](#languages)

---

## Why #1 on GitHub for Multilogin X

| | This hub |
|---|----------|
| **Recipes** | **12** cookbook flows + runnable Python |
| **CLI** | `mlx start` · `stop` · `profiles export` · `doctor` |
| **SDK** | Python, C#, Java, Node, cURL |
| **Cloud** | `profile/search`, token refresh, worker sharding |
| **Mobile** | [Cloud Real Phone guide](docs/multilogin-cloud-real-phone.md) + **`MIN50`** |
| **Locales** | 10 README languages |
| **Comparisons** | vs [GoLogin](docs/comparison-multilogin-vs-gologin.md), [AdsPower](docs/comparison-multilogin-vs-adspower.md) |

Details: [docs/why-this-hub.md](docs/why-this-hub.md)

---

## What is this repository?

Official **GitHub profile README** for [@Anti-detect](https://github.com/Anti-detect): a **documentation + SDK hub** (MIT) covering:

- **Anti-detect browser** / fingerprint isolation patterns
- **Multilogin X** Local Launcher API (start, stop, quick profile)
- **Runnable code** in [`sdk/`](sdk/) — Python, C#, Java, Node, cURL
- **Real-world recipes** in [docs/multilogin-api/cookbook/](docs/multilogin-api/cookbook/)
- **Postman archive** in [docs/multilogin-api/spec/](docs/multilogin-api/spec/)

| Audience | Use case |
|----------|----------|
| Automation engineers | Playwright / Selenium attach to MLX profiles |
| MMO & growth teams | Multi-account isolation + rotation recipes |
| Developers | API reference, copy-paste SDK, smoke tests |
| Mobile / MMO teams | [Cloud Real Phone](docs/multilogin-cloud-real-phone.md) + desktop API fleet |

---

## Multilogin Cloud Real Phone

**Real Android devices in the cloud** — genuine mobile fingerprints for platforms that punish desktop automation.

| | |
|---|---|
| **Product guide** | [docs/multilogin-cloud-real-phone.md](docs/multilogin-cloud-real-phone.md) |
| **Mobile MMO** | [docs/mobile-mmo-playbook.md](docs/mobile-mmo-playbook.md) |
| **Promo** | **`MIN50`** at [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) |

Desktop automation stays on Launcher API ([cookbook](docs/multilogin-api/cookbook/)); mobile sessions use MLX Cloud Real Phone alongside the same workspace discipline.

---

## Quick start

| Step | Action |
|------|--------|
| 1 | Install Multilogin X and create a browser profile |
| 2 | Get folder/profile UUIDs → [docs/token-and-ids.md](docs/token-and-ids.md) |
| 3 | `cp sdk/config.example.env sdk/.env` and fill IDs |
| 4 | `cd sdk/python && pip install -e .` (installs `mlx` CLI) |
| 5 | `mlx doctor` → `mlx start` or [`recipes/01`](sdk/python/recipes/01_saved_profile_lifecycle.py) |
| 6 | Mobile lane → [Cloud Real Phone](docs/multilogin-cloud-real-phone.md) · **`MIN50`** |
| 7 | Desktop plans → [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · **`SAAS50`** |

Full paths: [docs/getting-started.md](docs/getting-started.md)

---

## Multilogin X SDK & API cookbook

| Layer | Link |
|-------|------|
| **SDK** | [`sdk/`](sdk/) — `mlx_client`, start/stop/quick |
| **Cookbook** | [docs/multilogin-api/cookbook/](docs/multilogin-api/cookbook/) — **12** real-world recipes |
| **Cloud API** | [docs/multilogin-api/cloud-api.md](docs/multilogin-api/cloud-api.md) · `mlx profiles export` |
| **API reference** | [docs/multilogin-api/](docs/multilogin-api/) |
| **Postman archive** | [docs/multilogin-api/spec/](docs/multilogin-api/spec/) |
| **Library map** | [docs/libraries.md](docs/libraries.md) |

```text
sdk/python/
├── mlx_client.py          # reusable Launcher client
├── mlx_helpers.py         # CDP URL, quick v3 payload, retry
├── automation_patterns.py # login + Playwright/Selenium attach
└── recipes/               # 12 flows: lifecycle, Playwright, rotation, cloud export
```

| # | Recipe | Scenario |
|---|--------|----------|
| 01–05 | Lifecycle → smoke | Core launcher + CI |
| 06 | Error retry | Transient launcher failures |
| 07–08 | Login, Selenium | Production attach |
| 09–11 | Cookies | Warm, export, import |
| 12 | Cloud + workers | `profiles.json` + sharding |

Live Postman: [Postman collection](https://documenter.getpostman.com/view/28533318/2s946h9Cv9)

---

**Scaling profiles or fleets?** [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — apply **`SAAS50`** (Multilogin promo code) or **`MIN50`** (Multilogin Cloud Real Phone) at checkout.

---

## Architecture

```mermaid
flowchart TB
  H[Anti-detect Hub] --> SDK[sdk/]
  H --> CB[cookbook/]
  H --> SPEC[spec archive]
  SDK --> API[MLX Launcher API]
  API --> B[Browser profiles]
  CB --> PW[Playwright / Selenium]
  PW --> B
```

Details: [docs/architecture.md](docs/architecture.md)

---

## Compare & choose

| Doc | Search intent |
|-----|---------------|
| [vs GoLogin](docs/comparison-multilogin-vs-gologin.md) | Multilogin alternative |
| [vs AdsPower](docs/comparison-multilogin-vs-adspower.md) | AdsPower alternative |
| [vs Chrome](docs/comparison-anti-detect-vs-chrome.md) | Why anti-detect |
| [Use cases](docs/use-cases.md) | By industry |
| [Why this hub](docs/why-this-hub.md) | #1 open MLX resource |

---

## Guides

| Topic | Doc |
|-------|-----|
| Cloud Real Phone | [docs/multilogin-cloud-real-phone.md](docs/multilogin-cloud-real-phone.md) |
| Playwright + MLX | [docs/playwright-mlx-integration.md](docs/playwright-mlx-integration.md) |
| MMO / multi-account | [docs/mmo-automation-guide.md](docs/mmo-automation-guide.md) |
| Mobile MMO | [docs/mobile-mmo-playbook.md](docs/mobile-mmo-playbook.md) |
| Troubleshooting | [docs/troubleshooting.md](docs/troubleshooting.md) |
| Fingerprint QA | [docs/fingerprint-checklist.md](docs/fingerprint-checklist.md) |
| Market overview | [docs/browser-landscape.md](docs/browser-landscape.md) |

---

## Frequently asked questions

### What is an anti-detect browser?

Software that isolates fingerprints, storage, and proxies so each profile resembles a separate device.

### Where is the code?

In this repo: [`sdk/`](sdk/) and [cookbook recipes](docs/multilogin-api/cookbook/).

### How do I get profile IDs?

[docs/token-and-ids.md](docs/token-and-ids.md)

### Discount on Multilogin X?

**`SAAS50`** or **`MIN50`** on [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549).

More: [docs/faq.md](docs/faq.md)

---

## Multilogin pricing reference

| Code | Label | When to use |
|------|-------|-------------|
| **`SAAS50`** | Multilogin promo code | New Multilogin X plan, first purchase |
| **`MIN50`** | Multilogin Cloud Real Phone | Cloud Real Phone / entry-tier checkout |

**Checkout:** [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · [docs/urls.md](docs/urls.md) · [CTA placement guide](docs/pricing-cta.md)

---

## Languages

| Locale | README |
|--------|--------|
| English | You are here |
| Tiếng Việt | [README.vi.md](README.vi.md) |
| 中文 | [README.zh-CN.md](README.zh-CN.md) |
| Русский | [README.ru.md](README.ru.md) |
| Indonesia | [README.id.md](README.id.md) |
| Português (BR) | [README.pt-BR.md](README.pt-BR.md) |
| 한국어 | [README.ko.md](README.ko.md) |
| 日本語 | [README.ja.md](README.ja.md) |
| ไทย | [README.th.md](README.th.md) |
| Español | [README.es.md](README.es.md) |

[Index](docs/locales.md)

---

## Documentation

| Doc | Purpose |
|-----|---------|
| [docs/README.md](docs/README.md) | Documentation index |
| [docs/getting-started.md](docs/getting-started.md) | Onboarding paths |
| [docs/multilogin-cloud-real-phone.md](docs/multilogin-cloud-real-phone.md) | Cloud Real Phone + MIN50 |
| [docs/troubleshooting.md](docs/troubleshooting.md) | Fix launcher/CDP/cloud |
| [docs/repository-map.md](docs/repository-map.md) | What's inside this repo |
| [docs/token-and-ids.md](docs/token-and-ids.md) | Profile UUIDs & tokens |
| [docs/architecture.md](docs/architecture.md) | System design |
| [docs/multilogin-api/cookbook/](docs/multilogin-api/cookbook/) | API recipes |
| [sdk/README.md](sdk/README.md) | SDK entry |
| [docs/maintenance.md](docs/maintenance.md) | Maintainer workflow |
| [docs/disclaimer.md](docs/disclaimer.md) | Legal disclaimer |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribute |
| [SECURITY.md](SECURITY.md) | Security |
| [docs/pricing-cta.md](docs/pricing-cta.md) | Affiliate CTAs (**SAAS50** / **MIN50**) |

---

<p align="center">
  <strong><a href="https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549">Get Multilogin X</a></strong> — promo <code>SAAS50</code> · <code>MIN50</code> (Cloud Real Phone)
</p>

<p align="center">
  <sub>Anti-detect browser · Browser fingerprinting · Multilogin X · Playwright · Selenium</sub>
</p>
