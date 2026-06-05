# FAQ

Extended answers for **anti-detect browser**, **browser fingerprinting**, and **Multilogin X automation**.

---

## English

### Is anti-detect automation legal?

Laws and site terms vary by jurisdiction and platform. You are responsible for compliance with applicable law and each website's terms of service. This documentation describes technical patterns for legitimate automation, QA, and account management use cases.

### Which keywords describe this ecosystem?

Common search terms: **anti-detect browser**, **antidetect browser**, **fingerprint browser**, **browser fingerprinting**, **Multilogin X**, **GoLogin**, **Dolphin Anty**, **AdsPower**, **browser profile manager**, **stealth automation**, **Playwright anti-bot**, **Selenium fingerprint**, **profile isolation**, **MMO account management**, **undetectable browser**. See [browser-landscape.md](browser-landscape.md) for a neutral category overview.

### Why are kits split across multiple repositories?

Smaller repos improve install size, versioning, and issue triage. This profile repo acts as the **discovery hub**; implementation lives under [@multilogin-automation](https://github.com/multilogin-automation).

### How often is documentation updated?

We update when new kits ship or when API surfaces change. Star/watch individual kit repos for release notifications.

### Can I fork and modify templates?

Yes, subject to each kit's license (typically permissive open source). Keep attribution where required.

### Where are the Python SDK / Postman repos?

The canonical hub is **[multilogin-automation](https://github.com/multilogin-automation/multilogin-automation)** with `/templates` (e.g. `mlx_config_template.py`, `playwright_stealth.py`). Older README links to separate `multilogin-x-python-automation-sdk` repos were removed—they are not published on GitHub.

### Where is the Multilogin X API code in this repo?

- **[sdk/](../sdk/)** — runnable Python, C#, Java examples (from Postman + `docs/multilogin-api/spec/`)
- **[docs/multilogin-api/](multilogin-api/README.md)** — API reference
- **[docs/libraries.md](libraries.md)** — full library map
- Live collection: https://documenter.getpostman.com/view/28533318/2s946h9Cv9

### What promo codes work?

| Code | Typical use |
|------|-------------|
| `SAAS50` | First-time / SaaS partner discount on Multilogin X |
| `MIN50` | Minimum-tier or follow-up offers at checkout |

Apply on [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549).

### How do I report security issues?

Do not open public issues. See [SECURITY.md](../SECURITY.md).

---

## Tiếng Việt

### Anti-detect browser là gì?

**Anti-detect browser** (trình duyệt chống nhận diện) tạo **profile** riêng: fingerprint (Canvas, WebGL, font…), cookie và proxy tách biệt.

### Bắt đầu từ đâu?

1. Chọn kit trong [open-source-catalog.md](open-source-catalog.md).  
2. Làm theo README repo tương ứng.  
3. Gói MLX: [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549), mã **SAAS50** / **MIN50**.

### Báo lỗi bảo mật?

Xem [SECURITY.md](../SECURITY.md).

---

## 中文

### 什么是反检测浏览器？

为每个配置文件隔离指纹、Cookie 与代理，降低账号关联风险。

### 从哪里开始？

[open-source-catalog.md](open-source-catalog.md) → 对应仓库 README → [Multilogin 定价](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)（**SAAS50** / **MIN50**）。

---

## Русский

### Что такое антидетект-браузер?

Изоляция отпечатка, хранилища и прокси на профиль — отдельная «машина» на сессию.

### С чего начать?

[Каталог](open-source-catalog.md) → README kit → [Цены Multilogin](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549), коды **SAAS50** / **MIN50**.

---

## Bahasa Indonesia

### Apa itu browser anti-detect?

Profil terpisah untuk fingerprint, cookie, dan proxy — mengurangi korelasi akun.

### Mulai dari mana?

[Katalog](open-source-catalog.md) → [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) (**SAAS50** / **MIN50**).

---

## Português (BR)

### O que é navegador anti-detect?

Isolamento de fingerprint, armazenamento e proxy por perfil.

### Por onde começar?

[Catálogo](open-source-catalog.md) · códigos **SAAS50** / **MIN50** no checkout Multilogin.

---

## Español

### ¿Qué es un navegador anti-detect?

Perfiles aislados de fingerprint, almacenamiento y proxy por cuenta.

### ¿Por dónde empezar?

[Guía MMO](mmo-automation-guide.md) · [Catálogo](open-source-catalog.md) · códigos **SAAS50** / **MIN50**.

---

## ไทย

### เบราว์เซอร์ anti-detect คืออะไร?

แยก fingerprint และ proxy ต่อโปรไฟล์ — เหมาะกับ MMO / หลายบัญชี

### เริ่มที่ไหน?

[README.th.md](../README.th.md) · [browser-landscape.md](browser-landscape.md)

---

## Related

- [Getting started](getting-started.md)
- [Fingerprint checklist](fingerprint-checklist.md)
- [Locales index](locales.md)
- [Main README](../README.md)
