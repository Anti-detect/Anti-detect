<!--
title: Anti-detect Browser & Multilogin X — Português (Brasil)
description: Hub Multilogin X #1 — 12 receitas API, CLI mlx, Cloud Real Phone (MIN50), SDK Playwright/Selenium, comparação GoLogin/AdsPower
keywords: navegador anti-detect, Multilogin X, Cloud Real Phone, MIN50, SAAS50, fingerprint, Playwright, Selenium, MMO
homepage: https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549
lang: pt-BR
-->

# Anti-detect Browser · Fingerprinting · Multilogin X

**Hub autocontido** para **navegador anti-detect**, **browser fingerprinting**, automação da API **Multilogin X (MLX)** e fluxos **Playwright / Selenium** stealth.

Tudo o que você precisa — SDK, cookbook API, guias e arquivo Postman — está **neste repositório**.

> **Multilogin X — [Preços](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)** · **`SAAS50`** (código promo Multilogin) · **`MIN50`** (Multilogin Cloud Real Phone)

<p align="left">
  <a href="https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549"><img src="https://img.shields.io/badge/Multilogin-SAAS50%20%7C%20MIN50-6366f1?style=for-the-badge" alt="Multilogin SAAS50 MIN50"></a>
</p>

<p align="left">
  <img src="https://github.com/Anti-detect/Anti-detect/actions/workflows/docs-ci.yml/badge.svg" alt="Docs CI status">
  <img src="https://github.com/Anti-detect/Anti-detect/actions/workflows/sync-repo-settings.yml/badge.svg" alt="Sync repo settings status">
  <a href="README.md"><img src="https://img.shields.io/badge/English-README-blue?style=flat-square" alt="English"></a>
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

## Índice

