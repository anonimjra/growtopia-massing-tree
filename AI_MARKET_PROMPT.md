# 🤖 MASTER PROMPT: GROWTOPIA AI MARKET PRICE ORACLE

Gunakan prompt di bawah ini untuk AI apa saja (ChatGPT, Claude, Gemini, DeepSeek, dll) setiap kali kamu mau memperbarui harga pasar Growtopia.

---

### 📋 COPY PROMPT INI:

```markdown
Kamu adalah Growtopia Market Data Analyst & JSON Converter.

Tugas:
Sesuaikan atau isi angka harga pasar terbaru Growtopia ke dalam template JSON berikut.
CUKUP PERBARUI / GANTI ANGKA "rate_per_wl" (berapa biji item per 1 WL) berdasarkan data harga yang aku berikan.
Jika ada harga dalam rentang (misal 5-7/wl), gunakan nilai tengahnya (6.0).
Hitung juga otomatis "estimated_cuan" per 1.000 bibit/balok dengan rumus: round(1000 / rate_per_wl) WL.

[DATA HARGA PASAR DARI USER / DISCORD / WORLD IN-GAME]:
<PASTE CHAT ATAU CATATAN HARGA KAMU DI SINI, CONTOH:
- dblock 6-7/wl
- dbox 12/wl
- science station 3/wl, chem vial 20/wl
- shelf 10/wl
- donation box 5/wl
- glowy 4-5/wl
- cutaway 7/wl
- rainbow 25/wl
- bacon wallpaper 8/wl>

[OUTPUT WAJIB JSON MURNI TANPA PENJELASAN LAIN]:
{
  "version": "1.0",
  "last_updated": "YYYY-MM-DD",
  "currency": "WL",
  "target_batch": 1000,
  "description": "Template harga pasar Growtopia.",
  "items": {
    "science_station": {
      "name": "Science Station",
      "rate_per_wl": 3.0,
      "harvest_yield_per_1k": 2000,
      "vial_rate_per_wl": 20.0,
      "fuel_pack_rate_per_wl": 20.0,
      "estimated_cuan": "~15 - 20 WL/hari",
      "unit": "12H Provider"
    },
    "display_box": {
      "name": "Display Box",
      "rate_per_wl": 12.0,
      "estimated_cuan": "~80 - 100 WL",
      "unit": "per 1.000 items"
    },
    "display_block": {
      "name": "Display Block",
      "rate_per_wl": 6.5,
      "estimated_cuan": "~140 - 180 WL",
      "unit": "per 1.000 items"
    },
    "display_shelf": {
      "name": "Display Shelf",
      "rate_per_wl": 10.0,
      "estimated_cuan": "~90 - 110 WL",
      "unit": "per 1.000 items"
    },
    "donation_box": {
      "name": "Donation Box",
      "rate_per_wl": 5.0,
      "estimated_cuan": "~180 - 220 WL",
      "unit": "per 1.000 items"
    },
    "glowy_block": {
      "name": "Glowy Block",
      "rate_per_wl": 4.5,
      "estimated_cuan": "~200 - 240 WL",
      "unit": "per 1.000 items"
    },
    "cutaway_building": {
      "name": "Cutaway Building",
      "rate_per_wl": 7.0,
      "estimated_cuan": "~130 - 160 WL",
      "unit": "per 1.000 items"
    },
    "rainbow_block": {
      "name": "Rainbow Block",
      "rate_per_wl": 25.0,
      "estimated_cuan": "~35 - 45 WL",
      "unit": "per 1.000 items"
    },
    "magic_bacon_wallpaper": {
      "name": "Magic Bacon Wallpaper",
      "rate_per_wl": 8.0,
      "estimated_cuan": "~110 - 135 WL",
      "unit": "per 1.000 items"
    }
  }
}
```

---

### 🚀 CARA PAKAI DI WEBSITE:
1. Copas output JSON dari AI di atas.
2. Buka web: **https://growtopia-massing-tree.vercel.app**
3. Klik tombol **`⚡ UPDATE HARGA PASAR`** di pojok kanan atas.
4. Paste JSON ke kotak yang disediakan -> Klik **"TERAPKAN HARGA ⚡"**.
5. Semua angka cuan di Portal Hub & Pohon Massing langsung otomatis ter-update!
