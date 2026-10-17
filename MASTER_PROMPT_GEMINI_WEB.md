# 🚀 MASTER PROMPT: GEMINI PRO (WEB / ARGON HIGH EFFORT)
## TARGET: BUILD SURG-E MASSING TREE & RECURSIVE REVENUE ENGINE WEB APP

Salin dan tempel (copy-paste) seluruh teks di dalam blok berikut ke **Gemini Pro (Web) dengan mode Thinking / High Effort**:

```markdown
Role: Senior Principal Architect & Master Frontend Virtuoso.
Task: Buatkan SATU FILE LENGKAP production-ready `index.html` (HTML5 + CSS + JavaScript murni tanpa build tool, tanpa npm install, zero-dependency) untuk Web App: **"⚡ GROWTOPIA: SURG-E MASSING TREE & RECURSIVE REVENUE CHRONICLES • ANIME COMIC EDITION ⚡"**.

Karena kamu berjalan di web interface tanpa akses filesystem/terminal lokal, KODE HARUS 100% LENGKAP dalam SATU FILE `index.html` mandiri, siap dibuka langsung di browser dan siap di-deploy ke GitHub Pages atau Vercel. DILARANG menggunakan placeholder `// TODO: tambahkan di sini` atau memotong kode.

---

### 1. KONSEP & DESAIN SISTEM (SHONEN JUMP COMIC STYLE)
- Tampilan harus bergaya Anime Manga / Comic Book (seragam dengan portal universe Growtopia Massing Tree yang ada):
  - Kertas komik: `--manga-paper: #fffcf0;` dengan texture halftone dot `radial-gradient(circle, #2b2b36 1.2px, transparent 1.2px) 14px 14px`.
  - Tinta komik: `--manga-ink: #111116;`.
  - Border tebal komik: `3.5px solid #111116;` dan box shadow pekat komik: `4px 4px 0 #111116;` (atau `7px 7px 0 #111116;` untuk hero/card).
  - Aksen warna: Shonen Yellow (`#ffde00`), Shonen Red/Surg-E (`#ff1f4b`), Hospital Bed Cyan (`#00b4d8`), Puzzle Brick Purple (`#7209b7`), Profit Green (`#06d6a0`).
  - Font via Google Fonts CDN: `'Bangers'` (Judul/Header/Badge), `'Mochiy Pop One'` (Kanji SFX), `'Plus Jakarta Sans'` (Data & Tabel).
  - Top Manga Ticker Bar bergerak horizontal (marquee) menampilkan berita harga pasar Growtopia, tips massing, dan audio SFX trigger.

### 2. AUDIO SYNTHESIZER (ZERO ASSET / WEB AUDIO API)
Jangan gunakan link file audio eksternal (.mp3/.wav). Buat audio synthesizer bawaan menggunakan Web Audio API murni:
- `playTap()`: Sine wave 440Hz -> 880Hz (suara klik tombol).
- `playKaChing()`: Chord dua nada triangle wave 987Hz & 1318Hz (suara cuan/hitung profit).
- `playLimitBreak()`: Sawtooth sweep 150Hz -> 900Hz (suara aktivasi mode Harvester / FP).

### 3. ARSITEKTUR RESEP POHON (SPLICING TREE HIERARCHY)
Wajib tampilkan hierarki visual pohon splicing yang responsif dan interaktif:
- **TIER 0 (Puncak)**: **Surg-E Tree (Rarity 56)**
  - Hasil panen: Surg-E Block.
  - Splicing: Hospital Bed Seed + Puzzle Brick Seed.
- **TIER 1A (Cabang Kiri)**: **Hospital Bed (Rarity 31)**
  - Splicing: Bed Seed (Rarity 14) + Screen Door Seed (Rarity 17).
  - Block di-break kembali untuk menghasilkan Hospital Bed Seed.
- **TIER 1B (Cabang Kanan)**: **Puzzle Brick (Rarity 25)**
  - Splicing: Outie Block Seed (Rarity 20) + Evil Bricks Seed (Rarity 5).
  - Block di-break kembali untuk menghasilkan Puzzle Brick Seed.
- **TIER 2 (Bahan Dasar / Raw)**:
  - 4 Bahan Utama rasio 1:1:1:1: Bed Seed, Screen Door Seed, Outie Block Seed, Evil Bricks Seed.

### 4. ENGINE MATEMATIKA REKURSIF (UNTIL 0 REMAINDER)
Sediakan tombol toggle:
1. **"Perfectionist Mode (Recursive to 0)"** (Default & Unggulan)
2. **"Bot Discord Mode (Single-Pass 1x)"**

