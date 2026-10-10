# 🧪 MASTER PROMPT: SCIENCE STATION MASSING INGREDIENTS & COST ORACLE

Gunakan prompt ini untuk AI apa saja (ChatGPT, Claude, Gemini, DeepSeek) untuk memperbarui harga:
- **OUTPUT (HASIL PANEN)**: Science Station berupa **BLOCK** (contoh: 3 Blocks / 1 WL).
- **BAHAN-BAHAN SPLICING**: Semua berupa **SEED (BENIH BIBIT)** (contoh: Death Spikes SEED 50 Seeds / 1 WL, Toxic Waste SEED 6-7 Seeds / 1 WL).

---

### 📋 COPY PROMPT INI:

```markdown
Kamu adalah Growtopia Splicing Economics Specialist.

Tugas:
Sesuaikan angka harga pasar terbaru (rate_per_wl) ke dalam template JSON di bawah.
ATURAN SATUAN PENTING:
1. Science Station dihitung dalam bentuk BLOCK (hasil panen pohon yang siap dijual ke pasar).
2. Semua BAHAN SPLICING dihitung dalam bentuk SEED (benih bibit yang digabungkan saat splicing).
Cukup ganti atau perbarui angka "rate_per_wl" (berapa biji item per 1 WL).

Daftar Bahan Splicing (Semua SEED):
- Toxic Waste Barrel Seed
- Military Radio Seed
- Death Spikes Seed (Core Bottleneck di 2 cabang)
- Cactus Seed (Non-Farmable)
- Acid Seed
- Barrel Seed
- Plumbing Seed
- Biohazard Sign Seed
- Sheet Music Sharp Piano Seed
- Danger Sign Seed

[DATA HARGA DARI USER / DISCORD / GAME]:
<PASTE HARGA DI SINI, CONTOH:
- science station block 3/wl atau 3.5/wl
- toxic waste seed 6/wl atau 7/wl
- military radio seed 6/wl
- death spikes seed 50/wl atau 55/wl
- cactus seed 25/wl
- sheet music sharp piano seed 12/wl
- acid seed 14/wl
- barrel seed 30/wl
- plumbing seed 18/wl
- biohazard sign seed 18/wl>

[OUTPUT WAJIB JSON MURNI TANPA PENJELASAN LAIN]:
{
  "version": "2.1",
  "item_target": "Science Station",
  "selling_price": {
    "item": "Science Station (BLOCK)",
    "unit": "Blocks per WL",
    "science_station_rate_per_wl": 3.0
  },
  "materials": {
    "toxic_waste_barrel": {
      "name": "Toxic Waste Barrel Seed",
      "type": "SEED",
      "rate_per_wl": 6.5
    },
    "military_radio": {
      "name": "Military Radio Seed",
      "type": "SEED",
      "rate_per_wl": 6.5
    },
    "death_spikes": {
      "name": "Death Spikes Seed",
      "type": "SEED",
      "rate_per_wl": 50.0
    },
    "cactus": {
      "name": "Cactus Seed",
      "type": "SEED",
      "rate_per_wl": 25.0
    },
    "acid": {
      "name": "Acid Seed",
      "type": "SEED",
      "rate_per_wl": 14.0
    },
    "barrel": {
      "name": "Barrel Seed",
      "type": "SEED",
      "rate_per_wl": 30.0
    },
    "plumbing": {
      "name": "Plumbing Seed",
      "type": "SEED",
      "rate_per_wl": 18.0
    },
    "biohazard_sign": {
      "name": "Biohazard Sign Seed",
      "type": "SEED",
      "rate_per_wl": 18.0
    },
    "sheet_music_sharp_piano": {
      "name": "Sheet Music: Sharp Piano Seed",
      "type": "SEED",
      "rate_per_wl": 12.0
    },
    "danger_sign": {
      "name": "Danger Sign Seed",
      "type": "SEED",
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
4. Buka tab **"📥 UPLOAD / PASTE JSON BAHAN"** -> paste JSON -> Klik **"TERAPKAN DATA JSON ⚡"**.
5. Sistem langsung menghitung modal beli SEED bahan vs harga jual Science Station BLOCK, dan menampilkan **PROFIT BERSIH CUAN MASSING** lu!
