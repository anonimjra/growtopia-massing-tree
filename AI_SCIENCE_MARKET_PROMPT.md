# 🧪 MASTER PROMPT: SCIENCE STATION MASSING INGREDIENTS & COST ORACLE

Gunakan prompt ini untuk AI apa saja (ChatGPT, Claude, Gemini, DeepSeek) untuk memperbarui harga **BAHAN-BAHAN pembentuk Science Station** (bukan hasil panen chemical vial, tapi murni modal bahan bibit splicingnya).

---

### 📋 COPY PROMPT INI:

```markdown
Kamu adalah Growtopia Splicing Economics Specialist.

Tugas:
Sesuaikan angka harga pasar terbaru (rate_per_wl) untuk BAHAN-BAHAN MASSING SCIENCE STATION ke dalam template JSON di bawah.
Bahan-bahan ini adalah bibit atau balok yang dibutuhkan untuk melakukan splicing Science Station.
CUKUP PERBARUI / GANTI ANGKA "rate_per_wl" (berapa biji item per 1 WL) berdasarkan data harga yang aku berikan.

Resep Pohon Massing Science Station:
- Science Station (Output) = Toxic Waste Barrel + Military Radio
- Bahan Kunci: Death Spikes (dibutuhkan 2x di cabang kiri & kanan), Cactus, Acid, Barrel, Plumbing, Biohazard Sign, Sheet Music Sharp Piano, Danger Sign.

[DATA HARGA BAHAN DARI USER / DISCORD / GAME]:
<PASTE CHAT / HARGA PASAR BAHAN DI SINI, CONTOH:
- science station 3/wl atau 3.5/wl
- toxic waste 6/wl atau 7/wl
- military radio 6/wl
- death spikes 50/wl atau 60/wl
- cactus 25/wl
- acid 14/wl
- barrel 30/wl
- plumbing 18/wl
- biohazard sign 18/wl
- sheet music sharp piano 12/wl>

[OUTPUT WAJIB JSON MURNI TANPA PENJELASAN LAIN]:
{
  "version": "2.0",
  "item_target": "Science Station",
  "type": "Massing Ingredients & Recipe Cost Oracle",
  "target_batch": 1000,
  "selling_price": {
    "science_station_rate_per_wl": 3.0
  },
  "materials": {
    "toxic_waste_barrel": {
      "rate_per_wl": 6.5
    },
    "military_radio": {
      "rate_per_wl": 6.5
    },
    "death_spikes": {
      "rate_per_wl": 50.0
    },
    "cactus": {
      "rate_per_wl": 25.0
    },
    "acid": {
      "rate_per_wl": 14.0
    },
    "barrel": {
      "rate_per_wl": 30.0
    },
    "plumbing": {
      "rate_per_wl": 18.0
    },
    "biohazard_sign": {
      "rate_per_wl": 18.0
    },
    "sheet_music_sharp_piano": {
      "rate_per_wl": 12.0
    },
    "danger_sign": {
      "rate_per_wl": 70.0
    }
  }
}
```

---

### 🚀 CARA PAKAI DI WEBSITE:
1. Copas output JSON dari AI di atas.
2. Buka web: **https://growtopia-massing-tree.vercel.app/science-station-anime-comic/**
3. Klik tombol **`📈 HARGA BAHAN (AI)`** di menu atas.
4. Buka tab **"📥 UPLOAD / PASTE JSON"** -> paste JSON -> Klik **"TERAPKAN DATA JSON ⚡"**.
5. Sistem langsung menghitung modal beli bahan vs harga jual Science Station, dan memperlihatkan **PROFIT BERSIH CUAN MASSING** lu!
