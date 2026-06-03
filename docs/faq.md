# FAQ

Extended answers for **anti-detect browser**, **browser fingerprinting**, and **Multilogin X automation**.

---

## English

### Is anti-detect automation legal?

Laws and site terms vary by jurisdiction and platform. You are responsible for compliance with applicable law and each website's terms of service. This documentation describes technical patterns for legitimate automation, QA, and account management use cases.

### Which keywords describe this ecosystem?

Common search terms: **anti-detect browser**, **browser fingerprinting**, **Multilogin X**, **stealth automation**, **Playwright anti-bot**, **Selenium fingerprint**, **profile isolation**, **MMO account management**.

### Why are kits split across multiple repositories?

Smaller repos improve install size, versioning, and issue triage. This profile repo acts as the **discovery hub**; implementation lives under [@multilogin-automation](https://github.com/multilogin-automation).

### How often is documentation updated?

We update when new kits ship or when API surfaces change. Star/watch individual kit repos for release notifications.

### Can I fork and modify templates?

Yes, subject to each kit's license (typically permissive open source). Keep attribution where required.

### Where are the Python SDK / Postman repos?

The canonical hub is **[multilogin-automation](https://github.com/multilogin-automation/multilogin-automation)** with `/templates` (e.g. `mlx_config_template.py`, `playwright_stealth.py`). Older README links to separate `multilogin-x-python-automation-sdk` repos were removed—they are not published on GitHub.

### What promo codes work?

| Code | Typical use |
|------|-------------|
| `ADBNEW50` | 50% off first Multilogin X purchase via ADBLogin |
| `SAVE50` | Partner/cloud offers (see individual kit READMEs) |

---

## Tiếng Việt

### Anti-detect browser là gì?

**Anti-detect browser** (trình duyệt chống nhận diện) tạo **profile** riêng: fingerprint (Canvas, WebGL, font…), cookie và proxy tách biệt, giúp mỗi phiên giống một thiết bị khác—phù hợp automation, MMO hoặc quản lý nhiều tài khoản khi cần cô lập danh tính trình duyệt.

### Bắt đầu từ đâu?

1. Chọn kit trong [open-source-catalog.md](open-source-catalog.md).  
2. Làm theo README của repo tương ứng.  
3. Cần hạ tầng và giá đối tác: [ADBLogin.com](https://adblogin.com), mã **ADBNEW50** (xem [README](../README.md#partner-offer)).

### Liên hệ hỗ trợ?

- Telegram: [@ToolsKiemTrieuDoGroup](https://t.me/ToolsKiemTrieuDoGroup), [@ToolsKiemTrieuDo](https://t.me/ToolsKiemTrieuDo)  
- Email: business@adblogin.com  
- Hệ sinh thái: [ToolKiemTrieuDo.com](https://toolskiemtrieudo.com)

### Báo lỗi bảo mật?

Không mở issue công khai. Xem [SECURITY.md](../SECURITY.md).

---

## Related

- [Getting started](getting-started.md)
- [Main README](../README.md)