- [Por que #1 no GitHub](#por-que-1-no-github-para-multilogin)
- [O que é este repositório](#o-que-é-este-repositório)
- [Cloud Real Phone (MIN50)](#multilogin-cloud-real-phone)
- [Início rápido](#início-rápido)
- [SDK & Cookbook API](#sdk--cookbook-api-multilogin-x)
- [Compare & escolha](#compare--escolha)
- [Documentação](#documentação)
- [FAQ](#perguntas-frequentes)
- [Preços Multilogin](#preços-multilogin)
- [Idiomas](#idiomas)

---

## Por que #1 no GitHub para Multilogin

| | Este hub |
|---|----------|
| **Receitas** | **12** cookbook + Python executável |
| **CLI** | `mlx start` · `stop` · `profiles export` · `doctor` |
| **SDK** | Python, C#, Java, Node, cURL |
| **Cloud** | `profile/search`, refresh de token, sharding |
| **Mobile** | [Cloud Real Phone](docs/multilogin-cloud-real-phone.md) + **`MIN50`** |
| **Idiomas** | 10 READMEs multilíngues |
| **Comparações** | vs [GoLogin](docs/comparison-multilogin-vs-gologin.md), [AdsPower](docs/comparison-multilogin-vs-adspower.md) |

Detalhes: [docs/why-this-hub.md](docs/why-this-hub.md)

---

## O que é este repositório

README oficial do perfil GitHub [@Anti-detect](https://github.com/Anti-detect): **hub de documentação + SDK** (MIT) com:

- **Navegador anti-detect** / isolamento de fingerprint
- **Multilogin X** Local Launcher API (start, stop, quick profile)
- **Código executável** em [`sdk/`](sdk/) — Python, C#, Java, Node, cURL
- **Receitas reais** em [docs/multilogin-api/cookbook/](docs/multilogin-api/cookbook/)
- **Arquivo Postman** em [docs/multilogin-api/spec/](docs/multilogin-api/spec/)

| Público | Caso de uso |
|---------|-------------|
| Engenheiros de automação | Playwright / Selenium em perfis MLX |
| Times MMO & growth | Isolamento multi-conta + rotação |
| Desenvolvedores | Referência API, SDK, smoke tests |
| Mobile / MMO | [Cloud Real Phone](docs/multilogin-cloud-real-phone.md) + fleet desktop |

---

## Multilogin Cloud Real Phone

**Dispositivos Android reais na nuvem** — fingerprints mobile genuínos para plataformas que punem automação desktop.

| | |
|---|---|
| **Guia** | [docs/multilogin-cloud-real-phone.md](docs/multilogin-cloud-real-phone.md) |
| **MMO mobile** | [docs/mobile-mmo-playbook.md](docs/mobile-mmo-playbook.md) |
| **Promo** | **`MIN50`** em [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) |

Automação desktop usa Launcher API ([cookbook](docs/multilogin-api/cookbook/)); sessões mobile usam Cloud Real Phone com as mesmas regras de workspace.

---

## Início rápido

| Passo | Ação |
|-------|------|
| 1 | Instale Multilogin X e crie um perfil de navegador |
| 2 | Obtenha UUIDs folder/profile → [docs/token-and-ids.md](docs/token-and-ids.md) |
| 3 | `cp sdk/config.example.env sdk/.env` e preencha os IDs |
| 4 | `cd sdk/python && pip install -e .` (instala CLI `mlx`) |
| 5 | `mlx doctor` → `mlx start` ou [`recipes/01`](sdk/python/recipes/01_saved_profile_lifecycle.py) |
| 6 | Linha mobile → [Cloud Real Phone](docs/multilogin-cloud-real-phone.md) · **`MIN50`** |
| 7 | Plano desktop → [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · **`SAAS50`** |

Completo: [docs/getting-started.md](docs/getting-started.md)

---

## SDK & Cookbook API Multilogin X

| Camada | Link |
|--------|------|
| **SDK** | [`sdk/`](sdk/) — `mlx_client`, start/stop/quick |
| **Cookbook** | [docs/multilogin-api/cookbook/](docs/multilogin-api/cookbook/) — **12** receitas |
| **Cloud API** | [docs/multilogin-api/cloud-api.md](docs/multilogin-api/cloud-api.md) · `mlx profiles export` |
| **Referência API** | [docs/multilogin-api/](docs/multilogin-api/) |
| **Arquivo Postman** | [docs/multilogin-api/spec/](docs/multilogin-api/spec/) |
| **Mapa de bibliotecas** | [docs/libraries.md](docs/libraries.md) |

```text
sdk/python/
├── mlx_client.py          # cliente Launcher reutilizável
├── mlx_helpers.py         # CDP URL, quick v3, retry
├── automation_patterns.py # login + attach Playwright/Selenium
└── recipes/               # 12 fluxos: lifecycle, rotação, export cloud
```

| # | Receita | Cenário |
|---|---------|---------|
| 01–05 | Lifecycle → smoke | Launcher core + CI |
| 06 | Retry | Falhas transitórias do launcher |
| 07–08 | Login, Selenium | Attach em produção |
| 09–11 | Cookies | Warm, export, import |
| 12 | Cloud + workers | `profiles.json` + sharding |

Postman: https://documenter.getpostman.com/view/28533318/2s946h9Cv9

---

**Precisa de mais perfis?** [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — **`SAAS50`** ou **`MIN50`** no checkout.

---

## Arquitetura

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

Detalhes: [docs/architecture.md](docs/architecture.md)

---

## Compare & escolha

| Documento | Intenção de busca |
|-----------|-------------------|
| [vs GoLogin](docs/comparison-multilogin-vs-gologin.md) | Alternativa Multilogin |
| [vs AdsPower](docs/comparison-multilogin-vs-adspower.md) | Alternativa AdsPower |
| [vs Chrome](docs/comparison-anti-detect-vs-chrome.md) | Por que anti-detect |
| [Use cases](docs/use-cases.md) | Por indústria |
| [Why this hub](docs/why-this-hub.md) | Hub MLX open-source #1 |

---

## Guias

| Tópico | Documento |
|--------|-----------|
| Cloud Real Phone | [docs/multilogin-cloud-real-phone.md](docs/multilogin-cloud-real-phone.md) |
| Playwright + MLX | [docs/playwright-mlx-integration.md](docs/playwright-mlx-integration.md) |
| MMO / multi-conta | [docs/mmo-automation-guide.md](docs/mmo-automation-guide.md) |
| MMO mobile | [docs/mobile-mmo-playbook.md](docs/mobile-mmo-playbook.md) |
| Solução de problemas | [docs/troubleshooting.md](docs/troubleshooting.md) |
| QA fingerprint | [docs/fingerprint-checklist.md](docs/fingerprint-checklist.md) |
| Mercado | [docs/browser-landscape.md](docs/browser-landscape.md) |

---

## Perguntas frequentes

### O que é navegador anti-detect?

Software que isola fingerprints, armazenamento e proxies para cada perfil parecer um dispositivo separado.

### Onde está o código?

Neste repo: [`sdk/`](sdk/) e [cookbook](docs/multilogin-api/cookbook/).

### Como obter IDs de perfil?

[docs/token-and-ids.md](docs/token-and-ids.md)

### Desconto no Multilogin X?

**`SAAS50`** ou **`MIN50`** em [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549).

Mais: [docs/faq.md](docs/faq.md)

---

## Preços Multilogin

| Código | Rótulo | Quando usar |
|--------|--------|-------------|
| **`SAAS50`** | Promo Multilogin | Plano MLX novo, primeira compra |
| **`MIN50`** | Multilogin Cloud Real Phone | Cloud Real Phone / pacote entry |

**Checkout:** [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · [docs/urls.md](docs/urls.md) · [pricing-cta.md](docs/pricing-cta.md)

---

## Idiomas

| Idioma | README |
|--------|--------|
| English | [README.md](README.md) |
| Tiếng Việt | [README.vi.md](README.vi.md) |
| 中文 | [README.zh-CN.md](README.zh-CN.md) |
| Русский | [README.ru.md](README.ru.md) |
| Indonesia | [README.id.md](README.id.md) |
| Português (BR) | Você está aqui |
| 한국어 | [README.ko.md](README.ko.md) |
| 日本語 | [README.ja.md](README.ja.md) |
| ไทย | [README.th.md](README.th.md) |
| Español | [README.es.md](README.es.md) |

[Índice](docs/locales.md)

---

## Documentação

| Documento | Propósito |
|-----------|-----------|
| [docs/README.md](docs/README.md) | Índice de documentação |
| [docs/getting-started.md](docs/getting-started.md) | Caminhos de onboarding |
| [docs/multilogin-cloud-real-phone.md](docs/multilogin-cloud-real-phone.md) | Cloud Real Phone + MIN50 |
| [docs/troubleshooting.md](docs/troubleshooting.md) | Corrigir launcher/CDP/cloud |
| [docs/repository-map.md](docs/repository-map.md) | Mapa do repo |
| [docs/token-and-ids.md](docs/token-and-ids.md) | UUIDs e tokens |
| [docs/architecture.md](docs/architecture.md) | Arquitetura |
| [docs/multilogin-api/cookbook/](docs/multilogin-api/cookbook/) | Receitas API |
| [sdk/README.md](sdk/README.md) | SDK |
| [docs/maintenance.md](docs/maintenance.md) | Manutenção |
| [docs/disclaimer.md](docs/disclaimer.md) | Disclaimer |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribuir |
| [SECURITY.md](SECURITY.md) | Segurança |
| [docs/pricing-cta.md](docs/pricing-cta.md) | CTAs de afiliado (**SAAS50** / **MIN50**) |

---

<p align="center">
  <strong><a href="https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549">Obter Multilogin X</a></strong> — <code>SAAS50</code> · <code>MIN50</code> (Cloud Real Phone)
</p>

<p align="center">
  <sub>Anti-detect browser · Browser fingerprinting · Multilogin X · Playwright · Selenium</sub>
</p>
