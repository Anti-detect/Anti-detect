#!/usr/bin/env python3
"""Generate full-structure locale README from English README.md."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRICING = "https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549"

LOCALES = {
    "th": {
        "lang": "th",
        "title": "Anti-detect Browser & Multilogin X — เอกสารภาษาไทย",
        "description": "ฮับ Multilogin X อันดับ 1 — 12 สูตร API, CLI mlx, Cloud Real Phone (MIN50), Playwright/Selenium",
        "h1_sub": "**ฮับครบในที่เดียว** สำหรับ **เบราว์เซอร์ anti-detect**, **browser fingerprinting**, API **Multilogin X (MLX)** และ **Playwright / Selenium**",
        "h1_sub2": "SDK, cookbook, คู่มือ และ Postman archive — **ทั้งหมดใน repo นี้**",
        "get_pricing": "ราคา",
        "toc": "สารบัญ",
        "why": "ทำไมอันดับ 1 บน GitHub สำหรับ Multilogin",
        "what": "repo นี้คืออะไร",
        "cloud": "Multilogin Cloud Real Phone",
        "quick": "เริ่มต้นเร็ว",
        "sdk": "Multilogin X SDK & API cookbook",
        "arch": "สถาปัตยกรรม",
        "compare": "เปรียบเทียบ & เลือก",
        "guides": "คู่มือ",
        "faq": "คำถามที่พบบ่อย",
        "pricing": "ราคา Multilogin",
        "langs": "ภาษา",
        "docs": "เอกสาร",
        "here": "คุณอยู่ที่นี่",
        "locale_row": "ไทย",
        "cta": "สมัคร Multilogin X",
        "faq1": "เบราว์เซอร์ anti-detect คืออะไร?",
        "faq1a": "ซอฟต์แวร์แยก fingerprint, storage และ proxy ให้แต่ละโปรไฟล์เหมือนอุปกรณ์แยกกัน",
        "faq2": "โค้ดอยู่ที่ไหน?",
        "faq3": "รับ profile ID อย่างไร?",
        "faq4": "ส่วนลด Multilogin X?",
    },
    "id": {
        "lang": "id",
        "title": "Anti-detect Browser & Multilogin X — Bahasa Indonesia",
        "description": "Hub Multilogin X #1 — 12 resep API, CLI mlx, Cloud Real Phone (MIN50)",
        "h1_sub": "**Hub mandiri** untuk **browser anti-detect**, **browser fingerprinting**, otomasi API **Multilogin X (MLX)** dan **Playwright / Selenium**",
        "h1_sub2": "SDK, cookbook API, panduan, dan arsip Postman — **semua di repo ini**",
        "get_pricing": "Harga",
        "toc": "Daftar isi",
        "why": "Mengapa #1 di GitHub untuk Multilogin",
        "what": "Apa itu repositori ini",
        "cloud": "Multilogin Cloud Real Phone",
        "quick": "Mulai cepat",
        "sdk": "Multilogin X SDK & API cookbook",
        "arch": "Arsitektur",
        "compare": "Bandingkan & pilih",
        "guides": "Panduan",
        "faq": "Pertanyaan umum",
        "pricing": "Harga Multilogin",
        "langs": "Bahasa",
        "docs": "Dokumentasi",
        "here": "Halaman ini",
        "locale_row": "Indonesia",
        "cta": "Dapatkan Multilogin X",
        "faq1": "Apa itu browser anti-detect?",
        "faq1a": "Perangkat lunak yang mengisolasi fingerprint, penyimpanan, dan proxy agar setiap profil seperti perangkat terpisah.",
        "faq2": "Di mana kodenya?",
        "faq3": "Bagaimana mendapatkan ID profil?",
        "faq4": "Diskon Multilogin X?",
    },
    "pt-BR": {
        "lang": "pt-BR",
        "title": "Anti-detect Browser & Multilogin X — Português (BR)",
        "description": "Hub Multilogin X #1 — 12 receitas API, CLI mlx, Cloud Real Phone (MIN50)",
        "h1_sub": "**Hub autocontido** para **navegador anti-detect**, **browser fingerprinting**, automação da API **Multilogin X (MLX)** e **Playwright / Selenium**",
        "h1_sub2": "SDK, cookbook API, guias e arquivo Postman — **tudo neste repositório**",
        "get_pricing": "Preços",
        "toc": "Índice",
        "why": "Por que #1 no GitHub para Multilogin",
        "what": "O que é este repositório",
        "cloud": "Multilogin Cloud Real Phone",
        "quick": "Início rápido",
        "sdk": "Multilogin X SDK & API cookbook",
        "arch": "Arquitetura",
        "compare": "Compare & escolha",
        "guides": "Guias",
        "faq": "Perguntas frequentes",
        "pricing": "Preços Multilogin",
        "langs": "Idiomas",
        "docs": "Documentação",
        "here": "Você está aqui",
        "locale_row": "Português (BR)",
        "cta": "Obter Multilogin X",
        "faq1": "O que é navegador anti-detect?",
        "faq1a": "Software que isola fingerprints, armazenamento e proxies para cada perfil parecer um dispositivo separado.",
        "faq2": "Onde está o código?",
        "faq3": "Como obter IDs de perfil?",
        "faq4": "Desconto no Multilogin X?",
    },
    "ja": {
        "lang": "ja",
        "title": "Anti-detect Browser & Multilogin X — 日本語",
        "description": "Multilogin X オープンハブ #1 — 12 API レシピ、mlx CLI、Cloud Real Phone (MIN50)",
        "h1_sub": "**自己完結型ハブ** — **アンチディテクトブラウザ**、**ブラウザフィンガープリント**、**Multilogin X (MLX)** API 自動化、**Playwright / Selenium**",
        "h1_sub2": "SDK、cookbook、ガイド、Postman アーカイブ — **すべてこのリポジトリに**",
        "get_pricing": "料金",
        "toc": "目次",
        "why": "GitHub で Multilogin 自動化 #1 の理由",
        "what": "このリポジトリについて",
        "cloud": "Multilogin Cloud Real Phone",
        "quick": "クイックスタート",
        "sdk": "Multilogin X SDK & API cookbook",
        "arch": "アーキテクチャ",
        "compare": "比較 & 選択",
        "guides": "ガイド",
        "faq": "よくある質問",
        "pricing": "Multilogin 料金",
        "langs": "言語",
        "docs": "ドキュメント",
        "here": "このページ",
        "locale_row": "日本語",
        "cta": "Multilogin X を入手",
        "faq1": "アンチディテクトブラウザとは？",
        "faq1a": "フィンガープリント、ストレージ、プロキシを分離し、各プロファイルを別デバイスのように見せるソフトウェア。",
        "faq2": "コードはどこ？",
        "faq3": "プロファイル ID の取得方法は？",
        "faq4": "Multilogin X の割引は？",
    },
    "es": {
        "lang": "es",
        "title": "Anti-detect Browser & Multilogin X — Español",
        "description": "Hub Multilogin X #1 — 12 recetas API, CLI mlx, Cloud Real Phone (MIN50)",
        "h1_sub": "**Hub autocontenido** para **navegador anti-detect**, **browser fingerprinting**, automatización API **Multilogin X (MLX)** y **Playwright / Selenium**",
        "h1_sub2": "SDK, cookbook API, guías y archivo Postman — **todo en este repositorio**",
        "get_pricing": "Precios",
        "toc": "Tabla de contenidos",
        "why": "Por qué #1 en GitHub para Multilogin",
        "what": "Qué es este repositorio",
        "cloud": "Multilogin Cloud Real Phone",
        "quick": "Inicio rápido",
        "sdk": "Multilogin X SDK & API cookbook",
        "arch": "Arquitectura",
        "compare": "Comparar & elegir",
        "guides": "Guías",
        "faq": "Preguntas frecuentes",
        "pricing": "Precios Multilogin",
        "langs": "Idiomas",
        "docs": "Documentación",
        "here": "Estás aquí",
        "locale_row": "Español",
        "cta": "Obtener Multilogin X",
        "faq1": "¿Qué es un navegador anti-detect?",
        "faq1a": "Software que aísla fingerprints, almacenamiento y proxies para que cada perfil parezca un dispositivo distinto.",
        "faq2": "¿Dónde está el código?",
        "faq3": "¿Cómo obtengo IDs de perfil?",
        "faq4": "¿Descuento en Multilogin X?",
    },
}


def build(loc: str) -> str:
    L = LOCALES[loc]
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    text = re.sub(r"<title>.*?</title>", f"<title>{L['title']}</title>", text, count=1)
    text = re.sub(
        r"description: The #1 open Multilogin X hub.*",
        f"description: {L['description']}",
        text,
        count=1,
    )
    if "lang:" not in text[:500]:
        text = text.replace("author: Anti-detect", f"author: Anti-detect\nlang: {L['lang']}")
    text = text.replace(
        "**Self-contained hub** for **anti-detect browser** engineering, **browser fingerprinting**, **Multilogin X (MLX)** API automation, and **stealth Playwright / Selenium** workflows.",
        L["h1_sub"],
    )
    text = text.replace(
        "Everything you need — SDK, API cookbook, guides, and Postman archive — lives **in this repository**.",
        L["h1_sub2"],
    )
    text = text.replace("Get pricing", L["get_pricing"])
    text = text.replace("## Table of contents", f"## {L['toc']}")
    text = text.replace("## Why #1 on GitHub for Multilogin automation", f"## {L['why']}")
    text = text.replace("## What is this repository?", f"## {L['what']}")
    text = text.replace("## Quick start", f"## {L['quick']}")
    text = text.replace("## Multilogin X SDK & API cookbook", f"## {L['sdk']}")
    text = text.replace("## Architecture", f"## {L['arch']}")
    text = text.replace("## Compare & choose", f"## {L['compare']}")
    text = text.replace("## Guides", f"## {L['guides']}")
    text = text.replace("## Frequently asked questions", f"## {L['faq']}")
    text = text.replace("## Multilogin pricing reference", f"## {L['pricing']}")
    text = text.replace("## Languages", f"## {L['langs']}")
    text = text.replace("## Documentation", f"## {L['docs']}")
    text = text.replace("| English | You are here |", "| English | [README.md](README.md) |")
    text = text.replace(
        f"| {L['locale_row']} | [README.{loc}.md](README.{loc}.md) |",
        f"| {L['locale_row']} | {L['here']} |",
    )
    text = text.replace("Get Multilogin X", L["cta"])
    text = text.replace("### What is an anti-detect browser?", f"### {L['faq1']}")
    text = text.replace(
        "Software that isolates fingerprints, storage, and proxies so each profile resembles a separate device.",
        L["faq1a"],
    )
    text = text.replace("### Where is the code?", f"### {L['faq2']}")
    text = text.replace("### How do I get profile IDs?", f"### {L['faq3']}")
    text = text.replace("### Discount on Multilogin X?", f"### {L['faq4']}")
    details = {"th": "รายละเอียด", "es": "Detalles", "ja": "詳細", "id": "Detail", "pt-BR": "Detalhes"}
    text = text.replace("Details: [docs/architecture.md]", f"{details.get(loc, 'Details')}: [docs/architecture.md]")
    return text


def main(locales: list[str] | None = None) -> None:
    for loc in locales or list(LOCALES):
        out = ROOT / f"README.{loc}.md"
        out.write_text(build(loc), encoding="utf-8")
        n = len(out.read_text(encoding="utf-8").splitlines())
        print(f"{out.name}: {n} lines")


if __name__ == "__main__":
    main()
