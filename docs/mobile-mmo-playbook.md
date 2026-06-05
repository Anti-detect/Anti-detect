# Mobile MMO playbook — Cloud Real Phone

Operational patterns for **multi-account mobile** workflows with **Multilogin Cloud Real Phone** and desktop MLX in parallel.

> **Cloud Real Phone:** [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — **`MIN50`**  
> Comply with platform terms of service. Technical guide only.

---

## Fleet architecture

```text
Campaign
├── Desktop lane (SAAS50 / Launcher API)
│   ├── profiles.json → Recipe 04 rotation
│   └── Playwright/Selenium recipes 02, 07, 08
└── Mobile lane (MIN50 / Cloud Real Phone)
    ├── Separate profile pool (never share with desktop)
    └── Manual or cloud-session automation per MLX docs
```

---

## Rules that prevent mass bans

| Rule | Why |
|------|-----|
| 1 profile = 1 account | Fingerprint + storage isolation |
| Mobile lane ≠ desktop lane | Different device class — do not swap cookies blindly |
| Proxy sticks to profile | Mid-session IP change is a top ban signal |
| Warm before automate | New profiles need human-like history |
| Pace actions | Parallel is **multi-machine**, not 50 tabs one launcher |

---

## Day-0 setup checklist

- [ ] Cloud Real Phone plan active — **`MIN50`** applied
- [ ] Mobile profiles created per account
- [ ] Residential/mobile proxy per profile where required
- [ ] Export UUIDs: `mlx profiles export` ([Recipe 12](multilogin-api/cookbook/12-cloud-export-and-workers.md))
- [ ] Desktop side: `mlx doctor` passes
- [ ] [fingerprint-checklist.md](fingerprint-checklist.md) for desktop lane

---

## Typical flows

| Goal | Mobile (Real Phone) | Desktop (this SDK) |
|------|---------------------|---------------------|
| Register account | In-session on Real Phone | Recipe 03 quick profile (one-off) |
| Daily check-in | Mobile session | Recipe 01 lifecycle |
| Re-login | Mobile UI | Recipe 07 login |
| Cookie backup | MLX profile storage | Recipe 09 export |
| Fleet inventory | MLX UI / cloud search | Recipe 12 export |

---

## Scaling

1. **Pilot** 2–3 mobile + 2–3 desktop accounts.
2. **Export** profile lists to JSON for orchestration.
3. **Shard** desktop workers ([Recipe 12](multilogin-api/cookbook/12-cloud-export-and-workers.md)).
4. **Add** Real Phone devices via Multilogin billing — not by sharing profiles.

---

## Related

- [multilogin-cloud-real-phone.md](multilogin-cloud-real-phone.md)
- [mmo-automation-guide.md](mmo-automation-guide.md)
- [use-cases.md](use-cases.md)

---

**Multilogin X:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — **`SAAS50`** · **`MIN50`**