#### Parameter Panen (Harvest Drop Rates):
- **Hospital Bed (R31)**: Seed drop rate = 10% (0.10 seed/tree).
  - Yield Block: Normal = 2.50 | +Dreamcatcher Staff = 2.575 | +Harvester(FP) = 2.95 blocks/tree.
- **Puzzle Brick (R25)**: Seed drop rate = 11% (0.11 seed/tree).
  - Yield Block: Normal = 2.50 | +Dreamcatcher Staff = 2.575 | +Harvester(FP) = 2.95 blocks/tree.
- **Surg-E (R56)**: Seed drop rate = 5% (0.05 seed/tree).
  - Yield Block: Normal = 2.50 | +Dreamcatcher Staff = 2.575 | +Harvester(FP) = 2.95 blocks/tree.
- Pada mode rekursif, seluruh seed drop ditanam ulang batch demi batch hingga sisa seed = 0.
  Contoh: 6.000 H.Bed -> Batch 1 panen 600 seed -> Batch 2 tanam 600 panen 60 seed -> Batch 3 tanam 60 panen 6 seed -> Batch 4 tanam 6 panen 1 seed -> Batch 5 tanam 1 panen 0 seed = Total 6.667 pohon dipanen.

#### Parameter Break Balok (Ancestral Tesseract Lv. 1):
- Seed return: 25.0% per block.
- Extra block return: 13.33% per block.
- Pada mode rekursif, extra block return dipukul ulang di Pass 2, 3, 4... sampai sisa block = 0.
  Total pukulan balok = Initial Blocks / (1 - 0.1333) ≈ Initial Blocks × 1.1538.
  Total seed yang didapat = Total Pukulan × 0.25 ≈ Initial Blocks × 0.2885.
- Gems akumulasi: H.Bed ≈ 2.2965 Gems/block, P.Brick ≈ 1.2345 Gems/block, Surg-E harvest ≈ 4.148 Gems/tree.

### 5. KALKULATOR EKONOMI BENSIN (FUEL PACK / FP OPTIMIZER)
- Konsumsi Harvester: 2.700 Pohon ≈ 280 Fuel Pack (rasio ~9.6428 pohon per 1 FP).
- Input dinamis harga Fuel Pack (Default: 200 FP = 180 WL, setara 0.90 WL per FP).
- Perbandingan 3 Strategi FP secara live:
  1. *No FP*: 0 FP terpakai.
  2. *FP on Surg-E Only*: FP hanya dipakai panen pohon Surg-E (Sweet spot).
  3. *Full FP in All Steps (Recommended)*: FP dipakai di panen H.Bed, P.Brick, dan Surg-E (+23.85 DL net profit boost).
- Berikan kartu analisa rekomendasi otomatis berdasarkan input harga FP.

### 6. LEDGER KEUANGAN & AUDIT CUAN REAL-TIME
- Input Real-time harga pasar (dengan preset default):
  - Target Bibit Dasar: 6.000 (bisa diubah bebas, misal 1.000, 2.500, 10.000).
  - Bed Seed Rate: 2.0 / WL.
  - Screen Door Seed Rate: 4.0 / WL.
  - Outie Seed Rate: 2.0 / WL.
  - Evil Bricks Seed Rate: 10.0 / WL.
  - Surg-E Block Price: 1.0 WL per Block.
  - Fuel Pack Rate: 200 FP / 180 WL.
- Checkbox Kepemilikan Bahan:
  - [✓] "Sudah punya Screen Door Seed" (mengurangi pengeluaran cash 15 DL).
  - [ ] "Buat Outie Seed sendiri" (mengurangi belanja Outie 30 DL).
- Output Finansial Komprehensif:
  - **Modal Tunai yang Harus Disiapkan di Tas** (Cash Out of Pocket) dalam DL & WL.
  - **Total Valuasi Modal** (Sunk Cost).
  - **Gross Revenue Penjualan Surg-E**.
  - **Bonus Tambahan** (Valuasi ratusan ribu Gems + sisa seed).
  - **Net Profit Tunai** & **Net Profit Murni** dalam DL dan WL.
  - **ROI %**.
  - Tombol accordion "Lihat Audit Batch Rekursif" yang menampilkan tabel detail langkah demi langkah dari Batch 1 sampai sisa 0.

### 7. TEKNIS & STATE MANAGEMENT
- Simpan seluruh state (target pohon, harga, checkbox) ke `localStorage` agar tidak hilang saat refresh.
- Sediakan tombol "Reset Default Market Prices".
- Animasi tombol komik `:hover` dan `:active` (transform translate -2px / 2px dengan shadow tebal).
- Render seluruh dokumen dalam satu blok kode utuh: `<!DOCTYPE html> ... </html>`.
```
