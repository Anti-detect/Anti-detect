# Pricing CTAs — placement guide

Canonical affiliate URL and promo codes for **maximum conversion** across the hub. Sync from [urls.md](urls.md).

## Canonical link

**Checkout:** [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

## Promo codes

| Code | Label | Best for |
|------|-------|----------|
| **`SAAS50`** | Multilogin promo code | New Multilogin X plans, first checkout |
| **`MIN50`** | Multilogin Cloud Real Phone | Cloud Real Phone / minimum-tier bundles |

## Copy-paste blocks

### Head (above the fold)

```markdown
> **Multilogin X:** [Start for free or get paid plans from $7.08/mo](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · **`SAAS50`** (promo code) · **`MIN50`** (Cloud Real Phone)
```

### Mid (after SDK / technical value)

```markdown
---
**Need more profiles?** [Multilogin pricing (Free plan available)](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — plans from $7.08/month. Enter **`SAAS50`** or **`MIN50`** at checkout.
---
```

### Footer (last scroll)

```markdown
**Start with Multilogin X for free:** [multilogin.com/pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · paid plans from $7.08/mo · codes **`SAAS50`** · **`MIN50`**
```

## Where CTAs live

| Touch | Files |
|-------|--------|
| Head + mid + foot | [README.md](../README.md), all `README.*.md` |
| Head + foot | [docs/README.md](README.md), [getting-started.md](getting-started.md), [multilogin-api/README.md](multilogin-api/README.md), [cookbook/README.md](multilogin-api/cookbook/README.md), [sdk/README.md](../sdk/README.md), [sdk/python/README.md](../sdk/python/README.md) |
| Footer (minimum) | **Every** `docs/**/*.md` and `sdk/**/*.md` — CI enforces `SAAS50` + `MIN50` + pricing URL |
| Footer (recipes) | [cookbook/01–12](multilogin-api/cookbook/) — paste from [snippets/pricing-footer.md](snippets/pricing-footer.md) |
| Cloud Real Phone | [multilogin-cloud-real-phone.md](multilogin-cloud-real-phone.md), [mobile-mmo-playbook.md](mobile-mmo-playbook.md) |
| Comparisons | [comparison-multilogin-vs-gologin.md](comparison-multilogin-vs-gologin.md), [comparison-multilogin-vs-adspower.md](comparison-multilogin-vs-adspower.md) |
| Mid | [mmo-automation-guide.md](mmo-automation-guide.md), [browser-landscape.md](browser-landscape.md) |
| FAQ | [faq.md](faq.md) |
| GitHub UI | [.github/ISSUE_TEMPLATE/config.yml](../.github/ISSUE_TEMPLATE/config.yml) — pricing contact link |

New docs: run `python scripts/inject-affiliate-cta.py` if footer is missing.

Maintainers: **3 touches** on profile READMEs; **footer minimum** everywhere else.
